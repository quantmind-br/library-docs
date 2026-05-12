---
title: 'Qwen3-Next: Run Locally Guide'
url: https://unsloth.ai/docs/models/tutorials/qwen3-next.md
source: llms
fetched_at: 2026-04-27T18:14:19.185705766-03:00
rendered_js: false
word_count: 1072
summary: This guide explains how to run and optimally configure the Qwen3-Next 80B MoE model variants (Instruct and Thinking) locally using tools like Llama.cpp, detailing best practices for various inference settings.
tags:
    - qwen3-next
    - model-guide
    - local-inference
    - llm-usage
    - instruct-variant
    - thinking-mode
category: guide
optimized: true
optimized_at: 2026-04-27T21:30:00Z
---

# Qwen3-Next: Run Locally Guide

80B MoE released Sept 2025 with Thinking and Instruct variants. Hybrid architecture (MoEs + Gated DeltaNet + Gated Attention) optimized for fast inference on long contexts. 256K context window, **10x faster inference than Qwen3-32B**.

GGUF repos: [Instruct](https://huggingface.co/unsloth/Qwen3-Next-80B-A3B-Instruct-GGUF) | [Thinking](https://huggingface.co/unsloth/Qwen3-Next-80B-A3B-Thinking-GGUF)

Related: [[047-models-tutorials-qwen3-how-to-run-and-fine-tune|Qwen3]]

## Recommended Settings

> [!note] Updated Dec 6, 2025: Unsloth Qwen3-Next GGUFs now include iMatrix.

| Setting | Instruct | Thinking |
|---|---|---|
| **Temperature** | `0.7` | `0.6` |
| Min_P | `0.00` (llama.cpp default is 0.1) | `0.00` |
| **Top_P** | `0.80` | `0.95` |
| TopK | `20` | `20` |
| presence_penalty | `0.0`–`2.0` (try 1.0 to reduce repetition) | `0.0`–`2.0` |

- **Output length**: 32,768 tokens (Thinking), 16,384 tokens (Instruct). Increase for Thinking if needed.
- **Context**: supports 262,144 natively; set 32,768 for less RAM.

### Chat Template (both variants)

```
<|im_start|>user
Hey there!<|im_end|>
<|im_start|>assistant
What is 1+1?<|im_end|>
<|im_start|>user
2<|im_end|>
<|im_start|>assistant
```

## Run Qwen3-Next-80B-A3B-Instruct

Non-thinking model — does not generate `\u{1f9e0}` blocks.

### Build llama.cpp

```bash
apt-get update
apt-get install pciutils build-essential cmake curl libcurl4-openssl-dev -y
git clone https://github.com/ggml-org/llama.cpp
cmake llama.cpp -B llama.cpp/build \
    -DBUILD_SHARED_LIBS=OFF -DGGML_CUDA=ON -DLLAMA_CURL=ON
cmake --build llama.cpp/build --config Release -j --clean-first --target llama-cli llama-gguf-split
cp llama.cpp/build/bin/llama-* llama.cpp
```

Change `-DGGML_CUDA=ON` to `-DGGML_CUDA=OFF` for CPU-only. Apple Metal: `-DGGML_CUDA=OFF` (Metal on by default).

### Run via HuggingFace

```bash
./llama.cpp/llama-cli \
    -hf unsloth/Qwen3-Next-80B-A3B-Instruct-GGUF:Q4_K_XL \
    --jinja -ngl 99 --ctx-size 32768 \
    --temp 0.7 --min-p 0.0 --top-p 0.80 --top-k 20 --presence-penalty 1.0
```

### Download Model

```python
# !pip install huggingface_hub hf_transfer
import os
os.environ["HF_HUB_ENABLE_HF_TRANSFER"] = "1"
from huggingface_hub import snapshot_download
snapshot_download(
    repo_id = "unsloth/Qwen3-Next-80B-A3B-Instruct-GGUF",
    local_dir = "Qwen3-Next-80B-A3B-Instruct-GGUF",
    allow_patterns = ["*UD-Q4_K_XL*"],
)
```

Choose `UD_Q4_K_XL` or other quantized versions.

## Run Qwen3-Next-80B-A3B-Thinking

Thinking-only mode, 256K context. Chat template adds `\u{1f9e0}` automatically; output shows closing `\u{1f4a4}` tag.

### Build llama.cpp

Same build steps as Instruct above.

### Run via HuggingFace

```bash
./llama.cpp/llama-cli \
    -hf unsloth/Qwen3-Next-80B-A3B-Thinking-GGUF:Q4_K_XL \
    --jinja -ngl 99 --ctx-size 32768 \
    --temp 0.6 --min-p 0.0 --top-p 0.95 --top-k 20 --presence-penalty 1.0
```

### Download Model

```python
# !pip install huggingface_hub hf_transfer
import os
os.environ["HF_HUB_ENABLE_HF_TRANSFER"] = "1"
from huggingface_hub import snapshot_download
snapshot_download(
    repo_id = "unsloth/Qwen3-Next-80B-A3B-Thinking-GGUF",
    local_dir = "Qwen3-Next-80B-A3B-Thinking-GGUF",
    allow_patterns = ["*UD-Q4_K_XL*"],
)
```

## Improving Generation Speed

Use `-ot` (offload tensor) regex to control MoE layer offloading:

| VRAM | `-ot` flag | Effect |
|---|---|---|
| Least GPU | `".ffn_.*_exps.=CPU"` | Offload all MoE layers to CPU — fits all non-MoE on 1 GPU |
| More GPU | `".ffn_(up\|down)_exps.=CPU"` | Offload up+down projection MoE only |
| Most GPU | `".ffn_(up)_exps.=CPU"` | Offload only up projection MoE |

Custom regex example — offload gate/up/down MoE from layer 6+:
`-ot "\.(6\|7\|8\|9\|[0-9][0-9]\|[0-9][0-9][0-9])\.ffn_(gate\|up\|down)_exps.=CPU"`

High throughput mode: use `llama-parallel` ([docs](https://github.com/ggml-org/llama.cpp/tree/master/examples/parallel), [PR](https://github.com/ggml-org/llama.cpp/pull/14363)).

## Fitting Long Context (256K–1M)

KV cache quantization reduces K/V cache bits, also speeds generation by reducing RAM/VRAM data movement.

K cache options (default `f16`): `f32`, `f16`, `bf16`, `q8_0`, `q4_0`, `q4_1`, `iq4_nl`, `q5_0`, `q5_1`

- Use `_1` variants (`q4_1`, `q5_1`) for slightly better accuracy at minor speed cost. Try `--cache-type-k q4_1`.
- V cache quantization requires compiling llama.cpp with Flash Attention: `-DGGML_CUDA_FA_ALL_QUANTS=ON`, then `--flash-attn --cache-type-v q4_1`.

#unsloth #qwen3-next #llama-cpp #local-inference #moe
