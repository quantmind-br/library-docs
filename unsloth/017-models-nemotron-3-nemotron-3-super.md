---
title: 'NVIDIA Nemotron-3-Super: How To Run Guide'
url: https://unsloth.ai/docs/models/nemotron-3/nemotron-3-super.md
source: llms
fetched_at: 2026-04-27T18:13:42.827069919-03:00
rendered_js: false
word_count: 806
summary: This guide explains how to run, fine-tune, and deploy the NVIDIA Nemotron-3-Super-120B model using various methods like GGUF/llama.cpp, direct Hugging Face download, and llama-server for production.
tags:
    - nemotron-3-super
    - llm-guide
    - gguf-runner
    - local-inference
    - model-deployment
    - fine-tuning
category: tutorial
optimized: true
optimized_at: 2026-04-27T21:42:00Z
---

# NVIDIA Nemotron-3-Super: How To Run Guide

NVIDIA Nemotron-3-Super-120B-A12B: 120B hybrid reasoning MoE, 12B active, 1M-token context window. Leads its size class on AIME 2025, Terminal Bench, SWE-Bench Verified. Runs on 64GB RAM/VRAM/unified memory. See also [[018-models-nemotron-3|Nemotron-3-Nano]] (30B counterpart).

GGUF: [Nemotron-3-Super-120B-A12B-GGUF](https://huggingface.co/unsloth/NVIDIA-Nemotron-3-Super-120B-A12B-GGUF) | [NVFP4](https://huggingface.co/unsloth/NVIDIA-Nemotron-3-Super-120B-A12B-NVFP4) | [FP8](https://huggingface.co/unsloth/NVIDIA-Nemotron-3-Super-120B-A12B-FP8) | [BF16](https://huggingface.co/unsloth/NVIDIA-Nemotron-3-Super-120B-A12B)

## Usage Guide

### Recommended Inference Settings

| Use-case | `temperature` | `top_p` |
|----------|---------------|---------|
| General chat/instruction | 1.0 | 1.0 |
| Tool calling | 0.6 | 0.95 |

- `max_new_tokens`: 32,768 to 262,144 (max 1M); increase for deep reasoning as RAM/VRAM allows

> [!info] Model uses NoPE (No Positional Embeddings). Only change `max_position_embeddings`; YaRN is not needed.

### Chat Template

```python
tokenizer.apply_chat_template([
    {"role" : "user", "content" : "What is 1+1?"},
    {"role" : "assistant", "content" : "2"},
    {"role" : "user", "content" : "What is 2+2?"}
    ], add_generation_prompt = True, tokenize = False,
)
```

> [!info] Nemotron 3 uses `💭` (token ID 12) and `👍` (token ID 13) for reasoning. Use `--special` and `--verbose-prompt` in llama.cpp to see them.

Chat template format:

```
<|im_start|>system\n<|im_end|>\n<|im_start|>user\nWhat is 1+1?<|im_end|>\n<|im_start|>assistant\n💭👍2<|im_end|>\n<|im_start|>user\nWhat is 2+2?<|im_end|>\n<|im_start|>assistant\n💭\n
```

## Run Nemotron-3-Super-120B-A12B

Memory requirements: 4-bit ~64-72GB RAM, 8-bit 128GB. Some GGUFs are similar in size because architecture dimensions aren't divisible by 128, preventing lower-bit quantization on some parts.

### llama.cpp Tutorial

1. **Build** llama.cpp (set `-DGGML_CUDA=OFF` for CPU-only or Apple Metal):

```bash
apt-get update
apt-get install pciutils build-essential cmake curl libcurl4-openssl-dev -y
git clone https://github.com/ggml-org/llama.cpp
cmake llama.cpp -B llama.cpp/build \
    -DBUILD_SHARED_LIBS=OFF -DGGML_CUDA=ON
cmake --build llama.cpp/build --config Release -j --clean-first --target llama-cli llama-mtmd-cli llama-server llama-gguf-split
cp llama.cpp/build/bin/llama-* llama.cpp
```

2. **Run from HF**:

General instruction:

```bash
./llama.cpp/llama-cli \
    -hf unsloth/NVIDIA-Nemotron-3-Super-120B-A12B-GGUF:UD-Q4_K_XL \
    --ctx-size 16384 \
    --temp 1.0 --top-p 1.0
```

Tool-calling:

```bash
./llama.cpp/llama-cli \
    -hf unsloth/NVIDIA-Nemotron-3-Super-120B-A12B-GGUF:UD-Q4_K_XL \
    --ctx-size 32768 \
    --temp 0.6 --top-p 0.95
```

3. **Download** (`pip install huggingface_hub hf_transfer`):

```bash
hf download unsloth/NVIDIA-Nemotron-3-Super-120B-A12B-GGUF \
    --local-dir unsloth/NVIDIA-Nemotron-3-Super-120B-A12B-GGUF \
    --include "*UD-Q4_K_XL*" # Use "*UD-Q2_K_XL*" for Dynamic 2bit
```

4. **Conversation mode** (adjust context as needed; >256K may trigger CUDA OOM):

```bash
/llama.cpp/llama-cli \
    --model unsloth/NVIDIA-Nemotron-3-Super-120B-A12B-GGUF/UD-Q4_K_XL/NVIDIA-Nemotron-3-Super-120B-A12B-UD-Q4_K_XL-00001-of-00003.gguf \
    --ctx-size 16384 \
    --seed 3407 \
    --prio 2 \
    --temp 0.6 \
    --top-p 0.95
```

## Fine-tuning Nemotron 3 and RL

All Nemotron models supported. For Nano examples, see [[018-models-nemotron-3|Nemotron 3 Nano guide]].

- Router-layer fine-tuning disabled by default for stability
- bf16 LoRA works on 256GB VRAM; for multi-GPU add `device_map = "balanced"` or see [[093-basics-multi-gpu-training-with-unsloth|Multi-GPU Guide]]

## llama-server Serving & Deployment

Deploy via `llama-server`:

```bash
./llama.cpp/llama-server \
    --model unsloth/NVIDIA-Nemotron-3-Super-120B-A12B-GGUF/UD-Q4_K_XL/NVIDIA-Nemotron-3-Super-120B-A12B-UD-Q4_K_XL-00001-of-00003.gguf \
    --alias "unsloth/NVIDIA-Nemotron-3-Super-120B-A12B" \
    --prio 3 \
    --min_p 0.01 \
    --temp 0.6 \
    --top-p 0.95 \
    --ctx-size 16384 \
    --port 8001
```

With `pip install openai`:

```python
from openai import OpenAI
import json
openai_client = OpenAI(
    base_url = "http://127.0.0.1:8001/v1",
    api_key = "sk-no-key-required",
)
completion = openai_client.chat.completions.create(
    model = "unsloth/NVIDIA-Nemotron-3-Super-120B-A12B",
    messages = [{"role": "user", "content": "What is 2+2?"},],
)
print(completion.choices[0].message.reasoning_content)
print(completion.choices[0].message.content)
```

## Benchmarks

Competitive accuracy vs similar-sized models with highest throughput.

#nemotron-3-super #local-inference #gguf-runner #model-deployment #fine-tuning
