---
title: How to Fine-tune LLMs with Unsloth & Docker
url: https://unsloth.ai/docs/blog/how-to-fine-tune-llms-with-unsloth-and-docker.md
source: llms
fetched_at: 2026-04-27T18:15:23.401607948-03:00
rendered_js: false
word_count: 517
summary: This document provides a step-by-step guide and reference material on how to easily fine-tune Large Language Models (LLMs) using Unsloth within a Docker container, detailing prerequisites, commands, and advanced configuration options.
tags:
    - llm-fine-tuning
    - unsloth
    - docker
    - tutorial
    - containerization
    - nvidia-toolkit
category: tutorial
optimized: true
optimized_at: 2026-04-27T21:15:00Z
---

# How to Fine-tune LLMs with Unsloth & Docker

Unsloth's [Docker image](https://hub.docker.com/r/unsloth/unsloth) (`unsloth/unsloth`) bypasses dependency issues -- pull and run, no setup needed. Works in [[112-get-started-fine-tuning-for-beginners-unsloth-requirements|all supported setups]] including Windows. Single image covers all GPUs including [[105-blog-fine-tuning-llms-with-blackwell-rtx-50-series-and-unsloth|Blackwell/50-series]]. For DGX Spark, use [[106-blog-fine-tuning-llms-with-nvidia-dgx-spark-and-unsloth|DGX guide]].

## Step-by-Step Tutorial

### 1. Install Docker and NVIDIA Container Toolkit

Install Docker via [Linux](https://docs.docker.com/engine/install/) or [Desktop](https://docs.docker.com/desktop/). Then install [NVIDIA Container Toolkit](https://docs.nvidia.com/datacenter/cloud-native/container-toolkit/latest/install-guide.html#installation):

```bash
export NVIDIA_CONTAINER_TOOLKIT_VERSION=1.17.8-1
sudo apt-get update && sudo apt-get install -y \
  nvidia-container-toolkit=${NVIDIA_CONTAINER_TOOLKIT_VERSION} \
  nvidia-container-toolkit-base=${NVIDIA_CONTAINER_TOOLKIT_VERSION} \
  libnvidia-container-tools=${NVIDIA_CONTAINER_TOOLKIT_VERSION} \
  libnvidia-container1=${NVIDIA_CONTAINER_TOOLKIT_VERSION}
```

### 2. Run the container

```bash
docker run -d -e JUPYTER_PASSWORD="mypassword" \
  -p 8888:8888 -p 2222:22 \
  -v $(pwd)/work:/workspace/work \
  --gpus all \
  unsloth/unsloth
```

### 3. Access Jupyter Lab

Go to [http://localhost:8888](http://localhost:8888/) -- open `unsloth-notebooks` tab for example notebooks.

### 4. Start training

Follow the [[064-get-started-fine-tuning-llms-guide|Fine-tuning Guide]], [[072-get-started-reinforcement-learning-rl-guide|RL Guide]], or use premade [[073-get-started-unsloth-notebooks|notebooks]].

## Container Structure

- `/workspace/work/` -- Mounted work directory
- `/workspace/unsloth-notebooks/` -- Example fine-tuning notebooks
- `/home/unsloth/` -- User home directory

## Full Usage Example

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

### SSH Key setup

```bash
# Generate new key pair
ssh-keygen -t rsa -b 4096 -f ~/.ssh/container_key

# Use the public key in docker run
-e "SSH_KEY=$(cat ~/.ssh/container_key.pub)"

# Connect via SSH
ssh -i ~/.ssh/container_key -p 2222 unsloth@localhost
```

## Advanced Settings

| Variable           | Description                        | Default   |
| ------------------ | ---------------------------------- | --------- |
| `JUPYTER_PASSWORD` | Jupyter Lab password               | `unsloth` |
| `JUPYTER_PORT`     | Jupyter Lab port inside container  | `8888`    |
| `SSH_KEY`          | SSH public key for authentication  | `None`    |
| `USER_PASSWORD`    | Password for `unsloth` user (sudo) | `unsloth` |

Port mapping: `-p <host_port>:<container_port>` -- Jupyter: `-p 8000:8888`, SSH: `-p 2222:22`.

> [!warning] Use volume mounts to preserve work between container runs: `-v <local_folder>:<container_folder>`

## Security

- Container runs as non-root `unsloth` user by default
- Use `USER_PASSWORD` for sudo operations inside container
- SSH access requires public key authentication

#unsloth #docker #fine-tuning #containerization
