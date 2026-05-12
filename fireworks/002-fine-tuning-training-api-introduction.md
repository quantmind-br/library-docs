---
title: Introduction - Fireworks AI Docs
url: https://docs.fireworks.ai/fine-tuning/training-api/introduction
source: sitemap
fetched_at: 2026-04-27T20:15:26.782475959-03:00
rendered_js: false
word_count: 756
summary: This document introduces the Fireworks Training API, which allows users to run custom training loops in Python on remote GPUs without managing infrastructure. It details the core components, architecture, and specific APIs for implementing features like custom loss functions, checkpointing, and service-mode operation.
tags:
    - training-api
    - custom-loop
    - mlops
    - gpu-training
    - fireworks-ai
    - python-implementation
category: guide
optimized: true
optimized_at: 2026-04-27T00:00:00Z
---
## What is the Training API?

Fireworks Training API lets you write custom training loops in plain Python on your local machine while the actual model computation runs on remote GPUs managed by Fireworks. You get full control over your loss function and training logic without managing GPU clusters.

| Mode | Best for | Objective control | Infrastructure |
|------|----------|--------------------|-----------------|
| **Cookbook recipes** | GRPO/DPO/SFT/ORPO with config-driven customization | Fork and modify | You configure, platform runs GPUs |
| **API loops** | Custom losses, algorithm research | Full Python control | You drive the loop, platform runs GPUs |

## Why this approach

- **Custom losses in Python** eliminate waiting for vendor-specific algorithm implementations — implement GRPO, DPO, or any hybrid objective directly.
- **Full-parameter updates** maximize headroom for difficult reasoning and alignment tasks where LoRA may underfit.
- **Vision-language model support** — fine-tune VLMs with multimodal datasets containing images and text using the same API primitives.
- **Serving-integrated evaluation** via checkpoint weight sync avoids divergence between offline metrics and user-facing behavior.
- **No local GPUs needed** — a laptop is enough to drive training of models up to 1TB parameters like kimi k2.5.

### Who this is for

- **Research teams** doing alignment, RLHF, and reasoning improvement with custom reward functions.
- **ML engineers** who want to iterate on training algorithms without managing GPU clusters.
- **Teams transitioning** from managed fine-tuning to custom training loops as their requirements grow.

## Who does what

| Fireworks handles | You implement |
|------------------|---------------|
| GPU provisioning and cluster management | Training loop logic (`forward_backward_custom` + `optim_step`) |
| Service-mode trainer lifecycle (create, health-check, reconnect, delete) | Loss function and batch construction (`tinker.Datum` objects, custom objectives) |
| Checkpoint storage and export (`save_weights_for_sampler_ext`, DCP snapshots) | Reward signals and evaluation logic (sample from deployment, score responses) |
| Inference deployment and weight sync (checkpoint to live serving) | Hyperparameter tuning (learning rate, grad accum, context length) |
| Preemption recovery and job resume (transparent reconnect) | Data pipeline and dataset preparation |
| | Distributed training (multi-node, sharding, FSDP) |
| | Experiment tracking and logging (W&B, custom metrics) |

With [[014-fine-tuning-training-api-cookbook-overview|The Cookbook]], the "You implement" column is largely handled for you — the cookbook provides ready-to-run training loops, loss functions, reward scoring, and checkpointing out of the box. You bring your data and config.

## System architecture

A control-plane API provisions trainer and deployment resources. Your local Python loop connects to the trainer service, runs custom train steps, and periodically exports checkpoints to a serving deployment for sampling and evaluation.

## How service-mode training works

### Datums

A **Datum** is the unit of training data sent to the remote GPU. It wraps tokenized input and per-token weights that your loss function needs. Token weights tell the loss function which tokens to train on:

- **`0.0`** = prompt token (don't train on this)
- **`1.0`** = response token (train on this)

```python
import tinker
import torch
from tinker_cookbook.supervised.common import datum_from_model_input_weights

tokens = tokenizer.encode("What is 2+2? The answer is 4.")
prompt_len = len(tokenizer.encode("What is 2+2? "))

weights = torch.zeros(len(tokens), dtype=torch.float32)
weights[prompt_len:] = 1.0  # Train on response tokens only

datum = datum_from_model_input_weights(
    tinker.ModelInput.from_ints(tokens),
    weights,
    max_length=4096,
)
```

### Logprobs and forward_backward_custom

When you call `forward_backward_custom`, the GPU runs a forward pass and returns **per-token log-probabilities** as PyTorch tensors with `requires_grad=True`. Your loss function computes a scalar loss, the API calls `loss.backward()`, and gradients are sent back to the GPU for the model backward pass.

```python
def my_loss_fn(data, logprobs_list):
    loss = compute_something(logprobs_list)
    return loss, {"loss": loss.item()}

result = training_client.forward_backward_custom(datums, my_loss_fn).result()
```

After accumulating gradients, call `optim_step` to apply the optimizer update:

```python
import tinker

training_client.optim_step(
    tinker.AdamParams(learning_rate=1e-5, beta1=0.9, beta2=0.999, eps=1e-8, weight_decay=0.01)
).result()
```

### Futures

All training client API calls return **futures**. Call `.result()` to block until completion. Without `.result()`, errors are silently swallowed.

### Checkpointing and weight sync

After training, you export checkpoints for serving:

- **Base checkpoint**: Full model weights. Use for the first checkpoint.
- **Delta checkpoint**: Only the diff from the previous base (~10x smaller). Use for subsequent checkpoints.

**Weight sync** pushes a checkpoint onto a running inference deployment without restarting it, enabling evaluation under serving conditions during training.

## Key APIs

| API | Purpose |
|-----|---------|
| `TrainerJobManager` | Create, resume, reconnect, and delete service-mode trainer jobs |
| `FiretitanServiceClient` | Connect to a trainer endpoint and create training clients |
| `FiretitanTrainingClient` | `forward_backward_custom`, `optim_step`, checkpointing methods |
| `DeploymentManager` | Create deployments, weight sync, and warmup |
| `DeploymentSampler` | Client-side tokenized sampling from deployments |
| `WeightSyncer` | Manages checkpoint + weight sync lifecycle with delta chaining |

## Next steps

- [[006-fine-tuning-training-api-quickstart|Quickstart]] — get a custom training loop running in minutes
- [[060-fine-tuning-training-api-training-and-sampling|Training and Sampling]] — end-to-end API walkthrough
- [[054-fine-tuning-training-api-loss-functions|Loss Functions]] — built-in and custom loss functions
- [[062-fine-tuning-training-api-vision-inputs|Vision Inputs]] — fine-tune vision-language models with image and text data
- [[014-fine-tuning-training-api-cookbook-overview|The Cookbook]] — ready-to-run recipes for GRPO, DPO, and SFT
