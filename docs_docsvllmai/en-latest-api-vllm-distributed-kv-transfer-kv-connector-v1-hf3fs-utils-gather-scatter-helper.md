---
title: gather_scatter_helper - vLLM
url: https://docs.vllm.ai/en/latest/api/vllm/distributed/kv_transfer/kv_connector/v1/hf3fs/utils/gather_scatter_helper/
source: sitemap
fetched_at: 2026-05-07T21:18:20.789308147-03:00
rendered_js: false
word_count: 201
summary: This document describes utility functions and a memory allocator designed to facilitate gathering and scattering KV cache data between tensors and storage in distributed inference environments.
tags:
    - kv-cache
    - memory-management
    - tensor-processing
    - distributed-computing
    - vllm
    - cuda-kernels
category: reference
---

## CopyBufferAllocator [¶](#vllm.distributed.kv_transfer.kv_connector.v1.hf3fs.utils.gather_scatter_helper.CopyBufferAllocator "Permanent link")

Memory pool for tensor buffers to avoid frequent allocation/deallocation.

Source code in `vllm/distributed/kv_transfer/kv_connector/v1/hf3fs/utils/gather_scatter_helper.py`

```
classCopyBufferAllocator:
"""Memory pool for tensor buffers to avoid frequent allocation/deallocation."""

    def__init__(
        self, device: torch.device, dtype: torch.dtype, shape: list, max_count: int
    ):
        self._shape = shape
        self._max_count = max_count
        self._device = device
        self._free_buffers = [
            torch.empty(shape, dtype=dtype, device=device) for _ in range(max_count)
        ]
        self._inuse_count = 0

    defalloc_buffer(self, count: int) -> list[torch.Tensor] | None:
"""Allocate buffers from the pool."""
        if count == 0:
            return []

        if self._inuse_count + count <= self._max_count:
            self._inuse_count += count
            result = self._free_buffers[-count:]
            del self._free_buffers[-count:]
            return result
        return None

    deffree_buffer(self, buffers: list[torch.Tensor]) -> None:
"""Return buffers to the pool."""
        if not buffers:
            return

        if self._inuse_count >= len(buffers):
            self._inuse_count -= len(buffers)
            self._free_buffers.extend(buffers)
        else:
            raise RuntimeError("Attempted to free more buffers than allocated")
```

### alloc\_buffer [¶](#vllm.distributed.kv_transfer.kv_connector.v1.hf3fs.utils.gather_scatter_helper.CopyBufferAllocator.alloc_buffer "Permanent link")

Allocate buffers from the pool.

Source code in `vllm/distributed/kv_transfer/kv_connector/v1/hf3fs/utils/gather_scatter_helper.py`

```
defalloc_buffer(self, count: int) -> list[torch.Tensor] | None:
"""Allocate buffers from the pool."""
    if count == 0:
        return []

    if self._inuse_count + count <= self._max_count:
        self._inuse_count += count
        result = self._free_buffers[-count:]
        del self._free_buffers[-count:]
        return result
    return None
```

### free\_buffer [¶](#vllm.distributed.kv_transfer.kv_connector.v1.hf3fs.utils.gather_scatter_helper.CopyBufferAllocator.free_buffer "Permanent link")

Return buffers to the pool.

Source code in `vllm/distributed/kv_transfer/kv_connector/v1/hf3fs/utils/gather_scatter_helper.py`

```
deffree_buffer(self, buffers: list[torch.Tensor]) -> None:
"""Return buffers to the pool."""
    if not buffers:
        return

    if self._inuse_count >= len(buffers):
        self._inuse_count -= len(buffers)
        self._free_buffers.extend(buffers)
    else:
        raise RuntimeError("Attempted to free more buffers than allocated")
```

## gather\_kv\_caches [¶](#vllm.distributed.kv_transfer.kv_connector.v1.hf3fs.utils.gather_scatter_helper.gather_kv_caches "Permanent link")

```
gather_kv_caches(
    kv_caches_ptrs: Tensor,
    total_token_in_kvcache: int,
    dst_tensor: Tensor,
    token_indices: list[int],
    is_mla: bool = False,
) -> None
```

Gather KV cache data from KV cache storage to destination tensor.

Parameters:

Name Type Description Default `kv_caches_ptrs` `Tensor`

Tensor of KV cache pointers (one per layer)

*required* `total_token_in_kvcache` `int`

Total number of tokens in KV cache

*required* `dst_tensor` `Tensor`

Destination tensor to store gathered data - MHA format: \[num\_layers, 2, num\_tokens\_in\_block, hidden\_size] - MLA format: \[num\_layers, num\_tokens\_in\_block, hidden\_size]

*required* `token_indices` `list[int]`

List of token positions to gather

*required* `is_mla` `bool`

Whether using MLA model format

`False`

Source code in `vllm/distributed/kv_transfer/kv_connector/v1/hf3fs/utils/gather_scatter_helper.py`

```
defgather_kv_caches(
    kv_caches_ptrs: torch.Tensor,
    total_token_in_kvcache: int,
    dst_tensor: torch.Tensor,
    token_indices: list[int],
    is_mla: bool = False,
) -> None:
"""Gather KV cache data from KV cache storage to destination tensor.

    Args:
        kv_caches_ptrs: Tensor of KV cache pointers (one per layer)
        total_token_in_kvcache: Total number of tokens in KV cache
        dst_tensor: Destination tensor to store gathered data
            - MHA format: [num_layers, 2, num_tokens_in_block, hidden_size]
            - MLA format: [num_layers, num_tokens_in_block, hidden_size]
        token_indices: List of token positions to gather
        is_mla: Whether using MLA model format
    """
    num_layers = kv_caches_ptrs.shape[0]
    num_tokens_in_block = len(token_indices)

    if is_mla:
        # MLA: dst_tensor is [num_layers, num_tokens_in_block, hidden_size]
        assert len(dst_tensor.shape) == 3, (
            f"MLA dst_tensor should be 3D, got {dst_tensor.shape}"
        )
        assert dst_tensor.shape[0] == num_layers, (
            f"Layer count mismatch: {dst_tensor.shape[0]} vs {num_layers}"
        )
        assert dst_tensor.shape[1] == num_tokens_in_block, (
            f"Token count mismatch: {dst_tensor.shape[1]} vs {num_tokens_in_block}"
        )
        hidden_size = dst_tensor.shape[2]
    else:
        # MHA: dst_tensor is [num_layers, 2, num_tokens_in_block, hidden_size]
        assert len(dst_tensor.shape) == 4, (
            f"MHA dst_tensor should be 4D, got {dst_tensor.shape}"
        )
        assert dst_tensor.shape[0] == num_layers, (
            f"Layer count mismatch: {dst_tensor.shape[0]} vs {num_layers}"
        )
        assert dst_tensor.shape[1] == 2, (
            f"MHA should have 2 (K,V) components, got {dst_tensor.shape[1]}"
        )
        assert dst_tensor.shape[2] == num_tokens_in_block, (
            f"Token count mismatch: {dst_tensor.shape[2]} vs {num_tokens_in_block}"
        )
        hidden_size = dst_tensor.shape[3]

    device = dst_tensor.device
    token_indices_tensor = torch.tensor(
        token_indices, dtype=torch.int32, device="cpu"
    ).to(device, non_blocking=True)

    grid = (num_layers, num_tokens_in_block)
    BLOCK_SIZE = 128

    kv_cache_gather_kernel[grid](
        kv_caches_ptrs,
        dst_tensor,
        token_indices_tensor,
        num_tokens_in_block,
        hidden_size,
        total_token_in_kvcache,
        num_layers,
        is_mla,
        BLOCK_SIZE=BLOCK_SIZE,
    )
```

## scatter\_kv\_caches [¶](#vllm.distributed.kv_transfer.kv_connector.v1.hf3fs.utils.gather_scatter_helper.scatter_kv_caches "Permanent link")

```
scatter_kv_caches(
    kv_caches_ptrs: Tensor,
    total_token_in_kvcache: int,
    src_tensor: Tensor,
    token_indices: list[int],
    is_mla: bool = False,
) -> None
```

Scatter KV cache data from source tensor to KV cache storage.

Parameters:

Name Type Description Default `kv_caches_ptrs` `Tensor`

Tensor of KV cache pointers (one per layer)

*required* `total_token_in_kvcache` `int`

Total number of tokens in KV cache

*required* `src_tensor` `Tensor`

Source tensor containing data to scatter - MHA format: \[num\_layers, 2, num\_tokens\_in\_block, hidden\_size] - MLA format: \[num\_layers, num\_tokens\_in\_block, hidden\_size]

*required* `token_indices` `list[int]`

List of token positions to update

*required* `is_mla` `bool`

Whether using MLA model format

`False`

Source code in `vllm/distributed/kv_transfer/kv_connector/v1/hf3fs/utils/gather_scatter_helper.py`

```
defscatter_kv_caches(
    kv_caches_ptrs: torch.Tensor,
    total_token_in_kvcache: int,
    src_tensor: torch.Tensor,
    token_indices: list[int],
    is_mla: bool = False,
) -> None:
"""Scatter KV cache data from source tensor to KV cache storage.

    Args:
        kv_caches_ptrs: Tensor of KV cache pointers (one per layer)
        total_token_in_kvcache: Total number of tokens in KV cache
        src_tensor: Source tensor containing data to scatter
            - MHA format: [num_layers, 2, num_tokens_in_block, hidden_size]
            - MLA format: [num_layers, num_tokens_in_block, hidden_size]
        token_indices: List of token positions to update
        is_mla: Whether using MLA model format
    """
    num_layers = len(kv_caches_ptrs)
    num_tokens_in_block = len(token_indices)

    if is_mla:
        # MLA: src_tensor is [num_layers, num_tokens_in_block, hidden_size]
        assert len(src_tensor.shape) == 3, (
            f"MLA src_tensor should be 3D, got {src_tensor.shape}"
        )
        hidden_size = src_tensor.shape[2]
    else:
        # MHA: src_tensor is [num_layers, 2, num_tokens_in_block, hidden_size]
        assert len(src_tensor.shape) == 4, (
            f"MHA src_tensor should be 4D, got {src_tensor.shape}"
        )
        hidden_size = src_tensor.shape[3]

    device = src_tensor.device
    token_indices_tensor = torch.tensor(
        token_indices, dtype=torch.int32, device="cpu"
    ).to(device, non_blocking=True)

    grid = (num_layers, num_tokens_in_block)
    BLOCK_SIZE = 128

    kv_cache_scatter_kernel[grid](
        kv_caches_ptrs,
        src_tensor,
        token_indices_tensor,
        num_tokens_in_block,
        hidden_size,
        total_token_in_kvcache,
        num_layers,
        is_mla,
        BLOCK_SIZE=BLOCK_SIZE,
    )
```