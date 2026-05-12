---
title: machete_utils - vLLM
url: https://docs.vllm.ai/en/latest/api/vllm/model_executor/layers/quantization/utils/machete_utils/
source: sitemap
fetched_at: 2026-05-07T21:27:58.76209924-03:00
rendered_js: false
word_count: 67
summary: Provides a utility function to retrieve the supported quantization group sizes for Machete kernels based on the specified activation data type.
tags:
    - machete
    - quantization
    - group-size
    - activation-type
    - vllm-utils
category: api
---

Queries the supported group sizes for Machete based on the activation type.

Parameters:

Name Type Description Default `act_type` `dtype`

The activation data type (torch.float16, torch.bfloat16).

*required*

Returns:

Type Description `list[int]`

A list of supported group sizes. The group size must

`list[int]`

be divisible by `TileShapeK = 128 * 8 // num_bits(act_type)`.

`list[int]`

-1 indicates per-channel quantization.

Source code in `vllm/model_executor/layers/quantization/utils/machete_utils.py`

```
defquery_machete_supported_group_sizes(act_type: torch.dtype) -> list[int]:
"""
    Queries the supported group sizes for Machete based on the activation type.

    Args:
        act_type: The activation data type (torch.float16, torch.bfloat16).

    Returns:
        A list of supported group sizes. The group size must
        be divisible by `TileShapeK = 128 * 8 // num_bits(act_type)`.
        -1 indicates per-channel quantization.
    """
    if act_type in [torch.float16, torch.bfloat16]:
        return [-1, 64, 128]
    else:
        return [-1, 128]
```