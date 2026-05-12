---
title: mistral3 - vLLM
url: https://docs.vllm.ai/en/latest/api/vllm/model_executor/models/mistral3/
source: sitemap
fetched_at: 2026-05-07T21:31:53.886899483-03:00
rendered_js: false
word_count: 12
summary: This document defines the Mistral3 multimodal model architecture within the vLLM framework, including weight mapping, image processing, and forward pass logic.
tags:
    - multimodal
    - mistral-3
    - vllm
    - model-architecture
    - weights-mapping
    - tensor-processing
category: concept
---

```
@MULTIMODAL_REGISTRY.register_processor(
    Mistral3MultiModalProcessor,
    info=Mistral3ProcessingInfo,
    dummy_inputs=Mistral3DummyInputsBuilder,
)
classMistral3ForConditionalGeneration(
    nn.Module,
    SupportsLoRA,
    SupportsMultiModal,
    SupportsPP,
    SupportsEagle,
    SupportsEagle3,
):
    packed_modules_mapping = {
        "qkv_proj": ["q_proj", "k_proj", "v_proj"],
        "gate_up_proj": ["gate_proj", "up_proj"],
    }

    hf_to_vllm_mapper = WeightsMapper(
        orig_to_new_prefix={
            # mapping for new names in checkpoint saved after transformers v4.52
            "model.language_model.": "language_model.model.",
            "model.vision_tower.": "vision_tower.",
            "model.multi_modal_projector.": "multi_modal_projector.",
            "lm_head.": "language_model.lm_head.",
            # Some PEFT LoRAs are trained against the text submodule directly
            # and produce names like `base_model.model.model.layers.*`.
            "model.": "language_model.model.",
        },
        orig_to_new_suffix={
            # FP8 quantized HF checkpoints use "activation_scale" and
            # "weight_scale_inv" but vLLM's FP8 linear layers register
            # them as "input_scale" and "weight_scale"
            ".activation_scale": ".input_scale",
            ".weight_scale_inv": ".weight_scale",
        },
    )

    @classmethod
    defget_placeholder_str(cls, modality: str, i: int) -> str | None:
        if modality.startswith("image"):
            return None

        raise ValueError("Only image modality is supported")

    def__init__(self, *, vllm_config: VllmConfig, prefix: str = "") -> None:
        super().__init__()

        config = vllm_config.model_config.hf_config
        quant_config = vllm_config.quant_config
        multimodal_config = vllm_config.model_config.multimodal_config

        self.config = config
        self.multimodal_config = multimodal_config

        # NOTE: This is a special case for Pixtral-12B in the HF-format
        # https://huggingface.co/mistral-community/pixtral-12b/blob/main/config.json  # noqa
        if (
            config.projector_hidden_act is None
            and config.vision_config.hidden_act == "gelu"
        ):
            config.projector_hidden_act = "gelu"

        with self._mark_tower_model(vllm_config, "image"):
            self.vision_tower = init_vision_tower_for_mistral3(
                config,
                quant_config=quant_config,
                require_post_norm=False,
                prefix=maybe_prefix(prefix, "vision_tower"),
            )
            self.multi_modal_projector = Mistral3MultiModalProjector(
                vision_hidden_size=config.vision_config.hidden_size,
                text_hidden_size=config.text_config.hidden_size,
                projector_hidden_act=config.projector_hidden_act,
                spatial_merge_size=config.spatial_merge_size,
                patch_size=config.vision_config.patch_size,
                multimodal_projector_bias=config.multimodal_projector_bias,
                quant_config=quant_config,
                prefix=maybe_prefix(prefix, "multi_modal_projector"),
            )

        with self._mark_language_model(vllm_config):
            self.language_model = init_vllm_registered_model(
                vllm_config=vllm_config,
                hf_config=config.text_config,
                prefix=maybe_prefix(prefix, "language_model"),
            )

        self.make_empty_intermediate_tensors = (
            self.language_model.make_empty_intermediate_tensors
        )

    def_parse_and_validate_image_input(
        self, **kwargs: object
    ) -> Mistral3ImagePixelInputs | None:
        pixel_values = kwargs.pop("pixel_values", None)
        image_embeds = kwargs.pop("image_embeds", None)

        if pixel_values is None and image_embeds is None:
            return None

        return Mistral3ImagePixelInputs(
            type="pixel_values_pixtral",
            pixel_values=pixel_values,
        )

    def_process_image_input(
        self,
        image_input: Mistral3ImagePixelInputs,
    ) -> torch.Tensor | tuple[torch.Tensor, ...]:
        if image_input["type"] == "image_embeds":
            return image_input["data"]

        image_sizes = [
            (img.shape[-2], img.shape[-1]) for img in image_input["pixel_values"]
        ]

        image_features = self.vision_tower(image_input["pixel_values"])

        if isinstance(image_features, torch.Tensor):
            return self.multi_modal_projector(image_features, image_sizes)

        feature_sizes = [
            image_feature.shape[0] // self.config.spatial_merge_size**2
            for image_feature in image_features
        ]

        image_embeds = self.multi_modal_projector(
            torch.cat(image_features), image_sizes
        )
        if len(feature_sizes) > 1:
            image_embeds = torch.split(image_embeds, feature_sizes)
        else:
            image_embeds = (image_embeds,)
        return image_embeds

    defembed_multimodal(self, **kwargs: object) -> MultiModalEmbeddings:
        image_input = self._parse_and_validate_image_input(**kwargs)
        if image_input is None:
            return []

        vision_embeddings = self._process_image_input(image_input)

        return vision_embeddings

    defforward(
        self,
        input_ids: torch.Tensor | None,
        positions: torch.Tensor,
        intermediate_tensors: IntermediateTensors | None = None,
        inputs_embeds: torch.Tensor | None = None,
        **kwargs: object,
    ) -> torch.Tensor | IntermediateTensors:
"""Run forward pass for Mistral3.

        One key thing to understand is the `input_ids` already accounts for the
        positions of the to-be-inserted image embeddings.

        Concretely, consider a text prompt:
        `"USER: <image>\\nWhat's the content of the image?\\nASSISTANT:"`.

        Tokenizer outputs:
        `[1, 3148, 1001, 29901, 29871, 32000, 29871, 13, 5618, 29915, 29879,
        278, 2793, 310, 278, 1967, 29973, 13, 22933, 9047, 13566, 29901]`.

        To reserve space in KV cache, we have to insert placeholder tokens
        before they are inputted to the model, so the input processor prepends
        additional image tokens (denoted as `32000`), resulting in:
        `[1, 3148, 1001, 29901, 29871, 32000, ..., 32000, 29871, 13, 5618,
        29915, 29879, 278, 2793, 310, 278, 1967, 29973, 13, 22933, 9047, 13566,
        29901]`.

        We insert 575 tokens so that including the original image token in the
        input, there are a total of 576 (24 * 24) image tokens, which
        corresponds to the number of image tokens inputted to the language
        model, i.e. the number of image tokens outputted by the visual encoder.

        This way, the `positions` and `attn_metadata` are consistent
        with the `input_ids`.

        Args:
            input_ids: Flattened (concatenated) input_ids corresponding to a
                batch.
            positions: Position indices for the input tokens.
            intermediate_tensors: Intermediate tensors from prior forward pass.
            inputs_embeds: Optional tensor of input embeddings.

        Info:
            [`Mistral3ImagePixelInputs`][vllm.model_executor.models.mistral3.Mistral3ImagePixelInputs]
        """
        if intermediate_tensors is not None:
            inputs_embeds = None

        hidden_states = self.language_model.model(
            input_ids, positions, intermediate_tensors, inputs_embeds=inputs_embeds
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
```