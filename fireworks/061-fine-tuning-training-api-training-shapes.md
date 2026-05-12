---
title: Training Shapes - Fireworks AI Docs
url: https://docs.fireworks.ai/fine-tuning/training-api/training-shapes
source: sitemap
fetched_at: 2026-04-27T20:12:39.709758583-03:00
rendered_js: false
word_count: 543
summary: This document explains the concept of a training shape in the context of fireworks jobs, detailing how users select and utilize these shapes to configure GPU layout, model limits, trainer runtime, and linked deployment setup.
tags:
    - training-shape
    - fireworks-jobs
    - trainer-config
    - api-usage
    - model-deployment
    - gpus
    - qwen-3.5
category: guide
optimized: true
optimized_at: 2026-04-27T20:12:39.709758583-03:00
---
A training shape is the user-facing launch input for trainer jobs. Most users only need to choose a training shape ID such as `accounts/fireworks/trainingShapes/qwen3p5-9b-256k` and pass it to the API.

Shapes published under `accounts/fireworks/trainingShapes/<shape>` can be referenced by all users. You do not need to know the versioned shape reference, image tag, GPU layout, or linked deployment shape ahead of time — the API resolves those details internally.

## Workflow

For most users:

1. Pick a training shape ID (e.g. `accounts/fireworks/trainingShapes/qwen3p5-9b-256k`).
2. Call `resolve_training_profile(shape_id)`.
3. Pass `profile.training_shape_version` into `TrainerJobConfig.training_shape_ref`.

That is the only shape-specific value you choose yourself.

## What a training shape controls

| Field | Description |
|---|---|
| `acceleratorType`, `acceleratorCount`, `nodeCount` | GPU and node layout |
| `maxSupportedContextLength` | Model limits |
| `trainerImageTag` | Trainer runtime |
| `deploymentShapeVersion` | Linked serving setup |

## What you can still configure

- `base_model`, `lora_rank`, `learning_rate`, `gradient_accumulation_steps`, `display_name`
- `hot_load_trainer_job` (on `DeploymentConfig`)
- Deployment replica counts (`min_replica_count` / `max_replica_count`)

For field-level behavior and dataclass details, see [[056-fine-tuning-training-api-reference-deployment-manager|TrainerJobManager]] and [[056-fine-tuning-training-api-reference-deployment-manager|DeploymentManager]].

## Using a training shape

```python
from fireworks.training.sdk import TrainerJobManager, TrainerJobConfig

mgr = TrainerJobManager(api_key=api_key)
shape_id = "accounts/fireworks/trainingShapes/qwen3p5-9b-256k"

# This is the only shape-specific value you choose
profile = mgr.resolve_training_profile(shape_id)
# profile.training_shape_version → "accounts/fireworks/trainingShapes/qwen3p5-9b-256k/versions/s0q58a4p"

# Pass the resolved version to the trainer config
config = TrainerJobConfig(
    base_model="accounts/fireworks/models/qwen3p5-9b",
    training_shape_ref=profile.training_shape_version,
)
endpoint = mgr.create_and_wait(config)
```

## Available training shapes

During Reinforcement Fine-Tuning (RFT), two types of models are often deployed: a **policy trainer** (which updates its weights) and a **reference model** (forward-only, no optimizer states or backward passes).

### Qwen 3.5 (Dense)

#### Qwen 3.5 9B — `accounts/fireworks/models/qwen3p5-9b`

| Role | Shape | GPUs |
|---|---|---|
| Policy trainer | 256k | 2 |
| LoRA trainer | 256k | 2 |
| Forward-only / reference | 256k | 2 |

#### Qwen 3.5 27B — `accounts/fireworks/models/qwen3p5-27b`

| Role | Shape | GPUs |
|---|---|---|
| Policy trainer | 256k | 4 |
| LoRA trainer | 256k | 4 |
| Forward-only / reference | 256k | 2 |

### Qwen 3.5 (Mixture-of-Experts)

#### Qwen 3.5 35B A3B — `accounts/fireworks/models/qwen3p5-35b-a3b`

| Role | Shape | GPUs |
|---|---|---|
| Policy trainer | 256k | 8 |
| LoRA trainer | 256k | 8 |
| Forward-only / reference | 256k | 4 |

#### Qwen 3.5 397B A17B — `accounts/fireworks/models/qwen3p5-397b-a17b`

| Role | Shape | GPUs |
|---|---|---|
| Policy trainer | 256k | 4 nodes |
| LoRA trainer | 256k | 8 |
| Forward-only / reference | 256k | 8 |

### Gemma 4 (Dense)

#### Gemma 4 31B — `accounts/fireworks/models/gemma-4-31b-it`

| Role | Shape | GPUs |
|---|---|---|
| Policy trainer | 256k | 4 |
| LoRA trainer | 256k | 4 |
| Forward-only / reference | 256k | 4 |

### Gemma 4 (Mixture-of-Experts)

#### Gemma 4 26B A4B — `accounts/fireworks/models/gemma-4-26b-a4b-it`

| Role | Shape | GPUs |
|---|---|---|
| Policy trainer | 256k | 4 |
| LoRA trainer | 256k | 4 |
| Forward-only / reference | 256k | 4 |

### Llama 3

#### Llama 70B — `accounts/fireworks/models/llama-v3p3-70b-instruct`

| Role | Shape | GPUs |
|---|---|---|
| Policy trainer | 128k | 8 |
| Forward-only / reference | 128k | 4 |

### Kimi

#### Kimi 2.5 Text-Only — `accounts/fireworks/models/kimi-k2p5`

| Role | Shape | GPUs |
|---|---|---|
| Policy trainer | 256k | 64 |
| Forward-only / reference | 256k | 16 |
| LoRA trainer | 256k | 8 |

#training-shape #trainer-config #api-usage #model-deployment #gpus
