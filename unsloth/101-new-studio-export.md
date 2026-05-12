---
title: Export models with Unsloth Studio
url: https://unsloth.ai/docs/new/studio/export.md
source: llms
fetched_at: 2026-04-27T18:13:27.345260925-03:00
rendered_js: false
word_count: 516
summary: This document serves as a guide detailing how to use Unsloth Studio to export, save, and convert machine learning models into various formats like GGUF, Safetensors, or LoRA for deployment across multiple platforms.
tags:
    - unsloth-studio
    - model-exporting
    - gguf-conversion
    - lora-weights
    - checkpoint-management
    - hugging-face-hub
category: guide
optimized: true
optimized_at: 2026-04-27T21:30:00Z
---

# Export Models with Unsloth Studio

Export, save, or convert models to GGUF, Safetensors, or LoRA for deployment in Unsloth, llama.cpp, Ollama, vLLM, and more. Export a trained checkpoint or convert any existing model.

## Steps

### 1. Select Training Run

Each run represents a complete training session with multiple checkpoints.

### 2. Select Checkpoint

Later checkpoints typically represent the final trained model, but any checkpoint can be exported.

### 3. Choose Export Method

| Export Type | Description |
|---|---|
| Merged Model | **16-bit model** with LoRA adapter merged into base weights |
| LoRA Only | Exports **only the adapter weights**; requires the original base model |
| GGUF / llama.cpp | **GGUF format** for Unsloth / llama.cpp / Ollama / LM Studio inference |

### 4. Export / Save Locally

Download exported model files directly to your machine for local inference, manual distribution, or local inference tools.

### 5. Push to Hub

Upload to Hugging Face Hub for hosting, sharing, and deployment. Requires a Hugging Face write token.

> [!tip] CLI auth
> If already authenticated with the Hugging Face CLI, the write token can be left empty.

#unsloth-studio #model-export #gguf
