---
title: Unsloth Studio Installation
url: https://unsloth.ai/docs/new/studio/install.md
source: llms
fetched_at: 2026-04-27T18:13:24.377054153-03:00
rendered_js: false
word_count: 1402
summary: This document serves as a comprehensive installation and setup guide for Unsloth Studio across various operating systems, including Windows, macOS, Linux, WSL, and Docker. It details standard installation commands, launch procedures, system requirements, and advanced developer installation/uninstallation methods.
tags:
    - unsloth-studio
    - installation-guide
    - system-requirements
    - os-setup
    - docker-integration
    - developer-tools
category: guide
optimized: true
optimized_at: 2026-04-27T21:30:00Z
---

# Unsloth Studio Installation

Works on Windows, Linux, WSL, and MacOS. Same install process on every device.

- **Mac:** Like CPU -- [[099-new-studio-chat|Chat]] + [[100-new-studio-data-recipe|Data Recipes]] work now. MLX training coming soon.
- **CPU:** Works without GPU for Chat + Data Recipes.
- **Training:** NVIDIA (RTX 30/40/50, Blackwell, DGX Spark/Station) + Intel GPUs.
- **Coming soon:** Apple MLX, AMD.

## Install & Launch

### 1. Install Unsloth

**MacOS, Linux, WSL:**

```bash
curl -fsSL https://unsloth.ai/install.sh | sh
```

**Windows PowerShell:**

```bash
irm https://unsloth.ai/install.ps1 | iex
```

> [!tip] First install now 6x faster, 50% reduced size (precompiled llama.cpp binaries).
> WSL users: prompted for `sudo` password for build deps (`cmake`, `git`, `libcurl4-openssl-dev`).

### 2. Launch Studio

```bash
unsloth studio -H 0.0.0.0 -p 8888
```

Open `http://localhost:8888` in your browser.

### 3. Onboarding

Create a password on first launch, sign in, then complete the brief onboarding wizard (model, dataset, settings) or skip it.

### 4. Start Training

See [[102-new-studio-start|Get started with Unsloth Studio]] for step-by-step guide.

### Update

```bash
unsloth studio update
```

If that fails, re-run the install command from step 1.

## System Requirements

### Windows

- Windows 10/11 (64-bit)
- NVIDIA GPU with drivers
- **App Installer** (includes `winget`): [link](https://learn.microsoft.com/en-us/windows/msix/app-installer/install-update-app-installer)
- **Git:** `winget install --id Git.Git -e --source winget`
- **Python:** 3.11 to <3.14
- Use **uv**, **venv**, or **conda/mamba**

### MacOS

- macOS 12 Monterey+ (Intel or Apple Silicon)
- Homebrew: [brew.sh](https://brew.sh/)
- `brew install git cmake openssl`
- **Python:** 3.11 to <3.14
- Use **uv**, **venv**, or **conda/mamba**

### Linux & WSL

- Ubuntu 20.04+ or similar (64-bit)
- NVIDIA GPU with drivers
- CUDA toolkit (12.4+ recommended, 12.8+ for Blackwell)
- `sudo apt install git`
- **Python:** 3.11 to <3.14
- Use **uv**, **venv**, or **conda/mamba**

### Docker

> [!success] Docker image now works for Studio (Mac compatibility in progress).

```bash
docker pull unsloth/unsloth
docker run -d -e JUPYTER_PASSWORD="mypassword" \
  -p 8888:8888 -p 8000:8000 -p 2222:22 \
  -v $(pwd)/work:/workspace/work \
  --gpus all \
  unsloth/unsloth
```

Access at `http://localhost:8000` or `http://external_ip_address:8000/`. More info: [Docker Hub](https://hub.docker.com/r/unsloth/unsloth#unsloth-docker-image).

### CPU Only

Same as Linux (minus NVIDIA GPU drivers) and MacOS. Supports [[099-new-studio-chat|Chat]] for GGUF models and [[100-new-studio-data-recipe|Data Recipes]].

## Developer Installation

### From Main Repo

**macOS, Linux, WSL:**

```bash
git clone https://github.com/unslothai/unsloth
cd unsloth
./install.sh --local
unsloth studio -H 0.0.0.0 -p 8888
```

**Windows PowerShell:**

```powershell
winget install -e --id Python.Python.3.13 --source winget
winget install --id=astral-sh.uv  -e --source winget
winget install --id Git.Git -e --source winget
git clone https://github.com/unslothai/unsloth
cd unsloth
Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass
.\install.ps1 --local
unsloth studio -H 0.0.0.0 -p 8888
```

### Nightly Build

**macOS, Linux, WSL:**

```bash
git clone https://github.com/unslothai/unsloth
cd unsloth
git checkout nightly
./install.sh --local
```

Launch: `unsloth studio -H 0.0.0.0 -p 8888`

**Windows:**

```powershell
winget install -e --id Python.Python.3.13 --source winget
winget install --id=astral-sh.uv  -e --source winget
winget install --id Git.Git -e --source winget
git clone https://github.com/unslothai/unsloth
cd unsloth
git checkout nightly
Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass
.\install.ps1 --local
```

Launch: `unsloth studio -H 0.0.0.0 -p 8888`

## Uninstall

### 1. Remove Application

- **MacOS/WSL/Linux:** `rm -rf ~/.unsloth/studio/unsloth_studio`
- **Windows:** `Remove-Item -Recurse -Force "$HOME\.unsloth\studio\unsloth_studio"`

Keeps model checkpoints, exports, history, cache, and chats intact.

### 2. Remove Shortcuts & Symlinks

**macOS:**

```bash
rm -rf ~/Applications/Unsloth\ Studio.app ~/Desktop/Unsloth\ Studio
```

**Linux:**

```bash
rm -f ~/.local/share/applications/unsloth-studio.desktop ~/Desktop/unsloth-studio.desktop
```

**WSL/Windows (PowerShell):**

```bash
Remove-Item -Force "$HOME\Desktop\Unsloth Studio.lnk"
Remove-Item -Force "$env:APPDATA\Microsoft\Windows\Start Menu\Programs\Unsloth Studio.lnk"
```

### 3. Remove CLI Command

**macOS/Linux/WSL:** `rm -f ~/.local/bin/unsloth`

**Windows:** Remove the venv's `Scripts` directory from User PATH via Settings > System > About > Advanced system settings > Environment Variables.

### 4. Remove Everything (Optional)

- **MacOS/WSL/Linux:** `rm -rf ~/.unsloth`
- **Windows:** `Remove-Item -Recurse -Force "$HOME\.unsloth"`

> [!danger] `rm -rf` deletes everything including history, cache, and chats.

HF model files are stored separately and not removed by any step above.

### Deleting Cached HF Model Files

Delete from the bin icon in model search, or remove from the HF cache directory:

- **MacOS/Linux/WSL:** `~/.cache/huggingface/hub/`
- **Windows:** `%USERPROFILE%\.cache\huggingface\hub\`

If `HF_HUB_CACHE` or `HF_HOME` is set, use that location. On Linux/WSL, `XDG_CACHE_HOME` can also change the default cache root.

## Using Existing GGUF Models

Studio auto-detects older/pre-existing models from Hugging Face, LM Studio, etc. You can also select an existing folder for detection.

**Manual:** Studio detects models in HF Hub cache (`C:\Users\{username}\.cache\huggingface\hub`). LM Studio models are at `C:\Users\{username}\.cache\lm-studio\models` OR `C:\Users\{username}\lm-studio\models` -- copy `.gguf` files to the HF cache directory for Studio to load them.

## Google Colab

[Free Colab notebook](https://colab.research.google.com/github/unslothai/unsloth/blob/main/studio/Unsloth_Studio_Colab.ipynb) -- supports models up to 22B on T4 GPUs. Click "Run all", then scroll to "Start Unsloth Studio" and click the link.

> [!warning] Studio link may error with adblockers/Mozilla/disabled cookies -- scroll below the button instead. Colab may shut down GPU on inactivity.

## Troubleshooting

| Problem | Fix |
|---------|-----|
| Python version error | `sudo apt install python3.12 python3.12-venv` (3.11 to <3.14) |
| `nvidia-smi not found` | Install drivers from https://www.nvidia.com/Download/index.aspx |
| `nvcc not found` (CUDA) | `sudo apt install nvidia-cuda-toolkit` or add `/usr/local/cuda/bin` to PATH |
| llama-server build failed | Non-fatal (GGUF inference unavailable). Install `cmake` and re-run. |
| `cmake not found` | `sudo apt install cmake` |
| `git not found` | `sudo apt install git` |
| Build failed | Delete `~/.unsloth/llama.cpp` and re-run setup |

## Agent Query Endpoint

```
GET https://unsloth.ai/docs/new/studio/install.md?ask=<question>
```

#unsloth-studio #installation #docker
