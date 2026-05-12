---
title: kimi_audio - vLLM
url: https://docs.vllm.ai/en/latest/api/vllm/model_executor/models/kimi_audio/
source: sitemap
fetched_at: 2026-05-07T21:31:12.995929443-03:00
rendered_js: false
word_count: 0
summary: This document defines the Kimi-Audio model architecture, outlining its integration within the vLLM framework for multimodal processing, audio feature extraction using a Whisper-based encoder, and the specific fusion method for combining audio and text embeddings.
tags:
    - multimodal-model
    - audio-transcription
    - vllm-integration
    - pytorch
    - embedding-fusion
    - machine-learning-architecture
category: concept
---

```
@MULTIMODAL_REGISTRY.register_processor(
    KimiAudioMultiModalProcessor,
    info=KimiAudioProcessingInfo,
    dummy_inputs=KimiAudioDummyInputsBuilder,
)
classKimiAudioForConditionalGeneration(
    nn.Module,
    SupportsMultiModal,
    SupportsPP,
    SupportsTranscription,
):
"""Kimi-Audio model for ASR transcription."""

    # Kimi-Audio supports a subset of Whisper's supported languages
    supported_languages: ClassVar[Mapping[str, str]] = {
        k: ISO639_1_SUPPORTED_LANGS[k]
        for k in ["zh", "en", "ja", "ko", "de", "fr", "es", "it", "pt", "ru", "ar"]
    }
    supports_transcription: ClassVar[Literal[True]] = True

    hf_to_vllm_mapper = WeightsMapper(
        orig_to_new_prefix={
            # audio tower
            "model.encoder.": "audio_tower.",
            # Audio projector (VQ-Adaptor)
            "model.vq_adaptor.layers.0.": "multi_modal_projector.vq_adaptor_layers_0.",
            "model.vq_adaptor.layers.3.": "multi_modal_projector.vq_adaptor_layers_3.",
            "model.vq_adaptor.layers.4.": "multi_modal_projector.vq_adaptor_layers_4.",
            # Language model
            "model.layers.": "language_model.model.layers.",
            # Embeddings and output
            "model.embed_tokens.": "language_model.model.embed_tokens.",
            "model.norm.": "language_model.model.norm.",
            "lm_head.": "language_model.lm_head.",
        },
        orig_to_new_substr={
            ".fc1.": ".mlp.fc1.",
            ".fc2.": ".mlp.fc2.",
        },
    )

    # Audio placeholder token sequence
    AUDIO_PLACEHOLDER = "<|im_media_begin|><|im_kimia_text_blank|><|im_media_end|>"

    @classmethod
    defget_placeholder_str(cls, modality: str, i: int) -> str | None:
        return cls.AUDIO_PLACEHOLDER if modality.startswith("audio") else None

    def__init__(self, *, vllm_config: VllmConfig, prefix: str = ""):
        super().__init__()
        self.config = vllm_config.model_config.hf_config
        self.quant_config = vllm_config.quant_config
        self.multimodal_config = vllm_config.model_config.multimodal_config
        self.model_path = vllm_config.model_config.model

        self.secondary_weights = [
            DefaultModelLoader.Source(
                model_or_path=vllm_config.model_config.model,
                subfolder="whisper-large-v3",
                revision=None,
            )
        ]

        with self._mark_tower_model(vllm_config, "audio"):
            self.audio_tower = KimiAudioWhisperEncoder(
                vllm_config=vllm_config,
                prefix=maybe_prefix(prefix, "audio_tower"),
            )
            self.multi_modal_projector = KimiAudioMultiModalProjector(
                whisper_dim=getattr(self.config, "kimia_adaptor_input_dim", 5120),
                llm_dim=self.config.hidden_size,
                prefix=maybe_prefix(prefix, "multi_modal_projector"),
            )

        with self._mark_language_model(vllm_config):
            self.language_model = init_vllm_registered_model(
                vllm_config=vllm_config.with_hf_config(
                    self.config, architectures=["Qwen2ForCausalLM"]
                ),
                prefix=maybe_prefix(prefix, "language_model"),
            )

        self.make_empty_intermediate_tensors = (
            self.language_model.make_empty_intermediate_tensors
        )

    def_parse_and_validate_audio_input(
        self, **kwargs: object
    ) -> dict[str, torch.Tensor] | None:
        whisper_input_features = kwargs.pop("whisper_input_features", None)
        if whisper_input_features is None:
            return None

        return {"whisper_input_features": whisper_input_features}

    def_process_audio_input(
        self, audio_input: dict[str, torch.Tensor]
    ) -> torch.Tensor:
        input_features = audio_input["whisper_input_features"]

        # KimiAudioWhisperEncoder expects list of tensors
        if input_features.dim() == 3:
            input_features = input_features.unbind(dim=0)

        # Run through Whisper encoder
        audio_features = self.audio_tower(input_features)

        # Reshape for 4x downsampling (Whisper outputs at 50Hz, need 12.5Hz)
        B, T, D = audio_features.shape
        if T % 4 != 0:
            pad_len = 4 - (T % 4)
            audio_features = torch.nn.functional.pad(audio_features, (0, 0, 0, pad_len))
            T = audio_features.shape[1]  # Update T after padding

        audio_features = audio_features.reshape(B, T // 4, D * 4)

        # Project to LLM dimension
        audio_embeds = self.multi_modal_projector(audio_features)
        return audio_embeds

    defembed_multimodal(self, **kwargs: object) -> list[torch.Tensor] | None:
        audio_input = self._parse_and_validate_audio_input(**kwargs)
        if audio_input is None:
            return []

        audio_embeds = self._process_audio_input(audio_input)

        # audio_embeds shape: [batch_size, seq_len, hidden_dim]
        # Return as list of 2D tensors, one per batch item
        if audio_embeds.dim() == 3:
            # Unbind batch dimension: [B, T, D] -> list of B tensors [T, D]
            return list(audio_embeds.unbind(dim=0))
        else:
            # Single sample: [T, D] -> wrap in list
            return [audio_embeds]

    defembed_input_ids(
        self,
        input_ids: torch.Tensor,
        multimodal_embeddings: tuple[torch.Tensor, ...] | None = None,
        *,
        is_multimodal: torch.Tensor | None = None,
    ) -> torch.Tensor:
"""Embed input IDs and fuse with audio embeddings.

        Kimi-Audio fusion: inputs_embeds = (text_emb + audio_emb) × √2

        For PP compatibility, we use the is_multimodal mask from vLLM engine
        which is correctly computed per pipeline stage.
        """
        # Get text embeddings
        inputs_embeds = self.language_model.model.embed_tokens(input_ids)

        if multimodal_embeddings is None or len(multimodal_embeddings) == 0:
            return inputs_embeds

        # is_multimodal must be provided for PP to work correctly
        if is_multimodal is None or not is_multimodal.any():
            return inputs_embeds

        # multimodal_embeddings[0] contains audio embeddings
        audio_embeds = multimodal_embeddings[0]

        # Handle different tensor structures
        if isinstance(audio_embeds, (list, tuple)):
            audio_embeds = torch.cat(audio_embeds, dim=0)
        elif audio_embeds.dim() == 3:
            audio_embeds = audio_embeds.reshape(-1, audio_embeds.shape[-1])

        # In PP, audio_embeds count should match is_multimodal.sum()
        # For now, use embeddings sequentially
        # (works for non-PP, PP needs vLLM infra fix)
        num_mm_tokens = is_multimodal.sum().item()
        num_audio_embeds = audio_embeds.shape[0]

        # Use the minimum of available embeddings and positions
        # This ensures we don't access out-of-bounds
        num_to_use = min(num_audio_embeds, num_mm_tokens)

        # Get positions for the tokens we'll actually process
        mm_positions = is_multimodal.nonzero(as_tuple=True)[0]
        actual_mm_mask = torch.zeros_like(is_multimodal)
        actual_mm_mask[mm_positions[:num_to_use]] = True

        # Use corresponding embeddings
        used_audio_embeds = audio_embeds[:num_to_use]

        # Save text embeddings at multimodal positions
        text_at_mm_positions = inputs_embeds[actual_mm_mask].clone()

        # Replace text with audio at multimodal positions
        inputs_embeds[actual_mm_mask] = used_audio_embeds.to(dtype=inputs_embeds.dtype)

        # Apply Kimi-Audio's unique fusion formula: (text + audio) × √2
        inputs_embeds[actual_mm_mask] = (
            inputs_embeds[actual_mm_mask] + text_at_mm_positions
        ) * (2**0.5)

        return inputs_embeds

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
            input_ids,
            positions,
            intermediate_tensors,
            inputs_embeds=inputs_embeds,
        )

        return hidden_states

    defcompute_logits(
        self,
        hidden_states: torch.Tensor,
    ) -> torch.Tensor | None:
        return self.language_model.compute_logits(hidden_states)

    defload_weights(self, weights: Iterable[tuple[str, torch.Tensor]]) -> set[str]:
"""Load weights, skipping MIMO layers (TTS-only) for ASR."""
        # Filter out MIMO/TTS weights since we only do ASR (speech-to-text)
        skipped_patterns = [
            # Audio tower
            "model.",
            # MIMO/TTS
            "mimo_layers.",
            "mimo_output.",
            "mimo_norm.",
        ]

        # Load main model weights (LLM + projector) with mapper
        loader = AutoWeightsLoader(self, skip_prefixes=skipped_patterns)
        loaded = loader.load_weights(weights, mapper=self.hf_to_vllm_mapper)
        return loaded

    @classmethod
    defget_speech_to_text_config(
        cls, model_config: ModelConfig, task_type: str
    ) -> SpeechToTextConfig:
"""Get speech-to-text config with custom processor."""
        # Load feature extractor for config values
        feature_extractor = cached_feature_extractor_from_config(
            model_config,
            subfolder=KIMIA_WHISPER_SUBFOLDER,
        )

        return SpeechToTextConfig(
            max_audio_clip_s=feature_extractor.chunk_length,
            sample_rate=feature_extractor.sampling_rate,
        )

    @classmethod
    defget_generation_prompt(cls, stt_params: SpeechToTextParams) -> PromptType:
        audio = stt_params.audio
        model_config = stt_params.model_config
        task_type = stt_params.task_type
        request_prompt = stt_params.request_prompt

        tokenizer = cached_get_tokenizer(
            model_config.tokenizer,
            tokenizer_cls=KimiAudioTokenizer,
            tokenizer_mode=model_config.tokenizer_mode,
            revision=model_config.tokenizer_revision,
            trust_remote_code=model_config.trust_remote_code,
        )

        if task_type not in ("transcribe", "translate"):
            raise ValueError(
                f"Unsupported task_type '{task_type}'. "
                "Supported task types are 'transcribe' and 'translate'."
            )

        # Incorporate request_prompt as context/instruction if provided
        user_content = (
            f"{request_prompt}\n{cls.AUDIO_PLACEHOLDER}"
            if request_prompt
            else cls.AUDIO_PLACEHOLDER
        )

        prompt = (
            f"<|im_kimia_user_msg_start|>{user_content}"
            f"<|im_msg_end|><|im_kimia_assistant_msg_start|>"
        )

        prompt_token_ids = tokenizer.encode(prompt)

        return TokensPrompt(
            prompt_token_ids=prompt_token_ids,
            multi_modal_data={"audio": audio},
        )

    @classmethod
    defpost_process_output(cls, text: str) -> str:
        if not text:
            return ""
        return text.strip()
```