---
title: qwen2_audio - vLLM
url: https://docs.vllm.ai/en/latest/api/vllm/model_executor/models/qwen2_audio/
source: sitemap
fetched_at: 2026-05-07T21:32:50.883992394-03:00
rendered_js: false
word_count: 79
summary: This document defines the technical specifications and data structures for implementing the Qwen2-Audio model within the vLLM execution framework.
tags:
    - vllm
    - qwen2-audio
    - multimodal-model
    - tensor-schema
    - inference-engine
category: reference
---

## vllm.model\_executor.models.qwen2\_audio [¶](#vllm.model_executor.models.qwen2_audio "Permanent link")

Inference-only Qwen2-Audio model compatible with HuggingFace weights.

## Qwen2AudioEmbeddingInputs [¶](#vllm.model_executor.models.qwen2_audio.Qwen2AudioEmbeddingInputs "Permanent link")

Bases: `TensorSchema`

Dimensions

- bn: Batch size
- naf: Number of audio features
- hs: Hidden size (must match the hidden size of language model backbone)

Source code in `vllm/model_executor/models/qwen2_audio.py`

```
classQwen2AudioEmbeddingInputs(TensorSchema):
"""
    Dimensions:
        - bn: Batch size
        - naf: Number of audio features
        - hs: Hidden size (must match the hidden size of language model
          backbone)
    """

    type: Literal["audio_embeds"] = "audio_embeds"

    audio_embeds: Annotated[
        list[torch.Tensor],
        TensorShape("bn", "naf", "hs", dynamic_dims={"naf"}),
    ]
```

## Qwen2AudioFeatureInputs [¶](#vllm.model_executor.models.qwen2_audio.Qwen2AudioFeatureInputs "Permanent link")

Bases: `TensorSchema`

Dimensions

- na: Number of audios
- nmb: Number of mel bins

Source code in `vllm/model_executor/models/qwen2_audio.py`

```
classQwen2AudioFeatureInputs(TensorSchema):
"""
    Dimensions:
        - na: Number of audios
        - nmb: Number of mel bins
    """

    type: Literal["audio_features"]
    input_features: Annotated[
        torch.Tensor | list[torch.Tensor],
        TensorShape("na", "nmb", 3000),
    ]

    feature_attention_mask: Annotated[
        torch.Tensor,
        TensorShape("na", 3000),
    ]
```

## Qwen2AudioProcessingInfo [¶](#vllm.model_executor.models.qwen2_audio.Qwen2AudioProcessingInfo "Permanent link")

Bases: `BaseProcessingInfo`

Source code in `vllm/model_executor/models/qwen2_audio.py`

```
classQwen2AudioProcessingInfo(BaseProcessingInfo):
    defget_hf_config(self):
        return self.ctx.get_hf_config(Qwen2AudioConfig)

    defget_hf_processor(self, **kwargs: object) -> Qwen2AudioProcessor:
        return self.ctx.get_hf_processor(Qwen2AudioProcessor, **kwargs)

    defget_feature_extractor(self, **kwargs: object) -> WhisperFeatureExtractor:
        hf_processor = self.get_hf_processor(**kwargs)
        feature_extractor = hf_processor.feature_extractor  # type: ignore
        assert isinstance(feature_extractor, WhisperFeatureExtractor)
        return feature_extractor

    defget_data_parser(self):
        feature_extractor = self.get_feature_extractor()

        return Qwen2AudioMultiModalDataParser(
            target_sr=feature_extractor.sampling_rate,
            target_channels=self.get_target_channels(),
            expected_hidden_size=self._get_expected_hidden_size(),
        )

    defget_target_channels(self) -> int:
"""Return target audio channels for Qwen2 Audio models (mono)."""
        return 1

    defget_supported_mm_limits(self) -> Mapping[str, int | None]:
        return {"audio": None}

    defget_mm_max_tokens_per_item(
        self,
        seq_len: int,
        mm_counts: Mapping[str, int] | None = None,
    ) -> Mapping[str, int]:
        mm_counts = mm_counts or {}
        if mm_counts.get("audio", 0) <= 0:
            return {}

        feature_extractor = self.get_feature_extractor()
        chunk_length = min(feature_extractor.chunk_length, 30)
        audio_len = int(chunk_length * feature_extractor.sampling_rate)
        hop_length = feature_extractor.hop_length
        max_mel_seq_len = audio_len // hop_length

        input_lengths = torch.tensor([max_mel_seq_len], dtype=torch.long)
        _, output_lengths = _get_feat_extract_output_lengths(input_lengths)

        return {"audio": int(output_lengths.item())}
```

### get\_target\_channels [¶](#vllm.model_executor.models.qwen2_audio.Qwen2AudioProcessingInfo.get_target_channels "Permanent link")

```
get_target_channels() -> int
```

Return target audio channels for Qwen2 Audio models (mono).

Source code in `vllm/model_executor/models/qwen2_audio.py`

```
defget_target_channels(self) -> int:
"""Return target audio channels for Qwen2 Audio models (mono)."""
    return 1
```