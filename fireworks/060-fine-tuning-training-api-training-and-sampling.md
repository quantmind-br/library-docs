---
title: Training and Sampling - Fireworks AI Docs
url: https://docs.fireworks.ai/fine-tuning/training-api/training-and-sampling
source: sitemap
fetched_at: 2026-04-27T20:15:36.765508805-03:00
rendered_js: false
word_count: 441
summary: This document outlines the standard research loop workflow for fine-tuning models using Fireworks.AI, detailing steps from creating trainers and deployments to iterative training, checkpointing, weight synchronization, sampling, and evaluation.
tags:
    - fine-tuning
    - training-loop
    - checkpointing
    - weight-sync
    - deployment-sampler
    - api-workflow
    - research-iteration
category: tutorial
optimized: true
optimized_at: 2026-04-27T20:15:36.765508805-03:00
---
The default lifecycle for research loops: bootstrap a trainer and deployment, run iterative updates, export checkpoints, sync weights to the deployment, then sample through it for realistic evaluation.

## Workflow

1. **Create resources**: a service-mode trainer ([[056-fine-tuning-training-api-reference-deployment-manager|TrainerJobManager]]) first, then a deployment ([[056-fine-tuning-training-api-reference-deployment-manager|DeploymentManager]]) linked to the trainer's hot-load bucket.
2. **Connect a training client** from your Python loop.
3. **Run train steps**: `forward_backward_custom` + `optim_step` in a loop.
4. **Save checkpoints** at regular intervals using base/delta pattern.
5. **Weight-sync** the checkpoint to your serving deployment.
6. **Sample and evaluate** through the deployment endpoint.
7. **Record metrics** and decide whether to continue or branch experiments.

## End-to-end example

The only training-shape input you choose below is the shape ID. The API resolves the versioned reference for you before launch.

### 1. Bootstrap

```python
import os
import tinker
from fireworks.training.sdk import (
    FiretitanServiceClient,
    TrainerJobManager,
    TrainerJobConfig,
    DeploymentManager,
    DeploymentConfig,
    WeightSyncer,
)

api_key = os.environ["FIREWORKS_API_KEY"]
base_url = os.environ.get("FIREWORKS_BASE_URL", "https://api.fireworks.ai")
shape_id = "accounts/fireworks/trainingShapes/qwen3-8b-128k-h200"

rlor_mgr = TrainerJobManager(api_key=api_key, base_url=base_url)
deploy_mgr = DeploymentManager(api_key=api_key, base_url=base_url)

# This is the only shape-specific value you choose
profile = rlor_mgr.resolve_training_profile(shape_id)

# Create trainer first (trainer owns the hot-load bucket)
endpoint = rlor_mgr.create_and_wait(TrainerJobConfig(
    base_model="accounts/fireworks/models/qwen3-8b",
    training_shape_ref=profile.training_shape_version,
    lora_rank=0,
    learning_rate=1e-5,
    gradient_accumulation_steps=4,
))

# Create deployment linked to the trainer's hot-load bucket
deploy_mgr.create_or_get(DeploymentConfig(
    deployment_id="research-serving",
    base_model="accounts/fireworks/models/qwen3-8b",
    hot_load_trainer_job=endpoint.job_name,
    min_replica_count=0,
    max_replica_count=1,
))
deploy_mgr.wait_for_ready("research-serving")

# Connect client (FiretitanServiceClient provides checkpoint_type + session ID)
service = FiretitanServiceClient(base_url=endpoint.base_url, api_key=api_key)
training_client = service.create_training_client(
    base_model="accounts/fireworks/models/qwen3-8b", lora_rank=0,
)
```

### 2. Train step with custom objective

```python
def objective(data, logprobs_list):
    loss = compute_objective(data=data, logprobs_list=logprobs_list)
    return loss, {"loss": float(loss.item())}

for step in range(total_steps):
    batch = build_batch(step)
    training_client.forward_backward_custom(batch, objective).result()
    training_client.optim_step(
        tinker.AdamParams(learning_rate=1e-5, beta1=0.9, beta2=0.999, eps=1e-8, weight_decay=0.01)
    ).result()
```

### 3. Checkpoint, weight sync, and evaluate

```python
import asyncio

from transformers import AutoTokenizer
from fireworks.training.sdk import DeploymentSampler, AdaptiveConcurrencyController

# Set up WeightSyncer for automatic delta-chain management
tracker = WeightSyncer(
    policy_client=training_client,
    deploy_mgr=deploy_mgr,
    deployment_id="research-serving",
    base_model="accounts/fireworks/models/qwen3-8b",
    hotload_timeout=600,
    first_checkpoint_type="base",
)

if step % eval_interval == 0:
    # WeightSyncer auto-selects base (first) or delta (subsequent)
    tracker.save_and_hotload(f"step_{step:05d}")

    # Sample via deployment for evaluation
    tokenizer = AutoTokenizer.from_pretrained("Qwen/Qwen3-8B", trust_remote_code=True)
    sampler = DeploymentSampler(
        inference_url=deploy_mgr.inference_url,
        model=f"accounts/{deploy_mgr.account_id}/deployments/research-serving",
        api_key=api_key,
        tokenizer=tokenizer,
        concurrency_controller=AdaptiveConcurrencyController(initial_window=16),
    )
    completions = asyncio.run(
        sampler.sample_with_tokens(messages=eval_prompts, n=1)
    )
    score = evaluate_responses(completions)
    print({"step": step, "eval_score": score})
```

## Concurrency control

`sample_with_tokens(n=K)` fans out K concurrent requests. A concurrency controller prevents overloading the deployment:

- **`AdaptiveConcurrencyController`** (recommended) — automatically adjusts the concurrency window based on the server's prefill queue latency. Starts at `initial_window` and grows or shrinks between steps using AIMD.
- **`FixedConcurrencyController`** — a static semaphore with a fixed maximum. Use when you already know the right concurrency for your deployment.

See [[057-fine-tuning-training-api-reference-deployment-sampler|DeploymentSampler — Concurrency Control]] for full details.

## Reconnecting to a running trainer

If your client disconnects (script crash, notebook restart, network interruption), the trainer job keeps running on the server. Reconnect without restarting:

```python
# Reconnect to existing job (handles preemption, transitional states)
endpoint = rlor_mgr.reconnect_and_wait(job_id, timeout_s=300)

# Create a new client on the same trainer
service = FiretitanServiceClient(base_url=endpoint.base_url, api_key=api_key)
training_client = service.create_training_client(
    base_model="accounts/fireworks/models/qwen3-8b", lora_rank=0,
)

# Continue training — step_id and checkpoints are preserved
training_client.forward_backward_custom(batch, objective).result()
training_client.optim_step(adam_params).result()
```

## Operational guidance

- **Service mode supports both full-parameter and LoRA tuning.** Set `lora_rank=0` for full-parameter or a positive integer (e.g. `16`, `64`) for LoRA, and match `create_training_client(lora_rank=...)` accordingly.
- **Use `checkpoint_type="base"` for the first checkpoint**, then `"delta"` for subsequent ones to reduce save/transfer time. On full-parameter training, only `base` checkpoints are promotable — see [[049-fine-tuning-training-api-cookbook-checkpoints|Checkpoint kinds]].
- **`DeploymentSampler.sample_with_tokens()` is async** — use `await` in async code or `asyncio.run(...)` from synchronous scripts.
- **Keep checkpoint intervals predictable** so evaluation comparisons are stable.
- **Store the exact prompt set** used for each evaluation sweep for reproducibility.

## Common pitfalls

- **Sampling from trainer internals** instead of deployment endpoints can skew results — always evaluate through the serving path.
- **Missing checkpoint-to-deployment traceability** makes rollback risky — log checkpoint names alongside metrics.
- **Stale deployments**: Always verify the weight-synced checkpoint identity matches what you expect before sampling.

- [[054-fine-tuning-training-api-loss-functions|Loss Functions]] — built-in and custom loss function patterns
- [[062-fine-tuning-training-api-vision-inputs|Vision Inputs]] — fine-tune VLMs with image and text data
- [[059-fine-tuning-training-api-saving-and-loading|Saving and Loading]] — checkpoint types and weight sync details
- [[057-fine-tuning-training-api-reference-deployment-sampler|DeploymentSampler reference]] — sampling API details
- [[058-fine-tuning-training-api-reference-weight-syncer|WeightSyncer reference]] — weight sync lifecycle

#fine-tuning #training-loop #checkpointing #weight-sync #deployment-sampler #api-workflow #research-iteration
