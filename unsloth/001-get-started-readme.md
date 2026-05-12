---
title: Unsloth Docs
url: https://unsloth.ai/docs/get-started/readme.md
source: llms
fetched_at: 2026-04-27T18:12:49.067790693-03:00
rendered_js: false
word_count: 768
summary: This document serves as the main hub for Unsloth documentation, guiding users on how to run and train AI models locally. It highlights features like accelerated training, extensive model support, and provides quickstart guides for different operating systems.
tags:
    - local-llm
    - ai-training
    - model-serving
    - unsloth-studio
    - fine-tuning-guide
    - reinforcement-learning
category: guide
optimized: true
optimized_at: 2026-04-27T21:42:00Z
---

# Unsloth Docs

Unsloth lets you run and train AI models on your own local hardware. Supports MacOS, Linux, Windows, NVIDIA, Intel, and CPU setups.

## Key Resources

- [[006-models-tutorials-ibm-granite-4.0|IBM Granite 4.0]]
- [[007-models-gemma-4-train|Gemma 4 Fine-tuning Guide]]
- [[015-models-kimi-k2.6|Kimi K2.6]]
- [[097-new-studio|Unsloth Studio]]
- [[021-models-qwen3.5|Qwen3.5]]
- [[002-models-glm-5.1|GLM-5.1]]

## Quick Links

| Topic | Doc |
|-------|-----|
| Fine-tuning LLMs | [[064-get-started-fine-tuning-llms-guide\|Fine-tuning LLMs Guide]] |
| Notebooks | [[073-get-started-unsloth-notebooks\|Unsloth Notebooks]] |
| Model Catalog | [[114-get-started-unsloth-model-catalog\|Unsloth Model Catalog]] |
| Tutorials | [[050-models-tutorials\|LLM Tutorials]] |

## Why Unsloth

- Directly collaborates with teams behind gpt-oss, Qwen3, Llama 4, Mistral, Gemma 1-3, Phi-4; fixed critical bugs improving model accuracy
- Supports inference and training for **500+ models**: vision, TTS, embedding, RL
- Streamlines local training, inference, data, and deployment

## Features

### Inference

- Search + download + run GGUFs, LoRA adapters, safetensors
- Self-healing tool calling, web search, OpenAI-compatible API calls
- Auto inference parameter tuning, chat template editing
- Export/save to GGUF, 16-bit safetensor
- Side-by-side model output comparison (model arena)

### Training

- Train and [[072-get-started-reinforcement-learning-rl-guide|RL]] 500+ models ~2x faster with ~70% less VRAM (no accuracy loss)
- Supports full fine-tuning, pre-training, 4-bit, 16-bit, FP8 training
- Auto-create datasets from PDF, CSV, DOCX; visual node workflow editor
- Live training monitoring: loss, GPU usage, customizable graphs
- Most efficient [[072-get-started-reinforcement-learning-rl-guide|reinforcement learning]] library (80% less VRAM for GRPO, FP8)
- [[093-basics-multi-gpu-training-with-unsloth|Multi-GPU]] support

## Quickstart

### MacOS, Linux, WSL

```bash
curl -fsSL https://unsloth.ai/install.sh | sh
```

### Windows PowerShell

```bash
irm https://unsloth.ai/install.ps1 | iex
```

### Docker

Official image: `unsloth/unsloth` (Windows, WSL, Linux; MacOS coming soon)

### Launch Unsloth

```bash
unsloth studio -H 0.0.0.0 -p 8888
```

## Fine-tuning and RL

[[064-get-started-fine-tuning-llms-guide|Fine-tuning]] a pre-trained LLM customizes behavior, enhances domain knowledge, optimizes task performance:

- **Update Knowledge**: introduce domain-specific information
- **Customize Behavior**: adjust tone, personality, response style
- **Optimize for Tasks**: improve accuracy/relevance for specific use cases

[[072-get-started-reinforcement-learning-rl-guide|Reinforcement Learning (RL)]] trains an agent via environment interaction with reward/penalty feedback:

- **Action**: what the model generates
- **Reward**: quality signal (instruction-following, helpfulness)
- **Environment**: the scenario or task

Example use-cases: predict headline impact on companies, custom responses from historical interactions, legal text analysis for contracts and compliance.

> [!info] Fine-tuning can replicate all of RAG's capabilities, but not vice versa.

## Further Reading

| Topic | Doc |
|-------|-----|
| FAQ: Is fine-tuning right for me? | [[122-get-started-fine-tuning-for-beginners-faq-+-is-fine-tuning-right-for-me\|FAQ]] |
| Inference & Deployment | [[091-basics-inference-and-deployment\|Inference & Deployment]] |
| RL Guide | [[072-get-started-reinforcement-learning-rl-guide\|RL Guide]] |
| Dynamic GGUFs | [[115-basics-unsloth-dynamic-2.0-ggufs\|Unsloth Dynamic 2.0 GGUFs]] |

#local-llm #fine-tuning #unsloth-studio #reinforcement-learning #model-serving
