---
title: triton_reshape_and_cache_flash - vLLM
url: https://docs.vllm.ai/en/latest/api/vllm/v1/attention/ops/triton_reshape_and_cache_flash/
source: sitemap
fetched_at: 2026-05-07T21:40:07.189682196-03:00
rendered_js: false
word_count: 0
summary: This function performs per-token, per-head quantization of key and value tensors and writes the resulting quantized data and scale parameters into a paged cache.
tags:
    - quantization
    - kv-cache
    - triton
    - gpu-programming
    - memory-optimization
    - llm-inference
category: api
---

```
deftriton_reshape_and_cache_flash_per_token_head_quant(
    key: torch.Tensor,  # [num_tokens, num_kv_heads, head_size]
    value: torch.Tensor,  # [num_tokens, num_kv_heads, head_size_v]
    key_cache: torch.Tensor,  # [num_blocks, block_size, num_kv_heads, head_size]
    value_cache: torch.Tensor,  # [num_blocks, block_size, num_kv_heads, head_size_v]
    k_scale_cache: torch.Tensor,  # [num_blocks, block_size, num_kv_heads] float32
    v_scale_cache: torch.Tensor,  # [num_blocks, block_size, num_kv_heads] float32
    slot_mapping: torch.Tensor,  # [num_tokens]
):
"""Quantize key/value per (token, head) and write to paged cache.

    Computes one scale = absmax / QUANT_MAX per (token, head), stores
    quantized data in key_cache/value_cache, and stores the float32
    scale in k_scale_cache/v_scale_cache.

    The quantization range (QUANT_MAX, QUANT_MIN) is derived from the
    cache tensor dtype so the same code path works for int8 and fp8.
    """
    cache_dtype = key_cache.dtype
    quant_params = _PER_TOKEN_HEAD_QUANT_PARAMS.get(cache_dtype)
    if quant_params is None:
        raise ValueError(
            f"Per-token-head quantization not supported for cache dtype "
            f"{cache_dtype}.  Supported: {list(_PER_TOKEN_HEAD_QUANT_PARAMS)}"
        )
    quant_max, quant_min = quant_params

    num_tokens, num_kv_heads, head_size = key.shape
    head_size_v = value.shape[2]
    head_size_padded = triton.next_power_of_2(max(head_size, head_size_v))

    block_size = key_cache.shape[1]

    if current_platform.is_rocm() or current_platform.is_xpu():
        num_warps = 4
    else:
        num_warps = min(16, max(1, head_size_padded // 32))

    _reshape_cache_per_token_head[(num_tokens, num_kv_heads)](
        key_ptr=key,
        value_ptr=value,
        key_cache_ptr=key_cache,
        value_cache_ptr=value_cache,
        k_scale_cache_ptr=k_scale_cache,
        v_scale_cache_ptr=v_scale_cache,
        slot_mapping_ptr=slot_mapping,
        stride_key_tok=key.stride(0),
        stride_key_head=key.stride(1),
        stride_val_tok=value.stride(0),
        stride_val_head=value.stride(1),
        stride_kc_blk=key_cache.stride(0),
        stride_kc_slot=key_cache.stride(1),
        stride_kc_head=key_cache.stride(2),
        stride_vc_blk=value_cache.stride(0),
        stride_vc_slot=value_cache.stride(1),
        stride_vc_head=value_cache.stride(2),
        stride_ks_blk=k_scale_cache.stride(0),
        stride_ks_slot=k_scale_cache.stride(1),
        stride_ks_head=k_scale_cache.stride(2),
        stride_vs_blk=v_scale_cache.stride(0),
        stride_vs_slot=v_scale_cache.stride(1),
        stride_vs_head=v_scale_cache.stride(2),
        block_size=block_size,
        head_size=head_size,
        head_size_v=head_size_v,
        HEAD_SIZE_PADDED=head_size_padded,
        QUANT_MAX=quant_max,
        QUANT_MIN=quant_min,
        num_warps=num_warps,
    )
```