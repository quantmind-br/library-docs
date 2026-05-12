---
title: hunyuan_vision - vLLM
url: https://docs.vllm.ai/en/latest/api/vllm/model_executor/models/hunyuan_vision/
source: sitemap
fetched_at: 2026-05-07T21:30:45.829016712-03:00
rendered_js: false
word_count: 0
summary: This document defines the HunYuanVL model implementation for vLLM, detailing the multimodal architecture, positional encoding for XDRoPE, and the integration of vision transformer components with language models.
tags:
    - vllm
    - multimodal
    - hunyuan-vl
    - pytorch
    - vision-transformer
    - xdrope
    - model-architecture
category: concept
---

```
@MULTIMODAL_REGISTRY.register_processor(
    HunYuanVLMultiModalProcessor,
    info=HunYuanVLProcessingInfo,
    dummy_inputs=HunYuanVLDummyInputsBuilder,
)
classHunYuanVLForConditionalGeneration(
    nn.Module,
    SupportsMultiModal,
    SupportsLoRA,
    SupportsPP,
    SupportsQuant,
    SupportsXDRoPE,
    SupportsEagle,
    SupportsEagle3,
):
    # To ensure correct weight loading and mapping.
    hf_to_vllm_mapper = WeightsMapper(
        orig_to_new_prefix={
            # mapping for new names in checkpoint saved after transformers v4.52
            "vit.vit.": "visual.",
            "vit.": "visual.",
            "model.": "language_model.model.",
        }
    )

    supports_encoder_tp_data = True

    defget_xdrope_input_positions(
        self,
        input_tokens: list[int],
        mm_features: list[MultiModalFeatureSpec],
    ) -> torch.Tensor:
        kwargs = MultiModalFeatureSpec.gather_kwargs(
            mm_features,
            {"image_grid_thw"},
        )
        image_grid_thw = [item.tolist() for item in kwargs.get("image_grid_thw", [])]

        hf_config = self.config
        image_start_token_id = hf_config.image_start_token_id
        spatial_merge_size = hf_config.vision_config.spatial_merge_size
        xd_num = len(hf_config.rope_scaling["xdrope_section"])

        input_tokens_tensor = torch.tensor(input_tokens)
        image_start_indices = torch.argwhere(
            input_tokens_tensor == image_start_token_id
        ).squeeze(1)

        p_index = torch.arange(len(input_tokens_tensor))
        w_index = torch.arange(len(input_tokens_tensor))
        h_index = torch.arange(len(input_tokens_tensor))
        t_index = torch.arange(len(input_tokens_tensor))
        for image_index in range(len(image_start_indices)):
            # +1 : first image_token, +2: for xdrope positions
            pos = image_start_indices[image_index] + 2
            t, h, w = image_grid_thw[image_index]
            _, llm_grid_h, llm_grid_w = (
                t,
                h // spatial_merge_size,
                w // spatial_merge_size,
            )

            token_num = (llm_grid_w + 1) * llm_grid_h
            w_index[pos : pos + token_num].copy_(
                torch.arange(0, llm_grid_w + 1)
                .reshape(1, -1)
                .expand(llm_grid_h, -1)
                .reshape(-1)
            )
            h_index[pos : pos + token_num].copy_(
                torch.arange(0, llm_grid_h)
                .reshape(-1, 1)
                .expand(-1, llm_grid_w + 1)
                .reshape(-1)
            )
            t_index[pos : pos + token_num] = image_index

        if xd_num == 4:
            llm_positions = torch.stack([p_index, w_index, h_index, t_index])
        elif xd_num == 3:
            llm_positions = torch.stack([w_index, h_index, t_index])

        return llm_positions

    @classmethod
    defget_placeholder_str(cls, modality: str, i: int) -> str | None:
        if modality.startswith("image"):
            return "<｜hy_place▁holder▁no▁100｜><｜hy_place▁holder▁no▁102｜><｜hy_place▁holder▁no▁101｜>"  # noqa: E501

        raise ValueError("Only image modality is supported")

    def__init__(self, *, vllm_config: VllmConfig, prefix: str = ""):
        super().__init__()
        config: HunYuanVLConfig = vllm_config.model_config.hf_config

        self.config = config

        with self._mark_tower_model(vllm_config, {"image"}):
            self.visual = HunYuanVisionTransformer(
                config.vision_config,
                quant_config=vllm_config.quant_config,
                prefix=maybe_prefix(prefix, "visual"),
            )

        with self._mark_language_model(vllm_config):
            self.language_model = init_vllm_registered_model(
                vllm_config=vllm_config,
                prefix=maybe_prefix(prefix, "language_model.model"),
                architectures=[
                    "HunYuanDenseV1ForCausalLM",
                    "HunYuanMoEV1ForCausalLM",
                ],
            )

        self.make_empty_intermediate_tensors = (
            self.language_model.make_empty_intermediate_tensors
        )

    def_parse_and_validate_image_input(
        self, **kwargs: object
    ) -> HunYuanVLImageInputs | None:
        pixel_values = kwargs.pop("pixel_values", None)
        image_embeds = kwargs.pop("image_embeds", None)
        image_grid_thw = kwargs.pop("image_grid_thw", None)

        if pixel_values is None and image_embeds is None:
            return None

        # TODO: refine
        if isinstance(pixel_values, list):
            pixel_values = torch.cat(pixel_values, dim=0)
        if len(pixel_values.shape) == 3:
            last_dim = pixel_values.shape[-1]
            pixel_values = pixel_values.reshape(-1, last_dim)
            image_grid_thw = image_grid_thw.reshape(-1, 3)

        if pixel_values is not None:
            return HunYuanVLImagePixelInputs(
                type="pixel_values",
                pixel_values=pixel_values,
                image_grid_thw=image_grid_thw,
            )

        if image_embeds is not None:
            return HunYuanVLImageEmbeddingInputs(
                type="image_embeds",
                image_embeds=image_embeds,
                image_grid_thw=image_grid_thw,
            )

    def_process_image_input(
        self, image_input: HunYuanVLImageInputs
    ) -> tuple[torch.Tensor, ...]:
        grid_thw = image_input["image_grid_thw"]
        assert grid_thw.ndim == 2
        grid_thw_list = grid_thw.tolist()

        if image_input["type"] == "image_embeds":
            image_embeds = image_input["image_embeds"].type(self.visual.dtype)
        else:
            pixel_values = image_input["pixel_values"]

            # TODO: use_data_parallel (split image_embeds in visual)
            image_embeds = self.visual(pixel_values, grid_thw=grid_thw_list)

        return image_embeds

    def_parse_and_validate_multimodal_inputs(self, **kwargs: object) -> dict:
        mm_input_by_modality = {}

        # Preserve the order of modalities if there are multiple of them
        # from the order of kwargs.
        for input_key in kwargs:
            if (
                input_key in ("pixel_values", "image_embeds")
                and "image" not in mm_input_by_modality
            ):
                mm_input_by_modality["image"] = self._parse_and_validate_image_input(
                    **kwargs
                )
        return mm_input_by_modality

    defembed_multimodal(self, **kwargs: object) -> MultiModalEmbeddings:
        mm_input_by_modality = self._parse_and_validate_multimodal_inputs(**kwargs)
        if not mm_input_by_modality:
            return []

        # The result multimodal_embeddings is tuple of tensors, with each
        # tensor correspoending to a multimodal data item (image or video).
        multimodal_embeddings: tuple[torch.Tensor, ...] = ()

        # NOTE: It is important to iterate over the keys in this dictionary
        # to preserve the order of the modalities.
        for modality in mm_input_by_modality:
            multimodal_input = mm_input_by_modality[modality]
            if modality == "image":
                image_embeddings = self._process_image_input(multimodal_input)
                multimodal_embeddings += tuple(image_embeddings)
        return multimodal_embeddings

    defforward(
        self,
        input_ids: torch.Tensor | None,
        positions: torch.Tensor,
        intermediate_tensors: IntermediateTensors | None,
        inputs_embeds: torch.Tensor | None,
        **kwargs: object,
    ) -> torch.Tensor | IntermediateTensors:
        if intermediate_tensors is not None:
            inputs_embeds = None

        hidden_states = self.language_model(
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

    defload_weights(self, weights: Iterable[tuple[str, torch.Tensor]]) -> set[str]:
        loader = AutoWeightsLoader(
            self,
            skip_prefixes=(["lm_head."] if self.config.tie_word_embeddings else None),
        )
        return loader.load_weights(weights, mapper=self.hf_to_vllm_mapper)

    defget_mm_mapping(self) -> MultiModelKeys:
"""
        Get the module prefix in multimodal models
        """
        return MultiModelKeys.from_string_field(
            language_model="language_model.model",
            connector="visual.perceive",
            tower_model="visual",
        )
```