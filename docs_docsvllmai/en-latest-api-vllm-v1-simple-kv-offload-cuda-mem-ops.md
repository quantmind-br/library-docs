---
title: cuda_mem_ops - vLLM
url: https://docs.vllm.ai/en/latest/api/vllm/v1/simple_kv_offload/cuda_mem_ops/
source: sitemap
fetched_at: 2026-05-07T21:41:40.099603446-03:00
rendered_js: false
word_count: 150
summary: This document provides low-level memory operations for CUDA and ROCm platforms, specifically implementing batch memory transfers and efficient tensor pinning to bypass PyTorch allocator limitations.
tags:
    - cuda
    - rocm
    - memory-management
    - dma-transfers
    - gpu-programming
    - batch-processing
    - tensor-pinning
category: api
---

Low-level CUDA/HIP memory helpers: pinning and batch DMA transfers.

## \_resolve\_batch\_memcpy [¶](#vllm.v1.simple_kv_offload.cuda_mem_ops._resolve_batch_memcpy "Permanent link")

Resolve the platform batch-memcpy entry point (one-time).

- CUDA: `cuMemcpyBatchAsync` via `cuGetProcAddress` (uses srcAccessOrder=STREAM via one attributes entry).
- ROCm: `hipMemcpyBatchAsync` from libamdhip64 (ROCm 7.1+). ROCm 7.2.1 or 7.2.2 rejects any call with `numAttrs > 0` (see ROCm/clr @ rocm-7.2.1 hipamd/src/hip\_memory.cpp:2819-2822), so we call with `numAttrs=0`.

Raises `RuntimeError` if the symbol is unavailable (older CUDA driver, ROCm &lt; 7.1, unusual install). The connector requires the batch API.

Source code in `vllm/v1/simple_kv_offload/cuda_mem_ops.py`

```
def_resolve_batch_memcpy():
"""Resolve the platform batch-memcpy entry point (one-time).

    * CUDA: ``cuMemcpyBatchAsync`` via ``cuGetProcAddress`` (uses
      srcAccessOrder=STREAM via one attributes entry).
    * ROCm: ``hipMemcpyBatchAsync`` from libamdhip64 (ROCm 7.1+). ROCm
      7.2.1 or 7.2.2 rejects any call with ``numAttrs > 0``
      (see ROCm/clr @ rocm-7.2.1 hipamd/src/hip_memory.cpp:2819-2822), so
      we call with ``numAttrs=0``.

    Raises ``RuntimeError`` if the symbol is unavailable (older CUDA
    driver, ROCm < 7.1, unusual install). The connector requires the
    batch API.
    """
    if current_platform.is_rocm():
        try:
            lib = ctypes.CDLL("libamdhip64.so", mode=ctypes.RTLD_GLOBAL)
            fn = lib.hipMemcpyBatchAsync
        except (OSError, AttributeError) as e:
            raise RuntimeError(
                "hipMemcpyBatchAsync is unavailable in this ROCm install; "
                "SimpleCPUOffloadConnector requires ROCm 7.1+."
            ) frome
        fn.restype = ctypes.c_uint
        fn.argtypes = [
            ctypes.c_void_p,  # dsts
            ctypes.c_void_p,  # srcs
            ctypes.c_void_p,  # sizes
            ctypes.c_size_t,  # count
            ctypes.c_void_p,  # attrs
            ctypes.c_void_p,  # attrIdxs
            ctypes.c_size_t,  # numAttrs
            ctypes.c_void_p,  # failIdx
            ctypes.c_void_p,  # stream
        ]
        return fn

    fromcuda.bindingsimport driver as drv

    err, ptr, _ = drv.cuGetProcAddress(b"cuMemcpyBatchAsync", 12080, 0)
    if err != drv.CUresult.CUDA_SUCCESS:
        raise RuntimeError(f"cuGetProcAddress(cuMemcpyBatchAsync) failed: {err}")
    return _BATCH_MEMCPY_FUNC_TYPE(ptr)
```

## copy\_blocks [¶](#vllm.v1.simple_kv_offload.cuda_mem_ops.copy_blocks "Permanent link")

```
copy_blocks(
    src_block_ids: list[int],
    dst_block_ids: list[int],
    params: BatchMemcpyParams,
) -> None
```

Copy blocks via cuMemcpyBatchAsync / hipMemcpyBatchAsync.

Source code in `vllm/v1/simple_kv_offload/cuda_mem_ops.py`

```
defcopy_blocks(
    src_block_ids: list[int],
    dst_block_ids: list[int],
    params: BatchMemcpyParams,
) -> None:
"""Copy blocks via cuMemcpyBatchAsync / hipMemcpyBatchAsync."""
    n = len(src_block_ids)
    if n == 0:
        return

    src_ids = np.array(src_block_ids, dtype=np.uint64)
    dst_ids = np.array(dst_block_ids, dtype=np.uint64)

    src_all = (
        params.src_bases[:, None] + src_ids[None, :] * params.bpb[:, None]
    ).ravel()
    dst_all = (
        params.dst_bases[:, None] + dst_ids[None, :] * params.bpb[:, None]
    ).ravel()
    sz_all = np.repeat(params.bpb, n)
    total = n * params.num_layers

    # ROCm 7.2.1/7.2.2 rejects any call with numAttrs>0 (hipMemcpyBatchAsync
    # hipamd/src/hip_memory.cpp:2819-2822); CUDA uses one attrs entry so
    # srcAccessOrder is honored. attrs / attrsIdxs are ignored when
    # numAttrs==0, so we pass the same values from both paths.
    num_attrs = 0 if current_platform.is_rocm() else 1
    err = _batch_memcpy_fn(
        dst_all.ctypes.data,
        src_all.ctypes.data,
        sz_all.ctypes.data,
        total,
        ctypes.addressof(params.attrs),
        ctypes.byref(params.attrs_idx),
        num_attrs,
        ctypes.byref(params.fail_idx),
        params.stream_handle,
    )
    if err != 0:
        raise RuntimeError(
            f"batch memcpy failed: err={err} failIdx={params.fail_idx.value}"
        )
```

## pin\_tensor [¶](#vllm.v1.simple_kv_offload.cuda_mem_ops.pin_tensor "Permanent link")

```
pin_tensor(tensor: Tensor) -> None
```

Pin a CPU tensor via cudaHostRegister.

This bypasses PyTorch's CUDACachingHostAllocator which rounds every `pin_memory=True` allocation up to the next power of 2 (e.g. 100 GB becomes 128 GB).

Source code in `vllm/v1/simple_kv_offload/cuda_mem_ops.py`

```
defpin_tensor(tensor: torch.Tensor) -> None:
"""Pin a CPU tensor via cudaHostRegister.

    This bypasses PyTorch's CUDACachingHostAllocator which rounds
    every ``pin_memory=True`` allocation up to the next power of 2
    (e.g. 100 GB becomes 128 GB).
    """
    err = torch.cuda.cudart().cudaHostRegister(tensor.data_ptr(), tensor.nbytes, 0)
    if err.value != 0:
        raise RuntimeError(f"cudaHostRegister failed: {err}")
```