---
title: vit_attn_wrappers - vLLM
url: https://docs.vllm.ai/en/latest/api/vllm/v1/attention/ops/vit_attn_wrappers/
source: sitemap
fetched_at: 2026-05-07T21:40:11.048908667-03:00
rendered_js: false
word_count: 91
summary: This document outlines the ViT attention wrapper operations designed to improve performance and compatibility with torch.compile for vision models within the vLLM framework.
tags:
    - vit-attention
    - torch-compile
    - performance-optimization
    - sdpa
    - vision-models
    - vllm-ops
category: reference
---

## vllm.v1.attention.ops.vit\_attn\_wrappers [¶](#vllm.v1.attention.ops.vit_attn_wrappers "Permanent link")

This file contains ops for ViT attention to be compatible with torch.compile as there are operations here not supported by torch.compile (for instance, `.item()` in flash attention)

Using these ops and wrapping vision blocks with `torch.compile` can speed up throughput in vision models by ~5% relative on H100, and improve token latencies by ~7% (see qwen2\_5\_vl for example usage)

To use these ops, you must have a recent version of PyTorch installed (&gt;= 2.4.0)

## apply\_sdpa [¶](#vllm.v1.attention.ops.vit_attn_wrappers.apply_sdpa "Permanent link")

Input shape: (batch\_size x seq\_len x num\_heads x head\_size)

Source code in `vllm/v1/attention/ops/vit_attn_wrappers.py`

```
defapply_sdpa(
    q: torch.Tensor,
    k: torch.Tensor,
    v: torch.Tensor,
    scale: float | None = None,
    enable_gqa: bool = False,
) -> torch.Tensor:
"""
    Input shape:
    (batch_size x seq_len x num_heads x head_size)
    """
    q, k, v = (einops.rearrange(x, "b s h d -> b h s d") for x in [q, k, v])
    output = F.scaled_dot_product_attention(
        q, k, v, dropout_p=0.0, scale=scale, enable_gqa=enable_gqa
    )
    output = einops.rearrange(output, "b h s d -> b s h d ")
    return output
```