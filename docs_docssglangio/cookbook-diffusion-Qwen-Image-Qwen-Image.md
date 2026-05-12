---
title: Qwen-Image - SGLang Documentation
url: https://docs.sglang.io/cookbook/diffusion/Qwen-Image/Qwen-Image
source: sitemap
fetched_at: 2026-05-11T05:49:50.624749783-03:00
rendered_js: false
word_count: 448
summary: This document provides a guide for deploying and using the Qwen-Image model within the SGLang-diffusion framework, including configuration options, API usage, and performance optimization techniques like Cache-DiT.
tags:
    - sglang
    - qwen-image
    - diffusion-models
    - model-deployment
    - gpu-optimization
    - cache-dit
    - text-to-image
category: guide
---

> ## Documentation Index
> 
> Fetch the complete documentation index at: [https://docs.sglang.io/llms.txt](https://docs.sglang.io/llms.txt)
> 
> Use this file to discover all available pages before exploring further.

## 1. Model Introduction

[Qwen-Image](https://huggingface.co/Qwen/Qwen-Image) is a text-to-image diffusion model developed by the Qwen team. For more details, please refer to the [official Qwen-Image HuggingFace page](https://huggingface.co/Qwen/Qwen-Image), the [Blog](https://qwenlm.github.io/blog/qwen-image/), and the [Tech Report](https://qianwen-res.oss-cn-beijing.aliyuncs.com/Qwen-Image/Qwen_Image.pdf).

## 2. SGLang-diffusion Installation

SGLang-diffusion offers multiple installation methods. You can choose the most suitable installation method based on your hardware platform and requirements. Please refer to the [official SGLang-diffusion installation guide](https://docs.sglang.io/docs/sglang-diffusion/installation) for installation instructions.

## 3. Model Deployment

This section provides deployment configurations optimized for different hardware platforms and use cases.

### 3.1 Basic Configuration

Qwen-Image is a text-to-image model. The recommended launch configurations vary by hardware. **Interactive Command Generator**: Use the configuration selector below to automatically generate the appropriate deployment command for your hardware platform.

Hardware Platform

MI300XMI325XMI355X

Run this Command:

```
sglang serve \
  --model-path Qwen/Qwen-Image \
  --ulysses-degree=1 \
  --ring-degree=1
```

### 3.2 Configuration Tips

Current supported optimization all listed [here](https://docs.sglang.io/docs/sglang-diffusion/attention_backends#platform-support-matrix).

- `--vae-path`: Path to a custom VAE model or HuggingFace model ID (e.g., fal/FLUX.2-Tiny-AutoEncoder). If not specified, the VAE will be loaded from the main model path.
- `--num-gpus`: Number of GPUs to use
- `--tp-size`: Tensor parallelism size (only for the encoder; should not be larger than 1 if text encoder offload is enabled, as layer-wise offload plus prefetch is faster)
- `--sp-degree`: Sequence parallelism size (typically should match the number of GPUs)
- `--ulysses-degree`: The degree of DeepSpeed-Ulysses-style SP in USP
- `--ring-degree`: The degree of ring attention-style SP in USP

**AMD ROCm Notes**: Requires SGLang &gt;= v0.5.8.

## 4. API Usage

For complete API documentation, please refer to the [official API usage guide](https://docs.sglang.io/docs/sglang-diffusion/api/openai_api).

### 4.1 Generate an Image

```
import base64
from openai import OpenAI

client = OpenAI(api_key="EMPTY", base_url="http://localhost:30000/v1")

response = client.images.generate(
    model="Qwen/Qwen-Image",
    prompt="A logo With Bold Large text: SGL Diffusion",
    n=1,
    response_format="b64_json",
)

# Save the generated image
image_bytes = base64.b64decode(response.data[0].b64_json)
with open("output.png", "wb") as f:
    f.write(image_bytes)
```

### 4.2 Advanced Usage

#### 4.2.1 Cache-DiT Acceleration

SGLang integrates [Cache-DiT](https://github.com/vipshop/cache-dit), a caching acceleration engine for Diffusion Transformers (DiT), to achieve up to 7.4x inference speedup with minimal quality loss. You can set `SGLANG_CACHE_DIT_ENABLED=True` to enable it. For more details, please refer to the SGLang Cache-DiT [documentation](https://docs.sglang.io/docs/sglang-diffusion/cache_dit). **Basic Usage**

```
SGLANG_CACHE_DIT_ENABLED=true sglang serve --model-path Qwen/Qwen-Image
```

**Advanced Usage**

- DBCache Parameters: DBCache controls block-level caching behavior:

ParameterEnv VariableDefaultDescriptionFn`SGLANG_CACHE_DIT_FN`1Number of first blocks to always computeBn`SGLANG_CACHE_DIT_BN`0Number of last blocks to always computeW`SGLANG_CACHE_DIT_WARMUP`4Warmup steps before caching startsR`SGLANG_CACHE_DIT_RDT`0.24Residual difference thresholdMC`SGLANG_CACHE_DIT_MC`3Maximum continuous cached steps

- TaylorSeer Configuration: TaylorSeer improves caching accuracy using Taylor expansion:

ParameterEnv VariableDefaultDescriptionEnable`SGLANG_CACHE_DIT_TAYLORSEER`falseEnable TaylorSeer calibratorOrder`SGLANG_CACHE_DIT_TS_ORDER`1Taylor expansion order (1 or 2)

Combined Configuration Example:

```
SGLANG_CACHE_DIT_ENABLED=true \
SGLANG_CACHE_DIT_FN=2 \
SGLANG_CACHE_DIT_BN=1 \
SGLANG_CACHE_DIT_WARMUP=4 \
SGLANG_CACHE_DIT_RDT=0.4 \
SGLANG_CACHE_DIT_MC=4 \
SGLANG_CACHE_DIT_TAYLORSEER=true \
SGLANG_CACHE_DIT_TS_ORDER=2 \
sglang serve --model-path Qwen/Qwen-Image
```

#### 4.2.2 CPU Offload

- `--dit-cpu-offload`: Use CPU offload for DiT inference. Enable if run out of memory.
- `--text-encoder-cpu-offload`: Use CPU offload for text encoder inference.
- `--vae-cpu-offload`: Use CPU offload for VAE.
- `--pin-cpu-memory`: Pin memory for CPU offload. Only added as a temp workaround if it throws “CUDA error: invalid argument”.

## 5. Benchmark

Test Environment:

- Hardware: AMD Instinct MI300X GPU (1x)
- Model: Qwen/Qwen-Image
- Docker Image: lmsysorg/sglang:v0.5.8-rocm700-mi30x
- sglang diffusion version: 0.5.8

### 5.1 Speedup Benchmark

#### 5.1.1 Generate an image

**Server Command**:

```
sglang serve --model-path Qwen/Qwen-Image \
    --ulysses-degree=1 --ring-degree=1 --port 30000
```

**Benchmark Command**:

```
python3 -m sglang.multimodal_gen.benchmarks.bench_serving \
    --backend sglang-image --dataset vbench --task text-to-image --num-prompts 1 --max-concurrency 1
```

**Result**:

```
================= Serving Benchmark Result =================
Task:                                    text-to-image
Model:                                   Qwen/Qwen-Image
Dataset:                                 vbench
--------------------------------------------------
Benchmark duration (s):                  29.04
Request rate:                            inf
Max request concurrency:                 1
Successful requests:                     1/1
--------------------------------------------------
Request throughput (req/s):              0.03
Latency Mean (s):                        29.0378
Latency Median (s):                      29.0378
Latency P99 (s):                         29.0378
--------------------------------------------------
Peak Memory Max (MB):                    48018.83
Peak Memory Mean (MB):                   48018.83
Peak Memory Median (MB):                 48018.83
============================================================
```

#### 5.1.2 Generate images with high concurrency

**Benchmark Command**:

```
python3 -m sglang.multimodal_gen.benchmarks.bench_serving \
    --backend sglang-image --dataset vbench --task text-to-image --num-prompts 20 --max-concurrency 20
```

**Result**:

```
================= Serving Benchmark Result =================
Task:                                    text-to-image
Model:                                   Qwen/Qwen-Image
Dataset:                                 vbench
--------------------------------------------------
Benchmark duration (s):                  300.79
Request rate:                            inf
Max request concurrency:                 20
Successful requests:                     14/20
--------------------------------------------------
Request throughput (req/s):              0.05
Latency Mean (s):                        154.5368
Latency Median (s):                      154.8363
Latency P99 (s):                         285.4603
--------------------------------------------------
Peak Memory Max (MB):                    48030.31
Peak Memory Mean (MB):                   48030.30
Peak Memory Median (MB):                 48030.29
============================================================
```