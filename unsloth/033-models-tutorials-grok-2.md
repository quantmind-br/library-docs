---
title: Grok 2
url: https://unsloth.ai/docs/models/tutorials/grok-2.md
source: llms
fetched_at: 2026-04-27T18:14:29.968711419-03:00
rendered_js: false
word_count: 1253
summary: This document details the technical specifications, recommended settings, and provides step-by-step instructions on how to run Grok 2 (a 270B parameter model by xAI), particularly using llama.cpp for optimal performance.
tags:
    - grok-2
    - llm
    - llama-cpp
    - quantization
    - inference
    - model-guide
    - unsloth
category: tutorial
optimized: true
optimized_at: 2026-04-27T22:10:00Z
---

# Grok 2

Grok 2 (aka Grok 2.5) is xAI's 270B parameter model. Full precision = **539GB**; Unsloth Dynamic 3-bit = **118GB** (75% reduction). GGUF: [Grok-2-GGUF](https://huggingface.co/unsloth/grok-2-GGUF)

3-bit Q3_K_XL runs on single **128GB Mac** or **24GB VRAM + 128GB RAM** at **5+ tokens/s**. All uploads use Unsloth [Dynamic 2.0](https://unsloth.ai/docs/basics/unsloth-dynamic-2.0-ggufs) for SOTA MMLU/KL performance.

## Recommended Settings

3-bit dynamic quant = 118GB (126GiB). Fits 128GB unified memory Mac or 1x24GB GPU + 128GB RAM. Min recommended: 120GB RAM.

> [!warning] You must use `--jinja` for Grok 2. Incorrect results without it.

8-bit quant = ~300GB. Fits 1x80GB GPU (MoE offloaded to RAM). ~5 tokens/s with extra 200GB RAM.

> [!info] For best performance: VRAM + RAM >= quant size. Hard drive offloading works via llama.cpp but is slower.

### Sampling Parameters

- 128K max context -- use `131,072` or less
- Use `--jinja` for llama.cpp
- **temperature = 1.0**
- **Min-P = 0.01** (optional; llama.cpp default is 0.1)

## Run Grok 2 in llama.cpp

### Build llama.cpp (Grok 2 PR)

```bash
apt-get update
apt-get install pciutils build-essential cmake curl libcurl4-openssl-dev -y
git clone https://github.com/ggml-org/llama.cpp
cd llama.cpp && git fetch origin pull/15539/head:MASTER && git checkout MASTER && cd ..
cmake llama.cpp -B llama.cpp/build \
    -DBUILD_SHARED_LIBS=OFF -DGGML_CUDA=ON -DLLAMA_CURL=ON
cmake --build llama.cpp/build --config Release -j --clean-first --target llama-quantize llama-cli llama-gguf-split llama-mtmd-cli llama-server
cp llama.cpp/build/bin/llama-* llama.cpp
```

Set `-DGGML_CUDA=OFF` for CPU-only or Apple Mac/Metal (Metal on by default).

### Run via Hugging Face

```bash
export LLAMA_CACHE="unsloth/grok-2-GGUF"
./llama.cpp/llama-cli \
    -hf unsloth/grok-2-GGUF:Q3_K_XL \
    --jinja \
    --n-gpu-layers 99 \
    --temp 1.0 \
    --top-p 0.95 \
    --min-p 0.01 \
    --ctx-size 16384 \
    --seed 3407 \
    -ot ".ffn_.*_exps.=CPU"
```

### Download Model

```python
# !pip install huggingface_hub hf_transfer
import os
os.environ["HF_HUB_ENABLE_HF_TRANSFER"] = "0" # Can sometimes rate limit, so set to 0 to disable
from huggingface_hub import snapshot_download
snapshot_download(
    repo_id = "unsloth/grok-2-GGUF",
    local_dir = "unsloth/grok-2-GGUF",
    allow_patterns = ["*UD-Q3_K_XL*"], # Dynamic 3bit
)
```

Recommend **2.7bit dynamic quant `UD-Q2_K_XL`** or above to balance size and accuracy.

### Run Local Model

```bash
./llama.cpp/llama-cli \
    --model unsloth/grok-2-GGUF/UD-Q3_K_XL/grok-2-UD-Q3_K_XL-00001-of-00003.gguf \
    --jinja \
    --threads -1 \
    --n-gpu-layers 99 \
    --temp 1.0 \
    --top_p 0.95 \
    --min_p 0.01 \
    --ctx-size 16384 \
    --seed 3407 \
    -ot ".ffn_.*_exps.=CPU"
```

Adjust `--threads`, `--ctx-size`, `--n-gpu-layers` as needed. Remove GPU flags for CPU-only.

## MoE Layer Offloading

Use `-ot` with regex to offload MoE layers to CPU, fitting non-MoE layers on GPU:

| Pattern | Effect |
| ------- | ------ |
| `-ot ".ffn_.*_exps.=CPU"` | All MoE layers to CPU (least VRAM) |
| `-ot ".ffn_(up\|down)_exps.=CPU"` | Up + down projection MoE only |
| `-ot ".ffn_(up)_exps.=CPU"` | Only up projection MoE (most GPU) |
| `-ot "\.(6\|7\|8\|9\|[0-9][0-9]\|[0-9][0-9][0-9])\.ffn_(gate\|up\|down)_exps.=CPU"` | Gate/up/down MoE from layer 6+ |

## Model Uploads

All uploads use Unsloth's calibration dataset optimized for conversational, coding, and language tasks.

| MoE Bits | Type + Link | Disk Size | Details |
| ------- | ----------- | --------: | ------- |
| 1.66bit | [TQ1_0](https://huggingface.co/unsloth/grok-2-GGUF/blob/main/grok-2-UD-TQ1_0.gguf) | **81.8 GB** | 1.92/1.56bit |
| 1.78bit | [IQ1_S](https://huggingface.co/unsloth/grok-2-GGUF/tree/main/UD-IQ1_S) | **88.9 GB** | 2.06/1.56bit |
| 1.93bit | [IQ1_M](https://huggingface.co/unsloth/grok-2-GGUF/tree/main/UD-IQ1_M) | **94.5 GB** | 2.5/2.06/1.56 |
| 2.42bit | [IQ2_XXS](https://huggingface.co/unsloth/grok-2-GGUF/tree/main/UD-IQ2_XXS) | **99.3 GB** | 2.5/2.06bit |
| 2.71bit | [Q2_K_XL](https://huggingface.co/unsloth/grok-2-GGUF/tree/main/UD-Q2_K_XL) | **112 GB** | 3.5/2.5bit |
| 3.12bit | [IQ3_XXS](https://huggingface.co/unsloth/grok-2-GGUF/tree/main/UD-IQ3_XXS) | **117 GB** | 3.5/2.06bit |
| 3.5bit | [Q3_K_XL](https://huggingface.co/unsloth/grok-2-GGUF/tree/main/UD-Q3_K_XL) | **126 GB** | 4.5/3.5bit |
| 4.5bit | [Q4_K_XL](https://huggingface.co/unsloth/grok-2-GGUF/tree/main/UD-Q4_K_XL) | **155 GB** | 5.5/4.5bit |
| 5.5bit | [Q5_K_XL](https://huggingface.co/unsloth/grok-2-GGUF/tree/main/UD-Q5_K_XL) | **191 GB** | 6.5/5.5bit |

## Improving Generation Speed

- Offload more MoE layers or whole layers with more VRAM (see table above)
- [High throughput mode](https://github.com/ggml-org/llama.cpp/tree/master/examples/parallel) via `llama-parallel`
- Quantize KV cache to 4bits to reduce RAM/VRAM movement

## Fitting Long Context (Full 128K)

Use **KV cache quantization** to reduce K/V caches to lower bits. Also speeds generation via reduced data movement.

**K cache options** (`--cache-type-k`, default `f16`):

`f32, f16, bf16, q8_0, q4_0, q4_1, iq4_nl, q5_0, q5_1`

Use `_1` variants (e.g., `q4_1`, `q5_1`) for slightly better accuracy at slightly slower speed.

**V cache** requires compiling llama.cpp with Flash Attention: `-DGGML_CUDA_FA_ALL_QUANTS=ON`, then use `--flash-attn`.

**V cache options** (`--cache-type-v`):

`f32, f16, bf16, q8_0, q4_0, q4_1, iq4_nl, q5_0, q5_1`

---

# Agent Instructions: Querying This Documentation

If you need additional information that is not directly available in this page, you can query the documentation dynamically by asking a question.

Perform an HTTP GET request on the current page URL with the `ask` query parameter:

```
GET https://unsloth.ai/docs/models/tutorials/grok-2.md?ask=<question>
```

The question should be specific, self-contained, and written in natural language.
The response will contain a direct answer to the question and relevant excerpts and sources from the documentation.

Use this mechanism when the answer is not explicitly present in the current page, you need clarification or additional context, or you want to retrieve related documentation sections.

#grok-2 #llama-cpp #quantization #local-inference
