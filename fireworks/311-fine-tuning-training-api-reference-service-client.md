---
title: FiretitanServiceClient & TrainingClient - Fireworks AI Docs
url: https://docs.fireworks.ai/fine-tuning/training-api/reference/service-client
source: sitemap
fetched_at: 2026-04-27T20:15:28.856844723-03:00
rendered_js: false
word_count: 472
summary: This document details the `FiretitanServiceClient` and the resulting `FiretitanTrainingClient`, providing an overview of how to connect to a trainer endpoint and utilize various methods for training operations like running forward passes, custom backward steps, applying optimizer updates, and managing checkpoints.
tags:
    - firetitan-client
    - training-sdk
    - checkpointing
    - optimizer-step
    - forward-pass
    - training-api
category: reference
optimized: true
optimized_at: 2026-04-27T20:20:00Z
---
## Overview

`FiretitanServiceClient` connects to a trainer endpoint and creates a `FiretitanTrainingClient` for training operations. It extends Tinker's `ServiceClient` with Fireworks-specific features like `checkpoint_type` support and session-scoped snapshot naming.

```python
from fireworks.training.sdk import FiretitanServiceClient
```

### Constructor

```python
service = FiretitanServiceClient(
    base_url=endpoint.base_url,  # From TrainerJobManager.create_and_wait(...)
    api_key="<FIREWORKS_API_KEY>",
)
```

`base_url` is the trainer endpoint URL from `TrainerServiceEndpoint.base_url`.

### `create_training_client(base_model, lora_rank, user_metadata)`

Creates a `FiretitanTrainingClient` for training operations:

```python
training_client = service.create_training_client(
    base_model="accounts/fireworks/models/qwen3-8b",
    lora_rank=0,  # Must match lora_rank from job creation
)
```

| Param | Type | Default | Description |
|---|---|---|---|
| `base_model` | `str` | — | Must match the trainer job's `base_model` |
| `lora_rank` | `int` | `0` | Must match trainer creation config (`0` for full-parameter) |
| `user_metadata` | `dict[str, str] \| None` | `None` | Optional run metadata |

### Connecting to an existing trainer

Connect directly by URL if you already have a running trainer:

```python
service = FiretitanServiceClient(
    base_url="https://<existing-trainer-url>",
    api_key="<FIREWORKS_API_KEY>",
)
training_client = service.create_training_client(
    base_model="accounts/fireworks/models/qwen3-8b",
    lora_rank=0,
)
```

## FiretitanTrainingClient

The training client returned by `create_training_client()`. Core training RPCs (`forward(...)`, `forward_backward_custom(...)`, `optim_step(...)`, `save_state(...)`, `load_state_with_optimizer(...)`) return **futures**. Fireworks convenience helpers (`save_weights_for_sampler_ext(...)`, `list_checkpoints()`, `resolve_checkpoint_path(...)`) return concrete values directly.

### `forward(datums, loss_type)`

Forward-only pass (no gradient computation). Useful for computing reference logprobs in GRPO/DPO:

```python
result = training_client.forward(datums, "cross_entropy").result()
logprobs = result.loss_fn_outputs[0]["logprobs"].data
```

### `forward_backward_custom(datums, loss_fn)`

Forward + backward with your custom loss function. See [[054-fine-tuning-training-api-loss-functions|Loss Functions]] for details:

```python
def my_loss(data, logprobs_list):
    loss = compute_loss(data, logprobs_list)
    return loss, {"loss": float(loss.item())}

result = training_client.forward_backward_custom(datums, my_loss).result()
print(result.metrics)  # {"loss": 0.42}
```

### `optim_step(params)`

Apply optimizer update after accumulating gradients:

```python
import tinker

training_client.optim_step(
    tinker.AdamParams(
        learning_rate=1e-5,
        beta1=0.9,
        beta2=0.999,
        eps=1e-8,
        weight_decay=0.01,
    )
).result()
```

Supports `grad_accumulation_normalization` parameter for controlling how accumulated gradients are normalized. See [[054-fine-tuning-training-api-loss-functions|Loss Functions → Gradient Accumulation Normalization]] for the normalization modes and when to use them.

### `save_weights_for_sampler_ext(name, checkpoint_type, ttl_seconds)`

Export serving-compatible checkpoint with session-scoped naming. Returns a `SaveSamplerResult`:

```python
result = training_client.save_weights_for_sampler_ext(
    "step-100",
    checkpoint_type="base",  # "base" for full weights, "delta" for incremental
)
print(result.snapshot_name)  # Session-qualified name for hotloading
```

| Param | Type | Default | Description |
|---|---|---|---|
| `name` | `str` | — | Checkpoint name (auto-suffixed with session ID) |
| `checkpoint_type` | `str \| None` | `None` | `"base"` for full weights, `"delta"` for incremental |
| `ttl_seconds` | `int \| None` | `None` | Auto-delete checkpoint after this many seconds |

### `save_state(name, ttl_seconds=None)`

Save full train state (weights + optimizer) for resume:

```python
training_client.save_state("train_state_step_100").result()
```

| Param | Type | Default | Description |
|---|---|---|---|
| `name` | `str` | — | Checkpoint name |
| `ttl_seconds` | `int \| None` | `None` | Auto-delete checkpoint after this many seconds |

### `load_state_with_optimizer(name)`

Restore full train state (weights + optimizer) from a checkpoint:

```python
training_client.load_state_with_optimizer("train_state_step_100").result()
```

### `load_state(name)`

Load model weights from a checkpoint without restoring optimizer state. The optimizer is reset so the next `optim_step` starts fresh:

```python
training_client.load_state("train_state_step_100").result()
```

### `list_checkpoints()`

List available DCP checkpoints from the trainer. Returns a `list[str]`:

```python
checkpoint_names = training_client.list_checkpoints()
print(checkpoint_names)  # e.g. ["step-2", "step-4"]
```

### `resolve_checkpoint_path(name, source_job_id)`

Resolve a checkpoint path for cross-job resume:

```python
checkpoint_ref = training_client.resolve_checkpoint_path(
    "step-4",
    source_job_id="previous-job-id",
)
training_client.load_state_with_optimizer(checkpoint_ref).result()
```

## SaveSamplerResult

Returned by `save_weights_for_sampler_ext`:

| Field | Type | Description |
|---|---|---|
| `path` | `str` | Snapshot name from trainer |
| `snapshot_name` | `str` | Session-qualified name for weight sync operations |

## GradAccNormalization

Enum for `optim_step`'s `grad_accumulation_normalization` parameter:

| Value | Description |
|---|---|
| `"num_loss_tokens"` | Normalize by total loss tokens across accumulated micro-batches |
| `"num_sequences"` | Normalize by total sequences across accumulated micro-batches |
| `"none"` | No normalization (raw gradient sum) |

#firetitan-client #training-sdk #checkpointing #optimizer-step #forward-pass
