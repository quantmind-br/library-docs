---
title: kernel_warmup - vLLM
url: https://docs.vllm.ai/en/latest/api/vllm/model_executor/warmup/kernel_warmup/
source: sitemap
fetched_at: 2026-05-07T21:34:00.195828195-03:00
rendered_js: false
word_count: 79
summary: This document describes the kernel warmup and FlashInfer autotuning processes used to optimize model execution performance by pre-compiling kernels and benchmarking operational implementations.
tags:
    - vllm
    - kernel-warmup
    - flashinfer
    - autotuning
    - performance-optimization
    - gpu-execution
category: reference
---

## vllm.model\_executor.warmup.kernel\_warmup [¶](#vllm.model_executor.warmup.kernel_warmup "Permanent link")

Warmup kernels used during model execution. This is useful specifically for JIT'ed kernels as we don't want JIT'ing to happen during model execution.

## flashinfer\_autotune [¶](#vllm.model_executor.warmup.kernel_warmup.flashinfer_autotune "Permanent link")

Autotune FlashInfer operations. FlashInfer have many implementations for the same operation, autotuning runs benchmarks for each implementation and stores the results. The results are cached transparently and future calls to FlashInfer will use the best implementation. Without autotuning, FlashInfer will rely on heuristics, which may be significantly slower.

Source code in `vllm/model_executor/warmup/kernel_warmup.py`

```
defflashinfer_autotune(runner: "GPUModelRunner") -> None:
"""
    Autotune FlashInfer operations.
    FlashInfer have many implementations for the same operation,
    autotuning runs benchmarks for each implementation and stores
    the results. The results are cached transparently and
    future calls to FlashInfer will use the best implementation.
    Without autotuning, FlashInfer will rely on heuristics, which may
    be significantly slower.
    """
    importvllm.utils.flashinferasfi_utils

    with torch.inference_mode(), fi_utils.autotune():
        # Certain FlashInfer kernels (e.g. nvfp4 routed moe) are
        # incompatible with autotuning. This state is used to skip
        # those kernels during the autotuning process.
        fi_utils._is_fi_autotuning = True

        # We skip EPLB here since we don't want to record dummy metrics
        # When autotuning with number of tokens m, flashinfer will autotune
        # operations for all number of tokens up to m.
        # So we only need to run with the max number of tokens.
        runner._dummy_run(
            runner.scheduler_config.max_num_batched_tokens,
            skip_eplb=True,
            is_profile=True,
        )

        fi_utils._is_fi_autotuning = False
```