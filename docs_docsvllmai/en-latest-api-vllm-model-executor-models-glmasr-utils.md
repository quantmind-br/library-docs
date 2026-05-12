---
title: glmasr_utils - vLLM
url: https://docs.vllm.ai/en/latest/api/vllm/model_executor/models/glmasr_utils/
source: sitemap
fetched_at: 2026-05-07T21:30:29.987565893-03:00
rendered_js: false
word_count: 106
summary: This document provides utility functions to calculate output lengths for audio processing models, specifically accounting for convolutional layer downsampling and feature merging.
tags:
    - audio-processing
    - convolutional-layers
    - downsampling
    - tensor-manipulation
    - model-utility
    - feature-extraction
category: reference
---

## \_calculate\_conv\_output\_length [¶](#vllm.model_executor.models.glmasr_utils._calculate_conv_output_length "Permanent link")

```
_calculate_conv_output_length(
    input_length: Tensor,
    padding: int,
    kernel_size: int,
    stride: int,
) -> Tensor
```

Calculate Conv1d output length using standard formula.

Source code in `vllm/model_executor/models/glmasr_utils.py`

```
def_calculate_conv_output_length(
    input_length: torch.Tensor, padding: int, kernel_size: int, stride: int
) -> torch.Tensor:
"""Calculate Conv1d output length using standard formula."""
    # in sync with `hf_processor._get_audio_token_length`
    return (input_length + 2 * padding - (kernel_size - 1) - 1) // stride + 1
```

## \_get\_audio\_output\_lengths\_for\_tower [¶](#vllm.model_executor.models.glmasr_utils._get_audio_output_lengths_for_tower "Permanent link")

Calculate the output lengths after audio processing.

The output length accounts for: 1. Convolution layers (downsampling) 2. Merge factor (further downsampling during projection)

Parameters:

Name Type Description Default `audio_tower` `Module`

The audio encoder module

*required* `audio_lengths` `Tensor`

Input feature lengths \[batch\_size]

*required* `merge_factor` `int`

Factor for merging adjacent features

*required* `conv_params` `list[tuple[int, int, int]]`

List of (padding, kernel\_size, stride) for each conv layer

*required*

Returns:

Type Description `Tensor`

Output lengths after all processing \[batch\_size]

Source code in `vllm/model_executor/models/glmasr_utils.py`

```
def_get_audio_output_lengths_for_tower(
    audio_tower: nn.Module,
    audio_lengths: torch.Tensor,
    merge_factor: int,
    conv_params: list[tuple[int, int, int]],
) -> torch.Tensor:
"""
    Calculate the output lengths after audio processing.

    The output length accounts for:
    1. Convolution layers (downsampling)
    2. Merge factor (further downsampling during projection)

    Args:
        audio_tower: The audio encoder module
        audio_lengths: Input feature lengths [batch_size]
        merge_factor: Factor for merging adjacent features
        conv_params: List of (padding, kernel_size, stride) for each conv layer

    Returns:
        Output lengths after all processing [batch_size]
    """
    # First, calculate the output length after convolutions
    if hasattr(audio_tower, "_get_feat_extract_output_lengths"):
        _, conv_output_lengths = audio_tower._get_feat_extract_output_lengths(
            audio_lengths
        )
    else:
        conv_output_lengths = audio_lengths
        for padding, kernel_size, stride in conv_params:
            conv_output_lengths = _calculate_conv_output_length(
                conv_output_lengths, padding, kernel_size, stride
            )

    # Then, apply merge_factor to get final output length
    # Formula: (conv_output_lengths - merge_factor) // merge_factor + 1
    return (conv_output_lengths - merge_factor) // merge_factor + 1
```