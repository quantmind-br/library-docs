---
title: voxtral - vLLM
url: https://docs.vllm.ai/en/latest/api/vllm/model_executor/models/voxtral/
source: sitemap
fetched_at: 2026-05-07T21:33:44.148869288-03:00
rendered_js: false
word_count: 0
summary: This document defines the VoxtralForConditionalGeneration class, a multimodal PyTorch module designed for speech-to-text tasks by integrating a Whisper-based audio encoder with a language model.
tags:
    - multimodal
    - speech-to-text
    - pytorch
    - vllm
    - audio-processing
    - transformer-model
category: reference
---

```
@MULTIMODAL_REGISTRY.register_processor(
    VoxtralMultiModalProcessor,
    info=VoxtralProcessingInfo,
    dummy_inputs=VoxtralDummyInputsBuilder,
)
classVoxtralForConditionalGeneration(
    nn.Module, SupportsMultiModal, SupportsPP, SupportsLoRA, SupportsTranscription
):
    supported_languages = ISO639_1_SUPPORTED_LANGS
    # transformers' currently has limited support for MistralCommon backend
    # and cached_get_processor. Let's skip until fixed
    skip_warmup_audio_preprocessing = True

    packed_modules_mapping = {
        "qkv_proj": ["q_proj", "k_proj", "v_proj"],
        "gate_up_proj": ["gate_proj", "up_proj"],
    }

    def__init__(self, *, vllm_config: VllmConfig, prefix: str = ""):
        super().__init__()
        self.tokenizer = cached_tokenizer_from_config(vllm_config.model_config)

        # update quant config to so that ignored module and target module names
        # match the vLLM model names
        if hasattr(vllm_config, "quant_config"):
            vllm_config.quant_config = self.maybe_update_quant_config(
                vllm_config.quant_config
            )

        config = vllm_config.model_config.hf_config
        self.config = config
        self.downsample_factor = self.config.audio_config.downsample_factor

        with self._mark_language_model(vllm_config):
            self.language_model = init_vllm_registered_model(
                vllm_config=vllm_config,
                hf_config=config.text_config,
                prefix=maybe_prefix(prefix, "language_model"),
            )

        with self._mark_tower_model(vllm_config, "audio"):
            self.whisper_encoder = VoxtralEncoderModel(
                vllm_config.with_hf_config(config.audio_config),
                prefix=maybe_prefix(prefix, "whisper_encoder"),
            )
            self.audio_language_adapter = AudioLanguageAdapter(
                hidden_size=config.audio_config.d_model * self.downsample_factor,
                dim=config.text_config.hidden_size,
            )

    defget_mm_mapping(self) -> MultiModelKeys:
"""Get module prefix for multimodal models to filter LoRA modules."""
        return MultiModelKeys.from_string_field(
            language_model="language_model",
            connector="audio_language_adapter",
            tower_model=["whisper_encoder"],
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

    defembed_multimodal(
        self, **kwargs
    ) -> list[torch.Tensor] | torch.Tensor | tuple[torch.Tensor, ...] | None:
        audio_inputs = self._parse_and_validate_audio_arrays(**kwargs)
        if audio_inputs is None:
            return None

        audio_embeddings = self.whisper_encoder(audio_inputs)

        for i, audio_embedding in enumerate(audio_embeddings):
            seq_len, dim = audio_embedding.shape
            # Pad such that seq_len is divisible by downsample_factor
            target_seq_len = self.downsample_factor * math.ceil(
                seq_len / self.downsample_factor
            )
            audio_embedding = torch.nn.functional.pad(
                audio_embedding,
                (0, 0, 0, target_seq_len - seq_len),
            )
            audio_embeddings[i] = audio_embedding.reshape(
                target_seq_len // self.downsample_factor, dim * self.downsample_factor
            )

        # Concat, project and resplit
        audio_embeddings_packed = torch.cat(audio_embeddings, dim=0)
        audio_embeddings_packed = self.audio_language_adapter(audio_embeddings_packed)
        audio_embeddings = torch.split(
            audio_embeddings_packed, [a.shape[0] for a in audio_embeddings], dim=0
        )

        return audio_embeddings

    def_parse_and_validate_audio_arrays(
        self, **kwargs: object
    ) -> list[torch.Tensor] | None:
        audio_arrays = kwargs.pop("audio_arrays", None)
        if audio_arrays is None:
            return None

        if not isinstance(audio_arrays, (torch.Tensor, list)):
            raise ValueError(
                f"Incorrect type of audio_arrays. Got type: {type(audio_arrays)}"
            )

        if isinstance(audio_arrays, torch.Tensor):
            audio_arrays = list(audio_arrays.unbind(0))
        return audio_arrays

    defcompute_logits(
        self,
        hidden_states: torch.Tensor,
    ) -> torch.Tensor | None:
        return self.language_model.compute_logits(hidden_states)

    @classmethod
    defget_speech_to_text_config(
        cls, model_config: ModelConfig, task_type: str
    ) -> SpeechToTextConfig:
        tokenizer = cached_tokenizer_from_config(model_config)
        audio_config = tokenizer.instruct.audio_encoder.audio_config
        max_audio_clip_s = audio_config.chunk_length_s
        sample_rate = audio_config.sampling_rate
        return SpeechToTextConfig(
            max_audio_clip_s=max_audio_clip_s,
            sample_rate=sample_rate,
            # mistral_common and whisper encoder take care of chunking
            min_energy_split_window_size=None,
        )

    @classmethod
    # for speech-to-text transcription
    defget_generation_prompt(
        cls,
        stt_params: SpeechToTextParams,
    ) -> PromptType:
        audio = stt_params.audio
        model_config = stt_params.model_config
        stt_config = stt_params.stt_config
        language = stt_params.language

        tokenizer = cached_tokenizer_from_config(model_config)
        audio = Audio(audio, int(stt_config.sample_rate), format="wav")  # lossless
        req = TranscriptionRequest(
            model=model_config.model,
            audio=RawAudio.from_audio(audio),
            language=language,
        )

        tokenized = tokenizer.instruct.encode_transcription(req)

        return TokensPrompt(
            prompt_token_ids=tokenized.tokens,
            multi_modal_data={
                "audio": [
                    (audio.audio_array, stt_config.sample_rate)
                    for audio in tokenized.audios
                ],
            },
        )

    @classmethod
    defget_num_audio_tokens(
        cls,
        audio_duration_s: float,
        stt_config: SpeechToTextConfig,
        model_config: ModelConfig,
    ) -> int | None:
"""
        Map from audio duration to number of audio tokens produced by the ASR
        model, without running a forward pass.
        This is used for estimating the amount of processing for this audio.
        """
        tokenizer = cached_tokenizer_from_config(model_config)
        feature_extractor = MistralCommonFeatureExtractor(
            tokenizer.instruct.audio_encoder
        )
        return feature_extractor.get_num_audio_tokens(
            int(audio_duration_s * stt_config.sample_rate)
        )

    defload_weights(self, weights: Iterable[tuple[str, torch.Tensor]]) -> set[str]:
        remapping_rules = [
            (r"mm_streams_embeddings.embedding_module\.(.*)", r"\1"),
            (r"mm_whisper_embeddings\.(.*)", r"\1"),
            (r"audio_language_projection\.(.*)", r"audio_language_adapter.\1"),
            (
                r"audio_language_adapter\.0\.weight",
                r"audio_language_adapter.w_in.weight",
            ),
            (
                r"audio_language_adapter\.2\.weight",
                r"audio_language_adapter.w_out.weight",
            ),
        ]

        audio_params = dict(
            nn.ModuleDict(
                {
                    "audio_language_adapter": self.audio_language_adapter,
                }
            ).named_parameters()
        )
        weights = _create_fake_bias_for_k_proj(weights, ".wk.weight")

        loaded_weights = set()

        defllm_weights_generator():
            nonlocal loaded_weights
            for name, w in weights:
                is_encoder = False
                for k in [
                    "mm_whisper_embeddings",
                    "mm_streams_embeddings.embedding_module",
                ]:
                    is_encoder |= (
                        name.startswith(k)
                        and not name.startswith(f"{k}.tok_embeddings")
                        and not name.startswith(f"{k}.audio_language_projection")
                    )

                for pattern, repl in remapping_rules:
                    if re.fullmatch(pattern, name):
                        name = re.sub(pattern, repl, name)

                if is_encoder:
                    name = self.whisper_encoder.load_weight((name, w))
                    loaded_weights.add(f"whisper_encoder.{name}")
                    continue

                if name in audio_params:
                    param = audio_params[name]
                    with torch.no_grad():
                        default_weight_loader(param, w)
                    loaded_weights.add(name)
                else:
                    yield (name, w)

        for name in self.language_model.load_weights(llm_weights_generator()):
            loaded_weights.add(f"language_model.{name}")

        # potentially manually add position embeddings
        sin_key = "whisper_encoder.whisper_encoder.embed_positions.weight"
        if sin_key not in loaded_weights:
            # make sure we don't hit an error here
            loaded_weights.add(sin_key)

        return loaded_weights

    defmaybe_update_quant_config(
        self, quant_config: QuantizationConfig
    ) -> QuantizationConfig:
"""
        Update quant config to so that ignored module and target module names
        match the vLLM model names.
        Right now this is specific for compressed-tensors format and
        load_format mistral.
        """
        remapping_rules = [
            (r"output", r"language_model.lm_head"),
            (
                r"layers\.(\d+)\.attention\.wo",
                r"language_model.model.layers.\1.self_attn.out_proj",
            ),
            (
                r"layers\.(\d+)\.attention\.w(.*)",
                r"language_model.model.layers.\1.self_attn.\2_proj",
            ),
            (
                r"layers\.(\d+)\.feed_forward\.w1",
                r"language_model.model.layers.\1.mlp.gate_proj",
            ),
            (
                r"layers\.(\d+)\.feed_forward\.w2",
                r"language_model.model.layers.\1.mlp.down_proj",
            ),
            (
                r"layers\.(\d+)\.feed_forward\.w3",
                r"language_model.model.layers.\1.mlp.up_proj",
            ),
            (
                r"mm_whisper_embeddings\.whisper_encoder\.transformer\.layers\.(\d+)\.attention.w(.*)",
                r"whisper_encoder.whisper_encoder.layers.\1.layers.self_attn.\2_proj",
            ),
            (
                r"mm_whisper_embeddings\.whisper_encoder\.transformer\.layers\.(\d+)\.attention.wo",
                r"whisper_encoder.whisper_encoder.layers.\1.layers.self_attn.out_proj",
            ),
            (
                r"mm_whisper_embeddings\.whisper_encoder\.transformer\.layers\.(\d+)\.feed_forward.w(\d+)",
                r"whisper_encoder.whisper_encoder.layers.\1.layers.mlp.fc\2",
            ),
            (
                r"mm_whisper_embeddings\.whisper_encoder\.conv_layers\.0",
                r"whisper_encoder.whisper_encoder.conv1",
            ),
            (
                r"mm_whisper_embeddings\.whisper_encoder\.conv_layers\.1",
                r"whisper_encoder.whisper_encoder.conv2",
            ),
            (
                r"mm_whisper_embeddings\.audio_language_projection\.0",
                r"audio_language_adapter.w_in",
            ),
            (
                r"mm_whisper_embeddings\.audio_language_projection\.2",
                r"audio_language_adapter.w_out",
            ),
        ]

        # Update ignore list
        if hasattr(quant_config, "ignore"):
            mistral_ignore = []
            for name in quant_config.ignore:
                mistral_name = name
                for pattern, repl in remapping_rules:
                    if re.fullmatch(pattern, name):
                        mistral_name = re.sub(pattern, repl, name)
                mistral_ignore.append(mistral_name)
            quant_config.ignore = mistral_ignore

        # Update target list
        if hasattr(quant_config, "config_groups"):
            config_groups = quant_config.config_groups
            for group_name in config_groups:
                if "targets" in config_groups[group_name]:
                    targets = []
                    for name in config_groups[group_name]["targets"]:
                        mistral_name = name
                        for pattern, repl in remapping_rules:
                            if re.fullmatch(pattern, name):
                                mistral_name = re.sub(pattern, repl, name)
                        targets.append(mistral_name)
                config_groups[group_name]["targets"] = targets
            quant_config.config_groups = config_groups

        return quant_config
```