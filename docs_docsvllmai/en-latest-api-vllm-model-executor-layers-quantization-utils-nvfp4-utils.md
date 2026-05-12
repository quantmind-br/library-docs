---
title: nvfp4_utils - vLLM
url: https://docs.vllm.ai/en/latest/api/vllm/model_executor/layers/quantization/utils/nvfp4_utils/
source: sitemap
fetched_at: 2026-05-07T21:28:06.777453879-03:00
rendered_js: false
word_count: 142
summary: This document provides utility functions for preparing FP4 activations, weights, and block-scales to meet the specific memory alignment and layout requirements of CUTLASS and FlashInfer kernels.
tags:
    - fp4-quantization
    - tensor-alignment
    - memory-layout
    - cutlass
    - flashinfer
    - model-optimization
category: api
---

## pad\_nvfp4\_activation\_for\_cutlass [¶](#vllm.model_executor.layers.quantization.utils.nvfp4_utils.pad_nvfp4_activation_for_cutlass "Permanent link")

```
pad_nvfp4_activation_for_cutlass(
    x_fp4: Tensor, weights_padding_bytes: int
) -> Tensor
```

Pad packed FP4 activations to match the K-dimension padding applied to weights. The padding is in bytes (tensor dimension), not FP4 elements.

Source code in `vllm/model_executor/layers/quantization/utils/nvfp4_utils.py`

```
defpad_nvfp4_activation_for_cutlass(
    x_fp4: torch.Tensor,
    weights_padding_bytes: int,
) -> torch.Tensor:
"""
    Pad packed FP4 activations to match the K-dimension padding applied to weights.
    The padding is in bytes (tensor dimension), not FP4 elements.
    """
    if weights_padding_bytes > 0:
        return torch.nn.functional.pad(x_fp4, (0, weights_padding_bytes)).contiguous()
    return x_fp4
```

## pad\_nvfp4\_weight\_for\_cutlass [¶](#vllm.model_executor.layers.quantization.utils.nvfp4_utils.pad_nvfp4_weight_for_cutlass "Permanent link")

Pad packed NVFP4 weights so that both N (rows) and K (columns) satisfy the alignment constraints required by CUTLASS / FlashInfer FP4 kernels.

CUTLASS FP4 kernel requires both K and N matrix dimensions to be divisible by 32 for aligned memory access and efficient tensor core operations.

Source code in `vllm/model_executor/layers/quantization/utils/nvfp4_utils.py`

```
defpad_nvfp4_weight_for_cutlass(
    weight: torch.Tensor,
    alignment: int = 32,
) -> tuple[torch.Tensor, int]:
"""
    Pad packed NVFP4 weights so that both N (rows) and K (columns) satisfy
    the alignment constraints required by CUTLASS / FlashInfer FP4 kernels.

    CUTLASS FP4 kernel requires both K and N matrix dimensions to be divisible
    by 32 for aligned memory access and efficient tensor core operations.
    """
    weight_current_rows = weight.shape[0]

    # Pad N dimension (rows) if not aligned
    if weight_current_rows % alignment != 0:
        total_rows = round_up(weight_current_rows, alignment)
        pad_rows = total_rows - weight_current_rows
        weight = torch.nn.functional.pad(weight, (0, 0, 0, pad_rows)).contiguous()

    # Check K dimension alignment
    # 2 FP4 items are packed per byte in the input dimension
    weight_current_col_bytes = weight.shape[1]
    weight_current_col_elements = weight_current_col_bytes * 2

    weights_padding_bytes = 0
    if weight_current_col_elements % alignment != 0:
        total_cols = round_up(weight_current_col_elements, alignment)
        pad_cols = total_cols - weight_current_col_elements
        # Convert from FP4 element count to bytes (2 FP4 values per byte)
        # pad_cols is always even since alignment=32 and current elements are even
        pad_bytes = pad_cols // 2
        weight = torch.nn.functional.pad(weight, (0, pad_bytes, 0, 0)).contiguous()
        weights_padding_bytes = pad_bytes

    return weight, weights_padding_bytes
```

## slice\_nvfp4\_output [¶](#vllm.model_executor.layers.quantization.utils.nvfp4_utils.slice_nvfp4_output "Permanent link")

Slice the output tensor to remove padding in N dimension if weight was padded.

Source code in `vllm/model_executor/layers/quantization/utils/nvfp4_utils.py`

```
defslice_nvfp4_output(
    out: torch.Tensor,
    output_size: int,
) -> torch.Tensor:
"""
    Slice the output tensor to remove padding in N dimension if weight was padded.
    """
    if out.shape[-1] != output_size:
        return out[..., :output_size].contiguous()
    return out
```

## swizzle\_blockscale [¶](#vllm.model_executor.layers.quantization.utils.nvfp4_utils.swizzle_blockscale "Permanent link")

Pad and block-interleave the FP4 block-scales so that they match the data layout expected by the CUTLASS / FlashInfer kernels.

#### Parameters[¶](#vllm.model_executor.layers.quantization.utils.nvfp4_utils.swizzle_blockscale--parameters "Permanent link")

scale: torch.Tensor

#### Returns[¶](#vllm.model_executor.layers.quantization.utils.nvfp4_utils.swizzle_blockscale--returns "Permanent link")

torch.Tensor The swizzled tensor with the same logical shape as *scale*.

Source code in `vllm/model_executor/layers/quantization/utils/nvfp4_utils.py`

```
defswizzle_blockscale(scale: torch.Tensor) -> torch.Tensor:
"""
    Pad and block-interleave the FP4 block-scales so that they match the data
    layout expected by the CUTLASS / FlashInfer kernels.

    Parameters
    ----------
    scale: torch.Tensor

    Returns
    -------
    torch.Tensor
        The swizzled tensor with the same logical shape as *scale*.
    """
    assert scale.dtype == torch.float8_e4m3fn, (
        "swizzle_blockscale expects the input tensor to be in "
        "torch.float8_e4m3fn format."
    )

    scale_ndim = scale.ndim
    if scale_ndim == 2:
        scale = scale.unsqueeze(0)  # (1, M, K)
    assert scale.ndim == 3, "Expected a 2-D or 3-D tensor for block scales."

    B, M, K = scale.shape

    M_padded = round_up(M, 128)
    K_padded = round_up(K, 4)

    padded = torch.zeros(
        (B, M_padded, K_padded), dtype=scale.dtype, device=scale.device
    )
    padded[:B, :M, :K] = scale

    # Reshape / permute to the layout required by the kernel.
    padded = padded.reshape(B, M_padded // 128, 4, 32, K_padded // 4, 4)
    swizzled = padded.permute(0, 1, 4, 3, 2, 5).contiguous().cuda()

    if scale_ndim == 2:
        return swizzled.reshape(M_padded, K_padded)
    return swizzled.reshape(B, M_padded, K_padded)
```