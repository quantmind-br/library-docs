---
title: 'DeepSeek-R1: How to Run Locally'
url: https://unsloth.ai/docs/models/tutorials/deepseek-r1-how-to-run-locally.md
source: llms
fetched_at: 2026-04-27T18:14:34.771249262-03:00
rendered_js: false
word_count: 933
summary: This document serves as a guide detailing the various methods for running the DeepSeek R1 model locally, primarily focusing on using llama.cpp. It provides installation instructions, command examples for execution with different configurations (like GPU offloading), and notes on optimizing performance across various hardware setups.
tags:
    - deepseek-r1
    - llama-cpp
    - local-runtime
    - gguf-model
    - gpu-offload
    - command-line
category: guide
optimized: true
optimized_at: 2026-04-27T22:10:00Z
---

# DeepSeek-R1: How to Run Locally

> [!tip] Updated DeepSeek R1-0528 (May 28 2025) version: <https://docs.unsloth.ai/basics/deepseek-r1-0528-how-to-run-locally>

## Using llama.cpp (recommended)

Key notes:
- Use `<|User|>` and `<|Assistant|>` tokens, or a chat template formatter
- Use `--min-p 0.05` to counteract rare token predictions (especially for 1.58bit)
- For Apple Mac / Metal: set `-DGGML_CUDA=OFF` (Metal is on by default)

### Build llama.cpp

```bash
apt-get update
apt-get install pciutils build-essential cmake curl libcurl4-openssl-dev -y
git clone https://github.com/ggml-org/llama.cpp
cmake llama.cpp -B llama.cpp/build \
    -DBUILD_SHARED_LIBS=ON -DGGML_CUDA=ON -DLLAMA_CURL=ON
cmake --build llama.cpp/build --config Release -j --clean-first --target llama-quantize llama-cli llama-gguf-split
cp llama.cpp/build/bin/llama-* llama.cpp
```

### Download Model

```python
# pip install huggingface_hub hf_transfer
# import os # Optional for faster downloading
# os.environ["HF_HUB_ENABLE_HF_TRANSFER"] = "1"

from huggingface_hub import snapshot_download
snapshot_download(
  repo_id = "unsloth/DeepSeek-R1-GGUF",
  local_dir = "DeepSeek-R1-GGUF",
  allow_patterns = ["*UD-IQ1_S*"], # Select quant type UD-IQ1_S for 1.58bit
)
```

### Run (Q4_0 K cache, no conversation mode)

```bash
./llama.cpp/llama-cli \
    --model DeepSeek-R1-GGUF/DeepSeek-R1-UD-IQ1_S/DeepSeek-R1-UD-IQ1_S-00001-of-00003.gguf \
    --cache-type-k q4_0 \
    -no-cnv --prio 2 \
    --temp 0.6 \
    --ctx-size 8192 \
    --seed 3407 \
    --prompt "<|User|>What is 1+1?<|Assistant|>"
```

### Run with GPU Offloading

For 24GB GPU (RTX 4090 etc.): use `--n-gpu-layers 7`. Multiple GPUs can offload more layers.

```bash
./llama.cpp/llama-cli \
    --model DeepSeek-R1-GGUF/DeepSeek-R1-UD-IQ1_S/DeepSeek-R1-UD-IQ1_S-00001-of-00003.gguf \
    --cache-type-k q4_0 \
    -no-cnv --prio 2 \
    --n-gpu-layers 7 \
    --temp 0.6 \
    --ctx-size 8192 \
    --seed 3407 \
    --prompt "<|User|>Create a Flappy Bird game in Python.<|Assistant|>"
```

### Merge Split GGUF Files (for Ollama)

```bash
./llama.cpp/llama-gguf-split --merge \
    DeepSeek-R1-GGUF/DeepSeek-R1-UD-IQ1_S-00001-of-00003.gguf \
    merged_file.gguf
```

### GPU Layer Offloading Reference

DeepSeek R1 has 61 layers. Reduce by 1 if OOM:

| Quant | File Size | 24GB GPU | 80GB GPU | 2x80GB GPU |
| ----- | --------: | -------: | -------: | ---------: |
| 1.58bit | 131GB | 7 | 33 | All 61 |
| 1.73bit | 158GB | 5 | 26 | 57 |
| 2.22bit | 183GB | 4 | 22 | 49 |
| 2.51bit | 212GB | 2 | 19 | 32 |

## Running on Mac / Apple Devices

128GB unified memory: ~59 layers offloadable. Reduce `--n-gpu-layers` if OOM.

```bash
./llama.cpp/llama-cli \
    --model DeepSeek-R1-GGUF/DeepSeek-R1-UD-IQ1_S/DeepSeek-R1-UD-IQ1_S-00001-of-00003.gguf \
    --cache-type-k q4_0 \
    --prio 2 \
    --temp 0.6 \
    --ctx-size 8192 \
    --seed 3407 \
    --n-gpu-layers 59 \
    -no-cnv \
    --prompt "<|User|>Create a Flappy Bird game in Python.<|Assistant|>"
```

## Run in Ollama / Open WebUI

Open WebUI tutorial: [docs.openwebui.com/tutorials/integrations/deepseekr1-dynamic/](https://docs.openwebui.com/tutorials/integrations/deepseekr1-dynamic/)

For Ollama: first merge the 3 GGUF splits into 1, then run locally.

## DeepSeek Chat Template

All distilled versions and the 671B R1 model use the same template:

```
<|begin of sentence|><|User|>What is 1+1?<|Assistant|>It's 2.<|end of sentence|><|User|>Explain more!<|Assistant|>
```

BOS is forcibly added; EOS separates each interaction. For llama.cpp/GGUF: skip BOS (auto-added). Use `tokenizer.encode(..., add_special_tokens=False)` to avoid double BOS.

### Tokenizer ID Mappings

| Token | R1 | Distill Qwen | Distill Llama |
| ----- | --: | -----------: | ------------: |
| ༀ | 128798 | 151648 | 128013 |
| ཚ | 128799 | 151649 | 128014 |
| `<|begin_of_sentence|>` | 0 | 151646 | 128000 |
| `<|end_of_sentence|>` | 1 | 151643 | 128001 |
| `<|User|>` | 128803 | 151644 | 128011 |
| `<|Assistant|>` | 128804 | 151645 | 128012 |
| Padding token | 2 | 151654 | 128004 |

### Original Tokens in Base Models

| Token | Qwen 2.5 32B Base | Llama 3.3 70B Instruct |
| ----- | ----------------- | ---------------------- |
| ༀ | `<|box_start|>` | `<|reserved_special_token_5|>` |
| ཚ | `<|box_end|>` | `<|reserved_special_token_6|>` |
| `<|begin of sentence|>` | `<|object_ref_start|>` | `<|begin_of_text|>` |
| `<|end of sentence|>` | `<|endoftext|>` | `<|end_of_text|>` |
| `<|User|>` | `<|im_start|>` | `<|reserved_special_token_3|>` |
| `<|Assistant|>` | `<|im_end|>` | `<|reserved_special_token_4|>` |
| Padding token | `<|vision_pad|>` | `<|finetune_right_pad_id|>` |

> [!warning] All distilled and original R1 versions accidentally assigned padding to `<|end of sentence|>`, causing infinite generations during fine-tuning (frameworks mask EOS as -100). Unsloth fixed all versions with correct padding tokens.

## GGUF R1 Table

| MoE Bits | Type | Disk Size | Accuracy | Link | Details |
| ------- | ---- | --------: | -------- | ---- | ------- |
| 1.58bit | UD-IQ1_S | **131GB** | Fair | [Link](https://huggingface.co/unsloth/DeepSeek-R1-GGUF/tree/main/DeepSeek-R1-UD-IQ1_S) | MoE all 1.56bit. `down_proj` mixture of 2.06/1.56bit |
| 1.73bit | UD-IQ1_M | **158GB** | Good | [Link](https://huggingface.co/unsloth/DeepSeek-R1-GGUF/tree/main/DeepSeek-R1-UD-IQ1_M) | MoE all 1.56bit. `down_proj` at 2.06bit |
| 2.22bit | UD-IQ2_XXS | **183GB** | Better | [Link](https://huggingface.co/unsloth/DeepSeek-R1-GGUF/tree/main/DeepSeek-R1-UD-IQ2_XXS) | MoE all 2.06bit. `down_proj` mixture of 2.5/2.06bit |
| 2.51bit | UD-Q2_K_XL | **212GB** | Best | [Link](https://huggingface.co/unsloth/DeepSeek-R1-GGUF/tree/main/DeepSeek-R1-UD-Q2_K_XL) | MoE all 2.5bit. `down_proj` mixture of 3.5/2.5bit |

---

# Agent Instructions: Querying This Documentation

If you need additional information that is not directly available in this page, you can query the documentation dynamically by asking a question.

Perform an HTTP GET request on the current page URL with the `ask` query parameter:

```
GET https://unsloth.ai/docs/models/tutorials/deepseek-r1-how-to-run-locally.md?ask=<question>
```

The question should be specific, self-contained, and written in natural language.
The response will contain a direct answer to the question and relevant excerpts and sources from the documentation.

Use this mechanism when the answer is not explicitly present in the current page, you need clarification or additional context, or you want to retrieve related documentation sections.

#deepseek-r1 #llama-cpp #gguf #local-inference
