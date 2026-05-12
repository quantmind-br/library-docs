---
title: midashenglm - vLLM
url: https://docs.vllm.ai/en/latest/api/vllm/model_executor/models/midashenglm/
source: sitemap
fetched_at: 2026-05-07T21:31:38.096594354-03:00
rendered_js: false
word_count: 42
summary: This document provides technical reference documentation for the MiDashengLM model implementation in vLLM, including tensor schemas for audio inputs and utility functions for calculating Mel-spectrogram frames.
tags:
    - vllm
    - midashenglm
    - audio-processing
    - tensor-schema
    - mel-spectrogram
    - model-executor
category: reference
---

## vllm.model\_executor.models.midashenglm [¶](#vllm.model_executor.models.midashenglm "Permanent link")

Inference-only MiDashengLM model compatible with HuggingFace weights.

## MiDashengLMAudioInputs [¶](#vllm.model_executor.models.midashenglm.MiDashengLMAudioInputs "Permanent link")

Bases: `TensorSchema`

Dimensions

- bn: Batch size * number of audios
- p: Number of sampling points

Source code in `vllm/model_executor/models/midashenglm.py`

```
classMiDashengLMAudioInputs(TensorSchema):
"""

    Dimensions:
        - bn: Batch size * number of audios
        - p: Number of sampling points
    """

    input_values: Annotated[torch.Tensor, TensorShape("n", "p")]
    audio_length: Annotated[torch.Tensor, TensorShape("n")]
```

## calculate\_mel\_frames\_dasheng [¶](#vllm.model_executor.models.midashenglm.calculate_mel_frames_dasheng "Permanent link")

```
calculate_mel_frames_dasheng(
    audio_length_samples: int,
    n_fft: int = 512,
    hop_size: int = 160,
    dasheng_subsampling: int = 4,
    center=True,
    model_subsampling: int = 5,
) -> int
```

Calculate the number of Mel-spectrogram frames.

Source code in `vllm/model_executor/models/midashenglm.py`

```
defcalculate_mel_frames_dasheng(
    audio_length_samples: int,
    n_fft: int = 512,
    hop_size: int = 160,
    dasheng_subsampling: int = 4,
    center=True,
    model_subsampling: int = 5,
) -> int:
"""Calculate the number of Mel-spectrogram frames."""
    if center:
        audio_length_samples = audio_length_samples + n_fft

    return (
        int(1 + ((audio_length_samples - n_fft) / hop_size))
        // dasheng_subsampling
        // model_subsampling
    )
```