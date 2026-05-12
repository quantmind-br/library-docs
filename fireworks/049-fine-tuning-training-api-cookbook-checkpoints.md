---
title: Checkpoints and Resume - Fireworks AI Docs
url: https://docs.fireworks.ai/fine-tuning/training-api/cookbook/checkpoints
source: sitemap
fetched_at: 2026-04-27T20:12:39.799890798-03:00
rendered_js: false
word_count: 660
summary: This document details how training recipes manage checkpointing automatically, focusing on the configuration fields needed to enable saving and promotion. It outlines different methods for resuming (automatic vs. from another job), explains the relationship between local files and control plane data, and provides a reference guide to various checkpoint types and their promotability status across the stack.
tags:
    - checkpoint-management
    - training-recipes
    - config-fields
    - resuming-training
    - promotable-checkpoints
    - fireworks-api
category: guide
optimized: true
optimized_at: 2026-04-27T00:00:00Z
---
# Checkpoints and Resume

Cookbook recipes (`rl_loop`, `sft_loop`, `dpo_loop`, `orpo_loop`, `igpo_loop`) handle checkpointing automatically. Set two config fields and the recipe handles save, resume, and promote:

- `dcp_save_interval=N` — save resumable checkpoints every N steps
- `output_model_id="my-model"` — promote the final checkpoint to a deployable Fireworks model

Rerunning with the same `log_path` resumes from the last saved checkpoint automatically.

```python
from training.recipes.sft_loop import Config, main
from training.utils import InfraConfig, WeightSyncConfig

cfg = Config(
    log_path="./my_training",
    base_model="accounts/fireworks/models/qwen3-8b",
    dataset="data.jsonl",
    tokenizer_model="Qwen/Qwen3-8B",
    output_model_id="qwen3-8b-finetuned",
    weight_sync=WeightSyncConfig(dcp_save_interval=10),
    infra=InfraConfig(
        training_shape_id="accounts/fireworks/trainingShapes/qwen3-8b-128k-h200",
    ),
)
main(cfg)

# Interrupted? Run again with the same config — it picks up automatically.
main(cfg)
```

## Config fields

| Field | Type | Default | Description |
|-------|------|---------|-------------|
| `log_path` | `str` | (required) | Directory for the recipe's local bookkeeping (`dataloader.json`) and logs |
| `weight_sync.dcp_save_interval` | `int` | `0` | Save a resumable (DCP) checkpoint every N steps. `0` = off. |
| `output_model_id` | `str \| None` | `None` | Promote the final checkpoint to this Fireworks model ID at the end of training |
| `init_from_checkpoint` | `str \| None` | `None` | Load weights from another job (`"job-id:checkpoint-name"`). Step counter resets to 0. |

## Resuming training

### Automatic (same log_path)

Rerun with the same `log_path` and the recipe resumes automatically. It queries the control plane for the newest resumable checkpoint on the trainer job and reloads weights and optimizer state. The step counter and `data_consumed` counter are restored from `dataloader.json`.

### From another job

```python
config = Config(
    log_path="./new_run",
    init_from_checkpoint="i44pvd4syzg8hjfk:step-4",  # job_id:checkpoint_name
    ...
)
```

Loads weights from the specified job, resets step to 0. Mutually exclusive with automatic resume.

### Manual promotion

To promote an arbitrary checkpoint after training (not just the final one):

```bash
export FIREWORKS_API_KEY=...

python promote_checkpoint.py \
    --job-id <trainer-job-id> \
    --output-model-id my-fine-tuned-model \
    --base-model accounts/fireworks/models/qwen3-8b
```

By default the script promotes the newest promotable checkpoint. Pass `--checkpoint-name <name>` to promote a specific one.

## Advanced internals

### What gets saved, where

| Surface | Owns | Source of truth for |
|---------|------|---------------------|
| Control plane (`FireworksClient.list_checkpoints(job_id)`) | All remote checkpoint blobs (DCP and sampler) | What checkpoints exist, their type, and whether each is promotable |
| `{log_path}/dataloader.json` | Local file | The cookbook's `data_consumed` counter per checkpoint name |

There is no `checkpoints.jsonl` registry — the control plane is queried at resume/promote time.

### Two axes: resumable and promotable

| Axis | What it writes | Resumes? | Promotes to a model? |
|------|----------------|----------|----------------------|
| `resumable=True` | DCP (weights + optimizer) | Yes | No |
| `promotable=True` | Sampler weights (HF format) | No | Yes |
| Both | DCP + sampler | Yes | Yes |

Periodic saves use `resumable=True` only. The final save uses both. For LoRA RL runs, `WeightSyncer.save_and_hotload` already produces a promotable row each step.

### Forking a recipe

If you fork a recipe and need to drive checkpointing yourself, instantiate `TrainingCheckpoints`:

```python
from training.utils.checkpoints import TrainingCheckpoints

ckpt = TrainingCheckpoints(
    policy,           # ReconnectableClient
    rlor_mgr,         # TrainerJobManager (control-plane client)
    trainer_id=policy_job_id,
    log_path=cfg.log_path,
    lora_rank=cfg.lora_rank,
)

# Resume on startup
resume_info = ckpt.resume(
    init_from_checkpoint=cfg.init_from_checkpoint,
    warm_start_from_adapter=cfg.warm_start_from_adapter,
)
step_offset = resume_info.step if resume_info else 0

# Periodic save
ckpt.save(f"step-{step}", resumable=True, promotable=False, data_consumed=count)

# Final save + promote
ckpt.save(f"step-{step}", resumable=True, promotable=True, data_consumed=count)
if cfg.output_model_id:
    ckpt.promote_latest(cfg.output_model_id, cfg.base_model)
```

The class forwards `save_state` / `save_weights_for_sampler_ext` / `promote_checkpoint` to the SDK. See [[059-fine-tuning-training-api-saving-and-loading|Saving and Loading]] for the full API surface.

### Checkpoint kinds

Three separate layers have their own "type" — confusing them is the usual reason a promotion fails:

| Layer | Where | Values | What it controls |
|-------|-------|--------|------------------|
| **Cookbook** | `TrainingCheckpoints.save(resumable=, promotable=)` | Two booleans | Which of DCP / sampler blob (or both) gets saved |
| **SDK** | `save_weights_for_sampler_ext(checkpoint_type=...)` | `"base"`, `"delta"` | Whether the sampler blob is full weights or an `arc_v2` delta |
| **Server** | `checkpointType` on each control-plane row | `TRAINING`, `TRAINING_LORA`, `INFERENCE_BASE`, `INFERENCE_LORA`, `INFERENCE_ARC_V2` | Detected from blob contents |

When the cookbook saves with `promotable=True`, it always calls the SDK with `checkpoint_type="base"`, which the server detects as `INFERENCE_BASE` or `INFERENCE_LORA`. Both are promotable. `INFERENCE_ARC_V2` (delta on full-param) is not promotable.

### Promotability cheat sheet

| How it was saved | LoRA promotable | Full-param promotable |
|------------------|------------------|-----------------------|
| `TrainingCheckpoints.save(resumable=True, promotable=False)` | No | No |
| `TrainingCheckpoints.save(promotable=True)` | Yes | Yes |
| `save_weights_for_sampler_ext(checkpoint_type="base")` | Yes | Yes |
| `save_weights_for_sampler_ext(checkpoint_type="delta")` | Yes | No |
| `WeightSyncer.save_and_hotload()` — first save | Yes | Yes |
| `WeightSyncer.save_and_hotload()` — later saves | Yes | No |

## Related

- [[059-fine-tuning-training-api-saving-and-loading|Saving and Loading]] — SDK-level reference for save / load / promote
- [[058-fine-tuning-training-api-reference-weight-syncer|WeightSyncer reference]] — weight-sync lifecycle
- [[051-fine-tuning-training-api-cookbook-rl|Cookbook RL]] — full GRPO walkthrough

#checkpoint-management #training-recipes #config-fields #resuming-training #promotable-checkpoints #fireworks-api
