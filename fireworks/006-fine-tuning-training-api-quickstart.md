---
title: Quickstart - Fireworks AI Docs
url: https://docs.fireworks.ai/fine-tuning/training-api/quickstart
source: sitemap
fetched_at: 2026-04-27T20:15:25.088707116-03:00
rendered_js: false
word_count: 154
summary: This document provides a comprehensive quickstart guide on how to perform a minimal Supervised Fine-Tuning (SFT) training loop using the Fireworks AI Python SDK. It details installation, provisioning the trainer job, building data samples, defining a custom loss function for training, and finally saving and promoting the resulting weights into a deployable model.
tags:
    - sft-training
    - fireworks-ai
    - python-sdk
    - model-tuning
    - api-quickstart
    - checkpointing
category: tutorial
optimized: true
optimized_at: 2026-04-27T00:00:00Z
---
## Installation

Install the Fireworks Python package with training extensions:

```bash
pip install --pre "fireworks-ai[training]"
```

Set your credentials:

```bash
export FIREWORKS_API_KEY="your-api-key"
```

## Your first training loop

This quickstart walks through a minimal SFT loop from scratch using only the API. The only shape-specific input you provide is the training shape ID.

### Step 1: Provision a trainer

```python
import os
from fireworks.training.sdk import (
    FiretitanServiceClient,
    TrainerJobManager,
    TrainerJobConfig,
)

api_key = os.environ["FIREWORKS_API_KEY"]
base_url = os.environ.get("FIREWORKS_BASE_URL", "https://api.fireworks.ai")

base_model = "accounts/fireworks/models/qwen3-8b"
shape_id = "accounts/fireworks/trainingShapes/qwen3-8b-128k-h200"

rlor_mgr = TrainerJobManager(api_key=api_key, base_url=base_url)

# This is the only shape-specific value you choose
profile = rlor_mgr.resolve_training_profile(shape_id)

endpoint = rlor_mgr.create_and_wait(TrainerJobConfig(
    base_model=base_model,
    training_shape_ref=profile.training_shape_version,
    lora_rank=0,
    learning_rate=1e-5,
    gradient_accumulation_steps=1,
    display_name="sft-quickstart",
))
print(f"Trainer ready at: {endpoint.base_url}")
```

### Step 2: Connect the training client

```python
service = FiretitanServiceClient(
    base_url=endpoint.base_url,
    api_key=api_key,
)
training_client = service.create_training_client(
    base_model=base_model,
    lora_rank=0,
)
```

### Step 3: Build training data

Each training example is a **Datum** — a tokenized sequence with per-token weights indicating which tokens to train on.

```python
import tinker
import torch
import transformers
from tinker_cookbook.supervised.common import datum_from_model_input_weights

tokenizer = transformers.AutoTokenizer.from_pretrained(
    "Qwen/Qwen3-8B", trust_remote_code=True,
)

conversation = [
    {"role": "user", "content": "What is the capital of France?"},
    {"role": "assistant", "content": "The capital of France is Paris."},
]

full_text = tokenizer.apply_chat_template(conversation, tokenize=False)
full_tokens = tokenizer.encode(full_text)

prompt_only = tokenizer.apply_chat_template(conversation[:1], tokenize=False)
prompt_len = len(tokenizer.encode(prompt_only))

weights = torch.zeros(len(full_tokens), dtype=torch.float32)
weights[prompt_len:] = 1.0

datum = datum_from_model_input_weights(
    tinker.ModelInput.from_ints(full_tokens),
    weights,
    max_length=4096,
)
```

### Step 4: Write a loss function and train

```python
import tinker

def sft_loss(data, logprobs_list):
    total_loss = torch.tensor(0.0)
    n_tokens = 0
    for i, logprobs in enumerate(logprobs_list):
        weights = torch.tensor(
            data[i].loss_fn_inputs["weights"].data, dtype=torch.float32,
        )
        min_len = min(len(logprobs), len(weights))
        total_loss = total_loss - torch.dot(
            logprobs[:min_len].float(), weights[:min_len],
        )
        n_tokens += weights[:min_len].sum().item()
    loss = total_loss / max(n_tokens, 1)
    return loss, {"sft_loss": loss.item(), "n_tokens": n_tokens}

batch = [datum]
for step in range(10):
    result = training_client.forward_backward_custom(batch, sft_loss).result()
    training_client.optim_step(
        tinker.AdamParams(learning_rate=1e-5, beta1=0.9, beta2=0.999, eps=1e-8, weight_decay=0.01)
    ).result()
    print(f"Step {step}: {result.metrics}")
```

### Step 5: Save and promote

```python
result = training_client.save_weights_for_sampler_ext(
    "sft-final",
    checkpoint_type="base",
)
print(f"Checkpoint saved: {result.snapshot_name}")

# Promote the checkpoint to a deployable Fireworks model
model = rlor_mgr.promote_checkpoint(
    job_id=endpoint.job_id,
    checkpoint_id=result.snapshot_name,
    output_model_id="my-sft-model",
    base_model=base_model,
)

rlor_mgr.delete(endpoint.job_id)
```

## Next steps

- [[060-fine-tuning-training-api-training-and-sampling|Training and Sampling]] — full end-to-end lifecycle with deployment evaluation
- [[054-fine-tuning-training-api-loss-functions|Loss Functions]] — GRPO, DPO, and custom loss function patterns
- [[062-fine-tuning-training-api-vision-inputs|Vision Inputs]] — fine-tune vision-language models with image and text data
- [[059-fine-tuning-training-api-saving-and-loading|Saving and Loading]] — checkpointing and weight sync details
- [[014-fine-tuning-training-api-cookbook-overview|The Cookbook]] — ready-to-run recipes for GRPO, DPO, and SFT
