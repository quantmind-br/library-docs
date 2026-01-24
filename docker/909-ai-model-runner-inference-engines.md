---
title: Inference engines
url: https://docs.docker.com/ai/model-runner/inference-engines/
source: llms
fetched_at: 2026-01-24T14:14:20.071452192-03:00
rendered_js: false
word_count: 571
summary: This guide explains how to choose, configure, and manage the llama.cpp and vLLM inference engines within Docker Model Runner, detailing their hardware requirements and performance trade-offs.
tags:
    - docker-model-runner
    - inference-engines
    - llama-cpp
    - vllm
    - gpu-acceleration
    - model-deployment
    - gguf
    - safetensors
category: guide
---

Docker Model Runner supports two inference engines: **llama.cpp** and **vLLM**. Each engine has different strengths, supported platforms, and model format requirements. This guide helps you choose the right engine and configure it for your use case.

Featurellama.cppvLLM**Model formats**GGUFSafetensors, HuggingFace**Platforms**All (macOS, Windows, Linux)Linux x86\_64 only**GPU support**NVIDIA, AMD, Apple Silicon, VulkanNVIDIA CUDA only**CPU inference**YesNo**Quantization**Built-in (Q4, Q5, Q8, etc.)Limited**Memory efficiency**High (with quantization)Moderate**Throughput**GoodHigh (with batching)**Best for**Local development, resource-constrained environmentsProduction, high throughput

[llama.cpp](https://github.com/ggerganov/llama.cpp) is the default inference engine in Docker Model Runner. It's designed for efficient local inference and supports a wide range of hardware configurations.

### [Platform support](#platform-support)

PlatformGPU supportNotesmacOS (Apple Silicon)MetalAutomatic GPU accelerationWindows (x64)NVIDIA CUDARequires NVIDIA drivers 576.57+Windows (ARM64)Adreno OpenCLQualcomm 6xx series and laterLinux (x64)NVIDIA, AMD, VulkanMultiple backend optionsLinuxCPU onlyWorks on any x64/ARM64 system

### [Model format: GGUF](#model-format-gguf)

llama.cpp uses the GGUF format, which supports efficient quantization for reduced memory usage without significant quality loss.

#### [Quantization levels](#quantization-levels)

QuantizationBits per weightMemory usageQualityQ2\_K~2.5LowestReducedQ3\_K\_M~3.5MinimalAcceptableQ4\_K\_M~4.5LowGoodQ5\_K\_M~5.5ModerateExcellentQ6\_K~6.5HigherExcellentQ8\_08HighNear-originalF1616HighestOriginal

**Recommended**: Q4\_K\_M offers the best balance of quality and memory usage for most use cases.

#### [Pulling quantized models](#pulling-quantized-models)

Models on Docker Hub often include quantization in the tag:

### [Using llama.cpp](#using-llamacpp)

llama.cpp is the default engine. No special configuration is required:

To explicitly specify llama.cpp when running models:

### [llama.cpp API endpoints](#llamacpp-api-endpoints)

When using llama.cpp, API calls use the llama.cpp engine path:

Or without the engine prefix:

[vLLM](https://github.com/vllm-project/vllm) is a high-performance inference engine optimized for production workloads with high throughput requirements.

### [Platform support](#platform-support-1)

PlatformGPUSupport statusLinux x86\_64NVIDIA CUDASupportedWindows with WSL2NVIDIA CUDASupported (Docker Desktop 4.54+)macOS-Not supportedLinux ARM64-Not supportedAMD GPUs-Not supported

> vLLM requires an NVIDIA GPU with CUDA support. It does not support CPU-only inference.

### [Model format: Safetensors](#model-format-safetensors)

vLLM works with models in Safetensors format, which is the standard format for HuggingFace models. These models typically use more memory than quantized GGUF models but may offer better quality and faster inference on powerful hardware.

### [Setting up vLLM](#setting-up-vllm)

#### [Docker Engine (Linux)](#docker-engine-linux)

Install the Model Runner with vLLM backend:

Verify the installation:

#### [Docker Desktop (Windows with WSL2)](#docker-desktop-windows-with-wsl2)

1. Ensure you have:
   
   - Docker Desktop 4.54 or later
   - NVIDIA GPU with updated drivers
   - WSL2 enabled
2. Install vLLM backend:

### [Running models with vLLM](#running-models-with-vllm)

vLLM models are typically tagged with `-vllm` suffix:

To specify the vLLM backend explicitly:

### [vLLM API endpoints](#vllm-api-endpoints)

When using vLLM, specify the engine in the API path:

### [vLLM configuration](#vllm-configuration)

#### [HuggingFace overrides](#huggingface-overrides)

Use `--hf_overrides` to pass model configuration overrides:

#### [Common vLLM settings](#common-vllm-settings)

SettingDescriptionExample`max_model_len`Maximum context length8192`gpu_memory_utilization`Fraction of GPU memory to use0.9`tensor_parallel_size`GPUs for tensor parallelism2

### [vLLM and llama.cpp performance comparison](#vllm-and-llamacpp-performance-comparison)

ScenarioRecommended engineSingle user, local developmentllama.cppMultiple concurrent requestsvLLMLimited GPU memoryllama.cpp (with quantization)Maximum throughputvLLMCPU-only systemllama.cppApple Silicon Macllama.cppProduction deploymentvLLM (if hardware supports it)

You can run both llama.cpp and vLLM simultaneously. Docker Model Runner routes requests to the appropriate engine based on the model or explicit engine selection.

Check which engines are running:

### [Engine-specific API paths](#engine-specific-api-paths)

EngineAPI pathllama.cpp`/engines/llama.cpp/v1/...`vLLM`/engines/vllm/v1/...`Auto-select`/engines/v1/...`

### [Install an engine](#install-an-engine)

Options:

- `--backend`: `llama.cpp` or `vllm`
- `--gpu`: `cuda`, `rocm`, `vulkan`, or `metal` (depends on platform)

### [Reinstall an engine](#reinstall-an-engine)

### [Check engine status](#check-engine-status)

### [View engine logs](#view-engine-logs)

### [Package a GGUF model (llama.cpp)](#package-a-gguf-model-llamacpp)

### [Package a Safetensors model (vLLM)](#package-a-safetensors-model-vllm)

### [vLLM won't start](#vllm-wont-start)

1. Verify NVIDIA GPU is available:
2. Check Docker has GPU access:
3. Verify you're on a supported platform (Linux x86\_64 or Windows WSL2).

### [llama.cpp is slow](#llamacpp-is-slow)

1. Ensure GPU acceleration is working (check logs for Metal/CUDA messages).
2. Try a more aggressive quantization:
3. Reduce context size:

### [Out of memory errors](#out-of-memory-errors)

1. Use a smaller quantization (Q4 instead of Q8).
2. Reduce context size.
3. For vLLM, adjust `gpu_memory_utilization`:

<!--THE END-->

- [Configuration options](https://docs.docker.com/ai/model-runner/configuration/) - Detailed parameter reference
- [API reference](https://docs.docker.com/ai/model-runner/api-reference/) - API documentation
- [GPU support](https://docs.docker.com/desktop/features/gpu/) - GPU configuration for Docker Desktop