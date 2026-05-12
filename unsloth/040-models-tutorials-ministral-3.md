---
title: Ministral 3 - How to Run Guide
url: https://unsloth.ai/docs/models/tutorials/ministral-3.md
source: llms
fetched_at: 2026-04-27T18:14:13.565299085-03:00
rendered_js: false
word_count: 891
summary: This document serves as a comprehensive guide for running and utilizing the new Ministral 3 multimodal models in various variants (Base, Instruct, Reasoning) across different sizes (3B, 8B, 14B). It details recommended usage parameters, chat templates, and provides tutorials on how to deploy the model.
tags:
    - ministral-3
    - llm-guide
    - multimodal-models
    - usage-tutorial
    - gguf-formats
    - model-variants
category: guide
optimized: true
optimized_at: 2026-04-27T21:14:00Z
---

# Ministral 3 - How to Run Guide

Mistral Ministral 3 — multimodal models in Base, Instruct, and Reasoning variants. Sizes: **3B**, **8B**, **14B**. Best-in-class per size. Supports **256K context**, multiple languages, native function calling, JSON output. Full 14B unquantized fits in **24GB RAM/VRAM**.

Mistral Large 3 [GGUFs here](https://huggingface.co/unsloth/Mistral-Large-3-675B-Instruct-2512-GGUF). All Ministral 3 uploads (BnB, FP8): [see here](https://huggingface.co/collections/unsloth/ministral-3).

| Ministral-3-Instruct GGUFs | Ministral-3-Reasoning GGUFs |
|---|---|
| [3B](https://huggingface.co/unsloth/Ministral-3-3B-Instruct-2512-GGUF) | [3B](https://huggingface.co/unsloth/Ministral-3-3B-Reasoning-2512-GGUF) |
| [8B](https://huggingface.co/unsloth/Ministral-3-8B-Instruct-2512-GGUF) | [8B](https://huggingface.co/unsloth/Ministral-3-8B-Reasoning-2512-GGUF) |
| [14B](https://huggingface.co/unsloth/Ministral-3-14B-Instruct-2512-GGUF) | [14B](https://huggingface.co/unsloth/Ministral-3-14B-Reasoning-2512-GGUF) |

## Usage Guide

| | Instruct | Reasoning |
|---|---|---|
| **Temperature** | `0.15` or `0.1` | `0.7` |
| **Top_P** | default | `0.95` |
| **Output length** | 16,384 tokens | 32,768 tokens (increase if needed) |
| **Max context** | 262,144 | 262,144 |

### Chat Template

```python
tokenizer.apply_chat_template([
    {"role" : "user", "content" : "What is 1+1?"},
    {"role" : "assistant", "content" : "2"},
    {"role" : "user", "content" : "What is 2+2?"}
    ], add_generation_prompt = True
)
```

### Ministral Reasoning Chat Template

```
<s>[SYSTEM_PROMPT]# HOW YOU SHOULD THINK AND ANSWER

First draft your thinking process (inner monologue) until you arrive at a response. Format your response using Markdown, and use LaTeX for any mathematical equations. Write both your thoughts and the response in the same language as the input.

Your thinking process must follow the template below:[THINK]Your thoughts or/and draft, like working through an exercise on scratch paper. Be as casual and as long as you want until you are confident to generate the response to the user.[/THINK]Here, provide a self-contained response.[/SYSTEM_PROMPT][INST]What is 1+1?[/INST]2</s>[INST]What is 2+2?[/INST]
```

### Ministral Instruct Chat Template

```
<s>[SYSTEM_PROMPT]You are Ministral-3-3B-Instruct-2512, a Large Language Model (LLM) created by Mistral AI, a French startup headquartered in Paris.
You power an AI assistant called Le Chat.
Your knowledge base was last updated on 2023-10-01.
The current date is {today}.

When you're not sure about some information or when the user's request requires up-to-date or specific data, you must use the available tools to fetch the information. Do not hesitate to use tools whenever they can provide a more accurate or complete response. If no relevant tools are available, then clearly state that you don't have the information and avoid making up anything.
If the user's question is not clear, ambiguous, or does not provide enough context for you to accurately answer the question, you do not try to answer it right away and you rather ask the user to clarify their request (e.g. "What are some good restaurants around me?" => "Where are you?" or "When is the next flight to Tokyo" => "Where do you travel from?").
You are always very attentive to dates, in particular you try to resolve dates (e.g. "yesterday" is {yesterday}) and when asked about information at specific dates, you discard information that is at another date.
You follow these instructions in all languages, and always respond to the user in the language they use or request.
Next sections describe the capabilities that you have.

# WEB BROWSING INSTRUCTIONS

You cannot perform any web search or access internet to open URLs, links etc. If it seems like the user is expecting you to do so, you clarify the situation and ask the user to copy paste the text directly in the chat.

# MULTI-MODAL INSTRUCTIONS

You have the ability to read images, but you cannot generate images. You also cannot transcribe audio files or videos.
You cannot read nor transcribe audio files or videos.

# TOOL CALLING INSTRUCTIONS

You may have access to tools that you can use to fetch information or perform actions. You must use these tools in the following situations:

1. When the request requires up-to-date information.
2. When the request requires specific data that you do not have in your knowledge base.
3. When the request involves actions that you cannot perform without tools.

Always prioritize using tools to provide the most accurate and helpful response. If tools are not available, inform the user that you cannot perform the requested action at the moment.[/SYSTEM_PROMPT][INST]What is 1+1?[/INST]2</s>[INST]What is 2+2?[/INST]
```

## Run Ministral 3 Tutorials

### Instruct: Ministral-3-Instruct-2512

#### llama.cpp: Run Ministral-3-14B-Instruct

**1. Build llama.cpp** — get latest from [GitHub](https://github.com/ggml-org/llama.cpp). Set `-DGGML_CUDA=OFF` if no GPU. Metal on by default for Apple Mac.

```bash
apt-get update
apt-get install pciutils build-essential cmake curl libcurl4-openssl-dev -y
git clone https://github.com/ggml-org/llama.cpp
cmake llama.cpp -B llama.cpp/build \
    -DBUILD_SHARED_LIBS=OFF -DGGML_CUDA=ON -DLLAMA_CURL=ON
cmake --build llama.cpp/build --config Release -j --clean-first --target llama-cli llama-mtmd-cli llama-server llama-gguf-split
cp llama.cpp/build/bin/llama-* llama.cpp
```

**2. Run directly from Hugging Face:**

```bash
./llama.cpp/llama-cli \
    -hf unsloth/Ministral-3-14B-Instruct-2512-GGUF:Q4_K_XL \
    --jinja -ngl 99 --ctx-size 32684 \
    --temp 0.15
```

**3. Download the model** (after `pip install huggingface_hub hf_transfer`):

```python
# !pip install huggingface_hub hf_transfer
import os
os.environ["HF_HUB_ENABLE_HF_TRANSFER"] = "1"
from huggingface_hub import snapshot_download
snapshot_download(
    repo_id = "unsloth/Ministral-3-14B-Instruct-2512-GGUF",
    local_dir = "Ministral-3-14B-Instruct-2512-GGUF",
    allow_patterns = ["*UD-Q4_K_XL*"],
)
```

### Reasoning: Ministral-3-Reasoning-2512

#### llama.cpp: Run Ministral-3-14B-Reasoning

**1. Build llama.cpp** — same as instruct above.

**2. Run directly from Hugging Face:**

```bash
./llama.cpp/llama-cli \
    -hf unsloth/Ministral-3-14B-Reasoning-2512-GGUF:Q4_K_XL \
    --jinja -ngl 99 --ctx-size 32684 \
    --temp 0.6 --top-p 0.95
```

**3. Download the model** (after `pip install huggingface_hub hf_transfer`):

```python
# !pip install huggingface_hub hf_transfer
import os
os.environ["HF_HUB_ENABLE_HF_TRANSFER"] = "1"
from huggingface_hub import snapshot_download
snapshot_download(
    repo_id = "unsloth/Ministral-3-14B-Reasoning-2512-GGUF",
    local_dir = "Ministral-3-14B-Reasoning-2512-GGUF",
    allow_patterns = ["*UD-Q4_K_XL*"],
)
```

## Fine-tuning Ministral 3

Unsloth supports fine-tuning all Ministral 3 models including vision. Requires latest Hugging Face `transformers` v5 and `unsloth` (includes [ultra long context](https://unsloth.ai/docs/blog/500k-context-length-fine-tuning) support). 14B fits on free Colab GPU.

**Free Colab Notebooks:**

- Ministral-3B-Instruct [Vision notebook](https://colab.research.google.com/github/unslothai/notebooks/blob/main/nb/Ministral_3_VL_\(3B\)_Vision.ipynb)
- Ministral-3B-Instruct [GRPO notebook](https://colab.research.google.com/github/unslothai/notebooks/blob/main/nb/Ministral_3_\(3B\)_Reinforcement_Learning_Sudoku_Game.ipynb)

### Reinforcement Learning (GRPO)

Unsloth supports RL and GRPO for Mistral models with all Unsloth enhancements. The GRPO notebook demonstrates auto-generating strategies to solve Sudoku puzzles.

**Update to latest:**

```bash
pip install --upgrade --force-reinstall --no-cache-dir --no-deps unsloth unsloth_zoo
```

- Ministral-3B-Instruct [GRPO notebook](https://colab.research.google.com/github/unslothai/notebooks/blob/main/nb/Ministral_3_\(3B\)_Reinforcement_Learning_Sudoku_Game.ipynb)

#ministral-3 #mistral #gguf #unsloth #grpo
