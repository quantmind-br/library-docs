---
title: Install Unsloth via pip and uv
url: https://unsloth.ai/docs/get-started/install/pip-install.md
source: llms
fetched_at: 2026-04-27T18:12:53.495730736-03:00
rendered_js: false
word_count: 959
summary: This document serves as a comprehensive guide detailing multiple methods for installing, launching, and uninstalling Unsloth, covering both the Studio web UI version and the Core code-based version across different operating systems.
tags:
    - unsloth-installation
    - pip-setup
    - studio-cli
    - core-version
    - os-specific
    - python-env
category: guide
optimized: true
optimized_at: 2026-04-27T21:30:00Z
---

# Install Unsloth via pip and uv

Two modes: **Unsloth Studio** (web UI) and **Unsloth Core** (code library).

## Unsloth Studio

### Install

**macOS / Linux / WSL:**

```bash
curl -fsSL https://unsloth.ai/install.sh | sh
```

**Windows PowerShell:**

```bash
irm https://unsloth.ai/install.ps1 | iex
```

Same command updates; or use `unsloth studio update`.

### Launch

```bash
unsloth studio -H 0.0.0.0 -p 8888
```

For detailed Studio requirements, see [[098-new-studio-install|Studio install guide]].

### Install from Main Repo

**macOS / Linux / WSL:**

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

### Nightly Install

**macOS / Linux / WSL:**

```bash
git clone https://github.com/unslothai/unsloth
cd unsloth
git checkout nightly
./install.sh --local
```

**Windows:**

```bash
winget install -e --id Python.Python.3.13 --source winget
winget install --id=astral-sh.uv  -e --source winget
winget install --id Git.Git -e --source winget
git clone https://github.com/unslothai/unsloth
cd unsloth
git checkout nightly
Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass
.\install.ps1 --local
```

Then launch: `unsloth studio -H 0.0.0.0 -p 8888`

### Uninstall Studio

1. **Remove app** (keeps checkpoints, exports, history, cache, chats):
   - macOS/WSL/Linux: `rm -rf ~/.unsloth/studio/unsloth_studio`
   - Windows: `Remove-Item -Recurse -Force "$HOME\.unsloth\studio\unsloth_studio"`

2. **Remove shortcuts:**
   - **macOS:** `rm -rf ~/Applications/Unsloth\ Studio.app ~/Desktop/Unsloth\ Studio`
   - **Linux:** `rm -f ~/.local/share/applications/unsloth-studio.desktop ~/Desktop/unsloth-studio.desktop`
   - **WSL/Windows:** `Remove-Item -Force "$HOME\Desktop\Unsloth Studio.lnk"; Remove-Item -Force "$env:APPDATA\Microsoft\Windows\Start Menu\Programs\Unsloth Studio.lnk"`

3. **Remove CLI command:**
   - macOS/Linux/WSL: `rm -f ~/.local/bin/unsloth`
   - Windows: Remove venv `Scripts` entry from User PATH (Settings > System > About > Advanced system settings > Environment Variables > Path)

4. **Remove everything** (optional — deletes history, cache, chats, checkpoints, exports):
   - macOS/WSL/Linux: `rm -rf ~/.unsloth`
   - Windows: `Remove-Item -Recurse -Force "$HOME\.unsloth"`

> [!warning] `rm -rf` commands delete everything including history, cache, chats.

> [!note] HF model files are stored separately in HF cache. See **Deleting HF model files** below.

### Deleting Cached HF Model Files

Delete via bin icon in model search, or remove from cache directory:
- **macOS/Linux/WSL:** `~/.cache/huggingface/hub/`
- **Windows:** `%USERPROFILE%\.cache\huggingface\hub/`

If `HF_HUB_CACHE` or `HF_HOME` is set, use that location. On Linux/WSL, `XDG_CACHE_HOME` can override the default.

## Unsloth Core

### Recommended Install (uv pip)

```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
uv venv unsloth_env --python 3.13
source unsloth_env/bin/activate
uv pip install unsloth --torch-backend=auto
```

Or plain pip:

```bash
pip install unsloth
```

### With vLLM

```bash
uv pip install unsloth vllm --torch-backend=auto
```

### Latest Main Branch

```bash
uv pip install unsloth --torch-backend=auto
pip uninstall unsloth unsloth_zoo -y && pip install --no-deps git+https://github.com/unslothai/unsloth_zoo.git && pip install --no-deps git+https://github.com/unslothai/unsloth.git
```

### venv Install

```bash
apt install python3.10-venv python3.11-venv python3.12-venv python3.13-venv -y
python -m venv unsloth_env
source unsloth_env/bin/activate
pip install --upgrade pip && pip install uv
uv pip install unsloth --torch-backend=auto
```

> [!info] Python 3.13 is now supported!

In notebooks (Jupyter/Colab), prefix with `!`.

### Uninstall / Force Reinstall Core

```bash
pip install --upgrade --force-reinstall --no-cache-dir --no-deps unsloth
pip install --upgrade --force-reinstall --no-cache-dir --no-deps unsloth_zoo
```

## Advanced Pip Installation

> [!warning] Do NOT use this if you have Conda.

Pip differs per torch/CUDA version. Supported torch suffixes: `torch211`, `torch212`, `torch220`, `torch230`, `torch240`. CUDA suffixes: `cu118`, `cu121`, `cu124`. Ampere devices (A100, H100, RTX3090+): add `-ampere`.

Examples:

```bash
pip install --upgrade pip
pip install "unsloth[cu121-torch240] @ git+https://github.com/unslothai/unsloth.git"
```

```bash
pip install --upgrade pip
pip install "unsloth[cu124-torch250] @ git+https://github.com/unslothai/unsloth.git"
```

```bash
pip install "unsloth[cu121-ampere-torch240] @ git+https://github.com/unslothai/unsloth.git"
pip install "unsloth[cu118-ampere-torch240] @ git+https://github.com/unslothai/unsloth.git"
pip install "unsloth[cu121-torch240] @ git+https://github.com/unslothai/unsloth.git"
pip install "unsloth[cu118-torch240] @ git+https://github.com/unslothai/unsloth.git"

pip install "unsloth[cu121-torch230] @ git+https://github.com/unslothai/unsloth.git"
pip install "unsloth[cu121-ampere-torch230] @ git+https://github.com/unslothai/unsloth.git"

pip install "unsloth[cu121-torch250] @ git+https://github.com/unslothai/unsloth.git"
pip install "unsloth[cu124-ampere-torch250] @ git+https://github.com/unslothai/unsloth.git"
```

Auto-detect optimal pip command:

```bash
wget -qO- https://raw.githubusercontent.com/unslothai/unsloth/main/unsloth/_auto_install.py | python -
```

Or run manually in Python REPL:

```python
# Licensed under the Apache License, Version 2.0 (the "License")
try: import torch
except: raise ImportError('Install torch via `pip install torch`')
from packaging.version import Version as V
import re
v = V(re.match(r"[0-9\.]{3,}", torch.__version__).group(0))
cuda = str(torch.version.cuda)
is_ampere = torch.cuda.get_device_capability()[0] >= 8
USE_ABI = torch._C._GLIBCXX_USE_CXX11_ABI
if cuda not in ("11.8", "12.1", "12.4", "12.6", "12.8", "13.0"): raise RuntimeError(f"CUDA = {cuda} not supported!")
if   v <= V('2.1.0'): raise RuntimeError(f"Torch = {v} too old!")
elif v <= V('2.1.1'): x = 'cu{}{}-torch211'
elif v <= V('2.1.2'): x = 'cu{}{}-torch212'
elif v  < V('2.3.0'): x = 'cu{}{}-torch220'
elif v  < V('2.4.0'): x = 'cu{}{}-torch230'
elif v  < V('2.5.0'): x = 'cu{}{}-torch240'
elif v  < V('2.5.1'): x = 'cu{}{}-torch250'
elif v <= V('2.5.1'): x = 'cu{}{}-torch251'
elif v  < V('2.7.0'): x = 'cu{}{}-torch260'
elif v  < V('2.7.9'): x = 'cu{}{}-torch270'
elif v  < V('2.8.0'): x = 'cu{}{}-torch271'
elif v  < V('2.8.9'): x = 'cu{}{}-torch280'
elif v  < V('2.9.1'): x = 'cu{}{}-torch290'
elif v  < V('2.9.2'): x = 'cu{}{}-torch291'
else: raise RuntimeError(f"Torch = {v} too new!")
if v > V('2.6.9') and cuda not in ("11.8", "12.6", "12.8", "13.0"): raise RuntimeError(f"CUDA = {cuda} not supported!")
x = x.format(cuda.replace(".", ""), "-ampere" if False else "") # is_ampere is broken due to flash-attn
print(f'pip install --upgrade pip && pip install --no-deps git+https://github.com/unslothai/unsloth-zoo.git && pip install "unsloth[{x}] @ git+https://github.com/unslothai/unsloth.git" --no-build-isolation')
```

#unsloth #pip #installation #python #studio #core
