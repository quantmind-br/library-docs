---
title: parakeet - vLLM
url: https://docs.vllm.ai/en/latest/api/vllm/transformers_utils/configs/parakeet/
source: sitemap
fetched_at: 2026-05-07T21:37:23.141061461-03:00
rendered_js: false
word_count: 19
summary: This document defines the ExtractorConfig dataclass and a factory method for initializing configuration parameters from Hugging Face pretrained models for the Parakeet model architecture.
tags:
    - parakeet
    - configuration
    - feature-extraction
    - dataclass
    - audio-processing
    - hugging-face
category: configuration
---

Source code in `vllm/transformers_utils/configs/parakeet.py`

```
@dataclass(kw_only=True, frozen=True)
classExtractorConfig:
    feature_size: int
    sampling_rate: int
    subsampling_factor: int
    subsampling_conv_kernel_size: int
    subsampling_conv_stride: int
    hop_length: int = 160
"""Default `160`: Matches HF default"""
    clip_duration_s: int = 30
    clip_min_duration_s: float = 0.1

    win_length: int = 400
    preemphasis: float = 0.97
    n_fft: int = 512
    padding_value: float = 0.0

    @classmethod
    deffrom_hf_config(cls, config: PretrainedConfig) -> "ExtractorConfig":
        assert isinstance(config, PretrainedConfig)
        defaults = ("hop_length", "win_length", "preemphasis", "n_fft", "padding_value")
        optional_kwargs = {
            name: getattr(config, name) for name in defaults if hasattr(config, name)
        }

        return cls(
            feature_size=config.num_mel_bins,
            sampling_rate=config.sampling_rate,
            subsampling_factor=config.subsampling_factor,
            subsampling_conv_kernel_size=config.subsampling_conv_kernel_size,
            subsampling_conv_stride=config.subsampling_conv_stride,
            **optional_kwargs,
        )
```

Default `160`: Matches HF default