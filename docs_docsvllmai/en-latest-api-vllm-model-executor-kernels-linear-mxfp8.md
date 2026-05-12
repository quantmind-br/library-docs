---
title: mxfp8 - vLLM
url: https://docs.vllm.ai/en/latest/api/vllm/model_executor/kernels/linear/mxfp8/
source: sitemap
fetched_at: 2026-05-07T21:23:30.245938034-03:00
rendered_js: false
word_count: 28
summary: This document defines the configuration structure for an MXFP8 linear layer, specifying the use of FP8-E4M3 weights and uint8 per-block scales.
tags:
    - mxfp8
    - linear-layer
    - fp8
    - neural-network-configuration
    - tensor-kernel
category: configuration
---

Configuration for an MXFP8 linear layer.

All MXFP8 layers share the same structure: FP8-E4M3 weights with uint8 (E8M0) per-block scales at block size 32.

Source code in `vllm/model_executor/kernels/linear/mxfp8/Mxfp8LinearKernel.py`

```
@dataclass
classMxfp8LinearLayerConfig:
"""Configuration for an MXFP8 linear layer.

    All MXFP8 layers share the same structure: FP8-E4M3 weights with
    uint8 (E8M0) per-block scales at block size 32.
    """

    pass
```