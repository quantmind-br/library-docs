---
title: FP8 Reinforcement Learning
url: https://unsloth.ai/docs/get-started/reinforcement-learning-rl-guide/fp8-reinforcement-learning.md
source: llms
fetched_at: 2026-04-27T18:13:12.207214202-03:00
rendered_js: false
word_count: 2012
summary: This document details the implementation and performance benefits of using FP8 precision for Reinforcement Learning (RL) training, demonstrating significant improvements in speed and VRAM efficiency across various models.
tags:
    - fp8-reinforcement-learning
    - llm-training
    - vram-optimization
    - inference-speedup
    - quantization-techniques
    - unsloth
category: tutorial
optimized: true
optimized_at: 2026-04-27T21:15:00Z
---

# FP8 Reinforcement Learning

FP8-precision training for RL, making FP8 GRPO possible on **consumer GPUs** (RTX 40, 50 etc). Qwen3-1.7B FP8 GRPO works on just **5GB VRAM**. Built with [TorchAO](https://github.com/pytorch/ao) from PyTorch — no accuracy loss.

**Key results:**
- **~1.4x faster** RL inference via [vLLM](https://github.com/vllm-project/vllm), 2x longer context vs BF16/FP16
- **60% less VRAM**, **10x longer** context than other FP8 RL implementations
- **Only framework** with FP8 RL LoRA on consumer GPUs (RTX 40/50, H100, H200, B200 etc.)
- Enable with `load_in_fp8 = True` in `FastLanguageModel`
- Qwen3-8B fits in 16GB VRAM, but free Colab T4 GPUs **don't support FP8** — notebooks use **24GB L4 GPUs** (fits Qwen3-14B)

**Notebooks:** [Qwen3-8B FP8 GRPO](https://colab.research.google.com/github/unslothai/notebooks/blob/main/nb/Qwen3_8B_FP8_GRPO.ipynb) | [Llama-3.2-1B FP8 GRPO](https://colab.research.google.com/github/unslothai/notebooks/blob/main/nb/Llama_FP8_GRPO.ipynb)

> [!tip] Unsloth now uses significantly less VRAM — details in an upcoming blog.

Uses Unsloth's [weight-sharing feature](https://unsloth.ai/docs/get-started/reinforcement-learning-rl-guide/memory-efficient-rl) for another **50% VRAM reduction**, enabling **10x more context** with no accuracy loss. Uses [vLLM](https://github.com/vllm-project/vllm) for fast inference, plus [Standby](https://unsloth.ai/docs/get-started/reinforcement-learning-rl-guide/memory-efficient-rl) and [Flex Attention](https://unsloth.ai/docs/models/gpt-oss-how-to-run-and-fine-tune/long-context-gpt-oss-training) for further VRAM reduction. TorchAO enables universal on-the-fly FP8 (Llama, Gemma, Mistral & more). Most FP8 models uploaded to Hugging Face (including Qwen3).

## FP8 vs BF16 Training

FP8 training largely matches BF16 accuracy. Serving in the same precision as training helps preserve accuracy. FP8 yields **1.6x higher throughput** on H100s and **2x lower memory usage** vs BF16.

### Weight scales & FP8 types

Quantized training stores low-precision weight (FP8) + higher-precision scale (FP16/BF16/FP32). Recovery: `original_weight ≈ quantized_weight * weight_scale`. More scales = better accuracy but more memory. [DeepSeek R1](https://arxiv.org/abs/2501.12948) mostly favors block quantization.

3 common FP8 types (per vLLM's [llm-compressor](https://github.com/vllm-project/llm-compressor)). Benchmarked on Qwen3-8B — **FP8 Block-Wise or Per-Channel (-FP8-Dynamic) is best** for accuracy + throughput.

| Type | Description | Throughput | MMLU Pro | GQPA Diamond |
|------|-------------|------------|----------|--------------|
| *(baseline)* | Bfloat16 | 11,367 | **62.04%** | 28.79% |
| Block-wise | Scales per block (128x128) | 12,041 | **62.37%** | **29.29%** |
| Per-Channel | 1 scale per row/column | 12,963 | 61.89% | **31.82%** |
| Per-Tensor | 1 scale for whole tensor | **13,681** | 61.83% | 27.78% |

## FP8 Performance Benchmarks

Unsloth FP8 RL inference via vLLM is generally **1.4x faster** than BF16. Speedup increases with model size.

### Accuracy / Training loss

Tested: Qwen3-4B/8B/14B, Llama 3.2 1B/3B, Qwen3-VL-2B/4B and more — all trained in BF16 and FP8. **SFT loss curves closely track each other.** For GRPO, reward plots match without diverging (occasional differences on larger models like Qwen3-14B).

## Inference = 96% of RL Training

In RL: call LLM/VLM to generate candidates, score each, reward good / penalize bad. Training must be minimal. Unsloth achieves **<4% training, 96% pure vLLM inference.**

Example: Qwen3-8B is 1.15x faster on shorter sequences. vLLM FP8 inference-only throughput is also 1.15x faster. Unsloth RL runs at 1.15x faster on tokens processed — **training overhead is negligible.**

## 60% Less Memory Usage

Memory savings roughly **equal model weight memory** (optimizer states and activations remain high-precision). Observed savings for LoRA fine-tuning:
- Qwen3-32B: **~30 GB saved**
- Qwen2.5-14B: **~14 GB saved**
- Qwen3-8B: **~8 GB saved**

BF16 LoRA on Qwen3-32B OOMed at higher batch sizes; **FP8 variant had no such issues** — larger batch sizes possible without OOM. Uses [memory-efficient-rl](https://unsloth.ai/docs/get-started/reinforcement-learning-rl-guide/memory-efficient-rl) weight-sharing in the FP8 domain.

| 80GB GPU | Inference Engine | Training Engine |
|----------|-----------------|-----------------|
| Model Weights | **8GB SHARED FP8** | **<<< SHARED** |
| **72GB multi-purpose space** | KV Cache | Activations, Gradients, Optimizer States |

Enable [Unsloth Standby](https://unsloth.ai/docs/get-started/reinforcement-learning-rl-guide/memory-efficient-rl) for FP8/BF16 RL — add before any Unsloth import:

```python
import os
os.environ["UNSLOTH_VLLM_STANDBY"] = "1"
```

## How to Use FP8 RL / Installation

Update Unsloth or install in a new virtual environment for H100, L4, RTX 50x, RTX 40x, H200, B200, and any NVIDIA GPU after RTX 4090.

Update: `pip install --upgrade --force-reinstall --no-cache-dir --no-deps unsloth unsloth_zoo`

New environment:

```bash
python -m venv unsloth_env
source unsloth_env/bin/activate

pip install unsloth vllm
pip install --pre torchao --index-url https://download.pytorch.org/whl/nightly/cu128 --force-reinstall
pip install --pre fbgemm-gpu fbgemm-gpu-genai --index-url https://download.pytorch.org/whl/nightly/cu128 --force-reinstall
pip install --upgrade numba numpy
```

Use `load_in_fp8 = True` — Unsloth auto-maps to Float8 variant or converts on the fly:

```python
import os
os.environ['UNSLOTH_VLLM_STANDBY'] = "1" # Unsloth standby saves 30%+ memory for RL
from unsloth import FastLanguageModel
import torch
max_seq_length = 2048 # Can increase for longer reasoning traces
lora_rank = 32 # Larger rank = smarter, but slower
model, tokenizer = FastLanguageModel.from_pretrained(
    model_name = "unsloth/Qwen3-8B",
    max_seq_length = max_seq_length,
    load_in_4bit = False, # False for LoRA 16bit
    fast_inference = True, # Enable vLLM fast inference
    max_lora_rank = lora_rank,
    load_in_fp8 = True, # Float8 RL / GRPO!
)
```

## Implementing FP8 Training

Initial approach using `transformers` FP8 (block-quantized matmul) was **4x slower** than BF16 on H100. Switched to TorchAO collaboration.

### TorchAO Collab

Collaborated with [TorchAO](https://github.com/pytorch/ao) team (especially [Andrew](https://github.com/unslothai/unsloth/pull/3440)):

- Frozen LoRA weights stored in **FP8**
- Forward pass: **dynamic FP8 quantization** on input activations; trainable LoRA adapters in **BF16**
- FP8 weights share buffers with vLLM model weights — **single FP8 copy** in memory (no double-model overhead)
- Backward pass: dequantize LoRA weights; gradient computation in **BF16** for accuracy

Works across all supported RL algorithms: [GSPO](https://unsloth.ai/docs/get-started/reinforcement-learning-rl-guide/advanced-rl-documentation/gspo-reinforcement-learning), Dr. GRPO, PPO, DPO.

TorchAO provides PyTorch-native FP8 for training/inference with tensorwise, row-wise, and 128x128 blockwise scaling. Up to [1.64x inference throughput](https://huggingface.co/pytorch/gemma-3-27b-it-FP8/blob/main/README.md#results-h100-machine) at 27B scale with row-wise. See [TorchAO FP8 README](https://github.com/pytorch/ao/blob/main/torchao/float8/README.md).

### TorchAO's block-quantized FP8 matmul

Initial default: **80% of BF16 throughput** without degrading loss/stability. Now defaults to **FBGEMM's implementation** (if GPU supports it). Unsloth auto-selects the best backend based on installed packages. DeepSeek's DeepGEMM was experimented with but not fully integrated.

### On-the-fly TorchAO FP8 quantization

Quantize during model load time — no need to pre-quantize yourself. Set `load_in_fp8 = True` (or `"block"` for block FP8):

```python
from unsloth import FastLanguageModel
fp8_model = FastLanguageModel.from_pretrained(
    "unsloth/Llama-3.3-70B-Instruct", # Can be any model name!
    load_in_fp8 = True, # "block" for block FP8, True for row FP8, False
)
```

## Unsloth FP8 Uploads

FP8 Dynamic and FP8 Block models uploaded to Hugging Face for training or serving via [[090-basics-inference-and-deployment-vllm-guide|vLLM]]/[[088-basics-inference-and-deployment-sglang-guide|SGLang]]. FP8 Dynamic: slightly faster training, lower VRAM, small accuracy trade-off vs FP8 Block. Full list: [[114-get-started-unsloth-model-catalog|Unsloth Model Catalog]].

| Model | FP8 Uploads |
|-------|-------------|
| **Qwen3 (2507)** | 4B Instruct [FP8](https://huggingface.co/unsloth/Qwen3-4B-Instruct-2507-FP8), 4B Thinking [FP8](https://huggingface.co/unsloth/Qwen3-4B-Thinking-2507-FP8), 30B-A3B Instruct [FP8](https://huggingface.co/unsloth/Qwen3-30B-A3B-Instruct-2507-FP8), 30B-A3B Thinking [FP8](https://huggingface.co/unsloth/Qwen3-30B-A3B-Thinking-2507-FP8) |
| **Qwen3-VL** | 4B Instruct [FP8](https://huggingface.co/unsloth/Qwen3-VL-4B-Instruct-FP8), 4B Thinking [FP8](https://huggingface.co/unsloth/Qwen3-VL-4B-Thinking-FP8), 8B Instruct [FP8](https://huggingface.co/unsloth/Qwen3-VL-8B-Instruct-FP8), 8B Thinking [FP8](https://huggingface.co/unsloth/Qwen3-VL-8B-Thinking-FP8) |
| **Llama 3.1** | 8B Instruct [Dynamic](https://huggingface.co/unsloth/Llama-3.1-8B-Instruct-FP8-Dynamic) / [Block](https://huggingface.co/unsloth/Llama-3.1-8B-Instruct-FP8-Block), 8B Base [Dynamic](https://huggingface.co/unsloth/Llama-3.1-8B-FP8-Dynamic) / [Block](https://huggingface.co/unsloth/Llama-3.1-8B-FP8-Block), 70B [Dynamic](https://huggingface.co/unsloth/Llama-3.1-70B-FP8-Dynamic) / [Block](https://huggingface.co/unsloth/Llama-3.1-70B-FP8-Block) |
| **Qwen3** | 0.6B [FP8](https://huggingface.co/unsloth/Qwen3-0.6B-FP8), 1.7B [FP8](https://huggingface.co/unsloth/Qwen3-1.7B-FP8), 4B [FP8](https://huggingface.co/unsloth/Qwen3-4B-FP8), 8B [FP8](https://huggingface.co/unsloth/Qwen3-8B-FP8), 14B [FP8](https://huggingface.co/unsloth/Qwen3-14B-FP8), 32B [FP8](https://huggingface.co/unsloth/Qwen3-32B-FP8) |
| **Llama 3.3** | 70B [Dynamic](https://huggingface.co/unsloth/Llama-3.3-70B-Instruct-FP8-Dynamic) / [Block](https://huggingface.co/unsloth/Llama-3.3-70B-Instruct-FP8-Block) |
| **Llama 3.2** | 1B Base [Dynamic](https://huggingface.co/unsloth/Llama-3.2-1B-FP8-Dynamic) / [Block](https://huggingface.co/unsloth/Llama-3.2-1B-FP8-Block), 1B Instruct [Dynamic](https://huggingface.co/unsloth/Llama-3.2-1B-Instruct-FP8-Dynamic) / [Block](https://huggingface.co/unsloth/Llama-3.2-1B-Instruct-FP8-Block), 3B Base [Dynamic](https://huggingface.co/unsloth/Llama-3.2-3B-FP8-Dynamic) / [Block](https://huggingface.co/unsloth/Llama-3.2-3B-FP8-Block), 3B Instruct [Dynamic](https://huggingface.co/unsloth/Llama-3.2-3B-Instruct-FP8-Dynamic) / [Block](https://huggingface.co/unsloth/Llama-3.2-3B-Instruct-FP8-Block) |
| **Granite 4.0** | h-tiny [FP8 Dynamic](https://huggingface.co/unsloth/granite-4.0-h-tiny-FP8-Dynamic), h-small [FP8 Dynamic](https://huggingface.co/unsloth/granite-4.0-h-small-FP8-Dynamic) |
| **Magistral Small** | [FP8 Dynamic](https://huggingface.co/unsloth/Magistral-Small-2509-FP8-Dynamic), [FP8 torchao](https://huggingface.co/unsloth/Magistral-Small-2509-FP8-torchao) |
| **Mistral Small 3.2** | [FP8](https://huggingface.co/unsloth/Mistral-Small-3.2-24B-Instruct-2506-FP8) |
| **Gemma 3** | 270m [FP8](https://huggingface.co/unsloth/gemma-3-270m-it-FP8-Dynamic), 1B [FP8](https://huggingface.co/unsloth/gemma-3-1b-it-FP8-Dynamic), 4B [FP8](https://huggingface.co/unsloth/gemma-3-4b-it-FP8-Dynamic), 12B [FP8](https://huggingface.co/unsloth/gemma-3-12B-it-FP8-Dynamic), 27B [FP8](https://huggingface.co/unsloth/gemma-3-27b-it-FP8-Dynamic) |

## Acknowledgements

PyTorch and TorchAO team: Andrew Or, Jerry Zhang, Supriya Rao, Scott Roy, Mergen Nachin. Also the Executorch team.

---

# Agent Instructions: Querying This Documentation

For info not on this page, query dynamically:

```
GET https://unsloth.ai/docs/get-started/reinforcement-learning-rl-guide/fp8-reinforcement-learning.md?ask=<question>
```

Specific, self-contained natural language question. Returns direct answer with excerpts and sources.

#fp8-reinforcement-learning #vram-optimization #quantization #rl-training
