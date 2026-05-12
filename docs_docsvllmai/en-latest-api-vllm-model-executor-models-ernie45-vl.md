---
title: ernie45_vl - vLLM
url: https://docs.vllm.ai/en/latest/api/vllm/model_executor/models/ernie45_vl/
source: sitemap
fetched_at: 2026-05-07T21:29:50.041055339-03:00
rendered_js: false
word_count: 0
summary: This document defines the Ernie4_5_VLMoeForConditionalGeneration class, which integrates vision and language models within a multimodal inference framework, supporting specific token mapping, M-RoPE position calculation, and visual feature processing.
tags:
    - multimodal-model
    - vllm
    - pytorch
    - vision-transformer
    - mrope
    - inference
    - deep-learning
category: reference
---

```
@MULTIMODAL_REGISTRY.register_processor(
    Ernie4_5VLMultiModalProcessor,
    info=Ernie4_5_VLProcessingInfo,
    dummy_inputs=Ernie4_5_VLDummyInputsBuilder,
)
classErnie4_5_VLMoeForConditionalGeneration(
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

    # To ensure correct weight loading and mapping.
    hf_to_vllm_mapper = WeightsMapper(
        orig_to_new_prefix={
            "lm_head.": "language_model.lm_head.",
            "model.": "language_model.model.",
            # model.resampler_model.-> language_model.model.resampler_model.
            # language_model.model.resampler_model. -> resampler_model.
            "language_model.model.resampler_model.": "resampler_model.",
        },
        # resampler_weight_mappings
        orig_to_new_substr={
            "spatial_linear.0.": "spatial_linear1.",
            "spatial_linear.2.": "spatial_linear2.",
            "spatial_linear.3.": "spatial_norm.",
            "temporal_linear.0.": "temporal_linear1.",
            "temporal_linear.2.": "temporal_linear2.",
            "temporal_linear.3.": "temporal_norm.",
        },
    )

    @classmethod
    defget_placeholder_str(cls, modality: str, i: int) -> str | None:
        if modality.startswith("image"):
            return "<|IMAGE_START|><|image@placeholder|><|IMAGE_END|>"
        if modality.startswith("video"):
            return "<|VIDEO_START|><|video@placeholder|><|VIDEO_END|>"

        raise ValueError("Only image or video modality is supported")

    def__init__(self, vllm_config: VllmConfig, prefix: str = "") -> None:
        super().__init__()
        config = vllm_config.model_config.hf_config
        quant_config = vllm_config.quant_config
        multimodal_config = vllm_config.model_config.multimodal_config

        self.config = config
        self.multimodal_config = multimodal_config

        with self._mark_tower_model(vllm_config, {"image", "video"}):
            self.vision_model = Ernie4_5_VisionTransformer(
                config.vision_config,
                norm_eps=getattr(config, "rms_norm_eps", 1e-6),
                quant_config=quant_config,
                prefix=maybe_prefix(prefix, "vision_model"),
            )
            self.resampler_model = VariableResolutionResamplerModel(
                self.config.pixel_hidden_size,
                self.config.hidden_size,
                self.config.spatial_conv_size,
                self.config.temporal_conv_size,
                config=self.config,
                prefix=maybe_prefix(prefix, "resampler_model"),
            )

        with self._mark_language_model(vllm_config):
            self.language_model = Ernie4_5_VLMoeForCausalLM(
                vllm_config=vllm_config,
                prefix=maybe_prefix(prefix, "language_model"),
            )

        self.visual_token_mask = None
        self.make_empty_intermediate_tensors = (
            self.language_model.make_empty_intermediate_tensors
        )
        if getattr(self.config, "im_patch_id", None):
            visual_token_ids = [
                token_id
                for token_id in [
                    self.config.im_patch_id,
                    getattr(self.config, "image_start_token_id", None),
                    getattr(self.config, "image_end_token_id", None),
                    getattr(self.config, "video_start_token_id", None),
                    getattr(self.config, "video_end_token_id", None),
                ]
                if token_id is not None
            ]
            self._visual_token_ids_tensor_cache = torch.tensor(
                visual_token_ids, dtype=torch.long
            )
        else:
            self._visual_token_ids_tensor_cache = None

    defcompute_logits(
        self,
        hidden_states: torch.Tensor,
    ) -> torch.Tensor | None:
        return self.language_model.compute_logits(hidden_states)

    def_vision_forward(
        self,
        pixel_values: torch.Tensor,
        grid_thw: torch.Tensor,
    ) -> torch.Tensor:
        if grid_thw is not None:
            grid_thw = grid_thw[grid_thw > 0]
            if grid_thw.numel() % 3 != 0:
                raise ValueError(
                    f"grid_thw has {grid_thw.numel()} elements after filtering,"
                    "which is not divisible by 3."
                )
            grid_thw = grid_thw.reshape(-1, 3)
            # example: [[1,64,64],[2,80,80]] -> [[1,64,64],[1,80,80],[1,80,80]]
            grid_thw = F.pad(
                torch.repeat_interleave(grid_thw[:, 1:], grid_thw[:, 0], 0),
                [1, 0, 0, 0],
                value=1,
            )
        image_features = self.vision_model(pixel_values, grid_thw)
        return image_features

    def_set_visual_token_mask(self, input_ids: torch.Tensor) -> None:
"""Set mask for visual tokens (image/video patches and delimiters)."""
        if self._visual_token_ids_tensor_cache is None:
            self.visual_token_mask = None
            return
        # Create tensor on the correct device
        visual_token_ids_tensor = self._visual_token_ids_tensor_cache.to(
            device=input_ids.device,
            dtype=input_ids.dtype,
        )

        self.visual_token_mask = torch.isin(input_ids, visual_token_ids_tensor).reshape(
            -1, 1
        )

    defget_mrope_input_positions(
        self,
        input_tokens: list[int],
        mm_features: list[MultiModalFeatureSpec],
    ) -> tuple[torch.Tensor, int]:
        llm_pos_ids_list: list = []
        st = 0

        for (
            offset,
            llm_grid_t,
            llm_grid_h,
            llm_grid_w,
        ) in self.iter_mm_grid_thw(mm_features):
            text_len = offset - st
            st_idx = llm_pos_ids_list[-1].max() + 1 if len(llm_pos_ids_list) > 0 else 0
            llm_pos_ids_list.append(
                np.broadcast_to(np.arange(text_len), (3, text_len)) + st_idx
            )

            grid_indices = np.indices((llm_grid_t, llm_grid_h, llm_grid_w)).reshape(
                3, -1
            )
            llm_pos_ids_list.append(grid_indices + text_len + st_idx)
            st = offset + llm_grid_t * llm_grid_h * llm_grid_w

        if st < len(input_tokens):
            text_len = len(input_tokens) - st
            st_idx = llm_pos_ids_list[-1].max() + 1 if len(llm_pos_ids_list) > 0 else 0
            llm_pos_ids_list.append(
                np.broadcast_to(np.arange(text_len), (3, text_len)) + st_idx
            )

        llm_positions = np.concatenate(llm_pos_ids_list, axis=1).reshape(3, -1)
        mrope_position_delta = (llm_positions.max() + 1 - len(input_tokens)).item()
        return torch.from_numpy(llm_positions), mrope_position_delta

    defiter_mm_grid_thw(
        self, mm_features: list[MultiModalFeatureSpec]
    ) -> Iterator[tuple[int, int, int, int]]:
        spatial_conv_size = self.config.spatial_conv_size
        temporal_conv_size = self.config.temporal_conv_size

        for mm_feature in sorted(mm_features, key=lambda f: f.mm_position.offset):
            if mm_feature.data is None:
                raise ValueError("M-RoPE calculation requires multimodal feature data")

            offset = mm_feature.mm_position.offset
            if mm_feature.modality == "image":
                t, h, w = mm_feature.data["image_grid_thw"].data.tolist()
                yield offset, t, h // spatial_conv_size, w // spatial_conv_size
            elif mm_feature.modality == "video":
                t, h, w = mm_feature.data["video_grid_thw"].data.tolist()
                yield (
                    offset,
                    t // temporal_conv_size,
                    h // spatial_conv_size,
                    w // spatial_conv_size,
                )
            else:
                raise ValueError(f"Unsupported modality: {mm_feature.modality}")

    def_parse_and_validate_image_input(
        self, **kwargs: object
    ) -> Ernie4_5_VLImageInputs | None:
        pixel_values = kwargs.pop("pixel_values", None)
        image_grid_thw = kwargs.pop("image_grid_thw", None)

        if pixel_values is None:
            return None

        if pixel_values is not None:
            return Ernie4_5_VLImagePixelInputs(
                type="pixel_values",
                pixel_values=pixel_values,
                image_grid_thw=image_grid_thw,
            )

    def_parse_and_validate_video_input(
        self, **kwargs: object
    ) -> Ernie4_5_VLVideoInputs | None:
        pixel_values_videos = kwargs.pop("pixel_values_videos", None)
        video_grid_thw = kwargs.pop("video_grid_thw", None)

        if pixel_values_videos is None:
            return None

        if pixel_values_videos is not None:
            return Ernie4_5_VLVideoPixelInputs(
                type="pixel_values_videos",
                pixel_values_videos=pixel_values_videos,
                video_grid_thw=video_grid_thw,
            )

    def_process_image_input(
        self, image_input: Ernie4_5_VLImageInputs
    ) -> tuple[torch.Tensor, ...]:
        grid_thw = image_input["image_grid_thw"]
        assert grid_thw.ndim == 2

        pixel_values = image_input["pixel_values"].type(self.vision_model.dtype)
        image_features = self._vision_forward(
            pixel_values=pixel_values, grid_thw=grid_thw
        )
        image_embeds = self.resampler_model(image_features, grid_thw)

        merge_size = self.vision_model.spatial_merge_size
        sizes = grid_thw.prod(-1) // merge_size // merge_size

        return image_embeds.split(sizes.tolist())

    def_process_video_input(
        self, video_input: Ernie4_5_VLVideoInputs
    ) -> tuple[torch.Tensor, ...]:
        grid_thw = video_input["video_grid_thw"]
        assert grid_thw.ndim == 2

        pixel_values_videos = video_input["pixel_values_videos"].type(
            self.vision_model.dtype
        )
        video_features = self._vision_forward(
            pixel_values=pixel_values_videos, grid_thw=grid_thw
        )
        video_embeds = self.resampler_model(video_features, grid_thw)

        merge_size = self.vision_model.spatial_merge_size
        sizes = (
            (grid_thw.prod(-1) // self.config.temporal_conv_size)
            // merge_size
            // merge_size
        )

        return video_embeds.split(sizes.tolist())

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
            if (
                input_key in ("pixel_values_videos", "video_embeds")
                and "videos" not in modalities
            ):
                modalities["videos"] = self._parse_and_validate_video_input(**kwargs)

        return modalities

    defembed_multimodal(self, **kwargs: object) -> MultiModalEmbeddings | None:
        modalities = self._parse_and_validate_multimodal_inputs(**kwargs)
        if not modalities:
            return None

        # The result multimodal_embeddings is tuple of tensors, with each
        # tensor corresponding to a multimodal data item (image or video).
        multimodal_embeddings: tuple[torch.Tensor, ...] = ()

        # NOTE: It is important to iterate over the keys in this dictionary
        # to preserve the order of the modalities.
        for modality in modalities:
            if modality == "images":
                image_input = modalities["images"]
                image_embeddings = self._process_image_input(image_input)
                multimodal_embeddings += tuple(image_embeddings)
            if modality == "videos":
                video_input = modalities["videos"]
                video_embeddings = self._process_video_input(video_input)
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
        **kwargs,
    ):
        forward_kwargs = {
            "input_ids": input_ids,
            "positions": positions,
            "intermediate_tensors": intermediate_tensors,
            "inputs_embeds": inputs_embeds,
        }

        if self.visual_token_mask is not None:
            if self.visual_token_mask.shape[0] != inputs_embeds.shape[0]:
                padding_len = inputs_embeds.shape[0] - self.visual_token_mask.shape[0]
                # right pad False
                pad = torch.zeros(
                    (padding_len, self.visual_token_mask.shape[1]),
                    dtype=self.visual_token_mask.dtype,
                    device=self.visual_token_mask.device,
                )
                self.visual_token_mask = torch.cat([self.visual_token_mask, pad], dim=0)

            forward_kwargs.update({"visual_token_mask": self.visual_token_mask})
            self.visual_token_mask = None

        hidden_states = self.language_model.model(
            **forward_kwargs,
            **kwargs,
        )

        return hidden_states

    defload_weights(self, weights: Iterable[tuple[str, torch.Tensor]]) -> set[str]:
        loader = AutoWeightsLoader(self)
        return loader.load_weights(weights, mapper=self.hf_to_vllm_mapper)
```