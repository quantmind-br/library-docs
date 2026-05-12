---
title: 'Cookbook: RL - Fireworks AI Docs'
url: https://docs.fireworks.ai/fine-tuning/training-api/cookbook/rl
source: sitemap
fetched_at: 2026-04-27T20:15:22.139120311-03:00
rendered_js: false
optimized: true
optimized_at: 2026-04-27T00:00:00Z
tags:
    - grpo
    - policy-optimization
    - reinforcement-learning
    - cookbook
    - rl-loop
category: guide
word_count: 497
---
## What this is

GRPO (Group Relative Policy Optimization) samples multiple completions per prompt, scores them with a reward function, and uses group reward statistics for policy gradient updates via the cookbook's `rl_loop` recipe.

## Architecture

| Component | Role |
|---|---|
| **Policy trainer** | Trainable model — runs `forward_backward_custom` + `optim_step` |
| **Reference trainer** | Optional frozen copy — provides KL/reference logprobs (`--forward-only`) when `infra.ref_training_shape_id` is set |
| **Deployment** | Sampling completions via `DeploymentSampler` (client-side tokenized) |

## Using the recipe

```
from training.recipes.rl_loop import Config, main
from training.utils import DeployConfig, InfraConfig, WeightSyncConfig, WandBConfig

cfg = Config(
    log_path="./grpo_logs",
    base_model="accounts/fireworks/models/qwen3-8b",
    dataset="/path/to/gsm8k.jsonl",
    max_rows=200,
    epochs=1,
    completions_per_prompt=4,
    max_completion_tokens=1024,
    temperature=1.0,
    max_seq_len=4096,
    policy_loss="grpo",  # or "importance_sampling", "dapo", "dro", "gspo", "cispo"
    infra=InfraConfig(
        training_shape_id="accounts/fireworks/trainingShapes/qwen3-8b-128k-h200",
        ref_training_shape_id="accounts/fireworks/trainingShapes/qwen3-8b-128k-h200-forward",
    ),
    deployment=DeployConfig(
        deployment_id="grpo-serving",
        tokenizer_model="Qwen/Qwen3-8B",
    ),
    weight_sync=WeightSyncConfig(weight_sync_interval=1),
    wandb=WandBConfig(entity="my-team", project="grpo-experiment"),
)

main(cfg)
```

The recipe handles resource provisioning, rollout scheduling, reference logprobs, checkpointing, and cleanup automatically.

### Policy loss variants

| `policy_loss` | Description |
|---|---|
| `"grpo"` | REINFORCE + KL penalty (default) |
| `"importance_sampling"` | Off-policy ratio weighting with optional clipping |
| `"reinforce"` | Vanilla REINFORCE |
| `"dapo"` | Dynamic advantage with asymmetric PPO clipping |
| `"dro"` | Distributionally robust off-policy objective |
| `"gspo"` | Sequence-level clipped PPO |
| `"cispo"` | Clipped importance sampling policy optimization |

## Step-by-step (API-level)

For full control beyond what the recipe provides.

### Provision resources with `setup_infra`

`training.utils.rl.setup_infra` handles shape resolution, parallel trainer + deployment provisioning, LoRA shared-reference branching, and re-attach. Recipes pass a config + two booleans (`needs_reference`, `needs_inference`) and get back an `Infra` bundle of wired trainer clients.

```
import os
import transformers
from fireworks.training.sdk import (
    TrainerJobManager, DeploymentManager, DeploymentSampler, WeightSyncer,
    AdaptiveConcurrencyController,
)
from training.utils import (
    InfraConfig, DeployConfig, ResourceCleanup, WeightSyncScope,
)
from training.utils.rl import setup_infra

api_key = os.environ["FIREWORKS_API_KEY"]
base_url = os.environ.get("FIREWORKS_BASE_URL", "https://api.fireworks.ai")

rlor_mgr = TrainerJobManager(api_key=api_key, base_url=base_url)
deploy_mgr = DeploymentManager(api_key=api_key, base_url=base_url)

base_model = "accounts/fireworks/models/qwen3-8b"
infra_cfg = InfraConfig(
    training_shape_id="accounts/fireworks/trainingShapes/qwen3-8b-128k-h200",
    ref_training_shape_id="accounts/fireworks/trainingShapes/qwen3-8b-128k-h200-forward",
)
deploy_cfg = DeployConfig(
    deployment_id="grpo-serving",
    tokenizer_model="Qwen/Qwen3-8B",
    weight_sync_scope=WeightSyncScope.PER_TRAINER,  # default
)

with ResourceCleanup(rlor_mgr, deploy_mgr) as cleanup:
    infra = setup_infra(
        rlor_mgr=rlor_mgr,
        deploy_mgr=deploy_mgr,
        base_model=base_model,
        infra_cfg=infra_cfg,
        deploy_cfg=deploy_cfg,
        lora_rank=0,
        needs_reference=True,   # KL baseline
        needs_inference=True,   # rollouts
        role_prefix="grpo",
        api_key=api_key,
        cleanup=cleanup,
    )

policy = infra.policy          # ReconnectableClient (policy trainer)
reference = infra.reference    # ReconnectableClient (forward-only) or LoRA shared handle
inference_model = infra.inference_model

tokenizer = transformers.AutoTokenizer.from_pretrained("Qwen/Qwen3-8B", trust_remote_code=True)
sampler = DeploymentSampler(
    inference_url=deploy_mgr.inference_url,
    model=inference_model,
    api_key=api_key,
    tokenizer=tokenizer,
    concurrency_controller=AdaptiveConcurrencyController(initial_window=16),
)
```

> [!info]
> See [[053-fine-tuning-training-api-cookbook-weight-sync]] for `WeightSyncScope.PER_TRAINER` vs `PER_DEPLOYMENT`.

### Training loop

```
import asyncio

tracker = WeightSyncer(
    policy_client=policy.inner,
    deploy_mgr=deploy_mgr,
    deployment_id="grpo-serving",
    base_model=base_model,
    hotload_timeout=600,
    first_checkpoint_type="base",
)

for row in dataset:
    input_messages = [m for m in row["messages"] if m.get("role") != "assistant"]
    completions = asyncio.run(
        sampler.sample_with_tokens(messages=input_messages, n=4, max_tokens=512)
    )
    rewards = [score(c) for c in completions]
    if len(set(rewards)) == 1:
        continue

    datums = build_grpo_datums(completions)
    ref_fwd = reference.forward(datums, "cross_entropy")
    ref_logprobs = [list(x["logprobs"].data) for x in ref_fwd.loss_fn_outputs]

    loss_fn = make_grpo_loss_fn(rewards, ref_logprobs, kl_beta=0.001)
    policy.forward_backward_custom(datums, loss_fn)
    policy.optim_step(
        tinker.AdamParams(learning_rate=1e-5, beta1=0.9, beta2=0.999, eps=1e-8, weight_decay=0.01)
    )

    tracker.save_and_hotload(f"step-{step:05d}")
```

> [!info]
> See [[054-fine-tuning-training-api-loss-functions]] for `make_grpo_loss_fn` and `build_grpo_datums` implementations.

## Pipeline overlap

Sampling and training overlap within **policy windows** controlled by `weight_sync_interval`. All prompts in a window sample concurrently; results train as they arrive. At window boundaries the pipeline drains, weights sync to the deployment, and the next window samples against the updated weights.

| `weight_sync_interval` | Behavior |
|---|---|
| `1` (default) | No overlap — sample, train, sync, repeat |
| `N > 1` | N-step windows with overlap inside, sync at boundaries |
| `0` | No syncs — the deployment keeps the base weights for the entire run. Useful for debugging or ablations. |

## Operational guidance

- **`deployment.tokenizer_model` is required** — raises `ValueError` if not set.
- **Set `infra.training_shape_id`** — training shapes are the launch path for cookbook trainers.
- **Set `infra.ref_training_shape_id`** when you want a reference trainer; if unset, the recipe skips reference-model provisioning entirely.
- **Skip prompts with uniform rewards** — they provide no learning signal.
- **Track reward distributions and KL** every step to catch objective drift early.
- **The reference trainer uses `--forward-only`** — never call `optim_step` on it.
- **Sampling is async**: `DeploymentSampler.sample_with_tokens()` issues `n` concurrent `n=1` requests; wrap with `asyncio.run(...)`.
- **DCP checkpoints disabled by default** (`dcp_save_interval=0`). Set to a positive value to enable resume.

## Common pitfalls

- **Reward normalization bugs** destabilize GRPO updates quickly — verify advantage computation.
- **Reference/policy tokenizer mismatch** invalidates KL estimates — use the same `base_model`.
- **Logprob alignment**: Trainer returns N-1 logprobs for N tokens; inference returns N logprobs where the first is `None`. Use `inference[1:]` to align.

<!--THE END-->