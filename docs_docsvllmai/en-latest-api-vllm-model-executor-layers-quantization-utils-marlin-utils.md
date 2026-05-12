---
title: marlin_utils - vLLM
url: https://docs.vllm.ai/en/latest/api/vllm/model_executor/layers/quantization/utils/marlin_utils/
source: sitemap
fetched_at: 2026-05-07T21:28:00.004460315-03:00
rendered_js: false
word_count: 18
summary: This function calculates the MoE intermediate size for Marlin-quantized weight matrices by multiplying the column count of the second packed weight matrix by the fixed Marlin tile size.
tags:
    - marlin-quantization
    - moe
    - weight-matrix
    - tensor-manipulation
    - model-executor
category: reference
---

Given Marlin packed weight matrices w1\_packed, and w2\_packed, return the MoE intermediate size N

Source code in `vllm/model_executor/layers/quantization/utils/marlin_utils.py`

```
defmarlin_moe_intermediate_size(w1_packed: torch.Tensor, w2_packed: torch.Tensor):
"""
    Given Marlin packed weight matrices w1_packed, and w2_packed,
    return the MoE intermediate size N
    """
    marlin_tile_size = 16
    return w2_packed.size(1) * marlin_tile_size
```