---
title: schema - vLLM
url: https://docs.vllm.ai/en/latest/api/vllm/model_executor/layers/quantization/schema/
source: sitemap
fetched_at: 2026-05-07T21:27:42.796187688-03:00
rendered_js: false
word_count: 85
summary: This document defines the Pydantic schemas used to structure quantization parameters and metadata for model augmentation.
tags:
    - pydantic-schemas
    - model-quantization
    - kv-cache
    - data-serialization
    - machine-learning-infrastructure
category: reference
---

This file contains the Pydantic schemas for various quantization-related parameters. When a relevant quantization technique is specified, these parameters are loaded in the form of a JSON alongside the model weights and augment the model with additional information needed for use of that technique. The format of this JSON should be specified by one or more schemas contained here.

For example, when the KV cache is quantized to FP8-E4M3 (currently only possible on ROCm), the model can be optionally augmented with KV cache scaling factors.