---
title: XPU — SGLang
url: https://docs.sglang.io/platforms/xpu.html
source: crawler
fetched_at: 2026-02-04T08:47:13.077828684-03:00
rendered_js: false
word_count: 184
summary: This document provides instructions for setting up the SGLang environment and running LLM inference on Intel GPUs, covering installation from source, server deployment, and benchmarking.
tags:
    - intel-gpu
    - xpu
    - sglang
    - llm-inference
    - installation-guide
    - benchmarking
category: guide
---

## Contents

## XPU[#](#xpu "Link to this heading")

The document addresses how to set up the [SGLang](https://github.com/sgl-project/sglang) environment and run LLM inference on Intel GPU, [see more context about Intel GPU support within PyTorch ecosystem](https://docs.pytorch.org/docs/stable/notes/get_start_xpu.html).

Specifically, SGLang is optimized for [Intel® Arc™ Pro B-Series Graphics](https://www.intel.com/content/www/us/en/ark/products/series/242616/intel-arc-pro-b-series-graphics.html) and [Intel® Arc™ B-Series Graphics](https://www.intel.com/content/www/us/en/ark/products/series/240391/intel-arc-b-series-graphics.html).

## Optimized Model List[#](#optimized-model-list "Link to this heading")

A list of LLMs have been optimized on Intel GPU, and more are on the way:

**Note:** The model identifiers listed in the table above have been verified on [Intel® Arc™ B580 Graphics](https://www.intel.com/content/www/us/en/products/sku/241598/intel-arc-b580-graphics/specifications.html).

## Installation[#](#installation "Link to this heading")

### Install From Source[#](#install-from-source "Link to this heading")

Currently SGLang XPU only supports installation from source. Please refer to [“Getting Started on Intel GPU”](https://docs.pytorch.org/docs/stable/notes/get_start_xpu.html) to install XPU dependency.

```
# Create and activate a conda environment
condacreate-nsgl-xpupython=3.12-y
condaactivatesgl-xpu

# Set PyTorch XPU as primary pip install channel to avoid installing the larger CUDA-enabled version and prevent potential runtime issues.
pip3installtorch==2.9.0+xputorchaotorchvisiontorchaudiopytorch-triton-xpu==3.5.0--index-urlhttps://download.pytorch.org/whl/xpu
pip3installxgrammar--no-deps# xgrammar will introduce CUDA-enabled triton which might conflict with XPU

# Clone the SGLang code
gitclonehttps://github.com/sgl-project/sglang.git
cdsglang
gitcheckout<YOUR-DESIRED-VERSION>

# Use dedicated toml file
cdpython
cppyproject_xpu.tomlpyproject.toml
# Install SGLang dependent libs, and build SGLang main package
pipinstall--upgradepipsetuptools
pipinstall-v.
```

### Install Using Docker[#](#install-using-docker "Link to this heading")

The docker for XPU is under active development. Please stay tuned.

## Launch of the Serving Engine[#](#launch-of-the-serving-engine "Link to this heading")

Example command to launch SGLang serving:

```
python-msglang.launch_server\
--model<MODEL_ID_OR_PATH>\
--trust-remote-code\
--disable-overlap-schedule\
--devicexpu\
--host0.0.0.0\
--tp2\ # using multi GPUs
--attention-backendintel_xpu\ # using intel optimized XPU attention backend
--page-size\ # intel_xpu attention backend supports [32, 64, 128]
```

## Benchmarking with Requests[#](#benchmarking-with-requests "Link to this heading")

You can benchmark the performance via the `bench_serving` script. Run the command in another terminal.

```
python-msglang.bench_serving\
--dataset-namerandom\
--random-input-len1024\
--random-output-len1024\
--num-prompts1\
--request-rateinf\
--random-range-ratio1.0
```

The detail explanations of the parameters can be looked up by the command:

```
python-msglang.bench_serving-h
```

Additionally, the requests can be formed with [OpenAI Completions API](https://docs.sglang.io/basic_usage/openai_api_completions.html) and sent via the command line (e.g. using `curl`) or via your own script.