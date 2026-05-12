---
title: qwen2_5_omni_thinker - vLLM
url: https://docs.vllm.ai/en/latest/api/vllm/model_executor/models/qwen2_5_omni_thinker/
source: sitemap
fetched_at: 2026-05-07T21:32:49.328389148-03:00
rendered_js: false
word_count: 0
summary: This document defines the PyTorch module class for the Qwen2.5-Omni multimodal model within the vLLM framework, handling initialization, modality-specific feature parsing, and token counting.
tags:
    - multimodal
    - vllm
    - qwen2-5
    - transformer
    - audio-processing
    - video-processing
    - model-implementation
category: api
---

```
@MULTIMODAL_REGISTRY.register_processor(
    Qwen2_5OmniThinkerMultiModalProcessor,
    info=Qwen2_5OmniThinkerProcessingInfo,
    dummy_inputs=Qwen2_5OmniThinkerDummyInputsBuilder,
)
classQwen2_5OmniThinkerForConditionalGeneration(
    nn.Module,
    SupportsMultiModal,
    SupportsPP,
    SupportsLoRA,
    SupportsMRoPE,
    Qwen2_5OmniConditionalGenerationMixin,
):
    hf_to_vllm_mapper = WeightsMapper(
        orig_to_new_prefix={
            "thinker.lm_head.": "language_model.lm_head.",
            "thinker.model.": "language_model.model.",
            "thinker.": "",
        }
    )
    packed_modules_mapping = {
        "qkv_proj": [
            "q_proj",
            "k_proj",
            "v_proj",
        ],
        "attn.qkv": [
            "attn.q",
            "attn.k",
            "attn.v",
        ],
        "gate_up_proj": [
            "gate_proj",
            "up_proj",
        ],
    }

    @classmethod
    defget_placeholder_str(cls, modality: str, i: int) -> str | None:
        if modality.startswith("image"):
            return "<|vision_start|><|IMAGE|><|vision_end|>"
        if modality.startswith("video"):
            return "<|vision_start|><|VIDEO|><|vision_end|>"
        if modality.startswith("audio"):
            return f"Audio {i}: <|audio_bos|><|AUDIO|><|audio_eos|>"

        raise ValueError("Only image, video or audio modality is supported")

    def__init__(self, *, vllm_config: VllmConfig, prefix: str = ""):
        super().__init__()
        self.vllm_config = vllm_config
        thinker_config: Qwen2_5OmniThinkerConfig = (
            vllm_config.model_config.hf_config.thinker_config
        )
        quant_config = vllm_config.quant_config
        multimodal_config = vllm_config.model_config.multimodal_config
        self.config = thinker_config
        self.multimodal_config = multimodal_config
        self.quant_config = quant_config

        # force "use_flash_attention_2=True" to audio tower to align
        # the results.
        if flash_attn is not None:
            audio_config = thinker_config.audio_config
            audio_config._attn_implementation_autoset = True
            audio_config._attn_implementation = "flash_attention_2"
        else:
            logger.warning(
                "flash_attn is not available, the model may not yield the "
                "exactly same result as the transformers implementation "
                "in the audio tower part."
            )

        with self._mark_tower_model(vllm_config, "audio"):
            self.audio_tower = Qwen2_5OmniAudioEncoder(thinker_config.audio_config)

        with self._mark_tower_model(vllm_config, {"image", "video"}):
            self.visual = Qwen2_5_VisionTransformer(
                vision_config=thinker_config.vision_config,
                norm_eps=getattr(thinker_config.text_config, "rms_norm_eps", 1e-6),
                quant_config=quant_config,
                prefix=maybe_prefix(prefix, "visual"),
            )

        with self._mark_language_model(vllm_config):
            self.language_model = init_vllm_registered_model(
                vllm_config=vllm_config,
                prefix=maybe_prefix(prefix, "language_model"),
                hf_config=thinker_config.text_config,
                architectures=["Qwen2ForCausalLM"],
            )

        self.make_empty_intermediate_tensors = (
            self.language_model.make_empty_intermediate_tensors
        )

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
            if (
                input_key in ("input_audio_features")
                and "audio" not in mm_input_by_modality
            ):
                mm_input_by_modality["audio"] = self._parse_and_validate_audio_input(
                    **kwargs
                )
        return mm_input_by_modality

    def_get_audio_for_video_mapping(
        self, mm_features: list[MultiModalFeatureSpec]
    ) -> tuple[dict[int, int], set[int]]:
"""
        Map video offset -> paired audio_feature_length for use_audio_in_video.

        When use_audio_in_video=True, audio is interleaved within video chunks.
        The pairing is based on feature order in mm_features.

        Returns:
            Tuple of (video_offset -> audio_feature_length mapping,
                      set of paired audio offsets to skip)
        """
        videos_with_audio = [
            f
            for f in mm_features
            if f.modality == "video"
            and f.data.get("use_audio_in_video")
            and f.data["use_audio_in_video"].data.item()
        ]
        audios = [f for f in mm_features if f.modality == "audio"]

        # Pair videos with audio features (assumes matching order)
        mapping: dict[int, int] = {}
        paired_audio_offsets: set[int] = set()
        for i, video_f in enumerate(videos_with_audio):
            if i < len(audios):
                audio_len = audios[i].data["audio_feature_lengths"].data.item()
                mapping[video_f.mm_position.offset] = audio_len
                paired_audio_offsets.add(audios[i].mm_position.offset)
        return mapping, paired_audio_offsets

    def_compute_audio_token_count(self, audio_feature_length: int) -> int:
"""Compute audio tokens from feature length."""
        return ((audio_feature_length - 1) // 2 + 1 - 2) // 2 + 1

    defiter_mm_features(
        self, mm_features: list[MultiModalFeatureSpec]
    ) -> Iterator[tuple[int, str, dict[str, Any]]]:
"""
        Iterate over multimodal features sorted by position offset.

        Yields: (offset, modality, feature_data) where feature_data contains:
        - image: {"grid_t", "grid_h", "grid_w", "t_factor"}
        - video: {"grid_t", "grid_h", "grid_w", "t_factor",
                  "use_audio_in_video", "audio_feature_length"}
        - audio: {"audio_feature_length"}
        """
        thinker_config = self.config
        spatial_merge_size = thinker_config.vision_config.spatial_merge_size
        tokens_per_second = getattr(
            thinker_config.vision_config, "tokens_per_second", 25
        )

        # Sort features by offset first, then pair audio with video
        sorted_features = sorted(mm_features, key=lambda f: f.mm_position.offset)
        audio_for_video, paired_audio_offsets = self._get_audio_for_video_mapping(
            sorted_features
        )

        for mm_feature in sorted_features:
            offset = mm_feature.mm_position.offset
            modality = mm_feature.modality

            if modality == "image":
                t, h, w = mm_feature.data["image_grid_thw"].data.tolist()
                yield (
                    offset,
                    "image",
                    {
                        "grid_t": t,
                        "grid_h": h // spatial_merge_size,
                        "grid_w": w // spatial_merge_size,
                        "t_factor": 1.0 * tokens_per_second,
                    },
                )
            elif modality == "video":
                t, h, w = mm_feature.data["video_grid_thw"].data.tolist()
                second_per_grid_ts = 1.0
                if mm_feature.data.get("second_per_grid_ts"):
                    second_per_grid_ts = mm_feature.data[
                        "second_per_grid_ts"
                    ].data.item()
                use_audio_in_video = False
                if mm_feature.data.get("use_audio_in_video"):
                    use_audio_in_video = bool(
                        mm_feature.data["use_audio_in_video"].data.item()
                    )

                yield (
                    offset,
                    "video",
                    {
                        "grid_t": t,
                        "grid_h": h // spatial_merge_size,
                        "grid_w": w // spatial_merge_size,
                        "t_factor": second_per_grid_ts * tokens_per_second,
                        "use_audio_in_video": use_audio_in_video,
                        "audio_feature_length": audio_for_video.get(offset),
                    },
                )
            elif modality == "audio":
                # Skip audio that's paired with video (handled in video case)
                if offset not in paired_audio_offsets:
                    audio_len = mm_feature.data["audio_feature_lengths"].data.item()
                    yield offset, "audio", {"audio_feature_length": audio_len}

    def_compute_interleaved_positions(
        self, start_idx: int, data: dict[str, Any]
    ) -> tuple[np.ndarray, int]:
"""
        Compute positions for interleaved video+audio chunks.

        Returns: (position_ids, total_token_count)
        """
        grid_t = data["grid_t"]
        grid_h = data["grid_h"]
        grid_w = data["grid_w"]
        t_factor = data["t_factor"]
        audio_len = data["audio_feature_length"]

        thinker_config = self.config
        tokens_per_second = getattr(
            thinker_config.vision_config, "tokens_per_second", 25
        )
        seconds_per_chunk = thinker_config.seconds_per_chunk
        t_ntoken_per_chunk = int(tokens_per_second * seconds_per_chunk)

        # Temporal indices with scaling
        t_index = (np.arange(grid_t) * t_factor).astype(np.int64)

        # Split temporal indices into chunks
        t_index_split_chunk: list[list[int]] = [
            [] for _ in range((int(t_index.max()) // t_ntoken_per_chunk) + 1)
        ]
        for t_val in t_index:
            idx = int(t_val) // t_ntoken_per_chunk
            t_index_split_chunk[idx].append(int(t_val))

        pure_audio_len = self._compute_audio_token_count(audio_len)
        added_audio_len = 0
        pos_ids_list: list[np.ndarray] = []
        audio_start_idx = start_idx

        for t_chunk in t_index_split_chunk:
            if not t_chunk:
                continue

            chunk_t = len(t_chunk)

            # Build vision positions for this chunk
            h_indices = np.tile(
                np.arange(grid_h).reshape(1, -1, 1), (chunk_t, 1, grid_w)
            ).flatten()
            w_indices = np.tile(
                np.arange(grid_w).reshape(1, 1, -1), (chunk_t, grid_h, 1)
            ).flatten()
            t_indices = np.repeat(np.array(t_chunk), grid_h * grid_w)

            vision_pos = np.stack([t_indices, h_indices, w_indices]) + start_idx
            pos_ids_list.append(vision_pos)

            # Audio tokens for this chunk
            audio_chunk_size = min(t_ntoken_per_chunk, pure_audio_len - added_audio_len)
            if audio_chunk_size > 0:
                audio_pos = (
                    np.broadcast_to(np.arange(audio_chunk_size), (3, audio_chunk_size))
                    + audio_start_idx
                )
                pos_ids_list.append(audio_pos)
                audio_start_idx = audio_start_idx + audio_chunk_size
                added_audio_len += audio_chunk_size

        # Handle remaining audio that doesn't fit in chunks
        if added_audio_len < pure_audio_len:
            remaining = pure_audio_len - added_audio_len
            remaining_audio_pos = (
                np.broadcast_to(np.arange(remaining), (3, remaining)) + audio_start_idx
            )
            pos_ids_list.append(remaining_audio_pos)

        # Calculate total token count
        vision_tokens = grid_t * grid_h * grid_w
        total_tokens = vision_tokens + pure_audio_len

        return np.concatenate(pos_ids_list, axis=1), total_tokens

    defget_mrope_input_positions(
        self,
        input_tokens: list[int],
        mm_features: list[MultiModalFeatureSpec],
    ) -> tuple[torch.Tensor, int]:
"""
        Compute M-RoPE input positions using mm_features directly.

        Example for use_audio_in_video case:
            (V_i are vision position ids, A_i are audio position ids)

            |V_1 ...    V_n|A_1 ...   A_n|V_n+1 ... V_2n|A_n+1 ... A_2n|...
            |vision chunk 1|audio chunk 1|vision chunk 2|audio chunk 2 |...
        """
        llm_pos_ids_list: list[np.ndarray] = []
        st = 0

        for offset, modality, data in self.iter_mm_features(mm_features):
            # Add text segment before this feature
            text_len = offset - st
            st_idx = int(llm_pos_ids_list[-1].max()) + 1 if llm_pos_ids_list else 0
            if text_len > 0:
                llm_pos_ids_list.append(
                    np.broadcast_to(np.arange(text_len), (3, text_len)) + st_idx
                )
                st_idx += text_len

            if modality == "audio":
                # Standalone audio positions
                audio_tokens = self._compute_audio_token_count(
                    data["audio_feature_length"]
                )
                llm_pos_ids_list.append(
                    np.broadcast_to(np.arange(audio_tokens), (3, audio_tokens)) + st_idx
                )
                st = offset + audio_tokens

            elif modality == "image":
                # Image uses np.indices like Qwen2-VL
                grid_t = data["grid_t"]
                grid_h = data["grid_h"]
                grid_w = data["grid_w"]
                t_factor = data["t_factor"]

                grid_indices = np.indices((grid_t, grid_h, grid_w))
                if t_factor != 1.0:
                    grid_indices[0] = (grid_indices[0] * t_factor).astype(np.int64)
                llm_pos_ids_list.append(grid_indices.reshape(3, -1) + st_idx)
                st = offset + grid_t * grid_h * grid_w

            elif modality == "video":
                grid_t = data["grid_t"]
                grid_h = data["grid_h"]
                grid_w = data["grid_w"]
                t_factor = data["t_factor"]

                if not data["use_audio_in_video"]:
                    # Simple video (same as Qwen2-VL)
                    grid_indices = np.indices((grid_t, grid_h, grid_w))
                    if t_factor != 1.0:
                        grid_indices[0] = (grid_indices[0] * t_factor).astype(np.int64)
                    llm_pos_ids_list.append(grid_indices.reshape(3, -1) + st_idx)
                    st = offset + grid_t * grid_h * grid_w
                else:
                    # Interleaved video+audio
                    pos_ids, token_count = self._compute_interleaved_positions(
                        st_idx, data
                    )
                    llm_pos_ids_list.append(pos_ids)
                    st = offset + token_count

        # Add trailing text
        if st < len(input_tokens):
            st_idx = int(llm_pos_ids_list[-1].max()) + 1 if llm_pos_ids_list else 0
            text_len = len(input_tokens) - st
            llm_pos_ids_list.append(
                np.broadcast_to(np.arange(text_len), (3, text_len)) + st_idx
            )

        llm_positions = np.concatenate(llm_pos_ids_list, axis=1).reshape(3, -1)
        mrope_position_delta = int(llm_positions.max()) + 1 - len(input_tokens)

        return torch.from_numpy(llm_positions), mrope_position_delta

    defembed_multimodal(self, **kwargs: object) -> MultiModalEmbeddings:
        mm_input_by_modality = self._parse_and_validate_multimodal_inputs(**kwargs)
        if not mm_input_by_modality:
            return []

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
            if modality == "audio":
                audio_embeddings = self._process_audio_input(multimodal_input)
                multimodal_embeddings += tuple(audio_embeddings)
        return multimodal_embeddings

    defembed_input_ids(
        self,
        input_ids: torch.Tensor,
        multimodal_embeddings: MultiModalEmbeddings | None = None,
        *,
        is_multimodal: torch.Tensor | None = None,
    ) -> torch.Tensor:
        if multimodal_embeddings is None or is_multimodal is None:
            return super().embed_input_ids(input_ids)

        inputs_embeds = self._embed_text_input_ids(
            input_ids,
            self.get_language_model().embed_input_ids,
            is_multimodal=is_multimodal,
        )

        if len(multimodal_embeddings) == 0:
            return inputs_embeds

        # Check for audio-in-video: interleaved video and audio tokens
        # in the multimodal region. Only use the interleaved path when
        # needed; otherwise fall back to the default parent implementation.
        video_token_id = self.config.video_token_index
        audio_token_id = self.config.audio_token_index

        input_ids_cpu = input_ids.cpu()
        is_video = is_multimodal & (input_ids_cpu == video_token_id)
        is_audio = is_multimodal & (input_ids_cpu == audio_token_id)

        num_video = is_video.sum().item()
        num_audio = is_audio.sum().item()

        if check_interleaved_audio_video(is_video, is_audio, num_video, num_audio):
            inputs_embeds = self._embed_text_input_ids(
                input_ids,
                self.get_language_model().embed_input_ids,
                is_multimodal=is_multimodal,
            )
            return merge_interleaved_embeddings(
                inputs_embeds,
                multimodal_embeddings,
                is_video,
                is_audio,
                is_multimodal,
                num_video,
                num_audio,
            )

        # Default: standard merge (no interleaving), same as parent class
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
    ) -> torch.Tensor | IntermediateTensors:
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
        loader = AutoWeightsLoader(self, skip_prefixes=["talker.", "token2wav."])
        return loader.load_weights(weights, mapper=self.hf_to_vllm_mapper)

    defget_mm_mapping(self) -> MultiModelKeys:
"""
        Get the module prefix in multimodal models
        """
        return MultiModelKeys.from_string_field(
            language_model="language_model",
            connector="merger.",
            tower_model=["visual.", "audio_tower."],
        )
```