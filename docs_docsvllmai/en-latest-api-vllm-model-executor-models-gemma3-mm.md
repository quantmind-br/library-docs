---
title: gemma3_mm - vLLM
url: https://docs.vllm.ai/en/latest/api/vllm/model_executor/models/gemma3_mm/
source: sitemap
fetched_at: 2026-05-07T21:30:11.69098841-03:00
rendered_js: false
word_count: 0
summary: This document defines the Gemma3 model architecture integration for vLLM, including multimodal processing, weight mapping, and input handling for vision and language components.
tags:
    - gemma3
    - multimodal
    - vllm
    - computer-vision
    - model-architecture
    - pytorch
category: concept
---

```
@MULTIMODAL_REGISTRY.register_processor(
    Gemma3MultiModalProcessor,
    info=Gemma3ProcessingInfo,
    dummy_inputs=Gemma3DummyInputsBuilder,
)
classGemma3ForConditionalGeneration(
    nn.Module, SupportsMultiModal, SupportsPP, SupportsLoRA
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

    hf_to_vllm_mapper = WeightsMapper(
        orig_to_new_prefix={
            # mapping for new names in checkpoint saved after transformers v4.52
            "model.language_model.": "language_model.model.",
            "model.vision_tower.": "vision_tower.",
            "model.multi_modal_projector.": "multi_modal_projector.",
            "lm_head.": "language_model.lm_head.",
        }
    )

    @classmethod
    defget_placeholder_str(cls, modality: str, i: int) -> str | None:
        if modality.startswith("image"):
            return "<start_of_image>"

        raise ValueError("Only image modality is supported")

    def__init__(self, *, vllm_config: VllmConfig, prefix: str = ""):
        super().__init__()
        config = vllm_config.model_config.hf_config
        quant_config = vllm_config.quant_config
        multimodal_config = vllm_config.model_config.multimodal_config
        self.config = config
        self.quant_config = quant_config
        self.multimodal_config = multimodal_config

        self.configure_mm_token_handling(
            vocab_size=config.text_config.vocab_size,
            mm_token_ids=[config.image_token_index],
        )

        with self._mark_tower_model(vllm_config, "image"):
            self.vision_tower = SiglipVisionModel(
                config.vision_config,
                quant_config,
                prefix=maybe_prefix(prefix, "vision_tower"),
            )
            self.multi_modal_projector = Gemma3MultiModalProjector(config)

        with self._mark_language_model(vllm_config):
            self.language_model = init_vllm_registered_model(
                vllm_config=vllm_config,
                hf_config=config.text_config,
                prefix=maybe_prefix(prefix, "language_model"),
                architectures=["Gemma3ForCausalLM"],
            )

            logit_scale = getattr(config, "logit_scale", 1.0)
            self.language_model.logits_processor.scale *= logit_scale

        self.make_empty_intermediate_tensors = (
            self.language_model.make_empty_intermediate_tensors
        )

    @property
    defdtype(self):
        return next(self.parameters()).dtype

    def_parse_and_validate_image_input(
        self, **kwargs: object
    ) -> Gemma3ImageInputs | None:
        pixel_values = kwargs.pop("pixel_values", None)
        num_patches = kwargs.pop("num_patches", None)
        image_embeds = kwargs.pop("image_embeds", None)
        assert image_embeds is None, "Gemma3 does not support image_embeds."
        if pixel_values is None:
            return None

        image_size = self.config.vision_config.image_size

        return Gemma3ImagePixelInputs(
            pixel_values=pixel_values,
            num_patches=num_patches,
            resolve_bindings={"h": image_size, "w": image_size},
        )

    def_image_pixels_to_features(
        self,
        vision_tower: SiglipVisionModel,
        pixel_values: torch.Tensor,
    ) -> torch.Tensor:
        return vision_tower(pixel_values)

    def_process_image_input(
        self,
        image_input: Gemma3ImageInputs,
    ) -> list[torch.Tensor]:
        pixel_values = image_input["pixel_values"]
        num_patches = image_input["num_patches"]

        image_features = self._image_pixels_to_features(
            self.vision_tower,
            pixel_values,
        )
        image_embeds = self.multi_modal_projector(image_features)

        return [e.flatten(0, 1) for e in image_embeds.split(num_patches.tolist())]

    defembed_multimodal(self, **kwargs: object) -> MultiModalEmbeddings:
        image_input = self._parse_and_validate_image_input(**kwargs)
        if image_input is None:
            return []

        return self._process_image_input(image_input)

    defembed_input_ids(
        self,
        input_ids: torch.Tensor,
        multimodal_embeddings: MultiModalEmbeddings | None = None,
        *,
        is_multimodal: torch.Tensor | None = None,
    ) -> torch.Tensor:
        # Early return for text-only inference (no multimodal data)
        if multimodal_embeddings is None or is_multimodal is None:
            return super().embed_input_ids(input_ids)

        # Use interface default with OOV handling enabled
        return super().embed_input_ids(
            input_ids,
            multimodal_embeddings=multimodal_embeddings,
            is_multimodal=is_multimodal,
        )

    defforward(
        self,
        input_ids: torch.Tensor | None,
        positions: torch.Tensor,
        intermediate_tensors: IntermediateTensors | None = None,
        inputs_embeds: torch.Tensor | None = None,
        **kwargs: object,
    ) -> IntermediateTensors:
        if intermediate_tensors is not None:
            inputs_embeds = None

        hidden_states = self.language_model.model(
            input_ids,
            positions,
            intermediate_tensors,
            inputs_embeds=inputs_embeds,
            **kwargs,
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

    defget_mm_mapping(self) -> MultiModelKeys:
"""
        Get the module prefix in multimodal models
        """
        return MultiModelKeys.from_string_field(
            language_model="language_model",
            connector="multi_modal_projector",
            tower_model="vision_tower",
        )

    defget_num_mm_encoder_tokens(self, num_image_tokens: int) -> int:
"""
        Calculate the number of tokens output by the vision encoder.

        The vision encoder processes images into patch embeddings. For Gemma3,
        the relationship between prompt placeholder tokens and actual vision
        encoder output tokens depends on the patch grid size.

        Args:
            num_image_tokens: Number of image placeholder tokens in the prompt
                              (typically mm_tokens_per_image per image)

        Returns:
            Number of tokens output by the vision encoder
        """
        # For Gemma3, the vision encoder outputs tokens_per_side x tokens_per_side
        # tokens per image. Since num_image_tokens represents the number of
        # connector output tokens (mm_tokens_per_image = 256), and tokens_per_side
        # is sqrt(256) = 16, we need to account for the token expansion.
        # Based on empirical testing, the multiplier of 16 works correctly.
        return num_image_tokens * 16

    defget_num_mm_connector_tokens(self, num_vision_tokens: int) -> int:
"""
        Calculate the number of tokens output by the multimodal connector.

        The connector applies projection and normalization but maintains the
        token count for Gemma3.

        Args:
            num_vision_tokens: Number of tokens from vision encoder

        Returns:
            Number of tokens after connector processing
        """
        # The Gemma3 connector maintains a 1:1 token mapping
        return num_vision_tokens
```