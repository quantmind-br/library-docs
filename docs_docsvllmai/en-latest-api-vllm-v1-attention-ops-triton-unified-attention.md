---
title: triton_unified_attention - vLLM
url: https://docs.vllm.ai/en/latest/api/vllm/v1/attention/ops/triton_unified_attention/
source: sitemap
fetched_at: 2026-05-07T21:40:10.087909729-03:00
rendered_js: false
word_count: 133
summary: This document provides technical documentation and internal implementation details for unified attention operations, including KV tile casting and Gemma3-specific tile size optimizations within the vLLM framework.
tags:
    - vllm
    - triton
    - attention-mechanism
    - kv-cache
    - quantization
    - gemma3
    - cuda-optimization
category: reference
---

## vllm.v1.attention.ops.triton\_unified\_attention [¶](#vllm.v1.attention.ops.triton_unified_attention "Permanent link")

## \_cast\_kv\_tile [¶](#vllm.v1.attention.ops.triton_unified_attention._cast_kv_tile "Permanent link")

```
_cast_kv_tile(
    data, Q, tensor_scale, KV_QUANT_MODE: constexpr
)
```

Cast a loaded KV tile to Q's dtype, dequantizing if needed.

Modes handled inside the core kernel:

- `KV_QUANT_MODE == 0` (NONE) and `2` (INT8 per-token-head) and `3` (FP8 per-token-head): plain cast. Per-token-head modes apply their scales separately on S/P inside the loop.
- `KV_QUANT_MODE == 1` (FP8 per-tensor): dequantize using the tensor-wide scale.

Source code in `vllm/v1/attention/ops/triton_unified_attention.py`

```
@triton.jit
def_cast_kv_tile(data, Q, tensor_scale, KV_QUANT_MODE: tl.constexpr):
"""Cast a loaded KV tile to Q's dtype, dequantizing if needed.

    Modes handled inside the core kernel:

    - ``KV_QUANT_MODE == 0`` (NONE) and ``2`` (INT8 per-token-head) and
      ``3`` (FP8 per-token-head): plain cast.  Per-token-head modes apply
      their scales separately on S/P inside the loop.
    - ``KV_QUANT_MODE == 1`` (FP8 per-tensor): dequantize using the
      tensor-wide scale.
    """
    if KV_QUANT_MODE == 1:
        if Q.dtype.is_fp8():
            return data.to(Q.dtype)
        return (data.to(tl.float32) * tl.load(tensor_scale)).to(Q.dtype)
    return data.to(Q.dtype)
```

## \_get\_tile\_size [¶](#vllm.v1.attention.ops.triton_unified_attention._get_tile_size "Permanent link")

```
_get_tile_size(
    head_size: int,
    sliding_window: int,
    element_size: int,
    is_prefill: bool,
) -> int
```

Select tile size with Gemma3-specific optimization.

Source code in `vllm/v1/attention/ops/triton_unified_attention.py`

```
def_get_tile_size(
    head_size: int,
    sliding_window: int,
    element_size: int,
    is_prefill: bool,
) -> int:
"""Select tile size with Gemma3-specific optimization."""
    if _is_gemma3_attention(head_size, sliding_window):
        # Gemma3: use 32 for decode (default is 16)
        return 32

    # Default behavior
    if is_prefill:
        return 32
    # Note: tile size must be at least 32 for fp8 (element_size == 1).
    return 16 if element_size >= 2 else 32
```

## \_is\_gemma3\_attention [¶](#vllm.v1.attention.ops.triton_unified_attention._is_gemma3_attention "Permanent link")

```
_is_gemma3_attention(
    head_size: int, sliding_window: int
) -> bool
```

Detect Gemma3 models via unique (head\_size, sliding\_window) signature.

Gemma3 models are the only ones using sliding\_window=1024 with head\_size 128 (27B) or 256 (1B, 4B, 12B). Other SWA models use different window sizes (Mistral=4096, Phi-3=2047).

Source code in `vllm/v1/attention/ops/triton_unified_attention.py`

```
def_is_gemma3_attention(head_size: int, sliding_window: int) -> bool:
"""Detect Gemma3 models via unique (head_size, sliding_window) signature.

    Gemma3 models are the only ones using sliding_window=1024 with
    head_size 128 (27B) or 256 (1B, 4B, 12B). Other SWA models use
    different window sizes (Mistral=4096, Phi-3=2047).
    """
    return sliding_window == 1024 and head_size in (128, 256)
```