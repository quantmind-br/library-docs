---
title: layernorm - vLLM
url: https://docs.vllm.ai/en/latest/api/vllm/ir/ops/layernorm/
source: sitemap
fetched_at: 2026-05-07T21:22:04.039172928-03:00
rendered_js: false
word_count: 8
summary: This document defines the implementation of a weighted root-mean-square layer normalization operator for tensor data processing.
tags:
    - deep-learning
    - layer-normalization
    - tensor-operations
    - rms-norm
    - vllm-ir
category: api
---

Weighted root-mean-square layer normalization

Source code in `vllm/ir/ops/layernorm.py`

```
@register_op
defrms_norm(
    x: Tensor, weight: Tensor | None, epsilon: float, variance_size: int | None = None
) -> Tensor:
"""Weighted root-mean-square layer normalization"""
    orig_dtype = x.dtype
    x = x.to(torch.float32)
    x_var = x if variance_size is None else x[..., :variance_size]
    variance = x_var.pow(2).mean(dim=-1, keepdim=True)
    x = x * torch.rsqrt(variance + epsilon)
    if weight is not None:
        x = x.to(weight.dtype) * weight
    return x.to(orig_dtype)
```