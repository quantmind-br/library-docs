---
title: Offline / Local | Mistral Docs
url: https://docs.mistral.ai/mistral-vibe/local
source: sitemap
fetched_at: 2026-04-26T04:08:22.985520637-03:00
rendered_js: false
word_count: 489
summary: This document provides instructions for deploying the Devstral model locally on custom infrastructure to be used as a coding assistant within the Mistral Vibe CLI.
tags:
    - local-deployment
    - devstral
    - model-inference
    - vllm
    - gpu-acceleration
    - cli-configuration
category: guide
optimized: true
optimized_at: 2026-04-26T00:00:00Z
---

Mistral Vibe supports local models, allowing you to deploy Devstral on your own infrastructure for offline use as a personal coding assistant CLI.

## Recommended Hardware

- **Devstral Small 2** ([HuggingFace](https://huggingface.co/mistralai/Devstral-Small-2-24B-Instruct-2512)): open-source, efficient for local usage
- **FP8 precision, 128k context**: requires H100 or A100 GPU
- **4-bit precision, 32k context**: requires RTX 4090 with 24GB VRAM
- **CPU offloading**: works on any machine with enough RAM (significantly slower)

> [!note]
> Any OpenAI-compatible server works with Mistral Vibe. vLLM is the recommended inference framework.

## Running Devstral with vLLM

```bash
vllm serve mistralai/Devstral-Small-2-24B-Instruct-2512 --port 8080
```

| Flag | Purpose |
|------|---------|
| `--tensor-parallel-size` | Use multiple GPUs |
| `--dtype` | Lower precision (e.g., `fp8`) |
| `--max-model-len` | Reduce context length |

## Connecting Mistral Vibe to Local Server

1. Start your local server on port **8080** (default)
2. Run `/config` in Mistral Vibe and select the **"local"** model
3. Create a preset for your local model to switch between providers

> [!tip]
> Create separate presets for local and Mistral AI API models to switch providers easily.

Learn more: [[133-mistral-vibe-terminal-configuration|Configuration]] #local-deployment #devstral #vllm