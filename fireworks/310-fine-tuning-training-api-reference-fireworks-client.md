---
title: FireworksClient - Fireworks AI Docs
url: https://docs.fireworks.ai/fine-tuning/training-api/reference/fireworks-client
source: sitemap
fetched_at: 2026-04-27T20:15:42.249003529-03:00
rendered_js: false
word_count: 546
summary: This document explains the `FireworksClient` class, which provides essential methods to interact with Fireworks platform operations independently of an active training job. It details how to initialize the client, promote checkpoints, list existing ones, and resolve specific training profiles.
tags:
    - fireworks-client
    - training-sdk
    - checkpoint-promotion
    - training-shapes
    - api-operations
    - model-validation
category: reference
optimized: true
optimized_at: 2026-04-27T20:20:00Z
---
## Overview

`FireworksClient` provides Fireworks platform operations independent of any running trainer job: checkpoint promotion, training shape resolution, and model validation. It is the base class for [[312-fine-tuning-training-api-reference-trainer-job-manager|TrainerJobManager]], which adds trainer job lifecycle methods. Use `FireworksClient` when you don't need to create or manage trainer jobs — e.g., promoting a checkpoint after a trainer is deleted, or resolving training shape configuration.

```python
from fireworks.training.sdk import FireworksClient
```

## Constructor

```python
client = FireworksClient(
    api_key="<FIREWORKS_API_KEY>",
    base_url="https://api.fireworks.ai",  # optional
)
```

| Param | Type | Default | Description |
|---|---|---|---|
| `api_key` | `str` | — | Fireworks API key |
| `base_url` | `str` | `"https://api.fireworks.ai"` | Control-plane URL |
| `additional_headers` | `dict \| None` | `None` | Extra HTTP headers |
| `verify_ssl` | `bool \| None` | `None` | SSL verification override |

## Methods

### `promote_checkpoint(job_id, checkpoint_id, output_model_id, base_model)`

Promote a sampler checkpoint to a deployable Fireworks model. The trainer job does not need to be running — `job_id` resolves the GCS bucket where checkpoint files reside.

```python
model = client.promote_checkpoint(
    job_id="<job-id>",
    checkpoint_id="<snapshot-name>",
    output_model_id="my-fine-tuned-model",
    base_model="accounts/fireworks/models/qwen3-8b",
)
print(f"Model state: {model['state']}, kind: {model['kind']}")
```

| Param | Type | Description |
|---|---|---|
| `job_id` | `str` | RLOR trainer job ID that produced the checkpoint |
| `checkpoint_id` | `str` | The `snapshot_name` from `save_weights_for_sampler_ext` |
| `output_model_id` | `str` | Desired model ID (1-63 chars, lowercase a-z, 0-9, hyphen only) |
| `base_model` | `str` | Base model resource name for metadata inheritance (e.g. `accounts/fireworks/models/qwen3-8b`) |

Returns the model dict from the API (includes `state`, `kind`, `peftDetails`). See [[059-fine-tuning-training-api-saving-and-loading|Saving and Loading]] for details and [[049-fine-tuning-training-api-cookbook-checkpoints|Checkpoint Kinds]] for which checkpoints are promotable.

> [!warning]
> Validate `output_model_id` with [`validate_output_model_id`](#validate_output_model_idoutput_model_id) before calling — a rejected ID (>63 chars or bad charset) orphans the staged sampler blob.

### `list_checkpoints(job_id, *, page_size=200)`

Server-side list of a trainer's checkpoints (sampler + DCP, with promotability metadata). Works on any trainer state — including deleted — while the DB record + GCS blobs survive. Auto-paginates. Distinct from [[311-fine-tuning-training-api-reference-service-client|FiretitanTrainingClient.list_checkpoints()]] (live-pod, DCP names only).

```python
rows = client.list_checkpoints(job_id)
latest = max((r for r in rows if r["promotable"]), key=lambda r: r["createTime"])
```

Each row has `name`, `createTime` / `updateTime` (RFC3339), `checkpointType` (opaque server enum — filter on `promotable` rather than matching values), and `promotable` (bool, authoritative). Server returns rows **oldest-first** — re-sort client-side for newest-first. Requires `fireworks-ai[training] >= 1.0.0a62`.

### `resolve_training_profile(shape_id)`

Resolve a training shape ID into a full configuration profile:

```python
shape_id = "accounts/fireworks/trainingShapes/ts-qwen3-8b-policy"
profile = client.resolve_training_profile(shape_id)
print(profile.accelerator_type)      # e.g. "NVIDIA_B200_192GB"
print(profile.trainer_image_tag)      # e.g. "0.0.0-dev-..."
print(profile.node_count)             # e.g. 1
print(profile.pipeline_parallelism)   # e.g. 1
```

See [[061-fine-tuning-training-api-training-shapes|Training Shapes]] for the user-facing shape workflow.

### `validate_output_model_id(output_model_id)`

Client-side validation helper for `promote_checkpoint(..., output_model_id=...)`:

```python
from fireworks.training.sdk import validate_output_model_id

errors = validate_output_model_id("my-fine-tuned-model")
if errors:
    raise ValueError("\n".join(errors))
```

Returns a list of formatted error strings. An empty list means the model ID is valid.

## TrainingShapeProfile

Returned by `resolve_training_profile`:

| Field | Type | Description |
|---|---|---|
| `training_shape_version` | `str` | Resolved shape version |
| `trainer_image_tag` | `str` | Docker image tag for the trainer |
| `max_supported_context_length` | `int` | Maximum supported context length |
| `node_count` | `int` | Number of trainer nodes |
| `deployment_shape_version` | `str` | Linked deployment shape |
| `accelerator_type` | `str` | GPU type |
| `accelerator_count` | `int` | Number of GPUs per node |
| `base_model_weight_precision` | `str` | Model weight precision |
| `pipeline_parallelism` | `int` | Pipeline parallelism degree |
| `training_shape` | `str` | Training shape name (without `/versions/...` suffix) |
| `deployment_shape` | `str` | Deployment shape name (without `/versions/...` suffix) |

## Relationship to TrainerJobManager

`TrainerJobManager` inherits from `FireworksClient` and adds trainer job lifecycle methods (`create`, `wait_for_ready`, `delete`, etc.). Use [[312-fine-tuning-training-api-reference-trainer-job-manager|TrainerJobManager]] when you also need to create and manage trainer jobs.

```python
from fireworks.training.sdk import FireworksClient, TrainerJobManager

# Trainer-free: promote a checkpoint from a completed experiment
client = FireworksClient(api_key=api_key)
client.promote_checkpoint(job_id, checkpoint_id, "my-model")

# Full lifecycle: create trainer, train, promote
mgr = TrainerJobManager(api_key=api_key)
endpoint = mgr.create_and_wait(config)
# ... train ...
mgr.promote_checkpoint(job_id, checkpoint_id, "my-model")
mgr.delete(job_id)
```

#fireworks-client #training-sdk #checkpoint-promotion #training-shapes
