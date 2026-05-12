---
title: Install Unsloth via Docker
url: https://unsloth.ai/docs/get-started/install/docker.md
source: llms
fetched_at: 2026-04-27T18:12:58.206461885-03:00
rendered_js: false
word_count: 539
summary: This document provides a comprehensive guide on how to install and use Unsloth via Docker containers, covering quickstart procedures, container structure, advanced configuration options like SSH keys, and troubleshooting GPU detection issues.
tags:
    - docker-installation
    - unsloth-setup
    - container-guide
    - gpu-access
    - jupyter-lab
    - docker-run
category: tutorial
optimized: true
optimized_at: 2026-04-27T21:30:00Z
---

# Install Unsloth via Docker

All dependencies pre-installed. Docker image: [**`unsloth/unsloth`**](https://hub.docker.com/r/unsloth/unsloth)

> [!tip] Unsloth Studio shares the same cache as notebooks and scripts to avoid unnecessary re-downloads.

## Quickstart

### 1. Install Docker + NVIDIA Container Toolkit

Install Docker via [Linux](https://docs.docker.com/engine/install/) or [Desktop](https://docs.docker.com/desktop/). Then:

```bash
export NVIDIA_CONTAINER_TOOLKIT_VERSION=1.17.8-1
sudo apt-get update && sudo apt-get install -y \
  nvidia-container-toolkit=${NVIDIA_CONTAINER_TOOLKIT_VERSION} \
  nvidia-container-toolkit-base=${NVIDIA_CONTAINER_TOOLKIT_VERSION} \
  libnvidia-container-tools=${NVIDIA_CONTAINER_TOOLKIT_VERSION} \
  libnvidia-container1=${NVIDIA_CONTAINER_TOOLKIT_VERSION}
```

### 2. Run Container

```bash
docker run -d -e JUPYTER_PASSWORD="mypassword" \
  -p 8888:8888 -p 8000:8000 -p 2222:22 \
  -v $(pwd)/work:/workspace/work \
  --gpus all \
  unsloth/unsloth
```

### 3. Access Jupyter Lab

Go to [http://localhost:8888](http://localhost:8888/) and open Unsloth. Access `unsloth-notebooks` tabs for example notebooks.

### 4. Start Training

Follow the [[064-get-started-fine-tuning-llms-guide|Fine-tuning Guide]], [[072-get-started-reinforcement-learning-rl-guide|RL Guide]], or browse [[073-get-started-unsloth-notebooks|premade notebooks]].

## Container Structure

- `/workspace/work/` — Mounted work directory
- `/workspace/unsloth-notebooks/` — Example fine-tuning notebooks
- `/home/unsloth/` — User home directory

## Full Example

```bash
docker run -d -e JUPYTER_PORT=8000 \
  -e JUPYTER_PASSWORD="mypassword" \
  -e "SSH_KEY=$(cat ~/.ssh/container_key.pub)" \
  -e USER_PASSWORD="unsloth2024" \
  -p 8000:8000 -p 2222:22 \
  -v $(pwd)/work:/workspace/work \
  --gpus all \
  unsloth/unsloth
```

### SSH Key Setup

```bash
# Generate new key pair
ssh-keygen -t rsa -b 4096 -f ~/.ssh/container_key

# Use the public key in docker run
-e "SSH_KEY=$(cat ~/.ssh/container_key.pub)"

# Connect via SSH
ssh -i ~/.ssh/container_key -p 2222 unsloth@localhost
```

## Environment Variables

| Variable | Description | Default |
|---|---|---|
| `JUPYTER_PASSWORD` | Jupyter Lab password | `unsloth` |
| `JUPYTER_PORT` | Jupyter Lab port inside container | `8888` |
| `SSH_KEY` | SSH public key for authentication | `None` |
| `USER_PASSWORD` | Password for `unsloth` user (sudo) | `unsloth` |

Port mapping: `-p <host_port>:<container_port>`
- Jupyter Lab: `-p 8000:8888`
- SSH access: `-p 2222:22`

> [!warning] Use volume mounts to preserve work between container runs.
> `-v <local_folder>:<container_folder>`

## Why Unsloth Containers

- **Reliable** — curated env with stable packages. 7 GB compressed (vs 10–11 GB elsewhere)
- **Ready-to-use** — pre-installed notebooks in `/workspace/unsloth-notebooks/`
- **Secure** — runs as non-root user
- **Universal** — compatible with all transformer-based models (TTS, BERT, etc.)

## Security Notes

- Container runs as non-root `unsloth` user by default
- `USER_PASSWORD` for sudo operations inside container
- SSH requires public key authentication

## GPU Not Detected

```bash
docker pull unsloth/unsloth:latest
```

- `docker run`: use `--gpus all`
- Docker Compose: use `capabilities: [gpu]`
- Linux: ensure NVIDIA Container Toolkit is installed
- Windows: verify `nvcc --version` matches `nvidia-smi` CUDA version. Follow https://docs.docker.com/desktop/features/gpu/

#unsloth #docker #installation #gpu
