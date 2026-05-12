---
title: qutlass_utils - vLLM
url: https://docs.vllm.ai/en/latest/api/vllm/model_executor/layers/quantization/qutlass_utils/
source: sitemap
fetched_at: 2026-05-07T21:27:41.843029913-03:00
rendered_js: false
word_count: 212
summary: This document provides utility functions to rearrange matrix data into block-scaled swizzle formats using PyTorch and Triton, aligning with NVIDIA's hardware-specific layout requirements for optimized tensor operations.
tags:
    - matrix-rearrangement
    - tensor-processing
    - triton-kernel
    - quantization
    - gpu-optimization
    - swizzle-format
category: reference
---

## to\_blocked [¶](#vllm.model_executor.layers.quantization.qutlass_utils.to_blocked "Permanent link")

Rearrange a large matrix by breaking it into blocks and applying the rearrangement pattern.

See

https://docs.nvidia.com/cuda/cublas/index.html#d-block-scaling-factors-layout

Parameters:

Name Type Description Default `input_matrix` `Tensor`

Input tensor of shape (H, W)

*required* `backend` `Literal['torch', 'triton']`

"torch" (PyTorch path) or "triton" (Triton kernel)

`'triton'`

Returns:

Type Description `Tensor`

Rearranged tensor of shape (32*cdiv(H,128), 16*cdiv(W,4))

Source code in `vllm/model_executor/layers/quantization/qutlass_utils.py`

```
defto_blocked(
    input_matrix: torch.Tensor, backend: Literal["torch", "triton"] = "triton"
) -> torch.Tensor:
"""
    Rearrange a large matrix by breaking it into blocks and applying
    the rearrangement pattern.

    See:
        https://docs.nvidia.com/cuda/cublas/index.html#d-block-scaling-factors-layout

    Args:
        input_matrix: Input tensor of shape (H, W)
        backend: "torch" (PyTorch path) or "triton" (Triton kernel)

    Returns:
        Rearranged tensor of shape (32*cdiv(H,128), 16*cdiv(W,4))
    """
    if backend == "triton":
        return triton_mx_block_rearrange(input_matrix).flatten()
    elif backend != "torch":
        raise ValueError(f'backend must be "torch" or "triton", got {backend!r}')

    rows, cols = input_matrix.shape
    n_row_blocks = cdiv(rows, 128)
    n_col_blocks = cdiv(cols, 4)

    # Calculate the padded shape
    padded_rows = n_row_blocks * 128
    padded_cols = n_col_blocks * 4

    padded = input_matrix
    assert (rows, cols) == (padded_rows, padded_cols)

    # Rearrange the blocks
    blocks = padded.view(n_row_blocks, 128, n_col_blocks, 4).permute(0, 2, 1, 3)
    rearranged = blocks.reshape(-1, 4, 32, 4).transpose(1, 2).reshape(-1, 32, 16)

    return rearranged.flatten()
```

## triton\_mx\_block\_rearrange [¶](#vllm.model_executor.layers.quantization.qutlass_utils.triton_mx_block_rearrange "Permanent link")

Rearranges an E8M0 tensor scale from row-major format to block-scaled swizzle format.

This format is suitable for Tmem as described in NVIDIA documentation: https://docs.nvidia.com/cuda/cublas/index.html#d-block-scaling-factors-layout

Parameters:

Name Type Description Default `scale_tensor` `Tensor`

Input tensor in row-major format with 8-bit elements

*required*

Returns:

Type Description `Tensor`

Rearranged tensor in block-scaled swizzle format

Source code in `vllm/model_executor/layers/quantization/qutlass_utils.py`

```
deftriton_mx_block_rearrange(scale_tensor: torch.Tensor) -> torch.Tensor:
"""
    Rearranges an E8M0 tensor scale from row-major format to
    block-scaled swizzle format.

    This format is suitable for Tmem as described in NVIDIA documentation:
    https://docs.nvidia.com/cuda/cublas/index.html#d-block-scaling-factors-layout

    Args:
        scale_tensor: Input tensor in row-major format with 8-bit elements

    Returns:
        Rearranged tensor in block-scaled swizzle format
    """
    assert scale_tensor.element_size() == 1, (
        "Expected element size to be 1 byte (8 bits)"
    )
    assert scale_tensor.is_contiguous(), "Input tensor must be contiguous"

    rows, cols = scale_tensor.shape

    # Calculate blocks needed
    n_row_blocks = triton.cdiv(rows, 128)
    n_col_blocks = triton.cdiv(cols, 4)
    padded_rows = n_row_blocks * 128
    padded_cols = n_col_blocks * 4

    out = scale_tensor.new_empty((padded_rows, padded_cols))

    # Input stride (for row-major format)
    input_row_stride = cols

    # We probably want handle multiple blocks per tile but
    # for now keep it simple
    BLOCK_ROWS, BLOCK_COLS = 128, 4

    # Output block stride for the rearranged format
    output_block_stride = BLOCK_ROWS * BLOCK_COLS * (padded_cols // BLOCK_COLS)

    grid = lambda META: (
        triton.cdiv(padded_rows, BLOCK_ROWS),
        triton.cdiv(padded_cols, BLOCK_COLS),
    )

    wrap_triton(triton_scale_swizzle)[grid](
        scale_tensor.view(torch.uint8),
        rows,
        cols,
        out.view(torch.uint8),
        input_row_stride,
        output_block_stride,
        BLOCK_ROWS=BLOCK_ROWS,
        BLOCK_COLS=BLOCK_COLS,
    )

    return out
```

## triton\_scale\_swizzle [¶](#vllm.model_executor.layers.quantization.qutlass_utils.triton_scale_swizzle "Permanent link")

```
triton_scale_swizzle(
    scale_ptr: Tensor,
    scale_rows: int,
    scale_cols: int,
    output_ptr: Tensor,
    input_row_stride: int,
    output_block_stride: int,
    BLOCK_ROWS: constexpr,
    BLOCK_COLS: constexpr,
)
```

Rearranges tensor data from row-major to block-scaled swizzle format.

Parameters:

Name Type Description Default `scale_ptr` `Tensor`

Pointer to the input scale tensor

*required* `scale_rows` `int`

Number of rows in the scale tensor

*required* `scale_cols` `int`

Number of columns in the scale tensor

*required* `output_ptr` `Tensor`

Pointer to the output tensor

*required* `input_row_stride` `int`

Stride between rows in the input tensor

*required* `output_block_stride` `int`

Stride between blocks in the output tensor

*required* `BLOCK_ROWS` `constexpr`

Number of rows in a tile (compile-time constant)

*required* `BLOCK_COLS` `constexpr`

Number of columns in a tile (compile-time constant)

*required*

Source code in `vllm/model_executor/layers/quantization/qutlass_utils.py`

```
@triton.jit
deftriton_scale_swizzle(
    scale_ptr: torch.Tensor,
    scale_rows: int,
    scale_cols: int,
    output_ptr: torch.Tensor,
    input_row_stride: int,
    output_block_stride: int,
    BLOCK_ROWS: tl.constexpr,
    BLOCK_COLS: tl.constexpr,
):
"""
    Rearranges tensor data from row-major to block-scaled swizzle format.

    Args:
        scale_ptr: Pointer to the input scale tensor
        scale_rows: Number of rows in the scale tensor
        scale_cols: Number of columns in the scale tensor
        output_ptr: Pointer to the output tensor
        input_row_stride: Stride between rows in the input tensor
        output_block_stride: Stride between blocks in the output tensor
        BLOCK_ROWS: Number of rows in a tile (compile-time constant)
        BLOCK_COLS: Number of columns in a tile (compile-time constant)
    """
    pid_row = tl.program_id(0)
    pid_col = tl.program_id(1)

    rows = tl.arange(0, BLOCK_ROWS)[:, None]
    cols = tl.arange(0, BLOCK_COLS)[None, :]

    # Calculate starting row and column for this tile
    start_row = pid_row * BLOCK_ROWS
    start_col = pid_col * BLOCK_COLS
    global_rows = start_row + rows
    global_cols = start_col + cols

    mask = (global_rows < scale_rows) & (global_cols < scale_cols)

    input_scales = tl.load(
        scale_ptr + global_rows * input_row_stride + global_cols,
        mask=mask,
        other=0.0,
    )

    r_div_32 = rows // 32
    r_mod_32 = rows % 32

    # 2) Rearrange to (32, 4, 4) then to final (32, 16) coordinates
    dest_indices = r_mod_32 * 16 + r_div_32 * 4 + cols

    # Flatten
    dest_indices_flat = tl.reshape(dest_indices, (BLOCK_ROWS * BLOCK_COLS))
    scales_flat = tl.reshape(input_scales, (BLOCK_ROWS * BLOCK_COLS))

    # Calculate block offset using provided output block stride
    LOCAL_NUMEL = BLOCK_ROWS * BLOCK_COLS
    block_offset = pid_col * LOCAL_NUMEL + (pid_row * output_block_stride)

    tl.store(
        output_ptr + block_offset + dest_indices_flat,
        scales_flat,
    )
```