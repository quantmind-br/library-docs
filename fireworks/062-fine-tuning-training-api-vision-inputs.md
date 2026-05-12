---
title: Vision Inputs - Fireworks AI Docs
url: https://docs.fireworks.ai/fine-tuning/training-api/vision-inputs
source: sitemap
fetched_at: 2026-04-27T20:15:20.987015269-03:00
rendered_js: false
word_count: 437
summary: This document explains how to fine-tune Vision-Language Models (VLMs) using the Training API, detailing the changes required for vision inputs compared to text-only training.
tags:
    - vlm-fine-tuning
    - vision-language-models
    - training-api
    - sft-dpo-rl
    - multimodal-data
category: guide
optimized: true
optimized_at: 2026-04-27T20:15:20.987015269-03:00
---
The Training API supports vision-language model (VLM) fine-tuning across all training modes — SFT, DPO, and RL — using the same API primitives and cookbook recipes as text-only training.

## What changes for vision

| Aspect | Text-only | Vision |
|---|---|---|
| Training shape | Text model shape (e.g. `qwen3-8b-128k`) | VLM shape (e.g. `qwen3-vl-8b-65k`) |
| Tokenizer | Text tokenizer (e.g. `Qwen/Qwen3-8B`) | VLM processor (e.g. `Qwen/Qwen3-VL-8B-Instruct`) |
| Message format | `content` is a string | `content` is an array of text and `image_url` objects |

Everything else — loss functions, checkpointing, weight sync, deployment sampling — works identically.

## Dataset format

Vision datasets use the standard OpenAI-compatible chat format. The key difference is that `content` fields can contain an array of content parts mixing text and images.

### Single image

```json
{
  "messages": [
    {
      "role": "user",
      "content": [
        {"type": "text", "text": "What objects do you see in this image?"},
        {"type": "image_url", "image_url": {"url": "data:image/jpeg;base64,/9j/4AAQSkZJRgABAQ..."}}
      ]
    },
    {"role": "assistant", "content": "I can see a red car, a tree, and a blue house."}
  ]
}
```

### Multiple images

```json
{
  "messages": [
    {
      "role": "user",
      "content": [
        {"type": "text", "text": "Compare these two images"},
        {"type": "image_url", "image_url": {"url": "data:image/jpeg;base64,/9j/4AAQSkZJRg..."}},
        {"type": "image_url", "image_url": {"url": "data:image/jpeg;base64,/9j/4BBBSkZJRg..."}}
      ]
    },
    {"role": "assistant", "content": "The first image shows a daytime scene while the second shows the same location at night."}
  ]
}
```

### Multi-turn with images

```json
{
  "messages": [
    {
      "role": "user",
      "content": [
        {"type": "text", "text": "Describe this kitchen."},
        {"type": "image_url", "image_url": {"url": "data:image/jpeg;base64,/9j/4AAQ..."}}
      ]
    },
    {"role": "assistant", "content": "This is a modern open-plan kitchen with white cabinets and granite countertops."},
    {
      "role": "user",
      "content": [
        {"type": "text", "text": "Now compare it with this living room."},
        {"type": "image_url", "image_url": {"url": "data:image/jpeg;base64,/9j/4BBB..."}}
      ]
    },
    {"role": "assistant", "content": "Both spaces share a modern aesthetic with clean lines and neutral colors."}
  ]
}
```

### Image encoding requirements

Images must be base64-encoded with a MIME type prefix. Raw HTTP URLs are **not** supported in training data.

> [!warning]
> Supported image formats: **PNG**, **JPEG/JPG**. If your dataset contains image URLs, download and convert them to base64 first. See [[041-fine-tuning-fine-tuning-vlm|Fine Tuning VLM]] for the conversion script.

## Cookbook: VLM SFT

The cookbook's `sft_loop` recipe works with vision datasets out of the box. Use a VLM training shape and a VLM tokenizer:

```python
from training.recipes.sft_loop import Config, main
from training.utils import InfraConfig

cfg = Config(
    log_path="./vlm_sft_logs",
    base_model="accounts/fireworks/models/qwen3-vl-8b-instruct",
    dataset="/path/to/vision_data.jsonl",
    tokenizer_model="Qwen/Qwen3-VL-8B-Instruct",
    max_seq_len=4096,
    epochs=1,
    batch_size=4,
    learning_rate=1e-5,
    infra=InfraConfig(
        training_shape_id="accounts/fireworks/trainingShapes/qwen3-vl-8b-65k",
    ),
)

main(cfg)
```

The recipe handles vision-aware tokenization automatically — image tokens are assigned weight `0.0` (prompt) and text response tokens are assigned weight `1.0` (train).

## API-level: VLM training loop

For full control over the training loop, use the API directly with a VLM training shape. The workflow is the same as text-only training, but the tokenizer and shape are VLM-specific.

### 1. Provision a VLM trainer

```python
import os
from fireworks.training.sdk import (
    FiretitanServiceClient,
    TrainerJobManager,
    TrainerJobConfig,
)

api_key = os.environ["FIREWORKS_API_KEY"]
base_url = os.environ.get("FIREWORKS_BASE_URL", "https://api.fireworks.ai")

base_model = "accounts/fireworks/models/qwen3-vl-8b-instruct"
shape_id = "accounts/fireworks/trainingShapes/qwen3-vl-8b-65k"

rlor_mgr = TrainerJobManager(api_key=api_key, base_url=base_url)
profile = rlor_mgr.resolve_training_profile(shape_id)

endpoint = rlor_mgr.create_and_wait(TrainerJobConfig(
    base_model=base_model,
    training_shape_ref=profile.training_shape_version,
    lora_rank=0,
    learning_rate=1e-5,
    gradient_accumulation_steps=4,
    display_name="vlm-sft",
))
```

### 2. Connect and train

```python
import torch
import tinker
import transformers
from tinker_cookbook.supervised.common import datum_from_model_input_weights

service = FiretitanServiceClient(base_url=endpoint.base_url, api_key=api_key)
training_client = service.create_training_client(
    base_model=base_model, lora_rank=0,
)

processor = transformers.AutoProcessor.from_pretrained(
    "Qwen/Qwen3-VL-8B-Instruct", trust_remote_code=True,
)

conversation = [
    {
        "role": "user",
        "content": [
            {"type": "text", "text": "What is in this image?"},
            {"type": "image_url", "image_url": {"url": "data:image/jpeg;base64,/9j/..."}},
        ],
    },
    {"role": "assistant", "content": "The image shows a sunset over the ocean."},
]

text = processor.apply_chat_template(conversation, tokenize=False)
full_tokens = processor.tokenizer.encode(text)

prompt_text = processor.apply_chat_template(conversation[:1], tokenize=False)
prompt_len = len(processor.tokenizer.encode(prompt_text))

weights = torch.zeros(len(full_tokens), dtype=torch.float32)
weights[prompt_len:] = 1.0

datum = datum_from_model_input_weights(
    tinker.ModelInput.from_ints(full_tokens),
    weights,
    max_length=4096,
)

def sft_loss(data, logprobs_list):
    total_loss = torch.tensor(0.0)
    n_tokens = 0
    for i, logprobs in enumerate(logprobs_list):
        w = torch.tensor(data[i].loss_fn_inputs["weights"].data, dtype=torch.float32)
        min_len = min(len(logprobs), len(w))
        total_loss = total_loss - torch.dot(logprobs[:min_len].float(), w[:min_len])
        n_tokens += w[:min_len].sum().item()
    return total_loss / max(n_tokens, 1), {"sft_loss": (total_loss / max(n_tokens, 1)).item()}

for step in range(100):
    training_client.forward_backward_custom([datum], sft_loss).result()
    training_client.optim_step(
        tinker.AdamParams(learning_rate=1e-5, beta1=0.9, beta2=0.999, eps=1e-8, weight_decay=0.01)
    ).result()
```

### 3. Save and promote

Checkpointing and weight sync work identically to text-only training:

```python
result = training_client.save_weights_for_sampler_ext("vlm-final", checkpoint_type="base")

model = rlor_mgr.promote_checkpoint(
    job_id=endpoint.job_id,
    checkpoint_id=result.snapshot_name,
    output_model_id="my-vlm-model",
    base_model="accounts/fireworks/models/qwen3-vl-8b-instruct",
)
```

## VLM DPO and RL

Vision inputs also work with DPO and RL training. The dataset format is the same — use multimodal `content` arrays in your messages.

### DPO with vision

```json
{
  "chosen": {
    "messages": [
      {
        "role": "user",
        "content": [
          {"type": "text", "text": "Describe this chart."},
          {"type": "image_url", "image_url": {"url": "data:image/png;base64,iVBOR..."}}
        ]
      },
      {"role": "assistant", "content": "This bar chart shows quarterly revenue growth of 15% year-over-year."}
    ]
  },
  "rejected": {
    "messages": [
      {
        "role": "user",
        "content": [
          {"type": "text", "text": "Describe this chart."},
          {"type": "image_url", "image_url": {"url": "data:image/png;base64,iVBOR..."}}
        ]
      },
      {"role": "assistant", "content": "This is a chart."}
    ]
  }
}
```

### RL with vision prompts

```json
{
  "messages": [
    {
      "role": "user",
      "content": [
        {"type": "text", "text": "Solve the math problem shown in this image. Show your reasoning."},
        {"type": "image_url", "image_url": {"url": "data:image/png;base64,iVBOR..."}}
      ]
    }
  ]
}
```

Use the corresponding cookbook recipes (`dpo_loop`, `rl_loop`) with a VLM training shape and tokenizer — the multimodal message handling is automatic.

## Available VLM training shapes

| Model | Shape ID | Context | GPUs |
|---|---|---|---|
| Qwen3 VL 8B | `accounts/fireworks/trainingShapes/qwen3-vl-8b-65k` | 65k | 4 |

- [[061-fine-tuning-training-api-training-shapes|Training Shapes]] — available VLM and text training shapes
- [[041-fine-tuning-fine-tuning-vlm|Fine Tuning VLM]] — managed VLM fine-tuning without writing training loops
- [[076-guides-querying-vision-language-models|Querying Vision Language Models]] — inference with VLMs
- [[052-fine-tuning-training-api-cookbook-sft|Cookbook SFT]] — SFT recipe details
- [[054-fine-tuning-training-api-loss-functions|Loss Functions]] — custom loss function patterns

#vlm-fine-tuning #vision-language-models #training-api #sft-dpo-rl #multimodal-data
