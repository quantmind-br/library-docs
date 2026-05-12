---
title: LoRA Hot Swapping Guide
url: https://unsloth.ai/docs/basics/inference-and-deployment/vllm-guide/lora-hot-swapping-guide.md
source: llms
fetched_at: 2026-04-27T18:14:46.120500751-03:00
rendered_js: false
word_count: 196
summary: This document serves as a guide explaining how to enable and perform hot-swapping (dynamic updating) of LoRA adapters within vLLM. It provides commands for setting the environment flag, serving with LoRA support, loading/unloading adapters via cURL requests, and illustrates usage with Unsloth.
tags:
    - lora
    - hot-swapping
    - vllm
    - dynamic-lora
    - adapter-serving
    - inference
category: guide
optimized: true
optimized_at: 2026-04-27T21:30:00Z
---

# LoRA Hot Swapping Guide

## vLLM LoRA Hot Swapping / Dynamic LoRAs

Enable LoRA serving for up to 4 LoRAs concurrently (hot-swapped at runtime).

### 1. Set the environment flag

```bash
export VLLM_ALLOW_RUNTIME_LORA_UPDATING=True
```

### 2. Serve with LoRA support

```bash
export VLLM_ALLOW_RUNTIME_LORA_UPDATING=True
vllm serve unsloth/Llama-3.1-8B-Instruct \
    --quantization fp8 \
    --kv-cache-dtype fp8
    --gpu-memory-utilization 0.8 \
    --max-model-len 65536 \
    --enable-lora \
    --max-loras 4 \
    --max-lora-rank 64
```

### 3. Load a LoRA dynamically

```bash
curl -X POST http://localhost:8000/v1/load_lora_adapter \
    -H "Content-Type: application/json" \
    -d '{
        "lora_name": "LORA_NAME",
        "lora_path": "/path/to/LORA"
    }'
```

### 4. Unload a LoRA from the pool

```bash
curl -X POST http://localhost:8000/v1/unload_lora_adapter \
    -H "Content-Type: application/json" \
    -d '{
        "lora_name": "LORA_NAME"
    }'
```

## Example: Finetune with Unsloth then hot-swap

```python
from unsloth import FastLanguageModel
import torch
model, tokenizer = FastLanguageModel.from_pretrained(
    model_name = "unsloth/Llama-3.1-8B-Instruct",
    max_seq_length = 2048,
    load_in_4bit = True,
)
model = FastLanguageModel.get_peft_model(model)
```

After training, save the LoRA:

```python
model.save_pretrained("finetuned_lora")
tokenizer.save_pretrained("finetuned_lora")
```

Load it into the running vLLM server:

```bash
curl -X POST http://localhost:8000/v1/load_lora_adapter \
    -H "Content-Type: application/json" \
    -d '{
        "lora_name": "LORA_NAME_finetuned_lora",
        "lora_path": "finetuned_lora"
    }'
```

#lora #vllm #hot-swapping #inference
