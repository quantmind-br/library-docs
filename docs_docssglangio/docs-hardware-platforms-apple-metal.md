---
title: Apple Silicon with Metal - SGLang Documentation
url: https://docs.sglang.io/docs/hardware-platforms/apple_metal
source: sitemap
fetched_at: 2026-05-11T05:48:48.057818169-03:00
rendered_js: false
word_count: 175
summary: This document provides instructions for installing and running SGLang on Apple Silicon devices using the Metal (MLX) backend, including guidance on server deployment and performance benchmarking.
tags:
    - sglang
    - apple-silicon
    - mlx
    - metal
    - model-serving
    - benchmarking
category: guide
---

> ## Documentation Index
> 
> Fetch the complete documentation index at: [https://docs.sglang.io/llms.txt](https://docs.sglang.io/llms.txt)
> 
> Use this file to discover all available pages before exploring further.

This document describes how run SGLang on Apple Silicon using [Metal (MLX)](https://opensource.apple.com/projects/mlx/). If you encounter issues or have questions, please [open an issue](https://github.com/sgl-project/sglang/issues).

## Install SGLang

You can install SGLang using one of the methods below.

### Install from Source

```
# Use the default branch
git clone https://github.com/sgl-project/sglang.git
cd sglang

# Install sglang python package
pip install --upgrade pip
rm -f python/pyproject.toml && mv python/pyproject_other.toml python/pyproject.toml
uv pip install -e "python[all_mps]"
```

## Launch of the Serving Engine

Launch the server with:

```
SGLANG_USE_MLX=1 python -m sglang.launch_server \
  --model <MODEL_ID_OR_PATH> \
  --disable-cuda-graph \
  --host 0.0.0.0
```

**Key Parameters Explained:**

1. `SGLANG_USE_MLX=1` - Enables the use of MLX as the SGLang runtime backend (if disabled, SGLang will fall back to `torch.mps`, which has less support)
2. `--disable-cuda-graph` - Disables usage of CUDA graph, which is not relevant for Apple Metal.
3. `--disable-overlap-schedule` - Disables overlap scheduling (enabled/not present by default) achieved using MLX’s `async_eval()`

## Benchmarking with Requests

`sglang.benchmark_one_batch` calls the synchronous prefill/decode methods directly without going through the scheduler and the overlap code path. `sglang.benchmark_offline_throughput` can toggle overlap scheduling as it uses the scheduler and the overlap code path by using the flag `--disable-overlap-schedule`.

### Throughput Testing

Basic synchronous one batch throughput:

```
SGLANG_USE_MLX=1 python -m sglang.bench_one_batch \
  --model-path <MODEL_ID_OR_PATH> \
  --disable-cuda-graph \
  --tp-size 1 \
  --batch-size 1 \
  --input-len 60 \
  --output-len 10
```

Synchronous offline throughput:

```
SGLANG_USE_MLX=1 python -m sglang.bench_offline_throughput \
  --model-path <MODEL_ID_OR_PATH> \
  --disable-cuda-graph \
  --num-prompts 1 \
  --disable-overlap-schedule
```

Asynchronous offline throughput:

```
SGLANG_USE_MLX=1 python -m sglang.bench_offline_throughput \
  --model-path <MODEL_ID_OR_PATH> \
  --disable-cuda-graph \
  --num-prompts 1
```