---
title: 'Ring SP Benchmark: Wan2.2-TI2V-5B (u1r2 vs Baseline) - SGLang Documentation'
url: https://docs.sglang.io/docs/sglang-diffusion/ring_sp_performance
source: sitemap
fetched_at: 2026-05-11T05:48:06.451808598-03:00
rendered_js: false
word_count: 177
summary: This document presents a performance comparison of Ring-SP versus baseline configurations for the Wan2.2-TI2V-5B-Diffusers model, detailing latency improvements and memory usage metrics.
tags:
    - performance-benchmark
    - ring-sp
    - diffusion-models
    - gpu-memory-optimization
    - latency-analysis
    - sglang
category: reference
---

- [Benchmark Setup](#benchmark-setup)
- [Online Serving](#online-serving)
- [Ring SP (u1r2)](#ring-sp-u1r2)
- [Baseline (u1r1)](#baseline-u1r1)
- [Benchmarks](#benchmarks)
- [Benchmark Disclaimer](#benchmark-disclaimer)
- [Stage Time Breakdown](#stage-time-breakdown)
- [Memory Usage](#memory-usage)
- [Summary](#summary)

> ## Documentation Index
> 
> Fetch the complete documentation index at: [https://docs.sglang.io/llms.txt](https://docs.sglang.io/llms.txt)
> 
> Use this file to discover all available pages before exploring further.

This page reports Ring-SP performance for `Wan2.2-TI2V-5B-Diffusers` using:

- Parallel config: `sp=2, ulysses=1, ring=2` (short: `u1r2`)
- Baseline config: `sp=1, ulysses=1, ring=1` (short: `u1r1`)

## Benchmark Setup

- Model: `Wan2.2-TI2V-5B-Diffusers`
- GPU: `48G RTX40 series * 2`

## Online Serving

### Ring SP (`u1r2`)

```
sglang serve \
  --model-type diffusion \
  --model-path /model/HuggingFace/Wan-AI/Wan2.2-TI2V-5B-Diffusers \
  --num-gpus 2 --sp-degree 2 --ulysses-degree 1 --ring-degree 2 \
  --port 8898
```

### Baseline (`u1r1`)

```
sglang serve \
  --model-type diffusion \
  --model-path /model/HuggingFace/Wan-AI/Wan2.2-TI2V-5B-Diffusers \
  --num-gpus 1 --sp-degree 1 --ulysses-degree 1 --ring-degree 1 \
  --port 8898
```

## Benchmarks

### Benchmark Disclaimer

These benchmarks are provided for reference under one specific setup and command configuration. Actual performance may vary with model settings, runtime environment, and request patterns.

### Stage Time Breakdown

Stage / Metric`u1r2` (s)`u1r1` baseline (s)SpeedupInputValidation0.10600.10290.97xTextEncoding1.39652.22611.59xLatentPreparation0.00020.00021.00xTimestepPreparation0.00030.00041.33xDenoising52.635871.67851.36xDecoding7.670813.43141.75x**Total****63.74****90.63****1.42x**

### Memory Usage

Memory Metric`u1r2` (GB)`u1r1` baseline (GB)DeltaPeak GPU Memory20.0727.40-7.33Peak Allocated13.3520.40-7.05Memory Overhead6.727.00-0.28Overhead Ratio33.5%25.6%+7.9pp

## Summary

- End-to-end latency improves from `90.63s` to `63.74s` (`1.42x`).
- Main gains come from `Denoising` (`1.36x`) and `Decoding` (`1.75x`).
- Absolute memory usage drops noticeably on Ring-SP (`Peak GPU Memory -7.33GB`, `Peak Allocated -7.05GB`).
- Overhead ratio rises (`+7.9pp`), so future tuning can focus on reducing communication/runtime overhead while preserving the latency gain.