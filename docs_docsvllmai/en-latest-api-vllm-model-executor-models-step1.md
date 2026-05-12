---
title: step1 - vLLM
url: https://docs.vllm.ai/en/latest/api/vllm/model_executor/models/step1/
source: sitemap
fetched_at: 2026-05-07T21:33:22.961166505-03:00
rendered_js: false
word_count: 24
summary: This document provides the reference implementation for calculating ALiBi slopes used by the Step model architecture within the vLLM framework.
tags:
    - vllm
    - alibi-slopes
    - model-executor
    - attention-mechanism
    - tensor-computation
category: reference
---

## vllm.model\_executor.models.step1 [¶](#vllm.model_executor.models.step1 "Permanent link")

Shared Step decoder blocks and the Step1 text model.

## \_get\_step\_alibi\_slopes [¶](#vllm.model_executor.models.step1._get_step_alibi_slopes "Permanent link")

```
_get_step_alibi_slopes(total_num_heads: int) -> Tensor
```

Reference ALiBi slopes used by Step models.

Source code in `vllm/model_executor/models/step1.py`

```
def_get_step_alibi_slopes(total_num_heads: int) -> torch.Tensor:
"""Reference ALiBi slopes used by Step models."""
    closest_power_of_2 = 2 ** math.floor(math.log2(total_num_heads))
    base = torch.tensor(
        2 ** (-8.0 / closest_power_of_2),
        dtype=torch.float32,
    )
    slopes = torch.pow(
        base,
        torch.arange(1, 1 + closest_power_of_2, dtype=torch.int32),
    )
    if closest_power_of_2 != total_num_heads:
        extra_base = torch.tensor(
            2 ** (-4.0 / closest_power_of_2),
            dtype=torch.float32,
        )
        num_remaining_heads = total_num_heads - closest_power_of_2
        extra_powers = torch.arange(
            1,
            1 + 2 * num_remaining_heads,
            2,
            dtype=torch.int32,
        )
        slopes = torch.cat(
            [slopes, torch.pow(extra_base, extra_powers)],
            dim=0,
        )
    return slopes
```