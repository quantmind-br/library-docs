---
title: Ascend NPU Ring-SP Performance (Wan2.1-T2V-1.3B) - SGLang Documentation
url: https://docs.sglang.io/docs/hardware-platforms/ascend-npus/ascend_npu_ring_sp_performance
source: sitemap
fetched_at: 2026-05-11T05:48:36.829965989-03:00
rendered_js: false
word_count: 147
summary: This document presents a performance benchmark analysis of Ring-SP acceleration on Ascend NPU hardware using the SGLang framework compared to a baseline configuration.
tags:
    - performance-benchmark
    - ring-sp
    - ascend-npu
    - sglang
    - distributed-inference
    - hardware-acceleration
category: other
---

- [Benchmark Setup](#benchmark-setup)
- [Generate Commands](#generate-commands)
- [Baseline (u1r1)](#baseline-u1r1)
- [Ring-SP (u1r2)](#ring-sp-u1r2)
- [Benchmarks](#benchmarks)
- [Stage Time Breakdown](#stage-time-breakdown)
- [Summary](#summary)

> ## Documentation Index
> 
> Fetch the complete documentation index at: [https://docs.sglang.io/llms.txt](https://docs.sglang.io/llms.txt)
> 
> Use this file to discover all available pages before exploring further.

This page reports Ring-SP performance on Ascend NPU with `torch_npu==2.10.0`.

- Baseline config: `ulysses=1, ring=1` (short: `u1r1`)
- Ring-SP config: `ulysses=1, ring=2` (short: `u1r2`)

## Benchmark Setup

- Model: `Wan2.1-T2V-1.3B-Diffusers`
- Prompt: `"a cat is playing piano"`
- Framework command: `sglang generate`
- Runtime: `torch_npu==2.10.0`

## Generate Commands

### Baseline (`u1r1`)

```
sglang generate --model-path /nas/disk1/Wan2.1-T2V-1.3B-Diffusers \
    --prompt "a cat is playing piano" --num-gpus 1 --ring-degree 1 \
    --save-output
```

### Ring-SP (`u1r2`)

```
sglang generate --model-path /nas/disk1/Wan2.1-T2V-1.3B-Diffusers \
    --prompt "a cat is playing piano" --num-gpus 2 --ring-degree 2 \
    --save-output
```

## Benchmarks

Benchmark Disclaimer These numbers are from one fixed setup and one prompt case. Actual performance may vary by model settings, environment, and workload.

### Stage Time Breakdown

Stage / Metric`u1r2` (s)`u1r1` baseline (s)SpeedupInputValidation0.00030.00020.67xTextEncoding3.59363.58201.00xLatentPreparation0.00070.00557.86xTimestepPreparation0.00080.00070.88xDenoising121.2788239.25801.97xDecoding13.868516.49691.19x**Total (Pixel data generated)****141.86****266.50****1.88x**

## Summary

- With `torch_npu==2.10.0`, Ring-SP (`u1r2`) runs successfully on NPU for this case.
- End-to-end generation time improves from `266.50s` to `141.86s` (`1.88x`).
- The main gain comes from `DenoisingStage` (`1.97x`), while decoding also improves (`1.19x`).