---
title: aiter_ops - vLLM
url: https://docs.vllm.ai/en/latest/api/vllm/kernels/aiter_ops/
source: sitemap
fetched_at: 2026-05-07T21:22:10.867137567-03:00
rendered_js: false
word_count: 104
summary: This document defines module attributes and configuration constraints for integrating AITER custom operators within the vLLM kernel framework.
tags:
    - aiter
    - custom-ops
    - vllm-kernels
    - torch-compile
    - rms-norm
category: reference
---

## AITER\_SUPPORTED `module-attribute` [¶](#vllm.kernels.aiter_ops.AITER_SUPPORTED "Permanent link")

```
AITER_SUPPORTED = is_aiter_found()
```

Most kernels in this file are supported if AITER is installed.

## aiter\_lib `module-attribute` [¶](#vllm.kernels.aiter_ops.aiter_lib "Permanent link")

```
aiter_lib = Library('vllm_aiter', 'FRAGMENT')
```

This library holds torch custom ops for wrapped AITER ops. Many AITER ops want to remain invisible to torch.compile even after lowering. They are thus wrapped into torch custom ops inside the IR op implementations.

## direct\_register\_aiter\_op `module-attribute` [¶](#vllm.kernels.aiter_ops.direct_register_aiter_op "Permanent link")

Syntactic sugar for registering AITER custom ops.

## rms\_add\_no\_var\_16bit\_only `module-attribute` [¶](#vllm.kernels.aiter_ops.rms_add_no_var_16bit_only "Permanent link")

```
rms_add_no_var_16bit_only = (
    lambda x, x_residual, weight, epsilon, variance_size=None: (
        variance_size is None
        and dtype in (float16, bfloat16)
        and (weight is None or dtype == dtype)
    )
)
```

AITER fused\_add\_rms\_norm only supports 16-bit activations and no var\_size override. Requires weight dtype to match x dtype.

## rms\_no\_var\_16bit\_only `module-attribute` [¶](#vllm.kernels.aiter_ops.rms_no_var_16bit_only "Permanent link")

```
rms_no_var_16bit_only = (
    lambda x, weight, epsilon, variance_size=None: (
        variance_size is None
        and dtype in (float16, bfloat16)
        and (weight is None or dtype == dtype)
    )
)
```

AITER rms\_norm only supports float16 and bfloat16 acts, no var\_size override, and requires weight dtype to match x dtype.