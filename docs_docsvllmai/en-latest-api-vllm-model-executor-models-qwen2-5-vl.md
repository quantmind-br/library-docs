---
title: qwen2_5_vl - vLLM
url: https://docs.vllm.ai/en/latest/api/vllm/model_executor/models/qwen2_5_vl/
source: sitemap
fetched_at: 2026-05-07T21:32:50.043197965-03:00
rendered_js: false
word_count: 16
summary: This document defines the Qwen2.5-VL model implementation within a vLLM framework, covering architectural setup, multimodal feature processing, and positional encoding logic.
tags:
    - qwen2-5-vl
    - multimodal
    - vllm
    - transformer-architecture
    - vision-language-model
    - positional-encoding
    - model-integration
category: reference
---

```
@MULTIMODAL_REGISTRY.register_processor(
    Qwen2_5_VLMultiModalProcessor,
    info=Qwen2_5_VLProcessingInfo,
    dummy_inputs=Qwen2_5_VLDummyInputsBuilder,
)
classQwen2_5_VLForConditionalGeneration(
    nn.Module,
    SupportsMultiModal,
    SupportsEncoderCudaGraph,
    SupportsLoRA,
    SupportsPP,
    SupportsQuant,
    SupportsEagle,
    SupportsEagle3,
    SupportsMultiModalPruning,
    SupportsMRoPE,
):
    packed_modules_mapping = {
        "qkv_proj": ["q_proj", "k_proj", "v_proj"],
        "gate_up_proj": ["gate_proj", "up_proj"],
        "qkv": ["qkv"],  # For vision tower's already-packed QKV
    }

    # To ensure correct weight loading and mapping.
    hf_to_vllm_mapper = WeightsMapper(
        orig_to_new_prefix={
            # mapping for new names in checkpoint saved after transformers v4.52
            "model.language_model.": "language_model.model.",
            "model.visual.": "visual.",
            # mapping for original checkpoint
            "lm_head.": "language_model.lm_head.",
            "model.": "language_model.model.",
        }
    )

    supports_encoder_tp_data = True

    defiter_mm_grid_thw(
        self, mm_features: list[MultiModalFeatureSpec]
    ) -> Iterator[tuple[int, int, int, int, float]]:
"""
        Iterate over multimodal features and yield grid information.

        Args:
            mm_features: List of multimodal feature specifications

        Yields:
            Tuple of (offset, grid_t, grid_h, grid_w, t_factor) for each frame/image
        """
        spatial_merge_size = self.config.vision_config.spatial_merge_size
        tokens_per_second = getattr(self.config.vision_config, "tokens_per_second", 1.0)
        for mm_feature in sorted(mm_features, key=lambda f: f.mm_position.offset):
            offset = mm_feature.mm_position.offset
            if mm_feature.modality == "image":
                t, h, w = mm_feature.data["image_grid_thw"].data.tolist()
                assert t == 1, f"Image must have 1 frame, got {t}"
                yield offset, 1, h // spatial_merge_size, w // spatial_merge_size, 1.0
            elif mm_feature.modality == "video":
                t, h, w = mm_feature.data["video_grid_thw"].data.tolist()
                second_per_grid_ts = 1.0
                if mm_feature.data.get("second_per_grid_ts", None):
                    second_per_grid_ts = mm_feature.data[
                        "second_per_grid_ts"
                    ].data.item()
                t_factor = second_per_grid_ts * tokens_per_second
                yield (
                    offset,
                    t,
                    h // spatial_merge_size,
                    w // spatial_merge_size,
                    t_factor,
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
            t_factor,
        ) in self.iter_mm_grid_thw(mm_features):
            text_len = offset - st
            st_idx = llm_pos_ids_list[-1].max() + 1 if len(llm_pos_ids_list) > 0 else 0
            llm_pos_ids_list.append(
                np.broadcast_to(np.arange(text_len), (3, text_len)) + st_idx
            )

            grid_indices = np.indices((llm_grid_t, llm_grid_h, llm_grid_w))
            if t_factor != 1.0:
                grid_indices[0] = (grid_indices[0] * t_factor).astype(np.int64)
            llm_pos_ids_list.append(grid_indices.reshape(3, -1) + text_len + st_idx)
            st = offset + llm_grid_t * llm_grid_h * llm_grid_w

        if st < len(input_tokens):
            st_idx = llm_pos_ids_list[-1].max() + 1 if len(llm_pos_ids_list) > 0 else 0
            text_len = len(input_tokens) - st
            llm_pos_ids_list.append(
                np.broadcast_to(np.arange(text_len), (3, text_len)) + st_idx
            )

        llm_positions = np.concatenate(llm_pos_ids_list, axis=1).reshape(3, -1)
        mrope_position_delta = (llm_positions.max() + 1 - len(input_tokens)).item()

        return torch.from_numpy(llm_positions), mrope_position_delta

    @classmethod
    defget_placeholder_str(cls, modality: str, i: int) -> str | None:
        if modality.startswith("image"):
            return "<|vision_start|><|image_pad|><|vision_end|>"
        if modality.startswith("video"):
            return "<|vision_start|><|video_pad|><|vision_end|>"

        raise ValueError("Only image or video modality is supported")

    def__init__(self, *, vllm_config: VllmConfig, prefix: str = ""):
        super().__init__()
        config: Qwen2_5_VLConfig = vllm_config.model_config.hf_config
        multimodal_config = vllm_config.model_config.multimodal_config

        self.use_data_parallel = multimodal_config.mm_encoder_tp_mode == "data"
        self.config = config
        self.model_config = vllm_config.model_config
        self.vllm_config = vllm_config
        self.multimodal_config = multimodal_config
        self.video_pruning_rate = multimodal_config.video_pruning_rate
        self.is_multimodal_pruning_enabled = (
            multimodal_config.is_multimodal_pruning_enabled()
        )

        with self._mark_tower_model(vllm_config, {"image", "video"}):
            self.visual = Qwen2_5_VisionTransformer(
                vision_config=config.vision_config,
                norm_eps=getattr(config, "rms_norm_eps", 1e-6),
                quant_config=self.quant_config,
                prefix=maybe_prefix(prefix, "visual"),
            )

        with self._mark_language_model(vllm_config):
            self.language_model = init_vllm_registered_model(
                vllm_config=vllm_config,
                prefix=maybe_prefix(prefix, "language_model"),
                architectures=["Qwen2ForCausalLM"],
            )

        self.make_empty_intermediate_tensors = (
            self.language_model.make_empty_intermediate_tensors
        )

    def_parse_and_validate_image_input(
        self, **kwargs: object
    ) -> Qwen2_5_VLImageInputs | None:
        pixel_values = kwargs.pop("pixel_values", None)
        image_embeds = kwargs.pop("image_embeds", None)
        image_grid_thw = kwargs.pop("image_grid_thw", None)

        if pixel_values is None and image_embeds is None:
            return None

        if pixel_values is not None:
            return Qwen2_5_VLImagePixelInputs(
                type="pixel_values",
                pixel_values=pixel_values,
                image_grid_thw=image_grid_thw,
            )

        if image_embeds is not None:
            return Qwen2_5_VLImageEmbeddingInputs(
                type="image_embeds",
                image_embeds=image_embeds,
                image_grid_thw=image_grid_thw,
            )

    def_parse_and_validate_video_input(
        self, **kwargs: object
    ) -> Qwen2_5_VLVideoInputs | None:
        pixel_values_videos = kwargs.pop("pixel_values_videos", None)
        video_embeds = kwargs.pop("video_embeds", None)
        video_grid_thw = kwargs.pop("video_grid_thw", None)
        second_per_grid_ts = kwargs.pop("second_per_grid_ts", None)

        if pixel_values_videos is None and video_embeds is None:
            return None

        if pixel_values_videos is not None:
            return Qwen2_5_VLVideoPixelInputs(
                type="pixel_values_videos",
                pixel_values_videos=pixel_values_videos,
                video_grid_thw=video_grid_thw,
                second_per_grid_ts=second_per_grid_ts,
            )

        if video_embeds is not None:
            return Qwen2_5_VLVideoEmbeddingInputs(
                type="video_embeds",
                video_embeds=video_embeds,
                video_grid_thw=video_grid_thw,
                second_per_grid_ts=second_per_grid_ts,
            )

    def_process_image_input(
        self, image_input: Qwen2_5_VLImageInputs
    ) -> tuple[torch.Tensor, ...]:
        grid_thw = image_input["image_grid_thw"]
        assert grid_thw.ndim == 2
        grid_thw_list = grid_thw.tolist()

        if image_input["type"] == "image_embeds":
            image_embeds = image_input["image_embeds"].type(self.visual.dtype)
        else:
            pixel_values = image_input["pixel_values"]
            if self.use_data_parallel:
                return run_dp_sharded_mrope_vision_model(
                    self.visual, pixel_values, grid_thw_list, rope_type="rope_3d"
                )
            else:
                image_embeds = self.visual(pixel_values, grid_thw=grid_thw_list)

        # Split concatenated embeddings for each image item.
        merge_size = self.visual.spatial_merge_size
        sizes = (grid_thw.prod(-1) // merge_size // merge_size).tolist()
        return image_embeds.split(sizes)

    def_postprocess_image_embeds_evs(
        self,
        image_embeds_split: tuple[torch.Tensor, ...],
        image_input: Qwen2_5_VLImageInputs,
    ) -> tuple[torch.Tensor, ...]:
"""
        Append mrope positions for each for images.
        This is necessary to recover correct mrope
        positions after video pruning

        Args:
            image_embeds_split: Tuple of image embeddings for
                each image item.
            image_input: Image input data.

        Returns:
            Tuple of image embeddings for each image item.
            Resulting embeddings will have extra 4 channels for
            computed mrope positions.
        """
        merge_size = self.visual.spatial_merge_size
        grid_thw = image_input["image_grid_thw"]
        grid_thw_list = grid_thw.tolist()
        image_embeds_out = []
        for emb, size in zip(image_embeds_split, grid_thw_list):
            positions = compute_mrope_for_media(size, merge_size).to(emb.device)
            emb = torch.cat([emb, positions], dim=1)
            image_embeds_out.append(emb)
        image_embeds_split = image_embeds_out
        return tuple(image_embeds_split)

    def_process_video_input(
        self, video_input: Qwen2_5_VLVideoInputs
    ) -> tuple[torch.Tensor, ...]:
        grid_thw = video_input["video_grid_thw"]
        assert grid_thw.ndim == 2
        grid_thw_list = grid_thw.tolist()

        if video_input["type"] == "video_embeds":
            video_embeds = video_input["video_embeds"].type(self.visual.dtype)
        else:
            pixel_values_videos = video_input["pixel_values_videos"]
            if self.use_data_parallel:
                return run_dp_sharded_mrope_vision_model(
                    self.visual,
                    pixel_values_videos,
                    grid_thw_list,
                    rope_type="rope_3d",
                )
            else:
                video_embeds = self.visual(pixel_values_videos, grid_thw=grid_thw_list)

        # Split concatenated embeddings for each video item.
        merge_size = self.visual.spatial_merge_size
        sizes = (grid_thw.prod(-1) // merge_size // merge_size).tolist()
        return video_embeds.split(sizes)

    def_postprocess_video_embeds_evs(
        self,
        video_embeds_split: tuple[torch.Tensor, ...],
        video_input: Qwen2_5_VLVideoInputs,
    ) -> tuple[torch.Tensor, ...]:
"""
        Prunes video embeddings via Efficient Video Sampling (EVS)
        and then appends mrope positions for each retained embeddings

        Args:
            video_embeds_split: Tuple of video embeddings for each video item.
            video_input: Video input data.

        Returns:
            Tuple of video embeddings for each video item.
            Resulting embeddings will have extra 4 channels for
            computed mrope positions.
        """
        grid_thw = video_input["video_grid_thw"]
        assert grid_thw.ndim == 2
        grid_thw_list = grid_thw.tolist()
        merge_size = self.visual.spatial_merge_size

        # Cast to long to match the original code
        # https://github.com/huggingface/transformers/blob/41980ce93e775f6c88500c51c8db7946fc6a2add/src/transformers/models/qwen2_5_vl/modular_qwen2_5_vl.py#L491 # noqa
        second_per_grid_ts = video_input.get("second_per_grid_ts")
        if second_per_grid_ts is None:
            raise ValueError(
                "second_per_grid_ts is required when video_pruning_rate > 0 "
                "is enabled for video inputs, including the video_embeds path."
            )
        second_per_grid_ts = second_per_grid_ts.long()
        tokens_per_second = self.config.vision_config.tokens_per_second

        video_embeds_out = []
        for emb, size, video_second_per_grid_t in zip(
            video_embeds_split, grid_thw_list, second_per_grid_ts
        ):
            # For each video, we compute retention mask using EVS
            retention_mask = compute_retention_mask(
                emb,
                size,
                spatial_merge_size=self.visual.spatial_merge_size,
                q=self.video_pruning_rate,
            )
            positions = compute_mrope_for_media(
                size,
                merge_size,
                tokens_per_second=tokens_per_second,
                video_second_per_grid=video_second_per_grid_t.item(),
            ).to(emb.device)

            emb = emb[retention_mask]
            positions = positions[retention_mask]
            emb = torch.cat([emb, positions], dim=1)
            video_embeds_out.append(emb)
        return tuple(video_embeds_out)

    defrecompute_mrope_positions(
        self,
        input_ids: list[int],
        multimodal_embeddings: tuple[torch.Tensor, ...],
        mrope_positions: torch.LongTensor,
        num_computed_tokens: int,
    ) -> tuple[tuple[torch.Tensor, ...], torch.Tensor, int]:
"""
        Update part of input mrope positions (starting with
        num_computed_tokens index). Original mrope_positions are computed
        for unpruned sequence and becomes incorrect once pruning occurs,
        so once we prune media tokens we should reflect this in the
        mrope_positions before we feed it to LLM.

        Args:
            input_ids: (N,) All input tokens of the prompt (Containing
                entire sequence).
            multimodal_embeddings: Tuple of multimodal embeddings.
            mrope_positions: Existing mrope positions (3, N) for entire
                sequence
            num_computed_tokens: A number of computed tokens so far.

        Returns:
            Tuple of (multimodal_embeddings, mrope_positions,
                mrope_position_delta).
        """
        image_token_id = self.config.image_token_id
        video_token_id = self.config.video_token_id
        vision_start_token_id = self.config.vision_start_token_id

        # Device
        device = (
            multimodal_embeddings[0].device
            if len(multimodal_embeddings)
            else mrope_positions.device
        )

        # Tensors
        input_ids_t = torch.as_tensor(input_ids, device=device, dtype=torch.long)

        mm_embeddings_out = [mm[:, :-4] for mm in multimodal_embeddings]
        mm_embeddings_pos = [
            mm[:, -4:].permute(1, 0).long() for mm in multimodal_embeddings
        ]

        positions, mrope_positions_delta = recompute_mrope_positions(
            input_ids_t,
            mm_embeddings_pos,
            mrope_positions,
            num_computed_tokens,
            vision_start_token_id,
            image_token_id,
            video_token_id,
        )

        return tuple(mm_embeddings_out), positions, mrope_positions_delta

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
                if self.is_multimodal_pruning_enabled:
                    image_embeddings = self._postprocess_image_embeds_evs(
                        image_embeddings, multimodal_input
                    )
                multimodal_embeddings += tuple(image_embeddings)
            if modality == "video":
                video_embeddings = self._process_video_input(multimodal_input)
                if self.is_multimodal_pruning_enabled:
                    video_embeddings = self._postprocess_video_embeds_evs(
                        video_embeddings, multimodal_input
                    )
                multimodal_embeddings += tuple(video_embeddings)
        return multimodal_embeddings

    # -- SupportsEncoderCudaGraph protocol methods --

    defget_encoder_cudagraph_config(self):
        fromvllm.v1.worker.encoder_cudagraph_defsimport (
            EncoderCudaGraphConfig,
        )

        # NOTE: With EVS pruning enabled, multimodal embeddings are post-processed
        # (append positions for image and prune+append positions for video) in
        # embed_multimodal(). The encoder CUDA graph path bypasses that postprocess
        # hook, so disable CUDA graph for all modalities to avoid inconsistent
        # embedding formats between eager and cudagraph paths.
        modalities = [] if self.is_multimodal_pruning_enabled else ["image", "video"]

        return EncoderCudaGraphConfig(
            modalities=modalities,
            input_key_by_modality={
                "image": "pixel_values",
                "video": "pixel_values_videos",
            },
            buffer_keys=[
                "rotary_pos_emb_cos",
                "rotary_pos_emb_sin",
                "window_index",
                "reverse_indices",
                "cu_seqlens",
                "cu_window_seqlens",
                "max_seqlen_full",
                "max_seqlen_window",
            ],
            out_hidden_size=self.visual.out_hidden_size,
        )

    defget_input_modality(
        self,
        mm_kwargs: dict[str, Any],
    ) -> str:
        if "image_grid_thw" in mm_kwargs:
            return "image"
        return "video"

    defget_max_frames_per_video(self) -> int:
        mm_registry = MULTIMODAL_REGISTRY
        info = mm_registry.get_processing_info(self.model_config)
        max_frames_per_video = info.get_num_frames_with_most_features(
            seq_len=self.model_config.max_model_len,
            mm_counts={"video": self.multimodal_config.get_limit_per_prompt("video")},
        )
        return max_frames_per_video

    defget_encoder_cudagraph_budget_range(
        self,
        vllm_config: VllmConfig,
    ) -> tuple[int, int]:
        # Min: estimated smallest possible encoder input.
        # 224x224 image → 16x16 patches (patch_size=14)
        #                 spatial_merge_size=2 → 8x8 = 64 tokens
        min_budget = 64
        # Max: capped by max_num_batched_tokens
        max_budget = min(
            vllm_config.scheduler_config.max_num_batched_tokens,
            self.model_config.max_model_len,
        )
        return (min_budget, max_budget)

    def_get_pixel_values_by_modality(
        self,
        mm_kwargs: dict[str, Any],
    ) -> torch.Tensor:
        if self.get_input_modality(mm_kwargs) == "image":
            pixel_values = mm_kwargs["pixel_values"]
        else:
            pixel_values = mm_kwargs["pixel_values_videos"]
        return pixel_values

    def_get_grid_thw_by_modality(
        self,
        mm_kwargs: dict[str, Any],
    ) -> list[tuple[int, int, int]]:
        grid_thw_key = f"{self.get_input_modality(mm_kwargs)}_grid_thw"
        grid_thw = mm_kwargs[grid_thw_key]
        if not isinstance(grid_thw, list):
            grid_thw = grid_thw.tolist()
        return grid_thw

    defget_encoder_cudagraph_num_items(
        self,
        mm_kwargs: dict[str, Any],
    ) -> int:
        return len(self._get_grid_thw_by_modality(mm_kwargs))

    defget_encoder_cudagraph_per_item_output_tokens(
        self,
        mm_kwargs: dict[str, Any],
    ) -> list[int]:
        m = self.visual.spatial_merge_size
        grid_thw = self._get_grid_thw_by_modality(mm_kwargs)
        return [t * (h // m) * (w // m) for t, h, w in grid_thw]

    defget_encoder_cudagraph_per_item_input_sizes(
        self,
        mm_kwargs: dict[str, Any],
    ) -> list[int]:
        grid_thw = self._get_grid_thw_by_modality(mm_kwargs)
        return [t * h * w for t, h, w in grid_thw]

    defselect_encoder_cudagraph_items(
        self,
        mm_kwargs: dict[str, Any],
        indices: list[int],
    ) -> dict[str, Any]:
        grid_thw = self._get_grid_thw_by_modality(mm_kwargs)
        pixel_values = self._get_pixel_values_by_modality(mm_kwargs)

        if len(indices) == 0:
            if self.get_input_modality(mm_kwargs) == "image":
                return {
                    "pixel_values": pixel_values[:0],
                    "image_grid_thw": [],
                }
            else:
                return {
                    "pixel_values_videos": pixel_values[:0],
                    "video_grid_thw": [],
                }

        # Compute cumulative patch offsets for slicing pixel_values
        patches_per_item = [t * h * w for t, h, w in grid_thw]
        cum_patches = [0]
        for p in patches_per_item:
            cum_patches.append(cum_patches[-1] + p)

        selected_pv = torch.cat(
            [pixel_values[cum_patches[i] : cum_patches[i + 1]] for i in indices]
        )
        selected_grid = [grid_thw[i] for i in indices]

        if self.get_input_modality(mm_kwargs) == "image":
            return {
                "pixel_values": selected_pv,
                "image_grid_thw": selected_grid,
            }
        else:
            return {
                "pixel_values_videos": selected_pv,
                "video_grid_thw": selected_grid,
            }

    defprepare_encoder_cudagraph_capture_inputs(
        self,
        token_budget: int,
        max_batch_size: int,
        max_frames_per_batch: int,
        device: torch.device,
        dtype: torch.dtype,
    ):
        fromvllm.v1.worker.encoder_cudagraph_defsimport (
            EncoderCudaGraphCaptureInputs,
        )

        spatial_merge_size = self.visual.spatial_merge_size
        max_window_seqs_per_batch = min(
            self.vllm_config.scheduler_config.max_num_batched_tokens,
            self.model_config.max_model_len,
        )
        # Use ceil here (not floor) so total captured capacity is never smaller
        # than token_budget when token_budget is not divisible by max_batch_size
        # (e.g., 324 budget with max_batch_size=8). Floor under-allocates
        # input_buffer and can fail replay copy for valid single-item batches.
        per_mm_item_output = (token_budget + max_batch_size - 1) // max_batch_size

        frames_per_item = max_frames_per_batch // max_batch_size
        if frames_per_item > 1:
            # Build the capture grid using a video-format layout so that
            # cu_seqlens is sized for video replays from the start.
            # cu_seqlens has one entry per attention sequence (one per frame),
            # so using T > 1 per item makes the buffer large enough without
            # relying solely on padding.
            # Ceiling ensures frames_per_item * tokens_per_frame >= per_mm_item_output
            # so the pixel_values buffer covers any valid single-item replay.
            tokens_per_frame = (
                per_mm_item_output + frames_per_item - 1
            ) // frames_per_item
            # Video-format grid_config (T=frames_per_item).
            grid_config = [
                [
                    frames_per_item,
                    spatial_merge_size,
                    tokens_per_frame * spatial_merge_size,
                ]
                for _ in range(max_batch_size)
            ]
        else:
            # Image-format grid_config (T=1).
            grid_config = [
                [1, spatial_merge_size, per_mm_item_output * spatial_merge_size]
                for _ in range(max_batch_size)
            ]

        # Create dummy pixel_values
        patch_embed = self.visual.patch_embed
        in_channels = patch_embed.proj.in_channels
        patch_size = patch_embed.patch_size
        temporal_patch_size = patch_embed.temporal_patch_size
        total_patches = sum(t * h * w for t, h, w in grid_config)
        flattened_patch_size = (
            in_channels * temporal_patch_size * patch_size * patch_size
        )
        dummy_pixel_values = torch.randn(
            total_patches, flattened_patch_size, device=device, dtype=dtype
        )

        # Override max_seqlen with a safe upper bound for capture.
        # max_seqlen.item() gets baked into the CUDA graph (not replayed),
        # so the capture value must cover any replay scenario.
        # Worst case: 1 item consuming the full budget ->
        # seq_len = token_budget * spatial_merge_size^2.
        # For window-attention, each local window is bounded by fixed geometry:
        # (window_size / patch_size / spatial_merge_size)^2 windows in merged
        # token space, multiplied by spatial_merge_size^2 to map back to the
        # unmerged sequence length used by attention kernels.
        vit_merger_window_size = (
            self.visual.window_size
            // self.visual.spatial_merge_size
            // self.visual.patch_size
        )
        max_seqlen_window_override = vit_merger_window_size**2 * (spatial_merge_size**2)
        buffers = self.visual.prepare_encoder_metadata(
            grid_config,
            max_batch_size=max_batch_size,
            max_frames_per_batch=max_frames_per_batch,
            max_window_seqs_per_batch=max_window_seqs_per_batch,
            max_seqlen_override=token_budget * (spatial_merge_size**2),
            max_seqlen_window_override=max_seqlen_window_override,
            device=device,
        )

        # Just use image-modality dummy input_buffer for capturing, since it's also
        # compatible for video inputs (has the same shape: [num_patches, C*T*P*P]).
        mm_kwargs = {
            "pixel_values": dummy_pixel_values,
            "image_grid_thw": grid_config,
        }

        return EncoderCudaGraphCaptureInputs(
            mm_kwargs=mm_kwargs,
            buffers=buffers,
        )

    defprepare_encoder_cudagraph_replay_buffers(
        self,
        mm_kwargs: dict[str, Any],
        max_batch_size: int,
        max_frames_per_batch: int,
    ):
        modality = self.get_input_modality(mm_kwargs)
        grid_thw_list = self._get_grid_thw_by_modality(mm_kwargs)

        if modality == "image":
            buffers = self.visual.prepare_encoder_metadata(
                grid_thw_list,
                max_batch_size=max_batch_size,
                max_window_seqs_per_batch=min(
                    self.vllm_config.scheduler_config.max_num_batched_tokens,
                    self.model_config.max_model_len,
                ),
            )
        else:
            buffers = self.visual.prepare_encoder_metadata(
                grid_thw_list,
                max_frames_per_batch=max_frames_per_batch,
                max_window_seqs_per_batch=min(
                    self.vllm_config.scheduler_config.max_num_batched_tokens,
                    self.model_config.max_model_len,
                ),
            )

        return EncoderCudaGraphReplayBuffers(buffers=buffers)

    defencoder_cudagraph_forward(
        self,
        mm_kwargs: dict[str, Any],
        buffers: dict[str, torch.Tensor],
    ) -> torch.Tensor:
        pixel_values = self._get_pixel_values_by_modality(mm_kwargs)
        grid_thw = self._get_grid_thw_by_modality(mm_kwargs)
        return self.visual(pixel_values, grid_thw, encoder_metadata=buffers)

    defencoder_eager_forward(
        self,
        mm_kwargs: dict[str, Any],
    ) -> torch.Tensor:
        pixel_values = self._get_pixel_values_by_modality(mm_kwargs)
        grid_thw = self._get_grid_thw_by_modality(mm_kwargs)
        return self.visual(pixel_values, grid_thw)

    defforward(
        self,
        input_ids: torch.Tensor | None,
        positions: torch.Tensor,
        intermediate_tensors: IntermediateTensors | None = None,
        inputs_embeds: torch.Tensor | None = None,
        **kwargs: object,
    ) -> torch.Tensor | IntermediateTensors:
"""Run forward pass for Qwen2.5-VL.

        Args:
            input_ids: Flattened (concatenated) input_ids corresponding to a
                batch.
            positions: Flattened (concatenated) position ids corresponding to a
                batch. **NOTE**: If mrope is enabled (default setting for
                Qwen2.5-VL opensource models), the shape will be `(3, seq_len)`,
                otherwise it will be `(seq_len,).
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
            language_model="language_model",
            connector="visual.merger.",
            tower_model="visual.",
        )

    defget_num_mm_encoder_tokens(
        self,
        num_image_tokens: int,
    ) -> int:
        hf_config = self.config
        vision_config = hf_config.vision_config
        merge_size = vision_config.spatial_merge_size

        return num_image_tokens * merge_size**2

    defget_num_mm_connector_tokens(
        self,
        num_vision_tokens: int,
    ) -> int:
        hf_config = self.config
        vision_config = hf_config.vision_config
        merge_size = vision_config.spatial_merge_size
        return num_vision_tokens // merge_size**2
```