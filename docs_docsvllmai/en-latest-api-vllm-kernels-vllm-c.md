---
title: vllm_c - vLLM
url: https://docs.vllm.ai/en/latest/api/vllm/kernels/vllm_c/
source: sitemap
fetched_at: 2026-05-07T21:22:18.974519745-03:00
rendered_js: false
word_count: 42
summary: This document defines module attributes and constraints for vLLM kernel compatibility, specifically regarding platform support and required input parameters for RMS normalization operations.
tags:
    - vllm
    - cuda
    - kernel-optimization
    - rms-norm
    - compute-kernels
    - python-api
category: reference
---

## CUDA\_ALIKE `module-attribute` [¶](#vllm.kernels.vllm_c.CUDA_ALIKE "Permanent link")

```
CUDA_ALIKE = is_cuda_alike()
```

Most kernels in this file are supported on all CUDA-alike platforms.

## rms\_add\_no\_var\_size `module-attribute` [¶](#vllm.kernels.vllm_c.rms_add_no_var_size "Permanent link")

```
rms_add_no_var_size = (
    lambda x, x_residual, weight, epsilon, variance_size=None: (
        variance_size is None
        and (weight is None or dtype == dtype)
    )
)
```

vLLM Kernel does not support variance\_size parameter and requires matching input/weight dtype.

## rms\_no\_var\_size `module-attribute` [¶](#vllm.kernels.vllm_c.rms_no_var_size "Permanent link")

```
rms_no_var_size = (
    lambda x, weight, epsilon, variance_size=None: (
        variance_size is None
        and (weight is None or dtype == dtype)
    )
)
```

vLLM kernel requires no variance\_size override and matching input/weight dtype.