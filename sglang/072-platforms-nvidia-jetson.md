---
title: NVIDIA Jetson Orin — SGLang
url: https://docs.sglang.io/platforms/nvidia_jetson.html
source: crawler
fetched_at: 2026-02-04T08:47:11.491632334-03:00
rendered_js: false
word_count: 181
summary: This document provides instructions for installing and running SGLang on NVIDIA Jetson Orin devices, covering environment setup, containerized deployment, and performance optimization through quantization.
tags:
    - nvidia-jetson
    - sglang
    - jetson-containers
    - llm-inference
    - torchao
    - quantization
    - edge-computing
category: tutorial
---

## Contents

## NVIDIA Jetson Orin[#](#nvidia-jetson-orin "Link to this heading")

## Prerequisites[#](#prerequisites "Link to this heading")

Before starting, ensure the following:

- [**NVIDIA Jetson AGX Orin Devkit**](https://www.nvidia.com/en-us/autonomous-machines/embedded-systems/jetson-orin/) is set up with **JetPack 6.1** or later.
- **CUDA Toolkit** and **cuDNN** are installed.
- Verify that the Jetson AGX Orin is in **high-performance mode**:

* * *

## Installing and running SGLang with Jetson Containers[#](#installing-and-running-sglang-with-jetson-containers "Link to this heading")

Clone the jetson-containers github repository:

```
git clone https://github.com/dusty-nv/jetson-containers.git
```

Run the installation script:

```
bash jetson-containers/install.sh
```

Build the container image:

```
jetson-containers build sglang
```

Run the container:

```
jetson-containers run $(autotag sglang)
```

Or you can also manually run a container with this command:

```
docker run --runtime nvidia -it --rm --network=host IMAGE_NAME
```

* * *

## Running Inference[#](#running-inference "Link to this heading")

Launch the server:

```
python-msglang.launch_server\
--model-pathdeepseek-ai/DeepSeek-R1-Distill-Llama-8B\
--devicecuda\
--dtypehalf\
--attention-backendflashinfer\
--mem-fraction-static0.8\
--context-length8192
```

The quantization and limited context length (`--dtype half --context-length 8192`) are due to the limited computational resources in [Nvidia jetson kit](https://www.nvidia.com/en-us/autonomous-machines/embedded-systems/jetson-orin/). A detailed explanation can be found in [Server Arguments](https://docs.sglang.io/advanced_features/server_arguments.html).

After launching the engine, refer to [Chat completions](https://docs.sglang.io/basic_usage/openai_api_completions.html#Usage) to test the usability.

* * *

## Running quantization with TorchAO[#](#running-quantization-with-torchao "Link to this heading")

TorchAO is suggested to NVIDIA Jetson Orin.

```
python-msglang.launch_server\
--model-pathmeta-llama/Meta-Llama-3.1-8B-Instruct\
--devicecuda\
--dtypebfloat16\
--attention-backendflashinfer\
--mem-fraction-static0.8\
--context-length8192\
--torchao-configint4wo-128
```

This enables TorchAO’s int4 weight-only quantization with a 128-group size. The usage of `--torchao-config int4wo-128` is also for memory efficiency.

* * *

## Structured output with XGrammar[#](#structured-output-with-xgrammar "Link to this heading")

Please refer to [SGLang doc structured output](https://docs.sglang.io/advanced_features/structured_outputs.html).

* * *

Thanks to the support from [Nurgaliyev Shakhizat](https://github.com/shahizat), [Dustin Franklin](https://github.com/dusty-nv) and [Johnny Núñez Cano](https://github.com/johnnynunez).

## References[#](#references "Link to this heading")

- [NVIDIA Jetson AGX Orin Documentation](https://developer.nvidia.com/embedded/jetson-agx-orin)