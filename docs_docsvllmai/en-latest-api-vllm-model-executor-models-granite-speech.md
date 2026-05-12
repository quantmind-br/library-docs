---
title: granite_speech - vLLM
url: https://docs.vllm.ai/en/latest/api/vllm/model_executor/models/granite_speech/
source: sitemap
fetched_at: 2026-05-07T21:30:37.817194358-03:00
rendered_js: false
word_count: 0
summary: This document defines the implementation of a multimodal speech-to-text neural network model integrated with the vLLM framework, covering architectural setup and audio input processing.
tags:
    - vllm
    - multimodal
    - pytorch
    - speech-processing
    - model-architecture
    - neural-networks
category: api
---

```
@MULTIMODAL_REGISTRY.register_processor(
    GraniteSpeechMultiModalProcessor,
    info=GraniteSpeechMultiModalProcessingInfo,
    dummy_inputs=GraniteSpeechDummyInputsBuilder,
)
classGraniteSpeechForConditionalGeneration(
    nn.Module,
    SupportsMultiModal,
    SupportsPP,
    SupportsLoRA,
    SupportsTranscription,
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

    @classmethod
    defget_placeholder_str(cls, modality: str, i: int) -> str | None:
        if modality.startswith("audio"):
            return "<|audio|>"

        raise ValueError("Only audio modality is supported")

    def__init__(self, *, vllm_config: VllmConfig, prefix: str = ""):
        super().__init__()
        config = vllm_config.model_config.hf_config
        quant_config = vllm_config.quant_config
        cache_config = vllm_config.cache_config

        self.config = config
        self.quant_config = quant_config
        self.cache_config = cache_config

        # Check for OOV tokens to see if offsets need to be preserved
        self.configure_mm_token_handling(
            vocab_size=config.text_config.vocab_size,
            mm_token_ids=[config.audio_token_index],
        )

        with self._mark_language_model(vllm_config):
            # The language model is typically a Granite LLM
            self.language_model = init_vllm_registered_model(
                vllm_config=vllm_config,
                hf_config=config.text_config,
                prefix=maybe_prefix(prefix, "language_model"),
            )

        with self._mark_tower_model(vllm_config, "audio"):
            # Conformer encoder
            self.encoder = GraniteSpeechCTCEncoder(
                config=config.encoder_config,
                quant_config=quant_config,
                prefix=f"{prefix}.encoder",
            )

            # Blip2 QFormer
            self.projector = GraniteSpeechEncoderProjector(
                config=config,
                quant_config=quant_config,
                cache_config=cache_config,
                prefix=f"{prefix}.projector",
            )

        self.make_empty_intermediate_tensors = (
            self.language_model.make_empty_intermediate_tensors
        )

    def_parse_and_validate_audio_input(
        self,
        **kwargs: object,
    ) -> GraniteSpeechAudioInputs | None:
        input_features = kwargs.pop("input_features", None)
        input_features_mask = kwargs.pop("input_features_mask", None)
        audio_embed_sizes = kwargs.pop("audio_embed_sizes", None)

        if input_features is None:
            return None

        # If we have a batch of variable feature length audio clips, we need
        # to mask the features; usually we would get an input_features_mask
        # from the processor, but we handle rebuilding it here since
        # vLLM generally processes everything independently + batches.
        if input_features_mask is None:
            input_features_mask = self._build_input_features_mask(audio_embed_sizes)

        if not isinstance(input_features, (torch.Tensor, list)):
            raise ValueError(
                "Incorrect type of audio input features. "
                f"Got type: {type(input_features)}"
            )

        if input_features_mask is not None and not isinstance(
            input_features_mask, torch.Tensor
        ):
            raise ValueError(
                "Incorrect type of audio input features mask. "
                f"Got type: {type(input_features_mask)}"
            )

        if isinstance(input_features, torch.Tensor):
            # Granite speech currently only allows one audio token per instance
            # and features are already unsqueezed in the processor, so one
            # instance will have shape [1, {num_features}, 160]. As such,
            # input features will usually be of shape
            # [bsz, 1, num_features, 160], which we squeeze to be 3D here.
            if len(input_features.shape) == 4:
                input_features = input_features.squeeze(1)
            if len(input_features.shape) != 3:
                raise ValueError(
                    "Squeezed input features should be 3D but are of shape "
                    f"{input_features.shape}"
                )
            input_features = input_features.to(self.encoder.input_linear.weight.dtype)

        else:
            # Otherwise we have a list of tensors, which are almost certainly
            # differing in their respective numbers of audio features; when
            # passed as a batch, we expect a list of 2D var len input features
            # so unsqueeze them.
            input_features = [
                feat.unsqueeze(dim=0) for feat in input_features if feat.ndim == 2
            ]

            # stack them into a 3D tensor of size [bsz, most_num_features, 160].
            input_features = self._pad_and_stack_input_features(
                input_features,
            ).to(self.encoder.input_linear.weight.dtype)

        return GraniteSpeechAudioInputs(
            input_features=input_features,
            input_features_mask=input_features_mask,
            audio_embed_sizes=audio_embed_sizes.flatten().tolist(),
        )

    def_build_input_features_mask(
        self,
        audio_embed_sizes: torch.Tensor,
    ) -> torch.Tensor:
"""Calculate the input features mask, which will generally be used
        to mask the padded features for all entries in the batch except
        for those with the most audio features.

        Args:
            audio_embed_sizes: torch.Tensor
                Tensor of num features in each seq in the batch.
        Returns:
            torch.Tensor: Mask of shape (bsz, num_features) to be applied to
            the audio features prior to splitting the audio embeddings.
        """
        most_audio_features = torch.max(audio_embed_sizes).item()
        mask_indices = torch.arange(
            most_audio_features,
            device=audio_embed_sizes.device,
        ).view(1, -1)
        input_features_mask = mask_indices < audio_embed_sizes.view(-1, 1)
        return input_features_mask

    def_pad_and_stack_input_features(
        self,
        input_features: list[torch.Tensor],
    ) -> torch.Tensor:
"""Given a list of input features of varying length, pad them to the
        same length and stack them into a torch.Tensor.

        NOTE: Usually, padding is done in the input processor/feature extractor
        and zero padded prior to the computation of the Mel features; the
        resulting values are only constant within a batch and generally nonzero
        (i.e., slightly negative nums); we should validate that this is okay
        since we don't use a feature attention mask, but the more important
        thing is that we apply the input_features_mask with variable len
        batches.

        Args:
            input_features: list[torch.Tensor]
                3D Input features to be coerced into a tensor.
        Returns:
            torch.Tensor: Tensor of shape [bsz, num_features, 160], where
            num_features is the max number of features of any entry in the
            batch.
        """
        feat_lens = [feats.shape[1] for feats in input_features]
        padding = [max(feat_lens) - length for length in feat_lens]
        # TODO (Alex) - Validate that it's okay to zero pad like this;
        # in transformers we zero pad prior to calculating the speech features,
        # so the value is not zero and is dependent on the batched features.
        padded = [
            torch.nn.functional.pad(feats, (0, 0, 0, pad, 0, 0))
            for feats, pad in zip(input_features, padding)
        ]
        stacked_features = torch.cat(padded, dim=0).to(input_features[0])
        return stacked_features

    def_process_audio_input(
        self,
        audio_input: GraniteSpeechAudioInputs,
    ) -> tuple[torch.Tensor]:
"""Compute the audio features to be merged into the LLM embeddings.

        Args:
            audio_input: GraniteSpeechAudioInputs
                Audio inputs object containing Mel features, an input features
                mask, and the (flattened) number of audio tokens per instance.
        Returns:
            tuple[torch.Tensor]: List of length bsz.
        """
        # TODO (Alex) - support embedding inputs
        encoder_embeds = self.encoder(audio_input["input_features"])
        # [bsz, <max feature size>, 4096]
        projected_embeds = self.projector(encoder_embeds)
        # Apply mask on variable length audio features
        masked_embeds = projected_embeds[audio_input["input_features_mask"]]
        # Split variable length features into a tuple
        return torch.split(masked_embeds, audio_input["audio_embed_sizes"])

    defembed_multimodal(
        self,
        **kwargs: object,
    ) -> MultiModalEmbeddings:
"""Compute the audio embeddings if audio inputs are present."""
        audio_input = self._parse_and_validate_audio_input(**kwargs)
        if audio_input is None:
            return []

        audio_features = self._process_audio_input(audio_input)
        return audio_features

    defembed_input_ids(
        self,
        input_ids: torch.Tensor,
        multimodal_embeddings: MultiModalEmbeddings | None = None,
        *,
        is_multimodal: torch.Tensor | None = None,
    ) -> torch.Tensor:
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
    ) -> torch.Tensor | IntermediateTensors:
        if intermediate_tensors is not None:
            inputs_embeds = None

        model_output = self.language_model(
            input_ids, positions, intermediate_tensors, inputs_embeds
        )
        return model_output

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

    defget_mm_mapping(self) -> MultiModelKeys:
"""Get the module prefix in multimodal models."""
        return MultiModelKeys.from_string_field(
            language_model="language_model",
            connector="projector",
            tower_model="encoder",
        )

    ### Support for speech-to-text Transcription
    @classmethod
    defget_generation_prompt(
        cls,
        stt_params: SpeechToTextParams,
    ) -> PromptType:
"""Get the generation prompt to be used for transcription requests."""
        audio = stt_params.audio
        model_config = stt_params.model_config
        task_type = stt_params.task_type
        to_language = stt_params.to_language

        # Audio placeholders don't use an index, so value doesn't matter
        audio_tok = cls.get_placeholder_str("audio", 0)

        if task_type == "translate":
            full_lang_name_to = cls.supported_languages.get(to_language, to_language)
            user_prompt = f"{audio_tok}translate the speech to {full_lang_name_to}"  # noqa: E501
        elif task_type == "transcribe":
            user_prompt = (
                f"{audio_tok}can you transcribe the speech into a written format?"  # noqa: E501
            )
        else:
            raise ValueError(f"Unsupported task type {task_type}")

        tokenizer = cached_tokenizer_from_config(model_config)
        chat = [dict(role="user", content=user_prompt)]
        prompt = tokenizer.apply_chat_template(
            chat,
            tokenize=False,
            add_generation_prompt=True,
        )

        prompt_token_ids = tokenizer.encode(prompt)

        return TokensPrompt(
            prompt_token_ids=prompt_token_ids,
            multi_modal_data={"audio": audio},
        )

    # Adapted from https://github.com/huggingface/transformers/blob/v4.56.0/src/transformers/models/granite_speech/feature_extraction_granite_speech.py#L122 # noqa: E501
    @classmethod
    defget_num_audio_tokens(
        cls,
        audio_duration_s: float,
        stt_config: SpeechToTextConfig,
        model_config: ModelConfig,
    ) -> int | None:
"""Get the number of audio tokens for an audio duration in sec."""
        processor = cached_processor_from_config(model_config)
        hop_length = processor.audio_processor.melspec_kwargs["hop_length"]
        proj_win_size = processor.audio_processor.projector_window_size
        ds_rate = processor.audio_processor.projector_downsample_rate
        effective_window_size = proj_win_size // ds_rate

        raw_length = audio_duration_s * stt_config.sample_rate

        # mel sequence length computation
        mel_length = raw_length // hop_length + 1
        # encoder frame takes two mel features
        encoder_length = mel_length // 2
        nblocks = math.ceil(encoder_length / proj_win_size)
        # projector output length
        return nblocks * effective_window_size

    @classmethod
    defget_speech_to_text_config(
        cls, model_config: ModelConfig, task_type: str
    ) -> SpeechToTextConfig:
"""Get the stt config for this model."""
        # Default settings are reasonable for this model and we don't currently
        # expose this information in the model configs, but this may change in
        # the future
        return SpeechToTextConfig()
```