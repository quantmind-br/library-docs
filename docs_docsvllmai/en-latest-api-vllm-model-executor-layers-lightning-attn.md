---
title: lightning_attn - vLLM
url: https://docs.vllm.ai/en/latest/api/vllm/model_executor/layers/lightning_attn/
source: sitemap
fetched_at: 2026-05-07T21:25:48.072644942-03:00
rendered_js: false
word_count: 207
summary: This document describes the implementation of lightning attention and linear decoding mechanisms, including Triton-based kernels designed for efficient KV cache management and attention computation.
tags:
    - triton-kernel
    - lightning-attention
    - kv-cache
    - linear-attention
    - gpu-optimization
    - vllm
category: api
---

## \_linear\_attn\_decode\_kernel [¶](#vllm.model_executor.layers.lightning_attn._linear_attn_decode_kernel "Permanent link")

```
_linear_attn_decode_kernel(
    q_ptr,
    k_ptr,
    v_ptr,
    kv_cache_ptr,
    slope_rate,
    slot_idx,
    output_ptr,
    D: constexpr,
    qkv_b_stride,
    qkv_h_stride,
    cache_b_stride,
    cache_h_stride,
    cache_d0_stride,
    cache_d1_stride,
    pad_slot_id: constexpr,
    BLOCK_SIZE: constexpr,
)
```

Kernel for linear attention decoding with KV cache.

This kernel computes attention for a single token using the KV cache.

Source code in `vllm/model_executor/layers/lightning_attn.py`

```
@triton.jit
def_linear_attn_decode_kernel(
    q_ptr,
    k_ptr,
    v_ptr,
    kv_cache_ptr,
    slope_rate,
    slot_idx,
    output_ptr,
    D: tl.constexpr,
    qkv_b_stride,
    qkv_h_stride,
    cache_b_stride,
    cache_h_stride,
    cache_d0_stride,
    cache_d1_stride,
    pad_slot_id: tl.constexpr,
    BLOCK_SIZE: tl.constexpr,
):
"""
    Kernel for linear attention decoding with KV cache.

    This kernel computes attention for a single token using the KV cache.
    """
    pid_b = tl.program_id(0)  # batch index
    pid_h = tl.program_id(1)  # head index
    pid_d = tl.program_id(2)  # dimension block index

    # Load slot index for the current batch
    slot_id = tl.load(slot_idx + pid_b).to(tl.int64)

    # Skip if slot_id is PAD_SLOT_ID (padding)
    if slot_id == pad_slot_id:
        return

    batch_id = pid_b
    head_id = pid_h

    # Load decay rate for the current head
    ratio = tl.load(slope_rate + pid_h)

    # Calculate offsets for dimensions
    qk_d_offsets = tl.arange(0, D)
    v_d_offsets = tl.arange(0, BLOCK_SIZE) + pid_d * BLOCK_SIZE
    cache_d_offsets = (
        qk_d_offsets[:, None] * cache_d0_stride + v_d_offsets[None, :] * cache_d1_stride
    )

    # Calculate offsets for the current batch and head
    q_offset = batch_id * qkv_b_stride + head_id * qkv_h_stride
    k_offset = batch_id * qkv_b_stride + head_id * qkv_h_stride
    v_offset = batch_id * qkv_b_stride + head_id * qkv_h_stride

    cache_offset = slot_id * cache_b_stride + head_id * cache_h_stride

    # Create masks for loading tensors
    qk_mask = qk_d_offsets < D
    v_mask = v_d_offsets < D

    # Load query, key, and value tensors
    q = tl.load(q_ptr + q_offset + qk_d_offsets, mask=qk_mask, other=0.0)
    k = tl.load(k_ptr + k_offset + qk_d_offsets, mask=qk_mask, other=0.0)
    v = tl.load(v_ptr + v_offset + v_d_offsets, mask=v_mask, other=0.0)

    # Compute key-value outer product
    kv_outer = k[:, None] * v[None, :]
    kv_mask = qk_mask[:, None] & v_mask[None, :]

    # Apply decay to previous KV cache
    ratio = tl.exp(-ratio)
    kv_ptr = kv_cache_ptr + cache_offset + cache_d_offsets
    kv_cache_old = tl.load(kv_ptr, mask=kv_mask, other=0.0)
    kv_outer = kv_outer + ratio * kv_cache_old

    # Compute attention output
    output = q[:, None].to(tl.float32) * kv_outer
    output = tl.sum(output, axis=0)

    # Update KV cache and store output
    tl.store(kv_ptr, kv_outer, mask=kv_mask)
    tl.store(output_ptr + q_offset + v_d_offsets, output, mask=v_mask)
```

## lightning\_attention [¶](#vllm.model_executor.layers.lightning_attn.lightning_attention "Permanent link")

Apply lightning attention algorithm to compute attention efficiently.

Parameters:

Name Type Description Default `q` `Tensor`

Query tensor of shape \[batch, heads, seq\_len, dim]

*required* `k` `Tensor`

Key tensor of shape \[batch, heads, seq\_len, dim]

*required* `v` `Tensor`

Value tensor of shape \[batch, heads, seq\_len, dim\_v]

*required* `ed` `Tensor`

Decay rate tensor of shape \[heads]

*required* `block_size` `int`

Size of blocks for block-sparse attention

`256` `kv_history` `Tensor | None`

Optional key-value history from previous computations

`None`

Returns:

Name Type Description `output` `Tensor`

Attention output

`kv` `Tensor`

Updated key-value history

Source code in `vllm/model_executor/layers/lightning_attn.py`

```
deflightning_attention(
    q: torch.Tensor,
    k: torch.Tensor,
    v: torch.Tensor,
    ed: torch.Tensor,
    block_size: int = 256,
    kv_history: torch.Tensor | None = None,
) -> tuple[torch.Tensor, torch.Tensor]:
"""
    Apply lightning attention algorithm
    to compute attention efficiently.

    Args:
        q: Query tensor of shape [batch, heads, seq_len, dim]
        k: Key tensor of shape [batch, heads, seq_len, dim]
        v: Value tensor of shape [batch, heads, seq_len, dim_v]
        ed: Decay rate tensor of shape [heads]
        block_size: Size of blocks for block-sparse attention
        kv_history: Optional key-value history from previous computations

    Returns:
        output: Attention output
        kv: Updated key-value history
    """
    d = q.shape[-1]
    e = v.shape[-1]

    if ed.dim() == 1:
        ed = ed.view(1, -1, 1, 1)

    # Split the computation into chunks for better parallelism
    m = 128 if d >= 128 else 64
    assert d % m == 0, f"Dimension d ({d}) must be divisible by m ({m})"
    arr = [m * i for i in range(d // m + 1)]
    if arr[-1] != d:
        arr.append(d)
    n = len(arr)
    output = 0

    # Initialize or clone key-value history
    if kv_history is None:
        kv_history = torch.zeros(
            (q.shape[0], q.shape[1], d, e), dtype=torch.float32, device=q.device
        )
    else:
        kv_history = kv_history.clone().contiguous()

    # Process each chunk and accumulate results
    for i in range(n - 1):
        s = arr[i]
        e = arr[i + 1]
        q1 = q[..., s:e]
        k1 = k[..., s:e]
        o, kv = lightning_attention_(q1, k1, v, ed, kv_history)
        output = output + o
    return output, kv
```

## linear\_decode\_forward\_triton [¶](#vllm.model_executor.layers.lightning_attn.linear_decode_forward_triton "Permanent link")

Perform linear attention decoding using Triton kernels.

Parameters:

Name Type Description Default `q` `Tensor`

Query tensor of shape \[B, H, 1, D]

*required* `k` `Tensor`

Key tensor of shape \[B, H, 1, D]

*required* `v` `Tensor`

Value tensor of shape \[B, H, 1, D]

*required* `kv_caches` `Tensor`

Key-value cache tensor

*required* `slope_rate` `Tensor`

Decay rate tensor

*required* `slot_idx` `Tensor`

Slot indices for batches

*required* `BLOCK_SIZE` `int`

Size of blocks for processing

`32`

Returns:

Name Type Description `output` `Tensor`

Attention output tensor

Source code in `vllm/model_executor/layers/lightning_attn.py`

```
deflinear_decode_forward_triton(
    q: torch.Tensor,
    k: torch.Tensor,
    v: torch.Tensor,
    kv_caches: torch.Tensor,
    slope_rate: torch.Tensor,
    slot_idx: torch.Tensor,
    BLOCK_SIZE: int = 32,
) -> torch.Tensor:
"""
    Perform linear attention decoding using Triton kernels.

    Args:
        q: Query tensor of shape [B, H, 1, D]
        k: Key tensor of shape [B, H, 1, D]
        v: Value tensor of shape [B, H, 1, D]
        kv_caches: Key-value cache tensor
        slope_rate: Decay rate tensor
        slot_idx: Slot indices for batches
        BLOCK_SIZE: Size of blocks for processing

    Returns:
        output: Attention output tensor
    """
    B, H, _, D = q.shape
    assert k.shape == (B, H, 1, D)
    assert v.shape == (B, H, 1, D)

    # Initialize output tensor
    output = torch.empty_like(q)

    # Set grid dimensions for the kernel
    grid = (B, H, D // BLOCK_SIZE)

    # Calculate strides for tensors
    qkv_b_stride = q.stride(0)
    qkv_h_stride = q.stride(1)

    cache_b_stride = kv_caches.stride(0)
    cache_h_stride = kv_caches.stride(1)
    cache_d0_stride = kv_caches.stride(2)
    cache_d1_stride = kv_caches.stride(3)

    # Launch the kernel
    _linear_attn_decode_kernel[grid](
        q,
        k,
        v,
        kv_caches,
        slope_rate,
        slot_idx,
        output,
        D,
        qkv_b_stride,
        qkv_h_stride,
        cache_b_stride,
        cache_h_stride,
        cache_d0_stride,
        cache_d1_stride,
        pad_slot_id=PAD_SLOT_ID,
        BLOCK_SIZE=BLOCK_SIZE,
    )

    # Reshape output and return
    output = rearrange(output, "b h n d -> b n (h d)")
    return output.squeeze(1).contiguous()
```