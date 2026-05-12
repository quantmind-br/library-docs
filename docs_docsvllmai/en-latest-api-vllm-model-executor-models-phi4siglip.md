---
title: phi4siglip - vLLM
url: https://docs.vllm.ai/en/latest/api/vllm/model_executor/models/phi4siglip/
source: sitemap
fetched_at: 2026-05-07T21:32:40.960200499-03:00
rendered_js: false
word_count: 0
summary: This document defines the model architecture and integration logic for Phi4Siglip, a multimodal language model within the vLLM framework, including support for vision tower initialization, weight mapping, and image feature processing.
tags:
    - multimodal-model
    - vllm
    - phi4
    - siglip2
    - vision-transformer
    - model-integration
    - tensor-processing
category: configuration
---

```
@MULTIMODAL_REGISTRY.register_processor(
    Phi4SiglipMultiModalProcessor,
    info=Phi4SiglipProcessingInfo,
    dummy_inputs=Phi4SiglipDummyInputsBuilder,
)
classPhi4ForCausalLMV(nn.Module, SupportsMultiModal, SupportsPP):
    hf_to_vllm_mapper = WeightsMapper(
        orig_to_new_prefix={
            "model.vision_tower.vision_tower.vision_model.head.": None,
            "model.vision_tower.vision_tower.": "vision_tower.",
            "model.mm_projector.0.": "multi_modal_projector.linear_1.",
            "model.mm_projector.2.": "multi_modal_projector.linear_2.",
            "lm_head.": "language_model.lm_head.",
            "model.": "language_model.model.",
        },
    )

    @classmethod
    defget_placeholder_str(cls, modality: str, i: int) -> str | None:
        if modality.startswith("image"):
            return DEFAULT_IMAGE_TOKEN
        raise ValueError("Only image modality is supported")

    def__init__(self, *, vllm_config: VllmConfig, prefix: str = "") -> None:
        super().__init__()

        config: PretrainedConfig = vllm_config.model_config.hf_config
        quant_config = vllm_config.quant_config
        self.config = config

        vision_config_dict: dict = getattr(config, "vision_config", {})
        if isinstance(vision_config_dict, dict):
            if "patch_size" not in vision_config_dict:
                vision_config_dict["patch_size"] = 16
            siglip2_config = Siglip2VisionConfig(**vision_config_dict)
        else:
            siglip2_config = vision_config_dict

        vision_hidden_size: int = config.mm_hidden_size  # type: ignore[attr-defined]
        text_hidden_size: int = config.hidden_size  # type: ignore[attr-defined]

        with self._mark_tower_model(vllm_config, "image"):
            layer_idx = -2
            num_hidden_layers = siglip2_config.num_hidden_layers + layer_idx + 1

            self.vision_tower = Siglip2Model(
                siglip2_config,
                quant_config=quant_config,
                num_hidden_layers_override=num_hidden_layers,
                require_post_norm=False,
                prefix=maybe_prefix(prefix, "vision_tower"),
            )
            self.multi_modal_projector = LlavaMultiModalProjector(
                vision_hidden_size=vision_hidden_size,
                text_hidden_size=text_hidden_size,
                projector_hidden_act="gelu",
                multimodal_projector_bias=True,
                quant_config=quant_config,
                prefix=maybe_prefix(prefix, "multi_modal_projector"),
            )

        with self._mark_language_model(vllm_config):
            self.language_model = init_vllm_registered_model(
                vllm_config=vllm_config,
                hf_config=config,
                prefix=maybe_prefix(prefix, "language_model"),
                architectures=["Phi3ForCausalLM"],
            )

        self.make_empty_intermediate_tensors = (
            self.language_model.make_empty_intermediate_tensors
        )

        self.configure_mm_token_handling(
            vocab_size=config.vocab_size,  # type: ignore[attr-defined]
            mm_token_ids=[_IMAGE_TOKEN_ID],
        )

    def_packed_from_padded(
        self,
        pixel_values: torch.Tensor,
        pixel_attention_mask: torch.Tensor,
        spatial_shapes: torch.Tensor,
    ) -> tuple[torch.Tensor, torch.Tensor, torch.Tensor, torch.Tensor]:
"""Convert padded NaFlex tensors to packed format for Siglip2Model."""
        valid_counts = pixel_attention_mask.sum(dim=1).to(torch.int32)
        pixel_values_packed = pixel_values[pixel_attention_mask.bool()]
        cu_seqlens = torch.zeros(
            len(valid_counts) + 1,
            dtype=torch.int32,
            device=pixel_values.device,
        )
        cu_seqlens[1:] = valid_counts.cumsum(0)
        max_seqlen = valid_counts.max()
        return (
            pixel_values_packed,
            spatial_shapes,
            cu_seqlens,
            max_seqlen,
        )

    def_parse_and_validate_image_input(
        self, **kwargs: object
    ) -> Phi4SiglipImagePixelInputs | None:
        pixel_values = kwargs.pop("pixel_values", None)
        pixel_attention_mask = kwargs.pop("pixel_attention_mask", None)
        spatial_shapes = kwargs.pop("spatial_shapes", None)
        if pixel_values is None:
            return None

        return Phi4SiglipImagePixelInputs(
            type="pixel_values",
            pixel_values=pixel_values,
            pixel_attention_mask=pixel_attention_mask,
            spatial_shapes=spatial_shapes,
        )

    def_process_image_input(
        self, image_input: Phi4SiglipImagePixelInputs
    ) -> MultiModalEmbeddings:
        pixel_values = image_input["pixel_values"]
        pixel_attention_mask = image_input["pixel_attention_mask"]
        spatial_shapes = image_input["spatial_shapes"]

        (
            pixel_values_packed,
            spatial_shapes_packed,
            cu_seqlens,
            max_seqlen,
        ) = self._packed_from_padded(pixel_values, pixel_attention_mask, spatial_shapes)

        vision_features = self.vision_tower(
            pixel_values_packed=pixel_values_packed,
            spatial_shapes=spatial_shapes_packed,
            cu_seqlens=cu_seqlens,
            max_seqlen=max_seqlen,
            select_layers=[-2],
        )

        if vision_features.dim() == 3:
            vision_features = vision_features.squeeze(0)

        image_features = self.multi_modal_projector(vision_features)

        valid_counts = pixel_attention_mask.sum(dim=1).tolist()
        return torch.split(image_features, [int(c) for c in valid_counts])

    defembed_multimodal(self, **kwargs: object) -> MultiModalEmbeddings:
        image_input = self._parse_and_validate_image_input(**kwargs)
        if image_input is None:
            return []

        return self._process_image_input(image_input)

    defforward(
        self,
        input_ids: torch.Tensor | None,
        positions: torch.Tensor,
        intermediate_tensors: IntermediateTensors | None = None,
        inputs_embeds: torch.Tensor | None = None,
        **kwargs: object,
    ) -> torch.Tensor | IntermediateTensors:
        if intermediate_tensors is not None:
            inputs_embeds = None

        hidden_states = self.language_model.model(
            input_ids,
            positions,
            intermediate_tensors,
            inputs_embeds=inputs_embeds,
        )
        return hidden_states

    defcompute_logits(
        self,
        hidden_states: torch.Tensor,
    ) -> torch.Tensor | None:
        return self.language_model.compute_logits(hidden_states)

    defload_weights(self, weights: Iterable[tuple[str, torch.Tensor]]) -> set[str]:
        loader = AutoWeightsLoader(self)
        return loader.load_weights(weights, mapper=self.hf_to_vllm_mapper)
```