---
title: Gemma 4 - How to Run Locally
url: https://unsloth.ai/docs/models/gemma-4.md
source: llms
fetched_at: 2026-04-27T18:13:31.11657431-03:00
rendered_js: false
word_count: 1990
summary: This document serves as a guide to running the Gemma 4 family of open models locally, detailing which variants are suitable for different hardware constraints and workflows. It also covers recommended settings, how to enable/disable internal reasoning (thinking), and provides links to GGUF download pages.
tags:
    - gemma-4
    - local-inference
    - model-guide
    - gguf
    - multimodal
    - hardware-requirements
category: tutorial
optimized: true
optimized_at: 2026-04-27T21:40:00Z
---

# Gemma 4 - How to Run Locally

Google DeepMind's open model family: **E2B**, **E4B**, **26B-A4B**, **31B**. Multimodal, hybrid-thinking, 140+ languages, up to **256K context**, dense and MoE variants. Apache-2.0 licensed.

- [Run Gemma 4](#run-gemma-4-tutorials) | [[007-models-gemma-4-train|Fine-tune Gemma 4]]
- **E2B/E4B**: image + audio support. Run on 5GB RAM (4-bit) or 15GB (16-bit). [Gemma 4 GGUFs](https://huggingface.co/collections/unsloth/gemma-4).
- **26B-A4B**: 18GB (4-bit) or 28GB (8-bit). **31B**: 20GB (4-bit) or 34GB (8-bit).

> [!success] Apr 20: [Gemma 4 GGUF Benchmarks](#unsloth-gguf-benchmarks) added. Apr 11: updated chat template + llama.cpp fixes. **Do NOT** use CUDA 13.2 runtime for any GGUF (poor outputs). GGUFs and fine-tuning now available in [[097-new-studio|Unsloth Studio]].

## Usage Guide

Excels at reasoning, coding, tool use, long-context, agentic workflows, multimodal. Smaller E2B/E4B for phones/laptops; larger models for medium-high CPU/VRAM systems (NVIDIA RTX GPUs).

| Gemma 4 Variant | Details | Best fit |
| --- | --- | --- |
| **E2B** | Dense + PLE (128K context). Text, Image, Audio | Phone / edge inference, ASR, speech translation |
| **E4B** | Dense + PLE (128K context). Text, Image, Audio | Laptops, fast local multimodal |
| **26B-A4B** | MoE (256K context). Text, Image | Best speed/quality tradeoff for computer |
| **31B** | Dense (256K context). Text, Image | Strongest performance, slower inference |

**26B-A4B vs 31B:**
- **26B-A4B** -- balances speed and accuracy. MoE design, 4B active parameters. Pick if RAM-limited, accept slight quality trade for speed.
- **31B** -- strongest Gemma 4. Pick for max quality if enough memory.

See: [Performance benchmarks](#official-gemma-benchmarks) | [GGUF benchmarks](#unsloth-gguf-benchmarks)

## Hardware requirements

Units = total memory (RAM + VRAM, or unified). Works on MacOS, NVIDIA RTX GPUs, etc.

| Gemma 4 variant | 4-bit | 8-bit | BF16 / FP16 |
| --- | ---: | ---: | ---: |
| **E2B** | 4 GB | 5-8 GB | 10 GB |
| **E4B** | 5.5-6 GB | 9-12 GB | 16 GB |
| **26B A4B** | 16-18 GB | 28-30 GB | 52 GB |
| **31B** | 17-20 GB | 34-38 GB | 62 GB |

> [!info] Total available memory should exceed the quantized model size. If not, llama.cpp can still run via partial RAM/disk offload (slower generation). More compute needed for larger context windows.

## Recommended Settings

Google's default Gemma 4 parameters: `temperature = 1.0`, `top_p = 0.95`, `top_k = 64`.

Practical defaults:
- Start with **32K context**, increase as needed
- Keep **repetition/presence penalty** disabled or 1.0 (unless looping)
- EOS token: `<turn|>`

> [!info] Max context: **128K** for E2B/E4B, **256K** for 26B-A4B/31B.

### Thinking Mode

Gemma 4 uses standard `system`, `assistant`, `user` roles with explicit thinking control.

**Enable thinking:** Add `<|think|>` at the **start of the system prompt**.

Thinking enabled:
```
<|think|>
You are a careful coding assistant. Explain your answer clearly.
```

Thinking disabled:
```
You are a careful coding assistant. Explain your answer clearly.
```

**Output behavior:**

Thinking enabled -- model outputs internal reasoning before final answer:
```
<|channel>thought
[internal reasoning]
<channel|>
[final answer]
```

Thinking disabled -- larger models may emit empty thought block:
```
<|channel>thought
<channel|>
[final answer]
```

**Example** ("What is the capital of France?"):

Prompt:
```
<bos><|turn>system\n<|think|><turn|>\n<|turn>user\nWhat is the capital of France?<turn|>\n<|turn>model\n
```

Output:
```
<|channel>thought\nThe user is asking for the capital of France.\nThe capital of France is Paris.<channel|>The capital of France is Paris.<turn|>
```

**Multi-turn chat rule:** Only keep the **final visible answer** in chat history. Do **not** feed prior thought blocks back into next turn.

```
<bos><|turn>user\nWhat is 1+1?<turn|>\n<|turn>model\n2<turn|>\n<|turn>user\nWhat is 1+1?<turn|>\n<|turn>model\n2<turn|>\n<|turn>user\nWhat is 1+1?<turn|>\n<|turn>model\n2<turn|>\n<|turn>user\nWhat is 1+1?<turn|>\n<|turn>model\n2<turn|>\n
```

**Disable thinking:** `llama-cli` may not work reliably; use `llama-server`.

> [!warning] To disable thinking/reasoning: `--chat-template-kwargs '{"enable_thinking":false}'`
> Windows PowerShell: `--chat-template-kwargs "{\"enable_thinking\":false}"`
> Use 'true' and 'false' interchangeably.

## Run Gemma 4 Tutorials

Recommended starting point: small models at 8-bit, larger models at **Dynamic 4-bit**. [Gemma 4 GGUFs](https://huggingface.co/collections/unsloth/gemma-4) or [MLX](#mlx-dynamic-quants):

| [gemma-4-E2B](https://huggingface.co/unsloth/gemma-4-E2B-it-GGUF) | [gemma-4-E4B](https://huggingface.co/unsloth/gemma-4-E4B-it-GGUF) | [gemma-4-26B-A4B](https://huggingface.co/unsloth/gemma-4-26B-A4B-it-GGUF) | [gemma-4-31B](https://huggingface.co/unsloth/gemma-4-31B-it-GGUF) |
| --- | --- | --- | --- |

### Unsloth Studio Guide

[[097-new-studio|Unsloth Studio]] -- open-source web UI for local AI. Run models on MacOS, Windows, Linux:

- Search, download, run GGUFs and safetensor models
- [Self-healing tool calling](https://unsloth.ai/docs/new/studio#execute-code--heal-tool-calling) + web search
- [Code execution](https://unsloth.ai/docs/new/studio#run-models-locally) (Python, Bash)
- [Automatic inference](https://unsloth.ai/docs/new/studio#model-arena) parameter tuning
- Fast CPU + GPU inference via llama.cpp
- [Train LLMs](https://unsloth.ai/docs/new/studio#no-code-training) 2x faster with 70% less VRAM

**1. Install Unsloth**

MacOS, Linux, WSL:

```bash
curl -fsSL https://unsloth.ai/install.sh | sh
```

Windows PowerShell:

```bash
irm https://unsloth.ai/install.ps1 | iex
```

**2. Launch Unsloth**

```bash
unsloth studio -H 0.0.0.0 -p 8888
```

Open `http://localhost:8888` in browser.

**3. Search and download Gemma 4**

Create password on first launch, complete onboarding wizard (skippable). Go to Studio Chat tab, search for Gemma 4, download desired model and quant.

**4. Run Gemma 4**

Inference parameters auto-set; can adjust manually (context length, chat template, etc.). See [[099-new-studio-chat|Unsloth Studio inference guide]].

### Llama.cpp Guide

Using Dynamic 4-bit for 26B-A4B/31B, 8-bit for E2B/E4B. [Gemma 4 GGUF collection](https://huggingface.co/collections/unsloth/gemma-4). Uses [llama.cpp](https://github.com/ggml-org/llama.cpp) for fast local inference.

**1. Build llama.cpp**

```bash
apt-get update
apt-get install pciutils build-essential cmake curl libcurl4-openssl-dev -y
git clone https://github.com/ggml-org/llama.cpp
cmake llama.cpp -B llama.cpp/build \
    -DBUILD_SHARED_LIBS=OFF -DGGML_CUDA=ON
cmake --build llama.cpp/build --config Release -j --clean-first --target llama-cli llama-mtmd-cli llama-server llama-gguf-split
cp llama.cpp/build/bin/llama-* llama.cpp
```

Set `-DGGML_CUDA=OFF` if no GPU (CPU only). For Apple Mac/Metal: set `-DGGML_CUDA=OFF` (Metal on by default).

**2. Run with llama-cli**

`UD-Q4_K_XL` is the quantization type. Use `export LLAMA_CACHE="folder"` to save to specific location. No need to set context length (llama.cpp auto-detects).

**26B-A4B:**

```bash
export LLAMA_CACHE="unsloth/gemma-4-26B-A4B-it-GGUF"
./llama.cpp/llama-cli \
    -hf unsloth/gemma-4-26B-A4B-it-GGUF:UD-Q4_K_XL \
    --temp 1.0 \
    --top-p 0.95 \
    --top-k 64
```

**31B:**

```bash
export LLAMA_CACHE="unsloth/gemma-4-31B-it-GGUF"
./llama.cpp/llama-cli \
    -hf unsloth/gemma-4-31B-it-GGUF:UD-Q4_K_XL \
    --temp 1.0 \
    --top-p 0.95 \
    --top-k 64
```

**E4B:**

```bash
export LLAMA_CACHE="unsloth/gemma-4-E4B-it-GGUF"
./llama.cpp/llama-cli \
    -hf unsloth/gemma-4-E4B-it-GGUF:Q8_0 \
    --temp 1.0 \
    --top-p 0.95 \
    --top-k 64
```

**E2B:**

```bash
export LLAMA_CACHE="unsloth/gemma-4-E2B-it-GGUF"
./llama.cpp/llama-cli \
    -hf unsloth/gemma-4-E2B-it-GGUF:Q8_0 \
    --temp 1.0 \
    --top-p 0.95 \
    --top-k 64
```

**3. Download via Hugging Face** (after `pip install huggingface_hub hf_transfer`):

```bash
hf download unsloth/gemma-4-26B-A4B-it-GGUF \
    --local-dir unsloth/gemma-4-26B-A4B-it-GGUF \
    --include "*mmproj-BF16*" \
    --include "*UD-Q4_K_XL*" # Use "*UD-Q2_K_XL*" for Dynamic 2bit
```

If downloads get stuck, see: [[124-basics-troubleshooting-and-faqs-hugging-face-hub-xet-debugging|HF XET debugging]].

**4. Run with vision (mmproj-F16):**

```bash
./llama.cpp/llama-cli \
    --model unsloth/gemma-4-26B-A4B-it-GGUF/gemma-4-26B-A4B-it-UD-Q4_K_XL.gguf \
    --mmproj unsloth/gemma-4-26B-A4B-it-GGUF/mmproj-BF16.gguf \
    --temp 1.0 \
    --top-p 0.95 \
    --top-k 64
```

**5. Llama-server deployment:**

```bash
./llama.cpp/llama-server \
    --model unsloth/gemma-4-26B-A4B-it-GGUF/gemma-4-26B-A4B-it-UD-Q4_K_XL.gguf \
    --mmproj unsloth/gemma-4-26B-A4B-it-GGUF/mmproj-BF16.gguf \
    --temp 1.0 \
    --top-p 0.95 \
    --top-k 64 \
    --alias "unsloth/gemma-4-26B-A4B-it-GGUF" \
    --port 8001 \
    --chat-template-kwargs '{"enable_thinking":true}'
```

> [!warning] To disable thinking: `--chat-template-kwargs '{"enable_thinking":false}'`
> Windows PowerShell: `--chat-template-kwargs "{\"enable_thinking\":false}"`

### MLX Dynamic Quants

Dynamic 4-bit and 8-bit quants for MacOS (now with **vision** support).

| Gemma 4 | 4-bit MLX | 8-bit MLX |
| --- | --- | --- |
| 31B | [link](https://huggingface.co/unsloth/gemma-4-31b-it-UD-MLX-4bit) | [link](https://huggingface.co/unsloth/gemma-4-31b-it-MLX-8bit) |
| 26B-A4B | [link](https://huggingface.co/unsloth/gemma-4-26b-a4b-it-UD-MLX-4bit) | [link](https://huggingface.co/unsloth/gemma-4-26b-a4b-it-MLX-8bit) |
| E4B | [link](https://huggingface.co/unsloth/gemma-4-E4B-it-UD-MLX-4bit) | [link](https://huggingface.co/unsloth/gemma-4-E4B-it-MLX-8bit) |
| E2B | [link](https://huggingface.co/unsloth/gemma-4-E2B-it-UD-MLX-4bit) | [link](https://huggingface.co/unsloth/gemma-4-E2B-it-MLX-8bit) |

```bash
curl -fsSL https://raw.githubusercontent.com/unslothai/unsloth/refs/heads/main/scripts/install_gemma4_mlx.sh | sh
source ~/.unsloth/unsloth_gemma4_mlx/bin/activate
python -m mlx_vlm.chat --model unsloth/gemma-4-26b-a4b-it-UD-MLX-4bit
```

## Gemma 4 Best Practices

### Prompting examples

**Simple reasoning:**

```
System:
<|think|>
You are a precise reasoning assistant.

User:
A train leaves at 8:15 AM and arrives at 11:47 AM. How long was the journey?
```

**OCR / document:** Use high visual token budget like **560** or **1120**.

```
[image first]
Extract all text from this receipt. Return line items, total, merchant, and date as JSON.
```

**Multi-modal comparison:**

```
[image 1]
[image 2]
Compare these two screenshots and tell me which one is more likely to confuse a new user.
```

**Audio ASR:**

```
[audio first]
Transcribe the following speech segment in English into English text.

Follow these specific instructions for formatting the answer:
* Only output the transcription, with no newlines.
* When transcribing numbers, write the digits, i.e. write 1.7 and not one point seven, and write 3 instead of three.
```

**Audio translation:**

```
[audio first]
Transcribe the following speech segment in Spanish, then translate it into English.
When formatting the answer, first output the transcription in Spanish, then one newline, then output the string 'English: ', then the translation in English.
```

### Multi-modal Settings

- Put **image and/or audio before text**
- For video, pass frames first, then instruction

#### Variable image resolution

Supported visual token budgets: `70`, `140`, `280`, `560`, `1120`.

- **70 / 140**: classification, captioning, fast video understanding
- **280 / 560**: general multimodal chat, charts, screens, UI reasoning
- **1120**: OCR, document parsing, handwriting, small text

#### Audio and video limits

- **Audio**: E2B and E4B only. Max **30 seconds**.
- **Video**: Max **60 seconds** at **1 frame per second**.

#### Audio prompt templates

**ASR:**

```
Transcribe the following speech segment in {LANGUAGE} into {LANGUAGE} text.

Follow these specific instructions for formatting the answer:
* Only output the transcription, with no newlines.
* When transcribing numbers, write the digits, i.e. write 1.7 and not one point seven, and write 3 instead of three.
```

**Speech translation:**

```
Transcribe the following speech segment in {SOURCE_LANGUAGE}, then translate it into {TARGET_LANGUAGE}.
When formatting the answer, first output the transcription in {SOURCE_LANGUAGE}, then one newline, then output the string '{TARGET_LANGUAGE}: ', then the translation in {TARGET_LANGUAGE}.
```

## Benchmarks

### Unsloth GGUF Benchmarks

Mean KL Divergence benchmarks across providers (lower is better). KLD measures how well a quantized model matches the original BF16 output distribution.

- All Unsloth GGUFs on the SOTA Pareto frontier

### Official Gemma Benchmarks

| Gemma 4 | MMLU Pro | AIME 2026 (no tools) | LiveCodeBench v6 | MMMU Pro |
| --- | ---: | ---: | ---: | ---: |
| **31B** | 85.2% | 89.2% | 80.0% | 76.9% |
| **26B A4B** | 82.6% | 88.3% | 77.1% | 73.8% |
| **E4B** | 69.4% | 42.5% | 52.0% | 52.6% |
| **E2B** | 60.0% | 37.5% | 44.0% | 44.2% |

---

## Agent Instructions: Querying This Documentation

For information not on this page, query dynamically:

```
GET https://unsloth.ai/docs/models/gemma-4.md?ask=<question>
```

Question should be specific, self-contained, natural language. Response contains direct answer with relevant excerpts and sources.

#gemma-4 #local-inference #gguf #multimodal #hardware-requirements
