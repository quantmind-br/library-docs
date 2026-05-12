---
title: Unsloth Requirements
url: https://unsloth.ai/docs/get-started/fine-tuning-for-beginners/unsloth-requirements.md
source: llms
fetched_at: 2026-04-27T18:12:49.095011572-03:00
rendered_js: false
word_count: 862
summary: This document details the system requirements for using Unsloth across its various interfaces -- Unsloth Studio (web UI) and Unsloth Core (code-based) -- detailing needs for Windows, macOS, Linux, and CPU-only usage. It also provides tables outlining minimum VRAM requirements for fine-tuning different model sizes.
tags:
    - unsloth-requirements
    - hardware-support
    - windows-macos-linux
    - vram-needs
    - gpu-compatibility
    - installation-guide
category: reference
optimized: true
optimized_at: 2026-04-27T21:15:00Z
---

# Unsloth Requirements

Two interfaces: [[098-new-studio-install|Unsloth Studio]] (web UI) and [[058-get-started-install|Unsloth Core]] (code-based). Each has different requirements.

## Unsloth Studio Requirements

- **Mac**: Chat + Data Recipes work now. MLX training coming soon.
- **CPU**: Works without GPU for Chat + Data Recipes.
- **Training**: NVIDIA (RTX 30/40/50, Blackwell, DGX Spark/Station) + Intel GPUs. AMD and Apple MLX coming soon.

### Windows

- Windows 10 or 11 (64-bit)
- NVIDIA GPU with drivers installed
- **App Installer** (includes `winget`): [here](https://learn.microsoft.com/en-us/windows/msix/app-installer/install-update-app-installer)
- **Git**: `winget install --id Git.Git -e --source winget`
- **Python**: 3.11 up to, but not including, 3.14
- Work inside a Python environment (**uv**, **venv**, or **conda/mamba**)

### macOS

- macOS 12 Monterey or newer (Intel or Apple Silicon)
- Install Homebrew: [here](https://brew.sh/)
- Git: `brew install git`
- cmake: `brew install cmake`
- openssl: `brew install openssl`
- Python: 3.11 up to, but not including, 3.14
- Work inside a Python environment (**uv**, **venv**, or **conda/mamba**)

### Linux & WSL

- Ubuntu 20.04+ or similar distro (64-bit)
- NVIDIA GPU with drivers installed
- CUDA toolkit (12.4+ recommended, 12.8+ for Blackwell)
- Git: `sudo apt install git`
- Python: 3.11 up to, but not including, 3.14
- Work inside a Python environment (**uv**, **venv**, or **conda/mamba**)

### CPU Only

Same as Linux (except NVIDIA GPU drivers) and macOS. Supports Chat (GGUF models) and Data Recipes.

### Studio Training

Currently NVIDIA GPUs only. **Python 3.11-3.13** required.

| Requirement      | Linux / WSL                              | Windows                                       |
| ---------------- | ---------------------------------------- | --------------------------------------------- |
| **Git**          | Usually preinstalled                     | Installed by setup script (`winget`)          |
| **CMake**        | Preinstalled or `sudo apt install cmake` | Installed by setup script (`winget`)          |
| **C++ compiler** | `build-essential`                        | Visual Studio Build Tools 2022                |
| **CUDA Toolkit** | Optional; `nvcc` auto-detected           | Installed by setup script (matched to driver) |

## Unsloth Core Requirements

- **OS**: Linux and [[057-get-started-install-windows-installation|Windows]]
- **GPU**: NVIDIA GPUs since 2018+ including [[105-blog-fine-tuning-llms-with-blackwell-rtx-50-series-and-unsloth|Blackwell RTX 50]] and [[106-blog-fine-tuning-llms-with-nvidia-dgx-spark-and-unsloth|DGX Spark]]
- **CUDA Capability**: minimum 7.0 (V100, T4, Titan V, RTX 20 & 50, A100, H100, L40 etc) -- [Check your GPU](https://developer.nvidia.com/cuda-gpus). GTX 1070/1080 works but is slow.
- **Docker**: official image `unsloth/unsloth` on [Docker Hub](https://hub.docker.com/r/unsloth/unsloth) -- see [[052-get-started-install-docker|Docker install]]
- **AMD/Intel**: supported via [[051-get-started-install-amd|AMD]] and [[053-get-started-install-intel|Intel]] guides
- **Dependencies**: `xformers`, `torch`, `BitsandBytes`, `triton`
- Python 3.13 is supported
- `pip install unsloth` auto-installs latest compatible versions of all libraries

### Fine-tuning VRAM Requirements

> [!info] OOM fix: reduce batch size to 1, 2, or 3. For context length benchmarks, see [[118-basics-unsloth-benchmarks|Unsloth Benchmarks]].

QLoRA = 4-bit, LoRA = 16-bit. Values are absolute minimums; some models may require more.

| Model parameters | QLoRA (4-bit) VRAM | LoRA (16-bit) VRAM |
| ---------------- | ------------------ | ------------------ |
| 3B               | 3.5 GB             | 8 GB               |
| 7B               | 5 GB               | 19 GB              |
| 8B               | 6 GB               | 22 GB              |
| 9B               | 6.5 GB             | 24 GB              |
| 11B              | 7.5 GB             | 29 GB              |
| 14B              | 8.5 GB             | 33 GB              |
| 27B              | 22 GB              | 64 GB              |
| 32B              | 26 GB              | 76 GB              |
| 40B              | 30 GB              | 96 GB              |
| 70B              | 41 GB              | 164 GB             |
| 81B              | 48 GB              | 192 GB             |
| 90B              | 53 GB              | 212 GB             |
| 405B             | 237 GB             | 950 GB             |

#unsloth #requirements #hardware #vram #gpu
