---
title: isaac - vLLM
url: https://docs.vllm.ai/en/latest/api/vllm/model_executor/models/isaac/
source: sitemap
fetched_at: 2026-05-07T21:31:03.987608417-03:00
rendered_js: false
word_count: 0
summary: This document defines the model architecture and integration logic for the Isaac multimodal transformer within the vLLM framework, including support for image processing and Multi-dimensional Rotary Positional Embeddings (MRoPE).
tags:
    - multimodal-models
    - vllm
    - mrope
    - pytorch-nn
    - computer-vision
    - model-architecture
category: api
---

```
@MULTIMODAL_REGISTRY.register_processor(
    IsaacMultiModalProcessor,
    info=IsaacProcessingInfo,
    dummy_inputs=IsaacDummyInputsBuilder,
)
classIsaacForConditionalGeneration(
    nn.Module, SupportsMultiModal, SupportsLoRA, SupportsPP, SupportsMRoPE
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

    supports_encoder_tp_data = True

    # To ensure correct weight loading and mapping.
    hf_to_vllm_mapper = WeightsMapper(
        orig_to_new_prefix={
            "lm_head.": "language_model.lm_head.",
            "model.text_model.lm_head.": "language_model.lm_head.",
            "model.text_model.": "language_model.model.",
            "model.vision_embedding.0": "vision_embedding.transformer",
            "model.vision_embedding.1": "vision_embedding.linear_fc1",
            "model.vision_embedding.2": "vision_embedding.act",
            "model.vision_embedding.3": "vision_embedding.linear_fc2",
            "model.vision_embedding.": "vision_embedding.",
            "model.lm_head.": "language_model.lm_head.",
            "model.": "language_model.model.",
        }
    )

    @classmethod
    defget_placeholder_str(cls, modality: str, i: int) -> str | None:
        if modality.startswith("image"):
            return "<image>"

        raise ValueError("Only image modality is supported")

    def__init__(self, *, vllm_config: VllmConfig, prefix: str = "model"):
        super().__init__()
        config: IsaacConfig = vllm_config.model_config.hf_config
        quant_config = vllm_config.quant_config
        self.config = config

        head_dim = config.head_dim
        calculated_mrope_section = [
            head_dim // 4,  # 2x more for temporal dim
            head_dim // 8,
            head_dim // 8,
        ]

        self.vision_token_id = _resolve_vision_token_id(
            vllm_config.model_config, config.vision_token
        )
        config.image_token_id = self.vision_token_id

        text_cfg = getattr(config, "text_config", None)
        target_cfg = (
            text_cfg
            if text_cfg is not None and not isinstance(text_cfg, dict)
            else config
        )

        rope_scaling = getattr(target_cfg, "rope_scaling", None)
        if rope_scaling is None and target_cfg is config:
            rope_scaling = getattr(config, "_rope_scaling", None)

        patch_rope_parameters(target_cfg)
        rope_parameters = target_cfg.rope_parameters
        rope_parameters["mrope_section"] = calculated_mrope_section
        if rope_scaling is not None and "mrope_interleaved" in rope_scaling:
            rope_parameters.setdefault(
                "mrope_interleaved", rope_scaling["mrope_interleaved"]
            )
        target_cfg.rope_parameters = rope_parameters

        with self._mark_language_model(vllm_config):
            self.language_model = init_vllm_registered_model(
                vllm_config=vllm_config,
                architectures=["Qwen3ForCausalLM"],
                prefix=maybe_prefix(prefix, "language_model"),
            )

        self.make_empty_intermediate_tensors = (
            self.language_model.make_empty_intermediate_tensors
        )

        vision_cfg = config.vision_config
        if vision_cfg is None:
            raise ValueError("IsaacConfig should always have vision_config")
        attn_impl = (
            config.vision_attn_implementation
            if config.vision_attn_implementation is not None
            else getattr(config, "_attn_implementation", None)
        )
        if attn_impl is not None:
            vision_cfg._attn_implementation = attn_impl

        hidden_dim = vision_cfg.hidden_size * (vision_cfg.pixel_shuffle_scale_factor**2)

        with self._mark_tower_model(vllm_config, "image"):
            self.vision_embedding = IsaacVisionEmbedding(
                vision_cfg=vision_cfg,
                hidden_dim=hidden_dim,
                output_dim=config.hidden_size,
                quant_config=quant_config,
                prefix=maybe_prefix(prefix, "vision_embedding"),
            )

    defiter_mm_grid_hw(
        self, input_tokens: list[int], mm_features: list[MultiModalFeatureSpec]
    ) -> Iterator[tuple[int, int, int]]:
        spatial_merge_size = self.config.vision_config.pixel_shuffle_scale_factor
        for mm_feature in sorted(mm_features, key=lambda f: f.mm_position.offset):
            offset = mm_feature.mm_position.offset
            if mm_feature.modality == "image":
                t, h, w = mm_feature.data["image_grid_thw"].data.tolist()
                assert t == 1, f"Image must have 1 frame, got {t}"
                yield offset, h // spatial_merge_size, w // spatial_merge_size
            else:
                raise ValueError(f"Unsupported modality: {mm_feature.modality}")

    defget_mrope_input_positions(
        self,
        input_tokens: list[int],
        mm_features: list[MultiModalFeatureSpec],
    ) -> tuple[torch.Tensor, int]:
        llm_pos_ids_list = []
        st = 0
        for offset, llm_grid_h, llm_grid_w in self.iter_mm_grid_hw(
            input_tokens, mm_features
        ):
            text_len = offset - st
            st_idx = llm_pos_ids_list[-1].max() + 1 if len(llm_pos_ids_list) > 0 else 0
            llm_pos_ids_list.append(
                np.broadcast_to(np.arange(text_len), (3, text_len)) + st_idx
            )

            grid_indices = np.indices((1, llm_grid_h, llm_grid_w)).reshape(3, -1)
            grid_indices[0, :] = grid_indices[0, :] + text_len + st_idx
            llm_pos_ids_list.append(grid_indices)
            st = offset + llm_grid_h * llm_grid_w

        if st < len(input_tokens):
            st_idx = llm_pos_ids_list[-1][0, -1] + 1 if len(llm_pos_ids_list) > 0 else 0
            text_len = len(input_tokens) - st
            llm_pos_ids_list.append(
                np.broadcast_to(np.arange(text_len), (3, text_len)) + st_idx
            )

        llm_positions = np.concatenate(llm_pos_ids_list, axis=1).reshape(3, -1)
        mrope_position_delta = (llm_positions.max() + 1 - len(input_tokens)).item()

        return torch.from_numpy(llm_positions), mrope_position_delta

    def_parse_and_validate_image_input(
        self, **kwargs: object
    ) -> IsaacImagePixelInputs | None:
        pixel_values = kwargs.get("pixel_values")
        image_grid_thw = kwargs.get("image_grid_thw")
        if pixel_values is None or image_grid_thw is None:
            return None

        # TensorSchema will automatically validate shapes on initialization
        return IsaacImagePixelInputs(
            pixel_values=pixel_values,
            image_grid_thw=image_grid_thw,
        )

    def_process_image_input(
        self,
        image_input: IsaacImagePixelInputs,
    ) -> tuple[torch.Tensor, ...]:
        pixel_values = image_input["pixel_values"]
        image_grid_thw = image_input["image_grid_thw"]
        if pixel_values.numel() == 0:
            return ()

        device = next(self.language_model.parameters()).device
        dtype = self.vision_embedding.linear_fc1.weight.dtype
        pixel_values = pixel_values.to(device=device, dtype=dtype)
        spatial_grids = image_grid_thw[:, 1:3].to(device, dtype=torch.int32)

        vision_embeddings = self.vision_embedding((pixel_values, spatial_grids))
        merge_size = self.config.vision_config.pixel_shuffle_scale_factor
        sizes = spatial_grids.prod(-1) // (merge_size * merge_size)
        return tuple(vision_embeddings.split(sizes.tolist()))

    defembed_multimodal(self, **kwargs: object) -> MultiModalEmbeddings | None:
        image_input = self._parse_and_validate_image_input(**kwargs)
        if image_input is None:
            return ()
        return self._process_image_input(image_input)

    defforward(
        self,
        input_ids: torch.Tensor | None,
        positions: torch.Tensor,
        intermediate_tensors: IntermediateTensors | None = None,
        inputs_embeds: torch.Tensor | None = None,
        **kwargs: object,
    ) -> torch.Tensor | IntermediateTensors:
        return self.language_model(
            input_ids=input_ids,
            positions=positions,
            intermediate_tensors=intermediate_tensors,
            inputs_embeds=inputs_embeds,
            **kwargs,
        )

    defcompute_logits(self, hidden_states: torch.Tensor) -> torch.Tensor | None:
        return self.language_model.compute_logits(hidden_states)

    defload_weights(self, weights: Iterable[tuple[str, torch.Tensor]]) -> set[str]:
        loader = AutoWeightsLoader(self)
        return loader.load_weights(weights, mapper=self.hf_to_vllm_mapper)

    defget_mm_mapping(self) -> MultiModelKeys:
"""
        Get the module prefix in multimodal models
        """
        return MultiModelKeys.from_string_field(
            language_model="language_model",
            connector="vision_embedding.linear_fc2",  # The final linear layer
            tower_model="vision_embedding",
        )
```