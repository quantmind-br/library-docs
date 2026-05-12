---
title: Fine-tuning LLMs with Blackwell, RTX 50 series & Unsloth
url: https://unsloth.ai/docs/blog/fine-tuning-llms-with-blackwell-rtx-50-series-and-unsloth.md
source: llms
fetched_at: 2026-04-27T18:15:27.395222573-03:00
rendered_js: false
word_count: 704
summary: This document provides comprehensive instructions on how to fine-tune Large Language Models (LLMs) using Unsloth, detailing installation methods across various environments including pip, uv, Docker, Conda/mamba, and WSL. It also highlights compatibility with new NVIDIA Blackwell architecture GPUs like the RTX 50 series.
tags:
    - llm-fine-tuning
    - blackwell-gpu
    - unsloth
    - nvidia-rtx-50
    - installation-guide
    - docker-support
category: tutorial
optimized: true
optimized_at: 2026-04-27T21:30:00Z
---

# Fine-tuning LLMs with Blackwell, RTX 50 series & Unsloth

Unsloth supports NVIDIA Blackwell architecture: RTX 50-series (5060-5090), RTX PRO 6000, B200, B40, GB100, GB102, and more. Compatible with every NVIDIA GPU from 2018+ including [[106-blog-fine-tuning-llms-with-nvidia-dgx-spark-and-unsloth|DGX Spark]].

Official [NVIDIA blog post](https://developer.nvidia.com/blog/train-an-llm-on-an-nvidia-blackwell-desktop-with-unsloth-and-scale-it/).

> [!tip] Docker
> [**`unsloth/unsloth`**](https://hub.docker.com/r/unsloth/unsloth) supports Blackwell. See [[107-blog-how-to-fine-tune-llms-with-unsloth-and-docker|Docker guide]].

## Pip Install

```bash
pip install unsloth
```

Isolated environment alternative:

```bash
python -m venv unsloth
source unsloth/bin/activate
pip install unsloth
```

Note: may be `pip3`/`pip3.13` and `python3`/`python3.13`.

### Xformers Build from Source (if issues)

```bash
# First uninstall xformers installed by previous libraries
pip uninstall xformers -y

# Clone and build
pip install ninja
export TORCH_CUDA_ARCH_LIST="12.0"
git clone --depth=1 https://github.com/facebookresearch/xformers --recursive
cd xformers && python setup.py install && cd ..
```

## Docker

Use [`unsloth/unsloth`](https://hub.docker.com/r/unsloth/unsloth) -- same image for Blackwell and 50-series, no separate image needed. See [[107-blog-how-to-fine-tune-llms-with-unsloth-and-docker|Docker guide]] for instructions.

## uv

```bash
uv pip install unsloth
```

### uv (Advanced)

Installation order matters -- overwrite bundled dependencies with specific versions (`xformers`, `triton`).

1. Install `uv`:

```bash
curl -LsSf https://astral.sh/uv/install.sh | sh && source $HOME/.local/bin/env
```

Create project and venv:

```bash
mkdir 'unsloth-blackwell' && cd 'unsloth-blackwell'
uv venv .venv --python=3.12 --seed
source .venv/bin/activate
```

2. Install `vllm`:

```bash
uv pip install -U vllm --torch-backend=cu128
```

> [!warning] Must specify `cu128` -- otherwise vllm installs `torch==2.7.0` with `cu126`.

3. Install Unsloth dependencies:

```bash
uv pip install unsloth unsloth_zoo bitsandbytes
```

If xformers resolving issues occur, install from source without xformers:

```bash
uv pip install -qqq \
"unsloth_zoo[base] @ git+https://github.com/unslothai/unsloth-zoo" \
"unsloth[base] @ git+https://github.com/unslothai/unsloth"
```

4. Build xformers (optional -- faster and uses less memory; slow build):

```bash
pip uninstall xformers -y
pip install ninja
export TORCH_CUDA_ARCH_LIST="12.0"
git clone --depth=1 https://github.com/facebookresearch/xformers --recursive
cd xformers && python setup.py install && cd ..
```

Must set `TORCH_CUDA_ARCH_LIST=12.0` explicitly.

5. Update transformers (latest recommended):

```bash
uv pip install -U transformers
```

## Conda or mamba (Advanced)

1. Install conda/mamba:

```bash
curl -L -O "https://github.com/conda-forge/miniforge/releases/latest/download/Miniforge3-$(uname)-$(uname -m).sh"
bash Miniforge3-$(uname)-$(uname -m).sh
```

Create and activate environment:

```bash
conda create --name unsloth-blackwell python==3.12 -y
conda activate unsloth-blackwell
```

2. Install vllm (must specify `cu128`):

```bash
pip install -U vllm --extra-index-url https://download.pytorch.org/whl/cu128
```

3. Install Unsloth dependencies:

```bash
pip install unsloth unsloth_zoo bitsandbytes
```

4. Build xformers (optional):

```bash
pip uninstall xformers -y
pip install ninja
export TORCH_CUDA_ARCH_LIST="12.0"
git clone --depth=1 https://github.com/facebookresearch/xformers --recursive
cd xformers && python setup.py install && cd ..
```

5. Update triton (`triton>=3.3.1` required for Blackwell):

```bash
pip install -U triton>=3.3.1
```

6. Update transformers:

```bash
uv pip install -U transformers
```

Using mamba: replace `conda` with `mamba` in all commands above.

## WSL-Specific Notes

If using WSL and encountering xformers compilation issues (xformers is optional but faster):

1. **Increase WSL memory limit** -- create/edit `.wslconfig` in Windows user directory (`C:\Users\YourUsername\.wslconfig`):

```bash
[wsl2]
memory=16GB  # Minimum 16GB recommended for xformers compilation
processors=4  # Adjust based on your CPU cores
swap=2GB
localhostForwarding=true
```

Restart WSL:

```powershell
wsl --shutdown
```

2. **Install xformers with optimized flags**:

```bash
export TORCH_CUDA_ARCH_LIST="12.0"
pip install -v --no-build-isolation -U git+https://github.com/facebookresearch/xformers.git@main#egg=xformers
```

`--no-build-isolation` helps avoid build issues in WSL environments.

#llm-fine-tuning #blackwell #unsloth #installation
