---
title: TrainerJobManager - Fireworks AI Docs
url: https://docs.fireworks.ai/fine-tuning/training-api/reference/trainer-job-manager
source: sitemap
fetched_at: 2026-04-27T20:15:41.909615718-03:00
rendered_js: false
word_count: 758
summary: This document serves as a reference for the `TrainerJobManager` class, which manages the lifecycle of service-mode RLOR trainer jobs on Fireworks. It details methods like creating, waiting for, resuming, and deleting training jobs, alongside defining configuration objects such as `TrainerJobConfig`, `CreatedTrainerJob`, and `TrainerServiceEndpoint`.
tags:
    - trainerjobmanager
    - rlor-training
    - fireworks-client
    - job-lifecycle
    - service-mode
    - config
category: reference
optimized: true
optimized_at: 2026-04-27T20:20:00Z
---
## Overview

`TrainerJobManager` manages the lifecycle of service-mode RLOR trainer jobs — GPU-backed trainer endpoints that your custom Python loop connects to via `FiretitanServiceClient`. It extends [[310-fine-tuning-training-api-reference-fireworks-client|FireworksClient]], so all trainer-free operations (checkpoint promotion, training shape resolution) are also available here.

```python
from fireworks.training.sdk import TrainerJobManager, TrainerJobConfig
```

## Constructor

```python
rlor_mgr = TrainerJobManager(
    api_key="<FIREWORKS_API_KEY>",
    base_url="https://api.fireworks.ai",  # optional, defaults to https://api.fireworks.ai
)
```

| Param | Type | Default | Description |
|---|---|---|---|
| `api_key` | `str` | — | Fireworks API key |
| `base_url` | `str` | `"https://api.fireworks.ai"` | Control-plane URL |
| `additional_headers` | `dict \| None` | `None` | Extra HTTP headers |
| `verify_ssl` | `bool \| None` | `None` | SSL verification override |

## Methods

### `create(config)`

Create a service-mode trainer job and return immediately (without waiting). Returns a `CreatedTrainerJob`:

```python
created = rlor_mgr.create(TrainerJobConfig(
    base_model="accounts/fireworks/models/qwen3-8b",
    training_shape_ref="accounts/fireworks/trainingShapes/qwen3-8b-128k-h200",
    lora_rank=0,
    learning_rate=1e-5,
))

print(created.job_id)    # <JOB_ID>
print(created.job_name)  # accounts/<ACCOUNT_ID>/rlorTrainerJobs/<JOB_ID>
```

### `create_and_wait(config, poll_interval_s=5.0, timeout_s=900)`

Create a service-mode trainer and poll until the endpoint is healthy. Combines `create()` + `wait_for_ready()`. Returns a `TrainerServiceEndpoint`:

```python
endpoint = rlor_mgr.create_and_wait(TrainerJobConfig(
    base_model="accounts/fireworks/models/qwen3-8b",
    training_shape_ref="accounts/fireworks/trainingShapes/qwen3-8b-128k-h200",
    lora_rank=0,
    learning_rate=1e-5,
    gradient_accumulation_steps=4,
    display_name="grpo-policy-trainer",
))

print(endpoint.base_url)  # https://<trainer-endpoint>
print(endpoint.job_id)    # <JOB_ID>
print(endpoint.job_name)  # accounts/<ACCOUNT_ID>/rlorTrainerJobs/<JOB_ID>
```

### `wait_for_ready(job_id, job_name=None, poll_interval_s=5.0, timeout_s=900)`

Poll until a trainer job reaches `RUNNING` state and is healthy. Returns a `TrainerServiceEndpoint`.

### `wait_for_existing(job_id, poll_interval_s=5.0, timeout_s=900)`

Wait for an already-existing trainer job to reach `RUNNING` state:

```python
existing = rlor_mgr.wait_for_existing(job_id="<existing-job-id>")
print(existing.base_url)
```

### `resume_and_wait(job_id, poll_interval_s=5.0, timeout_s=900)`

Resume a failed/cancelled/paused job and wait until healthy:

```python
endpoint = rlor_mgr.resume_and_wait(job_id="<job-id>")
```

### `reconnect_and_wait(job_id, ...)`

Handle pod preemption and transient failures. Waits for the job to reach a resumable state, resumes it, then polls until healthy:

```python
endpoint = rlor_mgr.reconnect_and_wait(
    job_id="<job-id>",
    timeout_s=600,
    max_wait_for_resumable_s=120,
)
```

More robust than `resume_and_wait()` — retries when the job is in a transitional state (e.g. the control plane is still processing a pod death).

| Param | Type | Default | Description |
|---|---|---|---|
| `job_id` | `str` | — | The RLOR job ID to reconnect |
| `poll_interval_s` | `float` | `5.0` | Seconds between health checks after resume |
| `timeout_s` | `float` | `600` | Overall timeout for the job to become RUNNING |
| `max_wait_for_resumable_s` | `float` | `120` | Max seconds to wait for a resumable state |

### `get(job_id)`

Inspect job status:

```python
status = rlor_mgr.get(job_id=endpoint.job_id)
print(status["state"])  # JOB_STATE_RUNNING
```

### `delete(job_id)`

Delete a trainer job and release GPU resources:

```python
rlor_mgr.delete(job_id="<job-id>")
```

### `promote_checkpoint(job_id, checkpoint_id, output_model_id, base_model)`

*Inherited from [[310-fine-tuning-training-api-reference-fireworks-client|FireworksClient]].* Promote a sampler checkpoint to a deployable Fireworks model. The trainer job does not need to be running — `job_id` resolves the checkpoint's storage location.

```python
model = rlor_mgr.promote_checkpoint(
    job_id="<job-id>",
    checkpoint_id="<snapshot-name>",
    output_model_id="my-fine-tuned-model",
    base_model="accounts/fireworks/models/qwen3-8b",
)
```

### `resolve_training_profile(shape_id)`

*Inherited from [[310-fine-tuning-training-api-reference-fireworks-client|FireworksClient]].* Resolve a training shape ID into a full configuration profile. See [[310-fine-tuning-training-api-reference-fireworks-client#resolve_training_profileshape_id|FireworksClient.resolve_training_profile]] for full docs.

## TrainerJobConfig

`TrainerJobManager.create_and_wait(...)` accepts a `TrainerJobConfig` dataclass. Launching a trainer requires `training_shape_ref`. In normal user code, you should not hand-author that value — use `mgr.resolve_training_profile(...)` to get the pinned versioned ref. When `training_shape_ref` is set (the recommended **shape path**), the training shape owns the trainer's hardware and image configuration.

| Field | Type | Default | Description |
|---|---|---|---|
| `base_model` | `str` | — | Base model name (e.g. `"accounts/fireworks/models/qwen3-8b"`) |
| `training_shape_ref` | `str \| None` | `None` | Full training-shape resource name (e.g. `accounts/fireworks/trainingShapes/<shape>` or `.../versions/<ver>`). Use `mgr.resolve_training_profile(...)` to get the pinned versioned ref. See [[061-fine-tuning-training-api-training-shapes|Training Shapes]]. |
| `lora_rank` | `int` | `0` | LoRA rank. `0` for full-parameter tuning, or a positive integer (e.g. `16`, `64`) for LoRA |
| `max_context_length` | `int \| None` | `None` | Maximum sequence length. Usually inherited from the training shape on the shape path. |
| `learning_rate` | `float` | `1e-5` | Learning rate for the optimizer |
| `gradient_accumulation_steps` | `int` | `1` | Number of micro-batches before an optimizer step |
| `display_name` | `str \| None` | `None` | Human-readable trainer name |
| `region` | `str \| None` | `None` | Region for the job |
| `extra_args` | `list[str] \| None` | `None` | Extra trainer arguments |
| `forward_only` | `bool` | `False` | Create a forward-only trainer (reference model pattern) |

## CreatedTrainerJob

Returned by `create()`:

| Field | Type | Description |
|---|---|---|
| `job_name` | `str` | Full resource name (`accounts/<id>/rlorTrainerJobs/<id>`) |
| `job_id` | `str` | RLOR trainer job ID |

## TrainerServiceEndpoint

Returned by `create_and_wait`, `wait_for_ready`, `wait_for_existing`, `resume_and_wait`, and `reconnect_and_wait`:

| Field | Type | Description |
|---|---|---|
| `base_url` | `str` | Trainer endpoint URL for `FiretitanServiceClient` |
| `job_id` | `str` | RLOR trainer job ID |
| `job_name` | `str` | Full resource name (`accounts/<id>/rlorTrainerJobs/<id>`) |

## TrainingShapeProfile

See [[310-fine-tuning-training-api-reference-fireworks-client#trainingshapeprofile|FireworksClient → TrainingShapeProfile]].

## Job States

| State | Meaning |
|---|---|
| `JOB_STATE_CREATING` | Resources being provisioned |
| `JOB_STATE_PENDING` | Queued, waiting for GPU availability |
| `JOB_STATE_RUNNING` | Trainer is ready — you can connect a training client |
| `JOB_STATE_IDLE` | Service-mode job is idle |
| `JOB_STATE_COMPLETED` | Job finished successfully |
| `JOB_STATE_FAILED` | Job failed |
| `JOB_STATE_CANCELLED` | Job was cancelled |

#trainerjobmanager #rlor-training #job-lifecycle #service-mode
