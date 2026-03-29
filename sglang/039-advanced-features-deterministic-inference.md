---
title: Deterministic Inference — SGLang
url: https://docs.sglang.io/advanced_features/deterministic_inference.html
source: crawler
fetched_at: 2026-02-04T08:46:58.727071614-03:00
rendered_js: false
word_count: 343
summary: This document explains how to achieve deterministic LLM inference using SGLang to ensure consistent outputs across different batch sizes and runs. It covers the technical causes of non-determinism, supported attention backends, and configuration steps for reproducible greedy and non-greedy sampling.
tags:
    - deterministic-inference
    - sglang
    - llm-serving
    - reproducibility
    - gpu-optimization
    - inference-configuration
category: guide
---

## Contents

## Deterministic Inference[#](#deterministic-inference "Link to this heading")

## Why Deterministic Inference Matters[#](#why-deterministic-inference-matters "Link to this heading")

Deterministic inference ensures consistent LLM outputs across runs, which is critical for:

- **Reinforcement Learning**: Ensures consistent logprobs across runs, reducing stochastic noise and making RL training more stable, reproducible, and debuggable.
- **Testing & Debugging**: Enables reproducible validation
- **Production**: Improves reliability and user experience

Even with `temperature=0`, standard LLM inference can produce different outputs due to dynamic batching and varying reduction orders in GPU kernels.

## The Root Cause of Non-Determinism[#](#the-root-cause-of-non-determinism "Link to this heading")

The main source is **varying batch sizes**. Different batch sizes cause GPU kernels to split reduction operations differently, leading to different addition orders. Due to floating-point non-associativity (`(a + b) + c ≠ a + (b + c)`), this produces different results even for identical inputs.

## SGLang’s Solution[#](#sglang-s-solution "Link to this heading")

Building on [Thinking Machines Lab’s batch-invariant operators](https://github.com/thinking-machines-lab/batch_invariant_ops), SGLang achieves fully deterministic inference while maintaining compatibility with chunked prefill, CUDA graphs, radix cache, and non-greedy sampling. The development roadmap for deterministic inference features can be found in this [issue](https://github.com/sgl-project/sglang/issues/10278).

### Supported Backends[#](#supported-backends "Link to this heading")

Deterministic inference is only supported with the following three attention backends: **FlashInfer**, **FlashAttention 3 (FA3)**, and **Triton**.

The following table shows feature compatibility for deterministic inference across different attention backends:

## Usage[#](#usage "Link to this heading")

### Basic Usage[#](#basic-usage "Link to this heading")

Enable deterministic inference by adding the `--enable-deterministic-inference` flag:

```
python3-msglang.launch_server\
--model-pathQwen/Qwen3-8B\
--attention-backendfa3\
--enable-deterministic-inference
```

### Server Arguments[#](#server-arguments "Link to this heading")

### Example Configurations[#](#example-configurations "Link to this heading")

#### Qwen3-8B[#](#qwen3-8b "Link to this heading")

```
python3-msglang.launch_server\
--model-pathQwen/Qwen3-8B\
--attention-backendflashinfer\
--enable-deterministic-inference
```

#### Llama Models[#](#llama-models "Link to this heading")

```
python3-msglang.launch_server\
--model-pathmeta-llama/Llama-3.1-8B-Instruct\
--attention-backendfa3\
--enable-deterministic-inference
```

#### Qwen3-30B-A3B (MoE Model)[#](#qwen3-30b-a3b-moe-model "Link to this heading")

```
python3-msglang.launch_server\
--model-pathQwen/Qwen3-30B-A3B\
--attention-backendfa3\
--enable-deterministic-inference
```

### Deterministic Inference with Non-Greedy Sampling (Temperature &gt; 0)[#](#deterministic-inference-with-non-greedy-sampling-temperature-0 "Link to this heading")

SGLang supports deterministic inference even with non-greedy sampling by using sampling seeds. This is particularly useful for reinforcement learning scenarios like GRPO (Group Relative Policy Optimization) where you need multiple diverse but reproducible responses.

#### Default Behavior[#](#default-behavior "Link to this heading")

By default, SGLang uses a sampling seed of `42` for reproducible sampling:

```
importrequests

response = requests.post(
    "http://localhost:30000/generate",
    json={
        "text": "Tell me a joke",
        "sampling_params": {
            "temperature": 0.8,  # Non-greedy sampling
            "max_new_tokens": 128,
        },
    },
)
print(response.json())
# This will always produce the same response across runs
```

#### Generating Multiple Reproducible Responses[#](#generating-multiple-reproducible-responses "Link to this heading")

To sample different responses from the same prompt while maintaining reproducibility (e.g., for GRPO training), provide different sampling seeds in your requests:

```
importrequests

# Prepare a list of sampling seeds for different responses
sampling_seeds = [42, 43, 44, 45, 46]

responses = []
for seed in sampling_seeds:
    response = requests.post(
        "http://localhost:30000/generate",
        json={
            "text": "Tell me a joke",
            "sampling_params": {
                "temperature": 0.8,
                "max_new_tokens": 128,
                "sampling_seed": seed,  # Specify sampling seed
            },
        },
    )
    responses.append(response.json())

# Each seed will produce a different but reproducible response
# Using the same seed will always produce the same response
```

This approach ensures that:

- Different seeds produce diverse responses
- The same seed always produces the same response across different runs
- Results are reproducible for debugging and evaluation

## Verification[#](#verification "Link to this heading")

Run deterministic tests to verify consistent outputs:

```
# Single test: same prompt, varying batch sizes
python3-msglang.test.test_deterministic--test-modesingle--n-trials50

# Prefix test: prompts with different prefix lengths
python3-msglang.test.test_deterministic--test-modeprefix--n-trials50

# Radix Cache Consistency mode: test radix cache determinism (cached vs uncached prefill)
python3-msglang.test.test_deterministic--test-moderadix_cache
```

Expected result: All tests should show `Unique samples: 1` (perfectly deterministic).