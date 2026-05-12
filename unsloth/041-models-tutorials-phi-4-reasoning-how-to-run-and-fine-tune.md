---
title: 'Phi-4 Reasoning: How to Run & Fine-tune'
url: https://unsloth.ai/docs/models/tutorials/phi-4-reasoning-how-to-run-and-fine-tune.md
source: llms
fetched_at: 2026-04-27T18:14:38.76398824-03:00
rendered_js: false
word_count: 497
summary: This document provides a comprehensive guide on how to run and fine-tune Microsoft's Phi-4 reasoning models using Unsloth. It details various methods, including configuration settings, chat templates, and tutorials for running the model via Ollama and Llama.cpp.
tags:
    - phi-4
    - running
    - finetuning
    - unsloth
    - ollama
    - llama-cpp
    - model-guide
category: guide
optimized: true
optimized_at: 2026-04-27T22:00:00Z
---

# Phi-4 Reasoning: How to Run & Fine-tune

Microsoft Phi-4 reasoning models supported in Unsloth. 'plus' variant performs on par with OpenAI o1-mini, o3-mini, and Sonnet 3.7. 'plus' and standard: 14B params. 'mini': 4B params. Uses [[115-basics-unsloth-dynamic-2.0-ggufs|Unsloth Dynamic 2.0]] methodology.

## Available Uploads

| Dynamic 2.0 GGUF (to run) | Dynamic 4-bit Safetensor (to finetune/deploy) |
|---|---|
| [Reasoning-plus](https://huggingface.co/unsloth/Phi-4-reasoning-plus-GGUF/) (14B) | [Reasoning-plus](https://huggingface.co/unsloth/Phi-4-reasoning-plus-unsloth-bnb-4bit) |
| [Reasoning](https://huggingface.co/unsloth/Phi-4-reasoning-GGUF) (14B) | [Reasoning](https://huggingface.co/unsloth/phi-4-reasoning-unsloth-bnb-4bit) |
| [Mini-reasoning](https://huggingface.co/unsloth/Phi-4-mini-reasoning-GGUF/) (4B) | [Mini-reasoning](https://huggingface.co/unsloth/Phi-4-mini-reasoning-unsloth-bnb-4bit) |

## Recommended Settings (Microsoft)

- **Temperature = 0.8**
- **Top_P = 0.95**

## Chat Templates

> [!warning] 'mini' variant uses a different template than 'reasoning' and 'reasoning-plus'.

### Phi-4-mini

```
Your name is Phi, an AI math expert developed by Microsoft.<|end|>How to solve 3*x^2+4*x+5=1?<|end|>
```

### Phi-4-reasoning and Phi-4-reasoning-plus

```
<|im_start|>system<|im_sep|>You are Phi, a language model trained by Microsoft to help users. Your role as an assistant involves thoroughly exploring questions through a systematic thinking process before providing the final precise and accurate solutions. This requires engaging in a comprehensive cycle of analysis, summarizing, exploration, reassessment, reflection, backtracing, and iteration to develop well-considered thinking process. Please structure your response into two main sections: Thought and Solution using the specified format: Thinking {Thought section} Answer {Solution section}. In the Thought section, detail your reasoning process in steps. Each step should include detailed considerations such as analysing questions, summarizing relevant findings, brainstorming new ideas, verifying the accuracy of the current steps, refining any errors, and revisiting previous steps. In the Solution section, based on various attempts, explorations, and reflections from the Thought section, systematically present the final solution that you deem correct. The Solution section should be logical, accurate, and concise and detail necessary steps needed to reach the conclusion. Now, try to solve the following question through the above guidelines:<|im_end|><|im_start|>user<|im_sep|>What is 1+1?<|im_end|><|im_start|>assistant<|im_sep|>
```

> [!info] Yes, the chat template/prompt format is this long!

## Ollama: Run Phi-4 reasoning

1. Install Ollama:

```bash
apt-get update
apt-get install pciutils -y
curl -fsSL https://ollama.com/install.sh | sh
```

2. Run (call `ollama serve` in another terminal if it fails). Fixes and suggested parameters included in `params` in HF upload:

```bash
ollama run hf.co/unsloth/Phi-4-mini-reasoning-GGUF:Q4_K_XL
```

## Llama.cpp: Run Phi-4 reasoning

> [!warning] You must use `--jinja` in llama.cpp to enable reasoning for non-mini models. Otherwise no reasoning token will be provided. Not needed for 'mini' variant.

1. Build llama.cpp from [GitHub](https://github.com/ggml-org/llama.cpp). Use `-DGGML_CUDA=OFF` for CPU-only or Apple Mac (Metal on by default).

```bash
apt-get update
apt-get install pciutils build-essential cmake curl libcurl4-openssl-dev -y
git clone https://github.com/ggml-org/llama.cpp
cmake llama.cpp -B llama.cpp/build \
    -DBUILD_SHARED_LIBS=OFF -DGGML_CUDA=ON -DLLAMA_CURL=ON
cmake --build llama.cpp/build --config Release -j --clean-first --target llama-cli llama-gguf-split
cp llama.cpp/build/bin/llama-* llama.cpp
```

2. Download model (requires `pip install huggingface_hub hf_transfer`):

```python
# !pip install huggingface_hub hf_transfer
import os
os.environ["HF_HUB_ENABLE_HF_TRANSFER"] = "1"
from huggingface_hub import snapshot_download
snapshot_download(
    repo_id = "unsloth/Phi-4-mini-reasoning-GGUF",
    local_dir = "unsloth/Phi-4-mini-reasoning-GGUF",
    allow_patterns = ["*UD-Q4_K_XL*"],
)
```

3. Run in conversational mode. Use `--jinja` for reasoning models (not needed for 'mini'):

```bash
./llama.cpp/llama-cli \
    --model unsloth/Phi-4-mini-reasoning-GGUF/Phi-4-mini-reasoning-UD-Q4_K_XL.gguf \
    --threads -1 \
    --n-gpu-layers 99 \
    --prio 3 \
    --temp 0.8 \
    --top-p 0.95 \
    --jinja \
    --min_p 0.00 \
    --ctx-size 32768 \
    --seed 3407
```

## Fine-tuning Phi-4 with Unsloth

[Phi-4 fine-tuning](https://unsloth.ai/blog/phi4) supported in Unsloth. For free fine-tuning on Google Colab, change `model_name` from 'unsloth/Phi-4' to 'unsloth/Phi-4-mini-reasoning' etc.

- [Phi-4 (14B) fine-tuning notebook](https://colab.research.google.com/github/unslothai/notebooks/blob/main/nb/Phi_4-Conversational.ipynb)

#phi-4 #reasoning #ollama #llama-cpp #fine-tuning
