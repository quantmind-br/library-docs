---
title: Caching Acceleration - SGLang Documentation
url: https://docs.sglang.io/docs/sglang-diffusion/caching-acceleration
source: sitemap
fetched_at: 2026-05-11T05:51:27.894735854-03:00
rendered_js: false
word_count: 196
summary: This document outlines two caching optimization strategies, Cache-DiT and TeaCache, used to accelerate inference in Diffusion Transformer models by reducing redundant computation.
tags:
    - diffusion-models
    - caching-strategies
    - model-acceleration
    - inference-optimization
    - teacache
    - cache-dit
category: concept
---

> ## Documentation Index
> 
> Fetch the complete documentation index at: [https://docs.sglang.io/llms.txt](https://docs.sglang.io/llms.txt)
> 
> Use this file to discover all available pages before exploring further.

SGLang provides two complementary caching strategies for Diffusion Transformer (DiT) models. Both reduce denoising cost by skipping redundant computation, but they operate at different levels.

## Overview

SGLang supports two complementary caching approaches:

StrategyScopeMechanismBest ForCache-DiTBlock-levelSkip individual transformer blocks dynamicallyAdvanced, higher speedupTeaCacheTimestep-levelSkip entire denoising steps based on L1 similaritySimple, built-in

## Cache-DiT

[Cache-DiT](https://github.com/vipshop/cache-dit) provides block-level caching with advanced strategies like DBCache and TaylorSeer. It can achieve up to **1.69x speedup**. See [cache\_dit.md](https://docs.sglang.io/docs/sglang-diffusion/cache_dit) for detailed configuration.

### Quick Start

```
SGLANG_CACHE_DIT_ENABLED=true \
sglang generate --model-path Qwen/Qwen-Image \
    --prompt "A beautiful sunset over the mountains"
```

### Key Features

- **DBCache**: Dynamic block-level caching based on residual differences
- **TaylorSeer**: Taylor expansion-based calibration for optimized caching
- **SCM**: Step-level computation masking for additional speedup

## TeaCache

TeaCache (Temporal similarity-based caching) accelerates diffusion inference by detecting when consecutive denoising steps are similar enough to skip computation entirely. See [teacache.md](https://docs.sglang.io/docs/sglang-diffusion/teacache) for detailed documentation.

### Quick Overview

- Tracks L1 distance between modulated inputs across timesteps
- When accumulated distance is below threshold, reuses cached residual
- Supports CFG with separate positive/negative caches

### Supported Models

- Wan (wan2.1, wan2.2)
- Hunyuan (HunyuanVideo)
- Z-Image

For Flux and Qwen models, TeaCache is automatically disabled when CFG is enabled.

## References

- [Cache-DiT Repository](https://github.com/vipshop/cache-dit)
- [TeaCache Paper](https://arxiv.org/abs/2411.14324)