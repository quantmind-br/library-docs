---
title: gemma3n_mm - vLLM
url: https://docs.vllm.ai/en/latest/api/vllm/model_executor/models/gemma3n_mm/
source: sitemap
fetched_at: 2026-05-07T21:30:14.80984893-03:00
rendered_js: false
word_count: 8
summary: This document defines the model architecture and input processing logic for the Gemma3n multimodal model within the vLLM framework, specifically handling vision and audio tower integration.
tags:
    - multimodal
    - gemma
    - vllm
    - model-architecture
    - feature-extraction
    - neural-network
category: api
---

```
@MULTIMODAL_REGISTRY.register_processor(
    Gemma3nMultiModalProcessor,
    info=Gemma3nProcessingInfo,
    dummy_inputs=Gemma3nDummyInputsBuilder,
)
classGemma3nForConditionalGeneration(
    nn.Module, SupportsMultiModal, SupportsTranscription
):
    supported_languages = ISO639_1_SUPPORTED_LANGS

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

    hf_to_vllm_mapper = WeightsMapper(
        orig_to_new_prefix={
            # mapping for new names in checkpoint saved after transformers v4.52
            "model.embed_audio.": "embed_audio.",
            "model.embed_vision.": "embed_vision.",
            "model.language_model.": "language_model.model.",
            "model.vision_tower.": "vision_tower.",
            "model.audio_tower.": "audio_tower.",
            "model.multi_modal_projector.": "multi_modal_projector.",
            "lm_head.": "language_model.lm_head.",
            "model": "language_model.model",
        }
    )

    def__init__(self, *, vllm_config: VllmConfig, prefix: str = ""):
        super().__init__()
        config = vllm_config.model_config.hf_config
        quant_config = vllm_config.quant_config
        multimodal_config = vllm_config.model_config.multimodal_config
        self.config = config
        self.quant_config = quant_config
        self.multimodal_config = multimodal_config
        self.vocab_size = config.text_config.vocab_size

        with self._mark_tower_model(vllm_config, "image"):
            self.vision_tower = AutoModel.from_config(config=config.vision_config)
            self.embed_vision = Gemma3nMultimodalEmbedder(
                config.vision_config, config.text_config
            )

        with self._mark_tower_model(vllm_config, "audio"):
            self.audio_tower = AutoModel.from_config(config=config.audio_config)
            self.embed_audio = Gemma3nMultimodalEmbedder(
                config.audio_config, config.text_config
            )

        with self._mark_language_model(vllm_config):
            self.language_model: Gemma3nForCausalLM = init_vllm_registered_model(
                vllm_config=vllm_config,
                hf_config=config.text_config,
                prefix=maybe_prefix(prefix, "language_model"),
                architectures=["Gemma3nForCausalLM"],
            )

            # NOTE (NickLucche) In order to be compatible with cudagraph, the
            # buffer needs to be consistent, so we pre-allocate here.
            self.per_layer_embeddings = torch.zeros(
                vllm_config.scheduler_config.max_num_batched_tokens,
                self.config.text_config.num_hidden_layers,
                self.config.text_config.hidden_size_per_layer_input,
                device=self.language_model.model.embed_tokens.weight.device,
                dtype=self.language_model.model.embed_tokens.weight.dtype,
            )

    def_parse_and_validate_image_input(
        self, **kwargs: object
    ) -> Gemma3nImageInputs | None:
        pixel_values = kwargs.pop("pixel_values", None)
        image_embeds = kwargs.pop("image_embeds", None)
        # TODO is this the case?
        assert image_embeds is None, "Gemma3n does not support image_embeds."
        if pixel_values is None:
            return None

        return Gemma3nImagePixelInputs(pixel_values=pixel_values)

    def_parse_and_validate_audio_input(
        self, **kwargs: object
    ) -> Gemma3nAudioInputs | None:
        input_features_padded = kwargs.pop("input_features_padded", None)
        if input_features_padded is None:
            return None

        input_features_mask = kwargs.pop("input_features_mask", None)
        if input_features_mask is None:
            return None

        return Gemma3nAudioInputs(
            input_features_padded=input_features_padded,
            input_features_mask=input_features_mask,
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
                input_key == "input_features_padded"
                and "audio" not in mm_input_by_modality
            ):
                mm_input_by_modality["audio"] = self._parse_and_validate_audio_input(
                    **kwargs
                )
        return mm_input_by_modality

    def_process_image_input(
        self,
        image_input: Gemma3nImageInputs,
    ) -> list[torch.Tensor]:
        pixel_values = image_input["pixel_values"]
        vision_outputs = self.vision_tower(
            pixel_values=pixel_values, do_pooling=False, return_dict=True
        ).last_hidden_state
        # TODO try to avoid copy here
        # (batch, channels, height, width) to (batch, height * width, channels)
        vision_outputs = (
            vision_outputs.reshape(
                vision_outputs.shape[0],
                self.config.vision_config.hidden_size,
                self.config.vision_soft_tokens_per_image,
            )
            .permute(0, 2, 1)
            .contiguous()
        )
        # Normalize and embed the soft tokens into language model space.
        vision_outputs *= self.config.vision_config.hidden_size**0.5
        # Return a list of embeddings instead of a batched tensor
        return self.embed_vision(inputs_embeds=vision_outputs).unbind(0)

    def_process_audio_input(
        self,
        audio_input: Gemma3nAudioInputs,
    ) -> list[torch.Tensor]:
        # Run on padded features to enable batching
        input_features = audio_input["input_features_padded"].squeeze(1)
        input_features_mask = audio_input["input_features_mask"].squeeze(1)
        audio_outputs = self.audio_tower(input_features, ~input_features_mask)
        if isinstance(audio_outputs, tuple):
            # Transformers v4
            audio_encodings, audio_mask = audio_outputs
        else:
            # Transformers v5
            audio_encodings = audio_outputs.last_hidden_state
            audio_mask = audio_outputs.audio_mel_mask
        audio_features = self.embed_audio(inputs_embeds=audio_encodings)

        # The Gemma3nProcessor expects all audio will be 30s in length and
        # inserts 188 audio soft tokens into the text to account for this.
        # However, the audio preprocessing and encoder do not guarantee they
        # will produce exactly 188 soft tokens; they may produce fewer tokens
        # (for shorter audio) or more tokens (for longer audio or due to
        # BOA/EOA special tokens in the placeholder sequence).
        # We handle both cases:
        # - If fewer tokens: pad with the embedding of the last vocab token
        # - If more tokens: truncate to the expected count
        # TODO precompute and cache padding
        audio_padding_toks = torch.tensor(
            [[self.vocab_size - 1]], dtype=torch.long, device=audio_features.device
        )
        audio_padding_embs = self.embed_audio(input_ids=audio_padding_toks)
        audio_features = torch.where(
            audio_mask.unsqueeze(-1), audio_padding_embs, audio_features
        )

        expected_tokens = self.config.audio_soft_tokens_per_image
        audio_features, tokens_truncated = adjust_audio_features_to_expected_length(
            audio_features, expected_tokens, audio_padding_embs
        )
        if tokens_truncated > 0:
            logger.warning(
                "Gemma3n audio encoder produced %d extra tokens. "
                "Truncating to match placeholder count of %d.",
                tokens_truncated,
                expected_tokens,
            )

        # Return a list of embeddings instead of a batched tensor
        return audio_features.unbind(0)

    defembed_multimodal(self, **kwargs: object) -> MultiModalEmbeddings:
        mm_input_by_modality = self._parse_and_validate_multimodal_inputs(**kwargs)
        if mm_input_by_modality is None:
            return []

        multimodal_embeddings: list[torch.Tensor] = []

        # NOTE: It is important to iterate over the keys in this dictionary
        # to preserve the order of the modalities.
        for modality in mm_input_by_modality:
            multimodal_input = mm_input_by_modality[modality]
            if modality == "image":
                vision_embeddings = self._process_image_input(multimodal_input)
                multimodal_embeddings.extend(vision_embeddings)
            if modality == "audio":
                audio_embeddings = self._process_audio_input(multimodal_input)
                multimodal_embeddings.extend(audio_embeddings)
        return multimodal_embeddings

    defembed_input_ids(
        self,
        input_ids: torch.Tensor,
        multimodal_embeddings: MultiModalEmbeddings | None = None,
        *,
        is_multimodal: torch.Tensor | None = None,
    ) -> torch.Tensor:
        # NOTE (NickLucche) Each pass needs tokens to compute PLE so we cache
        # them here, as the model  forward has only access to the input_embeds.
        if input_ids is not None:
            per_layer_inputs = self.language_model.model.get_per_layer_input_embeddings(
                input_ids
            )
            per_layer_inputs = per_layer_inputs.reshape(
                -1,
                self.config.text_config.num_hidden_layers,
                self.config.text_config.hidden_size_per_layer_input,
            )
            self.per_layer_embeddings[: per_layer_inputs.shape[0]].copy_(
                per_layer_inputs
            )

        # This is to satisfy the type checker for each overload
        if multimodal_embeddings is None or is_multimodal is None:
            return super().embed_input_ids(input_ids)

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
    ) -> IntermediateTensors:
        if intermediate_tensors is not None:
            inputs_embeds = None

        # NOTE (NickLucche) During profiling, `embed_input_ids` is not
        # called, hence we don't have input_ids to compute PLEs. We simply
        # select a chunk of pre-allocated PLEs. During normal execution,
        # `embed_input_ids` is called before forward, hence this slice
        # will contain PLEs computed from the actual input_ids.
        per_layer_inputs = self.per_layer_embeddings[: inputs_embeds.shape[0]]

        hidden_states = self.language_model.model(
            input_ids,
            positions,
            per_layer_inputs=per_layer_inputs,
            intermediate_tensors=intermediate_tensors,
            inputs_embeds=inputs_embeds,
            **kwargs,
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
            connector="multi_modal_projector",
            tower_model="vision_tower",
        )

    @classmethod
    defget_placeholder_str(cls, modality: str, i: int) -> str | None:
        if modality == "image":
            return "<image_soft_token>"
        elif modality == "audio":
            return "<audio_soft_token>"
        else:
            raise ValueError(f"Unsupported modality: {modality}")

    @classmethod
    defget_generation_prompt(cls, stt_params: SpeechToTextParams) -> PromptType:
"""
        Gemma3n supports "free-form" transcription.
        We fix its prompt here to standardize transcriptions/translations
        requests.
        """
        audio = stt_params.audio
        stt_config = stt_params.stt_config
        language = stt_params.language
        task_type = stt_params.task_type
        to_language = stt_params.to_language
        # Transcribe this audio [into <>] | for transcription
        # Translate this audio [from <> into <>] | for translation
        prompt = "<start_of_turn>user\n"
        prompt += "Transcribe" if task_type == "transcribe" else "Translate"
        prompt += " this audio"

        # We assume the language is a valid ISO 639-1 code.
        full_lang_name = cls.supported_languages.get(language, "")
        # Translation only for now
        full_lang_name_to = cls.supported_languages.get(to_language, "")

        if task_type == "transcribe" and full_lang_name:
            prompt += f" into {full_lang_name}"
        elif task_type == "translate":
            if full_lang_name:
                prompt += f" from {full_lang_name}"
            if full_lang_name_to:
                prompt += f" into {full_lang_name_to}"

        prompt += ": <audio_soft_token><end_of_turn>\n<start_of_turn>model\n"

        return TextPrompt(
            prompt=prompt,
            multi_modal_data={"audio": (audio, stt_config.sample_rate)},
        )

    @classmethod
    defget_speech_to_text_config(
        cls, model_config: ModelConfig, task_type: str
    ) -> SpeechToTextConfig:
        return SpeechToTextConfig(
            # Let's set this to 30 as suggested in the docs for now, although
            # the model is only limited by its context length.
            max_audio_clip_s=30,
            sample_rate=16000,
            # TODO enable chunking after more thorough testing.
            min_energy_split_window_size=None,
        )
```