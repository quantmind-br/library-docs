---
title: MindSpore Models — SGLang
url: https://docs.sglang.io/supported_models/mindspore_models.html
source: crawler
fetched_at: 2026-02-04T08:47:09.293455443-03:00
rendered_js: false
word_count: 232
summary: This document provides instructions for running MindSpore models on Ascend NPUs using the SGLang framework, covering installation, inference scripts, and server deployment.
tags:
    - mindspore
    - sglang
    - ascend-npu
    - model-deployment
    - inference-engine
    - distributed-computing
category: guide
---

## Contents

## MindSpore Models[#](#mindspore-models "Link to this heading")

## Introduction[#](#introduction "Link to this heading")

MindSpore is a high-performance AI framework optimized for Ascend NPUs. This doc guides users to run MindSpore models in SGLang.

## Requirements[#](#requirements "Link to this heading")

MindSpore currently only supports Ascend NPU devices. Users need to first install CANN 8.5. The CANN software packages can be downloaded from the [Ascend Official Website](https://www.hiascend.com).

## Supported Models[#](#supported-models "Link to this heading")

Currently, the following models are supported:

- **Qwen3**: Dense and MoE models
- **DeepSeek V3/R1**
- *More models coming soon…*

## Installation[#](#installation "Link to this heading")

> **Note**: Currently, MindSpore models are provided by an independent package `sgl-mindspore`. Support for MindSpore is built upon current SGLang support for Ascend NPU platform. Please first [install SGLang for Ascend NPU](https://docs.sglang.io/platforms/ascend_npu.html) and then install `sgl-mindspore`:

```
gitclonehttps://github.com/mindspore-lab/sgl-mindspore.git
cdsgl-mindspore
pipinstall-e.
```

## Run Model[#](#run-model "Link to this heading")

Current SGLang-MindSpore supports Qwen3 and DeepSeek V3/R1 models. This doc uses Qwen3-8B as an example.

### Offline infer[#](#offline-infer "Link to this heading")

Use the following script for offline infer:

```
importsglangassgl

# Initialize the engine with MindSpore backend
llm = sgl.Engine(
    model_path="/path/to/your/model",  # Local model path
    device="npu",                      # Use NPU device
    model_impl="mindspore",            # MindSpore implementation
    attention_backend="ascend",        # Attention backend
    tp_size=1,                         # Tensor parallelism size
    dp_size=1                          # Data parallelism size
)

# Generate text
prompts = [
    "Hello, my name is",
    "The capital of France is",
    "The future of AI is"
]

sampling_params = {"temperature": 0, "top_p": 0.9}
outputs = llm.generate(prompts, sampling_params)

for prompt, output in zip(prompts, outputs):
    print(f"Prompt: {prompt}")
    print(f"Generated: {output['text']}")
    print("---")
```

### Start server[#](#start-server "Link to this heading")

Launch a server with MindSpore backend:

```
# Basic server startup
python3-msglang.launch_server\
--model-path/path/to/your/model\
--host0.0.0.0\
--devicenpu\
--model-implmindspore\
--attention-backendascend\
--tp-size1\
--dp-size1
```

For distributed server with multiple nodes:

```
# Multi-node distributed server
python3-msglang.launch_server\
--model-path/path/to/your/model\
--host0.0.0.0\
--devicenpu\
--model-implmindspore\
--attention-backendascend\
--dist-init-addr127.0.0.1:29500\
--nnodes2\
--node-rank0\
--tp-size4\
--dp-size2
```

## Troubleshooting[#](#troubleshooting "Link to this heading")

### Debug Mode[#](#debug-mode "Link to this heading")

Enable sglang debug logging by log-level argument.

```
python3-msglang.launch_server\
--model-path/path/to/your/model\
--host0.0.0.0\
--devicenpu\
--model-implmindspore\
--attention-backendascend\
--log-levelDEBUG
```

Enable mindspore info and debug logging by setting environments.

```
exportGLOG_v=1# INFO
exportGLOG_v=0# DEBUG
```

### Explicitly select devices[#](#explicitly-select-devices "Link to this heading")

Use the following environment variable to explicitly select the devices to use.

```
exportASCEND_RT_VISIBLE_DEVICES=4,5,6,7# to set device
```

### Some communication environment issues[#](#some-communication-environment-issues "Link to this heading")

In case of some environment with special communication environment, users need set some environment variables.

```
exportMS_ENABLE_LCCL=off# current not support LCCL communication mode in SGLang-MindSpore
```

### Some dependencies of protobuf[#](#some-dependencies-of-protobuf "Link to this heading")

In case of some environment with special protobuf version, users need set some environment variables to avoid binary version mismatch.

```
exportPROTOCOL_BUFFERS_PYTHON_IMPLEMENTATION=python# to avoid protobuf binary version mismatch
```

## Support[#](#support "Link to this heading")

For MindSpore-specific issues:

- Refer to the [MindSpore documentation](https://www.mindspore.cn/)