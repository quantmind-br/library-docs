---
title: granite4_vision - vLLM
url: https://docs.vllm.ai/en/latest/api/vllm/model_executor/models/granite4_vision/
source: sitemap
fetched_at: 2026-05-07T21:30:36.815529009-03:00
rendered_js: false
word_count: 0
summary: This document defines the vLLM implementation of the Granite 4 Vision model, detailing its architecture, projector configurations, weight mapping, and LoRA support for multimodal processing.
tags:
    - vllm
    - granite-vision
    - multimodal
    - computer-vision
    - lora-adapter
    - model-architecture
category: reference
---

```
@MULTIMODAL_REGISTRY.register_processor(
    Granite4VisionMultiModalProcessor,
    info=Granite4VisionProcessingInfo,
    dummy_inputs=LlavaDummyInputsBuilder,
)
classGranite4VisionForConditionalGeneration(
    nn.Module, SupportsLoRA, SupportsMultiModal, SupportsPP
):
"""vLLM implementation of Granite 4 Vision.

    Architecture:
    - SigLIP vision tower -> WindowQFormerDownsampler projectors
    - Deepstack: 4 vision layers projected and injected at 4 LLM layers
    - Spatial: 4 offset groups from last vision layer injected at 4 more LLM layers
    - Granite language backbone with embedding_multiplier
    - logits_scaling via LogitsProcessor

    The outer model runs the LLM layer loop directly (like HF does) to inject
    deepstack features. This avoids wrapping the inner model and keeps weight
    loading simple.

    LoRA support:
    - Full merge: --hf-overrides '{"adapter_path": "path/to/lora"}' merges
      LM-only LoRA deltas at load time (W += scaling * B @ A).
    - Native LoRA: --enable-lora --default-mm-loras '{"image": "path/to/lora"}'
      lets vLLM runtime serve LM LoRA per-request.
    Both modes expect a LM-only adapter (no modules_to_save).
    """

    # LoRA class attributes (matches GraniteForCausalLM)
    packed_modules_mapping = {
        "qkv_proj": ["q_proj", "k_proj", "v_proj"],
        "gate_up_proj": ["gate_proj", "up_proj"],
    }
    embedding_modules = {}

    # Weight mapping: HF checkpoint -> vLLM parameter names
    # HF: model.language_model.layers.0...
    # vLLM: language_model.model.layers.0...
    # (because GraniteForCausalLM.model = GraniteModel)
    hf_to_vllm_mapper = WeightsMapper(
        orig_to_new_prefix={
            "model.language_model.": "language_model.model.",
            "model.layerwise_projectors.": "layerwise_projectors.",
            "model.spatial_projectors.": "spatial_projectors.",
            "model.image_newline": "image_newline",
            "model.vision_tower.": "vision_tower.",
            "lm_head.": "language_model.lm_head.",
        }
    )

    @classmethod
    defget_placeholder_str(cls, modality: str, i: int) -> str | None:
        if modality.startswith("image"):
            return "<image>"
        raise ValueError(f"Only image modality is supported, got {modality}")

    defget_mm_mapping(self) -> MultiModelKeys:
        return MultiModelKeys.from_string_field(
            language_model="language_model",
            connector=["layerwise_projectors", "spatial_projectors"],
            tower_model="vision_tower",
        )

    def__init__(self, *, vllm_config: VllmConfig, prefix: str = "") -> None:
        super().__init__()

        config = vllm_config.model_config.hf_config
        quant_config = vllm_config.quant_config
        self.config = config
        self.vllm_config = vllm_config

        # ----- Vision tower + projectors (marked as tower) -----
        with self._mark_tower_model(vllm_config, "image"):
            # Do NOT use init_vision_tower_for_llava here — it truncates the
            # encoder to vision_feature_layer depth. Deepstack needs ALL hidden
            # states (deepstack_layer_map uses negative indices into the full
            # encoder output list).
            self.vision_tower = SiglipVisionModel(
                config.vision_config,
                quant_config=quant_config,
                require_post_norm=False,
                prefix=maybe_prefix(prefix, "vision_tower"),
            )

            # image_newline parameter
            if config.use_image_newline_parameter:
                self.image_newline = nn.Parameter(
                    torch.empty(config.text_config.hidden_size)
                )
            else:
                self.image_newline = None

            cache_config = vllm_config.cache_config

            # Deepstack projectors: one per (vision_layer, llm_layer) pair
            self.layerwise_projectors = nn.ModuleList(
                [
                    WindowQFormerDownsampler(
                        config,
                        quant_config=quant_config,
                        cache_config=cache_config,
                        prefix=maybe_prefix(prefix, f"layerwise_projectors.{i}"),
                    )
                    for i in range(len(config.deepstack_layer_map))
                ]
            )

            # Spatial projectors: 4 offset groups
            self.spatial_projectors = None
            if config.use_spatial_sampling:
                self.spatial_projectors = nn.ModuleList(
                    [
                        WindowQFormerDownsampler(
                            config,
                            quant_config=quant_config,
                            cache_config=cache_config,
                            spatial_offset=i,
                            prefix=maybe_prefix(prefix, f"spatial_projectors.{i}"),
                        )
                        for i in range(4)
                    ]
                )

        # ----- Language model (marked as LM) -----
        with self._mark_language_model(vllm_config):
            self.language_model = Granite4VisionLLMForCausalLM(
                vllm_config=vllm_config.with_hf_config(config.text_config),
                prefix=maybe_prefix(prefix, "language_model"),
            )

        self.make_empty_intermediate_tensors = (
            self.language_model.make_empty_intermediate_tensors
        )

        # Store config values we need
        self._deepstack_layer_map = config.deepstack_layer_map  # [[-19, 9], ...]
        self._use_spatial_sampling = getattr(config, "use_spatial_sampling", False)
        self._spatial_vision_layer = getattr(config, "spatial_vision_layer", -1)
        self._spatial_target_layers = getattr(config, "spatial_target_layers", [])
        self._vision_feature_select_strategy = getattr(
            config, "vision_feature_select_strategy", "full"
        )
        self._downsample_rate = Fraction(config.downsample_rate)

        # Ordered list of LLM layer indices for each deepstack level.
        # Pre-populated from config so it's available during CUDA graph capture
        # (before any embed_multimodal call).
        self._ds_layer_indices: list[int] = [
            llm_layer for _, llm_layer in config.deepstack_layer_map
        ] + list(getattr(config, "spatial_target_layers", []))

        # Share ds_layer_indices with the LLM causal model so
        # make_empty_intermediate_tensors includes the correct keys
        # (its self.config is text_config, no deepstack_layer_map).
        self.language_model._ds_layer_indices = self._ds_layer_indices

        # Pre-allocated persistent GPU buffers for deepstack features.
        # Written via .copy_() in embed_input_ids(), read by forward() via a
        # slice. Because the buffer address is fixed, CUDA graph replay sees
        # the updated values written just before each prefill.
        # Shape: (max_num_batched_tokens, lm_hidden_size) per level.
        n_layerwise = len(config.deepstack_layer_map)
        n_spatial = len(getattr(config, "spatial_target_layers", []))
        num_ds_levels = n_layerwise + n_spatial
        lm_hidden = config.text_config.hidden_size
        max_tokens = vllm_config.scheduler_config.max_num_batched_tokens
        # Allocated on CPU first; moved to GPU in embed_input_ids on first use.
        self._ds_buffers: list[torch.Tensor] = [
            torch.zeros(max_tokens, lm_hidden) for _ in range(num_ds_levels)
        ]
        self._ds_num_tokens: int = 0  # tokens written in last embed_input_ids call

    # ----- Vision feature extraction -----

    def_get_vision_hidden_states(
        self, pixel_values: torch.Tensor
    ) -> list[torch.Tensor]:
"""Run vision tower and return all hidden states (including input embeddings).

        Uses SiglipEncoder's built-in return_all_hidden_states support.
        Returns list[Tensor] where index 0 = embeddings, index i = after layer i-1.
        """
        vt = self.vision_tower
        vm = vt.vision_model if hasattr(vt, "vision_model") else vt

        hidden_states = vm.embeddings(pixel_values)
        all_hidden_states = vm.encoder(
            inputs_embeds=hidden_states,
            return_all_hidden_states=True,
        )
        return all_hidden_states

    def_pack_and_unpad_image_features(
        self,
        image_features: list[torch.Tensor] | tuple[torch.Tensor, ...],
        image_sizes: torch.Tensor,
    ) -> list[torch.Tensor]:
"""Reshape, unpad, and pack image features.

        Matches HF Granite4VisionModel.pack_and_unpad_image_features exactly.
        """
        config = self.config
        ds_rate = self._downsample_rate
        new_image_features = []

        for image_idx, image_feature in enumerate(image_features):
            if image_feature.shape[0] > 1:
                # Multi-patch: first is base, rest are high-res
                base_image_feature = image_feature[0]
                image_feature = image_feature[1:]

                height = width = (
                    config.vision_config.image_size // config.vision_config.patch_size
                )
                # After QFormer downsampling
                height = int(height * ds_rate)
                width = int(width * ds_rate)

                num_patch_height, num_patch_width = get_anyres_image_grid_shape(
                    image_sizes[image_idx],
                    config.image_grid_pinpoints,
                    config.vision_config.image_size,
                )

                image_feature = image_feature.view(
                    num_patch_height, num_patch_width, height, width, -1
                )
                image_feature = (
                    image_feature.permute(4, 0, 2, 1, 3)
                    .contiguous()
                    .flatten(1, 2)
                    .flatten(2, 3)
                )
                image_feature = unpad_image(image_feature, image_sizes[image_idx])

                if self.image_newline is not None:
                    image_feature = torch.cat(
                        (
                            image_feature,
                            self.image_newline[:, None, None]
                            .expand(*image_feature.shape[:-1], 1)
                            .to(image_feature.device, image_feature.dtype),
                        ),
                        dim=-1,
                    )

                image_feature = image_feature.flatten(1, 2).transpose(0, 1)
                image_feature = torch.cat((base_image_feature, image_feature), dim=0)
            else:
                image_feature = image_feature[0]
                if self.image_newline is not None:
                    image_feature = torch.cat(
                        (image_feature, self.image_newline[None].to(image_feature)),
                        dim=0,
                    )

            new_image_features.append(image_feature)

        return new_image_features

    def_get_all_layer_features(
        self,
        pixel_values: torch.Tensor,
        image_sizes: torch.Tensor,
    ) -> tuple[list[int], list[torch.Tensor]]:
"""Extract deepstack + spatial features for all levels.

        Returns:
          llm_layer_indices: ordered list of target LLM layer indices
          per_image_packed:  one tensor per image, shape
                             (num_tokens_i, lm_hidden_size * num_levels),
                             all levels packed on dim=-1.

        Packing on dim=-1 means the framework's token-level slicing for
        chunked prefill preserves all levels intact.
        """
        select_strategy = self._vision_feature_select_strategy

        image_num_patches = [
            image_size_to_num_patches(
                image_size=imsize,
                grid_pinpoints=self.config.image_grid_pinpoints,
                patch_size=self.config.vision_config.image_size,
            )
            for imsize in image_sizes
        ]

        if pixel_values.dim() == 5:
            pixel_values = torch.cat(
                [pv[:np_] for pv, np_ in zip(pixel_values, image_num_patches)],
                dim=0,
            )

        all_hidden_states = self._get_vision_hidden_states(pixel_values)

        # Collect per-level: (llm_layer, [per_image_tensor, ...])
        levels: list[tuple[int, list[torch.Tensor]]] = []

        for proj_idx, (vision_layer, llm_layer) in enumerate(self._deepstack_layer_map):
            selected = all_hidden_states[vision_layer]
            if select_strategy == "default":
                selected = selected[:, 1:]
            projected = self.layerwise_projectors[proj_idx](selected)
            per_image = self._pack_and_unpad_image_features(
                torch.split(projected, image_num_patches, dim=0), image_sizes
            )
            levels.append((llm_layer, per_image))

        if self._use_spatial_sampling and self.spatial_projectors is not None:
            spatial_hidden = all_hidden_states[self._spatial_vision_layer]
            if select_strategy == "default":
                spatial_hidden = spatial_hidden[:, 1:]
            for group_idx, llm_layer in enumerate(self._spatial_target_layers):
                projected = self.spatial_projectors[group_idx](spatial_hidden)
                per_image = self._pack_and_unpad_image_features(
                    torch.split(projected, image_num_patches, dim=0), image_sizes
                )
                levels.append((llm_layer, per_image))

        llm_layer_indices = [llm_layer for llm_layer, _ in levels]
        num_images = len(image_sizes)
        per_image_packed = [
            torch.cat([levels[lvl][1][img] for lvl in range(len(levels))], dim=-1)
            for img in range(num_images)
        ]

        return llm_layer_indices, per_image_packed

    # ----- Multimodal interface -----

    def_parse_and_validate_image_input(
        self, **kwargs: object
    ) -> LlavaNextImageInputs | None:
        pixel_values = kwargs.pop("pixel_values", None)
        image_sizes = kwargs.pop("image_sizes", None)
        image_embeds = kwargs.pop("image_embeds", None)

        if pixel_values is None and image_embeds is None:
            return None

        if pixel_values is not None:
            expected_h = expected_w = self.config.vision_config.image_size
            return LlavaNextImagePixelInputs(
                type="pixel_values",
                pixel_values=pixel_values,
                image_sizes=image_sizes,
                resolve_bindings={"h": expected_h, "w": expected_w},
            )

        if image_embeds is not None:
            return LlavaNextImageEmbeddingInputs(
                type="image_embeds",
                data=image_embeds,
            )

        raise AssertionError("Unreachable")

    defembed_multimodal(self, **kwargs: object) -> MultiModalEmbeddings:
"""Run vision tower and return per-image packed feature tensors.

        Each returned tensor has shape (num_tokens_i, lm_hidden_size * num_levels)
        with all deepstack levels packed on dim=-1. The framework caches these
        tensors and slices along dim=0 for chunked prefill — all levels survive
        intact because slicing is token-wise, not feature-wise.

        embed_input_ids() splits the packed tensor back into per-level buffers.
        """
        image_input = self._parse_and_validate_image_input(**kwargs)
        if image_input is None:
            return []

        if image_input["type"] == "image_embeds":
            return [image_input["data"]]

        pixel_values = image_input["pixel_values"]
        image_sizes = image_input.get("image_sizes")

        if isinstance(pixel_values, list):
            pixel_values = torch.cat(pixel_values, dim=0)

        llm_layer_indices, per_image_packed = self._get_all_layer_features(
            pixel_values, image_sizes
        )
        self._ds_layer_indices = llm_layer_indices
        return per_image_packed

    defembed_input_ids(
        self,
        input_ids: torch.Tensor,
        multimodal_embeddings: MultiModalEmbeddings | None = None,
        *,
        is_multimodal: torch.Tensor | None = None,
        handle_oov_mm_token: bool = True,
    ) -> torch.Tensor:
"""Merge text and vision embeddings, apply embedding_multiplier.

        HF flow:
        1. inputs_embeds = embed_tokens(input_ids)
        2. inputs_embeds.masked_fill(vision_mask, 0.0)
        3. hidden_states = inputs_embeds * embedding_multiplier
        4. layer loop injects deepstack features at target layers

        multimodal_embeddings contains packed tensors from embed_multimodal():
        shape (num_tokens_i, lm_hidden_size * num_levels). We split on dim=-1
        to get per-level features, build batch-sized buffers (zero at text
        positions), and store in self._ds_features for forward().
        """
        lm_inner = self.language_model.model

        has_vision = (
            multimodal_embeddings is not None
            and is_multimodal is not None
            and len(multimodal_embeddings) > 0
            and is_multimodal.any()
        )

        if not has_vision:
            self._ds_num_tokens = 0
            embeds = lm_inner.embed_input_ids(input_ids)
            return embeds * lm_inner.config.embedding_multiplier

        # 1. Text embeddings
        text_embeds = lm_inner.embed_input_ids(input_ids)

        # 2. Zero image positions (matches HF masked_fill(vision_mask, 0.0))
        text_embeds[is_multimodal] = 0.0

        # 3. Apply embedding_multiplier
        inputs_embeds = text_embeds * lm_inner.config.embedding_multiplier

        # 4. Split packed tensors into per-level features and build buffers.
        #    multimodal_embeddings is a list of per-image packed tensors
        #    (possibly a chunk slice from the framework's encoder cache).
        #    Concatenate along token dim → (total_mm_tokens, lm_h * num_levels).
        N, lm_h = inputs_embeds.shape
        all_packed = torch.cat(
            [t.to(dtype=inputs_embeds.dtype) for t in multimodal_embeddings],
            dim=0,
        )
        level_features = all_packed.split(lm_h, dim=-1)  # num_levels tensors

        # Ensure persistent buffers are on the right device/dtype (first call).
        buf0 = self._ds_buffers[0]
        if buf0.device != inputs_embeds.device or buf0.dtype != inputs_embeds.dtype:
            self._ds_buffers = [
                b.to(device=inputs_embeds.device, dtype=inputs_embeds.dtype)
                for b in self._ds_buffers
            ]

        for level_idx in range(len(self._ds_layer_indices)):
            target = self._ds_buffers[level_idx][:N]
            target.zero_()
            target[is_multimodal] = level_features[level_idx]

        self._ds_num_tokens = N
        return inputs_embeds

    # ----- Forward -----

    defforward(
        self,
        input_ids: torch.Tensor,
        positions: torch.Tensor,
        intermediate_tensors: IntermediateTensors | None = None,
        inputs_embeds: torch.Tensor | None = None,
        **kwargs: object,
    ) -> torch.Tensor | IntermediateTensors:
        if intermediate_tensors is not None:
            inputs_embeds = None

        # Build IntermediateTensors from pre-allocated persistent buffers.
        # Always pass deepstack when inputs_embeds is non-None (prefill path),
        # including during CUDA graph capture (buffers are zero → no-op injection).
        # This ensures the graph captures the injection code path.
        if (
            inputs_embeds is not None
            and get_pp_group().is_first_rank
            and self._ds_layer_indices
        ):
            n = inputs_embeds.size(0)
            ds: IntermediateTensors | None = IntermediateTensors(
                {
                    f"ds_{llm_layer}": self._ds_buffers[lvl][:n]
                    for lvl, llm_layer in enumerate(self._ds_layer_indices)
                }
            )
        else:
            ds = None

        hidden_states = self.language_model.model(
            input_ids=input_ids,
            positions=positions,
            intermediate_tensors=intermediate_tensors,
            inputs_embeds=inputs_embeds,
            deepstack_input_embeds=ds,
        )

        # Clear buffers after use so stale features don't leak into the next request.
        if (
            inputs_embeds is not None
            and get_pp_group().is_first_rank
            and self._ds_num_tokens > 0
        ):
            n = self._ds_num_tokens
            for buf in self._ds_buffers:
                buf[:n].zero_()
            self._ds_num_tokens = 0

        return hidden_states

    defcompute_logits(
        self,
        hidden_states: torch.Tensor,
    ) -> torch.Tensor | None:
        # GraniteForCausalLM.compute_logits uses
        # LogitsProcessor(scale=1/logits_scaling)
        return self.language_model.compute_logits(hidden_states)

    defload_weights(self, weights: Iterable[tuple[str, torch.Tensor]]) -> set[str]:
        loader = AutoWeightsLoader(self)
        return loader.load_weights(weights, mapper=self.hf_to_vllm_mapper)
```