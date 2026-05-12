---
title: Performance Optimization - SGLang Documentation
url: https://docs.sglang.io/docs/sglang-diffusion/performance-optimization
source: sitemap
fetched_at: 2026-05-11T05:51:13.81874197-03:00
rendered_js: false
word_count: 156
summary: This document provides an overview of performance optimization strategies for SGLang Diffusion, including attention backends, caching acceleration, inference batching, and diagnostic profiling tools.
tags:
    - sglang-diffusion
    - performance-optimization
    - attention-backends
    - caching-acceleration
    - inference-batching
    - model-profiling
category: guide
---

> ## Documentation Index
> 
> Fetch the complete documentation index at: [https://docs.sglang.io/llms.txt](https://docs.sglang.io/llms.txt)
> 
> Use this file to discover all available pages before exploring further.

This section covers the main performance levers for SGLang Diffusion: attention backends, caching acceleration, and profiling.

## Overview

OptimizationTypeDescriptionCache-DiTCachingBlock-level caching with DBCache, TaylorSeer, and SCMTeaCacheCachingTimestep-level caching based on temporal similarityAttention BackendsKernelOptimized attention implementations (FlashAttention, SageAttention, etc.)Inference BatchingSchedulerRequest batching for native diffusion servingProfilingDiagnosticsPyTorch Profiler and Nsight Systems guidance

## Start Here

- Use [Attention Backends](https://docs.sglang.io/docs/sglang-diffusion/attention_backends) to choose the best backend for your model and hardware.
- Use [Inference Batching](https://docs.sglang.io/docs/sglang-diffusion/dynamic_batching) to improve throughput for compatible concurrent requests.
- Use [Caching Acceleration](https://docs.sglang.io/docs/sglang-diffusion/caching-acceleration) to reduce denoising cost with Cache-DiT or TeaCache.
- Use [Profiling](https://docs.sglang.io/docs/sglang-diffusion/profiling) when you need to diagnose a bottleneck rather than guess.

## Caching at a Glance

- [Cache-DiT](https://docs.sglang.io/docs/sglang-diffusion/cache_dit) is block-level caching for diffusers pipelines and higher speedup-oriented tuning.
- [TeaCache](https://docs.sglang.io/docs/sglang-diffusion/teacache) is timestep-level caching built into SGLang model families.

## Current Baseline Snapshot

For Ring SP benchmark details, see:

- [Ring SP Performance](https://docs.sglang.io/docs/sglang-diffusion/ring_sp_performance)

## References

- [Cache-DiT Repository](https://github.com/vipshop/cache-dit)
- [TeaCache Paper](https://arxiv.org/abs/2411.14324)