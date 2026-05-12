---
title: WeightSyncer - Fireworks AI Docs
url: https://docs.fireworks.ai/fine-tuning/training-api/reference/weight-syncer
source: sitemap
fetched_at: 2026-04-27T20:15:52.69176207-03:00
rendered_js: false
word_count: 440
summary: This document describes the `WeightSyncer` class, which is responsible for managing the saving of sampler checkpoints and synchronizing them to a deployment.
tags:
    - weight-syncer
    - checkpointing
    - deployment-sync
    - hotload
    - training-workflow
    - base-delta
category: guide
optimized: true
optimized_at: 2026-04-27T20:15:52.69176207-03:00
---
`WeightSyncer` coordinates saving sampler checkpoints and syncing them to a deployment, including automatic base/delta chain state tracking, session-scoped snapshot naming, and post-sync warmup.

```python
from fireworks.training.sdk import WeightSyncer
```

## Constructor

```python
tracker = WeightSyncer(
    policy_client=training_client,
    deploy_mgr=deploy_mgr,
    deployment_id="my-deployment",
    base_model="accounts/fireworks/models/qwen3-8b",
    hotload_timeout=600,
    first_checkpoint_type="base",
    warmup_after_hotload=True,
    reset_prompt_cache=True,
    lora_rank=0,  # >0 for LoRA adapters (disables delta chain)
)
```

| Field | Type | Default | Description |
|---|---|---|---|
| `policy_client` | `FiretitanTrainingClient` | — | Training client for save operations |
| `deploy_mgr` | `DeploymentManager \| None` | `None` | Deployment manager for weight sync |
| `deployment_id` | `str \| None` | `None` | Target deployment for weight sync |
| `base_model` | `str` | `""` | Model name for weight sync API calls |
| `hotload_timeout` | `int` | `600` | Timeout in seconds for `hotload_and_wait` |
| `first_checkpoint_type` | `str` | `"base"` | Type for the first checkpoint (`"base"` or `"delta"`) |
| `compression_format` | `str` | `"arc_v2"` | Delta compression format |
| `warmup_after_hotload` | `bool` | `True` | Send a warmup request after each successful weight sync |
| `warmup_max_retries` | `int` | `10` | Max retries for post-weight-sync warmup |
| `reset_prompt_cache` | `bool` | `True` | Reset the deployment's prompt cache after each weight sync |
| `lora_rank` | `int` | `0` | When > 0, forces all checkpoints to `base` type. LoRA adapter exports are standalone PEFT artifacts that cannot use incremental delta compression. |

## Methods

### `save_and_hotload(name, checkpoint_type=None)`

Save sampler weights and sync to deployment. Automatically handles base (first) vs delta (subsequent) checkpoint types. Returns the `snapshot_name` (`str | None`) on success or raises on failure:

```python
tracker.save_and_hotload(f"step-{step:05d}")
```

### `save_only(name, checkpoint_type=None)`

Save sampler weights without syncing to deployment:

```python
snapshot = tracker.save_only("checkpoint-name", checkpoint_type="base")
```

Returns `snapshot_name` or `None`.

### `hotload(snapshot_name, checkpoint_type)`

Sync a previously saved snapshot to the deployment:

```python
tracker.hotload(snapshot, checkpoint_type="base")
```

Returns `True` on success, `False` on failure.

### `check_deployment_state()`

Query the deployment's current weight sync state:

```python
current = tracker.check_deployment_state()
print(current)  # current_snapshot_identity or None
```

### `wait_for_hotload_ready(timeout_s=300, poll_interval_s=5)`

Block until the deployment's weight sync manager is initialized.

### `reset_delta_chain()`

Force the next save to be treated as `base`. Call when the deployment's bucket changes under you — otherwise the next `delta` references a base the deployment never loaded. Re-attaching a live deployment to a new trainer is not a user workflow; reach out to Fireworks support for that.

## Usage patterns

### On-policy weight sync (every step)

For on-policy training (e.g. GRPO), sync weights after every optimizer step:

```python
import asyncio

for step in range(total_steps):
    # ... training step ...
    tracker.save_and_hotload(f"step-{step:05d}")
    completions = asyncio.run(
        sampler.sample_with_tokens(messages=input_messages, n=4)
    )
```

### Interval weight sync (off-policy)

For off-policy training, sync weights every N steps:

```python
for step in range(total_steps):
    # ... training step ...
    if step % weight_sync_interval == 0:
        tracker.save_and_hotload(f"step-{step:05d}")
```

### Split save and sync

Separate save from weight sync when you need intermediate steps (e.g. warmup):

```python
snapshot = tracker.save_only("resume-step-0", checkpoint_type="base")
deploy_mgr.warmup(model)
tracker.hotload(snapshot, checkpoint_type="base")
```

### DCP checkpoints for resume

Save DCP checkpoints at intervals using the training client directly:

```python
for step in range(total_steps):
    # ... training step ...
    tracker.save_and_hotload(f"step-{step:05d}")
    if step % dcp_interval == 0:
        training_client.save_state(f"step-{step}")
```

- [[056-fine-tuning-training-api-reference-deployment-manager|DeploymentManager]] — deployment lifecycle and hotload API
- [[059-fine-tuning-training-api-saving-and-loading|Saving and Loading]] — checkpoint concepts
- [[060-fine-tuning-training-api-training-and-sampling|Training and Sampling]] — end-to-end workflow

#weight-syncer #checkpointing #deployment-sync #hotload #training-workflow #base-delta
