---
title: mem_utils - vLLM
url: https://docs.vllm.ai/en/latest/api/vllm/utils/mem_utils/
source: sitemap
fetched_at: 2026-05-07T21:38:44.370702828-03:00
rendered_js: false
word_count: 308
summary: This document describes a memory profiling context manager used to quantify GPU memory usage by classifying it into torch-managed, non-torch, and external instance memory during model execution.
tags:
    - memory-profiling
    - gpu-optimization
    - vllm
    - torch-memory
    - performance-monitoring
    - context-manager
category: reference
---

Memory profiling context manager.

baseline\_snapshot: the memory snapshot before the current vLLM instance. weights\_memory: memory used by PyTorch when loading the model weights. Note that, before loading the model weights, we also initialize the device and distributed environment, which may consume some memory. This part is not included in the weights\_memory because PyTorch does not control it.

The memory in one GPU can be classified into 3 categories: 1. memory used by anything other than the current vLLM instance. 2. memory used by torch in the current vLLM instance. 3. memory used in the current vLLM instance, but not by torch.

A quantitive example:

Before creating the current vLLM instance

category 1: 1 GiB category 2: 0 GiB category 3: 0 GiB

After creating the current vLLM instance and loading the model, (i.e. before profiling): category 1: 1 GiB category 2: 2 GiB (model weights take 2 GiB) category 3: 0.5 GiB (memory used by NCCL)

During profiling (peak): category 1: 1 GiB category 2: 4 GiB (peak activation tensors take 2 GiB) category 3: 1 GiB (memory used by NCCL + buffers for some attention backends)

After profiling

category 1: 1 GiB category 2: 3 GiB (after garbage-collecting activation tensors) category 3: 1 GiB (memory used by NCCL + buffers for some attention backends)

In this case, non-kv cache takes 5 GiB in total, including: a. 2 GiB used by the model weights (category 2) b. 2 GiB reserved for the peak activation tensors (category 2) c. 1 GiB used by non-torch components (category 3)

The memory used for loading weights (a.) is directly given from the argument `weights_memory`.

The increase of `torch.accelerator.memory_stats()["allocated_bytes.all.peak"]` during profiling gives (b.).

The increase of `non_torch_memory` from creating the current vLLM instance until after profiling to get (c.).

Source code in `vllm/utils/mem_utils.py`

```
@contextlib.contextmanager
defmemory_profiling(
    baseline_snapshot: MemorySnapshot,
    weights_memory: int = 0,
) -> Generator[MemoryProfilingResult, None, None]:
"""
    Memory profiling context manager.

    baseline_snapshot: the memory snapshot before the current vLLM instance.
    weights_memory: memory used by PyTorch when loading the model weights.
        Note that, before loading the model weights, we also initialize the device
        and distributed environment, which may consume some memory. This part is not
        included in the weights_memory because PyTorch does not control it.

    The memory in one GPU can be classified into 3 categories:
    1. memory used by anything other than the current vLLM instance.
    2. memory used by torch in the current vLLM instance.
    3. memory used in the current vLLM instance, but not by torch.

    A quantitive example:

    Before creating the current vLLM instance:
        category 1: 1 GiB
        category 2: 0 GiB
        category 3: 0 GiB

    After creating the current vLLM instance and loading the model,
    (i.e. before profiling):
        category 1: 1 GiB
        category 2: 2 GiB (model weights take 2 GiB)
        category 3: 0.5 GiB (memory used by NCCL)

    During profiling (peak):
        category 1: 1 GiB
        category 2: 4 GiB (peak activation tensors take 2 GiB)
        category 3: 1 GiB (memory used by NCCL + buffers for some attention backends)

    After profiling:
        category 1: 1 GiB
        category 2: 3 GiB (after garbage-collecting activation tensors)
        category 3: 1 GiB (memory used by NCCL + buffers for some attention backends)

    In this case, non-kv cache takes 5 GiB in total, including:
    a. 2 GiB used by the model weights (category 2)
    b. 2 GiB reserved for the peak activation tensors (category 2)
    c. 1 GiB used by non-torch components (category 3)

    The memory used for loading weights (a.) is directly given from the
    argument `weights_memory`.

    The increase of `torch.accelerator.memory_stats()["allocated_bytes.all.peak"]`
    during profiling gives (b.).

    The increase of `non_torch_memory` from creating the current vLLM instance
    until after profiling to get (c.).
    """
    gc.collect()
    torch.accelerator.empty_cache()
    torch.accelerator.reset_peak_memory_stats(baseline_snapshot.device_)

    result = MemoryProfilingResult(
        before_create=baseline_snapshot,
        # the part of memory used for holding the model weights
        weights_memory=weights_memory,
    )

    result.before_profile.measure()

    yield result

    gc.collect()
    torch.accelerator.empty_cache()

    result.after_profile.measure()

    diff_profile = result.after_profile - result.before_profile
    diff_from_create = result.after_profile - result.before_create
    result.torch_peak_increase = diff_profile.torch_peak
    result.non_torch_increase = diff_from_create.non_torch_memory
    result.profile_time = diff_profile.timestamp

    non_torch_memory = result.non_torch_increase
    peak_activation_memory = result.torch_peak_increase
    result.non_kv_cache_memory = (
        non_torch_memory + peak_activation_memory + result.weights_memory
    )
```