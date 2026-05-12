---
title: quant_utils - vLLM
url: https://docs.vllm.ai/en/latest/api/vllm/model_executor/layers/quantization/utils/quant_utils/
source: sitemap
fetched_at: 2026-05-07T21:28:08.929914532-03:00
rendered_js: false
word_count: 8
summary: This document defines a function for performing group-wise scaled quantization on PyTorch tensors, facilitating conversion to specific data types with scale calculation.
tags:
    - pytorch
    - tensor-quantization
    - floating-point-arithmetic
    - data-scaling
    - neural-network-optimization
category: api
---

```
defscaled_quantize(
    x: torch.Tensor,
    group_shape: GroupShape,
    quant_dtype: torch.dtype,
    compute_dtype: torch.dtype | None = None,
) -> tuple[torch.Tensor, torch.Tensor]:
"""
    Args:
        x: Input tensor to quantize
        group_shape: Shape of quantization groups
        quant_dtype: Target quantized dtype (e.g., torch.float8_e4m3fn)
        compute_dtype: Optional dtype for intermediate computations.
            If None, uses input dtype. Use torch.float32 for higher precision.
    """
    group_shape = _normalize_quant_group_shape(x, group_shape)
    assert quant_dtype.is_floating_point, (
        "currently `scaled_quantize` only supports floating point dtypes "
        "but could be extended to support other dtypes"
    )

    finfo = torch.finfo(quant_dtype)

    # Convert to compute dtype if specified
    x_compute = x if compute_dtype is None else x.to(compute_dtype)

    # Reshape (M, N) into (BLK_M, BLOCK_SIZE_M, BLK_N, BLOCK_SIZE_N)
    assert x.ndim == 2
    assert x.shape[0] % group_shape[0] == 0 and x.shape[1] % group_shape[1] == 0
    blk_m, blk_n = x.shape[0] // group_shape[0], x.shape[1] // group_shape[1]
    x_blkd = x_compute.reshape(blk_m, group_shape[0], blk_n, group_shape[1])

    # Permute to (BLK_M, BLK_N, BLOCK_SIZE_M, BLOCK_SIZE_N)
    x_blkd_permd = x_blkd.permute(0, 2, 1, 3)
    # Flatten to (BLK_M, BLK_N, BLOCK_SIZE_M * BLOCK_SIZE_N)
    x_blkd_permd = x_blkd_permd.flatten(start_dim=2)

    # Compute scales
    min_val, max_val = x_blkd_permd.aminmax(dim=-1)
    amax = torch.maximum(min_val.abs(), max_val.abs()).clamp(min=1e-12)
    _, fp8_max = get_fp8_min_max()
    scale = fp8_max / amax

    # Apply scale and convert from:
    # (BLK_M, BLK_N, BLOCK_SIZE_M * BLOCK_SIZE_N) to (M, N)
    x_scl_sat = (
        (x_blkd_permd * scale.unsqueeze(-1))
        .clamp(min=finfo.min, max=finfo.max)
        .reshape(blk_m, blk_n, group_shape[0], group_shape[1])
        .permute(0, 2, 1, 3)
        .reshape(x.shape)
    )

    return x_scl_sat.to(quant_dtype).contiguous(), scale.float().reciprocal()
```