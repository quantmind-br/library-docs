---
title: IBM Granite 4.0
url: https://unsloth.ai/docs/models/tutorials/ibm-granite-4.0.md
source: llms
fetched_at: 2026-04-27T18:14:27.862501553-03:00
rendered_js: false
word_count: 733
summary: This document serves as a comprehensive resource detailing the IBM Granite 4.0 models, covering their various sizes and architecture features. It provides tutorials on how to run (via Ollama, llama.cpp, or Docker) and fine-tune these powerful language models using Unsloth.
tags:
    - granite-4.0
    - llm-models
    - unsloth
    - inference-guide
    - fine-tuning
    - amba-architecture
category: tutorial
optimized: true
optimized_at: 2026-04-27T21:42:00Z
---

# IBM Granite 4.0

IBM Granite-4.0 models: Nano (350M, 1B), Micro (3B), Tiny (7B/1B active), Small (32B/9B active). Trained on 15T tokens with Hybrid (H) Mamba architecture for faster inference and lower memory.

## Model Variants

- **Nano / H-Nano (350M, 1B)** — instruction-following for on-device/edge AI, research, fine-tuning
- **H-Small (MoE, 32B total / 9B active)** — enterprise workhorse, multi-session long-context on entry GPUs (e.g., L40S)
- **H-Tiny (MoE, 7B total / 1B active)** — fast, cost-efficient for high-volume low-complexity tasks
- **H-Micro (Dense, 3B)** — lightweight for local/edge deployment
- **Micro (Dense, 3B)** — alternative dense option when Mamba2 isn't fully supported

## Unsloth Granite-4.0 Uploads

| Dynamic GGUFs | Dynamic 4-bit + FP8 | 16-bit Instruct |
|---------------|---------------------|-----------------|
| [H-350M](https://huggingface.co/unsloth/granite-4.0-h-350m-GGUF), [350M](https://huggingface.co/unsloth/granite-4.0-350m-GGUF), [H-1B](https://huggingface.co/unsloth/granite-4.0-h-1b-GGUF), [1B](https://huggingface.co/unsloth/granite-4.0-1b-GGUF), [H-Small](https://huggingface.co/unsloth/granite-4.0-h-small-GGUF), [H-Tiny](https://huggingface.co/unsloth/granite-4.0-h-tiny-GGUF), [H-Micro](https://huggingface.co/unsloth/granite-4.0-h-micro-GGUF), [Micro](https://huggingface.co/unsloth/granite-4.0-micro-GGUF) | 4-bit: [H-Micro](https://huggingface.co/unsloth/granite-4.0-h-micro-unsloth-bnb-4bit), [Micro](https://huggingface.co/unsloth/granite-4.0-micro-unsloth-bnb-4bit) / FP8: [H-Small](https://huggingface.co/unsloth/granite-4.0-h-small-FP8-Dynamic), [H-Tiny](https://huggingface.co/unsloth/granite-4.0-h-tiny-FP8-Dynamic) | [H-350M](https://huggingface.co/unsloth/granite-4.0-h-350m), [350M](https://huggingface.co/unsloth/granite-4.0-350m), [H-1B](https://huggingface.co/unsloth/granite-4.0-h-1b), [1B](https://huggingface.co/unsloth/granite-4.0-1b), [H-Small](https://huggingface.co/unsloth/granite-4.0-h-small), [H-Tiny](https://huggingface.co/unsloth/granite-4.0-h-tiny), [H-Micro](https://huggingface.co/unsloth/granite-4.0-h-micro), [Micro](https://huggingface.co/unsloth/granite-4.0-micro) |

Full collection: [Granite-4.0 on HuggingFace](https://huggingface.co/collections/unsloth/granite-40-68ddf64b4a8717dc22a9322d)

## Run Granite-4.0 Tutorials

### Recommended Inference Settings

| Parameter | Value |
|-----------|-------|
| `temperature` | 0.0 |
| `top_k` | 0 |
| `top_p` | 1.0 |
| Min context | 16,384 |
| Max context | 131,072 (128K) |

**Chat template:**

```
<|start_of_role|>system<|end_of_role|>You are a helpful assistant. Please ensure responses are professional, accurate, and safe.<|end_of_text|>
<|start_of_role|>user<|end_of_role|>Please list one IBM Research laboratory located in the United States. You should only output its name and location.<|end_of_text|>
<|start_of_role|>assistant<|end_of_role|>Almaden Research Center, San Jose, California<|end_of_text|>
```

### Ollama

1. Install ollama:

```bash
apt-get update
apt-get install pciutils -y
curl -fsSL https://ollama.com/install.sh | sh
```

2. Run (change model name/quant as needed; params are embedded in HF upload):

```bash
ollama run hf.co/unsloth/granite-4.0-h-small-GGUF:UD-Q4_K_XL
```

### llama.cpp

1. Build llama.cpp (set `-DGGML_CUDA=OFF` for CPU-only or Apple Metal):

```bash
apt-get update
apt-get install pciutils build-essential cmake curl libcurl4-openssl-dev -y
git clone https://github.com/ggml-org/llama.cpp
cmake llama.cpp -B llama.cpp/build \
    -DBUILD_SHARED_LIBS=OFF -DGGML_CUDA=ON -DLLAMA_CURL=ON
cmake --build llama.cpp/build --config Release -j --clean-first --target llama-cli llama-gguf-split
cp llama.cpp/build/bin/llama-* llama.cpp
```

2. Run directly from HF:

```bash
./llama.cpp/llama-cli \
    -hf unsloth/granite-4.0-h-small-GGUF:UD-Q4_K_XL
```

3. Download via Python:

```python
# !pip install huggingface_hub hf_transfer
import os
os.environ["HF_HUB_ENABLE_HF_TRANSFER"] = "1"
from huggingface_hub import snapshot_download
snapshot_download(
    repo_id = "unsloth/granite-4.0-h-small-GGUF",
    local_dir = "unsloth/granite-4.0-h-small-GGUF",
    allow_patterns = ["*UD-Q4_K_XL*"], # For Q4_K_M
)
```

4. Conversation mode:

```bash
./llama.cpp/llama-mtmd-cli \
    --model unsloth/granite-4.0-h-small-GGUF/granite-4.0-h-small-UD-Q4_K_XL.gguf \
    --jinja \
    --ctx-size 16384 \
    --n-gpu-layers 99 \
    --seed 3407 \
    --prio 2 \
    --temp 0.0 \
    --top-k 0 \
    --top-p 1.0
```

### Docker

```bash
docker model pull hf.co/unsloth/granite-4.0-h-small-GGUF:UD-Q4_K_XL
```

## Fine-tuning Granite-4.0 in Unsloth

Training is 2x faster, uses 50% less VRAM, supports 6x longer context. Micro and Tiny fit in 15GB VRAM (T4 GPU).

- [Free fine-tuning notebook (Support Agent use-case)](https://colab.research.google.com/github/unslothai/notebooks/blob/main/nb/Granite4.0.ipynb)
- [350M fine-tuning notebook](https://github.com/unslothai/notebooks/blob/main/nb/Granite4.0_350M.ipynb)

Also includes training from Google Sheet data.

```python
!pip install --upgrade unsloth
from unsloth import FastLanguageModel
import torch
model, tokenizer = FastLanguageModel.from_pretrained(
    model_name = "unsloth/granite-4.0-h-micro",
    max_seq_length = 2048,   # Context length - can be longer, but uses more memory
    load_in_4bit = True,     # 4bit uses much less memory
    load_in_8bit = False,    # A bit more accurate, uses 2x memory
    full_finetuning = False, # We have full finetuning now!
    # token = "hf_...",      # use one if using gated models
)
```

Update Unsloth locally:

```bash
pip install --upgrade --force-reinstall --no-cache-dir unsloth unsloth_zoo
```

#granite-4.0 #llm-models #unsloth #fine-tuning #amba-architecture
