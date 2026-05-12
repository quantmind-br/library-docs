---
title: step3p5 - vLLM
url: https://docs.vllm.ai/en/latest/api/vllm/model_executor/models/step3p5/
source: sitemap
fetched_at: 2026-05-07T21:33:25.896124056-03:00
rendered_js: false
word_count: 18
summary: This document describes the implementation of the Step3p5 model architecture within vLLM, specifically highlighting the FP32ReplicatedLinear module designed for high-precision inference.
tags:
    - vllm
    - model-architecture
    - inference
    - fp32-precision
    - neural-network-layers
category: reference
---

## vllm.model\_executor.models.step3p5 [¶](#vllm.model_executor.models.step3p5 "Permanent link")

Inference-only Jurassic model.

## FP32ReplicatedLinear [¶](#vllm.model_executor.models.step3p5.FP32ReplicatedLinear "Permanent link")

Bases: `ReplicatedLinear`

Use FP32 for higher precision.

Source code in `vllm/model_executor/models/step3p5.py`

```
classFP32ReplicatedLinear(ReplicatedLinear):
"""
    Use FP32 for higher precision.
    """

    defforward(
        self,
        x: torch.Tensor,
    ) -> torch.Tensor | tuple[torch.Tensor, Parameter | None]:
        assert self.params_dtype == torch.float32
        return super().forward(x.to(torch.float32))
```