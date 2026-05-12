---
title: idefics3 - vLLM
url: https://docs.vllm.ai/en/latest/api/vllm/model_executor/models/idefics3/
source: sitemap
fetched_at: 2026-05-07T21:30:54.064459942-03:00
rendered_js: false
word_count: 0
summary: This document defines the implementation of the Idefics3 model architecture within a multimodal framework, providing methods for processing image inputs, embedding multimodal data, and managing model weights.
tags:
    - multimodal-model
    - idefics3
    - vllm
    - pytorch
    - image-processing
    - model-architecture
category: reference
---

```
@MULTIMODAL_REGISTRY.register_processor(
    Idefics3MultiModalProcessor,
    info=Idefics3ProcessingInfo,
    dummy_inputs=Idefics3DummyInputsBuilder,
)
classIdefics3ForConditionalGeneration(nn.Module, SupportsMultiModal, SupportsLoRA):
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

    @classmethod
    defget_placeholder_str(cls, modality: str, i: int) -> str | None:
        if modality.startswith("image"):
            return "<image>"

        raise ValueError("Only image modality is supported")

    def__init__(self, *, vllm_config: VllmConfig, prefix: str = ""):
        super().__init__()

        config = vllm_config.model_config.hf_config
        quant_config = vllm_config.quant_config
        multimodal_config = vllm_config.model_config.multimodal_config

        self.config = config
        self.multimodal_config = multimodal_config

        with self._mark_composite_model(
            vllm_config,
            language_targets=LlamaModel,
            tower_targets={"image": (Idefics3VisionTransformer, Idefics3Connector)},
        ):
            self.model = Idefics3Model(
                vllm_config=vllm_config,
                prefix=maybe_prefix(prefix, "model"),
            )

        self.image_token_id = self.config.image_token_id

        self.lm_head = ParallelLMHead(
            config.text_config.vocab_size,
            config.text_config.hidden_size,
            quant_config=quant_config,
            prefix=maybe_prefix(prefix, "lm_head"),
        )
        if self.config.text_config.tie_word_embeddings:
            self.lm_head.weight = self.model.text_model.embed_tokens.weight
        self.logits_processor = LogitsProcessor(config.text_config.vocab_size)

    def_parse_and_validate_image_input(self, **kwargs: object) -> ImageInputs | None:
        pixel_values = kwargs.pop("pixel_values", None)
        image_embeds = kwargs.pop("image_embeds", None)

        if pixel_values is None and image_embeds is None:
            return None

        if image_embeds is not None:
            return Idefics3ImageEmbeddingInputs(
                type="image_embeds",
                data=image_embeds,
            )

        if pixel_values is not None:
            pixel_attention_mask = kwargs.pop("pixel_attention_mask")
            num_patches = kwargs.pop("num_patches")
            expected_h = expected_w = self.config.vision_config.image_size

            return Idefics3ImagePixelInputs(
                type="pixel_values",
                pixel_values=pixel_values,
                pixel_attention_mask=pixel_attention_mask,
                num_patches=num_patches,
                resolve_bindings={"h": expected_h, "w": expected_w},
            )

        raise AssertionError("This line should be unreachable.")

    def_process_image_pixels(self, inputs: Idefics3ImagePixelInputs) -> torch.Tensor:
        pixel_values = inputs["pixel_values"]
        pixel_attention_mask = inputs["pixel_attention_mask"]

        return self.model.image_pixels_to_features(
            pixel_values,
            pixel_attention_mask=pixel_attention_mask,
        )

    def_process_image_input(
        self,
        image_input: ImageInputs,
    ) -> torch.Tensor | list[torch.Tensor]:
        if image_input["type"] == "image_embeds":
            return image_input["data"]

        image_features = self._process_image_pixels(image_input)
        image_features = self.model.connector(image_features)

        num_patches = image_input["num_patches"]
        return [e.flatten(0, 1) for e in image_features.split(num_patches.tolist())]

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

        hidden_states = self.model.text_model(
            input_ids, positions, intermediate_tensors, inputs_embeds=inputs_embeds
        )

        return hidden_states

    defcompute_logits(self, hidden_states: torch.Tensor) -> torch.Tensor:
        logits = self.logits_processor(self.lm_head, hidden_states)
        return logits

    defload_weights(self, weights: Iterable[tuple[str, torch.Tensor]]) -> set[str]:
        loader = AutoWeightsLoader(self)
        return loader.load_weights(weights)

    defget_mm_mapping(self) -> MultiModelKeys:
"""
        Get the module prefix in multimodal models
        """
        return MultiModelKeys.from_string_field(
            language_model="model.text_model",
            connector="model.connector",
            tower_model="model.vision_model",
        )

    defget_num_mm_encoder_tokens(
        self,
        num_image_tokens: int,
    ) -> int:
        hf_config = self.config
        scale_factor = hf_config.scale_factor

        return num_image_tokens * scale_factor**2

    defget_num_mm_connector_tokens(
        self,
        num_vision_tokens: int,
    ) -> int:
        hf_config = self.config
        scale_factor = hf_config.scale_factor

        return num_vision_tokens // scale_factor**2
```