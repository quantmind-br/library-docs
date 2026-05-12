---
title: musicflamingo - vLLM
url: https://docs.vllm.ai/en/latest/api/vllm/model_executor/models/musicflamingo/
source: sitemap
fetched_at: 2026-05-07T21:32:11.30764157-03:00
rendered_js: false
word_count: 12
summary: This document defines the implementation of the MusicFlamingo model within the vLLM framework, specifically handling the processing and encoding of multimodal audio inputs.
tags:
    - vllm
    - multimodal
    - music-flamingo
    - model-architecture
    - audio-processing
    - feature-extraction
category: api
---

```
@MULTIMODAL_REGISTRY.register_processor(
    MusicFlamingoMultiModalProcessor,
    info=MusicFlamingoProcessingInfo,
    dummy_inputs=MusicFlamingoDummyInputsBuilder,
)
classMusicFlamingoForConditionalGeneration(AudioFlamingo3ForConditionalGeneration):
"""vLLM MusicFlamingo model aligned with HF modular_musicflamingo."""

    def__init__(self, *, vllm_config: VllmConfig, prefix: str = ""):
        super().__init__(vllm_config=vllm_config, prefix=prefix)
        self.audio_tower = MusicFlamingoEncoder(self.config.audio_config)
        self.multi_modal_projector = MusicFlamingoMultiModalProjector(self.config)
        self.pos_emb = MusicFlamingoRotaryEmbedding(self.config)

    def_parse_and_validate_audio_input(
        self, **kwargs: object
    ) -> MusicFlamingoInputs | None:
        rote_timestamps = kwargs.pop("rote_timestamps", None)
        audio_input = super()._parse_and_validate_audio_input(**kwargs)
        if audio_input is None or audio_input["type"] == "audio_embeds":
            return audio_input

        return MusicFlamingoFeatureInputs(
            type="audio_features",
            input_features=audio_input["input_features"],
            feature_attention_mask=audio_input["feature_attention_mask"],
            chunk_counts=audio_input["chunk_counts"],
            rote_timestamps=rote_timestamps,
        )

    def_process_audio_input(
        self, audio_input: MusicFlamingoInputs
    ) -> torch.Tensor | tuple[torch.Tensor, ...]:
        if audio_input["type"] == "audio_embeds":
            return super()._process_audio_input(audio_input)

        rote_timestamps = audio_input["rote_timestamps"]
        if rote_timestamps is None:
            raise ValueError(
                "MusicFlamingo audio feature inputs must include `rote_timestamps`."
            )
        if isinstance(rote_timestamps, list):
            rote_timestamps = torch.cat(rote_timestamps, dim=0)

        (
            input_features,
            feature_attention_mask,
            chunk_counts,
        ) = self._normalize_audio_feature_inputs(audio_input)
        hidden_states = self._encode_audio_features(
            input_features,
            feature_attention_mask,
        )
        cos, sin = self.pos_emb(
            rote_timestamps.to(hidden_states.device),
            seq_len=hidden_states.shape[-2],
        )
        hidden_states = apply_rotary_time_emb(hidden_states, cos, sin)
        audio_features = self.multi_modal_projector(hidden_states)

        return self._group_audio_embeddings(
            audio_features,
            feature_attention_mask,
            chunk_counts,
        )
```