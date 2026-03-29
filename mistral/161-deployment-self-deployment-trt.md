---
title: TensorRT | Mistral Docs
url: https://docs.mistral.ai/deployment/self-deployment/trt
source: crawler
fetched_at: 2026-01-29T07:34:16.262842344-03:00
rendered_js: false
word_count: 51
summary: Documentation on optimizing and deploying Mistral models using NVIDIA TensorRT-LLM for high-performance inference.
tags:
    - TensorRT
    - Mistral AI
    - LLM optimization
    - NVIDIA
    - Inference
category: guide
---

Follow the official TensorRT-LLM documentation to [build the engine](https://github.com/NVIDIA/TensorRT-LLM/tree/main#quick-start).

- For Mistral-7B, you can use the [LLaMA example](https://github.com/NVIDIA/TensorRT-LLM/tree/main/examples/llama#mistral-v01)
- For Mixtral-8X7B, official documentation coming soon...

Deploying the engine

## Deploying the engine

Once the engine is built, it can be deployed using the Triton inference server and its TensorRTLLM backend.

Follow the [official documentation](https://github.com/triton-inference-server/tensorrtllm_backend#using-the-tensorrt-llm-backend).