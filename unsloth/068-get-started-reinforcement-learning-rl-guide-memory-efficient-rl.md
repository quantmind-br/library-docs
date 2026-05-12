---
title: Memory Efficient RL
url: https://unsloth.ai/docs/get-started/reinforcement-learning-rl-guide/memory-efficient-rl.md
source: llms
fetched_at: 2026-04-27T18:13:18.528505512-03:00
rendered_js: false
word_count: 1678
summary: This document details the memory-efficient advancements in Unsloth for Reinforcement Learning (RL), highlighting features like increased context lengths, faster training runs, and the introduction of 'Unsloth Standby' to further reduce VRAM usage by smartly managing model weight sharing between inference and training modes.
tags:
    - memory-efficiency
    - reinforcement-learning
    - unsloth-standby
    - context-lengths
    - vram-optimization
    - rl-training
category: guide
optimized: true
optimized_at: 2026-04-27T21:40:00Z
---

# Memory Efficient RL

Algorithmic advancements for more efficient RL:

- **1.2–1.7x increased context lengths** — no slowdown, no extra memory
- **10% faster RL training** — revamped kernels + async data movements
- **2x faster `torch.compile`** times during model loading

Unsloth already increases RL speed, context window, and reduces VRAM 50–90% vs. all other FA2 setups. [[068-get-started-reinforcement-learning-rl-guide-memory-efficient-rl|Unsloth Standby]] improves this further — uniquely limits speed degradation, sometimes makes training faster.

Results: Qwen3-32B LoRA 16-bit 6,144 context vs. 3,600 (**1.7x**) on 1x H100 80GB. Llama-3.1-8B QLoRA 4bit 47,500 vs. 42,000 (1.13x).

Speedups from kernel optimizations, removing LoRA CPU↔GPU communication channel, custom `torch.compile` flags (vLLM rollout 10% faster, compile time 2x reduced).

## How to Enable Optimizations

Set `UNSLOTH_VLLM_STANDBY` before any Unsloth import, then `gpu_memory_utilization = 0.95`:

```python
import os
os.environ["UNSLOTH_VLLM_STANDBY"] = "1"

from unsloth import FastLanguageModel
import torch
model, tokenizer = FastLanguageModel.from_pretrained(
    model_name = "unsloth/Qwen3-8B-Base",
    max_seq_length = 2048, # Can increase for longer reasoning traces
    load_in_4bit = False, # False for LoRA 16bit
    fast_inference = True,
    max_lora_rank = 32, # Larger rank = smarter, but slower
    gpu_memory_utilization = 0.95,
)
```

## No More `gpu_memory_utilization` Tuning

Set `gpu_memory_utilization` to 90% or 95% and forget it. 100% won't work (space needed for small tensors). Previously had to tune 30%–95% — Unsloth handles it now.

## Why Does RL Use So Much Memory?

GRPO relies heavily on generation (vLLM), requiring constant GPU memory for weights, activations, and KV Cache.

<figure><img src="https://3215535692-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FxhOjnexMCB3dmuQFQ2Zq%2Fuploads%2Fgit-blob-7e25501083081b201d59f6000219cafa535d2b2d%2Fimage.png?alt=media" alt=""><figcaption></figcaption></figure>
<figure><img src="https://3215535692-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FxhOjnexMCB3dmuQFQ2Zq%2Fuploads%2Fgit-blob-189fd45a9e7a6fa1e98d1c9646b57bd0ec48481d%2Ffig6-2.avif?alt=media" alt=""><figcaption></figcaption></figure>

RL needs 2 VRAM sets on GPU simultaneously:

1. Inference engine (model weights + KV cache)
2. Training engine (model weights + activations + gradients + optimizer states)

Current frameworks split 50/50 on 80GB GPU — 40GB inference, 40GB training. Moving weights between modes is slow.

| 80GB GPU                                 | Inference (50%) | Training (50%) |
| ---------------------------------------- | --------------- | -------------- |
| Model Weights                            | 16GB            | 16GB           |
| KV Cache                                 | 24GB            |                |
| Activations, Gradients, Optimizer States |                 | 24GB           |

Unsloth shares vLLM's weight space directly — removes double memory for model weights, freeing ~16GB for longer context or faster generation, with no memory movements.

| 80GB GPU                                 | Inference (50%) | Training (50%) |
| ---------------------------------------- | --------------- | -------------- |
| Model Weights                            | **16GB SHARED** | **<<< SHARED** |
| KV Cache                                 | 24GB + 8GB = **32GB** |             |
| Activations, Gradients, Optimizer States |                 | 24GB + 8GB = **32GB** |

## Unsloth Standby

RL alternates inference → training → inference → training, so memory space can be reused since modes are separate.

<figure><img src="https://3215535692-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FxhOjnexMCB3dmuQFQ2Zq%2Fuploads%2Fgit-blob-6e9b6a2f7381de84ed6eeb0feedc566cd443acf3%2F5b957843-eb58-4778-8b90-f25767c51495.png?alt=media" alt=""><figcaption></figcaption></figure>

[vLLM sleep mode](https://docs.vllm.ai/en/latest/features/sleep_mode.html#rlhf-weight-updates) options:

1. `level = 1` — copies weights to CPU, deletes KV cache
2. `level = 2` — deletes weights and KV cache

Since Unsloth shares vLLM weight space, Unsloth Standby deletes KV cache while ignoring weight deletion:

| 80GB GPU                                 | Inference      | Training                                 |
| ---------------------------------------- | -------------- | ---------------------------------------- |
| Model Weights                            | **16GB SHARED** | **<<< SHARED**                          |
| **Multi-purpose 64GB space**             | KV Cache       | Activations, Gradients, Optimizer States |

Enable before any Unsloth import:

```python
import os
os.environ["UNSLOTH_VLLM_STANDBY"] = "1"
```

## Performance Experiments

GRPO needs **2 generations per prompt** to calculate sample mean/variance. With 1 generation, std dev = 0 and advantage `(reward - mean)/std` is undefined:

$$Z=\frac{r_i - \mu}{\sqrt{\frac{1}{n}\sum(r_i-\mu)^2}} \\ Z_{n=1}=\frac{r_1 - \mu}{\sqrt{\frac{1}{1}\sum(r_1-\mu)^2}}=\frac{0}{0}=\text{undefined}$$

Max context length of 6,144 for Qwen3-32B = 6,144 × 2 generations = 12,288 actual length.

<figure><img src="https://3215535692-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FxhOjnexMCB3dmuQFQ2Zq%2Fuploads%2Fgit-blob-2f83185e373186aa67bc2ce7d1814b2edb0f3ce6%2Foutput%20(10).png?alt=media" alt="" width="563"><figcaption></figcaption></figure>

Training time difference: <1% slowdown or slight speedup (margin of error). Speedups likely from reduced memory pressure → less CUDA memory allocator cleanup.

<figure><img src="https://3215535692-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FxhOjnexMCB3dmuQFQ2Zq%2Fuploads%2Fgit-blob-db26f62f9080dba942add171880537c3f516f065%2Fgpu%20mem%20cofigure.png?alt=media" alt=""><figcaption></figcaption></figure>

Standby on single T4 GPU (Qwen3-4B): vLLM `gpu_memory_utilization` can be set to **0.95** without affecting training — fits 32K length sequences vs. >2K previously (OOM).

| # | Config | Status | GPU Memory | Notes |
|---|--------|--------|------------|-------|
| 1 | [standby True, util 0.95, gen 2, grad_acc 2](https://colab.research.google.com/drive/18CssBY5C0mStnLvu2Hlt4aFLoPugRG0K?usp=sharing) | 40 steps / 40 min | 14.5 GiB | 32K KVCache with 2-4K chunks or 16K+16K |
| 2 | [standby True, util 0.9, gen 2, grad_acc 2](https://colab.research.google.com/drive/1q0TOUychygfreI2wKpg51sqnRhs5cYnX?usp=sharing) | 32 steps / 40 min | 13.8 GiB | ~28K KVCache with 2-4K chunks or 15K+15K |
| 3 | [standby False, util 0.9, gen 2, grad_acc 2](https://colab.research.google.com/drive/12Uw8y5beLzPtx11mCWCYyh9Z_PEHHdId?usp=sharing) | Model loads, can't train | OOM | batch_size=1 doesn't fit |
| 4 | [standby False, util 0.8, gen 2, grad_acc 2](https://colab.research.google.com/drive/1GwTlaP5CLsW-BcE1LqZWkz6S8VTWYdJ2?usp=sharing) | Model loads, can't train | OOM | batch_size=1 doesn't fit |
| 5 | [standby False, util 0.7, gen 2, grad_acc 2](https://colab.research.google.com/drive/1IuSUNzEBTiURK-vbTQuRDuUl0Ya2pz2t?usp=sharing) | 28 steps / 39 min | ~15.1 GiB | slightly longer input → OOM |
| 6 | [standby True, util 0.7, gen 2, grad_acc 2](https://colab.research.google.com/drive/1RY7HwpZ0luJT70OyLJ6zXKZQ2COdT9QJ?usp=sharing) | 29 steps / 40 min | 13 GiB (10-11GB typical) | 2 GiB (15%) saved at same config |

### H100 Experiments

| Model                | GPU                   | Seq Len | Num Generations | Grad Acc Steps |
| -------------------- | --------------------- | ------- | --------------- | -------------- |
| Qwen2.5-14B-Instruct | NVIDIA H100 80GB PCIe | 32,768  | 8               | 4              |

9 GiB peak memory difference (90% of time, GPU usage = peak). **For reference: TRL + LoRA can only fine-tune 8B model at context 1024 max (32x less).** Higher sequences OOM with similar config.

<details>
<summary>Click for Unsloth Standby Mode vs. no Standby Benchmarks</summary>

```
Standy mode enabled:

|===========================================================================|
|                  PyTorch CUDA memory summary, device ID 0                 |
|---------------------------------------------------------------------------|
|            CUDA OOMs: 0            |        cudaMalloc retries: 0         |
|===========================================================================|
|        Metric         | Cur Usage  | Peak Usage | Tot Alloc  | Tot Freed  |
|---------------------------------------------------------------------------|
| Allocated memory      |  32249 MiB |  43042 MiB | 128336 GiB | 128305 GiB |
|       from large pool |  31415 MiB |  42165 MiB | 127204 GiB | 127173 GiB |
|       from small pool |    834 MiB |   1184 MiB |   1132 GiB |   1131 GiB |
|---------------------------------------------------------------------------|
| Active memory         |  32249 MiB |  43042 MiB | 128336 GiB | 128305 GiB |
|       from large pool |  31415 MiB |  42165 MiB | 127204 GiB | 127173 GiB |
|       from small pool |    834 MiB |   1184 MiB |   1132 GiB |   1131 GiB |
|---------------------------------------------------------------------------|
| Requested memory      |  32199 MiB |  42987 MiB | 128176 GiB | 128145 GiB |
|       from large pool |  31364 MiB |  42110 MiB | 127047 GiB | 127016 GiB |
|       from small pool |    834 MiB |   1184 MiB |   1129 GiB |   1128 GiB |
|---------------------------------------------------------------------------|
| GPU reserved memory   |  37644 MiB |  47504 MiB | 705806 MiB | 668162 MiB |
|       from large pool |  36376 MiB |  46588 MiB | 682818 MiB | 646442 MiB |
|       from small pool |   1268 MiB |   1284 MiB |  22988 MiB |  21720 MiB |
|---------------------------------------------------------------------------|
| Non-releasable memory | 713142 KiB |   4633 MiB | 103206 GiB | 103205 GiB |
|       from large pool | 525312 KiB |   4594 MiB | 101923 GiB | 101922 GiB |
|       from small pool | 187830 KiB |    250 MiB |   1283 GiB |   1283 GiB |
|---------------------------------------------------------------------------|
| Allocations           |    3460    |    4809    |   15606 K  |   15603 K  |
|       from large pool |     395    |     563    |    2812 K  |    2811 K  |
|       from small pool |    3065    |    4270    |   12794 K  |   12791 K  |
|---------------------------------------------------------------------------|
| Active allocs         |    3460    |    4809    |   15606 K  |   15603 K  |
|       from large pool |     395    |     563    |    2812 K  |    2811 K  |
|       from small pool |    3065    |    4270    |   12794 K  |   12791 K  |
|---------------------------------------------------------------------------|
| GPU reserved segments |     913    |     920    |   13260    |   12347    |
|       from large pool |     279    |     305    |    1766    |    1487    |
|       from small pool |     634    |     642    |   11494    |   10860    |
|---------------------------------------------------------------------------|
| Non-releasable allocs |     422    |     628    |    4766 K  |    4765 K  |
|       from large pool |      66    |      92    |    1290 K  |   1289 KiB |
|       from small pool |     356    |     555    |    3476 K  |   3475 KiB |
|---------------------------------------------------------------------------|
| Oversize allocations  |       0    |       0    |       0    |       0    |
|---------------------------------------------------------------------------|
| Oversize GPU segments |       0    |       0    |       0    |       0    |
|===========================================================================|


Without Standby:

|===========================================================================|
|                  PyTorch CUDA memory summary, device ID 0                 |
|---------------------------------------------------------------------------|
|            CUDA OOMs: 0            |        cudaMalloc retries: 0         |
|===========================================================================|
|        Metric         | Cur Usage  | Peak Usage | Tot Alloc  | Tot Freed  |
|---------------------------------------------------------------------------|
| Allocated memory      |  32711 MiB |  52084 MiB | 142756 GiB | 142724 GiB |
|       from large pool |  31877 MiB |  51207 MiB | 141499 GiB | 141467 GiB |
|       from small pool |    834 MiB |   1184 MiB |   1257 GiB |   1256 GiB |
|---------------------------------------------------------------------------|
| Active memory         |  32711 MiB |  52084 MiB | 142756 GiB | 142724 GiB |
|       from large pool |  31877 MiB |  51207 MiB | 141499 GiB | 141467 GiB |
|       from small pool |    834 MiB |   1184 MiB |   1257 GiB |   1256 GiB |
|---------------------------------------------------------------------------|
| Requested memory      |  32572 MiB |  51658 MiB | 141898 GiB | 141866 GiB |
|       from large pool |  31738 MiB |  50780 MiB | 140644 GiB | 140613 GiB |
|       from small pool |    833 MiB |   1184 MiB |   1253 GiB |   1252 GiB |
|---------------------------------------------------------------------------|
| GPU reserved memory   |  49552 MiB |  52188 MiB |  86354 MiB |  36802 MiB |
|       from large pool |  48320 MiB |  51300 MiB |  84740 MiB |  36420 MiB |
|       from small pool |   1232 MiB |   1232 MiB |   1614 MiB |    382 MiB |
|---------------------------------------------------------------------------|
| Non-releasable memory |      0 B   |      0 B   |      0 B   |      0 B   |
|       from large pool |      0 B   |      0 B   |      0 B   |      0 B   |
|       from small pool |      0 B   |      0 B   |      0 B   |      0 B   |
|---------------------------------------------------------------------------|
| Allocations           |    3460    |    4809    |   17440 K  |   17437 K  |
|       from large pool |     395    |     564    |    2742 K  |   2741 K  |
|       from small pool |    3065    |    4270    |   14698 K  |   14695 K  |
|---------------------------------------------------------------------------|
| Active allocs         |    3460    |    4809    |   17440 K  |   17437 K  |
|       from large pool |     395    |     564    |    2742 K  |   2741 K  |
|       from small pool |    3065    |    4270    |   14698 K  |   14695 K  |
|---------------------------------------------------------------------------|
| GPU reserved segments |       0    |       0    |       0    |       0    |
|       from large pool |       0    |       0    |       0    |       0    |
|       from small pool |       0    |       0    |       0    |       0    |
|---------------------------------------------------------------------------|
| Non-releasable allocs |       0    |       0    |       0    |       0    |
|       from large pool |       0    |       0    |       0    |       0    |
|       from small pool |       0    |       0    |       0    |       0    |
|---------------------------------------------------------------------------|
| Oversize allocations  |       0    |       0    |       0    |       0    |
|---------------------------------------------------------------------------|
| Oversize GPU segments |       0    |       0    |       0    |       0    |
|===========================================================================|
```

</details>

Standby vs. non-standby training comparison (averaged over 3 runs): standby is sometimes faster, likely from reduced memory pressure.

<figure><img src="https://3215535692-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FxhOjnexMCB3dmuQFQ2Zq%2Fuploads%2Fgit-blob-2f285043ea8afa38d1082513e424662d8cd04b90%2Ftrainglobalstep.png?alt=media" alt=""><figcaption></figcaption></figure>

### Previous A100 40GB Experiments

A100 40GB, Qwen-2.5-3b-instruct, 8 generations/sample: without standby → 6K sequence lengths; with standby → 10K+. **TRL gives only 1K context at same batch size.**

<figure><img src="https://3215535692-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FxhOjnexMCB3dmuQFQ2Zq%2Fuploads%2Fgit-blob-c7cd807b5d513b04f5f3a6219bfcea0fb12e442a%2Fqwen3%20gpu%20mem.png?alt=media" alt="" width="563"><figcaption></figcaption></figure>

## Other Optimizations

- Better compilation flags, compile times reduced 50%+ (2 min → under 40 sec)
- Dynamic patching of any vLLM version for better `gc.collect` (inspired by [vLLM PR #21146](https://github.com/vllm-project/vllm/pull/21146))
- `combo_kernels` and `multi_kernel` flags don't work on vLLM 0.10 + Torch 2.8/2.9 nightly
- `coordinate_descent_tuning` made autotuning 13+ min with minimal gains (disabled)

## GRPO Notebooks

All GRPO notebooks have Standby on by default with all optimizations. See <https://docs.unsloth.ai/get-started/unsloth-notebooks> or try:

- [**Qwen3 (4B)**](https://colab.research.google.com/github/unslothai/notebooks/blob/main/nb/Qwen3_\(4B\)-GRPO.ipynb) — Advanced GRPO LoRA
- [**DeepSeek-R1-0528-Qwen3 (8B)**](https://colab.research.google.com/github/unslothai/notebooks/blob/main/nb/DeepSeek_R1_0528_Qwen3_\(8B\)_GRPO.ipynb) — multilingual
- [Gemma 3 (1B)](https://colab.research.google.com/github/unslothai/notebooks/blob/main/nb/Gemma3_\(1B\)-GRPO.ipynb)
- [Llama 3.2 (3B)](https://colab.research.google.com/github/unslothai/notebooks/blob/main/nb/Advanced_Llama3_2_\(3B\)_GRPO_LoRA.ipynb) — Advanced GRPO LoRA
- [Llama 3.1 (8B)](https://colab.research.google.com/github/unslothai/notebooks/blob/main/nb/Llama3.1_\(8B\)-GRPO.ipynb)
- [Phi-4 (14B)](https://colab.research.google.com/github/unslothai/notebooks/blob/main/nb/Phi_4_\(14B\)-GRPO.ipynb)
- [Mistral v0.3 (7B)](https://colab.research.google.com/github/unslothai/notebooks/blob/main/nb/Mistral_v0.3_\(7B\)-GRPO.ipynb)
- [Qwen2.5 (3B)](https://colab.research.google.com/github/unslothai/notebooks/blob/main/nb/Qwen2.5_\(3B\)-GRPO.ipynb)

---

# Agent Instructions: Querying This Documentation

If you need additional information not on this page, query dynamically via HTTP GET on the current page URL with the `ask` query parameter:

```
GET https://unsloth.ai/docs/get-started/reinforcement-learning-rl-guide/memory-efficient-rl.md?ask=<question>
```

The question should be specific, self-contained, and in natural language. The response contains a direct answer with relevant excerpts and sources.

#memory-efficiency #reinforcement-learning #unsloth-standby #vram-optimization
