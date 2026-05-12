---
title: fireredlid - vLLM
url: https://docs.vllm.ai/en/latest/api/vllm/model_executor/models/fireredlid/
source: sitemap
fetched_at: 2026-05-07T21:30:03.790703898-03:00
rendered_js: false
word_count: 0
summary: This document defines the FireRedLID model implementation for vLLM, providing the necessary infrastructure for multimodal audio processing and language identification. It covers weight mapping, input embedding, and the integration of encoder-decoder logic for speech-based tasks.
tags:
    - vllm
    - multimodal
    - audio-processing
    - model-integration
    - pytorch
    - speech-recognition
category: api
---

```
@MULTIMODAL_REGISTRY.register_processor(
    FireRedLIDMultiModalProcessor,
    info=FireRedLIDProcessingInfo,
    dummy_inputs=FireRedLIDDummyInputsBuilder,
)
classFireRedLIDForConditionalGeneration(
    nn.Module, SupportsTranscription, SupportsMultiModal
):
    # -- SupportsTranscription protocol attributes --
    supports_transcription_only = True
    supported_languages = _FIREREDLID_SUPPORTED_LANGUAGES

    hf_to_vllm_mapper = WeightsMapper(
        orig_to_new_substr={
            "encoder.": "model.encoder.",
            "lid_decoder.": "model.decoder.",
            # Encoder FFN: nn.Sequential indices → named children
            "net.0": "pre_layer_norm",
            "net.1": "linear_expand",
            "net.4": "linear_project",
        }
    )

    def__init__(self, *, vllm_config: VllmConfig, prefix: str = ""):
        super().__init__()
        config = vllm_config.model_config.hf_config
        self.config = config
        self.dtype = vllm_config.model_config.dtype

        with self._mark_composite_model(
            vllm_config,
            language_targets=FireRedLIDDecoder,
            tower_targets={"audio": FireRedLIDEncoder},
        ):
            self.model = FireRedLIDModel(
                vllm_config=vllm_config,
                prefix=maybe_prefix(prefix, "model"),
            )

        self.proj_out = ParallelLMHead(
            getattr(config, "vocab_size", 120),
            getattr(config, "d_model", 1280),
            quant_config=vllm_config.quant_config,
            prefix=maybe_prefix(prefix, "proj_out"),
        )
        self.proj_out = self.proj_out.tie_weights(self.model.decoder.tgt_word_emb)

        logit_scale = getattr(config, "logit_scale", 1.0)
        self.logits_processor = LogitsProcessor(
            getattr(config, "vocab_size", 120),
            scale=logit_scale,
        )

    defforward(
        self,
        input_ids: torch.Tensor,
        positions: torch.Tensor,
        encoder_outputs: list[torch.Tensor] | None = None,
        **kwargs,
    ) -> torch.Tensor:
        if encoder_outputs is None:
            encoder_outputs = []
        decoder_outputs = self.model(
            input_ids=input_ids,
            positions=positions,
            encoder_outputs=encoder_outputs,
        )
        return decoder_outputs

    defembed_multimodal(self, **kwargs: object) -> MultiModalEmbeddings:
"""Run encoder on audio features and return per-item embeddings."""
        audio_input = self._parse_and_validate_audio_input(**kwargs)

        speech = audio_input["input_features"]
        speech_lengths = audio_input["speech_lengths"]
        if speech is None or speech_lengths is None:
            return []

        # When audio items have different time lengths, vLLM's
        # MultiModalBatchedField._reduce_data returns a plain
        # list[Tensor] instead of a stacked Tensor.  The encoder
        # expects a padded [B, Tmax, feat_dim] Tensor, so we
        # normalise both speech and speech_lengths here.
        if isinstance(speech, (list, tuple)):
            # Each element: [Ti, feat_dim]  (or [1, Ti, feat_dim])
            tensors = [
                s.squeeze(0) if s.dim() == 3 and s.size(0) == 1 else s for s in speech
            ]
            device = tensors[0].device
            dtype = tensors[0].dtype
            feat_dim = tensors[0].shape[-1]
            lengths = torch.tensor(
                [t.size(0) for t in tensors],
                device=device,
                dtype=torch.int32,
            )
            t_max = int(lengths.max().item())
            # Pre-allocate zero-padded batch tensor
            speech = torch.zeros(
                (len(tensors), t_max, feat_dim),
                device=device,
                dtype=dtype,
            )
            for i, t in enumerate(tensors):
                speech[i, : t.size(0)] = t
            speech_lengths = lengths
        else:
            # Already a batched Tensor [B, T, feat_dim]
            if speech.dim() == 2:
                speech = speech.unsqueeze(0)

        speech_lengths = torch.as_tensor(
            speech_lengths, dtype=torch.int32, device=speech.device
        )

        enc_output, enc_lengths = self.model.get_encoder_outputs(
            speech=speech,
            speech_lengths=speech_lengths,
        )

        # vLLM expects one 2D tensor per multimodal item. Slice each batch entry
        # by the true encoder length so cross-attention never sees padded frames.
        return tuple(
            enc_output[i, : max(0, int(enc_lengths[i].item()))]
            for i in range(enc_output.size(0))
        )

    defembed_input_ids(
        self,
        input_ids: torch.Tensor,
        multimodal_embeddings: MultiModalEmbeddings | None = None,
        *,
        is_multimodal: torch.Tensor | None = None,
    ) -> torch.Tensor:
        return self.model.decoder.embed_input_ids(input_ids)

    def_parse_and_validate_audio_input(
        self, **kwargs: object
    ) -> FireRedLIDAudioInputs:
        input_features = kwargs.pop("input_features", None)
        speech_lengths = kwargs.pop("speech_lengths", None)
        fake_token_lengths = kwargs.pop("fake_token_lengths", None)
        return FireRedLIDAudioInputs(
            input_features=input_features,
            speech_lengths=speech_lengths,
            fake_token_lengths=fake_token_lengths,
        )

    defcompute_logits(self, hidden_states: torch.Tensor) -> torch.Tensor:
        logits = self.logits_processor(self.proj_out, hidden_states)
        return logits

    @classmethod
    defvalidate_language(cls, language: str | None) -> str | None:
        # FireRedLID is a language *identification* model – the caller does
        # not need to specify a language up-front.  Accept None silently.
        if language is None:
            return None
        return super().validate_language(language)

    @classmethod
    defget_generation_prompt(
        cls,
        audio: np.ndarray,
        stt_config: SpeechToTextConfig,
        model_config: ModelConfig,
        language: str | None,
        task_type: Literal["transcribe", "translate"],
        request_prompt: str,
        to_language: str | None,
    ) -> PromptType:
"""Build the prompt for the FireRedLID encoder-decoder model.

        The decoder receives a single <sos> token; the encoder processes
        the raw audio waveform via the multimodal pipeline.
        """
        prompt: PromptType = {
            "encoder_prompt": {
                "prompt": "",
                "multi_modal_data": {
                    "audio": (audio, int(stt_config.sample_rate)),
                },
            },
            "decoder_prompt": {
                "prompt": "<sos>",
            },
        }
        return prompt

    @classmethod
    defget_speech_to_text_config(
        cls,
        model_config: ModelConfig,
        task_type: Literal["transcribe", "translate"],
    ) -> SpeechToTextConfig:
        processor = cached_processor_from_config(model_config)
        return SpeechToTextConfig(
            max_audio_clip_s=processor.feature_extractor.chunk_length,
            sample_rate=processor.feature_extractor.sampling_rate,
            # LID output is at most 2 tokens – no chunking needed.
            min_energy_split_window_size=None,
        )

    @classmethod
    defpost_process_output(cls, text: str) -> str:
        # Strip any leading/trailing whitespace from the raw LID output.
        return text.strip()

    defload_weights(self, weights: Iterable[tuple[str, torch.Tensor]]) -> set[str]:
        loader = AutoWeightsLoader(
            self,
            skip_prefixes=[
                # Position encoding buffers are rebuilt at init
                "model.encoder.positional_encoding.pe",
                "model.decoder.positional_encoding.pe",
                # Tied output projection (shared with embedding)
                "model.decoder.tgt_word_prj.weight",
                "proj_out.",
            ],
        )
        return loader.load_weights(weights, mapper=self.hf_to_vllm_mapper)
```