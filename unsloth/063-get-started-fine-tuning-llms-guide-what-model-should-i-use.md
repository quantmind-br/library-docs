---
title: What Model Should I Use for Fine-tuning?
url: https://unsloth.ai/docs/get-started/fine-tuning-llms-guide/what-model-should-i-use.md
source: llms
fetched_at: 2026-04-27T18:13:06.546779864-03:00
rendered_js: false
word_count: 768
summary: This document provides a guide on how to select the appropriate LLM model for fine-tuning based on specific criteria, including use case, available compute/storage, and dataset size, while also explaining the differences between base and instruct models.
tags:
    - llm-selection
    - fine-tuning
    - model-choice
    - base-vs-instruct
    - model-types
    - training-guide
category: guide
optimized: true
optimized_at: 2026-04-27T21:30:00Z
---

# What Model Should I Use for Fine-tuning?

## Choosing a Model

1. **Match model to use case** — Image training: vision model (e.g., Llama 3.2 Vision). Code datasets: specialized model (e.g., Qwen Coder 2.5). Check [licensing and system requirements](https://unsloth.ai/docs/fine-tuning-for-beginners/unsloth-requirements#system-requirements).
2. **Assess storage, compute, and dataset** — Use [VRAM guidelines](https://unsloth.ai/docs/fine-tuning-for-beginners/unsloth-requirements#approximate-vram-requirements-based-on-model-parameters) to determine requirements. Dataset determines model type and training time.
3. **Select model and parameters** — Use the latest model for best performance. Browse the [[114-get-started-unsloth-model-catalog|model catalog]] for current options.
4. **Choose base vs. instruct** — See section below.

## Instruct vs. Base Model

- **Instruct models** — Pre-trained with built-in instructions; work out of the box with conversational chat templates (ChatML, ShareGPT).
- **Base models** — Original pre-trained versions without instruction fine-tuning; designed for customization. Compatible with instruction-style templates ([Alpaca, Vicuna](https://unsloth.ai/docs/basics/chat-templates)) but not conversational chat templates natively.

### Decision Guide

| Dataset Size | Recommendation |
|---|---|
| 1,000+ rows | Fine-tune the **base** model |
| 300–1,000 rows (high quality) | Base or instruct both viable |
| < 300 rows | Fine-tune the **instruct** model |

Dataset sizing details: [Datasets Guide](https://unsloth.ai/docs/get-started/datasets-guide#how-big-should-my-dataset-be)

## Fine-tuning Models with Unsloth

Change model name to match Hugging Face (e.g., `unsloth/llama-3.1-8b-unsloth-bnb-4bit`). Recommend starting with **Instruct models** (conversational chat templates, less data required) over **Base models** (Alpaca/Vicuna templates).

### Model Name Suffixes

- **`unsloth-bnb-4bit`** — Unsloth dynamic 4-bit quants; slightly more VRAM than standard BitsAndBytes 4-bit but significantly higher accuracy ([details](https://unsloth.ai/blog/dynamic-4bit))
- **`bnb-4bit`** (no "unsloth") — Standard BitsAndBytes 4-bit quantization
- **No suffix** — Original 16-bit or 8-bit; may include chat template or tokenizer fixes — use Unsloth versions when available

> [!tip] Experimentation is Key
> Fine-tune each model type and evaluate outputs to see which aligns better with your goals.

#llm-selection #fine-tuning #model-choice #unsloth
