---
title: Fine-Tuning LLMs on NVIDIA DGX Station with Unsloth
url: https://unsloth.ai/docs/blog/dgx-station.md
source: llms
fetched_at: 2026-04-27T18:15:22.84910306-03:00
rendered_js: false
word_count: 889
summary: This guide explains how to fine-tune large language models (LLMs) like Qwen3.5 and GPT-OSS on an NVIDIA DGX Station using the Unsloth framework. It provides detailed steps for setup, dependency installation, and execution via Jupyter Notebooks.
tags:
    - llm-fine-tuning
    - nvidia-dgx-station
    - unsloth
    - ai-training
    - pytorch
    - notebook-guide
category: tutorial
optimized: true
optimized_at: 2026-04-27T21:30:00Z
---

# Fine-Tuning LLMs on NVIDIA DGX Station with Unsloth

Train LLMs locally on NVIDIA DGX Station with [Unsloth](https://github.com/unslothai/unsloth). DGX Station specs: **~200GB VRAM**, **700GB+ unified GPU/CPU memory**, Grace CPU + Blackwell GPU linked by NVLink-C2C.

This guide trains [Qwen3.5-35B-A3B](#qwen35-35b-a3b-training) and [gpt-oss-120b](#gpt-oss-120b-training) on DGX Station.

## Quickstart

Install Python dev headers:

```bash
sudo apt update
sudo apt install python3.12-dev
```

Create a fresh virtual environment to minimize dependency conflicts:

```bash
python3 -m venv .unsloth
source .unsloth/bin/activate
pip install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu130
```

> [!warning] Torch CUDA version
> Install `torch` from the CUDA 13 index first -- otherwise you may get the CPU version or an architecture mismatch.

Install Unsloth:

```bash
pip install unsloth
```

Install xformers (and optionally flash-attention from source -- takes time):

```bash
pip install --no-deps --no-build-isolation xformers==0.0.33.post1
# Optionally flash-attn
# Clone and build (targets sm_100 for B300)
git clone https://github.com/Dao-AILab/flash-attention
cd flash-attention
# B300 = sm_100, set arch explicitly
TORCH_CUDA_ARCH_LIST="10.0" MAX_JOBS=8 pip install . --no-build-isolation
cd ..
```

For Qwen 3.5 MoE, install additional kernel packages:

```bash
pip install --no-build-isolation flash-linear-attention causal_conv1d==1.6.0
```

Install Jupyter Notebook (if not already available):

```bash
pip install notebook
pip install ipywidgets
```

Download Unsloth notebooks (250+ notebooks for LLM training + Python scripts):

```bash
git clone https://github.com/unslothai/notebooks.git
cd notebooks
```

## Training Tutorials

Launch Jupyter Notebook:

```bash
jupyter notebook
```

Copy the `localhost` URL with token parameter into your browser. The `nb/` folder contains all notebooks.

### Qwen3.5-35B-A3B Training

Open `nb/Qwen3_5_MoE.ipynb`. Skip the installation section (already done). Navigate to the Unsloth section and start executing cells from there.

The notebook covers model setup, dataset preparation, and trainer configuration. Each step takes time (large model download, weight initialization, optimization). Training is fast with default settings -- plenty of memory available to experiment with hyperparameters.

After training: save the model locally, push to Hugging Face Hub, or export to a quantized format.

### gpt-oss-120b Training

Open `nb/gpt-oss-(120B)_A100-Fine-tuning.ipynb`. Skip installation section, navigate to the Unsloth section.

- Uses ~72 GB GPU memory
- Takes ~10 minutes
- Covers dataset preprocessing and trainer setup

After training: save locally, push to Hugging Face Hub, or export to GGUF format.

More info: <https://www.nvidia.com/en-us/products/workstations/dgx-station/>

#llm-fine-tuning #dgx-station #unsloth #blackwell
