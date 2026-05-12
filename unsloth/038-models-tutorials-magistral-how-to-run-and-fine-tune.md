---
title: 'Magistral: How to Run & Fine-tune'
url: https://unsloth.ai/docs/models/tutorials/magistral-how-to-run-and-fine-tune.md
source: llms
fetched_at: 2026-04-27T18:14:25.508199046-03:00
rendered_js: false
word_count: 1211
summary: This document serves as a guide and reference for the Magistral-Small-2509 LLM, detailing how to run it locally on various hardware configurations, providing recommended settings, explaining fine-tuning procedures with Unsloth, and offering tutorials specific to running it in Ollama.
tags:
    - magistral
    - llm
    - mistral-ai
    - running
    - fine-tuning
    - ollama
    - guide
category: guide
optimized: true
optimized_at: 2026-04-27T21:30:00Z
---

# Magistral: How to Run & Fine-tune

**Magistral-Small-2509** is a reasoning LLM by Mistral AI, finetuned from [Mistral-Small-3.2](https://huggingface.co/unsloth/Mistral-Small-3.2-24B-Instruct-2506). Excels at coding and mathematics, supports 128k context (stable to ~40k), multilingual, runs on a single RTX 4090 or Mac with 16-24 GB RAM.

> [!tip] Magistral-2509 Update (September 2025)
> Now includes Vision support. Use Mistral's or Unsloth's official uploads for correct system prompt and chat template. **llama.cpp users: add `--jinja` to enable the system prompt.**

All uploads use Unsloth [[115-basics-unsloth-dynamic-2.0-ggufs|Dynamic 2.0]] for SOTA 5-shot MMLU and KL Divergence performance.

### Unsloth Dynamic Uploads

| Dynamic 2.0 GGUF (run) | Dynamic 4-bit (finetune/deploy) | Dynamic Float8 |
|---|---|---|
| [Magistral-Small-2509-GGUF](https://huggingface.co/unsloth/Magistral-Small-2509-GGUF) (new) | [Magistral-Small-2509-unsloth-bnb-4bit](https://huggingface.co/unsloth/Magistral-Small-2509-unsloth-bnb-4bit) (new) | [Magistral-Small-2509-FP8-Dynamic](https://huggingface.co/unsloth/Magistral-Small-2509-FP8-Dynamic) |
| [Magistral-Small-2507-GGUF](https://huggingface.co/unsloth/Magistral-Small-2507-GGUF) | [Magistral-Small-2507-unsloth-bnb-4bit](https://huggingface.co/unsloth/Magistral-Small-2507-unsloth-bnb-4bit) | [Magistral-Small-2509-FP8-torchao](https://huggingface.co/unsloth/Magistral-Small-2509-FP8-torchao) |
| [Magistral-Small-2506-GGUF](https://huggingface.co/unsloth/Magistral-Small-2506-GGUF) | [Magistral-Small-2506-unsloth-bnb-4bit](https://huggingface.co/unsloth/Magistral-Small-2506-unsloth-bnb-4bit) | |

> [!info] Dynamic uploads have the `UD` prefix. Those without still use our calibration dataset.

## Running Magistral

### Official Recommended Settings

| Parameter | Value | Notes |
|---|---|---|
| Temperature | **0.7** | |
| Min\_P | **0.01** | Optional; llama.cpp default is 0.1 |
| top\_p | **0.95** | |
| Context length | Up to 128k, **recommend 40k** | Performance may degrade past 40k |

**System prompt for Magistral 2509 / 2507:**

```
First draft your thinking process (inner monologue) until you arrive at a response. Format your response using Markdown, and use LaTeX for any mathematical equations. Write both your thoughts and the response in the same language as the input.

Your thinking process must follow the template below:[THINK]Your thoughts or/and draft, like working through an exercise on scratch paper. Be as casual and as long as you want until you are confident to generate the response. Use the same language as the input.[/THINK]Here, provide a self-contained response.
```

**System prompt for Magistral 2506:**

```
A user will ask you to solve a task. You should first draft your thinking process (inner monologue) until you have derived the final answer. Afterwards, write a self-contained summary of your thoughts (i.e. your summary should be succinct but contain all the critical steps you needed to reach the conclusion). You should use Markdown to format your response. Write both your thoughts and summary in the same language as the task posed by the user. NEVER use \boxed{} in your response.

Your thinking process must follow the template below:
```
Your thoughts or/and draft, like working through an exercise on scratch paper. Be as casual and as long as you want until you are confident to generate a correct answer.
```
Here, provide a concise summary that reflects your reasoning and presents a clear final answer to the user. Don't mention that this is a summary.

Problem:
```

- **Multilingual:** English, French, German, Greek, Hindi, Indonesian, Italian, Japanese, Korean, Malay, Nepali, Polish, Portuguese, Romanian, Russian, Serbian, Spanish, Swedish, Turkish, Ukrainian, Vietnamese, Arabic, Bengali, Chinese, Farsi.

### Testing the Model

Mistral's vibe-checking prompts (tested on unquantized; also works quantized):

**Easy** (always correct):

```py
prompt_1 = 'How many "r" are in strawberry?'

prompt_2 = 'John is one of 4 children. The first sister is 4 years old. Next year, the second sister will be twice as old as the first sister. The third sister is two years older than the second sister. The third sister is half the ago of her older brother. How old is John?'

prompt_3 = '9.11 and 9.8, which is greater?'
```

**Medium** (usually correct):

```py
prompt_4 = "Think about 5 random numbers. Verify if you can combine them with addition, multiplication, subtraction or division to 133"

prompt_5 = "Write 4 sentences, each with at least 8 words. Now make absolutely sure that every sentence has exactly one word less than the previous sentence."

prompt_6 = "If it takes 30 minutes to dry 12 T-shirts in the sun, how long does it take to dry 33 T-shirts?"
```

**Hard** (sometimes correct):

```py
prompt_7 = "Pick 5 random words each with at least 10 letters. Print them out. Reverse each word and print it out. Then extract letters that are alphabetically sorted smaller than "g" and print them. Do not use code."

prompt_8 = "Exactly how many days ago did the French Revolution start? Today is June 4th, 2025."
```

See [sample outputs](#sample-outputs) below.

## Running Magistral in Ollama

1. Install Ollama:

```bash
apt-get update
apt-get install pciutils -y
curl -fsSL https://ollama.com/install.sh | sh
```

2. Run with dynamic quant. Use `ollama serve &` in another terminal if it fails. All suggested parameters (temperature etc) are included in `params` in the HuggingFace upload.
3. Magistral supports 40K context -- enable [KV cache quantization](https://github.com/ollama/ollama/blob/main/docs/faq.md#how-can-i-set-the-quantization-type-for-the-kv-cache) (8bit saves 50% memory; can also try `q4_0` or `q8_0`).
4. Ollama defaults context to 4096 ([ref](https://github.com/ollama/ollama/blob/main/docs/faq.md#how-can-i-specify-the-context-window-size)). Use `OLLAMA_CONTEXT_LENGTH=8192` to change. Magistral supports up to 128K; 40K (40960) is tested most.

```bash
export OLLAMA_KV_CACHE_TYPE="f16"
OLLAMA_CONTEXT_LENGTH=8192 ollama serve &
ollama run hf.co/unsloth/Magistral-Small-2509-GGUF:UD-Q4_K_XL
```

## Running Magistral in llama.cpp

1. Build llama.cpp ([GitHub](https://github.com/ggml-org/llama.cpp)). Set `-DGGML_CUDA=OFF` for CPU-only or Apple Mac/Metal (Metal is on by default).

```bash
apt-get update
apt-get install pciutils build-essential cmake curl libcurl4-openssl-dev -y
git clone https://github.com/ggml-org/llama.cpp
cmake llama.cpp -B llama.cpp/build \
    -DBUILD_SHARED_LIBS=OFF -DGGML_CUDA=ON -DLLAMA_CURL=ON
cmake --build llama.cpp/build --config Release -j --clean-first --target llama-quantize llama-cli llama-gguf-split llama-mtmd-cli
cp llama.cpp/build/bin/llama-* llama.cpp
```

2. Quick run (similar to `ollama run`):

```bash
./llama.cpp/llama-cli -hf unsloth/Magistral-Small-2509-GGUF:UD-Q4_K_XL --jinja --temp 0.7 --top-k -1 --top-p 0.95 -ngl 99
```

> [!warning] Use `--jinja` in llama.cpp to enable the system prompt.

3. **OR** download via Python (after `pip install huggingface_hub hf_transfer`):

```python
# !pip install huggingface_hub hf_transfer
import os
os.environ["HF_HUB_ENABLE_HF_TRANSFER"] = "1"
from huggingface_hub import snapshot_download
snapshot_download(
    repo_id = "unsloth/Magistral-Small-2509-GGUF",
    local_dir = "unsloth/Magistral-Small-2509-GGUF",
    allow_patterns = ["*UD-Q4_K_XL*"], # For UD-Q4_K_XL
)
```

4. Run the model.
5. Conversation mode with full settings (`--threads -1` = max CPU, `--ctx-size 40960` = 40K context, `--n-gpu-layers 99` = full GPU offload -- adjust if OOM, remove for CPU-only, 8bit K cache quant):

```bash
./llama.cpp/llama-cli \
    --model unsloth/Magistral-Small-2509-GGUF/Magistral-Small-2509-UD-Q4_K_XL.gguf \
    --ctx-size 40960 \
    --cache-type-k f16 \
    --n-gpu-layers 99 \
    --seed 3407 \
    --prio 2 \
    --temp 0.7 \
    --repeat-penalty 1.0 \
    --min-p 0.01 \
    --top-k -1 \
    --top-p 0.95 \
    --jinja
```

> [!warning] Remove `<bos>` -- Magistral auto-adds it.

## Sample Outputs

### How many "r" are in strawberry? [Correct = 3]

```
```
The model correctly identifies 3 'r's at positions 3, 8, and 9 in "strawberry".

### Exactly how many days ago did the French Revolution start? Today is June 4th, 2025. [Correct = 86,157]

```
```
The model correctly calculates 86,157 days from July 14, 1789 to June 4, 2025.

## Vision Support

> [!tip] Magistral 2509 (September 2025 update) includes Vision by default.

```bash
./llama.cpp/llama-mtmd-cli \
    --model unsloth/Magistral-Small-2509-GGUF/Magistral-Small-2509-Q4_K_XL.gguf \
    --mmproj unsloth/Magistral-Small-2509-GGUF/mmproj-BF16.gguf \
    --ctx-size 40960 \
    --cache-type-k f16
    --n-gpu-layers 99 \
    --seed 3407 \
    --prio 2 \
    --temp 0.7 \
    --repeat-penalty 1.0 \
    --min-p 0.01 \
    --top-k -1 \
    --top-p 0.95 \
    --jinja
```

For pre-September 2025 versions, the vision encoder from Mistral 3.1 Instruct can be grafted onto Magistral (demonstrated by [Xuan-Son](https://x.com/ngxson) for [Devstral](https://huggingface.co/ngxson/Devstral-Small-Vision-2505-GGUF)). Unsloth provides mmproj files for this purpose.

## Fine-tuning Magistral with Unsloth

Training is 2x faster, uses 70% less VRAM, supports 8x longer context. Fits in a 24 GB VRAM L4 GPU. Slightly exceeds 16 GB VRAM limits.

- [Kaggle (2x Tesla T4s) free notebook](https://www.kaggle.com/notebooks/welcome?src=https://github.com/unslothai/notebooks/blob/main/nb/Kaggle-Magistral_\(24B\)-Reasoning-Conversational.ipynb\&accelerator=nvidiaTeslaT4) -- use this for free finetuning
- [Colab L4 (24 GB) notebook](https://colab.research.google.com/github/unslothai/notebooks/blob/main/nb/Magistral_\(24B\)-Reasoning-Conversational.ipynb) -- requires Colab paid tier (24 GB minimum)

```python
!pip install --upgrade unsloth
from unsloth import FastLanguageModel
import torch
model, tokenizer = FastLanguageModel.from_pretrained(
    model_name = "unsloth/Magistral-Small-2509-unsloth-bnb-4bit",
    max_seq_length = 2048,   # Context length - can be longer, but uses more memory
    load_in_4bit = True,     # 4bit uses much less memory
    load_in_8bit = False,    # A bit more accurate, uses 2x memory
    full_finetuning = False, # We have full finetuning now!
    device_map = "balanced", # Uses 2x Telsa T4s
    # token = "hf_...",      # use one if using gated models
)
```

If fine-tuning locally with an older Unsloth version:

```bash
pip install --upgrade --force-reinstall --no-cache-dir unsloth unsloth_zoo
```

## Dynamic Float8 Checkpoints

Two float8 formats using dynamic methodology for max accuracy:

- [vLLM's Float8 format](https://huggingface.co/unsloth/Magistral-Small-2509-FP8-Dynamic)
- [TorchAO's Float8 format](https://huggingface.co/unsloth/Magistral-Small-2509-FP8-torchao)

Both deploy via vLLM. See [TorchAO FP8 in vLLM docs](https://docs.vllm.ai/en/latest/features/quantization/torchao.html).

#magistral #mistral-ai #llm #fine-tuning #ollama
