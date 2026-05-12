---
title: cache_utils - vLLM
url: https://docs.vllm.ai/en/latest/api/vllm/v1/attention/ops/deepseek_v4_ops/cache_utils/
source: sitemap
fetched_at: 2026-05-07T21:39:53.124483863-03:00
rendered_js: false
word_count: 0
summary: This document defines a Triton JIT kernel for quantizing K-cache tensors into an FP8 format for use in optimized paged KV-caching systems.
tags:
    - triton
    - kernel
    - quantization
    - fp8
    - kv-cache
    - gpu-programming
    - memory-optimization
category: api
---

```
@triton.jit
defquantize_and_insert_k_kernel(
    # Input tensors
    k_ptr,  # [num_tokens, 512] bf16
    slot_mapping_ptr,  # [num_tokens] int64
    # Output tensor
    k_cache_ptr,  # [num_blocks, block_bytes] as uint8 (flattened view)
    # Dimensions
    num_tokens,
    input_dim: tl.constexpr,  # 512
    fp8_dim: tl.constexpr,  # 448
    bf16_dim: tl.constexpr,  # 64
    scale_dim: tl.constexpr,  # 8
    quant_block: tl.constexpr,  # 64 (quantization block size)
    cache_block_size: tl.constexpr,  # 64 (paged cache block size)
    token_data_size: tl.constexpr,  # 576 bytes per token data
    block_stride: tl.constexpr,  # total bytes per block (padded)
    fp8_max: tl.constexpr,
    n_quant_blocks: tl.constexpr,  # 8 (7 real + 1 padding)
):
"""
    Quantize K tensor and insert into paged K cache.

    K Cache block layout (block_size=64 tokens):
    - [0, 64*576): Token data, each token has 448 fp8 + 128 bf16
    - [64*576, 64*576 + 64*8): Scales, each token has 8 uint8 scales
    - [64*576 + 64*8, block_stride): Padding

    One program per token.
    """
    pid = tl.program_id(0)

    if pid >= num_tokens:
        return

    # Get slot mapping
    slot_idx = tl.load(slot_mapping_ptr + pid)
    if slot_idx == -1:
        return

    block_idx = slot_idx // cache_block_size
    pos_in_block = slot_idx % cache_block_size

    # Input pointer for this token
    input_row_ptr = k_ptr + pid * input_dim

    # int64: block_idx * block_stride can exceed 2^31 with many KV-cache blocks
    # (e.g. >= 57K at block_stride ~37K). Matches gather path below.
    cache_block_ptr = k_cache_ptr + block_idx.to(tl.int64) * block_stride

    # Token data pointer: token data is stored contiguously at start of block
    # Each token's data is at offset pos_in_block * token_data_size
    token_data_ptr = cache_block_ptr + pos_in_block * token_data_size

    # Scale pointer: scales are stored after ALL token data in the block
    # Scale for this token is at offset (64 * 576) + pos_in_block * 8
    token_scale_ptr = (
        cache_block_ptr + cache_block_size * token_data_size + pos_in_block * scale_dim
    )

    # Token data layout: [0:448] fp8, [448:576] bf16
    token_fp8_ptr = token_data_ptr
    token_bf16_ptr = token_data_ptr + fp8_dim

    # ========== Quantize and store FP8 portion (first 448 elements) ==========
    # Using UE8M0 quantization strategy (scale is power of 2, stored as uint8 exponent)
    for qblock_idx in tl.static_range(n_quant_blocks):
        qblock_start = qblock_idx * quant_block

        if qblock_start < fp8_dim:
            offsets = qblock_start + tl.arange(0, quant_block)
            mask = offsets < fp8_dim

            # Load bf16 input
            x = tl.load(input_row_ptr + offsets, mask=mask, other=0.0)

            # Compute absmax scale (same as CUDA kernel)
            abs_x = tl.abs(x)
            block_max = tl.max(abs_x, axis=0)
            block_max = tl.maximum(block_max, 1e-4)  # Match CUDA: fmaxf(amax, 1e-4)

            # UE8M0: Round scale UP to next power of 2
            # scale = 2^ceil(log2(block_max / fp8_max))
            raw_scale = block_max / fp8_max
            log_scale = tl.log2(raw_scale)
            exponent = tl.ceil(log_scale)  # Round UP to next integer exponent
            scale = tl.exp2(exponent)  # scale = 2^exponent (power of 2)

            # Quantize to fp8: fp8_value = bf16_value / scale
            x_scaled = x / scale
            x_clamped = tl.clamp(x_scaled, -fp8_max, fp8_max)

            # Convert to fp8, then bitcast to uint8 for storage
            x_fp8 = x_clamped.to(tl.float8e4nv)
            x_uint8 = x_fp8.to(tl.uint8, bitcast=True)

            # Store as uint8 (1 byte each)
            tl.store(token_fp8_ptr + offsets, x_uint8, mask=mask)

            # UE8M0 scale encoding: stored_value = exponent + 127 (bias)
            # During dequant: scale = 2^(stored_value - 127)
            encoded_scale = exponent + 127.0
            encoded_scale = tl.maximum(tl.minimum(encoded_scale, 255.0), 0.0)
            tl.store(token_scale_ptr + qblock_idx, encoded_scale.to(tl.uint8))

    # Padding scale at index 7
    tl.store(token_scale_ptr + 7, tl.zeros((), dtype=tl.uint8))

    # ========== Store BF16 portion (last 64 elements, no quantization) ==========
    bf16_input_offset = fp8_dim

    # Process bf16 in chunks of 16
    bf16_out_ptr = token_bf16_ptr.to(tl.pointer_type(tl.bfloat16))
    for i in tl.static_range(bf16_dim // 16):
        chunk_offsets = i * 16 + tl.arange(0, 16)
        bf16_vals = tl.load(input_row_ptr + bf16_input_offset + chunk_offsets)
        tl.store(bf16_out_ptr + chunk_offsets, bf16_vals)
```