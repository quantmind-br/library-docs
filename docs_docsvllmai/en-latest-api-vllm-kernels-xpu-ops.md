---
title: xpu_ops - vLLM
url: https://docs.vllm.ai/en/latest/api/vllm/kernels/xpu_ops/
source: sitemap
fetched_at: 2026-05-07T21:22:19.016389171-03:00
rendered_js: false
word_count: 15
summary: This document defines the XPU_KERNELS_SUPPORTED attribute, which identifies whether the vLLM XPU kernel extensions are currently installed and available for use.
tags:
    - xpu-kernels
    - vllm
    - module-attribute
    - hardware-acceleration
    - dependency-check
category: reference
---

## XPU\_KERNELS\_SUPPORTED `module-attribute` [¶](#vllm.kernels.xpu_ops.XPU_KERNELS_SUPPORTED "Permanent link")

```
XPU_KERNELS_SUPPORTED = is_xpu_kernels_found()
```

Kernels in this file are supported if vLLM XPU kernels are installed.