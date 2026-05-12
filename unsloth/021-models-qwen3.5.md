---
title: Qwen3.5 - How to Run Locally
url: https://unsloth.ai/docs/models/qwen3.5.md
source: llms
fetched_at: 2026-04-27T18:13:34.719631005-03:00
rendered_js: false
word_count: 3806
summary: Guide to running Qwen3.5 models locally — hardware requirements, inference settings, thinking/non-thinking modes across all model sizes.
tags:
    - qwen3.5
    - llm-guide
    - local-inference
    - model-running
    - parameter-settings
    - quantization
category: guide
optimized: true
optimized_at: 2026-04-27T21:30:00Z
---

# Qwen3.5 - How to Run Locally

Alibaba's multimodal hybrid reasoning LLM family: Qwen3.5-**35B**-A3B, **27B**, **122B**-A10B, **397B**-A17B, and Small series (0.8B, 2B, 4B, 9B). Supports **256K context** across 201 languages, thinking + non-thinking modes. Excels in agentic coding, vision, chat, and long-context tasks. 35B and 27B run on 22GB Mac/RAM. [All GGUFs on HuggingFace](https://huggingface.co/collections/unsloth/qwen35).

- [[020-models-qwen3.5-fine-tune|Fine-tune Qwen3.5]]
- [[097-new-studio|Unsloth Studio]]

> [!success] Mar 17 Update
> Qwen3.5 now runs in [[097-new-studio|Unsloth Studio]].
>
> **Mar 5 Update:** Redownload Qwen3.5-**35B**, **27B**, **122B** and **397B**.
> - All GGUFs updated with **improved quantization** algorithm + **new imatrix data**. Improvements in chat, coding, long context, and tool-calling.
> - **Tool-calling fix** is universal — applies to any Qwen3.5 format and any uploader.
> - See [[121-models-qwen3.5-gguf-benchmarks|new GGUF benchmarks]] + [MXFP4 investigation](https://unsloth.ai/docs/models/gguf-benchmarks#id-1-some-tensors-are-very-sensitive-to-quantization).
> - **Retiring MXFP4 layers** from Q2_K_XL, Q3_K_XL and Q4_K_XL GGUFs.

All uploads use Unsloth [[115-basics-unsloth-dynamic-2.0-ggufs|Dynamic 2.0]] for SOTA quantization — 4-bit has important layers upcasted to 8 or 16-bit.

> [!info] Thinking mode toggle
> See [How to enable or disable reasoning & thinking](#how-to-enable-or-disable-reasoning--thinking). Small models disable thinking by default.

## Usage Guide

### Hardware Requirements

Units = total memory (RAM + VRAM, or unified memory).

| Qwen3.5 | 3-bit | 4-bit | 6-bit | 8-bit | BF16 |
|---|---|---|---|---|---|
| **0.8B** + **2B** | 3 GB | 3.5 GB | 5 GB | 7.5 GB | 9 GB |
| **4B** | 4.5 GB | 5.5 GB | 7 GB | 10 GB | 14 GB |
| **9B** | 5.5 GB | 6.5 GB | 9 GB | 13 GB | 19 GB |
| **27B** | 14 GB | 17 GB | 24 GB | 30 GB | 54 GB |
| **35B-A3B** | 17 GB | 22 GB | 30 GB | 38 GB | 70 GB |
| **122B-A10B** | 60 GB | 70 GB | 106 GB | 132 GB | 245 GB |
| **397B-A17B** | 180 GB | 214 GB | 340 GB | 512 GB | 810 GB |

> [!success] Memory tip
> For best performance, total available memory must exceed the quantized model file size. llama.cpp can run via SSD/HDD offloading if memory is insufficient, but inference will be slower.

**27B vs 35B-A3B:** Use 27B for slightly more accurate results; 35B-A3B for much faster inference.

### Recommended Settings

- **Max context window:** `262,144` (extendable to 1M via YaRN)
- **Adequate output length:** `32,768` tokens for most queries
- `presence_penalty = 0.0 to 2.0` — default off; reduces repetitions but higher values may cause slight performance decrease

> [!info] Gibberish output?
> Context length may be set too low. Try `--cache-type-k bf16 --cache-type-v bf16`.

Qwen3.5 is hybrid reasoning — thinking and non-thinking modes have different settings:

#### Thinking Mode

| Parameter | General Tasks | Precise Coding (e.g. WebDev) |
|---|---|---|
| temperature | 1.0 | 0.6 |
| top_p | 0.95 | 0.95 |
| top_k | 20 | 20 |
| min_p | 0.0 | 0.0 |
| presence_penalty | 1.5 | 0.0 |
| repeat penalty | disabled or 1.0 | disabled or 1.0 |

General tasks:
```bash
temperature=1.0, top_p=0.95, top_k=20, min_p=0.0, presence_penalty=1.5, repetition_penalty=1.0
```

Precise coding:
```bash
temperature=0.6, top_p=0.95, top_k=20, min_p=0.0, presence_penalty=0.0, repetition_penalty=1.0
```

#### Instruct (Non-Thinking) Mode

| Parameter | General Tasks | Reasoning Tasks |
|---|---|---|
| temperature | 0.7 | 1.0 |
| top_p | 0.8 | 0.95 |
| top_k | 20 | 20 |
| min_p | 0.0 | 0.0 |
| presence_penalty | 1.5 | 1.5 |
| repeat penalty | disabled or 1.0 | disabled or 1.0 |

> [!warning] Disabling thinking
> Use `--chat-template-kwargs '{"enable_thinking":false}'`
>
> **Windows PowerShell:** `--chat-template-kwargs "{\"enable_thinking\":false}"`
>
> **Qwen3.5 Small (0.8B, 2B, 4B, 9B):** reasoning disabled by default — enable with `'{"enable_thinking":true}'`

General tasks:
```bash
temperature=0.7, top_p=0.8, top_k=20, min_p=0.0, presence_penalty=1.5, repetition_penalty=1.0
```

Reasoning tasks:
```bash
temperature=1.0, top_p=0.95, top_k=20, min_p=0.0, presence_penalty=1.5, repetition_penalty=1.0
```

## Qwen3.5 Inference Tutorials

All guides use Dynamic 4-bit `MXFP4_MOE` GGUF variants. Navigate to your model size below.

### Unsloth Dynamic GGUF Uploads

| [Qwen3.5-**35B-A3B**](https://huggingface.co/unsloth/Qwen3.5-35B-A3B-GGUF) | [Qwen3.5-**27B**](https://huggingface.co/unsloth/Qwen3.5-27B-GGUF) | [Qwen3.5-**122B-A10B**](https://huggingface.co/unsloth/Qwen3.5-122B-A10B-GGUF) | [Qwen3.5-**397B-A17B**](https://huggingface.co/unsloth/Qwen3.5-397B-A17B-GGUF) |
|---|---|---|---|
| [Qwen3.5-**0.8B**](https://huggingface.co/unsloth/Qwen3.5-0.8B-GGUF) | [Qwen3.5-**2B**](https://huggingface.co/unsloth/Qwen3.5-2B-GGUF) | [Qwen3.5-**4B**](https://huggingface.co/unsloth/Qwen3.5-4B-GGUF) | [Qwen3.5-**9B**](https://huggingface.co/unsloth/Qwen3.5-9B-GGUF) |

> [!warning]
> `presence_penalty` higher values may cause slight performance decrease.
>
> **No Qwen3.5 GGUF works in Ollama** due to separate mmproj vision files. Use llama.cpp compatible backends.

## Unsloth Studio Guide

[[097-new-studio|Unsloth Studio]] is an open-source web UI for local AI (MacOS, Windows, Linux).

Features:
- Search, download, run GGUFs and safetensor models
- Self-healing tool calling + web search
- Code execution (Python, Bash)
- Automatic inference parameter tuning
- Fast CPU + GPU inference via llama.cpp
- Train LLMs 2x faster with 70% less VRAM

### Step 1: Install Unsloth

**MacOS, Linux, WSL:**
```bash
curl -fsSL https://unsloth.ai/install.sh | sh
```

**Windows PowerShell:**
```bash
irm https://unsloth.ai/install.ps1 | iex
```

### Step 2: Launch Unsloth

**MacOS, Linux, WSL and Windows:**
```bash
unsloth studio -H 0.0.0.0 -p 8888
```

Then open `http://localhost:8888` in your browser.

### Step 3: Search and download Qwen3.5

On first launch, create a password and sign in. Skip the onboarding wizard if desired. Go to the [[099-new-studio-chat|Studio Chat]] tab, search for "Qwen3.5" in the search bar, and download your desired model and quant.

### Step 4: Run Qwen3.5

Inference parameters are auto-set in Unsloth Studio but can be changed manually. Edit context length, chat template, and other settings. See [[099-new-studio-chat|Unsloth Studio inference guide]].

## Llama.cpp Guides

### Qwen3.5-35B-A3B

Dynamic 4-bit works on 24GB RAM/Mac. Full F16 ~72GB. GGUF: [Qwen3.5-35B-A3B-GGUF](https://huggingface.co/unsloth/Qwen3.5-35B-A3B-GGUF)

#### Build llama.cpp

```bash
apt-get update
apt-get install pciutils build-essential cmake curl libcurl4-openssl-dev -y
git clone https://github.com/ggml-org/llama.cpp
cmake llama.cpp -B llama.cpp/build \
    -DBUILD_SHARED_LIBS=OFF -DGGML_CUDA=ON
cmake --build llama.cpp/build --config Release -j --clean-first --target llama-cli llama-mtmd-cli llama-server llama-gguf-split
cp llama.cpp/build/bin/llama-* llama.cpp
```

Change `-DGGML_CUDA=ON` to `-DGGML_CUDA=OFF` for CPU-only inference. **Apple Mac/Metal:** set `-DGGML_CUDA=OFF` (Metal is on by default).

#### Run via HuggingFace (llama-cli / llama-server)

Use `export LLAMA_CACHE="folder"` to force save location. Max 256K context length.

**Thinking mode — Precise coding:**
```bash
export LLAMA_CACHE="unsloth/Qwen3.5-35B-A3B-GGUF"
./llama.cpp/llama-cli \
    -hf unsloth/Qwen3.5-35B-A3B-GGUF:UD-Q4_K_XL \
    --ctx-size 16384 \
    --temp 0.6 \
    --top-p 0.95 \
    --top-k 20 \
    --min-p 0.00
```

**Thinking mode — General tasks:**
```bash
export LLAMA_CACHE="unsloth/Qwen3.5-35B-A3B-GGUF"
./llama.cpp/llama-cli \
    -hf unsloth/Qwen3.5-35B-A3B-GGUF:UD-Q4_K_XL \
    --ctx-size 16384 \
    --temp 1.0 \
    --top-p 0.95 \
    --top-k 20 \
    --min-p 0.00
```

**Non-thinking mode — General tasks:**
```bash
export LLAMA_CACHE="unsloth/Qwen3.5-35B-A3B-GGUF"
./llama.cpp/llama-server \
    -hf unsloth/Qwen3.5-35B-A3B-GGUF:UD-Q4_K_XL \
    --ctx-size 16384 \
    --temp 0.7 \
    --top-p 0.8 \
    --top-k 20 \
    --min-p 0.00 \
    --chat-template-kwargs '{"enable_thinking":false}'
```

**Non-thinking mode — Reasoning tasks:**
```bash
export LLAMA_CACHE="unsloth/Qwen3.5-35B-A3B-GGUF"
./llama.cpp/llama-server \
    -hf unsloth/Qwen3.5-35B-A3B-GGUF:UD-Q4_K_XL \
    --ctx-size 16384 \
    --temp 1.0 \
    --top-p 0.95 \
    --top-k 20 \
    --min-p 0.00 \
    --chat-template-kwargs '{"enable_thinking":false}'
```

#### Download model manually

Requires `pip install huggingface_hub hf_transfer`. If downloads get stuck, see [[124-basics-troubleshooting-and-faqs-hugging-face-hub-xet-debugging|HF XET debugging]].

```bash
hf download unsloth/Qwen3.5-35B-A3B-GGUF \
    --local-dir unsloth/Qwen3.5-35B-A3B-GGUF \
    --include "*mmproj-F16*" \
    --include "*UD-Q4_K_XL*" # Use "*UD-Q2_K_XL*" for Dynamic 2bit
```

#### Run in conversation mode

```bash
./llama.cpp/llama-cli \
    --model unsloth/Qwen3.5-35B-A3B-GGUF/Qwen3.5-35B-A3B-UD-Q4_K_XL.gguf \
    --mmproj unsloth/Qwen3.5-35B-A3B-GGUF/mmproj-F16.gguf \
    --temp 1.0 \
    --top-p 0.95 \
    --min-p 0.00 \
    --top-k 20
```

### Qwen3.5 Small (0.8B, 2B, 4B, 9B)

> [!warning] Thinking disabled by default on Small models
> Enable with: `--chat-template-kwargs '{"enable_thinking":true}'`
>
> **Windows:** `--chat-template-kwargs "{\"enable_thinking\":true}"`

All Small variants: change model name in scripts to desired variant (0.8B, 2B, 4B, 9B). Near full precision needs ~12GB RAM/VRAM.

GGUFs: [0.8B](https://huggingface.co/unsloth/Qwen3.5-0.8B-GGUF) | [2B](https://huggingface.co/unsloth/Qwen3.5-2B-GGUF) | [4B](https://huggingface.co/unsloth/Qwen3.5-4B-GGUF) | [9B](https://huggingface.co/unsloth/Qwen3.5-9B-GGUF)

#### Build llama.cpp

Same as [35B build instructions](#build-llama.cpp).

#### Run via HuggingFace (9B shown — replace with 0.8B/2B/4B as needed)

**Thinking mode (requires llama-server to enable):**
```bash
export LLAMA_CACHE="unsloth/Qwen3.5-9B-GGUF"
./llama.cpp/llama-server \
    -hf unsloth/Qwen3.5-9B-GGUF:UD-Q4_K_XL \
    --ctx-size 16384 \
    --temp 0.6 \
    --top-p 0.95 \
    --top-k 20 \
    --min-p 0.00 \
    --alias "unsloth/Qwen3.5-9B-GGUF" \
    --port 8001 \
    --chat-template-kwargs '{"enable_thinking":true}'
```

General tasks (thinking):
```bash
export LLAMA_CACHE="unsloth/Qwen3.5-9B-GGUF"
./llama.cpp/llama-server \
    -hf unsloth/Qwen3.5-9B-GGUF:UD-Q4_K_XL \
    --ctx-size 16384 \
    --temp 1.0 \
    --top-p 0.95 \
    --top-k 20 \
    --min-p 0.00 \
    --alias "unsloth/Qwen3.5-9B-GGUF" \
    --port 8001 \
    --chat-template-kwargs '{"enable_thinking":true}'
```

**Non-thinking mode (default):**

General tasks:
```bash
export LLAMA_CACHE="unsloth/Qwen3.5-9B-GGUF"
./llama.cpp/llama-cli \
    -hf unsloth/Qwen3.5-9B-GGUF:UD-Q4_K_XL \
    --ctx-size 16384 \
    --temp 0.7 \
    --top-p 0.8 \
    --top-k 20 \
    --min-p 0.00
```

Reasoning tasks:
```bash
export LLAMA_CACHE="unsloth/Qwen3.5-9B-GGUF"
./llama.cpp/llama-cli \
    -hf unsloth/Qwen3.5-9B-GGUF:UD-Q4_K_XL \
    --ctx-size 16384 \
    --temp 1.0 \
    --top-p 0.95 \
    --top-k 20 \
    --min-p 0.00
```

#### Download model manually

```bash
hf download unsloth/Qwen3.5-9B-GGUF \
    --local-dir unsloth/Qwen3.5-9B-GGUF \
    --include "*mmproj-F16*" \
    --include "*UD-Q4_K_XL*" # Use "*UD-Q2_K_XL*" for Dynamic 2bit
```

#### Run in conversation mode

```bash
./llama.cpp/llama-cli \
    --model unsloth/Qwen3.5-9B-GGUF/Qwen3.5-9B-UD-Q4_K_XL.gguf \
    --mmproj unsloth/Qwen3.5-9B-GGUF/mmproj-F16.gguf \
    --temp 1.0 \
    --top-p 0.95 \
    --min-p 0.00 \
    --top-k 20
```

### Qwen3.5-27B

Dynamic 4-bit works on 18GB RAM/Mac. GGUF: [Qwen3.5-27B-GGUF](https://huggingface.co/unsloth/Qwen3.5-27B-GGUF)

#### Build llama.cpp

Same as [35B build instructions](#build-llama.cpp).

#### Run via HuggingFace

**Thinking mode — Precise coding:**
```bash
export LLAMA_CACHE="unsloth/Qwen3.5-27B-GGUF"
./llama.cpp/llama-cli \
    -hf unsloth/Qwen3.5-27B-GGUF:UD-Q4_K_XL \
    --ctx-size 16384 \
    --temp 0.6 \
    --top-p 0.95 \
    --top-k 20 \
    --min-p 0.00
```

**Thinking mode — General tasks:**
```bash
export LLAMA_CACHE="unsloth/Qwen3.5-27B-GGUF"
./llama.cpp/llama-cli \
    -hf unsloth/Qwen3.5-27B-GGUF:UD-Q4_K_XL \
    --ctx-size 16384 \
    --temp 1.0 \
    --top-p 0.95 \
    --top-k 20 \
    --min-p 0.00
```

**Non-thinking mode — General tasks:**
```bash
export LLAMA_CACHE="unsloth/Qwen3.5-27B-GGUF"
./llama.cpp/llama-server \
    -hf unsloth/Qwen3.5-27B-GGUF:UD-Q4_K_XL \
    --ctx-size 16384 \
    --temp 0.7 \
    --top-p 0.8 \
    --top-k 20 \
    --min-p 0.00 \
    --chat-template-kwargs '{"enable_thinking":false}'
```

**Non-thinking mode — Reasoning tasks:**
```bash
export LLAMA_CACHE="unsloth/Qwen3.5-27B-GGUF"
./llama.cpp/llama-server \
    -hf unsloth/Qwen3.5-27B-GGUF:UD-Q4_K_XL \
    --ctx-size 16384 \
    --temp 1.0 \
    --top-p 0.95 \
    --top-k 20 \
    --min-p 0.00 \
    --chat-template-kwargs '{"enable_thinking":false}'
```

#### Download model manually

```bash
hf download unsloth/Qwen3.5-27B-GGUF \
    --local-dir unsloth/Qwen3.5-27B-GGUF \
    --include "*mmproj-F16*" \
    --include "*UD-Q4_K_XL*" # Use "*UD-Q2_K_XL*" for Dynamic 2bit
```

#### Run in conversation mode

```bash
./llama.cpp/llama-cli \
    --model unsloth/Qwen3.5-27B-GGUF/Qwen3.5-27B-UD-Q4_K_XL.gguf \
    --mmproj unsloth/Qwen3.5-27B-GGUF/mmproj-F16.gguf \
    --temp 1.0 \
    --top-p 0.95 \
    --min-p 0.00 \
    --top-k 20
```

### Qwen3.5-122B-A10B

Dynamic 4-bit works on 70GB RAM/Mac. GGUF: [Qwen3.5-122B-A10B-GGUF](https://huggingface.co/unsloth/Qwen3.5-122B-A10B-GGUF)

#### Build llama.cpp

Same as [35B build instructions](#build-llama.cpp).

#### Run via HuggingFace

**Thinking mode — Precise coding:**
```bash
export LLAMA_CACHE="unsloth/Qwen3.5-122B-A10B-GGUF"
./llama.cpp/llama-cli \
    -hf unsloth/Qwen3.5-122B-A10B-GGUF:UD-Q4_K_XL \
    --ctx-size 16384 \
    --temp 0.6 \
    --top-p 0.95 \
    --top-k 20 \
    --min-p 0.00
```

**Thinking mode — General tasks:**
```bash
export LLAMA_CACHE="unsloth/Qwen3.5-122B-A10B-GGUF"
./llama.cpp/llama-cli \
    -hf unsloth/Qwen3.5-122B-A10B-GGUF:UD-Q4_K_XL \
    --ctx-size 16384 \
    --temp 1.0 \
    --top-p 0.95 \
    --top-k 20 \
    --min-p 0.00
```

**Non-thinking mode — General tasks:**
```bash
export LLAMA_CACHE="unsloth/Qwen3.5-122B-A10B-GGUF"
./llama.cpp/llama-server \
    -hf unsloth/Qwen3.5-122B-A10B-GGUF:UD-Q4_K_XL \
    --ctx-size 16384 \
    --temp 0.7 \
    --top-p 0.8 \
    --top-k 20 \
    --min-p 0.00 \
    --chat-template-kwargs '{"enable_thinking":false}'
```

**Non-thinking mode — Reasoning tasks:**
```bash
export LLAMA_CACHE="unsloth/Qwen3.5-122B-A10B-GGUF"
./llama.cpp/llama-server \
    -hf unsloth/Qwen3.5-122B-A10B-GGUF:UD-Q4_K_XL \
    --ctx-size 16384 \
    --temp 1.0 \
    --top-p 0.95 \
    --top-k 20 \
    --min-p 0.00 \
    --chat-template-kwargs '{"enable_thinking":false}'
```

#### Download model manually

```bash
hf download unsloth/Qwen3.5-122B-A10B-GGUF \
    --local-dir unsloth/Qwen3.5-122B-A10B-GGUF \
    --include "*mmproj-F16*" \
    --include "*UD-Q4_K_XL*" # Use "*UD-Q2_K_XL*" for Dynamic 2bit
```

#### Run in conversation mode

Note: this model uses sharded GGUFs (multi-file).

```bash
./llama.cpp/llama-cli \
    --model unsloth/Qwen3.5-122B-A10B-GGUF/UD-Q4_K_XL/Qwen3.5-122B-A10B-UD-Q4_K_XL-00001-of-00003.gguf \
    --mmproj unsloth/Qwen3.5-122B-A10B-GGUF/mmproj-F16.gguf \
    --ctx-size 16384 \
    --temp 0.6 \
    --top-p 0.95 \
    --top-k 20 \
    --min-p 0.00
```

### Qwen3.5-397B-A17B

Same performance tier as Gemini 3 Pro, Claude Opus 4.5, GPT-5.2. Full 397B ~807GB on disk.

| Quant | Memory | Notes |
|---|---|---|
| 3-bit | 192 GB RAM | e.g. 192GB Mac |
| 4-bit (MXFP4) | 256 GB RAM | Unsloth **UD-Q4_K_XL** ~214GB — loads on 256GB M3 Ultra |
| 4-bit + MoE offload | 24GB GPU + 256GB system RAM | 25+ tokens/s |
| 8-bit | ~512 GB RAM/VRAM | |

GGUF: [Qwen3.5-397B-A17B-GGUF](https://huggingface.co/unsloth/Qwen3.5-397B-A17B-GGUF)

#### Build llama.cpp

Same as [35B build instructions](#build-llama.cpp).

#### Run via HuggingFace

**Thinking mode:**
```bash
export LLAMA_CACHE="unsloth/Qwen3.5-397B-A17B-GGUF"
./llama.cpp/llama-cli \
    -hf unsloth/Qwen3.5-397B-A17B-GGUF:UD-Q4_K_XL \
    --ctx-size 16384 \
    --temp 0.6 \
    --top-p 0.95 \
    --top-k 20 \
    --min-p 0.00
```

**Non-thinking mode:**
```bash
export LLAMA_CACHE="unsloth/Qwen3.5-397B-A17B-GGUF"
./llama.cpp/llama-server \
    -hf unsloth/Qwen3.5-397B-A17B-GGUF:UD-Q4_K_XL \
    --ctx-size 16384 \
    --temp 0.7 \
    --top-p 0.8 \
    --top-k 20 \
    --min-p 0.00 \
    --chat-template-kwargs '{"enable_thinking":false}'
```

#### Download model manually

```bash
hf download unsloth/Qwen3.5-397B-A17B-GGUF \
    --local-dir unsloth/Qwen3.5-397B-A17B-GGUF \
    --include "*mmproj-F16*" \
    --include "*UD-Q4_K_XL" # Use "*UD-Q2_K_XL*" for Dynamic 2bit
```

#### Run in conversation mode

Sharded GGUF. Adjust `--threads 32` (CPU threads), `--ctx-size 16384`, `--n-gpu-layers 2` (GPU offloading layers). Remove GPU layer flag for CPU-only.

```bash
./llama.cpp/llama-cli \
    --model unsloth/Qwen3.5-397B-A17B-GGUF/UD-Q4_K_XL/Qwen3.5-397B-A17B-UD-Q4_K_XL-00001-of-00006.gguf \
    --mmproj unsloth/Qwen3.5-397B-A17B-GGUF/mmproj-F16.gguf \
    --ctx-size 16384 \
    --temp 0.6 \
    --top-p 0.95 \
    --top-k 20 \
    --min-p 0.00
```

## LM Studio Guide

Using [LM Studio](https://lmstudio.ai/) unified UI. The thinking/non-thinking toggle may not appear by default.

### Step 1: Download

Download [LM Studio](https://lmstudio.ai/download). Open Model Search, search for 'unsloth/qwen3.5', download desired GGUF.

### Step 2: Enable thinking toggle

Run `lms --help` in Terminal/PowerShell. If commands appear, run:
```bash
lms get unsloth/qwen3.5-4b
```
This downloads a yaml file enabling the thinking toggle. Change `4b` to your desired variant. Alternatively, download the yaml from [our LM Studio page](https://lmstudio.ai/unsloth).

### Step 3: Load model

Restart LM Studio, load the downloaded model. Thinking toggle should now appear. Set [correct parameters](#recommended-settings).

## Llama-server Serving & OpenAI Completion Library

Deploy via `llama-server`:

```bash
./llama.cpp/llama-server \
--model unsloth/Qwen3.5-35B-A3B-GGUF/Qwen3.5-35B-A3B-UD-Q4_K_XL.gguf \
    --mmproj unsloth/Qwen3.5-35B-A3B-GGUF/mmproj-F16.gguf \
    --alias "unsloth/Qwen3.5-35B-A3B" \
    --temp 0.6 \
    --top-p 0.95 \
    --ctx-size 16384 \
    --top-k 20 \
    --min-p 0.00 \
    --port 8001
```

Then in Python (`pip install openai`):

```python
from openai import OpenAI
import json
openai_client = OpenAI(
    base_url = "http://127.0.0.1:8001/v1",
    api_key = "sk-no-key-required",
)
completion = openai_client.chat.completions.create(
    model = "unsloth/Qwen3.5-397B-A17B",
    messages = [{"role": "user", "content": "Create a Snake game."},],
)
print(completion.choices[0].message.content)
```

## How to Enable or Disable Reasoning & Thinking

- [[097-new-studio|Unsloth Studio]] has a Think toggle by default.
- For LM Studio thinking toggle, see [LM Studio Guide](#lm-studio-guide).

> [!info] Disable thinking
> ```
> --chat-template-kwargs '{"enable_thinking":false}'
> ```
> **Windows/Powershell:** `--chat-template-kwargs "{\"enable_thinking\":false}"`

> [!info] Enable thinking
> ```
> --chat-template-kwargs '{"enable_thinking":true}'
> ```
> **Windows/Powershell:** `--chat-template-kwargs "{\"enable_thinking\":true}"`

> [!danger] Small models (0.8B, 2B, 4B, 9B)
> Reasoning disabled by default. Enable with: `--chat-template-kwargs '{"enable_thinking":true}'`

Example — Qwen3.5-9B with thinking enabled:

```bash
./llama.cpp/llama-server \
    --model unsloth/Qwen3.5-9B-GGUF/Qwen3.5-9B-BF16.gguf \
    --alias "unsloth/Qwen3.5-9B-GGUF" \
    --temp 0.6 \
    --top-p 0.95 \
    --ctx-size 16384 \
    --top-k 20 \
    --min-p 0.00 \
    --port 8001 \
    --chat-template-kwargs '{"enable_thinking":true}'
```

Python client with reasoning output:
```python
from openai import OpenAI
import json
openai_client = OpenAI(
    base_url = "http://127.0.0.1:8001/v1",
    api_key = "sk-no-key-required",
)
completion = openai_client.chat.completions.create(
    model = "unsloth/Qwen3.5-9B-GGUF",
    messages = [{"role": "user", "content": "What is 2+2?"},],
)
print(completion.choices[0].message.content)
print(completion.choices[0].message.reasoning_content)
```

## OpenAI Codex & Claude Code

For local coding agentic workloads, follow [[077-basics-claude-code|Claude Code guide]] or [[078-basics-codex|Codex guide]]. Change model name to your Qwen3.5 variant and follow correct parameters. Use the `llama-server` setup above.

## Tool Calling with Qwen3.5

See [[095-basics-tool-calling-guide-for-local-llms|Tool Calling Guide]] for details. Define tool functions:

```python
import json, subprocess, random
from typing import Any
def add_number(a: float | str, b: float | str) -> float:
    return float(a) + float(b)
def multiply_number(a: float | str, b: float | str) -> float:
    return float(a) * float(b)
def substract_number(a: float | str, b: float | str) -> float:
    return float(a) - float(b)
def write_a_story() -> str:
    return random.choice([
        "A long time ago in a galaxy far far away...",
        "There were 2 friends who loved sloths and code...",
        "The world was ending because every sloth evolved to have superhuman intelligence...",
        "Unbeknownst to one friend, the other accidentally coded a program to evolve sloths...",
    ])
def terminal(command: str) -> str:
    if "rm" in command or "sudo" in command or "dd" in command or "chmod" in command:
        msg = "Cannot execute 'rm, sudo, dd, chmod' commands since they are dangerous"
        print(msg); return msg
    print(f"Executing terminal command `{command}`")
    try:
        return str(subprocess.run(command, capture_output = True, text = True, shell = True, check = True).stdout)
    except subprocess.CalledProcessError as e:
        return f"Command failed: {e.stderr}"
def python(code: str) -> str:
    data = {}
    exec(code, data)
    del data["__builtins__"]
    return str(data)
MAP_FN = {
    "add_number": add_number,
    "multiply_number": multiply_number,
    "substract_number": substract_number,
    "write_a_story": write_a_story,
    "terminal": terminal,
    "python": python,
}
tools = [
    {
        "type": "function",
        "function": {
            "name": "add_number",
            "description": "Add two numbers.",
            "parameters": {
                "type": "object",
                "properties": {
                    "a": {
                        "type": "string",
                        "description": "The first number.",
                    },
                    "b": {
                        "type": "string",
                        "description": "The second number.",
                    },
                },
                "required": ["a", "b"],
            },
        },
    },
    {
        "type": "function",
        "function": {
            "name": "multiply_number",
            "description": "Multiply two numbers.",
            "parameters": {
                "type": "object",
                "properties": {
                    "a": {
                        "type": "string",
                        "description": "The first number.",
                    },
                    "b": {
                        "type": "string",
                        "description": "The second number.",
                    },
                },
                "required": ["a", "b"],
            },
        },
    },
    {
        "type": "function",
        "function": {
            "name": "substract_number",
            "description": "Substract two numbers.",
            "parameters": {
                "type": "object",
                "properties": {
                    "a": {
                        "type": "string",
                        "description": "The first number.",
                    },
                    "b": {
                        "type": "string",
                        "description": "The second number.",
                    },
                },
                "required": ["a", "b"],
            },
        },
    },
    {
        "type": "function",
        "function": {
            "name": "write_a_story",
            "description": "Writes a random story.",
            "parameters": {
                "type": "object",
                "properties": {},
                "required": [],
            },
        },
    },
    {
        "type": "function",
        "function": {
            "name": "terminal",
            "description": "Perform operations from the terminal.",
            "parameters": {
                "type": "object",
                "properties": {
                    "command": {
                        "type": "string",
                        "description": "The command you wish to launch, e.g `ls`, `rm`, ...",
                    },
                },
                "required": ["command"],
            },
        },
    },
    {
        "type": "function",
        "function": {
            "name": "python",
            "description": "Call a Python interpreter with some Python code that will be ran.",
            "parameters": {
                "type": "object",
                "properties": {
                    "code": {
                        "type": "string",
                        "description": "The Python code to run",
                    },
                },
                "required": ["code"],
            },
        },
    },
]
```

Auto-parsing inference function — calls OpenAI endpoint and executes tool calls:

```python
from openai import OpenAI
def unsloth_inference(
    messages,
    temperature = 0.6,
    top_p = 0.95,
    top_k = 20,
    min_p = 0.00,
    repetition_penalty = 1.0,
):
    messages = messages.copy()
    openai_client = OpenAI(
        base_url = "http://127.0.0.1:8001/v1",
        api_key = "sk-no-key-required",
    )
    model_name = next(iter(openai_client.models.list())).id
    print(f"Using model = {model_name}")
    has_tool_calls = True
    original_messages_len = len(messages)
    while has_tool_calls:
        print(f"Current messages = {messages}")
        response = openai_client.chat.completions.create(
            model = model_name,
            messages = messages,
            temperature = temperature,
            top_p = top_p,
            tools = tools if tools else None,
            tool_choice = "auto" if tools else None,
            extra_body = {"top_k": top_k, "min_p": min_p, "repetition_penalty" :repetition_penalty,}
        )
        tool_calls = response.choices[0].message.tool_calls or []
        content = response.choices[0].message.content or ""
        tool_calls_dict = [tc.to_dict() for tc in tool_calls] if tool_calls else tool_calls
        messages.append({"role": "assistant", "tool_calls": tool_calls_dict, "content": content,})
        for tool_call in tool_calls:
            fx, args, _id = tool_call.function.name, tool_call.function.arguments, tool_call.id
            out = MAP_FN[fx](**json.loads(args))
            messages.append({"role": "tool", "tool_call_id": _id, "name": fx, "content": str(out),})
        else:
            has_tool_calls = False
    return messages
```

Launch Qwen3.5 via `llama-server` as shown above, then call `unsloth_inference()`.

## Benchmarks

### Unsloth GGUF Benchmarks

Qwen3.5-35B Unsloth Dynamic quants are SOTA on nearly all bits. 150+ KL Divergence benchmarks, 9TB of GGUFs tested.

- All GGUFs updated with improved quantization algorithm + new imatrix data
- 99.9% KL Divergence SOTA on Pareto Frontier for UD-Q4_K_XL, IQ3_XXS & more
- Retiring MXFP4 from Q2_K_XL, Q3_K_XL, Q4_K_XL (except pure MXFP4_MOE)
- Fixed tool calling chat template bug (affects all quant uploaders)

See [[121-models-qwen3.5-gguf-benchmarks|Qwen3.5 GGUF Benchmarks]] for full analysis.

### Qwen3.5-397B-A17B Benchmarks

[Benjamin Marie (third-party)](https://x.com/bnjmn_marie/status/2025951400119751040/photo/1) benchmarked 397B-A17B using Unsloth GGUFs on a 750-prompt mixed suite (LiveCodeBench v6, MMLU Pro, GPQA, Math500):

| Quant | Accuracy | Change vs Original | Relative Error Increase |
|---|---|---|---|
| Original weights | 81.3% | — | — |
| **UD-Q4_K_XL** | **80.5%** | -0.8 pts | +4.3% |
| **UD-Q3_K_XL** | **80.7%** | -0.6 pts | +3.5% |

Both stay under 1-point accuracy drop. Memory footprint reduction ~500GB with little practical loss.

**How to choose:** Q3 vs Q4 difference is run-to-run variance — treat as effectively similar quality. Pick Q3 for smallest footprint; Q4 for slightly more conservative option.

All quants use dynamic methodology. `UD-IQ2_M` uses the same methodology as `UD-Q2-K-XL` but different conversion process — K-XL is usually faster despite being bigger.

### Official Qwen Benchmarks

- **35B-A3B, 27B, 122B-A10B:** See official Qwen benchmark images
- **4B, 9B:** See official Qwen Small benchmark images
- **397B-A17B:** See official Qwen 397B benchmark images

#qwen3.5 #llm-inference #quantization #gguf #local-llm
