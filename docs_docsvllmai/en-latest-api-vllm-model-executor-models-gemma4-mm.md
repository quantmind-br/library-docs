---
title: gemma4_mm - vLLM
url: https://docs.vllm.ai/en/latest/api/vllm/model_executor/models/gemma4_mm/
source: sitemap
fetched_at: 2026-05-07T21:30:17.042414396-03:00
rendered_js: false
word_count: 0
summary: This document defines the Gemma4ForConditionalGeneration class, implementing a multimodal architecture within the vLLM framework that integrates vision, audio, and language processing modules.
tags:
    - gemma4
    - multimodal
    - vllm
    - model-architecture
    - deep-learning
    - pytorch
category: api
---

```
@MULTIMODAL_REGISTRY.register_processor(
    Gemma4MultiModalProcessor,
    info=Gemma4ProcessingInfo,
    dummy_inputs=Gemma4DummyInputsBuilder,
)
classGemma4ForConditionalGeneration(
    nn.Module,
    SupportsMultiModal,
    SupportsPP,
    SupportsLoRA,
    SupportsEagle3,
):
    packed_modules_mapping = {
        "qkv_proj": [
            "q_proj",
            "k_proj",
            "v_proj",
        ],
        "gate_up_proj": [
            "gate_proj",
            "up_proj",
        ],
    }

    # Maps checkpoint prefixes to vLLM module paths.
    hf_to_vllm_mapper = WeightsMapper(
        orig_to_new_prefix={
            "model.embed_audio.": "embed_audio.",
            "model.embed_vision.": "embed_vision.",
            "model.language_model.": "language_model.model.",
            "model.vision_tower.": "vision_tower.",
            "model.audio_tower.": "audio_tower.",
            "lm_head.": "language_model.lm_head.",
            "model": "language_model.model",
        }
    )

    def__init__(self, *, vllm_config: VllmConfig, prefix: str = ""):
        super().__init__()
        config = vllm_config.model_config.hf_config
        quant_config = vllm_config.quant_config
        multimodal_config = vllm_config.model_config.multimodal_config
        self.config = config
        self.quant_config = quant_config
        self.multimodal_config = multimodal_config

        # ---- Vision tower (shared by image and video) ----
        with self._mark_tower_model(vllm_config, {"image", "video"}):
            self.vision_tower = AutoModel.from_config(config=config.vision_config)
            self.embed_vision = Gemma4MultimodalEmbedder(
                config.vision_config, config.text_config
            )

        # ---- Audio tower (variants with audio_config) ----
        if config.audio_config is not None:
            with self._mark_tower_model(vllm_config, "audio"):
                self.audio_tower = AutoModel.from_config(config=config.audio_config)
                # AutoModel.from_config does NOT call post_init(),
                # which is needed to initialize buffers that are absent
                # from the checkpoint (e.g. inv_timescales for relative
                # position embeddings, softcap, gradient_clipping).
                self.audio_tower.post_init()
                self.embed_audio = Gemma4MultimodalEmbedder(
                    config.audio_config, config.text_config
                )
        else:
            self.audio_tower = None
            self.embed_audio = None

        # ---- Language model (vLLM optimised) ----
        with self._mark_language_model(vllm_config):
            self.language_model: Gemma4ForCausalLM = init_vllm_registered_model(
                vllm_config=vllm_config,
                hf_config=config.text_config,
                prefix=maybe_prefix(prefix, "language_model"),
                architectures=["Gemma4ForCausalLM"],
            )

            # Pre-allocate PLE buffer for CUDA graph compatibility.
            # Some variants have hidden_size_per_layer_input=None (no PLE).
            ple_dim = config.text_config.hidden_size_per_layer_input
            if ple_dim is not None:
                self.per_layer_embeddings = torch.zeros(
                    vllm_config.scheduler_config.max_num_batched_tokens,
                    config.text_config.num_hidden_layers,
                    ple_dim,
                    device=(self.language_model.model.embed_tokens.weight.device),
                    dtype=(self.language_model.model.embed_tokens.weight.dtype),
                )
            else:
                self.per_layer_embeddings = None

        self.make_empty_intermediate_tensors = (
            self.language_model.make_empty_intermediate_tensors
        )

        # --- Precompute full-attention layer indices for bidi clearing ---
        self._full_attn_layer_idxs: frozenset[int] = frozenset()
        text_config = config.text_config
        if getattr(text_config, "use_bidirectional_attention", None) == "vision":
            layer_types = getattr(text_config, "layer_types", None)
            if layer_types:
                self._full_attn_layer_idxs = frozenset(
                    i for i, lt in enumerate(layer_types) if lt != "sliding_attention"
                )

        # --- MixtureOfExperts delegation to language_model ---
        self.expert_weights = self.language_model.expert_weights
        self.moe_layers = self.language_model.moe_layers
        self.num_moe_layers = self.language_model.num_moe_layers
        self.num_logical_experts = self.language_model.num_logical_experts
        self.num_physical_experts = self.language_model.num_physical_experts
        self.num_local_physical_experts = self.language_model.num_local_physical_experts
        self.num_routed_experts = self.language_model.num_routed_experts
        self.num_expert_groups = self.language_model.num_expert_groups
        self.num_shared_experts = self.language_model.num_shared_experts
        self.num_redundant_experts = self.language_model.num_redundant_experts

    # ------------------------------------------------------------------ #
    # Input parsing
    # ------------------------------------------------------------------ #

    def_parse_and_validate_image_input(
        self, **kwargs: object
    ) -> Gemma4ImageInputs | None:
        pixel_values = kwargs.pop("pixel_values", None)
        pixel_position_ids = kwargs.pop("pixel_position_ids", None)
        image_embeds = kwargs.pop("image_embeds", None)
        assert image_embeds is None, "Gemma4 does not support image_embeds."
        if pixel_values is None:
            return None
        return Gemma4ImagePixelInputs(
            pixel_values=pixel_values,
            pixel_position_ids=pixel_position_ids,
        )

    def_parse_and_validate_audio_input(
        self, **kwargs: object
    ) -> Gemma4AudioInputs | None:
        input_features_padded = kwargs.pop("input_features_padded", None)
        if input_features_padded is None:
            return None
        input_features_mask = kwargs.pop("input_features_mask", None)
        if input_features_mask is None:
            return None
        return Gemma4AudioInputs(
            input_features_padded=input_features_padded,
            input_features_mask=input_features_mask,
        )

    def_parse_and_validate_video_input(
        self, **kwargs: object
    ) -> dict[str, torch.Tensor] | None:
        pixel_values_videos = kwargs.pop("pixel_values_videos", None)
        pixel_position_ids_videos = kwargs.pop("pixel_position_ids_videos", None)
        video_frame_counts = kwargs.pop("video_frame_counts", None)
        if pixel_values_videos is None:
            return None
        return {
            "pixel_values_videos": pixel_values_videos,
            "pixel_position_ids_videos": pixel_position_ids_videos,
            "video_frame_counts": video_frame_counts,
        }

    def_parse_and_validate_multimodal_inputs(
        self, **kwargs: object
    ) -> dict[str, Gemma4ImageInputs | Gemma4AudioInputs | Gemma4VideoInputs | None]:
        mm_input_by_modality = {}
        for input_key in list(kwargs):
            if (
                input_key in ("pixel_values", "image_embeds")
                and "image" not in mm_input_by_modality
            ):
                mm_input_by_modality["image"] = self._parse_and_validate_image_input(
                    **kwargs
                )
            if (
                input_key == "pixel_values_videos"
                and "video" not in mm_input_by_modality
            ):
                mm_input_by_modality["video"] = self._parse_and_validate_video_input(
                    **kwargs
                )
            if (
                input_key == "input_features_padded"
                and "audio" not in mm_input_by_modality
            ):
                mm_input_by_modality["audio"] = self._parse_and_validate_audio_input(
                    **kwargs
                )
        return mm_input_by_modality

    # ------------------------------------------------------------------ #
    # Image processing
    # ------------------------------------------------------------------ #

    def_process_image_input(
        self,
        image_input: Gemma4ImageInputs,
    ) -> list[torch.Tensor]:
        pixel_values = image_input["pixel_values"]
        pixel_position_ids = image_input["pixel_position_ids"]

        # The HF image processor now outputs pre-patchified data:
        #   pixel_values:       (num_images, max_patches, patch_pixels)
        #   pixel_position_ids: (num_images, max_patches, 2)
        # We call the vision tower's forward() directly, which handles
        # patch embedding, encoding, pooling, padding removal, and
        # optional standardization internally.
        vt = self.vision_tower
        pooling_k2 = self.config.vision_config.pooling_kernel_size**2

        # TODO: Move this per-image loop into the input processor to
        # reduce dynamism at the model runner / engine core. This
        # requires spatially padding all images to uniform (H_max,
        # W_max) in _call_hf_processor() so they arrive as a single
        # stacked tensor, tracking padded regions via image_sizes
        # metadata, and validating numerical equivalence with the
        # current per-image path.
        #
        # Process each image individually through the vision tower.
        # The vision tower's forward() strips padding and returns a
        # flat tensor of valid tokens. We process per-image to get
        # variable-length outputs matching the dynamic token count
        # from get_image_repl.
        per_image_features = []
        for i in range(pixel_values.shape[0]):
            pv = pixel_values[i].unsqueeze(0)  # (1, max_patches, patch_pixels)
            pp = pixel_position_ids[i].unsqueeze(0)  # (1, max_patches, 2)

            # Derive the pooler's output_length from the total patch
            # count (including padding).  The vision tower encoder
            # processes ALL patches — padding patches get zero hidden
            # states but still occupy sequence positions.  The pooler's
            # _avg_pool_by_positions requires:
            #     input_seq_len / output_length == k²
            # where k == pooling_kernel_size.  The image processor
            # allocates max_patches = max_soft_tokens * k² total slots,
            # so output_length = max_patches / k² == max_soft_tokens.
            # Without this, the pooler falls back to
            # config.image_seq_length (e.g. 280), which fails when a
            # different max_soft_tokens was used at preprocessing time.
            max_patches = pv.shape[1]
            output_length = max_patches // pooling_k2

            vt_output = vt(pv, pp, output_length=output_length)
            # last_hidden_state: (num_valid_tokens, hidden_size)
            # — already flat with padding stripped by the vision tower
            per_image_features.append(vt_output.last_hidden_state)

        # Project each image's features into LM embedding space.
        # Per-image loop is required because images have variable
        # token counts after padding removal.
        # Cast to match the projection layer's dtype (model may be
        # bf16 while the vision tower outputs fp32).
        target_dtype = self.embed_vision.embedding_projection.weight.dtype
        return [
            self.embed_vision(inputs_embeds=img.unsqueeze(0).to(target_dtype)).squeeze(
                0
            )
            for img in per_image_features
        ]

    # ------------------------------------------------------------------ #
    # Video processing (frames through vision tower)
    # ------------------------------------------------------------------ #

    def_process_video_input(
        self,
        video_input: dict[str, torch.Tensor],
    ) -> list[torch.Tensor]:
"""Process video frames through the vision tower.

        Reuses the image processing pipeline — Gemma4 has no separate
        video tower; video frames are just images at lower resolution
        (max_soft_tokens=70).

        Returns one concatenated embedding tensor per video (not per
        frame), because vLLM treats one video as one multimodal item.
        The flat_from_sizes field config groups all frames of a video
        together, so embed_multimodal must return one tensor per video.
        """
        pixel_values = video_input["pixel_values_videos"]
        pixel_position_ids = video_input["pixel_position_ids_videos"]
        frame_counts = video_input["video_frame_counts"]

        vt = self.vision_tower
        pooling_k2 = self.config.vision_config.pooling_kernel_size**2
        target_dtype = self.embed_vision.embedding_projection.weight.dtype

        # Split flat tensors into per-video chunks
        if isinstance(frame_counts, torch.Tensor):
            fc_list = frame_counts.tolist()
        else:
            fc_list = list(frame_counts)

        pv_per_video = torch.split(pixel_values, fc_list, dim=0)
        pp_per_video = torch.split(pixel_position_ids, fc_list, dim=0)

        per_video_embeddings = []
        for pv_chunk, pp_chunk in zip(pv_per_video, pp_per_video):
            frame_embs = []
            for i in range(pv_chunk.shape[0]):
                pv = pv_chunk[i].unsqueeze(0)
                pp = pp_chunk[i].unsqueeze(0)

                max_patches = pv.shape[1]
                output_length = max_patches // pooling_k2

                vt_output = vt(pv, pp, output_length=output_length)
                frame_emb = self.embed_vision(
                    inputs_embeds=(
                        vt_output.last_hidden_state.unsqueeze(0).to(target_dtype)
                    )
                ).squeeze(0)
                frame_embs.append(frame_emb)

            # Concatenate all frames of this video into one tensor.
            per_video_embeddings.append(torch.cat(frame_embs, dim=0))

        return per_video_embeddings

    # ------------------------------------------------------------------ #
    # Audio processing
    # ------------------------------------------------------------------ #

    def_process_audio_input(
        self,
        audio_input: Gemma4AudioInputs,
    ) -> list[torch.Tensor]:
        input_features = audio_input["input_features_padded"].squeeze(1)
        input_features_mask = audio_input["input_features_mask"].squeeze(1)

        # Run audio tower — mask uses standard HF convention
        # (True=valid, False=padding).
        audio_outputs = self.audio_tower(input_features, input_features_mask)
        if isinstance(audio_outputs, tuple):
            audio_encodings, audio_mask = audio_outputs
        else:
            audio_encodings = audio_outputs.last_hidden_state
            audio_mask = audio_outputs.attention_mask

        # Project into LM embedding space.
        audio_features = self.embed_audio(inputs_embeds=audio_encodings)

        # Strip padding per-batch element: only keep real (non-padding)
        # tokens. audio_mask is True for valid positions (HF convention).
        per_audio = []
        for enc, mask in zip(audio_features, audio_mask, strict=True):
            per_audio.append(enc[mask])  # [num_real, hidden_size]

        return per_audio

    # ------------------------------------------------------------------ #
    # MultiModalEmbeddings interface
    # ------------------------------------------------------------------ #

    defembed_multimodal(self, **kwargs: object) -> MultiModalEmbeddings:
        mm_input_by_modality = self._parse_and_validate_multimodal_inputs(**kwargs)
        multimodal_embeddings: list[torch.Tensor] = []

        for modality, multimodal_input in mm_input_by_modality.items():
            if multimodal_input is None:
                continue
            if modality == "image":
                multimodal_embeddings.extend(
                    self._process_image_input(multimodal_input)
                )
            elif modality == "video":
                multimodal_embeddings.extend(
                    self._process_video_input(multimodal_input)
                )
            elif modality == "audio":
                multimodal_embeddings.extend(
                    self._process_audio_input(multimodal_input)
                )

        return multimodal_embeddings

    defembed_input_ids(
        self,
        input_ids: torch.Tensor,
        multimodal_embeddings: MultiModalEmbeddings | None = None,
        *,
        is_multimodal: torch.Tensor | None = None,
    ) -> torch.Tensor:
        # Cache per-layer embeddings (PLE) for the language model's
        # forward pass.  During profiling embed_input_ids is not called,
        # so the pre-allocated zeros are used instead.
        if self.per_layer_embeddings is not None:
            # Mask multimodal tokens (image/audio) to 0 for PLE
            # computation (using token_type_ids == 0 as text_mask).
            # Replicate this: map image token positions to token 0.
            if is_multimodal is not None:
                ple_input_ids = torch.where(
                    is_multimodal.to(input_ids.device, non_blocking=True),
                    torch.zeros_like(input_ids),
                    input_ids,
                )
            else:
                ple_input_ids = input_ids

            per_layer_inputs = self.language_model.model.get_per_layer_inputs(
                ple_input_ids
            )
            if per_layer_inputs is not None:
                per_layer_inputs = per_layer_inputs.reshape(
                    -1,
                    self.config.text_config.num_hidden_layers,
                    self.config.text_config.hidden_size_per_layer_input,
                )
                self.per_layer_embeddings[: per_layer_inputs.shape[0]].copy_(
                    per_layer_inputs
                )

        if multimodal_embeddings is None or is_multimodal is None:
            return super().embed_input_ids(input_ids)

        return super().embed_input_ids(
            input_ids,
            multimodal_embeddings=multimodal_embeddings,
            is_multimodal=is_multimodal,
        )

    # ------------------------------------------------------------------ #
    # Forward
    # ------------------------------------------------------------------ #

    defforward(
        self,
        input_ids: torch.Tensor,
        positions: torch.Tensor,
        intermediate_tensors: IntermediateTensors | None = None,
        inputs_embeds: torch.Tensor | None = None,
        **kwargs: object,
    ) -> IntermediateTensors:
        if intermediate_tensors is not None:
            inputs_embeds = None

        # Select the pre-cached PLEs for this batch (None when PLE
        # is disabled for variants without PLE).
        per_layer_inputs = (
            self.per_layer_embeddings[: inputs_embeds.shape[0]]
            if self.per_layer_embeddings is not None and inputs_embeds is not None
            else None
        )

        # Gemma4 bidi: clear mm_prefix_range for full_attention layers.
        # Must run here (outside @support_torch_compile boundary) because
        # _run_decoder_layers is inside a compiled graph where Python
        # side effects are eliminated.
        self._clear_mm_prefix_for_full_attn_layers()

        hidden_states = self.language_model.model(
            input_ids,
            positions,
            per_layer_inputs=per_layer_inputs,
            intermediate_tensors=intermediate_tensors,
            inputs_embeds=inputs_embeds,
            **kwargs,
        )

        return hidden_states

    defcompute_logits(
        self,
        hidden_states: torch.Tensor,
    ) -> torch.Tensor | None:
        return self.language_model.compute_logits(hidden_states)

    # ------------------------------------------------------------------ #
    # Bidirectional attention helpers
    # ------------------------------------------------------------------ #

    def_clear_mm_prefix_for_full_attn_layers(self) -> None:
"""Clear mm_prefix_range for non-sliding layers.

        Gemma4 with use_bidirectional_attention='vision' applies
        bidirectional attention only to sliding_attention layers.
        Full attention layers use plain causal masking.

        Uses _full_attn_layer_idxs (precomputed in __init__) for O(1)
        lookup instead of per-call regex parsing.
        """
        if not self._full_attn_layer_idxs:
            return

        fromvllm.forward_contextimport get_forward_context

        attn_metadata = get_forward_context().attn_metadata
        if attn_metadata is None:
            return

        def_process(metadata_dict: dict) -> None:
            for layer_name, metadata in metadata_dict.items():
                if ".layers." not in layer_name:
                    continue
                try:
                    layer_idx = int(layer_name.split(".layers.")[1].split(".")[0])
                except (ValueError, IndexError):
                    continue
                if layer_idx in self._full_attn_layer_idxs:
                    if hasattr(metadata, "mm_prefix_range"):
                        metadata.mm_prefix_range = None
                    if hasattr(metadata, "mm_prefix_range_tensor"):
                        metadata.mm_prefix_range_tensor = None

        if isinstance(attn_metadata, list):
            for ub_metadata in attn_metadata:
                _process(ub_metadata)
        elif isinstance(attn_metadata, dict):
            _process(attn_metadata)

    # ------------------------------------------------------------------ #
    # Weight loading
    # ------------------------------------------------------------------ #

    defload_weights(self, weights: Iterable[tuple[str, torch.Tensor]]) -> set[str]:
        # Some checkpoints have vestigial embed_vision.embedding and
        # embed_audio.embedding weights from the Gemma3n architecture
        # that are not used by Gemma4's MultimodalEmbedder (which only
        # has embedding_projection + embedding_post_projection_norm).
        ignore_prefixes = [
            "embed_vision.embedding.",
            "embed_audio.embedding.",
        ]
        # Models without audio tower should skip
        # audio weights entirely.
        if self.audio_tower is None:
            ignore_prefixes.extend(
                [
                    "audio_tower.",
                    "embed_audio.",
                ]
            )
        loader = AutoWeightsLoader(
            self,
            ignore_unexpected_prefixes=ignore_prefixes,
        )
        return loader.load_weights(weights, mapper=self.hf_to_vllm_mapper)

    # ------------------------------------------------------------------ #
    # LoRA / multimodal mapping
    # ------------------------------------------------------------------ #

    defget_mm_mapping(self) -> MultiModelKeys:
"""Get the module prefix mapping for multimodal models."""
        connectors = ["embed_vision"]
        tower_models = ["vision_tower"]
        if self.audio_tower is not None:
            connectors.append("embed_audio")
            tower_models.append("audio_tower")

        return MultiModelKeys.from_string_field(
            language_model="language_model",
            connector=connectors,
            tower_model=tower_models,
        )

    @classmethod
    defget_placeholder_str(cls, modality: str, i: int) -> str | None:
        if modality == "image":
            return "<image_soft_token>"
        if modality == "audio":
            return "<audio_soft_token>"
        if modality == "video":
            return "<|video|>"
        raise ValueError(f"Unsupported modality: {modality}")
```