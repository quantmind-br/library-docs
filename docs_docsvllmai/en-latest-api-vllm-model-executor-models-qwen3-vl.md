---
title: qwen3_vl - vLLM
url: https://docs.vllm.ai/en/latest/api/vllm/model_executor/models/qwen3_vl/
source: sitemap
fetched_at: 2026-05-07T21:33:06.406966448-03:00
rendered_js: false
word_count: 31
summary: This document defines the Qwen3VLForConditionalGeneration class, which integrates a vision transformer and a language model within the vLLM framework for multimodal processing. It includes support for various optimizations such as deepstack mechanisms, CUDA graphs for vision encoders, and specialized weight mapping for model loading.
tags:
    - vllm
    - qwen3-vl
    - multimodal
    - vision-transformer
    - model-architecture
    - cuda-graph
    - deepstack
category: reference
---

```
@MULTIMODAL_REGISTRY.register_processor(
    Qwen3VLMultiModalProcessor,
    info=Qwen3VLProcessingInfo,
    dummy_inputs=Qwen3VLDummyInputsBuilder,
)
classQwen3VLForConditionalGeneration(
    nn.Module,
    SupportsMultiModal,
    SupportsEncoderCudaGraph,
    SupportsLoRA,
    SupportsPP,
    SupportsMRoPE,
    SupportsEagle,
    SupportsEagle3,
    SupportsMultiModalPruning,
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
        "qkv": ["qkv"],  # For vision tower's already-packed QKV
    }

    supports_encoder_tp_data = True

    # To ensure correct weight loading and mapping.
    hf_to_vllm_mapper = WeightsMapper(
        orig_to_new_prefix={
            "model.visual.": "visual.",
            "lm_head.": "language_model.lm_head.",
            "model.language_model.": "language_model.model.",
        }
    )

    @classmethod
    defget_placeholder_str(cls, modality: str, i: int) -> str | None:
        if modality.startswith("image"):
            return "<|vision_start|><|image_pad|><|vision_end|>"
        if modality.startswith("video"):
            return "<|vision_start|><|video_pad|><|vision_end|>"

        raise ValueError("Only image or video modality is supported")

    def__init__(self, *, vllm_config: VllmConfig, prefix: str = "model"):
        super().__init__()
        config: Qwen3VLConfig = vllm_config.model_config.hf_config
        quant_config = vllm_config.quant_config
        multimodal_config = vllm_config.model_config.multimodal_config

        self.config = config
        self.model_config = vllm_config.model_config
        self._tokenizer = cached_tokenizer_from_config(vllm_config.model_config)
        self.multimodal_config = multimodal_config
        self.use_data_parallel = multimodal_config.mm_encoder_tp_mode == "data"
        self.video_pruning_rate = multimodal_config.video_pruning_rate
        self.is_multimodal_pruning_enabled = (
            multimodal_config.is_multimodal_pruning_enabled()
        )

        self.use_deepstack = hasattr(config.vision_config, "deepstack_visual_indexes")
        self.deepstack_num_level = (
            len(config.vision_config.deepstack_visual_indexes)
            if self.use_deepstack
            else 0
        )
        self.visual_dim = config.vision_config.out_hidden_size
        self.multiscale_dim = self.visual_dim * self.deepstack_num_level

        with self._mark_tower_model(vllm_config, {"image", "video"}):
            self.visual = Qwen3_VisionTransformer(
                config.vision_config,
                norm_eps=getattr(config, "rms_norm_eps", 1e-6),
                quant_config=quant_config,
                prefix=maybe_prefix(prefix, "visual"),
            )

            # register buffer for deepstack
            if self.use_deepstack:
                self.deepstack_input_embeds = [
                    torch.zeros(
                        vllm_config.scheduler_config.max_num_batched_tokens,
                        config.text_config.hidden_size,
                    )
                    for _ in range(self.deepstack_num_level)
                ]
                # Tracks the valid token span currently stored in the buffer.
                # Zero means there is no active deepstack payload to consume.
                self.deepstack_input_embeds_num_tokens = 0

        with self._mark_language_model(vllm_config):
            self.language_model = Qwen3LLMForCausalLM(
                vllm_config=vllm_config.with_hf_config(config.text_config),
                prefix=maybe_prefix(prefix, "language_model"),
            )

        if not get_pp_group().is_first_rank and hasattr(
            config.vision_config, "deepstack_visual_indexes"
        ):
            assert self.language_model.start_layer >= len(
                config.vision_config.deepstack_visual_indexes
            ), (
                "start_layer should be greater than or equal to "
                "len(deepstack_visual_indexes)"
            )

        self.make_empty_intermediate_tensors = (
            self.language_model.make_empty_intermediate_tensors
        )

    def_get_deepstack_input_embeds(
        self,
        num_tokens: int,
    ) -> IntermediateTensors | None:
        if not getattr(self, "deepstack_input_embeds", None):
            return None  # If vision tower is skipped
        if getattr(self, "deepstack_input_embeds_num_tokens", 0) == 0:
            return None

        # get deepstack_input_embeds from buffer, and clear the buffer
        return IntermediateTensors(
            {
                f"deepstack_input_embeds_{idx}": self.deepstack_input_embeds[idx][
                    :num_tokens
                ]
                for idx in range(self.deepstack_num_level)
            }
        )

    def_set_deepstack_input_embeds(self, deepstack_input_embeds: torch.Tensor) -> None:
        if not getattr(self, "deepstack_input_embeds", None):
            return

        # set deepstack_input_embeds to buffer
        num_tokens = deepstack_input_embeds.size(1)
        if num_tokens > self.deepstack_input_embeds[0].size(0):
            self.deepstack_input_embeds = [
                torch.zeros(
                    num_tokens,
                    self.config.text_config.hidden_size,
                    device=self.deepstack_input_embeds[0].device,
                    dtype=self.deepstack_input_embeds[0].dtype,
                )
                for _ in range(self.deepstack_num_level)
            ]
        for idx in range(self.deepstack_num_level):
            self.deepstack_input_embeds[idx][:num_tokens].copy_(
                deepstack_input_embeds[idx]
            )
        self.deepstack_input_embeds_num_tokens = num_tokens

    def_clear_deepstack_input_embeds(self, num_tokens: int) -> None:
        if not getattr(self, "deepstack_input_embeds", None):
            return
        if getattr(self, "deepstack_input_embeds_num_tokens", 0) == 0:
            return

        # clear deepstack_input_embeds in buffer
        if num_tokens > 0:
            for idx in range(self.deepstack_num_level):
                self.deepstack_input_embeds[idx][:num_tokens].zero_()
            self.deepstack_input_embeds_num_tokens = 0

    # -- SupportsEncoderCudaGraph protocol methods --

    defget_encoder_cudagraph_config(self):
        fromvllm.v1.worker.encoder_cudagraph_defsimport (
            EncoderCudaGraphConfig,
        )

        modalities = ["image"]
        # NOTE: When EVS (Efficient Video Sampling) pruning is enabled, the number
        # of tokens becomes data-dependent (i.e., the retained tokens are
        # dynamically selected based on inter-frame differences) and therefore
        # cannot be captured by CUDA Graphs. As a result, video CUDA Graphs are
        # only enabled when EVS is disabled.
        if not self.is_multimodal_pruning_enabled:
            modalities.append("video")

        return EncoderCudaGraphConfig(
            modalities=modalities,
            input_key_by_modality={
                "image": "pixel_values",
                "video": "pixel_values_videos",
            },
            buffer_keys=[
                "pos_embeds",
                "rotary_pos_emb_cos",
                "rotary_pos_emb_sin",
                "cu_seqlens",
                "max_seqlen",
                "sequence_lengths",
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
        vllm_config,
    ) -> tuple[int, int]:
        # Min: estimated smallest possible encoder input.
        # 224x224 image → 16x16 patches (patch_size=14)
        #                 spatial_merge_size=2 → 8x8 = 64 tokens
        min_budget = 64
        # Max: capped by max_num_batched_tokens
        # TODO(shen-shanshan): the max_budget auto-infer needs to be optimized later.
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
        per_mm_item_output = token_budget // max_batch_size

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
        buffers = self.visual.prepare_encoder_metadata(
            grid_config,
            max_batch_size=max_batch_size,
            max_frames_per_batch=max_frames_per_batch,
            max_seqlen_override=token_budget * (spatial_merge_size**2),
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
            )
        else:
            buffers = self.visual.prepare_encoder_metadata(
                grid_thw_list,
                max_frames_per_batch=max_frames_per_batch,
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
        timestamps = kwargs.pop("timestamps", None)

        if pixel_values_videos is None and video_embeds is None:
            return None

        if pixel_values_videos is not None:
            return Qwen2_5_VLVideoPixelInputs(
                type="pixel_values_videos",
                pixel_values_videos=pixel_values_videos,
                video_grid_thw=video_grid_thw,
                second_per_grid_ts=second_per_grid_ts,
                timestamps=timestamps,
            )

        if video_embeds is not None:
            return Qwen2_5_VLVideoEmbeddingInputs(
                type="video_embeds",
                video_embeds=video_embeds,
                video_grid_thw=video_grid_thw,
                timestamps=timestamps,
            )

    def_process_image_input(
        self, image_input: Qwen2_5_VLImageInputs
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

        # Split concatenated embeddings for each image item.
        merge_size = self.visual.spatial_merge_size
        sizes = (grid_thw.prod(-1) // merge_size // merge_size).tolist()
        return image_embeds.split(sizes)

    def_process_video_input(
        self, video_input: Qwen2_5_VLVideoInputs
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
                grid_thw_list = grid_thw.tolist()
                return run_dp_sharded_mrope_vision_model(
                    self.visual, pixel_values_videos, grid_thw_list, rope_type="rope_3d"
                )
            else:
                video_embeds = self.visual(pixel_values_videos, grid_thw=grid_thw)

        # Split concatenated embeddings for each video item.
        merge_size = self.visual.spatial_merge_size
        sizes = (grid_thw.prod(-1) // merge_size // merge_size).tolist()
        return video_embeds.split(sizes)

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
            Resulting embeddings will have extra 5 channels for
            computed mrope positions, consistent with video embeddings.
        """
        if self.is_multimodal_pruning_enabled:
            merge_size = self.visual.spatial_merge_size
            grid_thw = image_input["image_grid_thw"]
            grid_thw_list = grid_thw.tolist()
            image_embeds_out = []
            for emb, size in zip(image_embeds_split, grid_thw_list):
                positions = compute_mrope_for_media(size, merge_size).to(emb.device)
                positions = torch.cat(
                    [
                        positions,
                        torch.zeros_like(
                            positions[:, 0:1]
                        ),  # Dummy extra fifth channel
                    ],
                    dim=1,
                )
                emb = torch.cat([emb, positions], dim=1)
                image_embeds_out.append(emb)
            image_embeds_split = tuple(image_embeds_out)
        return image_embeds_split

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
            Resulting embeddings will have extra 5 channels for computed mrope
            positions, and whether the index corresponds to a video embedding.
        """
        grid_thw = video_input["video_grid_thw"]
        assert grid_thw.ndim == 2
        grid_thw_list = grid_thw.tolist()
        merge_size = self.visual.spatial_merge_size

        # Apply EVS to each video.
        video_embeds_out = []
        for video_idx, (emb, size) in enumerate(zip(video_embeds_split, grid_thw_list)):
            # Compute positions.
            timestamps = video_input.timestamps[video_idx]
            num_frames = len(timestamps)

            t, h, w = size
            if self.is_multimodal_pruning_enabled:
                # For each video, compute retention mask using EVS.
                # retention_mask: [11424].
                retention_mask = compute_retention_mask(
                    emb,
                    size,
                    spatial_merge_size=self.visual.spatial_merge_size,
                    q=self.video_pruning_rate,
                )
                # Apply retention mask.
                emb = emb[retention_mask]

                # Calculate the actual number of retained tokens per frame.
                num_frames, rows, cols = (
                    t,
                    h // merge_size,
                    w // merge_size,
                )
                retention_mask_thw = retention_mask.reshape(num_frames, rows, cols)
                num_tokens_per_frame = (
                    retention_mask_thw.sum(dim=(1, 2)).long().tolist()
                )
            else:
                feature_size = emb.shape[0] // num_frames
                num_tokens_per_frame = [feature_size] * num_frames
                retention_mask = None

            emb = self._create_final_video_embeddings(
                video_embeddings=emb,
                num_tokens_per_frame=num_tokens_per_frame,
                timestamps=timestamps,
                video_grid_thw=size,
                retention_mask=retention_mask,
            )

            video_embeds_out.append(emb)

        return tuple(video_embeds_out)

    def_create_final_video_embeddings(
        self,
        video_embeddings: torch.Tensor,
        num_tokens_per_frame: list[int],
        timestamps: list[float],
        video_grid_thw: list[int],
        retention_mask: torch.Tensor,
    ) -> torch.Tensor:
"""Create final embeddings that combine video embeddings with
        text embeddings of indicator tokens.

        These final embeddings contain:
        - Actual video embeddings in positions corresponding to video content
        - Text embeddings for indicator tokens (<img>, </img>, and
          frame separation text) in their respective positions

        These embeddings will replace the placeholder embeddings to create
        input_embeds for the LLM.
        """

        # Generate video replacement token IDs using get_video_repl
        # This tokenizes each frame separator independently, then uses pre-tokenized
        # special tokens to ensure consistent tokenization regardless of
        # num_tokens_per_frame values.
        video_repl = Qwen3VLMultiModalProcessor.get_video_repl(
            tokens_per_frame=num_tokens_per_frame,
            tokenizer=self._tokenizer,
            timestamps=timestamps,
            vision_start_token_id=self.config.vision_start_token_id,
            vision_end_token_id=self.config.vision_end_token_id,
            video_token_id=self.config.video_token_id,
            select_token_id=self.is_multimodal_pruning_enabled,
        )

        repl_token_ids = torch.tensor(video_repl.full)
        embed_token_id = _cached_tensor(
            self.config.video_token_id, repl_token_ids.device
        )
        is_video_embed = torch.isin(repl_token_ids, embed_token_id)

        # Get text embeddings for indicator tokens (has only `visual_dim``).
        text_embeddings = self.get_language_model().embed_input_ids(repl_token_ids)

        if self.use_deepstack:
            (
                deepstack_input_embeds,
                multimodal_embeddings,
            ) = self._compute_deepstack_embeds(
                inputs_embeds=text_embeddings,
                multimodal_embeddings=[video_embeddings],
                is_multimodal=is_video_embed,
            )
        else:
            deepstack_input_embeds = None
            multimodal_embeddings = [video_embeddings]

        merged_embeddings = _merge_multimodal_embeddings(
            inputs_embeds=text_embeddings,
            multimodal_embeddings=multimodal_embeddings,
            is_multimodal=is_video_embed,
        )

        to_concat = [merged_embeddings]
        if deepstack_input_embeds is not None:
            to_concat.append(
                deepstack_input_embeds.permute(1, 0, 2).reshape(
                    deepstack_input_embeds.shape[1], -1
                )
            )

        expanded_positions = None
        if self.is_multimodal_pruning_enabled:
            is_vision_start = repl_token_ids.eq(self.config.vision_start_token_id)
            expanded_positions = self._get_expanded_positions(
                device=merged_embeddings.device,
                seq_len=merged_embeddings.shape[0],
                video_grid_thw=video_grid_thw,
                num_tokens_per_frame=num_tokens_per_frame,
                timestamps=timestamps,
                is_video_embed=is_video_embed,
                is_vision_start=is_vision_start,
                retention_mask=retention_mask,
            )
            to_concat.append(expanded_positions)

        final_video_embeddings = torch.cat(to_concat, dim=-1)

        return final_video_embeddings

    def_get_expanded_positions(
        self,
        device,
        seq_len,
        video_grid_thw,
        num_tokens_per_frame,
        timestamps,
        is_video_embed,
        is_vision_start,
        retention_mask,
    ):
        embed_token_id = _cached_tensor(self.config.video_token_id, device=device)

        # Expand positions to match the full sequence length
        # (includes both video tokens and indicator tokens)
        # Shape: [full_length, 5] where positions are filled for video tokens
        # and zeros for indicator tokens.
        # Channel 3 flags VISION_START tokens so that
        # recompute_mrope_positions can reliably count timestamp tokens
        # (even when early frames have all video tokens pruned).
        # Channel 4 flags video-embedding tokens.
        expanded_positions = torch.zeros(
            seq_len,
            5,  # [t_index, h_index, w_index, is_vision_start, is_video]
            device=device,
            dtype=torch.long,
        )
        _, h, w = video_grid_thw
        merge_size = self.visual.spatial_merge_size
        num_frames = len(num_tokens_per_frame)
        unpruned_token_ids = Qwen3VLMultiModalProcessor.get_video_repl(
            tokens_per_frame=[(h // merge_size) * (w // merge_size)] * num_frames,
            tokenizer=self._tokenizer,
            timestamps=timestamps,
            vision_start_token_id=self.config.vision_start_token_id,
            vision_end_token_id=self.config.vision_end_token_id,
            video_token_id=self.config.video_token_id,
        ).full
        unpruned_token_ids_tensor = torch.tensor(unpruned_token_ids, device=device)
        mm_feature = MultiModalFeatureSpec(
            data=MultiModalKwargsItem(
                {
                    "video_grid_thw": MultiModalFieldElem(
                        data=torch.tensor(video_grid_thw),
                        field=None,  # HACK.
                    ),
                }
            ),
            modality="video",
            identifier="DUMMY",
            mm_position=PlaceholderRange(offset=0, length=len(unpruned_token_ids)),
        )
        original_mrope = (
            self.get_mrope_input_positions(
                input_tokens=unpruned_token_ids,
                mm_features=[mm_feature],
            )[0]
            .to(device)
            .permute(1, 0)
        )
        full_is_video_embed = unpruned_token_ids_tensor == embed_token_id
        expanded_positions[is_video_embed, :3] = original_mrope[full_is_video_embed][
            retention_mask
        ]
        expanded_positions[~is_video_embed, :3] = original_mrope[~full_is_video_embed]
        expanded_positions[..., 3] = is_vision_start
        expanded_positions[..., 4] = is_video_embed

        return expanded_positions

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

    @staticmethod
    def_iter_mm_grid_hw(
        input_tokens: list[int],
        mm_features: list[MultiModalFeatureSpec],
        video_token_id: int,
        vision_start_token_id: int,
        vision_end_token_id: int,
        spatial_merge_size: int,
    ) -> Iterator[tuple[int, int, int, int]]:
"""Iterate over multimodal features and yield position info.

        Args:
            input_tokens: List of token IDs in the input sequence.
            mm_features: List of multimodal feature specifications containing
                image/video data and position information.
            video_token_id: Token ID used for video tokens.
            vision_start_token_id: Token ID marking the start of a vision sequence.
            vision_end_token_id: Token ID marking the end of a vision sequence.
            spatial_merge_size: Size of the spatial merge operation used to
                compute logical grid dimensions from the original feature grid.

        Yields:
            offset: Position of the first video/image token in the sequence.
            llm_grid_h: Logical grid height (may not match actual token count with EVS).
            llm_grid_w: Logical grid width (may not match actual token count with EVS).
            actual_num_tokens: Actual number of video/image tokens in the placeholder.
        """
        for mm_feature in sorted(mm_features, key=lambda f: f.mm_position.offset):
            offset = mm_feature.mm_position.offset
            if mm_feature.modality == "image":
                t, h, w = mm_feature.data["image_grid_thw"].data.tolist()
                assert t == 1, f"Image must have 1 frame, got {t}"
                llm_grid_h = h // spatial_merge_size
                llm_grid_w = w // spatial_merge_size
                yield offset, llm_grid_h, llm_grid_w, llm_grid_h * llm_grid_w
            elif mm_feature.modality == "video":
                t, h, w = mm_feature.data["video_grid_thw"].data.tolist()
                llm_grid_h = h // spatial_merge_size
                llm_grid_w = w // spatial_merge_size

                for _ in range(t):
                    # When EVS is enabled, some frames may have 0 video tokens in the
                    # placeholder. We use `vision_start_token_id` to locate each frame
                    # since it is always present for every frame.
                    # We then look for the first `video_token_id` after
                    # `vision_start_token_id` and before `vision_end_token_id`.
                    offset = input_tokens.index(vision_start_token_id, offset)
                    vision_end_offset = input_tokens.index(vision_end_token_id, offset)

                    try:
                        actual_num_tokens = 0
                        video_offset = input_tokens.index(
                            video_token_id, offset, vision_end_offset
                        )
                        # NOTE: looking at the
                        # `Qwen3VLMultiModalProcessor.get_video_repl` code, we can
                        # see that we can use the below formula to get the token
                        # count, since everything in between `video_offset` and
                        # `vision_end_offset` is populated as `video_token_id`.
                        # This saves us from manually counting the number tokens
                        # that match `video_token_id` in between.
                        actual_num_tokens += vision_end_offset - video_offset
                    except ValueError:
                        # No `video_token_id` in this frame (EVS with 0 tokens for
                        # this frame) -> use `offset + 1`` to move past
                        # `vision_start_token_id`.
                        video_offset = offset + 1

                    yield video_offset, llm_grid_h, llm_grid_w, actual_num_tokens
                    # Move offset past this frame for next iteration.
                    offset = vision_end_offset + 1
            else:
                raise ValueError(f"Unsupported modality: {mm_feature.modality}")

    defget_mrope_input_positions(
        self,
        input_tokens: list[int],
        mm_features: list[MultiModalFeatureSpec],
    ) -> tuple[torch.Tensor, int]:
        return self._get_mrope_input_positions(
            input_tokens=input_tokens,
            mm_features=mm_features,
            config=self.config,
        )

    @staticmethod
    def_get_mrope_input_positions(
        input_tokens: list[int],
        mm_features: list[MultiModalFeatureSpec],
        config: Qwen3VLConfig,
    ):
        llm_pos_ids_list = []
        st = 0
        for (
            offset,
            llm_grid_h,
            llm_grid_w,
            actual_num_tokens,
        ) in Qwen3VLForConditionalGeneration._iter_mm_grid_hw(
            input_tokens,
            mm_features,
            video_token_id=config.video_token_id,
            vision_start_token_id=config.vision_start_token_id,
            vision_end_token_id=config.vision_end_token_id,
            spatial_merge_size=config.vision_config.spatial_merge_size,
        ):
            # Skip frames with 0 tokens (EVS placeholder with tokens lumped elsewhere)
            if actual_num_tokens == 0:
                continue

            text_len = offset - st
            st_idx = llm_pos_ids_list[-1].max() + 1 if len(llm_pos_ids_list) > 0 else 0
            llm_pos_ids_list.append(
                np.broadcast_to(np.arange(text_len), (3, text_len)) + st_idx
            )

            # Check if this is a "lumped placeholder" (all tokens from multiple frames
            # assigned to the 0-th frame - see
            # `Qwen3VLMultiModalProcessor.get_video_repl`.
            expected_tokens_per_frame = llm_grid_h * llm_grid_w
            if actual_num_tokens > expected_tokens_per_frame:
                # Lumped placeholder: create grid positions for all "logical" frames
                # represented.
                num_logical_frames = actual_num_tokens // expected_tokens_per_frame
                remainder = actual_num_tokens % expected_tokens_per_frame

                # Create positions for complete frames.
                for _ in range(num_logical_frames):
                    grid_indices = np.indices((1, llm_grid_h, llm_grid_w)).reshape(
                        3, -1
                    )
                    llm_pos_ids_list.append(grid_indices + text_len + st_idx)
                    st_idx = llm_pos_ids_list[-1].max() + 1
                    text_len = 0  # No text between frames within the lump

                # Handle remainder tokens if any (partial frame).
                # NOTE: this should never be the case. Should we have an assert?
                if remainder > 0:
                    # Create a partial grid - take first 'remainder' positions
                    full_grid = np.indices((1, llm_grid_h, llm_grid_w)).reshape(3, -1)
                    grid_indices = full_grid[:, :remainder]
                    llm_pos_ids_list.append(grid_indices + text_len + st_idx)
            else:
                # Normal case: frame has exactly the expected tokens (after actual EVS
                # pruning).
                grid_indices = np.indices((1, llm_grid_h, llm_grid_w)).reshape(3, -1)
                llm_pos_ids_list.append(grid_indices + text_len + st_idx)

            st = offset + actual_num_tokens

        if st < len(input_tokens):
            st_idx = llm_pos_ids_list[-1].max() + 1 if len(llm_pos_ids_list) > 0 else 0
            text_len = len(input_tokens) - st
            llm_pos_ids_list.append(
                np.broadcast_to(np.arange(text_len), (3, text_len)) + st_idx
            )

        llm_positions = np.concatenate(llm_pos_ids_list, axis=1).reshape(3, -1)
        mrope_position_delta = (llm_positions.max() + 1 - len(input_tokens)).item()
        return torch.from_numpy(llm_positions), mrope_position_delta

    defrecompute_mrope_positions(
        self,
        input_ids: list[int],
        multimodal_embeddings: MultiModalEmbeddings,
        mrope_positions: torch.LongTensor,
        num_computed_tokens: int,
    ) -> tuple[MultiModalEmbeddings, torch.Tensor, int]:
"""
        Update part of input mrope positions (starting with
        num_computed_tokens index). Original mrope_positions are computed
        for unpruned sequence and becomes incorrect once pruning occurs,
        so once we prune media tokens we should reflect this in the
        mrope_positions before we feed it to LLM.

        Args:
            input_ids: (N,) All input tokens of the prompt containing
                entire sequence.
            multimodal_embeddings: Tuple of multimodal embeddings that
                fits into the prefill chunk that is being processed.
            mrope_positions: Existing mrope positions (3, N) for entire
                sequence
            num_computed_tokens: A number of computed tokens so far.

        Returns:
            Tuple of (multimodal_embeddings, mrope_positions,
                mrope_position_delta).
        """
        return self._recompute_mrope_positions(
            input_ids=input_ids,
            multimodal_embeddings=multimodal_embeddings,
            mrope_positions=mrope_positions,
            num_computed_tokens=num_computed_tokens,
            image_token_id=self.config.image_token_id,
            video_token_id=self.config.video_token_id,
            vision_start_token_id=self.config.vision_start_token_id,
        )

    @staticmethod
    def_recompute_mrope_positions(
        input_ids: list[int],
        multimodal_embeddings: MultiModalEmbeddings,
        mrope_positions: torch.LongTensor,
        num_computed_tokens: int,
        vision_start_token_id: int,
        image_token_id: int,
        video_token_id: int,
    ) -> tuple[MultiModalEmbeddings, torch.Tensor, int]:
        # Device
        device = (
            multimodal_embeddings[0].device
            if len(multimodal_embeddings)
            else mrope_positions.device
        )

        # Tensors
        input_ids_t = torch.as_tensor(input_ids, device=device, dtype=torch.long)

        mm_embeddings_out = []
        mm_embeddings_pos = []
        # Strip position information from embeddings (last 5 channels)
        # For Qwen3 VL, handle potentially empty frames (from unpacking)
        for mm in multimodal_embeddings:
            if mm.shape[0] > 0:  # Only process non-empty frames
                mm_embeddings_out.append(mm[:, :-5])
                mm_embeddings_pos.append(mm[:, -5:].permute(1, 0).long())
            else:
                # Empty frame - keep as is
                mm_embeddings_out.append(mm)
                # Create empty position tensor with correct shape
                mm_embeddings_pos.append(
                    torch.empty(5, 0, device=device, dtype=torch.long)
                )

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

    defembed_multimodal(self, **kwargs: object) -> MultiModalEmbeddings | None:
        mm_input_by_modality = self._parse_and_validate_multimodal_inputs(**kwargs)
        if not mm_input_by_modality:
            return None

        # The result multimodal_embeddings is tuple of tensors, with each
        # tensor corresponding to a multimodal data item (image or video).
        multimodal_embeddings: list[torch.Tensor] = []

        # NOTE: It is important to iterate over the keys in this dictionary
        # to preserve the order of the modalities.
        for modality in mm_input_by_modality:
            multimodal_input = mm_input_by_modality[modality]
            if modality == "image":
                image_embeddings = self._process_image_input(multimodal_input)
                image_embeddings = self._postprocess_image_embeds_evs(
                    image_embeddings, multimodal_input
                )
                multimodal_embeddings.extend(image_embeddings)
            if modality == "video":
                video_embeddings = self._process_video_input(multimodal_input)
                if self.is_multimodal_pruning_enabled:
                    video_embeddings = self._postprocess_video_embeds_evs(
                        video_embeddings, multimodal_input
                    )
                multimodal_embeddings.extend(video_embeddings)

        embeddings_tuple = tuple(multimodal_embeddings)
        return embeddings_tuple

    def_compute_deepstack_embeds(
        self,
        inputs_embeds: torch.Tensor,
        multimodal_embeddings: MultiModalEmbeddings,
        is_multimodal: torch.Tensor,
    ) -> tuple[torch.Tensor, MultiModalEmbeddings]:
        visual_lens = [len(x) for x in multimodal_embeddings]
        multimodal_embeddings_cat = torch.cat(multimodal_embeddings, dim=0)

        (
            multimodal_embeddings_main,
            multimodal_embeddings_multiscale,
        ) = torch.split(
            multimodal_embeddings_cat,
            [self.visual_dim, self.multiscale_dim],
            dim=-1,
        )

        multimodal_embeddings = torch.split(
            multimodal_embeddings_main, visual_lens, dim=0
        )
        multimodal_embeddings_multiscale = torch.split(
            multimodal_embeddings_multiscale, visual_lens, dim=0
        )

        deepstack_input_embeds = inputs_embeds.new_zeros(
            inputs_embeds.size(0), self.deepstack_num_level * inputs_embeds.size(1)
        )

        deepstack_input_embeds = _merge_multimodal_embeddings(
            inputs_embeds=deepstack_input_embeds,
            multimodal_embeddings=multimodal_embeddings_multiscale,
            is_multimodal=is_multimodal,
        )
        deepstack_input_embeds = deepstack_input_embeds.view(
            inputs_embeds.shape[0], self.deepstack_num_level, self.visual_dim
        )
        deepstack_input_embeds = deepstack_input_embeds.permute(1, 0, 2)

        return deepstack_input_embeds, multimodal_embeddings

    defembed_input_ids(
        self,
        input_ids: torch.Tensor,
        multimodal_embeddings: MultiModalEmbeddings | None = None,
        *,
        is_multimodal: torch.Tensor | None = None,
    ) -> torch.Tensor:
        inputs_embeds = self._embed_text_input_ids(
            input_ids,
            self.language_model.embed_input_ids,
            is_multimodal=is_multimodal,
        )

        if multimodal_embeddings is None or len(multimodal_embeddings) == 0:
            return inputs_embeds

        is_multimodal = _require_is_multimodal(is_multimodal)

        if self.use_deepstack:
            (
                deepstack_input_embeds,
                multimodal_embeddings,
            ) = self._compute_deepstack_embeds(
                inputs_embeds=inputs_embeds,
                multimodal_embeddings=multimodal_embeddings,
                is_multimodal=is_multimodal,
            )
        else:
            deepstack_input_embeds = None

        inputs_embeds = _merge_multimodal_embeddings(
            inputs_embeds=inputs_embeds,
            multimodal_embeddings=multimodal_embeddings,
            is_multimodal=is_multimodal,
        )

        if deepstack_input_embeds is not None:
            self._set_deepstack_input_embeds(deepstack_input_embeds)

        return inputs_embeds

    defforward(
        self,
        input_ids: torch.Tensor | None,
        positions: torch.Tensor,
        intermediate_tensors: IntermediateTensors | None = None,
        inputs_embeds: torch.Tensor | None = None,
        **kwargs: object,
    ) -> torch.Tensor | IntermediateTensors:
"""Run forward pass for Qwen3VL.

        Args:
            input_ids: Flattened (concatenated) input_ids corresponding to a
                batch.
            positions: Flattened (concatenated) position ids corresponding to a
                batch.
                **NOTE**: If mrope is enabled (default setting for Qwen3VL
                opensource models), the shape will be `(3, seq_len)`,
                otherwise it will be `(seq_len,).
            intermediate_tensors: Intermediate tensors from previous pipeline
                stages.
            inputs_embeds: Pre-computed input embeddings.
            **kwargs: Additional keyword arguments including:
                - pixel_values: Pixel values to be fed to a model.
                    `None` if no images are passed.
                - image_grid_thw: Tensor `(n_images, 3)` of image 3D grid in
                    LLM. `None` if no images are passed.
                - pixel_values_videos: Pixel values of videos to be fed to a
                    model. `None` if no videos are passed.
                - video_grid_thw: Tensor `(n_videos, 3)` of video 3D grid in
                    LLM. `None` if no videos are passed.
        """

        if intermediate_tensors is not None:
            inputs_embeds = None

        if inputs_embeds is not None and get_pp_group().is_first_rank:
            deepstack_input_embeds = self._get_deepstack_input_embeds(
                inputs_embeds.size(0)
            )
        else:
            deepstack_input_embeds = None

        hidden_states = self.language_model.model(
            input_ids=input_ids,
            positions=positions,
            intermediate_tensors=intermediate_tensors,
            inputs_embeds=inputs_embeds,
            # args for deepstack
            deepstack_input_embeds=deepstack_input_embeds,
        )

        if inputs_embeds is not None and get_pp_group().is_first_rank:
            self._clear_deepstack_input_embeds(inputs_embeds.size(0))

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
            connector=["visual.merger", "visual.deepstack_merger_list"],
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