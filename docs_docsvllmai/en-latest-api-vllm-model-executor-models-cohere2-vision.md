---
title: cohere2_vision - vLLM
url: https://docs.vllm.ai/en/latest/api/vllm/model_executor/models/cohere2_vision/
source: sitemap
fetched_at: 2026-05-07T21:29:21.042195587-03:00
rendered_js: false
word_count: 14
summary: This document defines the Cohere2Vision model architecture for multi-modal conditional generation within the vLLM framework, including implementations for image processing, weight mapping, and multi-modal embedding generation.
tags:
    - vllm
    - multi-modal
    - model-architecture
    - computer-vision
    - machine-learning
    - pytorch
category: reference
---

```
@MULTIMODAL_REGISTRY.register_processor(
    Cohere2VisionMultiModalProcessor,
    info=Cohere2VisionProcessingInfo,
    dummy_inputs=Cohere2VisionDummyInputsBuilder,
)
classCohere2VisionForConditionalGeneration(
    nn.Module, SupportsMultiModal, SupportsPP, SupportsQuant
):
    hf_to_vllm_mapper = WeightsMapper(
        orig_to_new_prefix={
            "model.vision_tower.": "vision_tower.",
            "model.multi_modal_projector.": "multi_modal_projector.",
            "model.language_model.": "language_model.model.",
        }
    )

    packed_modules_mapping = {
        "qkv_proj": ["q_proj", "k_proj", "v_proj"],
        "gate_up_proj": ["gate_proj", "up_proj"],
    }

    def__init__(self, *, vllm_config: VllmConfig, prefix: str = ""):
        super().__init__()
        config: Cohere2VisionConfig = vllm_config.model_config.hf_config
        quant_config = vllm_config.quant_config
        multimodal_config = vllm_config.model_config.multimodal_config
        self.config = config
        self.quant_config = quant_config
        self.multimodal_config = multimodal_config
        self._patch_quant_config(config, quant_config)

        with self._mark_tower_model(vllm_config, "image"):
            self.vision_tower = SiglipVisionModel(
                config.vision_config,
                quant_config,
                prefix=maybe_prefix(prefix, "vision_tower"),
            )
            self.multi_modal_projector = Cohere2VisionMultiModalProjector(
                config, prefix=maybe_prefix(prefix, "multi_modal_projector")
            )

        with self._mark_language_model(vllm_config):
            self.language_model = init_vllm_registered_model(
                vllm_config=vllm_config,
                hf_config=config.text_config,
                prefix=maybe_prefix(prefix, "language_model"),
                architectures=config.text_config.architectures,
            )

    @property
    defdtype(self):
        return next(self.parameters()).dtype

    defload_weights(self, weights: Iterable[tuple[str, torch.Tensor]]) -> set[str]:
        loader = AutoWeightsLoader(self)
        return loader.load_weights(weights, mapper=self.hf_to_vllm_mapper)

    def_process_image_input(
        self, image_input: Cohere2VisionImagePixelInputs, **kwargs
    ) -> list[torch.Tensor]:
"""Process image pixels through vision tower and projector.

        Args:
            image_input: Validated image input containing pixel values and
                         patch counts

        Returns:
            List of flattened image embeddings, one per image
        """
        pixel_values = image_input["pixel_values"]
        num_patches = image_input["num_patches"]

        # Extract visual features
        image_features = self.vision_tower(pixel_values)

        # Project to text embedding space
        image_embeds = self.multi_modal_projector(image_features)

        # Split and flatten embeddings per image
        return [e.flatten(0, 2) for e in image_embeds.split(num_patches.tolist())]

    def_parse_and_validate_image_input(
        self, **kwargs: object
    ) -> Cohere2VisionImagePixelInputs | None:
        pixel_values = kwargs.pop("pixel_values", None)
        num_patches = kwargs.pop("num_patches", None)
        image_embeds = kwargs.pop("image_embeds", None)
        assert image_embeds is None, "Cohere2Vision does not support image_embeds."

        if pixel_values is None:
            return None

        return Cohere2VisionImagePixelInputs(
            type="pixel_values",
            pixel_values=pixel_values,
            num_patches=num_patches,
            resolve_bindings={
                "h": self.config.vision_config.image_size,
                "w": self.config.vision_config.image_size,
            },
        )

    def_patch_quant_config(
        self, config: PretrainedConfig, quant_config: QuantizationConfig
    ):
        # the awq models from OpenGVLab missing `modules_to_not_convert`
        # patch the quant_config to add `modules_to_not_convert` back
        if isinstance(quant_config, AWQConfig):
            text_config = config.text_config
            llm_quant_config = getattr(text_config, "quantization_config", None)
            if (not quant_config.modules_to_not_convert) and (
                llm_quant_config is not None
            ):
                quant_config.modules_to_not_convert.append("vision_tower")

    defembed_multimodal(self, **kwargs: object) -> MultiModalEmbeddings:
        image_input = self._parse_and_validate_image_input(**kwargs)
        if image_input is None:
            return []

        return self._process_image_input(image_input, **kwargs)

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
            input_ids=input_ids,
            positions=positions,
            intermediate_tensors=intermediate_tensors,
            inputs_embeds=inputs_embeds,
        )
        return hidden_states

    defcompute_logits(
        self,
        hidden_states: torch.Tensor,
    ) -> torch.Tensor | None:
        return self.language_model.compute_logits(hidden_states)
```