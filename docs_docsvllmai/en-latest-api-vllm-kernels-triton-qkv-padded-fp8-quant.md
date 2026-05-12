---
title: qkv_padded_fp8_quant - vLLM
url: https://docs.vllm.ai/en/latest/api/vllm/kernels/triton/qkv_padded_fp8_quant/
source: sitemap
fetched_at: 2026-05-07T21:22:18.21410131-03:00
rendered_js: false
word_count: 0
summary: This function provides a Triton-accelerated implementation for quantizing high-dimensional tensors to FP8 format while simultaneously padding the head dimension to a multiple of 16 for hardware efficiency.
tags:
    - fp8-quantization
    - triton-kernel
    - tensor-processing
    - memory-padding
    - high-performance-computing
    - deep-learning-optimization
category: api
---

```
defquantize_fp8_pad_head_dim_triton(
    tensor: torch.Tensor,
    scale: torch.Tensor,
    skip_scale: bool = False,
    block_m: int | None = None,
    block_n: int | None = None,
    num_warps: int | None = None,
) -> torch.Tensor:
"""Quantize a 3D/4D tensor to FP8, padding head_dim to a multiple of 16.

    Reads directly from the input using its 3D strides, so non-contiguous
    views (e.g. Q/K/V slices from an interleaved QKV buffer) are handled
    without an extra copy.  Output is always a fresh contiguous tensor
    with shape (S, H, padded_D).
    """
    if not HAS_TRITON:
        raise RuntimeError("Triton is required to quantize with head_dim padding.")

    original_shape = tensor.shape
    if tensor.dim() == 4:
        tensor = tensor.view(-1, tensor.shape[-2], tensor.shape[-1])
    assert tensor.dim() == 3, f"Expected 3D input (S, H, D), got {tensor.dim()}D"
    S, H, D = tensor.shape
    padded_head_dim = round_up(D, 16)
    out_dtype = current_platform.fp8_dtype()
    output = torch.empty(
        (S, H, padded_head_dim),
        device=tensor.device,
        dtype=out_dtype,
    )

    scale_1d = scale.reshape(-1)
    n_rows = S * H

    if block_m is None or block_n is None or num_warps is None:
        block_m, block_n, num_warps = _get_fp8_pad_quant_config(padded_head_dim)

    grid = (
        triton.cdiv(n_rows, block_m),
        triton.cdiv(padded_head_dim, block_n),
    )

    _quantize_pad_fp8_kernel[grid](
        tensor,
        output,
        scale_1d,
        tensor.stride(0),
        tensor.stride(1),
        tensor.stride(2),
        output.stride(0),
        output.stride(1),
        output.stride(2),
        H,
        n_rows,
        D,
        padded_head_dim,
        _FP8_MIN,
        _FP8_MAX,
        SKIP_SCALE=skip_scale,
        BLOCK_M=block_m,
        BLOCK_N=block_n,
        num_warps=num_warps,
    )

    return output.view((*original_shape[:-1], padded_head_dim))
```