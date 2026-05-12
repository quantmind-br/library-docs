---
title: TeaCache Acceleration - SGLang Documentation
url: https://docs.sglang.io/docs/sglang-diffusion/teacache
source: sitemap
fetched_at: 2026-05-11T05:51:21.814712205-03:00
rendered_js: false
word_count: 288
summary: This document explains the TeaCache mechanism, a temporal similarity-based caching strategy used to accelerate diffusion model inference by skipping redundant computations.
tags:
    - teacache
    - diffusion-models
    - inference-acceleration
    - caching-strategy
    - l1-distance
    - model-optimization
category: concept
---

> ## Documentation Index
> 
> Fetch the complete documentation index at: [https://docs.sglang.io/llms.txt](https://docs.sglang.io/llms.txt)
> 
> Use this file to discover all available pages before exploring further.

> **Note**: This is one of two caching strategies available in SGLang. For an overview of all caching options, see [caching](https://docs.sglang.io/docs/sglang-diffusion/caching-acceleration).

TeaCache (Temporal similarity-based caching) accelerates diffusion inference by detecting when consecutive denoising steps are similar enough to skip computation entirely.

## Overview

TeaCache works by:

1. Tracking the L1 distance between modulated inputs across consecutive timesteps
2. Accumulating the rescaled L1 distance over steps
3. When accumulated distance is below a threshold, reusing the cached residual
4. Supporting CFG (Classifier-Free Guidance) with separate positive/negative caches

## How It Works

### L1 Distance Tracking

At each denoising step, TeaCache computes the relative L1 distance between the current and previous modulated inputs:

```
rel_l1 = |current - previous|.mean() / |previous|.mean()
```

This distance is then rescaled using polynomial coefficients and accumulated:

```
accumulated += poly(coefficients)(rel_l1)
```

### Cache Decision

- If `accumulated >= threshold`: Force computation, reset accumulator
- If `accumulated < threshold`: Skip computation, use cached residual

### CFG Support

For models that support CFG cache separation (Wan, Hunyuan, Z-Image), TeaCache maintains separate caches for positive and negative branches:

- `previous_modulated_input` / `previous_residual` for positive branch
- `previous_modulated_input_negative` / `previous_residual_negative` for negative branch

For models that don’t support CFG separation (Flux, Qwen), TeaCache is automatically disabled when CFG is enabled.

## Configuration

TeaCache is configured via `TeaCacheParams` in the sampling parameters:

```
from sglang.multimodal_gen.configs.sample.teacache import TeaCacheParams

params = TeaCacheParams(
    teacache_thresh=0.1,           # Threshold for accumulated L1 distance
    coefficients=[1.0, 0.0, 0.0],  # Polynomial coefficients for L1 rescaling
)
```

### Parameters

ParameterTypeDescription`teacache_thresh`floatThreshold for accumulated L1 distance. Lower = more caching, faster but potentially lower quality`coefficients`list\[float]Polynomial coefficients for L1 rescaling. Model-specific tuning

### Model-Specific Configurations

Different models may have different optimal configurations. The coefficients are typically tuned per-model to balance speed and quality.

## Supported Models

TeaCache is built into the following model families:

Model FamilyCFG Cache SeparationNotesWan (wan2.1, wan2.2)YesFull supportHunyuan (HunyuanVideo)YesTo be supportedZ-ImageYesTo be supportedFluxNoTo be supportedQwenNoTo be supported

## References

- [TeaCache: Accelerating Diffusion Models with Temporal Similarity](https://arxiv.org/abs/2411.14324)