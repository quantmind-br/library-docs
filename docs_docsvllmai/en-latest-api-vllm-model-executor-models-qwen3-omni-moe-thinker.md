---
title: qwen3_omni_moe_thinker - vLLM
url: https://docs.vllm.ai/en/latest/api/vllm/model_executor/models/qwen3_omni_moe_thinker/
source: sitemap
fetched_at: 2026-05-07T21:33:05.25563639-03:00
rendered_js: false
word_count: 0
summary: This document defines the PyTorch model implementation for the Qwen3OmniMoeThinker architecture, integrating multimodal vision and audio processing with a causal language model.
tags:
    - multimodal
    - vllm
    - deep-learning
    - model-architecture
    - pytorch
    - qwen
    - transformer
category: concept
---

```
@MULTIMODAL_REGISTRY.register_processor(
    Qwen3OmniMoeThinkerMultiModalProcessor,
    info=Qwen3OmniMoeThinkerProcessingInfo,
    dummy_inputs=Qwen3OmniMoeThinkerDummyInputsBuilder,
)
classQwen3OmniMoeThinkerForConditionalGeneration(
    nn.Module,
    SupportsMultiModal,
    SupportsPP,
    SupportsMRoPE,
    Qwen3OmniMoeConditionalGenerationMixin,
    SupportsTranscription,
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
        "gate_up_proj": [
            "gate_proj",
            "up_proj",
        ],
    }

    supported_languages = ISO639_1_SUPPORTED_LANGS

    @classmethod
    defget_placeholder_str(cls, modality: str, i: int) -> str | None:
        if modality.startswith("image"):
            return "<|vision_start|><|image_pad|><|vision_end|>"
        if modality.startswith("video"):
            return "<|vision_start|><|video_pad|><|vision_end|>"
        if modality.startswith("audio"):
            return "<|audio_start|><|audio_pad|><|audio_end|>"

        raise ValueError("Only image, video or audio modality is supported")

    def__init__(self, *, vllm_config: VllmConfig, prefix: str = ""):
        super().__init__()
        self.vllm_config = vllm_config  # needed for torch compile forward context
        thinker_config: Qwen3OmniMoeThinkerConfig = (
            vllm_config.model_config.hf_config.thinker_config
        )
        quant_config = vllm_config.quant_config
        multimodal_config = vllm_config.model_config.multimodal_config
        self.config = thinker_config
        self.multimodal_config = multimodal_config
        self.quant_config = quant_config

        with self._mark_tower_model(vllm_config, "audio"):
            self.audio_tower = Qwen3OmniMoeAudioEncoder(
                thinker_config.audio_config,
                prefix=maybe_prefix(prefix, "audio_tower"),
            )

        self.use_deepstack = hasattr(
            thinker_config.vision_config, "deepstack_visual_indexes"
        )
        self.deepstack_num_level = (
            len(thinker_config.vision_config.deepstack_visual_indexes)
            if self.use_deepstack
            else 0
        )
        self.visual_dim = thinker_config.vision_config.out_hidden_size
        self.multiscale_dim = self.visual_dim * self.deepstack_num_level

        with self._mark_tower_model(vllm_config, {"image", "video"}):
            self.visual = Qwen3Omni_VisionTransformer(
                vision_config=thinker_config.vision_config,
                norm_eps=getattr(thinker_config.text_config, "rms_norm_eps", 1e-6),
                quant_config=quant_config,
                prefix=maybe_prefix(prefix, "visual"),
            )

            # register buffer for deepstack
            if self.use_deepstack:
                self.deepstack_input_embeds = [
                    torch.zeros(
                        vllm_config.scheduler_config.max_num_batched_tokens,
                        thinker_config.text_config.hidden_size,
                    )
                    for _ in range(self.deepstack_num_level)
                ]
                # Tracks the valid token span currently stored in the buffer.
                # Zero means there is no active deepstack payload to consume.
                self.deepstack_input_embeds_num_tokens = 0

        with self._mark_language_model(vllm_config):
            self.language_model = Qwen3MoeLLMForCausalLM(
                vllm_config=vllm_config.with_hf_config(
                    thinker_config.text_config,
                    architectures=["Qwen3MoeForCausalLM"],
                ),
                prefix=maybe_prefix(prefix, "language_model"),
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

    defembed_multimodal(self, **kwargs: object) -> MultiModalEmbeddings | None:
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
        inputs_embeds = self._embed_text_input_ids(
            input_ids,
            self.language_model.embed_input_ids,
            is_multimodal=is_multimodal,
        )

        if multimodal_embeddings is None or len(multimodal_embeddings) == 0:
            return inputs_embeds

        # Detect interleaved audio-in-video early, since it affects
        # both the deepstack path and the final embedding merge.
        video_token_id = self.config.video_token_id
        audio_token_id = self.config.audio_token_id
        input_ids_cpu = input_ids.cpu()
        is_video = is_multimodal & (input_ids_cpu == video_token_id)
        is_audio = is_multimodal & (input_ids_cpu == audio_token_id)
        num_video = is_video.sum().item()
        num_audio = is_audio.sum().item()

        is_interleaved = check_interleaved_audio_video(
            is_video, is_audio, num_video, num_audio
        )

        deepstack_input_embeds = None
        # split the feat dim to obtain multi-scale visual feature
        has_vision_embeddings = [
            embeddings.shape[-1] != self.config.text_config.hidden_size
            for embeddings in multimodal_embeddings
        ]
        if self.visual.deepstack_visual_indexes is not None and any(
            has_vision_embeddings
        ):
            multiscale_len = len(self.visual.deepstack_visual_indexes)
            multimodal_embeddings_multiscale = []

            if is_interleaved:
                # Use input_ids-based mask for correct vision positions
                # when audio and video tokens are interleaved.
                is_vision = is_video.clone()
            else:
                is_vision = torch.zeros_like(is_multimodal)
                mm_positions = torch.nonzero(is_multimodal, as_tuple=True)[0]
                mm_position_idx = 0

            for index, embeddings in enumerate(multimodal_embeddings):
                num_tokens = embeddings.shape[0]

                # Vision embeddings
                if embeddings.shape[-1] != self.config.text_config.hidden_size:
                    visual_dim = embeddings.shape[-1] // (multiscale_len + 1)
                    multi_dim = visual_dim * multiscale_len
                    embeddings_main, embeddings_multiscale = torch.split(
                        embeddings, [visual_dim, multi_dim], dim=-1
                    )
                    multimodal_embeddings[index] = embeddings_main
                    multimodal_embeddings_multiscale.append(embeddings_multiscale)
                    if not is_interleaved:
                        current_positions = mm_positions[
                            mm_position_idx : mm_position_idx + num_tokens
                        ]
                        is_vision[current_positions] = True

                # Audio embeddings
                else:
                    if not is_interleaved:
                        current_positions = mm_positions[
                            mm_position_idx : mm_position_idx + num_tokens
                        ]
                        is_vision[current_positions] = False

                if not is_interleaved:
                    mm_position_idx += num_tokens

            deepstack_input_embeds = inputs_embeds.new_zeros(
                inputs_embeds.size(0), multiscale_len * inputs_embeds.size(1)
            )
            deepstack_input_embeds = _merge_multimodal_embeddings(
                inputs_embeds=deepstack_input_embeds,
                multimodal_embeddings=multimodal_embeddings_multiscale,
                is_multimodal=is_vision,
            )
            deepstack_input_embeds = (
                deepstack_input_embeds.view(
                    inputs_embeds.shape[0], multiscale_len, visual_dim
                )
                .permute(1, 0, 2)
                .contiguous()
            )
            self._set_deepstack_input_embeds(deepstack_input_embeds)

        if is_interleaved:
            return merge_interleaved_embeddings(
                inputs_embeds,
                multimodal_embeddings,
                is_video,
                is_audio,
                is_multimodal,
                num_video,
                num_audio,
            )

        # Default: standard merge (no interleaving), same as parent class.
        # multimodal_embeddings may have been updated above (deepstack
        # main-scale). Use super() to stay consistent with the parent
        # implementation and avoid issues seen in Qwen2.5-Omni (#34506).
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

        if inputs_embeds is not None and get_pp_group().is_first_rank:
            deepstack_input_embeds = self._get_deepstack_input_embeds(
                inputs_embeds.size(0)
            )
        else:
            deepstack_input_embeds = None

        hidden_states = self.language_model.model(
            input_ids,
            positions,
            intermediate_tensors,
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
        loader = AutoWeightsLoader(
            self,
            skip_prefixes=["talker.", "code2wav."],
        )
        loaded_weights = loader.load_weights(weights, mapper=self.hf_to_vllm_mapper)

        return loaded_weights

    def_compute_audio_token_count(self, audio_feature_length: int) -> int:
"""Compute audio tokens from feature length using Qwen3-Omni formula."""
        return _get_feat_extract_output_lengths(
            torch.tensor([audio_feature_length])
        ).item()

    def_get_audio_for_video_mapping(
        self, mm_features: list[MultiModalFeatureSpec]
    ) -> tuple[dict[int, int], set[int]]:
"""
        Map video offset -> paired audio_feature_length for use_audio_in_video.

        When use_audio_in_video=True, audio is interleaved within video.
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

        mapping: dict[int, int] = {}
        paired_audio_offsets: set[int] = set()
        for i, video_f in enumerate(videos_with_audio):
            if i < len(audios):
                audio_len = audios[i].data["audio_feature_lengths"].data.item()
                mapping[video_f.mm_position.offset] = audio_len
                paired_audio_offsets.add(audios[i].mm_position.offset)
        return mapping, paired_audio_offsets

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
        config = self.config
        spatial_merge_size = config.vision_config.spatial_merge_size
        position_id_per_seconds = config.position_id_per_seconds

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
                        "t_factor": position_id_per_seconds,
                    },
                )
            elif modality == "video":
                t, h, w = mm_feature.data["video_grid_thw"].data.tolist()
                second_per_grid_ts = 2.0
                if mm_feature.data.get("second_per_grid_ts"):
                    second_per_grid_ts = mm_feature.data[
                        "second_per_grid_ts"
                    ].data.item()
                use_audio_in_video = bool(
                    mm_feature.data.get("use_audio_in_video")
                    and mm_feature.data["use_audio_in_video"].data.item()
                )

                yield (
                    offset,
                    "video",
                    {
                        "grid_t": t,
                        "grid_h": h // spatial_merge_size,
                        "grid_w": w // spatial_merge_size,
                        "t_factor": second_per_grid_ts * position_id_per_seconds,
                        "use_audio_in_video": use_audio_in_video,
                        "audio_feature_length": audio_for_video.get(offset),
                    },
                )
            elif modality == "audio":
                if offset not in paired_audio_offsets:
                    audio_len = mm_feature.data["audio_feature_lengths"].data.item()
                    yield offset, "audio", {"audio_feature_length": audio_len}

    def_compute_interleaved_positions(
        self, start_idx: int, data: dict[str, Any]
    ) -> tuple[np.ndarray, int]:
"""
        Compute positions for interleaved video+audio using Qwen3 token-by-token
        interleaving logic.

        Returns: (position_ids [3, N], total_token_count)
        """
        grid_t = data["grid_t"]
        grid_h = data["grid_h"]
        grid_w = data["grid_w"]
        t_factor = data["t_factor"]
        audio_feature_length = data["audio_feature_length"]

        audio_len = self._compute_audio_token_count(audio_feature_length)

        h_index = np.tile(
            np.arange(grid_h).reshape(1, -1, 1), (grid_t, 1, grid_w)
        ).flatten()
        w_index = np.tile(
            np.arange(grid_w).reshape(1, 1, -1), (grid_t, grid_h, 1)
        ).flatten()
        t_index_raw = np.arange(grid_t)
        t_index_scaled = (t_index_raw * t_factor).astype(np.int64)
        t_index = np.repeat(t_index_scaled, grid_h * grid_w)

        video_pos = np.stack([t_index, h_index, w_index]) + start_idx
        audio_pos = np.broadcast_to(np.arange(audio_len), (3, audio_len)) + start_idx

        video_t_values = video_pos[0]
        audio_t_values = audio_pos[0]

        pos_ids_list: list[np.ndarray] = []
        video_idx, audio_idx = 0, 0
        num_video = grid_t * grid_h * grid_w

        while video_idx < num_video and audio_idx < audio_len:
            if video_t_values[video_idx] <= audio_t_values[audio_idx]:
                pos_ids_list.append(video_pos[:, video_idx : video_idx + 1])
                video_idx += 1
            else:
                pos_ids_list.append(audio_pos[:, audio_idx : audio_idx + 1])
                audio_idx += 1

        if video_idx < num_video:
            pos_ids_list.append(video_pos[:, video_idx:])
        if audio_idx < audio_len:
            pos_ids_list.append(audio_pos[:, audio_idx:])

        total_tokens = num_video + audio_len
        return np.concatenate(pos_ids_list, axis=1), total_tokens

    @classmethod
    defget_speech_to_text_config(
        cls, model_config: ModelConfig, task_type: str
    ) -> SpeechToTextConfig:
        processor = cached_processor_from_config(
            model_config, processor_cls=Qwen3OmniMoeProcessor
        )
        return SpeechToTextConfig(
            max_audio_clip_s=processor.feature_extractor.chunk_length,
            sample_rate=processor.feature_extractor.sampling_rate,
            min_energy_split_window_size=None,
        )

    @classmethod
    defget_generation_prompt(cls, stt_params: SpeechToTextParams) -> PromptType:
"""
        Construct a transcription/translation prompt for Qwen3-Omni.
        """
        audio = stt_params.audio
        stt_config = stt_params.stt_config
        model_config = stt_params.model_config
        language = stt_params.language
        task_type = stt_params.task_type
        to_language = stt_params.to_language
        request_prompt = stt_params.request_prompt
        # Transcribe this audio [into <language>] | for transcription
        # Translate this audio [from <language> into <to_language>] | for translation
        instruction = "Transcribe" if task_type == "transcribe" else "Translate"
        instruction += " this audio"

        # Default to_language to English for translation
        if task_type == "translate" and to_language is None:
            to_language = "en"

        # Get full language names from supported_languages mapping
        full_lang_name = cls.supported_languages.get(language, "")
        full_lang_name_to = cls.supported_languages.get(to_language, "")

        if task_type == "transcribe" and full_lang_name:
            instruction += f" into {full_lang_name}"
        elif task_type == "translate":
            if full_lang_name:
                instruction += f" from {full_lang_name}"
            if full_lang_name_to:
                instruction += f" into {full_lang_name_to}"

        instruction += "."

        if request_prompt:
            instruction += f" {request_prompt}"

        processor = cached_processor_from_config(
            model_config, processor_cls=Qwen3OmniMoeProcessor
        )
        # Audio placeholder format: <|audio_start|><|audio_pad|><|audio_end|>
        audio_placeholder = "<|audio_start|><|audio_pad|><|audio_end|>"
        user_content = f"{audio_placeholder}{instruction}"

        messages = [{"role": "user", "content": user_content}]
        prompt = processor.apply_chat_template(
            messages,
            tokenize=False,
            add_generation_prompt=True,
        )

        audio_data = (audio, stt_config.sample_rate)
        prompts_dict = {"multi_modal_data": {"audio": audio_data}, "prompt": prompt}
        return cast(PromptType, prompts_dict)

    defget_mrope_input_positions(
        self,
        input_tokens: list[int],
        mm_features: list[MultiModalFeatureSpec],
    ) -> tuple[torch.Tensor, int]:
"""Compute M-RoPE input positions using mm_features directly."""
        seq_len = len(input_tokens)

        llm_pos_ids_list: list[np.ndarray] = []
        st = 0

        for offset, modality, data in self.iter_mm_features(mm_features):
            text_len = offset - st
            st_idx = int(llm_pos_ids_list[-1].max()) + 1 if llm_pos_ids_list else 0

            if text_len > 0:
                llm_pos_ids_list.append(
                    np.broadcast_to(np.arange(text_len), (3, text_len)) + st_idx
                )
                st_idx += text_len

            bos_pos = np.broadcast_to(np.array([st_idx]), (3, 1))
            llm_pos_ids_list.append(bos_pos)
            st_idx += 1

            if modality == "audio":
                audio_tokens = self._compute_audio_token_count(
                    data["audio_feature_length"]
                )
                audio_pos = (
                    np.broadcast_to(np.arange(audio_tokens), (3, audio_tokens)) + st_idx
                )
                llm_pos_ids_list.append(audio_pos)
                st_idx = int(audio_pos.max()) + 1

                eos_pos = np.broadcast_to(np.array([st_idx]), (3, 1))
                llm_pos_ids_list.append(eos_pos)
                st = offset + 1 + audio_tokens + 1

            elif modality == "image":
                grid_t = data["grid_t"]
                grid_h = data["grid_h"]
                grid_w = data["grid_w"]
                t_factor = data["t_factor"]

                grid_indices = np.indices((grid_t, grid_h, grid_w))
                if t_factor != 1.0:
                    grid_indices[0] = (grid_indices[0] * t_factor).astype(np.int64)
                llm_pos_ids_list.append(grid_indices.reshape(3, -1) + st_idx)

                image_len = grid_t * grid_h * grid_w
                st_idx = int(llm_pos_ids_list[-1].max()) + 1

                eos_pos = np.broadcast_to(np.array([st_idx]), (3, 1))
                llm_pos_ids_list.append(eos_pos)
                st = offset + 1 + image_len + 1

            elif modality == "video":
                grid_t = data["grid_t"]
                grid_h = data["grid_h"]
                grid_w = data["grid_w"]
                t_factor = data["t_factor"]

                if not data["use_audio_in_video"]:
                    grid_indices = np.indices((grid_t, grid_h, grid_w))
                    if t_factor != 1.0:
                        grid_indices[0] = (grid_indices[0] * t_factor).astype(np.int64)
                    llm_pos_ids_list.append(grid_indices.reshape(3, -1) + st_idx)

                    video_len = grid_t * grid_h * grid_w
                    st_idx = int(llm_pos_ids_list[-1].max()) + 1

                    eos_pos = np.broadcast_to(np.array([st_idx]), (3, 1))
                    llm_pos_ids_list.append(eos_pos)
                    st = offset + 1 + video_len + 1
                else:
                    audio_bos_pos = np.broadcast_to(np.array([st_idx - 1]), (3, 1))
                    llm_pos_ids_list.append(audio_bos_pos)

                    pos_ids, _ = self._compute_interleaved_positions(st_idx, data)
                    llm_pos_ids_list.append(pos_ids)
                    st_idx = int(pos_ids.max()) + 1

                    eos_pos = np.broadcast_to(np.array([st_idx]), (3, 1))
                    llm_pos_ids_list.append(eos_pos)
                    llm_pos_ids_list.append(eos_pos)

                    video_len = grid_t * grid_h * grid_w
                    audio_len = self._compute_audio_token_count(
                        data["audio_feature_length"]
                    )
                    st = offset + 2 + video_len + audio_len + 2

        if st < seq_len:
            st_idx = int(llm_pos_ids_list[-1].max()) + 1 if llm_pos_ids_list else 0
            text_len = seq_len - st
            llm_pos_ids_list.append(
                np.broadcast_to(np.arange(text_len), (3, text_len)) + st_idx
            )

        llm_positions = np.concatenate(llm_pos_ids_list, axis=1).reshape(3, -1)
        if llm_positions.shape[1] != seq_len:
            raise RuntimeError("Position ids length mismatch with input ids length")

        mrope_position_delta = int(llm_positions.max()) + 1 - seq_len
        return torch.from_numpy(llm_positions), mrope_position_delta

    defget_mm_mapping(self) -> MultiModelKeys:
"""
        Get the module prefix in multimodal models
        """
        return MultiModelKeys.from_string_field(
            language_model="language_model",
            connector="visual.merger",
            tower_model=["visual.", "audio_tower."],
        )
```