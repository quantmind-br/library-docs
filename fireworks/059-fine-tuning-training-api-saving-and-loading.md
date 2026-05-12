---
title: Saving and Loading - Fireworks AI Docs
url: https://docs.fireworks.ai/fine-tuning/training-api/saving-and-loading
source: sitemap
fetched_at: 2026-04-27T20:12:39.74788013-03:00
rendered_js: false
word_count: 407
summary: This document serves as a technical guide detailing the various ways to save, manage, and utilize training checkpoints within the Fireworks AI ecosystem.
tags:
    - checkpointing
    - training-state
    - weight-sync
    - promotion
    - delta-saving
    - fireworks-ai
category: guide
optimized: true
optimized_at: 2026-04-27T20:12:39.74788013-03:00
---
Checkpoints serve three purposes during training:

1. **Weight sync** (`save_weights_for_sampler_ext`) — push updated weights to a running inference deployment without restarting it.
2. **Resuming** (`save_state` / `load_state_with_optimizer`) — persist full training state (weights + optimizer) to continue training later.
3. **Promotion** (`promote_checkpoint`) — turn a saved sampler checkpoint into a deployable Fireworks model.

## Sampler checkpoints

Sampler checkpoints are weight-only snapshots used for weight sync and promotion. Two `checkpoint_type` modes affect size and weight-sync speed:

| `checkpoint_type` | What it saves | Size |
|---|---|---|
| `"base"` | Full model weights | Large (~16 GB for 8B) |
| `"delta"` | XOR diff from previous base | ~10× smaller |

Delta is much faster for per-step weight sync (`current_weights = base XOR delta` on the deployment). LoRA sampler checkpoints always contain the full adapter regardless of `checkpoint_type`.

### Saving checkpoints

```python
# First checkpoint — must be base (full weights)
result = training_client.save_weights_for_sampler_ext(
    "step-0001",
    checkpoint_type="base",
)
# result.snapshot_name is session-qualified (e.g. "step-0001-a1b2c3d4")

# Subsequent checkpoints — delta is faster
result = training_client.save_weights_for_sampler_ext(
    "step-0010",
    checkpoint_type="delta",
)

# With TTL (auto-delete after N seconds)
result = training_client.save_weights_for_sampler_ext(
    "temp-checkpoint",
    checkpoint_type="delta",
    ttl_seconds=3600,
)
```

### Promoting a checkpoint

Promote a sampler checkpoint to a deployable Fireworks model. Available on both `FireworksClient` and `TrainerJobManager`. The trainer job does not need to be running — promotion is a metadata + file-copy operation.

> [!note]
> See [[049-fine-tuning-training-api-cookbook-checkpoints|Checkpoint kinds]] for which checkpoints are promotable.

#### Preferred: pass the 4-segment `name=` from `list_checkpoints`

```python
from fireworks.training.sdk import FireworksClient

client = FireworksClient(api_key=api_key)

# Pick a row from the trainer's checkpoints — usually newest promotable.
rows = client.list_checkpoints(job_id)
target = next(r for r in rows if r.get("promotable"))

model = client.promote_checkpoint(
    name=target["name"],                          # 4-segment resource path
    output_model_id="my-fine-tuned-qwen3-8b",
    base_model="accounts/fireworks/models/qwen3-8b",
)
```

| Parameter | Type | Description |
|---|---|---|
| `name` | `str` | Full 4-segment checkpoint resource name from `list_checkpoints` output |
| `output_model_id` | `str` | Desired model ID (1-63 chars, lowercase a-z, 0-9, hyphen only). Validate with `validate_output_model_id` before calling. |
| `base_model` | `str` | Base model resource name for metadata inheritance (e.g. `accounts/fireworks/models/qwen3-8b`) |

#### Legacy: positional `(job_id, checkpoint_id)` form

```python
model = client.promote_checkpoint(
    job_id=endpoint.job_id,
    checkpoint_id=result.snapshot_name,
    output_model_id="my-fine-tuned-qwen3-8b",
    base_model="accounts/fireworks/models/qwen3-8b",
)
# DeprecationWarning: promote_checkpoint(job_id, checkpoint_id, ...)
# positional form is deprecated. Pass the 4-segment resource name instead.
```

The `hot_load_deployment_id` parameter is also deprecated (the gateway resolves the bucket URL from the trainer's stored metadata).

### Listing checkpoints on a trainer

```bash
curl "https://api.fireworks.ai/v1/accounts/<account-id>/rlorTrainerJobs/<job-id>/checkpoints?pageSize=200" \
  -H "Authorization: Bearer $FIREWORKS_API_KEY"
```

Each entry includes `name`, `createTime`, `updateTime`, `checkpointType`, and `promotable`.

## Weight sync

Weight sync pushes a checkpoint onto a running inference deployment without restarting it. See [[058-fine-tuning-training-api-reference-weight-syncer|WeightSyncer]] for the recommended lifecycle manager.

```python
from fireworks.training.sdk import WeightSyncer

syncer = WeightSyncer(
    policy_client=training_client,
    deploy_mgr=deploy_mgr,
    deployment_id="my-deployment",
    base_model="accounts/fireworks/models/qwen3-8b",
    hotload_timeout=600,
    first_checkpoint_type="base",
)

# Automatically handles base (first) vs delta (subsequent)
syncer.save_and_hotload(f"step-{step:05d}")
```

## Train-state checkpoints

Use `save_state` to persist full training state, and one of two load methods to restore it:

| Method | Weights | Optimizer state |
|---|---|---|
| `load_state_with_optimizer(path)` | Restored | Restored |
| `load_state(path)` | Restored | Reset to zero |

```python
# Save full train state for resume
training_client.save_state("train_state_step_100").result()

# Resume training (weights + optimizer restored)
training_client.load_state_with_optimizer("train_state_step_100").result()
```

`save_state` accepts an optional `ttl_seconds` parameter for auto-expiring checkpoints.

### Cross-job checkpoint resolution

```python
checkpoint_ref = training_client.resolve_checkpoint_path(
    "step-4",
    source_job_id="previous-job-id",
)
training_client.load_state_with_optimizer(checkpoint_ref).result()
```

### List available checkpoints

```python
checkpoint_names = training_client.list_checkpoints()
print(checkpoint_names)  # e.g. ["step-2", "step-4"]
```

- [[049-fine-tuning-training-api-cookbook-checkpoints|Checkpoints and Resume (cookbook)]] — recipe-driven save / resume / promote
- [[058-fine-tuning-training-api-reference-weight-syncer|WeightSyncer reference]] — full weight sync lifecycle
- [[056-fine-tuning-training-api-reference-deployment-manager|DeploymentManager reference]] — direct hotload API

#checkpointing #training-state #weight-sync #promotion #delta-saving
