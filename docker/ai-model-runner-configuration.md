---
title: Configuration options
url: https://docs.docker.com/ai/model-runner/configuration/
source: llms
fetched_at: 2026-01-24T14:14:12.051685611-03:00
rendered_js: false
word_count: 606
summary: This document explains how to configure Docker Model Runner settings, including context size, runtime flags, and performance parameters to optimize model behavior and resource usage.
tags:
    - docker-model-runner
    - llm-configuration
    - context-size
    - inference-performance
    - llama-cpp
    - vllm
    - docker-compose
category: configuration
---

Docker Model Runner provides several configuration options to tune model behavior, memory usage, and inference performance. This guide covers the key settings and how to apply them.

## [Context size (context length)](#context-size-context-length)

The context size determines the maximum number of tokens a model can process in a single request, including both the input prompt and generated output. This is one of the most important settings affecting memory usage and model capabilities.

### [Default context size](#default-context-size)

By default, Docker Model Runner uses a context size that balances capability with resource efficiency:

EngineDefault behaviorllama.cpp4096 tokensvLLMUses the model's maximum trained context size

> The actual default varies by model. Most models support between 2,048 and 8,192 tokens by default. Some newer models support 32K, 128K, or even larger contexts.

### [Configure context size](#configure-context-size)

You can adjust context size per model using the `docker model configure` command:

Or in a Compose file:

### [Context size guidelines](#context-size-guidelines)

Context sizeTypical use caseMemory impact2,048Simple queries, short code snippetsLow4,096Standard conversations, medium code filesModerate8,192Long conversations, larger code filesHigher16,384+Extended documents, multi-file contextHigh

> Larger context sizes require more memory (RAM/VRAM). If you experience out-of-memory errors, reduce the context size. As a rough guide, each additional 1,000 tokens requires approximately 100-500 MB of additional memory, depending on the model size.

### [Check a model's maximum context](#check-a-models-maximum-context)

To see a model's configuration including context size:

> The `docker model inspect` command shows the model's maximum supported context length (e.g., `gemma3.context_length`), not the configured context size. The configured context size is what you set with `docker model configure --context-size` and represents the actual limit used during inference, which should be less than or equal to the model's maximum supported context length.

Runtime flags let you pass parameters directly to the underlying inference engine. This provides fine-grained control over model behavior.

### [Using runtime flags](#using-runtime-flags)

Runtime flags can be provided through multiple mechanisms:

#### [Using Docker Compose](#using-docker-compose)

In a Compose file:

#### [Using Command Line](#using-command-line)

With the `docker model configure` command:

### [Common llama.cpp parameters](#common-llamacpp-parameters)

These are the most commonly used llama.cpp parameters. You don't need to look up the llama.cpp documentation for typical use cases.

#### [Sampling parameters](#sampling-parameters)

FlagDescriptionDefaultRange`--temp`Temperature for sampling. Lower = more deterministic, higher = more creative0.80.0-2.0`--top-k`Limit sampling to top K tokens. Lower = more focused401-100`--top-p`Nucleus sampling threshold. Lower = more focused0.90.0-1.0`--min-p`Minimum probability threshold0.050.0-1.0`--repeat-penalty`Penalty for repeating tokens1.11.0-2.0

**Example: Deterministic output (for code generation)**

**Example: Creative output (for storytelling)**

#### [Performance parameters](#performance-parameters)

FlagDescriptionDefaultNotes`--threads`CPU threads for generationAutoSet to number of performance cores`--threads-batch`CPU threads for batch processingAutoUsually same as `--threads``--batch-size`Batch size for prompt processing512Higher = faster prompt processing`--mlock`Lock model in memoryOffPrevents swapping, requires sufficient RAM`--no-mmap`Disable memory mappingOffMay improve performance on some systems

**Example: Optimized for multi-core CPU**

#### [GPU parameters](#gpu-parameters)

FlagDescriptionDefaultNotes`--n-gpu-layers`Layers to offload to GPUAll (if GPU available)Reduce if running out of VRAM`--main-gpu`GPU to use for computation0For multi-GPU systems`--split-mode`How to split across GPUslayerOptions: `none`, `layer`, `row`

**Example: Partial GPU offload (limited VRAM)**

#### [Advanced parameters](#advanced-parameters)

FlagDescriptionDefault`--rope-scaling`RoPE scaling methodAuto`--rope-freq-base`RoPE base frequencyModel default`--rope-freq-scale`RoPE frequency scaleModel default`--no-prefill-assistant`Disable assistant pre-fillOff`--reasoning-budget`Token budget for reasoning models0 (disabled)

### [vLLM parameters](#vllm-parameters)

When using the vLLM backend, different parameters are available.

Use `--hf_overrides` to pass HuggingFace model config overrides as JSON:

Here are complete configuration examples for common use cases.

### [Code completion (fast, deterministic)](#code-completion-fast-deterministic)

### [Chat assistant (balanced)](#chat-assistant-balanced)

### [Creative writing (high temperature)](#creative-writing-high-temperature)

### [Long document analysis (large context)](#long-document-analysis-large-context)

### [Low memory system](#low-memory-system)

You can also configure models via environment variables in containers:

VariableDescription`LLM_URL`Auto-injected URL of the model endpoint`LLM_MODEL`Auto-injected model identifier

See [Models and Compose](https://docs.docker.com/ai/compose/models-and-compose/) for details on how these are populated.

Configuration set via `docker model configure` persists until the model is removed. To reset configuration:

Using `-1` resets to the default value.

- [Inference engines](https://docs.docker.com/ai/model-runner/inference-engines/) - Learn about llama.cpp and vLLM
- [API reference](https://docs.docker.com/ai/model-runner/api-reference/) - API parameters for per-request configuration
- [Models and Compose](https://docs.docker.com/ai/compose/models-and-compose/) - Configure models in Compose applications