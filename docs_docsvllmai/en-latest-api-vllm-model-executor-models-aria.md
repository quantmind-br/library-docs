---
title: aria - vLLM
url: https://docs.vllm.ai/en/latest/api/vllm/model_executor/models/aria/
source: sitemap
fetched_at: 2026-05-07T21:29:03.165281515-03:00
rendered_js: false
word_count: 0
summary: This document defines the Aria model class for multimodal conditional generation, implementing vision-language integration within the vLLM framework. It details the architecture for processing image inputs and text generation, including weight mapping and embedding logic.
tags:
    - multimodal-model
    - vllm-integration
    - vision-transformer
    - neural-network
    - tensor-processing
    - weight-mapping
category: reference
---

```
@MULTIMODAL_REGISTRY.register_processor(
    AriaMultiModalProcessor,
    info=AriaProcessingInfo,
    dummy_inputs=AriaDummyInputsBuilder,
)
classAriaForConditionalGeneration(nn.Module, SupportsMultiModal):
"""
    Aria model for conditional generation tasks.

    This model combines a vision tower, a multi-modal projector, and a language
    model to perform tasks that involve both image and text inputs.
    """

    hf_to_vllm_mapper = WeightsMapper(
        orig_to_new_prefix={
            # mapping for new names in checkpoint saved after transformers v4.52
            "model.language_model.": "language_model.model.",
            "model.vision_tower.": "vision_tower.",
            "model.multi_modal_projector.": "multi_modal_projector.",
            # mapping for original checkpoint
            "language_model.model": "language_model",
            "language_model.lm_head": "lm_head",
        },
        orig_to_new_suffix={
            "router.weight": "router_weight",
        },
    )

    @classmethod
    defget_placeholder_str(cls, modality: str, i: int) -> str | None:
        if modality.startswith("image"):
            return "<|fim_prefix|><|img|><|fim_suffix|>"

        raise ValueError("Only image modality is supported")

    def__init__(
        self,
        vllm_config: VllmConfig,
        prefix: str = "",
    ):
        super().__init__()
        config = vllm_config.model_config.hf_config
        quant_config = vllm_config.quant_config

        self.config = config

        with self._mark_tower_model(vllm_config, "image"):
            self.vision_tower = AriaVisionTransformer(
                config.vision_config,
                quant_config=quant_config,
                prefix=f"{prefix}.vision_tower",
            )
            self.multi_modal_projector = AriaProjector(
                config, prefix=maybe_prefix(prefix, "multi_modal_projector")
            )

        with self._mark_language_model(vllm_config):
            self.language_model = AriaTextModel(
                vllm_config=vllm_config.with_hf_config(config.text_config),
                prefix=maybe_prefix(prefix, "language_model.model"),
            )

            self.lm_head = ParallelLMHead(
                config.text_config.vocab_size,
                config.text_config.hidden_size,
                quant_config=quant_config,
                prefix=maybe_prefix(prefix, "lm_head"),
            )

            logit_scale = getattr(config, "logit_scale", 1.0)
            self.logits_processor = LogitsProcessor(
                config.text_config.vocab_size, scale=logit_scale
            )

    def_parse_and_validate_image_input(
        self, **kwargs: object
    ) -> AriaImagePixelInputs | None:
        pixel_values = kwargs.pop("pixel_values", None)
        pixel_mask = kwargs.pop("pixel_mask", None)

        if pixel_values is None:
            return None

        return AriaImagePixelInputs(
            type="pixel_values",
            pixel_values=pixel_values,
            pixel_mask=pixel_mask,
        )

    def_create_patch_attention_mask(
        self,
        pixel_mask: torch.Tensor | None,
    ) -> torch.Tensor | None:
        if pixel_mask is None:
            return None

        patches_subgrid = pixel_mask.unfold(
            dimension=1,
            size=self.vision_tower.config.patch_size,
            step=self.vision_tower.config.patch_size,
        ).unfold(
            dimension=2,
            size=self.vision_tower.config.patch_size,
            step=self.vision_tower.config.patch_size,
        )
        return (patches_subgrid.sum(dim=(-1, -2)) > 0).bool()

    def_process_image_input(
        self, image_input: AriaImagePixelInputs
    ) -> tuple[torch.Tensor, torch.Tensor]:
        pixel_values = image_input["pixel_values"]
        pixel_mask = image_input["pixel_mask"]

        patch_attention_mask = self._create_patch_attention_mask(pixel_mask)

        image_outputs = self.vision_tower(
            pixel_values=pixel_values,
            patch_attention_mask=patch_attention_mask,
        )
        image_attn_mask = None
        if patch_attention_mask is not None:
            flattened_mask = patch_attention_mask.flatten(1)
            image_attn_mask = torch.logical_not(flattened_mask)

        return self.multi_modal_projector(image_outputs, image_attn_mask)

    defembed_multimodal(self, **kwargs: object) -> MultiModalEmbeddings:
        image_input = self._parse_and_validate_image_input(**kwargs)
        if image_input is None:
            return []
        multimodal_embeddings = self._process_image_input(image_input)
        return multimodal_embeddings

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

        hidden_states = self.language_model(
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
        logits = self.logits_processor(self.lm_head, hidden_states)
        return logits

    defload_weights(self, weights: Iterable[tuple[str, torch.Tensor]]):
        loader = AutoWeightsLoader(self)
        loader.load_weights(weights, mapper=self.hf_to_vllm_mapper)
```