---
title: gpt-oss Reinforcement Learning
url: https://unsloth.ai/docs/models/gpt-oss-how-to-run-and-fine-tune/gpt-oss-reinforcement-learning.md
source: llms
fetched_at: 2026-04-27T18:13:50.005853316-03:00
rendered_js: false
word_count: 1795
summary: This document details how Unsloth allows for training OpenAI's gpt-oss model using Reinforcement Learning (RL) with GRPO, showcasing significant performance benefits like faster inference and reduced VRAM usage compared to other implementations.
tags:
    - gpt-oss
    - reinforcement-learning
    - unsloth
    - grpo
    - inference-speed
    - flex-attention
category: guide
optimized: true
optimized_at: 2026-04-27T21:30:00Z
---

# gpt-oss Reinforcement Learning

Unsloth trains [gpt-oss](https://unsloth.ai/docs/models/gpt-oss-how-to-run-and-fine-tune) with RL and GRPO, delivering the fastest inference (3x), lowest VRAM (50% less), and longest context (8x) for gpt-oss RL vs. any implementation -- with no accuracy degradation.

Since RL on gpt-oss is not yet vLLM compatible, Unsloth rewrote inference from Transformers to achieve ~21 tokens/s (4-bit) and ~30 tokens/s (BF16). gpt-oss-20b trains with GRPO on 15GB VRAM (free on Colab). gpt-oss-120b fits on 120GB VRAM GPUs.

**Free notebook:** [gpt-oss-20b GRPO Colab](https://colab.research.google.com/github/unslothai/notebooks/blob/main/nb/gpt-oss-\(20B\)-GRPO.ipynb) -- auto-creates faster matrix multiplication kernels, uses 4 Unsloth reward functions, and shows how to [[#can-we-counter-reward-hacking|counteract reward-hacking]].

**Key capabilities:**

- **4-bit RL** -- only framework supporting 4-bit RL for gpt-oss
- **Embedding offloading** via `offload_embeddings` (~1GB savings)
- Works on **any** GPU: A100, H100, and old T4's
- Performance from [[068-get-started-reinforcement-learning-rl-guide-memory-efficient-rl|weight sharing]], [[011-models-gpt-oss-how-to-run-and-fine-tune-long-context-gpt-oss-training|Flex Attention]], [[068-get-started-reinforcement-learning-rl-guide-memory-efficient-rl|Standby]], and custom kernels

> [!warning] Flash Attention 3 (FA3) is unsuitable for gpt-oss training
> FA3 does not support the backward pass for attention sinks, causing incorrect training losses ([Issue 1797](https://github.com/Dao-AILab/flash-attention/issues/1797)). If not using Unsloth, FA3 may be enabled by default -- double-check. Disabling FA3 incurs O(N^2) memory usage; Unsloth is the only RL framework offering O(N) memory usage via Flex Attention.

## Making Inference Much Faster

Inference is crucial in RL (generate candidate solutions before maximizing reward; see [[072-get-started-reinforcement-learning-rl-guide|RL guide]]). Unsloth rewrote Transformers inference code and integrated custom algorithms including [[011-models-gpt-oss-how-to-run-and-fine-tune-long-context-gpt-oss-training|Flex Attention]] and special `torch.compile` flags (combo kernels). Evaluated against an already 2x-optimized baseline.

**Why not vLLM:** Lacks BF16 training and LoRA support for gpt-oss. Without Unsloth, only full-precision BF16 works (800%+ more memory). Most frameworks enable FA3 by default which causes incorrect training loss. Without FA3, naive attention balloons to O(N^2).

**Benchmark results:** Unsloth 4-bit inference is ~4x faster; BF16 is also more efficient especially in VRAM use.

## gpt-oss Flex Attention Issues and Quirks

Attention sinks were reimplemented (see [[011-models-gpt-oss-how-to-run-and-fine-tune-long-context-gpt-oss-training|long-context training]]) to allow generation with left padding. The approach: get the logsumexp and apply sigmoid to alter attention weights:

$$
A(X) = \sigma \bigg( \frac{1}{\sqrt{d}}QK^T \bigg)V \\

A(X) = \frac{\exp{\frac{1}{\sqrt{d}}QK^T}}{\sum{\exp{\frac{1}{\sqrt{d}}QK^T}}}V \\

\text{LSE} = \log{\sum{\exp{\frac{1}{\sqrt{d}}QK^T}}} \\

A\_{sinks}(X) = A(X) \odot \sigma (\text{LSE} - \text{sinks})
$$

### Left Padding and KV Cache Masking

Left-padded masking during inference was tricky. Must account for KV Cache prefill during generation and unique pad token counts per prompt in batch generations, changing how the block mask is stored.

**Normal causal mask:**

```
   k0 k1 k2 k3 k4   <-- keys
q0  X
q1  X  X
q2  X  X  X
q3  X  X  X  X
q4  X  X  X  X  X   <-- last query row (most important for decoding)
```

**Inference (decoding) -- only last row matters:**

```
    k0 k1 k2 k3 k4
q0
q1
q2
q3
q4   X  X  X  X  X
```

**Naive masking fails** -- single query has index 0 while n_k key tokens exist, so `q_idx >= k_idx` fails. Need an offset in mask creation, but naive offsets change each step (forcing mask and kernel regeneration). Solved with cache and compile optimizations.

**Batch generation** is harder: sequences differ in length, padding complicates mask creation, Flex Attention dynamic masks are tricky. Without `torch.compile`, it falls back to eager attention (slow, memory-heavy: O(N^2) vs O(N)).

> You need to call `flex_attention` with `_compile=True`. Without compile, the full Q_LEN x KV_LEN matrix must be materialized, causing OOMs on long sequences. Also run `flex_attention = torch.compile(flex_attention)` -- without compile, flex falls back to a non-fused eager implementation that is much slower and materializes the full scores matrix.
> -- [meta-pytorch/attention-gym#15](https://github.com/meta-pytorch/attention-gym/issues/15#issuecomment-2284148665)

**Requirements for the mask:** dynamically handle prefill vs decode with KV Cache, batch and padding tokens per sequence, remain `torch.compile` friendly, support sliding windows.

### Flash Attention Investigation

Attempted to integrate Flash Attention (operating solely on attention output and logsumexp). First few layers behaved as expected, but layers 18-24 diverged significantly from eager-mode transformers. The discrepancy is not error accumulation (identical inputs at every layer). Also compared against Unsloth FlexAttention -- same divergence. Under investigation.

> [!danger] FA3 does not support backward pass for attention sinks
> FA3 is often enabled by default in most training packages (not Unsloth). Using FA3 makes gpt-oss training loss completely wrong. Many users are unaware -- be cautious.

## Can We Counter Reward Hacking?

RL maximizes reward but can cheat by learning tricks that increase reward without actually performing the task. Examples: models that modify unit tests to pass coding challenges. See [[110-get-started-reinforcement-learning-rl-guide-advanced-rl-documentation-rl-reward-hacking|RL Reward Hacking]] for more examples.

The [free gpt-oss RL notebook](https://colab.research.google.com/github/unslothai/notebooks/blob/main/nb/gpt-oss-\(20B\)-GRPO.ipynb) explores countering reward hacking in code generation -- the model was observed editing timing functions, outsourcing to libraries, caching results, and outright cheating. After countering, the model generates genuinely optimized matrix multiplication kernels.

### Common Reward Hacking Patterns

- **Laziness** -- RL calls optimized CUDA kernels via NumPy/Torch. Fix: inspect generated code for non-stdlib Python library imports.
- **Caching and cheating** -- RL caches results or inspects Python globals. Fix: wipe cache with a large fake matrix; benchmark carefully with multiple loops and turns.
- **Cheating** -- RL edits the timing function to output 0 time. Fix: restrict `locals` and `globals`; use `exec` with empty dict output; disallow global access via `types.FunctionType(f.__code__, {})`.

## Tutorial: How to Train gpt-oss with RL

Full step-by-step tutorial: [[009-models-gpt-oss-how-to-run-and-fine-tune-gpt-oss-reinforcement-learning-tutorial-how-to-train-gpt-oss-with-rl|How to Train gpt-oss with RL]].

**Overview:** Train gpt-oss-20b to autonomously win 2048 using GRPO and Unsloth.

| Resource | Link |
|---|---|
| 2048 notebook (Official OpenAI) | [Colab](https://colab.research.google.com/github/openai/gpt-oss/blob/main/examples/reinforcement-fine-tuning.ipynb) |
| Kernel generation notebook (Unsloth) | [Colab](https://colab.research.google.com/github/unslothai/notebooks/blob/main/nb/gpt-oss-\(20B\)-GRPO.ipynb) |

**What you'll build:**

1. Train gpt-oss-20b to automatically win 2048
2. Create a minimal 2048 environment the model can interact with
3. Define reward functions: compilation check, anti-cheat, game success
4. Run inference and export (MXFP4 4-bit or merged FP16)

> [!info] Hardware
> The 2048 example runs on a free Colab T4 (slow). A100/H100 is much faster. 4-bit loading + LoRA fits a 20B model into modest VRAM.

#reinforcement-learning #grpo #gpt-oss #flex-attention #unsloth
