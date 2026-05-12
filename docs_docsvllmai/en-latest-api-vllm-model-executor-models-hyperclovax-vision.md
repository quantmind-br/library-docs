---
title: hyperclovax_vision - vLLM
url: https://docs.vllm.ai/en/latest/api/vllm/model_executor/models/hyperclovax_vision/
source: sitemap
fetched_at: 2026-05-07T21:30:50.207623987-03:00
rendered_js: false
word_count: 0
summary: This document defines the architecture and multimodal integration logic for the HyperCLOVAX-SEED vision-language model within a vLLM-compatible framework.
tags:
    - vllm
    - vision-language-model
    - multimodal
    - pytorch
    - hyperclovax
    - deep-learning
    - model-architecture
category: api
---

```
@MULTIMODAL_REGISTRY.register_processor(
    HCXVisionMultiModalProcessor,
    info=HCXVisionProcessingInfo,
    dummy_inputs=HCXVisionDummyInputsBuilder,
)
classHCXVisionForCausalLM(nn.Module, SupportsMultiModal, SupportsPP):
"""
    HyperCLOVAX-SEED Vision-Language Model (V1 architecture).

    Supports:
    - HyperCLOVAX-SEED-Vision-Instruct-3B

    Uses CLIP/SigLIP as the vision encoder with C-Abstractor projector.
    """

    packed_modules_mapping = {
        "qkv_proj": ["q_proj", "k_proj", "v_proj"],
        "gate_up_proj": ["gate_proj", "up_proj"],
    }

    def__init__(
        self,
        *,
        vllm_config: VllmConfig,
        prefix: str = "",
    ) -> None:
        super().__init__()

        # init configs
        config = vllm_config.model_config.hf_config
        quant_config = vllm_config.quant_config
        # text_config
        text_config = config.text_config
        if text_config.model_type in ["gpt2", "hyperclovax", "llama"]:
            text_config._attn_implementation = "sdpa"
        if text_config.model_type != "hyperclovax":
            text_config.logits_scaling = 1.0
        # vision_config
        vision_config = config.vision_config
        vision_config.auto_map = {}
        vision_config.anyres = config.anyres
        vision_config.max_num_grids = config.max_num_grids
        self.dtype = vllm_config.model_config.dtype

        ## possible_resolution should be matched with preprocessor_config.json
        config.possible_resolutions = self._init_possible_resolutions(
            config, vision_config
        )

        with self._mark_tower_model(vllm_config, {"image", "video"}):
            self.vision_model = init_vision_tower_for_hcxvision(
                vision_config,
                quant_config=quant_config,
                use_nth_layer=getattr(config, "use_nth_layer", -1),
                require_post_norm=False,
                prefix=maybe_prefix(prefix, "vision_model"),
            )
            self.mm_projector = self._init_mm_projector(
                config, text_config, vision_config
            )

            if config.anyres:
                self.image_newline = nn.Parameter(
                    torch.empty(text_config.hidden_size, dtype=self.dtype)
                )

        with self._mark_language_model(vllm_config):
            self.language_model = init_vllm_registered_model(
                vllm_config=vllm_config,
                hf_config=text_config,
                prefix=maybe_prefix(prefix, "language_model"),
            )

        self.config = config
        self.vision_config = vision_config
        self.text_config = text_config

        self.make_empty_intermediate_tensors = (
            self.language_model.make_empty_intermediate_tensors
        )

    @classmethod
    defget_placeholder_str(cls, modality: str, i: int) -> str | None:
        if modality.startswith("image"):
            return IMAGE_TOKEN
        if modality.startswith("video"):
            return VIDEO_TOKEN

        raise ValueError("Only image or video modality is supported")

    def_parse_and_validate_image_input(
        self,
        **kwargs: object,
    ) -> HCXVisionImageInputs | None:
        pixel_values_images = kwargs.pop("pixel_values_images", None)

        if pixel_values_images is None:
            return None

        image_sizes_images = kwargs.pop("image_sizes_images")

        return HCXVisionImagePixelInputs(
            pixel_values_images=pixel_values_images,
            image_sizes_images=image_sizes_images,
        )

    def_parse_and_validate_video_input(
        self,
        **kwargs: object,
    ) -> HCXVisionVideoInputs | None:
        pixel_values_videos = kwargs.pop("pixel_values_videos", None)

        if pixel_values_videos is None:
            return None

        return HCXVisionVideoPixelInputs(
            pixel_values_videos=pixel_values_videos,
        )

    def_process_image_input(
        self,
        image_input: HCXVisionImageInputs,
    ) -> tuple[torch.Tensor, ...]:
        return self.forward_images(
            pixel_values_images=image_input["pixel_values_images"],
            image_sizes_images=image_input["image_sizes_images"],
        )

    def_process_video_input(
        self,
        video_input: HCXVisionVideoInputs,
    ) -> tuple[torch.Tensor, ...]:
        return self.forward_videos(
            pixel_values_videos=video_input["pixel_values_videos"],
        )

    def_parse_and_validate_multimodal_inputs(self, **kwargs: object) -> dict:
        modalities = {}

        # Preserve the order of modalities if there are multiple of them
        # from the order of kwargs.
        for input_key in kwargs:
            if input_key == "pixel_values_images" and "images" not in modalities:
                modalities["images"] = self._parse_and_validate_image_input(**kwargs)
            if input_key == "pixel_values_videos" and "videos" not in modalities:
                modalities["videos"] = self._parse_and_validate_video_input(**kwargs)

        return modalities

    defembed_multimodal(
        self,
        **kwargs: object,
    ) -> MultiModalEmbeddings:
        modalities = self._parse_and_validate_multimodal_inputs(**kwargs)
        if not modalities:
            return []

        # The result multimodal_embeddings is tuple of tensors, with each
        # tensor correspoending to a multimodal data item (image or video).
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
            input_ids, positions, intermediate_tensors, inputs_embeds=inputs_embeds
        )
        return hidden_states

    defforward_images(
        self,
        pixel_values_images: list[torch.Tensor],
        image_sizes_images: torch.Tensor,
    ) -> tuple[torch.Tensor, ...]:
        pixel_values_image_flat = flatten_bn(pixel_values_images, concat=True)

        visual_token_idx = 0 if "siglip" in self.vision_config.model_type else 1
        image_forward_outs = self.vision_model(pixel_values_image_flat)[
            :, visual_token_idx:
        ]

        image_forward_outs = image_forward_outs.to(dtype=self.mm_projector.dtype)
        image_forward_outs = self.mm_projector(image_forward_outs)  # b (h w) d

        split_sizes = [len(item) for item in pixel_values_images]
        image_forward_outs = torch.split(image_forward_outs, split_sizes, dim=0)

        # newline for anyres postprocessing
        image_features = anyres_postprocessing(
            image_forward_outs=image_forward_outs,
            image_sizes=image_sizes_images.tolist(),
            num_queries_vis_abstractor=self.config.num_queries_vis_abstractor_image,
            unpad=self.config.unpad,
            patch_size=self.vision_config.patch_size,
            grid_size=self.vision_config.image_size,
            image_newline=self.image_newline,
            possible_resolutions=self.config.possible_resolutions,
        )

        return tuple(image_features)

    defforward_videos(
        self,
        pixel_values_videos: list[list[torch.Tensor]],
    ) -> tuple[torch.Tensor, ...]:
        pixel_values_videos_flat = flatten_bn(
            [frame for frames in pixel_values_videos for frame in frames],
            concat=True,
        )

        visual_token_idx = 0 if "siglip" in self.vision_config.model_type else 1
        video_forward_outs = self.vision_model(pixel_values_videos_flat)[
            :, visual_token_idx:
        ]

        video_forward_outs = video_forward_outs.to(dtype=self.mm_projector.dtype)

        # Run MM-Projector
        # len(num_grids) == len(num_queries_vis_abstractors) + 1
        grid_idx = 0
        # e.g. [0, 9, 18, 19, 27, 28, 36, 37, 45, 46, 54, 55, 56]
        num_grids = [grid_idx]
        # e.g. [81, 81, 81, 9, 81, 9, 81, 9, 81, 9, 81, 9]
        num_queries_vis_abstractors = []
        len_total_frames = video_forward_outs.shape[0]

        if self.config.first_last_frames_slow:
            # slowfast (first_last_frames_slow)
            assert len_total_frames != 0
            if len_total_frames <= 2:
                num_queries_vis_abstractors.append(
                    self.config.num_queries_vis_abstractor_video_slow
                )
                grid_idx += len_total_frames
                num_grids.append(grid_idx)
            else:
                num_queries_vis_abstractors.append(
                    self.config.num_queries_vis_abstractor_video_slow
                )
                grid_idx += 1
                num_grids.append(grid_idx)

                num_queries_vis_abstractors.append(
                    self.config.num_queries_vis_abstractor_video_fast
                )
                grid_idx += len_total_frames - 2
                num_grids.append(grid_idx)

                num_queries_vis_abstractors.append(
                    self.config.num_queries_vis_abstractor_video_slow
                )
                grid_idx += 1
                num_grids.append(grid_idx)
        else:
            # slowfast
            for pixel_values_frames in pixel_values_videos:
                for pixel_values_frame in pixel_values_frames:
                    if len(pixel_values_frame) > 0:
                        num_queries_vis_abstractors.append(
                            self.config.num_queries_vis_abstractor_video_slow
                        )
                        grid_idx += 1
                        num_grids.append(grid_idx)
                        num_queries_vis_abstractors.append(
                            self.config.num_queries_vis_abstractor_video_fast
                        )
                        grid_idx = grid_idx + len(pixel_values_frame) - 1
                        num_grids.append(grid_idx)

        video_forward_outs = self.mm_projector(
            video_forward_outs, num_queries_vis_abstractors, num_grids
        )

        video_features = []  # what we want to return
        target_features = []
        target_group_size = 0
        group_counter = 0
        video_groups = [
            len(frame) for frames in pixel_values_videos for frame in frames
        ]  # for concat video features after projector

        for forward_out in video_forward_outs:
            target_group_size += len(forward_out)
            target_features.append(forward_out.flatten(0, 1))

            video_group_size = video_groups[group_counter]
            if video_group_size == target_group_size:
                video_features.append(torch.cat(target_features, dim=0))
                target_features = []
                group_counter += 1
                target_group_size = 0

            elif video_group_size < target_group_size:
                raise RuntimeError(f"{video_group_size=} < {target_group_size=}")

        assert len(target_features) == 0, (
            f"target_features is not empty!! {target_features}"
        )
        assert len(video_groups) == len(video_features)

        feats_per_video = [len(video) for video in pixel_values_videos]
        idxs_per_video = [0, *accumulate(feats_per_video)]
        return tuple(
            torch.cat(video_features[idxs_per_video[i] : idxs_per_video[i + 1]])
            for i in range(len(feats_per_video))
        )

    def_prepare_multimodal_kwargs(self, **kwargs: object):
        output = defaultdict(list)
        for k, v in kwargs.items():
            if len(v) < 1 or len(v[0]) < 1:
                continue  # if empty batch of empty sample

            new_k, is_video = k, False
            if not k.endswith("_images") and not k.endswith("_videos"):
                pass
            else:
                new_k, is_video = k.split("_")[:-1], k.split("_")[-1]
                new_k = "_".join(new_k)
                is_video = is_video == "videos"

            for _sample_idx, _v in enumerate(v):  # batch -> sample
                if new_k not in ["pixel_values"]:
                    if len(output[new_k]) < _sample_idx + 1:
                        output[new_k].append(list())
                    _v = _v.detach().cpu().numpy().tolist()
                    output[new_k][_sample_idx] += _v
                elif isinstance(_v, torch.Tensor):
                    if len(output[new_k]) < _sample_idx + 1:
                        output[new_k].append(list())
                        output["is_videos"].append(list())
                    _v = list(torch.unbind(_v, dim=0))
                    output[new_k][_sample_idx] += _v
                    output["is_videos"][_sample_idx] += [
                        is_video,
                    ] * len(_v)
        return dict(output)

    defcompute_logits(
        self,
        hidden_states: torch.Tensor,
    ) -> torch.Tensor | None:
        return self.language_model.compute_logits(hidden_states)

    defload_weights(
        self,
        weights: Iterable[tuple[str, torch.Tensor]],
    ) -> set[str]:
        loader = AutoWeightsLoader(self)
        return loader.load_weights(weights)

    def_init_possible_resolutions(
        self,
        config,
        vision_config,
    ):
        if not getattr(config, "possible_resolutions", []):
            possible_resolutions = []
            if config.anyres:
                assert config.max_num_grids > 0
                for i in range(1, config.max_num_grids + 1):
                    for j in range(1, config.max_num_grids + 1):
                        if i == 1 and j == 1 and not config.use_1x1_grid:
                            continue
                        if i * j <= config.max_num_grids:
                            possible_resolutions.append([i, j])

                possible_resolutions = [
                    [ys * vision_config.image_size, xs * vision_config.image_size]
                    for ys, xs in possible_resolutions
                ]
            return possible_resolutions
        else:
            return config.possible_resolutions

    def_init_mm_projector(
        self,
        config,
        text_config,
        vision_config,
    ):
        input_hidden_size = vision_config.hidden_size
        if config.mm_projector_type == "linear":
            mm_projector = nn.Linear(input_hidden_size, text_config.hidden_size)
            mm_projector.dtype = next(mm_projector.parameters()).dtype
        elif config.mm_projector_type == "cabstractor":
            mm_projector = HCXVisionCAbstractor(
                num_queries=config.num_queries_vis_abstractor_image,
                num_input_tokens=(vision_config.image_size // vision_config.patch_size)
                ** 2,
                encoder_hidden_size=input_hidden_size,
                hidden_size=input_hidden_size,
                output_hidden_size=text_config.hidden_size,
                pos_emb=config.proj_pos_emb,
                prenorm=config.proj_prenorm,
            )
        else:
            mm_projector = HCXVisionMlp(
                config.mm_projector_type,
                input_hidden_size,
                hidden_features=input_hidden_size,
                out_features=self.text_config.hidden_size,
            )
        return mm_projector
```