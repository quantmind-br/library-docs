---
title: Qwen-Image-Edit-2511 - SGLang Documentation
url: https://docs.sglang.io/cookbook/diffusion/Qwen-Image/Qwen-Image-Edit
source: sitemap
fetched_at: 2026-05-11T05:50:02.6716604-03:00
rendered_js: false
word_count: 600
summary: This document provides an overview, deployment configurations, and usage instructions for the Qwen-Image-Edit-2511 model within the SGLang-diffusion framework.
tags:
    - qwen-image-edit
    - sglang
    - image-editing
    - deployment
    - diffusion-models
    - model-acceleration
category: guide
---

> ## Documentation Index
> 
> Fetch the complete documentation index at: [https://docs.sglang.io/llms.txt](https://docs.sglang.io/llms.txt)
> 
> Use this file to discover all available pages before exploring further.

## 1. Model Introduction

[Qwen-Image-Edit-2511](https://huggingface.co/Qwen/Qwen-Image-Edit-2511) is an enhanced version over Qwen-Image-Edit-2509, featuring multiple improvements—including notably better consistency. Built upon the 20B Qwen-Image model, Qwen-Image-Edit-2511 successfully extends Qwen-Image’s unique text rendering capabilities to image editing tasks, enabling precise text editing. Key Enhancements in Qwen-Image-Edit-2511:

- **Mitigate Image Drift**: Reduces unwanted changes in non-edited regions of the image.
- **Improved Character Consistency**: The model can perform imaginative edits based on an input portrait while preserving the identity and visual characteristics of the subject.
- **Multi-Person Consistency**: Enhanced consistency in multi-person group photos, enabling high-fidelity fusion of two separate person images into a coherent group shot.
- **Integrated LoRA Capabilities**: Selected popular community-created LoRAs are integrated directly into the base model, unlocking their effects without extra tuning (e.g., lighting enhancement, viewpoint generation).
- **Enhanced Industrial Design Generation**: Special attention to practical engineering scenarios, including batch industrial product design and material replacement for industrial components.
- **Strengthened Geometric Reasoning**: Stronger geometric reasoning capability for generating auxiliary construction lines for design or annotation purposes.

For more details, please refer to the [official Qwen-Image-Edit-2511 HuggingFace page](https://huggingface.co/Qwen/Qwen-Image-Edit-2511), the [Blog](https://qwenlm.github.io/blog/qwen-image-edit-2511/), and the [Tech Report](https://qianwen-res.oss-cn-beijing.aliyuncs.com/Qwen-Image/Qwen_Image.pdf).

## 2. SGLang-diffusion Installation

SGLang-diffusion offers multiple installation methods. You can choose the most suitable installation method based on your hardware platform and requirements. Please refer to the [official SGLang-diffusion installation guide](https://github.com/sgl-project/sglang/blob/main/python/sglang/multimodal_gen/docs/install.md) for installation instructions.

## 3. Model Deployment

This section provides deployment configurations optimized for different hardware platforms and use cases.

### 3.1 Basic Configuration

Qwen-Image-Edit-2511 is a 20B parameter model optimized for image editing tasks. The recommended launch configurations vary by hardware. **Interactive Command Generator**: Use the configuration selector below to automatically generate the appropriate deployment command for your hardware platform.

Hardware Platform

B200H200H100MI300XMI325XMI355X

Run this Command:

```
sglang serve \
  --model-path Qwen/Qwen-Image-Edit-2511 \
  --ulysses-degree=1 \
  --ring-degree=1
```

### 3.2 Configuration Tips

Current supported optimization all listed [here](https://github.com/sgl-project/sglang/blob/main/python/sglang/multimodal_gen/docs/support_matrix.md).

- `--vae-path`: Path to a custom VAE model or HuggingFace model ID (e.g., fal/FLUX.2-Tiny-AutoEncoder). If not specified, the VAE will be loaded from the main model path.
- `--num-gpus`: Number of GPUs to use
- `--tp-size`: Tensor parallelism size (only for the encoder; should not be larger than 1 if text encoder offload is enabled, as layer-wise offload plus prefetch is faster)
- `--sp-degree`: Sequence parallelism size (typically should match the number of GPUs)
- `--ulysses-degree`: The degree of DeepSpeed-Ulysses-style SP in USP
- `--ring-degree`: The degree of ring attention-style SP in USP

## 4. API Usage

For complete API documentation, please refer to the [official API usage guide](https://github.com/sgl-project/sglang/blob/main/python/sglang/multimodal_gen/docs/openai_api.md).

### 4.1 Edit an Image

```
import base64
from openai import OpenAI

client = OpenAI(api_key="EMPTY", base_url="http://localhost:3000/v1")

response = client.images.edit(
    model="Qwen/Qwen-Image-Edit-2511",
    image=open("input.png", "rb"),
    prompt="Change the color of the taxi to black.",
    n=1,
    response_format="b64_json",
)

# Save the edited image
image_bytes = base64.b64decode(response.data[0].b64_json)
with open("output.png", "wb") as f:
    f.write(image_bytes)
```

### 4.2 Advanced Usage

#### 4.2.1 Cache-DiT Acceleration

SGLang integrates [Cache-DiT](https://github.com/vipshop/cache-dit), a caching acceleration engine for Diffusion Transformers (DiT), to achieve up to 7.4x inference speedup with minimal quality loss. You can set `SGLANG_CACHE_DIT_ENABLED=True` to enable it. For more details, please refer to the SGLang Cache-DiT [documentation](https://github.com/sgl-project/sglang/blob/main/python/sglang/multimodal_gen/docs/cache_dit.md). **Basic Usage**

```
SGLANG_CACHE_DIT_ENABLED=true sglang serve --model-path Qwen/Qwen-Image-Edit-2511
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
sglang serve --model-path Qwen/Qwen-Image-Edit-2511
```

#### 4.2.2 CPU Offload

- `--dit-cpu-offload`: Use CPU offload for DiT inference. Enable if run out of memory.
- `--text-encoder-cpu-offload`: Use CPU offload for text encoder inference.
- `--image-encoder-cpu-offload`: Use CPU offload for image encoder inference.
- `--vae-cpu-offload`: Use CPU offload for VAE.
- `--pin-cpu-memory`: Pin memory for CPU offload. Only added as a temp workaround if it throws “CUDA error: invalid argument”.

## 5. Benchmark

Test Environment:

- Hardware: NVIDIA B200 GPU (1x)
- Model: Qwen/Qwen-Image-Edit-2511
- sglang diffusion version: 0.5.6.post2

### 5.1 Speedup Benchmark

#### 5.1.1 Edit a image

**Server Command**:

```
sglang serve --model-path Qwen/Qwen-Image-Edit-2511 --port 30000
```

**Benchmark Command**:

```
python3 -m sglang.multimodal_gen.benchmarks.bench_serving \
    --backend sglang-image --dataset vbench --task ti2i --num-prompts 1 --max-concurrency 1
```

**Result**:

```
================= Serving Benchmark Result =================
Backend:                                 sglang-image
Model:                                   Qwen/Qwen-Image-Edit-2511
Dataset:                                 vbench
Task:                                    ti2i
--------------------------------------------------
Benchmark duration (s):                  35.31
Request rate:                            inf
Max request concurrency:                 1
Successful requests:                     1/1
--------------------------------------------------
Request throughput (req/s):              0.03
Latency Mean (s):                        35.3053
Latency Median (s):                      35.3053
Latency P99 (s):                         35.3053
--------------------------------------------------
Peak Memory Max (MB):                    47959.35
Peak Memory Mean (MB):                   47959.35
Peak Memory Median (MB):                 47959.35
============================================================
```

#### 5.1.2 Edit a image with high concurrency

**Benchmark Command**:

```
python3 -m sglang.multimodal_gen.benchmarks.bench_serving \
    --backend sglang-image --dataset vbench --task ti2i --num-prompts 20 --max-concurrency 20
```

**Result**:

```
================= Serving Benchmark Result =================
Backend:                                 sglang-image
Model:                                   Qwen/Qwen-Image-Edit-2511
Dataset:                                 vbench
Task:                                    ti2i
--------------------------------------------------
Benchmark duration (s):                  286.11
Request rate:                            inf
Max request concurrency:                 20
Successful requests:                     20/20
--------------------------------------------------
Request throughput (req/s):              0.07
Latency Mean (s):                        150.0428
Latency Median (s):                      150.0600
Latency P99 (s):                         283.3843
--------------------------------------------------
Peak Memory Max (MB):                    47971.82
Peak Memory Mean (MB):                   47971.49
Peak Memory Median (MB):                 47971.29
============================================================
```