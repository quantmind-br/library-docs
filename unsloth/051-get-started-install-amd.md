---
title: Fine-tuning LLMs on AMD GPUs with Unsloth Guide
url: https://unsloth.ai/docs/get-started/install/amd.md
source: llms
fetched_at: 2026-04-27T18:13:00.422587087-03:00
rendered_js: false
word_count: 924
summary: This guide details the process of setting up and fine-tuning Large Language Models (LLMs) using Unsloth specifically on AMD GPUs. It provides options for a one-line installation or manual environment setup, covering PyTorch and bitsandbytes installations necessary for optimal performance.
tags:
    - unsloth-amd
    - llm-fine-tuning
    - rocm-gpu
    - pytorch-setup
    - bitsandbytes
    - installation-guide
category: guide
optimized: true
optimized_at: 2026-04-27T21:30:00Z
---

# Fine-tuning LLMs on AMD GPUs with Unsloth Guide

Fine-tune LLMs up to 2x faster with ~70% less memory on AMD. Supports Radeon RDNA 2/3/3.5/4 (RX 6000–9000) and data center GPUs incl. MI300X (192GB).

## One-line Installer

Auto-detects AMD GPU, installs ROCm-optimized PyTorch, bitsandbytes, and launches Unsloth Studio:

```
curl -fsSL https://unsloth.ai/install.sh | sh
```

Below steps are for Python library-only install without Studio.

## Manual Install

### 1. Isolated Environment (Optional)

```bash
apt update && apt install python3.10-venv python3.11-venv python3.12-venv python3.13-venv -y

python3 -m venv unsloth_env
source unsloth_env/bin/activate
pip install uv
```

### 2. Install PyTorch (ROCm)

Check ROCm version via `amd-smi version`. **ROCm 6.0+ required** (no PyTorch wheels for 5.x).

```bash
uv pip install "torch>=2.4,<2.11.0" "torchvision<0.26.0" "torchaudio<2.11.0" \
    --index-url https://download.pytorch.org/whl/rocm7.1 --upgrade --force-reinstall
```

Change `rocm7.1` to match your version. If ROCm >= 7.2, use `rocm7.1` (no wheels for 7.2+ yet).

Auto-detect ROCm version:

```bash
ROCM_TAG="$({ command -v amd-smi >/dev/null 2>&1 && amd-smi version 2>/dev/null | awk -F'ROCm version: ' 'NF>1{split($2,a,"."); print "rocm"a[1]"."a[2]; ok=1; exit} END{exit !ok}'; } || { [ -r /opt/rocm/.info/version ] && awk -F. '{print "rocm"$1"."$2; exit}' /opt/rocm/.info/version; } || { command -v hipconfig >/dev/null 2>&1 && hipconfig --version 2>/dev/null | awk -F': *' '/HIP version/{split($2,a,"."); print "rocm"a[1]"."a[2]; ok=1; exit} END{exit !ok}'; } || { command -v dpkg-query >/dev/null 2>&1 && ver="$(dpkg-query -W -f="${Version}\n" rocm-core 2>/dev/null)" && [ -n "$ver" ] && awk -F'[.-]' '{print "rocm"$1"."$2; exit}' <<<"$ver"; } || { command -v rpm >/dev/null 2>&1 && ver="$(rpm -q --qf '%{VERSION}\n' rocm-core 2>/dev/null)" && [ -n "$ver" ] && awk -F'[.-]' '{print "rocm"$1"."$2; exit}' <<<"$ver"; })"; [ -n "$ROCM_TAG" ] && uv pip install "torch>=2.4,<2.11.0" "torchvision<0.26.0" "torchaudio<2.11.0" --index-url "https://download.pytorch.org/whl/$ROCM_TAG" --upgrade --force-reinstall
```

### 3. Install Unsloth

```bash
uv pip install unsloth[amd]
```

> [!warning] Required for AMD: install ROCm-compatible bitsandbytes
> All ROCm systems need a pre-release bitsandbytes build. Versions <= 0.49.2 have a 4-bit decode NaN bug on every AMD GPU. Use `pip` not `uv` for this step — `uv` rejects the pre-release wheel due to filename version mismatch.

```bash
# x86_64 systems:
pip install --force-reinstall --no-cache-dir --no-deps \
    "https://github.com/bitsandbytes-foundation/bitsandbytes/releases/download/continuous-release_main/bitsandbytes-1.33.7.preview-py3-none-manylinux_2_24_x86_64.whl"

# aarch64 systems: replace x86_64 with aarch64 in the URL above

# Fallback if the URL is unreachable:
# pip install --force-reinstall --no-cache-dir --no-deps "bitsandbytes>=0.49.1"
```

### 4. Start Fine-tuning

**Set environment variables:**

```bash
export HSA_OVERRIDE_GFX_VERSION=9.4.2  # Required for AMD MI300X
export HF_HUB_DISABLE_XET=1            # Fixes HuggingFace download issues on AMD
```

> [!note] `HSA_OVERRIDE_GFX_VERSION=9.4.2` tells ROCm to treat your GPU as gfx942 (MI300X). Without this, some kernels may fail to compile or run.

**Load and configure model:**

```python
from unsloth import FastModel

model, tokenizer = FastModel.from_pretrained(
    model_name = "unsloth/gemma-4-26b-a4b-it",
    max_seq_length = 2048,
    load_in_4bit = True,
)

model = FastModel.get_peft_model(
    model,
    r = 16,
    lora_alpha = 16,
    target_modules = ["q_proj", "k_proj", "v_proj", "o_proj"],
)
```

**Train:**

```python
from trl import SFTTrainer, SFTConfig

trainer = SFTTrainer(
    model = model,
    tokenizer = tokenizer,
    train_dataset = dataset,
    formatting_func = formatting_func,
    args = SFTConfig(
        per_device_train_batch_size = 1,
        gradient_accumulation_steps = 4,
        max_steps = 60,
        output_dir = "outputs",
        report_to = "none",
    ),
)

trainer_stats = trainer.train()
```

> [!note] On AMD GPUs, Flash Attention 2 is not available. Unsloth automatically falls back to Xformers (equivalent ROCm performance). The warning can be safely ignored.

## Reinforcement Learning on AMD

Example: [gpt-oss RL auto win 2048](https://github.com/unslothai/notebooks/blob/main/nb/gpt_oss_\(20B\)_Reinforcement_Learning_2048_Game_BF16.ipynb) on MI300X (192GB). LLM (gpt-oss 20B) auto-devises strategies to win 2048; high reward for winning, low for failing. Reward increases after ~300 steps.

Also: [automatic kernel gen RL notebook](https://github.com/unslothai/notebooks/blob/main/nb/gpt_oss_\(20B\)_GRPO_BF16.ipynb) — auto-creates matrix multiplication kernels in Python, learns Strassen algorithm. Includes multiple methods to counteract reward hacking.

## AMD Free One-click Notebooks

Free 192GB VRAM MI300X GPUs via AMD Dev Cloud (no signup/card required):

- [Qwen3 (32B)](https://oneclickamd.ai/github/unslothai/notebooks/blob/main/nb/Qwen3_\(32B\)_A100-Reasoning-Conversational.ipynb)
- [Llama 3.3 (70B)](https://oneclickamd.ai/github/unslothai/notebooks/blob/main/nb/Llama3.3_\(70B\)_A100-Conversational.ipynb)
- [Qwen3 (14B)](http://oneclickamd.ai/github/unslothai/notebooks/blob/main/nb/Qwen3_\(14B\)-Reasoning-Conversational.ipynb)
- [Mistral v0.3 (7B)](http://oneclickamd.ai/github/unslothai/notebooks/blob/main/nb/Mistral_v0.3_\(7B\)-Alpaca.ipynb)
- [GPT OSS MXFP4 (20B)](http://oneclickamd.ai/github/unslothai/notebooks/blob/main/nb/Kaggle-GPT_OSS_MXFP4_\(20B\)-Inference.ipynb) — Inference
- [RL notebook](https://oneclickamd.ai/github/unslothai/notebooks/blob/main/nb/gpt_oss_(20B)_Reinforcement_Learning_2048_Game_BF16.ipynb)

Convert any Unsloth notebook by prepending `https://oneclickamd.ai/github/unslothai/notebooks/blob/main/nb` to the path.

Related: [[073-get-started-unsloth-notebooks|Unsloth Notebooks]]

#unsloth #amd #rocm #fine-tuning #gpu-installation
