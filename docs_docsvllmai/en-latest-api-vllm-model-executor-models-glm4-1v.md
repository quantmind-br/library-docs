---
title: glm4_1v - vLLM
url: https://docs.vllm.ai/en/latest/api/vllm/model_executor/models/glm4_1v/
source: sitemap
fetched_at: 2026-05-07T21:30:20.968836921-03:00
rendered_js: false
word_count: 397
summary: This document defines the Glm4vForConditionalGeneration class, which integrates GLM-4.1V and GLM-4.6V vision-language models into the vLLM framework, providing functionality for processing image and video inputs.
tags:
    - vllm
    - glm-4
    - multimodal
    - vision-encoder
    - model-architecture
    - inference
category: reference
---

Inference-only GLM-4.1V & GLM-4.6V-Flash, AutoGLM-Phone-9B model compatible with HuggingFace weights.

## Glm4vForConditionalGeneration [¶](#vllm.model_executor.models.glm4_1v.Glm4vForConditionalGeneration "Permanent link")

Bases: `Module`, `SupportsMultiModal`, `SupportsLoRA`, `SupportsPP`, `SupportsMRoPE`

Source code in `vllm/model_executor/models/glm4_1v.py`

```
@MULTIMODAL_REGISTRY.register_processor(
    Glm4vMultiModalProcessor,
    info=Glm4vProcessingInfo,
    dummy_inputs=Glm4vDummyInputsBuilder,
)
classGlm4vForConditionalGeneration(
    nn.Module, SupportsMultiModal, SupportsLoRA, SupportsPP, SupportsMRoPE
):
    packed_modules_mapping = {
        "qkv_proj": [
            "q_proj",
            "k_proj",
            "v_proj",
        ],
        "gate_up_proj": ["gate_up_proj"],
    }

    # To ensure correct weight loading and mapping.
    hf_to_vllm_mapper = WeightsMapper(
        orig_to_new_prefix={
            "lm_head.": "language_model.lm_head.",
            "model.language_model.": "language_model.model.",
            "model.visual.": "visual.",
        }
    )

    supports_encoder_tp_data = True

    @classmethod
    defget_placeholder_str(cls, modality: str, i: int) -> str | None:
        if modality.startswith("image"):
            return "<|begin_of_image|><|image|><|end_of_image|>"
        if modality.startswith("video"):
            return "<|begin_of_video|><|video|><|end_of_video|>"

        raise ValueError("Only image or video modality is supported")

    def__init__(self, *, vllm_config: VllmConfig, prefix: str = ""):
        super().__init__()
        config = vllm_config.model_config.hf_config
        quant_config = vllm_config.quant_config
        multimodal_config = vllm_config.model_config.multimodal_config

        self.config = config
        self.multimodal_config = multimodal_config
        self.use_data_parallel = multimodal_config.mm_encoder_tp_mode == "data"

        with self._mark_tower_model(vllm_config, {"image", "video"}):
            self.visual = Glm4vVisionTransformer(
                config.text_config,
                config.vision_config,
                norm_eps=getattr(config, "rms_norm_eps", 1e-5),
                quant_config=quant_config,
                prefix=maybe_prefix(prefix, "visual"),
            )

        if config.model_type in ("glm4v", "glm_ocr"):
            architectures = ["Glm4ForCausalLM"]
        elif config.model_type == "glm4v_moe":
            architectures = ["Glm4MoeForCausalLM"]
        else:
            architectures = None

        with self._mark_language_model(vllm_config):
            self.language_model = init_vllm_registered_model(
                vllm_config=vllm_config,
                hf_config=config.text_config,
                prefix=maybe_prefix(prefix, "language_model"),
                architectures=architectures,
            )

        self.make_empty_intermediate_tensors = (
            self.language_model.make_empty_intermediate_tensors
        )

    def_parse_and_validate_image_input(
        self, **kwargs: object
    ) -> Glm4vImageInputs | None:
        pixel_values = kwargs.pop("pixel_values", None)
        image_embeds = kwargs.pop("image_embeds", None)
        image_grid_thw = kwargs.pop("image_grid_thw", None)

        if pixel_values is None and image_embeds is None:
            return None

        if pixel_values is not None:
            return Glm4vImagePixelInputs(
                type="pixel_values",
                pixel_values=pixel_values,
                image_grid_thw=image_grid_thw,
            )

        if image_embeds is not None:
            return Glm4vImageEmbeddingInputs(
                type="image_embeds",
                image_embeds=image_embeds,
                image_grid_thw=image_grid_thw,
            )

    def_parse_and_validate_video_input(
        self, **kwargs: object
    ) -> Glm4vVideoInputs | None:
        pixel_values_videos = kwargs.pop("pixel_values_videos", None)
        video_embeds = kwargs.pop("video_embeds", None)
        video_grid_thw = kwargs.pop("video_grid_thw", None)

        if pixel_values_videos is None and video_embeds is None:
            return None

        if pixel_values_videos is not None:
            return Glm4vVideoPixelInputs(
                type="pixel_values_videos",
                pixel_values_videos=pixel_values_videos,
                video_grid_thw=video_grid_thw,
            )

        if video_embeds is not None:
            return Glm4vVideoEmbeddingInputs(
                type="video_embeds",
                video_embeds=video_embeds,
                video_grid_thw=video_grid_thw,
            )

    def_process_image_input(
        self, image_input: Glm4vImageInputs
    ) -> tuple[torch.Tensor, ...]:
        grid_thw = image_input["image_grid_thw"]
        assert grid_thw.ndim == 2

        if image_input["type"] == "image_embeds":
            image_embeds = image_input["image_embeds"].type(self.visual.dtype)
        else:
            pixel_values = image_input["pixel_values"].type(self.visual.dtype)
            if self.use_data_parallel:
                return run_dp_sharded_mrope_vision_model(
                    self.visual, pixel_values, grid_thw.tolist(), rope_type="rope_3d"
                )
            else:
                image_embeds = self.visual(pixel_values, grid_thw=grid_thw)

        merge_size = self.visual.spatial_merge_size
        sizes = (grid_thw.prod(-1) // merge_size // merge_size).tolist()
        return image_embeds.split(sizes)

    def_process_video_input(
        self, video_input: Glm4vVideoInputs
    ) -> tuple[torch.Tensor, ...]:
        grid_thw = video_input["video_grid_thw"]
        assert grid_thw.ndim == 2

        if video_input["type"] == "video_embeds":
            video_embeds = video_input["video_embeds"].type(self.visual.dtype)
        else:
            pixel_values_videos = video_input["pixel_values_videos"].type(
                self.visual.dtype
            )
            if self.use_data_parallel:
                return run_dp_sharded_mrope_vision_model(
                    self.visual,
                    pixel_values_videos,
                    grid_thw.tolist(),
                    rope_type="rope_3d",
                )
            else:
                video_embeds = self.visual(pixel_values_videos, grid_thw=grid_thw)

        # Split concatenated embeddings for each video item.
        merge_size = self.visual.spatial_merge_size
        sizes = (grid_thw.prod(-1) // merge_size // merge_size).tolist()
        return video_embeds.split(sizes)

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
            if (
                input_key in ("pixel_values_videos", "video_embeds")
                and "video" not in mm_input_by_modality
            ):
                mm_input_by_modality["video"] = self._parse_and_validate_video_input(
                    **kwargs
                )
        return mm_input_by_modality

    defembed_multimodal(self, **kwargs: object) -> MultiModalEmbeddings | None:
        mm_input_by_modality = self._parse_and_validate_multimodal_inputs(**kwargs)
        if not mm_input_by_modality:
            return None

        # The result multimodal_embeddings is tuple of tensors, with each
        # tensor corresponding to a multimodal data item (image or video).
        multimodal_embeddings: tuple[torch.Tensor, ...] = ()

        # NOTE: It is important to iterate over the keys in this dictionary
        # to preserve the order of the modalities.
        for modality in mm_input_by_modality:
            multimodal_input = mm_input_by_modality[modality]
            if modality == "image":
                image_embeddings = self._process_image_input(multimodal_input)
                multimodal_embeddings += tuple(image_embeddings)
            if modality == "video":
                video_embeddings = self._process_video_input(multimodal_input)
                multimodal_embeddings += tuple(video_embeddings)
        return multimodal_embeddings

    defiter_mm_grid_thw(
        self, mm_features: list[MultiModalFeatureSpec]
    ) -> Iterator[tuple[int, int, int, int]]:
        hf_config = self.config
        spatial_merge_size = hf_config.vision_config.spatial_merge_size
        for mm_feature in sorted(mm_features, key=lambda f: f.mm_position.offset):
            offset = mm_feature.mm_position.offset
            if mm_feature.modality == "image":
                t, h, w = mm_feature.data["image_grid_thw"].data.tolist()
                assert t == 1, f"Image must have 1 frame, got {t}"
                yield offset, t, h // spatial_merge_size, w // spatial_merge_size
            elif mm_feature.modality == "video":
                t, h, w = mm_feature.data["video_grid_thw"].data.tolist()
                yield (
                    offset,
                    t,
                    h // spatial_merge_size,
                    w // spatial_merge_size,
                )
            else:
                raise ValueError(f"Unsupported modality: {mm_feature.modality}")

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

    defforward(
        self,
        input_ids: torch.Tensor | None,
        positions: torch.Tensor,
        intermediate_tensors: IntermediateTensors | None = None,
        inputs_embeds: torch.Tensor | None = None,
        **kwargs: object,
    ) -> torch.Tensor | IntermediateTensors:
"""Run forward pass for GLM-4V.

        Args:
            input_ids: Flattened (concatenated) input_ids corresponding to a
                batch.
            positions: Flattened (concatenated) position ids corresponding to a
                batch.
                **NOTE**: If mrope is enabled (default setting for GLM-4V
                opensource models), the shape will be `(3, seq_len)`,
                otherwise it will be `(seq_len,).
            intermediate_tensors: Optional intermediate tensors for pipeline
                parallelism.
            inputs_embeds: Optional pre-computed input embeddings.
            **kwargs: Additional keyword arguments.
        """
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

    defload_weights(self, weights: Iterable[tuple[str, torch.Tensor]]) -> set[str]:
        loader = AutoWeightsLoader(self)
        return loader.load_weights(weights, mapper=self.hf_to_vllm_mapper)

    defget_mm_mapping(self) -> MultiModelKeys:
"""
        Get the module prefix in multimodal models
        """
        return MultiModelKeys.from_string_field(
            language_model="language_model.model",
            connector="visual.merger.",
            tower_model="visual.",
        )

    defget_num_mm_encoder_tokens(
        self,
        num_image_tokens: int,
    ) -> int:
        merge_size = self.config.vision_config.spatial_merge_size
        return num_image_tokens * (merge_size**2)

    defget_num_mm_connector_tokens(
        self,
        num_vision_tokens: int,
    ) -> int:
        merge_size = self.config.vision_config.spatial_merge_size
        return num_vision_tokens // (merge_size**2)
```

### forward [¶](#vllm.model_executor.models.glm4_1v.Glm4vForConditionalGeneration.forward "Permanent link")

Run forward pass for GLM-4V.

Parameters:

Name Type Description Default `input_ids` `Tensor | None`

Flattened (concatenated) input\_ids corresponding to a batch.

*required* `positions` `Tensor`

Flattened (concatenated) position ids corresponding to a batch. **NOTE**: If mrope is enabled (default setting for GLM-4V opensource models), the shape will be `(3, seq_len)`, otherwise it will be \`(seq\_len,).

*required* `intermediate_tensors` `IntermediateTensors | None`

Optional intermediate tensors for pipeline parallelism.

`None` `inputs_embeds` `Tensor | None`

Optional pre-computed input embeddings.

`None` `**kwargs` `object`

Additional keyword arguments.

`{}`

Source code in `vllm/model_executor/models/glm4_1v.py`

```
defforward(
    self,
    input_ids: torch.Tensor | None,
    positions: torch.Tensor,
    intermediate_tensors: IntermediateTensors | None = None,
    inputs_embeds: torch.Tensor | None = None,
    **kwargs: object,
) -> torch.Tensor | IntermediateTensors:
"""Run forward pass for GLM-4V.

    Args:
        input_ids: Flattened (concatenated) input_ids corresponding to a
            batch.
        positions: Flattened (concatenated) position ids corresponding to a
            batch.
            **NOTE**: If mrope is enabled (default setting for GLM-4V
            opensource models), the shape will be `(3, seq_len)`,
            otherwise it will be `(seq_len,).
        intermediate_tensors: Optional intermediate tensors for pipeline
            parallelism.
        inputs_embeds: Optional pre-computed input embeddings.
        **kwargs: Additional keyword arguments.
    """
    if intermediate_tensors is not None:
        inputs_embeds = None

    hidden_states = self.language_model.model(
        input_ids=input_ids,
        positions=positions,
        intermediate_tensors=intermediate_tensors,
        inputs_embeds=inputs_embeds,
    )
    return hidden_states
```

### get\_mm\_mapping [¶](#vllm.model_executor.models.glm4_1v.Glm4vForConditionalGeneration.get_mm_mapping "Permanent link")

```
get_mm_mapping() -> MultiModelKeys
```

Get the module prefix in multimodal models

Source code in `vllm/model_executor/models/glm4_1v.py`

```
defget_mm_mapping(self) -> MultiModelKeys:
"""
    Get the module prefix in multimodal models
    """
    return MultiModelKeys.from_string_field(
        language_model="language_model.model",
        connector="visual.merger.",
        tower_model="visual.",
    )
```

## Glm4vImageEmbeddingInputs [¶](#vllm.model_executor.models.glm4_1v.Glm4vImageEmbeddingInputs "Permanent link")

Bases: `TensorSchema`

Dimensions

- f: Number of image features (varies based on image resolution)
- h: Hidden size (must match language model backbone)
- n: Number of images
- g: Grid dimensions (3 for grid\_t, grid\_h, grid\_w)

Source code in `vllm/model_executor/models/glm4_1v.py`

```
classGlm4vImageEmbeddingInputs(TensorSchema):
"""
    Dimensions:
        - f: Number of image features (varies based on image resolution)
        - h: Hidden size (must match language model backbone)
        - n: Number of images
        - g: Grid dimensions (3 for grid_t, grid_h, grid_w)
    """

    type: Literal["image_embeds"] = "image_embeds"

    image_embeds: Annotated[torch.Tensor, TensorShape("f", "h")]
    image_grid_thw: Annotated[torch.Tensor, TensorShape("n", 3)]
```

## Glm4vImagePixelInputs [¶](#vllm.model_executor.models.glm4_1v.Glm4vImagePixelInputs "Permanent link")

Bases: `TensorSchema`

Dimensions

- np: Number of patches
- cpp: Number of channels * patch\_size * patch\_size
- ni: Number of images
- g: Grid dimensions (3 for grid\_t, grid\_h, grid\_w)

Source code in `vllm/model_executor/models/glm4_1v.py`

```
classGlm4vImagePixelInputs(TensorSchema):
"""
    Dimensions:
        - np: Number of patches
        - cpp: Number of channels * patch_size * patch_size
        - ni: Number of images
        - g: Grid dimensions (3 for grid_t, grid_h, grid_w)
    """

    type: Literal["pixel_values"] = "pixel_values"

    pixel_values: Annotated[torch.Tensor, TensorShape("np", "cpp")]
    image_grid_thw: Annotated[torch.Tensor, TensorShape("ni", 3)]
```

## Glm4vProcessingInfo [¶](#vllm.model_executor.models.glm4_1v.Glm4vProcessingInfo "Permanent link")

Bases: `BaseProcessingInfo`

Source code in `vllm/model_executor/models/glm4_1v.py`

```
classGlm4vProcessingInfo(BaseProcessingInfo):
    defget_supported_mm_limits(self) -> Mapping[str, int | None]:
        return {"image": None, "video": 1}

    defget_image_processor(self, **kwargs: object) -> Glm4vImageProcessor:
        return self.get_hf_processor(**kwargs).image_processor

    defget_video_processor(self, **kwargs: object) -> Glm4vVideoProcessor:
        return self.get_hf_processor(**kwargs).video_processor

    defget_data_parser(self):
        return MultiModalDataParser(
            video_needs_metadata=True,
            expected_hidden_size=self._get_expected_hidden_size(),
        )

    def_get_vision_info(
        self,
        *,
        image_width: int,
        image_height: int,
        num_frames: int = 16,
        do_resize: bool = True,
        max_image_pixels: int = 28 * 28 * 2 * 30000,
    ) -> tuple[ImageSize, int]:
        hf_config = self.get_hf_config()
        vision_config = hf_config.vision_config
        patch_size = vision_config.patch_size
        merge_size = vision_config.spatial_merge_size
        temporal_patch_size = vision_config.temporal_patch_size
        if do_resize:
            resized_height, resized_width = smart_resize(
                num_frames=num_frames
                if num_frames > temporal_patch_size
                else temporal_patch_size,
                height=image_height,
                width=image_width,
                factor=patch_size * merge_size,
                max_pixels=max_image_pixels,
            )
            preprocessed_size = ImageSize(width=resized_width, height=resized_height)
        else:
            preprocessed_size = ImageSize(width=image_width, height=image_height)

        # NOTE: Frames are padded to be divisible by `temporal_patch_size`
        # https://github.com/huggingface/transformers/blob/v4.48.3/src/transformers/models/qwen2_vl/image_processing_qwen2_vl.py#L294
        padded_num_frames = num_frames + num_frames % temporal_patch_size

        grid_t = max(padded_num_frames // temporal_patch_size, 1)
        grid_h = preprocessed_size.height // patch_size
        grid_w = preprocessed_size.width // patch_size

        num_patches = grid_t * grid_h * grid_w
        num_vision_tokens = num_patches // (merge_size**2)

        return preprocessed_size, num_vision_tokens

    def_get_image_max_pixels(self) -> int:
"""Read max_pixels from the HF image processor config.

        Despite the name, ``longest_edge`` is a pixel **area** (total pixel
        count), not an edge length.  The HF processor passes it directly to
        ``smart_resize`` as the ``max_pixels`` argument, which constrains
        ``t_bar * h_bar * w_bar <= max_pixels``.
        """
        return self.get_image_processor().size["longest_edge"]

    defget_image_size_with_most_features(self) -> ImageSize:
        # Use num_frames=1 for single-image budget estimation.
        # _get_vision_info defaults to num_frames=16 (video), which
        # makes smart_resize constrain 16*H*W <= max_pixels, vastly
        # underestimating the spatial budget for a single image and
        # causing encoder cache overflow for large images
        # (see https://github.com/vllm-project/vllm/issues/34040).
        max_image_size, _ = self._get_vision_info(
            image_width=9999999,
            image_height=9999999,
            num_frames=1,
            max_image_pixels=self._get_image_max_pixels(),
        )
        return max_image_size

    defget_num_image_tokens(
        self,
        *,
        image_width: int,
        image_height: int,
    ) -> int:
        _, num_image_tokens = self._get_vision_info(
            image_width=image_width,
            image_height=image_height,
            num_frames=1,
            max_image_pixels=self._get_image_max_pixels(),
        )
        return num_image_tokens

    defget_max_image_tokens(self) -> int:
        target_width, target_height = self.get_image_size_with_most_features()

        return self.get_num_image_tokens(
            image_width=target_width,
            image_height=target_height,
        )

    defget_num_video_tokens(
        self,
        *,
        image_width: int,
        image_height: int,
        num_frames: int,
    ) -> int:
        _, num_video_tokens = self._get_vision_info(
            image_width=image_width,
            image_height=image_height,
            num_frames=num_frames,
            max_image_pixels=28 * 28 * 2 * 30000,
        )
        return num_video_tokens

    def_get_max_video_frames(self, max_tokens: int) -> int:
        target_width, target_height = self.get_image_size_with_most_features()

        num_frames = 0

        while True:
            next_num_frames = num_frames + 1
            next_max_tokens = self.get_num_video_tokens(
                image_width=target_width,
                image_height=target_height,
                num_frames=next_num_frames,
            )
            if next_max_tokens > max_tokens or next_max_tokens == 0:
                break

            num_frames = next_num_frames

        return num_frames

    defget_num_frames_with_most_features(
        self,
        seq_len: int,
        mm_counts: Mapping[str, int],
    ) -> int:
        max_images = mm_counts.get("image", 0)
        max_videos = mm_counts.get("video", 0)

        max_image_tokens = self.get_max_image_tokens() * max_images
        max_total_frames = self._get_max_video_frames(seq_len - max_image_tokens)
        max_frames_per_video = min(
            max_total_frames // max(max_videos, 1), _MAX_FRAMES_PER_VIDEO
        )

        return max(max_frames_per_video, 1)

    def_get_video_second_idx_glm4v(
        self, metadata: dict[str, Any], total_frames: int
    ) -> list[int]:
        video_processor = self.get_video_processor()

        video_fps = metadata.get("fps", video_processor.fps)
        meta_frames = metadata.get("total_num_frames", total_frames)
        max_frame_idx = meta_frames - 1
        duration = metadata.get("duration", round(max_frame_idx / video_fps) + 1)
        do_sample_frames = metadata["do_sample_frames"]
        if not do_sample_frames:
            frame_indices = metadata["frames_indices"]
        else:
            if duration <= video_processor.max_duration:
                n = int(math.floor(duration * video_processor.fps))
                frame_indices = [
                    min(
                        max_frame_idx,
                        int(math.ceil(i * video_fps / video_processor.fps)),
                    )
                    for i in range(n)
                ]
            else:
                num_samples = int(video_processor.max_duration * video_processor.fps)
                if num_samples >= meta_frames:
                    frame_indices = list(range(meta_frames))
                else:
                    target_seconds = np.linspace(
                        0, duration, num_samples, endpoint=True
                    )
                    frame_indices = [
                        min(max_frame_idx, int(math.ceil(t * video_fps)))
                        for t in target_seconds
                    ]

        seen, uniq = set(), []
        for idx in frame_indices:
            if idx not in seen:
                seen.add(idx)
                uniq.append(idx)
        if len(uniq) & 1:
            uniq.append(uniq[-1])
        frame_indices = uniq

        full_second_idxs = [int(idx / video_fps) for idx in frame_indices]
        timestamps_list = full_second_idxs[::2]
        selected_timestamps = []
        for idx in range(0, len(timestamps_list)):
            selected_timestamps.append(timestamps_list[idx])
        return selected_timestamps

    def_get_video_second_idx_glm46v(
        self, metadata: dict[str, Any], total_frames: int
    ) -> list[int]:
        video_processor = self.get_video_processor()

        video_fps = metadata["fps"]
        meta_frames = metadata.get("total_num_frames", total_frames)
        max_frame_idx = meta_frames - 1
        duration = metadata.get("duration", round(max_frame_idx / video_fps) + 1)

        do_sample_frames = metadata.get("do_sample_frames", True)
        if not do_sample_frames:
            frame_indices = metadata["frames_indices"]
        else:
            DYNAMIC_FPS_THRES = {30: 3, 300: 1, 2400: 0.5}
            MAX_FRAME_COUNT_DYNAMIC = 640
            MAX_DURATION = 2400

            effective_duration = min(duration, MAX_DURATION)
            if effective_duration <= 30:
                target_fps = DYNAMIC_FPS_THRES[30]
            elif effective_duration <= 300:
                target_fps = DYNAMIC_FPS_THRES[300]
            else:
                target_fps = DYNAMIC_FPS_THRES[2400]

            temporal_patch_size = getattr(video_processor, "temporal_patch_size", 1)
            extract_t = int(effective_duration * target_fps * temporal_patch_size)
            extract_t = min(extract_t, MAX_FRAME_COUNT_DYNAMIC)

            duration_per_frame = 1 / video_fps
            timestamps = [i * duration_per_frame for i in range(meta_frames)]
            max_second = int(duration)

            if meta_frames < extract_t:
                frame_indices = np.linspace(
                    0, meta_frames - 1, extract_t, dtype=int
                ).tolist()
            else:
                frame_indices = []
                current_second = 0.0
                inv_fps = 1 / (temporal_patch_size * target_fps)
                for frame_index in range(meta_frames):
                    if timestamps[frame_index] >= current_second:
                        current_second += inv_fps
                        frame_indices.append(frame_index)
                        if current_second >= max_second:
                            break

            if len(frame_indices) < extract_t:
                if len(frame_indices) == 0:
                    start, end = 0, max(meta_frames - 1, 0)
                else:
                    start, end = frame_indices[0], frame_indices[-1]
                frame_indices = np.linspace(start, end, extract_t, dtype=int).tolist()
            elif len(frame_indices) > extract_t:
                frame_indices = np.linspace(
                    0, meta_frames - 1, extract_t, dtype=int
                ).tolist()

        seen, uniq = set(), []
        for idx in frame_indices:
            if idx not in seen:
                seen.add(idx)
                uniq.append(idx)

        if len(uniq) & 1:
            uniq.append(uniq[-1])

        frame_indices = uniq
        full_second_idxs = [int(idx / video_fps) for idx in frame_indices]
        timestamps_list = full_second_idxs[::2]
        selected_timestamps = []
        for idx in range(len(timestamps_list)):
            selected_timestamps.append(timestamps_list[idx])
        return selected_timestamps

    def_construct_video_placeholder(
        self,
        video_array: np.ndarray,
        metadata: dict[str, Any],
        grid_thw: torch.Tensor,
    ) -> str:
        hf_processor = self.get_hf_processor()
        tokenizer = self.get_tokenizer()
        image_processor = hf_processor.image_processor

        hf_config = self.get_hf_config()
        boi_token_id = hf_config.image_start_token_id
        eoi_token_id = hf_config.image_end_token_id
        bov_token_id = hf_config.video_start_token_id
        eov_token_id = hf_config.video_end_token_id
        merge_length = image_processor.merge_size**2

        assert isinstance(grid_thw, torch.Tensor)
        timestamps = (
            self._get_video_second_idx_glm4v(metadata, len(video_array))
            if isinstance(hf_processor, Glm4vProcessor)
            else self._get_video_second_idx_glm46v(metadata, len(video_array))
        )

        timestamp_format = (
            "{}" if isinstance(hf_processor, Glm4vProcessor) else "{:.1f} seconds"
        )
        frames_idx_token = [
            tokenizer.encode(timestamp_format.format(i), add_special_tokens=False)
            for i in timestamps
        ]
        T, H, W = grid_thw
        num_tokens_per_frame = int(H * W) // merge_length
        placeholder = []
        placeholder.append(bov_token_id)
        for frame_idx in frames_idx_token:
            placeholder.append(boi_token_id)
            placeholder.extend([hf_processor.video_token_id] * num_tokens_per_frame)
            placeholder.append(eoi_token_id)
            placeholder.extend(frame_idx)
        placeholder.append(eov_token_id)

        return placeholder
```

### \_get\_image\_max\_pixels [¶](#vllm.model_executor.models.glm4_1v.Glm4vProcessingInfo._get_image_max_pixels "Permanent link")

```
_get_image_max_pixels() -> int
```

Read max\_pixels from the HF image processor config.

Despite the name, `longest_edge` is a pixel **area** (total pixel count), not an edge length. The HF processor passes it directly to `smart_resize` as the `max_pixels` argument, which constrains `t_bar * h_bar * w_bar <= max_pixels`.

Source code in `vllm/model_executor/models/glm4_1v.py`

```
def_get_image_max_pixels(self) -> int:
"""Read max_pixels from the HF image processor config.

    Despite the name, ``longest_edge`` is a pixel **area** (total pixel
    count), not an edge length.  The HF processor passes it directly to
    ``smart_resize`` as the ``max_pixels`` argument, which constrains
    ``t_bar * h_bar * w_bar <= max_pixels``.
    """
    return self.get_image_processor().size["longest_edge"]
```

## Glm4vVideoEmbeddingInputs [¶](#vllm.model_executor.models.glm4_1v.Glm4vVideoEmbeddingInputs "Permanent link")

Bases: `TensorSchema`

Dimensions

- p: Number of video patches across all frames
- h: Hidden size (must match language model backbone)
- f: Number of frames
- g: Grid dimensions (3 for grid\_t which is usually 1 for processed video, grid\_h, grid\_w)

Source code in `vllm/model_executor/models/glm4_1v.py`

```
classGlm4vVideoEmbeddingInputs(TensorSchema):
"""
    Dimensions:
        - p: Number of video patches across all frames
        - h: Hidden size (must match language model backbone)
        - f: Number of frames
        - g: Grid dimensions (3 for grid_t which is usually 1 for processed
          video, grid_h, grid_w)
    """

    type: Literal["video_embeds"] = "video_embeds"

    video_embeds: Annotated[torch.Tensor, TensorShape("p", "h")]
    video_grid_thw: Annotated[torch.Tensor, TensorShape("f", 3)]
```

## Glm4vVideoPixelInputs [¶](#vllm.model_executor.models.glm4_1v.Glm4vVideoPixelInputs "Permanent link")

Bases: `TensorSchema`

Dimensions

- np: Number of patches
- ctpp: Number of channels * temporal\_patch\_size * patch\_size * patch\_size
- f: Number of frames
- g: Grid dimensions (3 for grid\_t which is usually 1 for processed video, grid\_h, grid\_w)

Source code in `vllm/model_executor/models/glm4_1v.py`

```
classGlm4vVideoPixelInputs(TensorSchema):
"""
    Dimensions:
        - np: Number of patches
        - ctpp: Number of channels * temporal_patch_size *
            patch_size * patch_size
        - f: Number of frames
        - g: Grid dimensions (3 for grid_t which is usually 1 for processed
          video, grid_h, grid_w)
    """

    type: Literal["pixel_values_videos"] = "pixel_values_videos"

    pixel_values_videos: Annotated[torch.Tensor, TensorShape("np", "ctpp")]
    video_grid_thw: Annotated[torch.Tensor, TensorShape("f", 3)]
```

## all\_gather\_interleave [¶](#vllm.model_executor.models.glm4_1v.all_gather_interleave "Permanent link")

```
all_gather_interleave(
    local_tensor, hidden_size: int, tp_size: int
)
```

All-gather the input tensor interleavely across model parallel group.

Source code in `vllm/model_executor/models/glm4_1v.py`

```
defall_gather_interleave(local_tensor, hidden_size: int, tp_size: int):
"""All-gather the input tensor interleavely across model parallel group."""
    importtorch.distributedasdist

    gathered_tensors = [torch.zeros_like(local_tensor) for _ in range(tp_size)]
    dist.all_gather(
        gathered_tensors,
        local_tensor,
        group=parallel_state.get_tp_group().device_group,
    )

    gathered_tensors_split = [
        torch.split(tensor, hidden_size // tp_size, -1) for tensor in gathered_tensors
    ]
    ordered_tensors = [
        tensor for pair in zip(*gathered_tensors_split) for tensor in pair
    ]
    result_tensor = torch.cat(ordered_tensors, dim=-1)
    return result_tensor
```