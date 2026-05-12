---
title: Diffusion Models Benchmark Documentation - SGLang Documentation
url: https://docs.sglang.io/cookbook/base/benchmarks/diffusion_model_benchmark
source: sitemap
fetched_at: 2026-05-11T05:50:02.111185919-03:00
rendered_js: false
word_count: 324
summary: This document provides a guide and parameter reference for the sglang benchmark tool used to evaluate the serving throughput and latency of multimodal diffusion models.
tags:
    - sglang
    - benchmarking
    - performance-testing
    - diffusion-models
    - multimodal-generation
    - throughput-analysis
category: guide
---

> ## Documentation Index
> 
> Fetch the complete documentation index at: [https://docs.sglang.io/llms.txt](https://docs.sglang.io/llms.txt)
> 
> Use this file to discover all available pages before exploring further.

`sglang.multimodal_gen.benchmarks.bench_serving` is a command-line tool designed to benchmark the online serving throughput and latency of Diffusion Models. It supports two backends (`sglang-image`, `sglang-video`) and offers flexible configurations for request rates, dataset types, and profiling.

## 1. Quick Start

### 1.1 Benchmarking in Low Concurrency

Run a benchmark on a local server (port 30000) generating 1 videos/images from the `vbench` dataset.

```
# For text to video: such as Wan2.2-T2V-A14B-Diffusers
python3 -m sglang.multimodal_gen.benchmarks.bench_serving \
    --backend sglang-video --dataset vbench --task t2v --num-prompts 1 --max-concurrency 1

# For image to video: such as Wan2.2-I2V-A14B-Diffusers
python3 -m sglang.multimodal_gen.benchmarks.bench_serving \
    --backend sglang-video --dataset vbench --task i2v --num-prompts 1 --max-concurrency 1

# For image-text to video: such as Wan2.2-TI2V-5B-Diffusers
python3 -m sglang.multimodal_gen.benchmarks.bench_serving \
    --backend sglang-video --dataset vbench --task ti2v --num-prompts 1 --max-concurrency 1

# For text to image: such as Qwen-Image
python3 -m sglang.multimodal_gen.benchmarks.bench_serving \
    --backend sglang-image --dataset vbench --task t2i --num-prompts 1 --max-concurrency 1

# For image-text to image: such as Qwen-Image-Edit
python3 -m sglang.multimodal_gen.benchmarks.bench_serving \
    --backend sglang-image --dataset vbench --task ti2i --num-prompts 1 --max-concurrency 1
```

### 1.2 Benchmarking in High Concurrency

Run a benchmark on a local server (port 30000) generating 20 videos/images from the `vbench` dataset.

```
# For text to video: such as Wan2.2-T2V-A14B-Diffusers
python3 -m sglang.multimodal_gen.benchmarks.bench_serving \
    --backend sglang-video --dataset vbench --task t2v --num-prompts 20 --max-concurrency 20

# For image to video: such as Wan2.2-I2V-A14B-Diffusers
python3 -m sglang.multimodal_gen.benchmarks.bench_serving \
    --backend sglang-video --dataset vbench --task i2v --num-prompts 20 --max-concurrency 20

# For image-text to video: such as Wan2.2-TI2V-5B-Diffusers
python3 -m sglang.multimodal_gen.benchmarks.bench_serving \
    --backend sglang-video --dataset vbench --task ti2v --num-prompts 20 --max-concurrency 20

# For text to image: such as Qwen-Image
python3 -m sglang.multimodal_gen.benchmarks.bench_serving \
    --backend sglang-image --dataset vbench --task t2i --num-prompts 20 --max-concurrency 20

# For image-text to image: such as Qwen-Image-Edit
python3 -m sglang.multimodal_gen.benchmarks.bench_serving \
    --backend sglang-image --dataset vbench --task ti2i --num-prompts 20 --max-concurrency 20
```

## 2. Parameter Reference

### 2.1 Connection & Backend Settings

ArgumentDefaultDescription`--backend`**Required**The backend type to use. Choices: `sglang-image`, `sglang-video`.`--base-url``None`Base URL of the server (e.g., `http://localhost:30000`). If specified, this overrides `--host` and `--port`.`--host``None`The server host (e.g., `127.0.0.1`).`--port``None`The server port.`--model``None`Model name or path.

### 2.2 Workload & Task Configuration

ArgumentChoicesDescription`--task``t2v`, `i2v`, `ti2v`, `t2i`, `ti2i`Defines the generation task: `t2v` (Text-to-Video), `i2v` (Image-to-Video), `ti2v` (Text+Image-to-Video), `t2i` (Text-to-image), `ti2i` (Text+Image-to-Image).`--dataset``vbench`, `random`The source of prompts/inputs.`--dataset-path``None`(Optional) Path to a local dataset file if not using built-in presets.`--num-prompts``None`The total number of prompts/requests to execute during the benchmark.

### 2.3 Generation Parameters

ArgumentDescription`--width`The target width for the generated image or video.`--height`The target height for the generated image or video.`--num-frames`Number of frames to generate (Specific to Video backends).`--fps`Frames Per Second configuration (Specific to Video backends).

### 2.4 Concurrency & Load Control

ArgumentDescription`--request-rate`The number of requests initiated per second. If set to `inf`, all requests are sent immediately (burst). If set to a number, request arrival times follow a Poisson process.`--max-concurrency`The maximum number of requests allowed to execute simultaneously. This simulates a semaphore or upstream limit. Even if `request-rate` is high, the actual processing rate is capped by this value.

### 2.5 Logging & Output

ArgumentDescription`--output-file`Path to save the benchmark metrics (JSON format).`--disable-tqdm`If set, disables the progress bar in the console.

## 3. Metrics

- `Request Throughput` (req/s), Output Throughput (tok/s)
- `Latency Mean` (ms): Time to Per Step
- `Peak Memory Max` (ms): Max Memory Usage during running