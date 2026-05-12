---
title: openpangu_vl - vLLM
url: https://docs.vllm.ai/en/latest/api/vllm/model_executor/models/openpangu_vl/
source: sitemap
fetched_at: 2026-05-07T21:32:23.994083246-03:00
rendered_js: false
word_count: 0
summary: This document defines the PyTorch model implementation for OpenPangu-VL, providing logic for multimodal input validation, input embedding, and integration with the vLLM framework.
tags:
    - multimodal
    - vllm
    - model-integration
    - pytorch
    - vision-transformer
    - tensor-processing
category: api
---

```
@MULTIMODAL_REGISTRY.register_processor(
    OpenPanguVLMultiModalProcessor,
    info=OpenPanguVLProcessingInfo,
    dummy_inputs=OpenPanguVLDummyInputsBuilder,
)
classOpenPanguVLForConditionalGeneration(
    nn.Module, SupportsMultiModal, SupportsLoRA, SupportsPP, SupportsMRoPE
):
    hf_to_vllm_mapper = WeightsMapper(
        orig_to_new_prefix={
            "model.language_model.": "language_model.model.",
            "model.visual.": "visual.",
            "lm_head.": "language_model.lm_head.",
            "model.": "language_model.model.",
        }
    )
    packed_modules_mapping = {
        "qkv_proj": ["q_proj", "k_proj", "v_proj"],
        "gate_up_proj": ["gate_proj", "up_proj"],
    }

    def__init__(self, *, vllm_config: VllmConfig, prefix: str = ""):
        super().__init__()
        config = vllm_config.model_config.hf_config
        self.config = config
        self.vllm_config = vllm_config
        quant_config = vllm_config.quant_config

        with self._mark_tower_model(vllm_config, {"image", "video"}):
            self.visual = OpenPanguVisionTransformer(
                vision_config=config.vision_config,
                out_hidden_size=config.vision_config.out_hidden_size,
                hidden_size=config.hidden_size,
                norm_eps=getattr(config.vision_config, "rms_norm_eps", 1e-6),
                quant_config=self._maybe_ignore_quant_config(quant_config),
                prefix=maybe_prefix(prefix, "visual"),
            )

        with self._mark_language_model(vllm_config):
            self.language_model = init_vllm_registered_model(
                vllm_config=vllm_config,
                prefix=maybe_prefix("openpangu", "language_model"),
                architectures=["PanguEmbeddedForCausalLM"],
            )

        self.make_empty_intermediate_tensors = (
            self.language_model.make_empty_intermediate_tensors
        )
        self._parse_preprocess_params(config.vision_config)

    def_parse_preprocess_params(self, vision_config):
        self.channel = vision_config.in_channels
        self.patch_size = vision_config.patch_size
        fromvllm.multimodalimport MULTIMODAL_REGISTRY

        image_processor = (
            MULTIMODAL_REGISTRY.create_processor(self.vllm_config.model_config)
            .info.get_hf_processor()
            .image_processor
        )
        self.do_rescale = image_processor.do_rescale
        self.rescale_factor = image_processor.rescale_factor
        self.do_normalize = image_processor.do_normalize
        self.image_mean = tuple(image_processor.image_mean)
        self.image_std = tuple(image_processor.image_std)

    def_maybe_ignore_quant_config(self, quant_config: QuantizationConfig):
        if isinstance(quant_config, (GPTQConfig, GPTQMarlinConfig)):
            return None
        return quant_config

    def_validate_and_reshape_mm_tensor(
        self, mm_input: object, name: str
    ) -> torch.Tensor:
        if not isinstance(mm_input, (torch.Tensor, list)):
            raise ValueError(f"Incorrect type of {name}. Got type: {type(mm_input)}")
        if isinstance(mm_input, torch.Tensor):
            if mm_input.ndim == 2:
                return mm_input
            if mm_input.ndim != 3:
                raise ValueError(
                    f"{name} should be 2D or batched 3D tensor. "
                    f"Got ndim: {mm_input.ndim} "
                    f"(shape={mm_input.shape})"
                )
            return torch.concat(list(mm_input))
        else:
            return torch.concat(mm_input)

    def_parse_and_validate_image_input(self, **kwargs: object):
        pixel_values = kwargs.pop("pixel_values", None)
        image_embeds = kwargs.pop("image_embeds", None)
        image_grid_thw = kwargs.pop("image_grid_thw", None)

        if pixel_values is None and image_embeds is None:
            return None

        if pixel_values is not None:
            pixel_values = self._validate_and_reshape_mm_tensor(
                pixel_values, "image pixel values"
            )
            image_grid_thw = self._validate_and_reshape_mm_tensor(
                image_grid_thw, "image grid_thw"
            )

            if not isinstance(pixel_values, (torch.Tensor, list)):
                raise ValueError(
                    "Incorrect type of image pixel values. "
                    f"Got type: {type(pixel_values)}"
                )

            return OpenPanguVLImagePixelInputs(
                type="pixel_values",
                pixel_values=pixel_values,
                image_grid_thw=image_grid_thw,
            )

        if image_embeds is not None:
            image_embeds = self._validate_and_reshape_mm_tensor(
                image_embeds, "image embeds"
            )
            image_grid_thw = self._validate_and_reshape_mm_tensor(
                image_grid_thw, "image grid_thw"
            )

            if not isinstance(image_embeds, torch.Tensor):
                raise ValueError(
                    "Incorrect type of image embeddings. "
                    f"Got type: {type(image_embeds)}"
                )
            return OpenPanguVLImageEmbeddingInputs(
                type="image_embeds",
                image_embeds=image_embeds,
                image_grid_thw=image_grid_thw,
            )

    def_parse_and_validate_video_input(self, **kwargs: object):
        pixel_values_videos = kwargs.pop("pixel_values_videos", None)
        video_embeds = kwargs.pop("video_embeds", None)
        video_grid_thw = kwargs.pop("video_grid_thw", None)

        if pixel_values_videos is None and video_embeds is None:
            return None

        if pixel_values_videos is not None:
            pixel_values_videos = self._validate_and_reshape_mm_tensor(
                pixel_values_videos, "video pixel values"
            )
            video_grid_thw = self._validate_and_reshape_mm_tensor(
                video_grid_thw, "video grid_thw"
            )

            return OpenPanguVLVideoPixelInputs(
                type="pixel_values_videos",
                pixel_values_videos=pixel_values_videos,
                video_grid_thw=video_grid_thw,
            )

        if video_embeds is not None:
            video_embeds = self._validate_and_reshape_mm_tensor(
                video_embeds, "video embeds"
            )
            video_grid_thw = self._validate_and_reshape_mm_tensor(
                video_grid_thw, "video grid_thw"
            )

            if not isinstance(video_embeds, torch.Tensor):
                raise ValueError(
                    "Incorrect type of video embeddings. "
                    f"Got type: {type(video_embeds)}"
                )
            return OpenPanguVLVideoEmbeddingInputs(
                type="video_embeds",
                video_embeds=video_embeds,
                video_grid_thw=video_grid_thw,
            )

    def_parse_and_validate_multimodal_inputs(self, **kwargs: object) -> dict:
        mm_input_by_modality = {}
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

        multimodal_embeddings: tuple[torch.Tensor, ...] = ()

        for modality in mm_input_by_modality:
            multimodal_input = mm_input_by_modality[modality]
            if modality == "image":
                vision_embeddings = self._process_image_input(multimodal_input)
                multimodal_embeddings = (
                    multimodal_embeddings
                    if not vision_embeddings
                    else (multimodal_embeddings + vision_embeddings)
                )
            if modality == "video":
                video_embeddings = self._process_video_input(multimodal_input)
                multimodal_embeddings = (
                    multimodal_embeddings
                    if not video_embeddings
                    else (multimodal_embeddings + video_embeddings)
                )
        return multimodal_embeddings

    defget_input_embeddings(
        self,
        input_ids: torch.Tensor,
        multimodal_embeddings=None,
    ) -> torch.Tensor:
        inputs_embeds = self.language_model.embed_input_ids(input_ids)
        if multimodal_embeddings is not None:
            inputs_embeds = self.embed_input_ids(
                input_ids,
                inputs_embeds,
                multimodal_embeddings,
                [self.config.image_token_id, self.config.video_token_id],
            )
        return inputs_embeds

    def_process_image_input(self, image_input) -> tuple[torch.Tensor, ...]:
        grid_thw = image_input["image_grid_thw"]
        if grid_thw.ndim != 2:
            raise ValueError(f"grid_thw.ndim must be 2, but it is {grid_thw.ndim}")

        if image_input["type"] == "image_embeds":
            image_embeds = image_input["image_embeds"].type(self.visual.dtype)
        else:
            pixel_values = image_input["pixel_values"].type(self.visual.dtype)
            # rescale and normalize
            pixel_values = pixel_values.reshape(
                -1, self.channel, self.patch_size, self.patch_size
            )
            pixel_values = rescale_and_normalize(
                pixel_values,
                self.do_rescale,
                self.rescale_factor,
                self.do_normalize,
                self.image_mean,
                self.image_std,
            )
            pixel_values = pixel_values.reshape(
                -1, self.channel * self.patch_size * self.patch_size
            )
            image_embeds = self.visual(pixel_values, grid_thw=grid_thw)

        # Split concatenated embeddings for each image item.
        merge_size = self.visual.spatial_merge_size
        sizes = grid_thw.prod(-1) // merge_size // merge_size
        return image_embeds.split(sizes.tolist())

    def_process_video_input(self, video_input) -> torch.Tensor:
        grid_thw = video_input["video_grid_thw"]
        if grid_thw.ndim != 2:
            raise ValueError(f"grid_thw.ndim must be 2, but it is {grid_thw.ndim}")

        if video_input["type"] == "video_embeds":
            video_embeds = video_input["video_embeds"].type(self.visual.dtype)
        else:
            pixel_values_videos = video_input["pixel_values_videos"].type(
                self.visual.dtype
            )
            video_embeds = self.visual(pixel_values_videos, grid_thw=grid_thw)

        # Split concatenated embeddings for each video item.
        merge_size = self.visual.spatial_merge_size
        sizes = grid_thw.prod(-1) // merge_size // merge_size

        return video_embeds.split(sizes.tolist())

    defforward(
        self,
        input_ids: torch.Tensor,
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
        sampling_metadata=None,
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
            connector="visual.merger.",
            tower_model="visual.",
        )

    @classmethod
    defget_placeholder_str(cls, modality: str, i: int) -> str | None:
        if modality.startswith("image"):
            return "[unused18][unused19][unused20]"
        if modality.startswith("video"):
            return "[unused18][unused32][unused20]"

        raise ValueError("Only image or video modality is supported")

    defiter_mm_grid_thw(
        self, mm_features: list[MultiModalFeatureSpec]
    ) -> Iterator[tuple[str, int, int, int, int]]:
        spatial_merge_size = self.config.vision_config.spatial_merge_size
        for mm_feature in sorted(mm_features, key=lambda f: f.mm_position.offset):
            offset = mm_feature.mm_position.offset
            modality = mm_feature.modality
            if modality == "image":
                t, h, w = mm_feature.data["image_grid_thw"].data.tolist()
                assert t == 1, f"Image must have 1 frame, got {t}"
                yield (
                    modality,
                    offset,
                    1,
                    h // spatial_merge_size,
                    w // spatial_merge_size,
                )
            elif modality == "video":
                t, h, w = mm_feature.data["video_grid_thw"].data.tolist()
                yield (
                    modality,
                    offset,
                    t,
                    h // spatial_merge_size,
                    w // spatial_merge_size,
                )
            else:
                raise ValueError(f"Unsupported modality: {modality}")

    defget_mrope_input_positions(
        self,
        input_tokens: list[int],
        mm_features: list[MultiModalFeatureSpec],
    ) -> tuple[torch.Tensor, int]:
        llm_pos_ids_list: list = []
        st = 0

        for (
            modality,
            offset,
            llm_grid_t,
            llm_grid_h,
            llm_grid_w,
        ) in self.iter_mm_grid_thw(mm_features):
            text_len = offset - st
            st_idx = llm_pos_ids_list[-1].max() + 1 if len(llm_pos_ids_list) > 0 else 0
            llm_pos_ids_list.append(
                torch.arange(text_len).view(1, -1).expand(3, -1) + st_idx
            )
            if modality == "video":
                eot_bot_pos = torch.full((3, 1), 0, dtype=torch.long)
                offset_pos = max(llm_grid_h, llm_grid_w)
                current_pos = text_len + st_idx
                grid_h = (
                    torch.arange(llm_grid_h)
                    .view(-1, 1)
                    .expand(-1, llm_grid_w)
                    .flatten()
                )
                grid_w = (
                    torch.arange(llm_grid_w)
                    .view(1, -1)
                    .expand(llm_grid_h, -1)
                    .flatten()
                )
                frame_pos = torch.stack(
                    [
                        torch.full_like(grid_h, 0, dtype=torch.long),  # t
                        grid_h,  # h
                        grid_w,  # w
                    ]
                )
                llm_pos_ids_list.append(frame_pos + current_pos)
                for _ in range(llm_grid_t - 1):
                    current_pos = current_pos + offset_pos
                    llm_pos_ids_list.append(eot_bot_pos + current_pos)
                    llm_pos_ids_list.append(eot_bot_pos + current_pos + 1)
                    llm_pos_ids_list.append(frame_pos + current_pos + 2)
                    current_pos += 2
                st = (
                    offset + llm_grid_t * llm_grid_h * llm_grid_w + (llm_grid_t - 1) * 2
                )
            else:
                t_index = (
                    (
                        torch.arange(llm_grid_t)
                        .view(-1, 1)
                        .expand(-1, llm_grid_h * llm_grid_w)
                    )
                    .long()
                    .flatten()
                )
                h_index = (
                    torch.arange(llm_grid_h)
                    .view(1, -1, 1)
                    .expand(llm_grid_t, -1, llm_grid_w)
                    .flatten()
                )
                w_index = (
                    torch.arange(llm_grid_w)
                    .view(1, 1, -1)
                    .expand(llm_grid_t, llm_grid_h, -1)
                    .flatten()
                )
                llm_pos_ids_list.append(
                    torch.stack([t_index, h_index, w_index]) + text_len + st_idx
                )
                st = offset + llm_grid_t * llm_grid_h * llm_grid_w
        if st < len(input_tokens):
            st_idx = llm_pos_ids_list[-1].max() + 1 if len(llm_pos_ids_list) > 0 else 0
            text_len = len(input_tokens) - st
            llm_pos_ids_list.append(
                torch.arange(text_len).view(1, -1).expand(3, -1) + st_idx
            )
        llm_positions = torch.cat(llm_pos_ids_list, dim=1).reshape(3, -1)
        mrope_position_delta = (llm_positions.max() + 1 - len(input_tokens)).item()
        return llm_positions, mrope_position_delta
```