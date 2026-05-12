---
title: Cookbook Reference - Fireworks AI Docs
url: https://docs.fireworks.ai/fine-tuning/training-api/cookbook/reference
source: sitemap
fetched_at: 2026-04-27T20:15:17.538665758-03:00
rendered_js: false
word_count: 979
summary: This document provides a reference guide to various configuration classes (InfraConfig, DeployConfig, WeightSyncConfig, WandBConfig) and the ReconnectableClient utility used in training recipes, detailing their fields, defaults, and purpose.
tags:
    - infra-config
    - deploy-config
    - weight-sync
    - wandb-logging
    - reconnectable-client
    - training-parameters
category: reference
optimized: true
optimized_at: 2026-04-27T23:04:00Z
---
# Training API Cookbook Reference

Configuration classes and utilities used in training recipes. All imports from `training.utils`.

## InfraConfig

GPU, region, and training shape settings. Wraps `TrainerJobConfig` fields.

```python
from training.utils import InfraConfig

infra = InfraConfig(
    training_shape_id="accounts/fireworks/trainingShapes/qwen3-8b-128k-h200",
    ref_training_shape_id="accounts/fireworks/trainingShapes/qwen3-8b-128k-h200-forward",
)
```

Use `training_shape_id` for every launched trainer. Pass the full shared path `accounts/fireworks/trainingShapes/<shape>`. Add `ref_training_shape_id` when the recipe also launches a reference trainer.

| Field | Type | Default | Description |
|---|---|---|---|
| `training_shape_id` | `str \| None` | `None` | Full training-shape ID for the policy trainer, e.g. `accounts/fireworks/trainingShapes/<shape>`. Resolves versioned reference and auto-populates shape-owned infra. |
| `ref_training_shape_id` | `str \| None` | `None` | Full training-shape ID for the reference trainer. When unset, `rl_loop` skips reference-model provisioning. |
| `region` | `str \| None` | `None` | Region override |
| `trainer_timeout_s` | `float` | `3600` | Timeout for trainer provisioning / readiness waits |
| `extra_args` | `list[str] \| None` | `None` | Extra trainer arguments |

## DeployConfig

Deployment settings for sampling and weight sync. Wraps `DeploymentConfig` fields.

```python
from training.utils import DeployConfig

deploy_cfg = DeployConfig(
    deployment_id="grpo-serving",
    tokenizer_model="Qwen/Qwen3-8B",
)
```

When `deployment_shape` is set (recommended), the shape owns deployment hardware and serving configuration.

| Field | Type | Default | Description |
|---|---|---|---|
| `deployment_id` | `str \| None` | `None` | Deployment identifier. If unset, auto-derived from the base model name. |
| `tokenizer_model` | `str \| None` | `None` | HuggingFace model name for client-side tokenization. Required for RL sampling. |
| `deployment_shape` | `str \| None` | `None` | Deployment shape resource name. When set, the shape owns GPU type and serving config. |
| `deployment_region` | `str \| None` | `None` | Region override for the deployment |
| `hot_load_bucket_type` | `str` | `"FW_HOSTED"` | Weight-sync storage backend |
| `hot_load_trainer_job` | `str \| None` | `None` | Trainer job whose weight-sync bucket this deployment should use. Format: `accounts/{account}/rlorTrainerJobs/{job_id}` |
| `deployment_timeout_s` | `float` | `5400` | Timeout for deployment provisioning / readiness waits |
| `deployment_extra_args` | `list[str] \| None` | `None` | Extra serving arguments |
| `sample_timeout` | `int` | `600` | HTTP read timeout for sampling completions |
| `disable_speculative_decoding` | `bool` | `True` | Disable speculative decoding for weight-sync compatibility |
| `extra_values` | `dict[str, str] \| None` | `None` | Extra deployment Helm values |
| `replica_count` | `int \| None` | `None` | Pin deployment to a fixed replica count (sets both min and max) |

## WeightSyncConfig

Checkpoint and weight-sync intervals.

```python
from training.utils import WeightSyncConfig

weight_sync = WeightSyncConfig(
    weight_sync_interval=1,
    dcp_save_interval=10,
)
```

| Field | Type | Default | Description |
|---|---|---|---|
| `dcp_save_interval` | `int` | `0` | Save DCP checkpoints for resume every N steps. `0` disables. **Set > 0 to enable resume.** |
| `weight_sync_interval` | `int` | `1` | Save + sync sampler weights every N optimizer steps. `0` disables weight sync. |
| `dcp_timeout` | `int` | `2700` | Timeout for DCP save/load operations |
| `first_checkpoint_type` | `str` | `"base"` | First sampler checkpoint type passed to `WeightSyncer` |
| `weight_sync_before_training` | `bool` | `False` | Save a base checkpoint and sync it to the deployment before the first training step |
| `weight_sync_timeout` | `int` | `600` | Timeout for each weight-sync operation |

## WandBConfig

Weights & Biases logging settings.

```python
from training.utils import WandBConfig

wandb = WandBConfig(
    entity="my-team",
    project="grpo-experiment",
    run_name="qwen3-8b-v1",
)
```

| Field | Type | Default | Description |
|---|---|---|---|
| `entity` | `str \| None` | `None` | W&B team or user name |
| `project` | `str \| None` | `None` | W&B project name |
| `run_name` | `str \| None` | `None` | Run name (auto-generated if omitted) |

## ReconnectableClient

Blocking convenience wrapper around `FiretitanTrainingClient`. All cookbook recipes use this as their training client — it dispatches each call and blocks until the result is ready or the timeout expires. Failures propagate to the caller so the training loop can crash cleanly and resume from the last DCP checkpoint.

```python
from training.utils import ReconnectableClient

client = ReconnectableClient(
    rlor_mgr=rlor_mgr,
    job_id=endpoint.job_id,
    base_model="accounts/fireworks/models/qwen3-8b",
    lora_rank=0,
    fw_api_key=api_key,
)

result = client.forward_backward_custom(datums, loss_fn)
client.optim_step(tinker.AdamParams(...))
```

### Constructor parameters

| Param | Type | Default | Description |
|---|---|---|---|
| `rlor_mgr` | `TrainerJobManager` | required | Manager used to connect to the trainer |
| `job_id` | `str` | required | RLOR trainer job ID |
| `base_model` | `str` | required | Base model name |
| `lora_rank` | `int` | `0` | LoRA rank (`0` for full-parameter) |
| `fw_api_key` | `str \| None` | `None` | Fireworks API key (falls back to `FIREWORKS_API_KEY` env var) |
| `default_timeout` | `int` | `600` | Timeout in seconds for forward/backward/optim calls |
| `endpoint` | `TrainerServiceEndpoint \| None` | `None` | Pre-resolved endpoint (skips `wait_for_existing` on init) |

### Properties

| Property | Type | Description |
|---|---|---|
| `inner` | `FiretitanTrainingClient` | Underlying API client (advanced use) |
| `endpoint` | `TrainerServiceEndpoint` | Resolved trainer endpoint (base_url, job_id, job_name) |
| `job_id` | `str` | Trainer job ID |

### Methods

| Method | Description |
|---|---|
| `forward(data, loss_fn)` | Forward pass, blocks until complete |
| `forward_backward(data, loss_fn, loss_fn_config)` | Forward + backward pass |
| `forward_backward_custom(data, loss_fn)` | Forward + backward with custom loss function |
| `optim_step(params, grad_accumulation_normalization)` | Optimizer step |
| `save_state(name, timeout)` | Save DCP checkpoint (default timeout: 2700s) |
| `load_state_with_optimizer(path, timeout)` | Load DCP checkpoint (default timeout: 2700s) |
| `save_weights_for_sampler_ext(name, checkpoint_type, timeout)` | Save sampler checkpoint for promotion |
| `resolve_checkpoint_path(name, source_job_id)` | Resolve cross-job checkpoint path |
| `list_checkpoints()` | List available DCP checkpoints |

## Checkpoint utilities

For checkpointing, resume, and promote — see [[049-fine-tuning-training-api-cookbook-checkpoints|Checkpoints and Resume]].

## Gradient accumulation normalization

Recipe configs expose `grad_accumulation_normalization`, passed to `optim_step(...)`:

```python
client.optim_step(adam_params, grad_accumulation_normalization="num_loss_tokens")
```

See [[054-fine-tuning-training-api-loss-functions#gradient-accumulation-normalization|Loss Functions — Gradient Accumulation Normalization]] for how to choose the mode and avoid double-normalization.

### Recipe defaults

| Recipe | Default | Rationale |
|---|---|---|
| SFT | `None` | SFT loss is already normalized client-side |
| GRPO / RL | `"num_loss_tokens"` | RL losses use server-side per-token normalization by default |
| DPO | `None` | DPO loss is already normalized client-side |
| ORPO | `None` | ORPO loss is already normalized client-side |
