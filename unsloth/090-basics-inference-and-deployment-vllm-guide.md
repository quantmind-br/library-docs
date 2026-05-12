---
title: vLLM Deployment & Inference Guide
url: https://unsloth.ai/docs/basics/inference-and-deployment/vllm-guide.md
source: llms
fetched_at: 2026-04-27T18:14:44.480329782-03:00
rendered_js: false
word_count: 336
summary: This guide details how to install vLLM for various GPU types (NVIDIA and AMD), describes methods for deploying saved models, and provides detailed instructions on running the deployment server with specific arguments, especially when working with Unsloth fine-tuned models.
tags:
    - vllm
    - deployment
    - installation
    - inference
    - unsloth
    - model-serving
category: guide
optimized: true
optimized_at: 2026-04-27T21:30:00Z
---

# vLLM Deployment & Inference Guide

## Installing vLLM

**NVIDIA GPUs:**

```bash
pip install --upgrade pip
pip install uv
uv pip install -U vllm --torch-backend=auto
```

**AMD GPUs:** use nightly Docker image: `rocm/vllm-dev:nightly`

**NVIDIA nightly:**

```bash
pip install --upgrade pip
pip install uv
uv pip install -U vllm --torch-backend=auto --extra-index-url https://wheels.vllm.ai/nightly
```

See [vLLM docs](https://docs.vllm.ai/en/stable/getting_started/installation) for more details.

## Deploying vLLM Models

```bash
vllm serve unsloth/gpt-oss-120b
```

## vLLM Server Flags & Engine Arguments

See [[089-basics-inference-and-deployment-vllm-guide-lora-hot-swapping-guide|LoRA Hot Swapping Guide]] and [[117-basics-inference-and-deployment-vllm-guide-vllm-engine-arguments|vLLM Engine Arguments]] for detailed options.

## Deploying Unsloth Finetunes in vLLM

After [[064-get-started-fine-tuning-llms-guide|fine-tuning]] or using [[073-get-started-unsloth-notebooks|Unsloth Notebooks]], save/deploy directly through vLLM.

```python
from unsloth import FastLanguageModel
import torch
model, tokenizer = FastLanguageModel.from_pretrained(
    model_name = "unsloth/gpt-oss-20b",
    max_seq_length = 2048,
    load_in_4bit = True,
)
model = FastLanguageModel.get_peft_model(model)
```

### Save Methods

**16-bit (recommended for vLLM):**

```python
model.save_pretrained_merged("finetuned_model", tokenizer, save_method = "merged_16bit")
## OR to upload to HuggingFace:
model.push_to_hub_merged("hf/model", tokenizer, save_method = "merged_16bit", token = "")
```

**LoRA adapters only:**

```python
model.save_pretrained("finetuned_lora")
tokenizer.save_pretrained("finetuned_lora")
## OR built-in:
model.save_pretrained_merged("finetuned_model", tokenizer, save_method = "lora")
## OR to upload to HuggingFace
model.push_to_hub_merged("hf/model", tokenizer, save_method = "lora", token = "")
```

**4-bit merge** (for DPO training or HF online inference): use `merged_4bit`. Use `merged_4bit_forced` only if certain.

```python
model.save_pretrained_merged("finetuned_model", tokenizer, save_method = "merged_4bit")
## To upload to HuggingFace:
model.push_to_hub_merged("hf/model", tokenizer, save_method = "merged_4bit", token = "")
```

### Serve the Finetuned Model

```bash
vllm serve finetuned_model
```

If path resolution fails, use the full path:

```bash
vllm serve /mnt/disks/daniel/finetuned_model
```

## Agent Query Endpoint

```
GET https://unsloth.ai/docs/basics/inference-and-deployment/vllm-guide.md?ask=<question>
```

#vllm #deployment #inference
