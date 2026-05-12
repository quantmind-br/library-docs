---
title: xpu_model_runner - vLLM
url: https://docs.vllm.ai/en/latest/api/vllm/v1/worker/xpu_model_runner/
source: sitemap
fetched_at: 2026-05-07T21:43:20.748113703-03:00
rendered_js: false
word_count: 28
summary: This document defines the classes responsible for executing machine learning models on XPU hardware within the vLLM architecture.
tags:
    - xpu
    - model-runner
    - vllm
    - deep-learning
    - device-abstraction
category: reference
---

## XPUModelRunner [¶](#vllm.v1.worker.xpu_model_runner.XPUModelRunner "Permanent link")

Bases: `GPUModelRunner`

A model runner for XPU devices.

Source code in `vllm/v1/worker/xpu_model_runner.py`

```
classXPUModelRunner(GPUModelRunner):
"""A model runner for XPU devices."""

    def__init__(
        self,
        vllm_config: VllmConfig,
        device: torch.device,
    ):
        with _torch_cuda_wrapper():
            super().__init__(vllm_config, device)
        # FIXME: To be verified.
        self.cascade_attn_enabled = False
```

## XPUModelRunnerV2 [¶](#vllm.v1.worker.xpu_model_runner.XPUModelRunnerV2 "Permanent link")

Bases: `GPUModelRunner`

A model runner for XPU devices.

Source code in `vllm/v1/worker/xpu_model_runner.py`

```
classXPUModelRunnerV2(GPUModelRunnerV2):
"""A model runner for XPU devices."""

    def__init__(
        self,
        vllm_config: VllmConfig,
        device: torch.device,
    ):
        with _torch_cuda_wrapper():
            super().__init__(vllm_config, device)
```