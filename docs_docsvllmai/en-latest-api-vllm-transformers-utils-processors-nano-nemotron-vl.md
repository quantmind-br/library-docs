---
title: nano_nemotron_vl - vLLM
url: https://docs.vllm.ai/en/latest/api/vllm/transformers_utils/processors/nano_nemotron_vl/
source: sitemap
fetched_at: 2026-05-07T21:38:07.027962939-03:00
rendered_js: false
word_count: 13
summary: This document defines the NanoNemotronVLProcessor class, which extends Hugging Face processor functionality to support video input processing, frame tiling, and tokenization for vision-language models.
tags:
    - video-processing
    - hugging-face
    - vision-language-model
    - tokenization
    - image-tiling
    - multimodal
category: api
---

```
classNanoNemotronVLProcessor(BaseNanoNemotronVLProcessor):
"""
    HF Processor with extended video processing logic.
    Code for video processing is adapted from video example:
    https://huggingface.co/OpenGVLab/InternVL3-1B#inference-with-transformers
    """

    def__init__(
        self,
        config: PretrainedConfig,
        tokenizer: HfTokenizer,
        *,
        max_model_len: int,
        max_num_tiles: int | None = None,
        video_token: str | None = None,
        video_pruning_rate: float | None = None,
        use_audio_in_video: bool = False,
    ) -> None:
        super().__init__(
            config=config,
            tokenizer=tokenizer,
            max_model_len=max_model_len,
            max_num_tiles=max_num_tiles,
        )
        # add extra video token for video processing
        self.video_token = video_token
        self.video_pruning_rate = video_pruning_rate
        self.use_audio_in_video = use_audio_in_video

        # Video params live exclusively in vision_config
        vision_config = getattr(config, "vision_config", config)
        self.video_temporal_patch_size: int = getattr(
            vision_config, "video_temporal_patch_size", 1
        )
        self.video_maintain_aspect_ratio: bool = getattr(
            vision_config, "video_maintain_aspect_ratio", False
        )

        # Resolve video frame target size: exactly one of video_target_num_patches
        # or video_target_img_size may be set (mirrors Megatron's
        # DynamicResolutionImageTilingStrategy validation).
        target_num_patches = getattr(vision_config, "video_target_num_patches", None)
        target_img_size = getattr(vision_config, "video_target_img_size", None)
        if target_num_patches is not None and target_img_size is not None:
            raise ValueError(
                "Exactly one of video_target_num_patches or "
                "video_target_img_size must be set, got both"
            )
        if target_num_patches is not None:
            self.video_target_num_patches: int | None = target_num_patches
        elif target_img_size is not None:
            base_patches = math.ceil(target_img_size / config.patch_size)
            self.video_target_num_patches = base_patches * base_patches
        else:
            self.video_target_num_patches = None

        self.audio_extractor: ParakeetExtractor | None = None
        raw_sound_config = getattr(config, "sound_config", None)
        if raw_sound_config is not None:
            self.audio_extractor = ParakeetExtractor(raw_sound_config)

        # Pre-tokenize special tokens for video processing
        # to avoid repeated tokenization
        self._img_start_token_ids = tokenizer.encode(
            IMG_START, add_special_tokens=False
        )
        self._img_end_token_ids = tokenizer.encode(IMG_END, add_special_tokens=False)
        self._img_context_token_ids = tokenizer.encode(
            IMG_CONTEXT, add_special_tokens=False
        )

    @cached_property
    defnum_video_token(self) -> int:
"""Token count per video frame, accounting for video_target_num_patches.

        When video_target_num_patches is set the per-frame feature count
        differs from the image-based num_image_token.  We use a square
        dummy (1:1) to compute the feature_size because the dummy video is
        square and the user confirmed that is acceptable.
        """
        if self.video_target_num_patches is not None:
            _, _, feature_size = get_video_target_size_and_feature_size(
                orig_w=self.image_size,
                orig_h=self.image_size,
                target_patches=self.video_target_num_patches,
                maintain_aspect_ratio=self.video_maintain_aspect_ratio,
                patch_size=self.config.patch_size,
                downsample_ratio=self.config.downsample_ratio,
            )
            return feature_size
        return self.num_image_token

    @property
    defsupports_video(self) -> bool:
        return True

    @property
    defvideo_token_id(self) -> int:
        assert self.video_token is not None
        return self.tokenizer.get_vocab()[self.video_token]

    @property
    defimage_token_id(self) -> int:
        return self.tokenizer.convert_tokens_to_ids(IMG_CONTEXT)

    def_videos_to_pixel_values_lst(
        self,
        videos: list[npt.NDArray],
        *,
        dtype: torch.dtype = torch.float32,
    ) -> list[torch.Tensor]:
        return [
            video_to_pixel_values(
                video,
                input_size=self.image_size,
                video_target_num_patches=self.video_target_num_patches,
                video_maintain_aspect_ratio=self.video_maintain_aspect_ratio,
                patch_size=self.config.patch_size,
                downsample_ratio=self.config.downsample_ratio,
                norm_mean=self.norm_mean,
                norm_std=self.norm_std,
                dtype=dtype,
            )
            for video in videos
        ]

    def_preprocess_video(
        self,
        text: list[str],
        videos: list[tuple[npt.NDArray, dict[str, Any]]],
    ) -> tuple[list[str], dict[str, Any]]:
        if len(videos) == 0 or not self.supports_video:
            return text, {}

        videos_lst = [v[0] for v in videos]
        video_metadata_lst = [v[1] for v in videos]

        pixel_values_lst_video = self._videos_to_pixel_values_lst(
            videos_lst,
            dtype=self.dtype,
        )

        # We use frame duration in milliseconds (as integer) to ensure
        # we have consistent timestamps calculation. At preprocessing
        # fps parameter is given in fp32, while at inference it is bf16
        # which leads to inaccurate timestamp calculation and causes
        # timestamp values to differ.In rare cases this causes
        # mismatching number of output tokens for tokenized  frame prefixes
        frame_duration_ms_lst = [
            int(1000.0 / metadata["fps"]) for metadata in video_metadata_lst
        ]
        frames_indices_lst = [
            metadata["frames_indices"] for metadata in video_metadata_lst
        ]
        video_num_patches = torch.tensor([len(item) for item in pixel_values_lst_video])

        # Normalization already fused into resize above.
        # Skip the torch.cat copy when there is exactly one video
        if len(pixel_values_lst_video) == 1:
            pixel_values_flat = pixel_values_lst_video[0]
        else:
            pixel_values_flat = torch.cat(pixel_values_lst_video)
        video_inputs = {
            "pixel_values_flat_video": pixel_values_flat,
            "video_num_patches": video_num_patches,
            "frames_indices": frames_indices_lst,
            "frame_duration_ms": torch.tensor(frame_duration_ms_lst),
        }

        patch_size: int = self.config.patch_size
        downsample_ratio = self.config.downsample_ratio

        T = self.video_temporal_patch_size

        for pixel_values, video_metadata, frames_indices, frame_duration_ms in zip(
            pixel_values_lst_video,
            video_metadata_lst,
            frames_indices_lst,
            frame_duration_ms_lst,
        ):
            num_frames = pixel_values.shape[0]
            frame_h, frame_w = pixel_values.shape[-2], pixel_values.shape[-1]
            tokens_in_single_frame = int(
                (frame_h * frame_w // patch_size**2) * (downsample_ratio**2)
            )
            num_tubelets = math.ceil(num_frames / T) if T > 1 else num_frames

            if self.video_pruning_rate is not None and self.video_pruning_rate > 0.0:
                # Start of EVS-specific code
                num_tokens = compute_retained_tokens_count(
                    tokens_per_frame=tokens_in_single_frame,
                    num_frames=num_tubelets,
                    q=self.video_pruning_rate,
                )

                # Here we just need placeholders that won't actually be replaced -
                # we just need to make sure the total number of tokens is correct
                # assign all tokens to the first frame
                tokens_per_frame = [num_tokens] + [0] * (num_tubelets - 1)

                # End of EVS-specific code
            else:
                tokens_per_frame = [tokens_in_single_frame] * num_tubelets

            video_repl = self.get_video_repl(
                tokens_per_frame=tokens_per_frame,
                frames_indices=frames_indices,
                frame_duration_ms=frame_duration_ms,
                tokenizer=self.tokenizer,
                img_start_token_ids=self._img_start_token_ids,
                img_end_token_ids=self._img_end_token_ids,
                img_context_token_ids=self._img_context_token_ids,
                video_temporal_patch_size=T,
            )

            # video_repl.full is a list of token IDs
            # Convert token IDs back to text for the HF processor flow
            video_repl_text = self.tokenizer.decode(
                video_repl.full, skip_special_tokens=False
            )
            text = [t.replace("<video>", video_repl_text, 1) for t in text]

        return text, video_inputs

    def_preprocess_audio(
        self,
        text: list[str],
        audios: list[npt.NDArray],
    ) -> tuple[list[str], dict[str, Any]]:
        if len(audios) == 0:
            return text, {"audio_num_clips": []}

        assert self.audio_extractor is not None
        extractor = self.audio_extractor

        parts = [x for x in re.split(f"({re.escape(AUDIO_CONTEXT)})", text[0]) if x]
        token_count = parts.count(AUDIO_CONTEXT)
        if token_count != len(audios):
            raise ValueError(
                "Number of audio tokens in text does not match the number "
                f"of audios (tokens={token_count}, audios={len(audios)})."
            )
        audio_index = 0
        for idx, part in enumerate(parts):
            if part == AUDIO_CONTEXT:
                audio_repl = self.get_audio_repl(audios[audio_index])
                parts[idx] = audio_repl.full
                audio_index += 1
        text = ["".join(parts)]
        audio_inputs = extractor(audios)
        return text, audio_inputs

    def__call__(
        self,
        text: str | list[str] | None = None,
        images: Image.Image | list[Image.Image] | None = None,
        videos: tuple[npt.NDArray, dict[str, Any]]
        | list[tuple[npt.NDArray, dict[str, Any]]]
        | None = None,
        audios: AudioItem | list[AudioItem] | None = None,
        *,
        return_tensors: str | TensorType | None = None,
        max_num_tiles: int | None = None,
        **kwargs,
    ) -> BatchFeature:
        # Use default if not provided
        if max_num_tiles is None:
            max_num_tiles = self.max_num_tiles

        text = self._make_batch_input(text)
        images = self._make_batch_input(images)
        videos = self._make_batch_input(videos)
        audios = self._make_batch_input(audios)

        text, image_inputs = self._preprocess_image(
            text=text,
            images=images,
            max_num_tiles=max_num_tiles,
        )

        text, video_inputs = self._preprocess_video(
            text=text,
            videos=videos,
        )

        text, audio_inputs = self._preprocess_audio(
            text=text,
            audios=audios,
        )

        text_inputs = self.tokenizer(text, add_special_tokens=False)

        combined_inputs = {**text_inputs, **video_inputs, **audio_inputs}
        frames_indices = combined_inputs.get("frames_indices")
        ragged_frames_indices = (
            isinstance(frames_indices, list)
            and len({len(frame_indices) for frame_indices in frames_indices}) > 1
        )
        if ragged_frames_indices:
            combined_inputs.pop("frames_indices")

        if self.dynamic_tiler is None:
            batch = BatchFeature(
                {**combined_inputs, **image_inputs},
                tensor_type=return_tensors,
            )
        else:
            batch = BatchFeature(combined_inputs, tensor_type=return_tensors)
            # allow images to be exempt from the BatchFeature validation:
            # We will .stack() them in _parse_and_validate_image_input
            batch.update(image_inputs)
        if ragged_frames_indices:
            assert isinstance(frames_indices, list)
            batch["frames_indices"] = [
                torch.as_tensor(frame_indices, dtype=torch.int64)
                for frame_indices in frames_indices
            ]
        return batch

    defget_image_repl(
        self,
        feature_size: int,
        num_patches: int | None,
    ) -> PromptUpdateDetails[str]:
        repl_features = IMG_CONTEXT * feature_size
        repl_full = IMG_START + repl_features + IMG_END

        return PromptUpdateDetails.select_text(repl_full, IMG_CONTEXT)

    defget_audio_repl(
        self,
        audio: npt.NDArray,
    ) -> PromptUpdateDetails[str]:
        assert self.audio_extractor is not None
        num_tokens = self.audio_extractor.audio_token_count(len(audio))
        repl_full = f"{AUDIO_START}{AUDIO_CONTEXT*num_tokens}{AUDIO_END}"
        return PromptUpdateDetails.select_text(repl_full, AUDIO_CONTEXT)

    @classmethod
    defget_video_repl(
        cls,
        *,
        tokens_per_frame: list[int],
        frames_indices: list[int],
        frame_duration_ms: int,
        tokenizer: HfTokenizer,
        img_start_token_ids: list[int],
        img_end_token_ids: list[int],
        img_context_token_ids: list[int],
        video_temporal_patch_size: int = 1,
    ) -> PromptUpdateDetails[list[int]]:
"""
        Build prompt replacement for a video.
        The replacement returned is not actually used to replace the placeholder
        tokens - it's just used to make sure we allocate the correct number
        of tokens.
        Actual replacement is done in embed_multimodal of
        NemotronH_Nano_VL_V2
        (specifically in _process_video_input -> _create_final_video_embeddings).
        There, we create the final embeddings with text embeddings for indicator tokens
        and video embeddings for video tokens.
        This is a single function that handles all cases - non EVS, EVS dummy, EVS real.
        The differentiation is done via tokens_per_frame parameter.
        - non EVS case - constant value same value across all frames
        - EVS dummy - Doesn't matter how tokens are distributed between frames - just
                        make sure the total number of tokens is correct.
        - EVS real (called from get_real_video_repl_for_evs) - different value per frame
        Args:
            tokens_per_frame (list[int]): number of tokens per frame
                (one per tubelet when T > 1)
            frames_indices (list[int]): orig. frame indices
                (one per frame, before tubelet subsampling)
            frame_duration_ms (int): duration of each frame in milliseconds
            tokenizer (TokenizerLike): tokenizer to use for tokenizing frame separators
            img_start_token_ids (list[int]): pre-tokenized IMG_START tokens
            img_end_token_ids (list[int]): pre-tokenized IMG_END tokens
            img_context_token_ids (list[int]): pre-tokenized IMG_CONTEXT tokens
            video_temporal_patch_size (int): temporal patch size for videos
        """
        # TODO: Add support of frame_duration_ms to be None
        # At preprocessing step we should allow absent / metadata without
        # frames_indices field.
        timestamps_enabled = frame_duration_ms is not None
        T = video_temporal_patch_size
        num_frames = len(frames_indices)

        if T > 1 and timestamps_enabled:
            all_timestamps = calculate_timestamps(frames_indices, frame_duration_ms)

            frame_separators = []
            for group_idx, i in enumerate(range(0, num_frames, T)):
                group_frames = []
                for j in range(T):  # Every frame in the group
                    frame_idx = i + j
                    if frame_idx < num_frames:
                        # Valid idx (haven't padded to mult. of T yet)
                        ts = all_timestamps[frame_idx]
                        frame_str = "Frame" if j == 0 else "frame"
                        group_frames.append(
                            f"{frame_str}{frame_idx+1} sampled at {ts:.2f} seconds"
                        )
                if group_frames:
                    # Join by `and` if there are >1 frame, otherwise no `and`
                    # Prepend \n to match training format (except first group)
                    sep = " and ".join(group_frames) + ": "
                    if group_idx > 0:
                        sep = "\n" + sep
                    frame_separators.append(sep)
        elif timestamps_enabled:
            timestamps = calculate_timestamps(frames_indices, frame_duration_ms)

            assert len(timestamps) == len(tokens_per_frame), (
                "timestamps and tokens_per_frame must have the same length"
            )
            frame_separators = [
                ("\n" if i > 0 else "")
                + f"Frame {i+1} sampled at {timestamp:.2f} seconds: "
                for i, timestamp in enumerate(timestamps)
            ]
        else:
            frame_separators = [
                ("\n" if i > 0 else "") + f"Frame {i+1}: "
                for i, _ in enumerate(tokens_per_frame)
            ]

        # Batch-tokenize all frame separators at once — the HuggingFace
        # tokenizers Rust backend parallelizes batch encoding across threads.
        batch_encoded = tokenizer(
            frame_separators,
            add_special_tokens=False,
            return_attention_mask=False,
        )
        frame_separators_tokenized: list[list[int]] = batch_encoded["input_ids"]

        # Tokenize each component independently to avoid tokenizer merging tokens
        # across boundaries. This ensures consistent tokenization regardless of
        # num_tokens_per_frame values.
        all_token_ids = []
        for i, num_tokens in enumerate(tokens_per_frame):
            all_token_ids.extend(frame_separators_tokenized[i])
            all_token_ids.extend(img_start_token_ids)
            all_token_ids.extend(img_context_token_ids * num_tokens)
            all_token_ids.extend(img_end_token_ids)

        return PromptUpdateDetails.from_seq(all_token_ids)
```