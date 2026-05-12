---
title: voxtral - vLLM
url: https://docs.vllm.ai/en/latest/api/vllm/transformers_utils/processors/voxtral/
source: sitemap
fetched_at: 2026-05-07T21:38:15.490758168-03:00
rendered_js: false
word_count: 14
summary: This document defines the MistralCommonFeatureExtractor class, which provides a Hugging Face-compatible interface for processing and tokenizing audio inputs using the Mistral multimodal audio encoder.
tags:
    - audio-processing
    - feature-extraction
    - hugging-face
    - multimodal
    - tokenization
    - voxtral
category: api
---

Provide a HF-compatible interface for `mistral_common.tokens.tokenizers.multimodal.AudioEncoder`.

Source code in `vllm/transformers_utils/processors/voxtral.py`

```
classMistralCommonFeatureExtractor:
"""
    Provide a HF-compatible interface for
    `mistral_common.tokens.tokenizers.multimodal.AudioEncoder`.
    """

    def__init__(self, audio_encoder: AudioEncoder) -> None:
        self.audio_encoder = audio_encoder

    @property
    defsampling_rate(self):
        return self.audio_encoder.audio_config.sampling_rate

    @property
    defframe_rate(self):
        return self.audio_encoder.audio_config.frame_rate

    def__call__(
        self,
        audios: AudioInput,
        return_tensors: str | TensorType | None = None,
        **kwargs,
    ) -> BatchFeature:
        audios_lst = [audios] if not isinstance(audios, list) else audios

        audios_processed = list[torch.Tensor]()

        for audio in audios_lst:
            audio = np.asarray(audio, dtype=np.float32).ravel()
            if not self.audio_encoder.audio_config.is_streaming:
                audio = self.audio_encoder.pad(audio, self.sampling_rate)

            audios_processed.append(torch.tensor(audio))

        return BatchFeature(
            {"audio_arrays": audios_processed}, tensor_type=return_tensors
        )

    defget_num_audio_tokens(self, audio_length: int) -> int:
        return ceil(audio_length / (self.sampling_rate // self.frame_rate))
```