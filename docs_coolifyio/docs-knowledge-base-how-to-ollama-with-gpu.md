---
title: Ollama with GPU
url: https://coolify.io/docs/knowledge-base/how-to/ollama-with-gpu.md
source: llms
fetched_at: 2026-02-17T14:40:44.576412-03:00
rendered_js: false
word_count: 98
summary: This document outlines the requirements and configuration steps for self-hosting Ollama with GPU acceleration using Coolify and Docker. It covers hardware prerequisites, software installation for NVIDIA support, and deployment settings for managing large language models.
tags:
    - ollama
    - gpu-acceleration
    - nvidia-container-toolkit
    - coolify
    - self-hosting
    - docker-deployment
    - llm
category: guide
---

# Ollama with GPU

Based on the detailed guide from [geek.sg](https://geek.sg/blog/how-i-self-hosted-llama-32-with-coolify-on-my-home-server-a-step-by-step-guide?ref=coolify.io):

1. **Hardware Requirements**
   * A server with NVIDIA GPU (tested with RTX 3060 12GB)
   * Minimum 32GB RAM recommended
   * Sufficient storage space for models

2. **Software Setup**
   * Install NVIDIA drivers
   * Install NVIDIA Container Toolkit
   * Configure Docker to use NVIDIA runtime

3. **Coolify Configuration**
   * Deploy Ollama through Coolify's one-click installer
   * Modify the Docker compose configuration to include GPU support
   * Add required environment variables for GPU acceleration

4. **Model Management**
   * Pull and manage your preferred LLM models
   * Monitor GPU usage and performance
   * Adjust model parameters as needed

For the complete detailed guide, visit the [original article](https://geek.sg/blog/how-i-self-hosted-llama-32-with-coolify-on-my-home-server-a-step-by-step-guide?ref=coolify.io).