---
title: TensorRT | Mistral Docs
url: https://docs.mistral.ai/models/deployment/local-deployment/trt
source: sitemap
fetched_at: 2026-04-26T04:09:21.105878665-03:00
rendered_js: false
word_count: 51
summary: This document provides guidance on building and deploying large language model engines using TensorRT-LLM and the Triton inference server.
tags:
    - tensorrt-llm
    - triton-inference-server
    - model-deployment
    - llm-optimization
    - inference-backend
category: guide
optimized: true
optimized_at: 2026-04-26T00:00:00Z
---

Follow the official TensorRT-LLM documentation to [build the engine](https://github.com/NVIDIA/TensorRT-LLM/tree/main#quick-start).

- For Mistral-7B, you can use the [LLaMA example](https://github.com/NVIDIA/TensorRT-LLM/tree/main/examples/llama#mistral-v01)
- For Mixtral-8X7B, official documentation coming soon...

## Deploying the Engine

Once the engine is built, it can be deployed using the Triton inference server and its TensorRTLLM backend.

Follow the [official documentation](https://github.com/triton-inference-server/tensorrtllm_backend#using-the-tensorrt-llm-backend).

## Quick Reference

| Model | Example |
|-------|---------|
| Mistral-7B | Use LLaMA example |
| Mixtral-8X7B | Coming soon |