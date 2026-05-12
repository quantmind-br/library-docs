---
title: topk_topp_triton - vLLM
url: https://docs.vllm.ai/en/latest/api/vllm/v1/sample/ops/topk_topp_triton/
source: sitemap
fetched_at: 2026-05-07T21:41:33.144289534-03:00
rendered_js: false
word_count: 227
summary: This document describes the implementation of high-performance Triton kernels for applying combined top-k and top-p logit masking, including helper functions for statistical tracking across GPU tiles.
tags:
    - triton-kernels
    - logit-sampling
    - top-k-sampling
    - top-p-sampling
    - gpu-optimization
    - vllm
category: api
---

## vllm.v1.sample.ops.topk\_topp\_triton [¶](#vllm.v1.sample.ops.topk_topp_triton "Permanent link")

Combined Top-K and Top-P Triton kernels.

Based on the paper "Qrita: High-performance Top-k and Top-p Algorithm for GPUs using Pivot-based Truncation and Selection" By Park et al. (https://arxiv.org/abs/2602.01518)

## \_update\_min\_larger\_stats [¶](#vllm.v1.sample.ops.topk_topp_triton._update_min_larger_stats "Permanent link")

```
_update_min_larger_stats(
    data, above_mask, min_larger, num_min_larger, sentinel
)
```

Update running (min, count) of values above a pivot across tiles.

Tracks the smallest value strictly above a pivot and how many times it occurs. Called once per tile per pivot; the running state is carried across tiles via `min_larger` / `num_min_larger`.

Merge rule

- tile min &lt; running min → replace both
- tile min == running min → accumulate count
- tile min &gt; running min → keep running values

Source code in `vllm/v1/sample/ops/topk_topp_triton.py`

```
@triton.jit
def_update_min_larger_stats(data, above_mask, min_larger, num_min_larger, sentinel):
"""Update running (min, count) of values above a pivot across tiles.

    Tracks the smallest value strictly above a pivot and how many times
    it occurs.  Called once per tile per pivot; the running state is
    carried across tiles via `min_larger` / `num_min_larger`.

    Merge rule:
      - tile min < running min  → replace both
      - tile min == running min → accumulate count
      - tile min > running min  → keep running values
    """
    tile_min = tl.min(tl.where(above_mask, data, sentinel))
    tile_eq = above_mask & (tl.abs(data - tile_min) < 1e-9)
    tile_cnt = tl.sum(tile_eq)
    is_new = tile_min < min_larger
    is_same = tl.abs(tile_min - min_larger) < 1e-9
    num_min_larger = tl.where(is_new, tile_cnt, num_min_larger + tile_cnt * is_same)
    min_larger = tl.minimum(min_larger, tile_min)
    return min_larger, num_min_larger
```

## apply\_top\_k\_top\_p\_triton [¶](#vllm.v1.sample.ops.topk_topp_triton.apply_top_k_top_p_triton "Permanent link")

Apply combined top-k and top-p masking using Triton.

Top-k is applied first (by logit value), then top-p is applied to the remaining k values (by probability).

Parameters:

Name Type Description Default `logits` `Tensor`

\[batch\_size, vocab\_size] float32 tensor, modified in-place

*required* `k` `Tensor | None`

\[batch\_size] int32 tensor of top-k values per row, or None to disable top-k

*required* `p` `Tensor | None`

\[batch\_size] float32 tensor of top-p values per row (0 to 1), or None to disable top-p

*required* `mask_value` `float`

Value for masked positions (default: -inf)

`float('-inf')`

Returns:

Type Description `Tensor`

The logits tensor (modified in-place)

Source code in `vllm/v1/sample/ops/topk_topp_triton.py`

```
defapply_top_k_top_p_triton(
    logits: torch.Tensor,
    k: torch.Tensor | None,
    p: torch.Tensor | None,
    mask_value: float = float("-inf"),
) -> torch.Tensor:
"""
    Apply combined top-k and top-p masking using Triton.

    Top-k is applied first (by logit value), then top-p is applied
    to the remaining k values (by probability).

    Args:
        logits: [batch_size, vocab_size] float32 tensor, modified in-place
        k: [batch_size] int32 tensor of top-k values per row, or None to disable top-k
        p: [batch_size] float32 tensor of top-p values per row (0 to 1),
            or None to disable top-p
        mask_value: Value for masked positions (default: -inf)

    Returns:
        The logits tensor (modified in-place)
    """
    assert logits.ndim == 2
    assert logits.dtype == torch.float32

    batch_size, vocab_size = logits.shape

    topk_enabled = k is not None
    topp_enabled = p is not None

    if batch_size == 0 or not (topk_enabled or topp_enabled):
        return logits

    if k is not None:
        assert k.ndim == 1 and k.shape[0] == batch_size
        k_ptr = k.to(torch.int32)
    else:
        k_ptr = logits  # Dummy pointer (won't be read)

    if p is not None:
        assert p.ndim == 1 and p.shape[0] == batch_size
        p_ptr = p.to(torch.float32)
    else:
        p_ptr = logits  # Dummy pointer (won't be read)

    num_sm = num_compute_units(logits.device.index)
    NUM_PROGRAMS = min(num_sm, batch_size)

    # Cache per-Triton Program buffer on each device.
    buf_key = (logits.device, logits.dtype, vocab_size)
    buffer = _TRITON_BUFFER_CACHE.get(buf_key)
    if buffer is None or buffer.shape[0] < NUM_PROGRAMS:
        size = min(next_power_of_2(NUM_PROGRAMS), num_sm)
        buffer = logits.new_empty((size, vocab_size))
        _TRITON_BUFFER_CACHE[buf_key] = buffer
    if buffer.shape[0] > NUM_PROGRAMS:
        buffer = buffer[:NUM_PROGRAMS]

    # Cache lookup table entries on each device.
    tables = _TRITON_TABLE_CACHE.get(logits.device)
    if tables is None:
        normal_cdf_to_sigma_table = logits.new_tensor(_NORMAL_CDF_TO_SIGMA_TABLE)
        percentile_to_std_table = logits.new_tensor(_PERCENTILE_TO_STD_TABLE)
        _TRITON_TABLE_CACHE[logits.device] = (
            normal_cdf_to_sigma_table,
            percentile_to_std_table,
        )
    else:
        normal_cdf_to_sigma_table, percentile_to_std_table = tables

    _topk_topp_kernel[(NUM_PROGRAMS,)](
        logits,
        buffer,
        percentile_to_std_table,
        normal_cdf_to_sigma_table,
        k_ptr,
        p_ptr,
        BATCH_SIZE=batch_size,
        MASK_VALUE=mask_value,
        VOCAB_SIZE=vocab_size,
        BLOCK_SIZE=8192,
        BLOCK_SIZE_TRUNC=4096,
        TOPK_ENABLED=topk_enabled,
        TOPP_ENABLED=topp_enabled,
    )

    return logits
```