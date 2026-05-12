---
title: interns1 - vLLM
url: https://docs.vllm.ai/en/latest/api/vllm/model_executor/models/interns1/
source: sitemap
fetched_at: 2026-05-07T21:30:59.138127145-03:00
rendered_js: false
word_count: 0
summary: This document defines the InternS1ForConditionalGeneration model class, which integrates vision and language processing components within a vLLM-compatible framework to support multimodal inference.
tags:
    - multimodal-model
    - vllm
    - interns1
    - vision-tower
    - neural-networks
    - pytorch
category: concept
---

```
@MULTIMODAL_REGISTRY.register_processor(
    InternS1MultiModalProcessor,
    info=InternS1ProcessingInfo,
    dummy_inputs=InternS1DummyInputsBuilder,
)
classInternS1ForConditionalGeneration(
    nn.Module, SupportsMultiModal, SupportsPP, SupportsLoRA
):
    # To ensure correct weight loading and mapping.
    hf_to_vllm_mapper = WeightsMapper(
        orig_to_new_prefix={
            "lm_head.": "language_model.lm_head.",
            "model.language_model.": "language_model.model.",
            "model.vision_tower.": "vision_tower.",
            "model.multi_modal_projector.": "multi_modal_projector.",
        }
    )

    @classmethod
    defget_placeholder_str(cls, modality: str, i: int) -> str | None:
        # transformers InternVLProcessor uses <IMG_CONTEXT> as the separator
        # refer to https://github.com/huggingface/transformers/blob/f90de364c2484c7c325bbe05befdcf487bd75b63/src/transformers/models/internvl/processing_internvl.py#L116
        if modality.startswith("image"):
            return "<IMG_CONTEXT>"
        if modality.startswith("video"):
            return "<video>"

        raise ValueError("Only image or video modality is supported")

    def__init__(self, *, vllm_config: VllmConfig, prefix: str = "") -> None:
        super().__init__()
        config = vllm_config.model_config.hf_config
        quant_config = vllm_config.quant_config
        multimodal_config = vllm_config.model_config.multimodal_config

        self.config = config
        self.multimodal_config = multimodal_config

        image_size = config.vision_config.image_size[0]
        patch_size = config.vision_config.patch_size[0]
        self.patch_size = patch_size
        self.num_image_token = int(
            (image_size // patch_size) ** 2 * (config.downsample_ratio**2)
        )
        self.downsample_ratio = config.downsample_ratio

        with self._mark_tower_model(vllm_config, {"image", "video"}):
            self.vision_tower = self._init_vision_model(
                config,
                quant_config=quant_config,
                prefix=maybe_prefix(prefix, "vision_tower"),
            )
            self.multi_modal_projector = self._init_mlp1(config)

        with self._mark_language_model(vllm_config):
            self.language_model = init_vllm_registered_model(
                vllm_config=vllm_config,
                hf_config=config.text_config,
                prefix=maybe_prefix(prefix, "language_model"),
            )

        self.img_context_token_id = None
        self.video_context_token_id = None

        self.visual_token_mask = None
        self.make_empty_intermediate_tensors = (
            self.language_model.make_empty_intermediate_tensors
        )

    def_init_vision_model(
        self,
        config: PretrainedConfig,
        quant_config: QuantizationConfig | None,
        *,
        prefix: str,
    ):
        num_hidden_layers = config.vision_config.num_hidden_layers
        return InternS1VisionModel(
            config.vision_config,
            quant_config=quant_config,
            num_hidden_layers_override=num_hidden_layers,
            prefix=prefix,
        )

    def_init_mlp1(self, config: PretrainedConfig) -> nn.Module:
        return InternS1MultiModalProjector(config)

    defpixel_shuffle(self, x, scale_factor=0.5):
        n, w, h, c = x.size()
        # N, W, H, C --> N, W, H * scale, C // scale
        x = x.view(n, w, int(h * scale_factor), int(c / scale_factor))
        # N, W, H * scale, C // scale --> N, H * scale, W, C // scale
        x = x.permute(0, 2, 1, 3).contiguous()
        x = x.view(
            n,
            int(h * scale_factor),
            int(w * scale_factor),
            int(c / (scale_factor * scale_factor)),
        )
        x = x.permute(0, 2, 1, 3).contiguous()
        return x

    defextract_feature(self, pixel_values: torch.Tensor) -> torch.Tensor:
        vit_embeds = self.vision_tower(pixel_values=pixel_values)
        vit_embeds = vit_embeds[:, 1:, :]

        h = w = int(vit_embeds.shape[1] ** 0.5)
        vit_embeds = vit_embeds.reshape(vit_embeds.shape[0], h, w, -1)
        vit_embeds = self.pixel_shuffle(vit_embeds, scale_factor=self.downsample_ratio)
        vit_embeds = vit_embeds.reshape(vit_embeds.shape[0], -1, vit_embeds.shape[-1])

        vit_embeds = self.multi_modal_projector(vit_embeds)
        return vit_embeds

    def_parse_and_validate_image_input(
        self, **kwargs: object
    ) -> InternS1ImageInputs | None:
        pixel_values = kwargs.pop("pixel_values", None)
        image_num_patches = kwargs.pop("image_num_patches", None)
        image_embeds = kwargs.pop("image_embeds", None)

        if pixel_values is None and image_embeds is None:
            return None

        if image_embeds is not None:
            return InternS1ImageEmbeddingInputs(
                type="image_embeds",
                data=image_embeds,
            )

        image_token_id = kwargs["image_token_id"]
        if isinstance(image_token_id, torch.Tensor):
            image_token_id = image_token_id.flatten().unique().item()

        assert isinstance(image_token_id, int)
        self.img_context_token_id = image_token_id

        if pixel_values is not None:
            h, w = self.config.vision_config.image_size
            return InternS1ImagePixelInputs(
                type="pixel_values",
                pixel_values=pixel_values,
                num_patches=image_num_patches,
                resolve_bindings={
                    "h": h,
                    "w": w,
                },
            )

        raise AssertionError("This line should be unreachable.")

    def_parse_and_validate_video_input(
        self, **kwargs: object
    ) -> InternS1VideoInputs | None:
        pixel_values_flat_video = kwargs.pop("pixel_values_videos", None)
        video_num_patches = kwargs.pop("video_num_patches", None)
        video_embeds = kwargs.pop("video_embeds", None)

        if pixel_values_flat_video is None and video_embeds is None:
            return None

        if video_embeds is not None:
            return InternS1VideoEmbeddingInputs(
                type="video_embeds",
                data=video_embeds,
            )

        video_token_id = kwargs["video_token_id"]
        if isinstance(video_token_id, torch.Tensor):
            video_token_id = video_token_id.flatten().unique().item()

        assert isinstance(video_token_id, int)
        self.video_context_token_id = video_token_id

        if pixel_values_flat_video is not None:
            h, w = self.config.vision_config.image_size
            return InternS1VideoPixelInputs(
                type="pixel_values_videos",
                num_patches=video_num_patches,
                pixel_values=pixel_values_flat_video,
                resolve_bindings={
                    "h": h,
                    "w": w,
                },
            )

        raise AssertionError("This line should be unreachable.")

    def_process_vision_input(
        self,
        image_input: InternS1ImageInputs | InternS1VideoInputs,
    ) -> tuple[torch.Tensor, ...]:
        if (
            image_input["type"] == "image_embeds"
            or image_input["type"] == "video_embeds"
        ):
            return image_input["data"]

        image_embeds = self.extract_feature(image_input["pixel_values"])

        num_patches = image_input["num_patches"]

        # Only one image in the current batch
        if len(num_patches) == 1:
            return (image_embeds.view(-1, self.config.text_config.hidden_size),)

        # NOTE: Image embeddings are split into separate tensors for each image
        # by the size of each embedding.
        feature_size = image_embeds.shape[1]
        image_embeds = image_embeds.view(-1, self.config.text_config.hidden_size)
        image_feature_sizes = [
            num_patches * feature_size for num_patches in num_patches
        ]
        return image_embeds.split(image_feature_sizes)

    def_parse_and_validate_multimodal_inputs(self, **kwargs: object) -> dict:
        modalities = {}

        # Preserve the order of modalities if there are multiple of them
        # from the order of kwargs.
        for input_key in kwargs:
            if (
                input_key in ("pixel_values", "image_embeds")
                and "images" not in modalities
            ):
                modalities["images"] = self._parse_and_validate_image_input(**kwargs)
            if input_key in ("pixel_values_videos",) and "videos" not in modalities:
                modalities["videos"] = self._parse_and_validate_video_input(**kwargs)

        return modalities

    def_set_visual_token_mask(self, input_ids: torch.Tensor) -> None:
        self.visual_token_mask = None

    defembed_multimodal(self, **kwargs: object) -> MultiModalEmbeddings:
        modalities = self._parse_and_validate_multimodal_inputs(**kwargs)
        if not modalities:
            return []

        # The result multimodal_embeddings is tuple of tensors, with each
        # tensor corresponding to a multimodal data item (image or video).
        multimodal_embeddings: tuple[torch.Tensor, ...] = ()

        # NOTE: It is important to iterate over the keys in this dictionary
        # to preserve the order of the modalities.
        for modality in modalities:
            if modality == "images":
                image_input = modalities["images"]
                image_embeddings = self._process_vision_input(image_input)
                multimodal_embeddings += tuple(image_embeddings)
            if modality == "videos":
                video_input = modalities["videos"]
                video_embeddings = self._process_vision_input(video_input)
                multimodal_embeddings += tuple(video_embeddings)

        return multimodal_embeddings

    defembed_input_ids(
        self,
        input_ids: torch.Tensor,
        multimodal_embeddings: MultiModalEmbeddings | None = None,
        *,
        is_multimodal: torch.Tensor | None = None,
    ) -> torch.Tensor:
        if multimodal_embeddings is not None and len(multimodal_embeddings) > 0:
            self._set_visual_token_mask(input_ids)

        # This is to satisfy the type checker for each overload
        if multimodal_embeddings is None or is_multimodal is None:
            return super().embed_input_ids(input_ids)

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

        forward_kwargs = {
            "input_ids": input_ids,
            "positions": positions,
            "intermediate_tensors": intermediate_tensors,
            "inputs_embeds": inputs_embeds,
        }

        hidden_states = self.language_model.model(**forward_kwargs)
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