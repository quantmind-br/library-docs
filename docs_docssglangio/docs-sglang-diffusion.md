---
title: SGLang Diffusion - SGLang Documentation
url: https://docs.sglang.io/docs/sglang-diffusion
source: sitemap
fetched_at: 2026-05-11T05:51:14.701494462-03:00
rendered_js: false
word_count: 240
summary: This document introduces SGLang Diffusion, a high-performance framework designed for efficient image and video model inference through optimized kernels and versatile deployment interfaces.
tags:
    - diffusion-models
    - inference-optimization
    - image-generation
    - video-generation
    - gpu-acceleration
    - openai-api
category: guide
---

> ## Documentation Index
> 
> Fetch the complete documentation index at: [https://docs.sglang.io/llms.txt](https://docs.sglang.io/llms.txt)
> 
> Use this file to discover all available pages before exploring further.

SGLang Diffusion is a high-performance inference framework for image and video generation. It provides native SGLang pipelines, diffusers backend support, an OpenAI-compatible server, and an optimized kernel stack built on both precompiled `sgl-kernel` operators and JIT kernels for key inference paths.

## Key Features

- Broad model support across Wan, Hunyuan, Qwen-Image, FLUX, Z-Image, GLM-Image, and more
- Fast inference with `sgl-kernel`, JIT kernels, scheduler improvements, and caching acceleration
- Multiple interfaces: `sglang generate`, `sglang serve`, and an OpenAI-compatible API
- Multi-platform support for NVIDIA, AMD, Intel XPU, Ascend, Apple Silicon, and Moore Threads

## Quick Start

```
uv pip install "sglang[diffusion]" --prerelease=allow

sglang generate --model-path Qwen/Qwen-Image \
  --prompt "A beautiful sunset over the mountains" \
  --save-output

sglang serve --model-path Qwen/Qwen-Image --port 30010
```

## Start Here

- [Installation](https://docs.sglang.io/docs/sglang-diffusion/installation): install SGLang Diffusion and platform dependencies
- [Compatibility Matrix](https://docs.sglang.io/docs/sglang-diffusion/compatibility_matrix): check model, optimization, and component override support
- [CLI](https://docs.sglang.io/docs/sglang-diffusion/api/cli): run one-off generation jobs or launch a persistent server
- [OpenAI-Compatible API](https://docs.sglang.io/docs/sglang-diffusion/api/openai_api): send image and video requests to the HTTP server
- [Attention Backends](https://docs.sglang.io/docs/sglang-diffusion/attention_backends): choose the best backend for your model and hardware
- [Inference Batching](https://docs.sglang.io/docs/sglang-diffusion/dynamic_batching): batch compatible native diffusion requests during serving
- [Caching Acceleration](https://docs.sglang.io/docs/sglang-diffusion/caching-acceleration): use Cache-DiT or TeaCache to reduce denoising cost
- [Quantization](https://docs.sglang.io/docs/sglang-diffusion/quantization): load quantized transformer checkpoints
- [Contributing](https://docs.sglang.io/docs/sglang-diffusion/contributing): contribution workflow, adding new models, and CI perf baselines

## Additional Documentation

- [Post-Processing](https://docs.sglang.io/docs/sglang-diffusion/api/post_processing): frame interpolation and upscaling
- [Performance Overview](https://docs.sglang.io/docs/sglang-diffusion/performance-optimization): overview of attention, caching, and profiling
- [Environment Variables](https://docs.sglang.io/docs/sglang-diffusion/environment_variables): platform, caching, storage, and debugging configuration
- [Support New Models](https://docs.sglang.io/docs/sglang-diffusion/support_new_models): implementation guide for new diffusion pipelines
- [CI Performance](https://docs.sglang.io/docs/sglang-diffusion/ci_perf): performance baseline generation

## References

- [SGLang GitHub](https://github.com/sgl-project/sglang)
- [Cache-DiT](https://github.com/vipshop/cache-dit)
- [FastVideo](https://github.com/hao-ai-lab/FastVideo)
- [xDiT](https://github.com/xdit-project/xDiT)
- [Diffusers](https://github.com/huggingface/diffusers)