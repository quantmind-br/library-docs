---
title: CI Performance Baselines - SGLang Documentation
url: https://docs.sglang.io/docs/sglang-diffusion/ci_perf
source: sitemap
fetched_at: 2026-05-11T05:51:24.152940049-03:00
rendered_js: false
word_count: 81
summary: This document describes how to use the performance baseline generation script to test diffusion server latency and update benchmark scenarios.
tags:
    - performance-testing
    - benchmark-script
    - diffusion-server
    - latency-measurement
    - automation-tools
category: guide
---

- [Perf Baseline Generation Script](#perf-baseline-generation-script)
- [Usage](#usage)

> ## Documentation Index
> 
> Fetch the complete documentation index at: [https://docs.sglang.io/llms.txt](https://docs.sglang.io/llms.txt)
> 
> Use this file to discover all available pages before exploring further.

## Perf Baseline Generation Script

`python/sglang/multimodal_gen/test/scripts/gen_perf_baselines.py` starts a local diffusion server, issues requests for selected test cases, aggregates stage/denoise-step/E2E timings from the perf log, and writes the results back to the `scenarios` section of `perf_baselines.json`.

### Usage

Update a single case:

```
python python/sglang/multimodal_gen/test/scripts/gen_perf_baselines.py --case qwen_image_t2i
```

Select by regex:

```
python python/sglang/multimodal_gen/test/scripts/gen_perf_baselines.py --match 'qwen_image_.*'
```

Run all keys from the baseline file `scenarios`:

```
python python/sglang/multimodal_gen/test/scripts/gen_perf_baselines.py --all-from-baseline
```

Specify input/output paths and timeout:

```
python python/sglang/multimodal_gen/test/scripts/gen_perf_baselines.py --baseline python/sglang/multimodal_gen/test/server/perf_baselines.json --out /tmp/perf_baselines.json --timeout 600
```