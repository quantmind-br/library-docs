---
title: fused_inv_rope_fp8_quant - vLLM
url: https://docs.vllm.ai/en/latest/api/vllm/v1/attention/ops/deepseek_v4_ops/fused_inv_rope_fp8_quant/
source: sitemap
fetched_at: 2026-05-07T21:39:56.280804653-03:00
rendered_js: false
word_count: 0
summary: This document defines a PyTorch function for performing fused inverse Rotary Positional Embedding (RoPE) operations followed by block-scaled FP8 quantization.
tags:
    - pytorch
    - fp8-quantization
    - rope
    - gpu-kernels
    - attention-optimization
    - vllm
category: api
---

```
deffused_inv_rope_fp8_quant(
    o: torch.Tensor,
    positions: torch.Tensor,
    cos_sin_cache: torch.Tensor,
    n_groups: int,
    heads_per_group: int,
    nope_dim: int = 448,
    rope_dim: int = 64,
    quant_group_size: int = 128,
    tma_aligned_scales: bool = False,
) -> tuple[torch.Tensor, torch.Tensor]:
"""Fused inverse RoPE + block-scaled FP8 quantization.

    Args:
        o: Attention output [num_tokens, num_heads, head_dim] bf16.
        positions: Token positions [num_tokens] int64.
        cos_sin_cache: Precomputed [max_pos, rope_dim] with cos||sin.
        n_groups: Number of output groups.
        heads_per_group: Heads per group.
        nope_dim: Non-RoPE dimensions per head (default 448).
        rope_dim: RoPE dimensions per head (default 64).
        quant_group_size: FP8 quantization block size (default 128).
        tma_aligned_scales: Output INT32 packed UE8M0 for SM100 (True)
                            or FP32 for SM90 (False).

    Returns:
        o_fp8: [T, G, D] float8_e4m3fn, strides (D, T*D, 1).
        o_scale: Pre-transformed scale tensor for fp8_einsum.
    """
    fromvllm.utils.deep_gemmimport get_tma_aligned_size

    num_tokens, num_heads, head_dim = o.shape
    assert num_heads == n_groups * heads_per_group
    assert head_dim == nope_dim + rope_dim
    assert head_dim % quant_group_size == 0
    assert nope_dim % quant_group_size == (quant_group_size - rope_dim)
    assert rope_dim % 2 == 0
    assert cos_sin_cache.shape[-1] == rope_dim
    assert cos_sin_cache.dtype == torch.float32

    d = heads_per_group * head_dim
    num_scale_blocks = d // quant_group_size
    chunks_per_head = head_dim // quant_group_size

    fp8_dtype = torch.float8_e4m3fn
    fp8_max = torch.finfo(fp8_dtype).max

    tma_aligned_T = get_tma_aligned_size(num_tokens, 4)
    if tma_aligned_scales:
        packed_sf_k = (num_scale_blocks + 3) // 4
        scale_inner = packed_sf_k
    else:
        scale_inner = num_scale_blocks

    # Run kernel through a custom op so inductor sees an opaque boundary.
    # It's a pytorch bug, see https://github.com/vllm-project/vllm/issues/41106
    fp8_buf, scale_buf = torch.ops.vllm.fused_inv_rope_fp8_quant_kernel(
        o,
        positions,
        cos_sin_cache,
        heads_per_group,
        quant_group_size,
        chunks_per_head,
        nope_dim % quant_group_size,
        rope_dim // 2,
        tma_aligned_scales,
        fp8_max,
        tma_aligned_T,
        num_tokens,
        n_groups,
        d,
        scale_inner,
    )
    return fp8_buf.transpose(0, 1), scale_buf.transpose(0, 1)
```