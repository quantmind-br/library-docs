---
title: deepseek_v4_ops - vLLM
url: https://docs.vllm.ai/en/latest/api/vllm/v1/attention/ops/deepseek_v4_ops/
source: sitemap
fetched_at: 2026-05-07T21:39:52.186089145-03:00
rendered_js: false
word_count: 16
summary: This document defines a fused function for applying Rotary Positional Embeddings (RoPE) and quantization to query tensors within a sparse indexer system, supporting both FP8 and MXFP4 formats.
tags:
    - pytorch
    - rope
    - quantization
    - fp8
    - mxfp4
    - tensor-processing
    - kernel-optimization
category: api
---

```
deffused_indexer_q_rope_quant(
    positions: torch.Tensor,
    index_q: torch.Tensor,
    index_q_cos_sin_cache: torch.Tensor,
    # Index weights
    index_weights: torch.Tensor,
    index_weights_softmax_scale: float,
    index_weights_head_scale: float,
    use_fp4: bool = False,
) -> tuple[
    torch.Tensor | tuple[torch.Tensor, torch.Tensor],
    torch.Tensor,
]:
"""Fused RoPE + quantize Q for the sparse indexer.

    Weight-fold semantics (important — the two paths differ):

    FP8 path (use_fp4=False, default):
        q_fp8      : (T, H, HEAD_DIM) float8_e4m3fn, per-token-per-head
                     scalar scale (NOT stored — folded into weights below)
        weights_out = weights * q_scale * softmax_scale * head_scale
        Rationale: a single per-token q_scale is a scalar the downstream FP8
        logits kernel would otherwise multiply in. Folding it into `weights`
        avoids emitting a separate tensor and is free for the logits kernel.

    MXFP4 path (use_fp4=True):
        q_packed   : (T, H, HEAD_DIM // 2) uint8 (2 E2M1 nibbles per byte)
        q_scale    : (T, H, HEAD_DIM // MXFP4_BLOCK_SIZE) uint8 ue8m0 bytes
        weights_out = weights * softmax_scale * head_scale
        Rationale: MXFP4 has PER-BLOCK (32-element) scales that live with
        the Q values — they cannot be folded into a per-token weight
        scalar, so `weights` carries only the softmax and head scales.

    Returns (q_quant, weights_out) where q_quant is either a Tensor (FP8) or
    a (values, scales) tuple (MXFP4). This matches the union type accepted
    by `SparseAttnIndexer.forward_*`.
    """
    assert positions.ndim == 1
    assert index_q.ndim == 3
    assert index_q_cos_sin_cache.ndim == 2

    num_tokens = positions.shape[0]
    num_index_q_heads = index_q.shape[1]
    index_q_head_dim = index_q.shape[2]

    index_weights_out = torch.empty_like(index_weights, dtype=torch.float32)

    if use_fp4:
        assert index_q_head_dim % MXFP4_BLOCK_SIZE == 0, (
            f"head_dim={index_q_head_dim} must be a multiple of MXFP4 block "
            f"size {MXFP4_BLOCK_SIZE}"
        )
        num_scale_blocks = index_q_head_dim // MXFP4_BLOCK_SIZE
        index_q_packed = torch.empty(
            (num_tokens, num_index_q_heads, index_q_head_dim // 2),
            dtype=torch.uint8,
            device=index_q.device,
        )
        index_q_scale = torch.empty(
            (num_tokens, num_index_q_heads, num_scale_blocks),
            dtype=torch.uint8,
            device=index_q.device,
        )
        _fused_indexer_q_rope_mxfp4_kernel[(num_tokens, num_index_q_heads)](
            positions,
            index_q,
            index_q.stride(0),
            index_q.stride(1),
            index_q_cos_sin_cache,
            index_q_cos_sin_cache.stride(0),
            index_q_cos_sin_cache.shape[-1] // 2,
            index_q_packed,
            index_q_packed.stride(0),
            index_q_packed.stride(1),
            index_q_scale,
            index_q_scale.stride(0),
            index_q_scale.stride(1),
            index_q_head_dim,
            MXFP4_BLOCK_SIZE,
            index_weights,
            index_weights.stride(0),
            index_weights_softmax_scale,
            index_weights_head_scale,
            index_weights_out,
            index_weights_out.stride(0),
            num_warps=1,  # TODO: Tune this
        )
        # Values stay uint8 (2 E2M1 nibbles per byte). Scales are 4 ue8m0
        # bytes per (token, head) reinterpreted as one int32, then squeezed
        # from (T, H, 1) to (T, H) to match DeepGEMM's expected q_sf rank
        # (prefill wants 2-D (seq_len, num_heads); decode reshapes this to
        # 3-D (batch, next_n, num_heads)).
        return (
            index_q_packed,
            index_q_scale.view(torch.int32).squeeze(-1),
        ), index_weights_out

    index_q_fp8 = torch.empty_like(index_q, dtype=torch.float8_e4m3fn)
    _fused_indexer_q_rope_quant_kernel[(num_tokens, num_index_q_heads)](
        positions,
        index_q,
        index_q.stride(0),
        index_q.stride(1),
        index_q_cos_sin_cache,
        index_q_cos_sin_cache.stride(0),
        index_q_cos_sin_cache.shape[-1] // 2,
        index_q_fp8,
        index_q_fp8.stride(0),
        index_q_fp8.stride(1),
        index_q_head_dim,
        index_weights,
        index_weights.stride(0),
        index_weights_softmax_scale,
        index_weights_head_scale,
        index_weights_out,
        index_weights_out.stride(0),
        num_warps=1,  # TODO: Tune this
    )
    return index_q_fp8, index_weights_out
```