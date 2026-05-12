---
title: 'Cookbook: DPO - Fireworks AI Docs
url: https://docs.fireworks.ai/fine-tuning/training-api/cookbook/dpo
source: sitemap
fetched_at: 2026-04-27T20:15:14.354035867-03:00
rendered_js: false
word_count: 338
summary: This guide explains Direct Preference Optimization (DPO) training, detailing how it learns preferences from chosen vs. rejected pairs without a separate reward model. It provides architectural context, configuration recipes, dataset formats, and step-by-step implementation examples for using DPO via an API.
tags:
    - dpo
    - direct-preference-optimization
    - rl-training
    - policy-gradient
    - cookbook
    - preference-tuning
category: guide
optimized: true
optimized_at: 2026-04-27T00:00:00Z
---
# Cookbook: DPO

Direct Preference Optimization (DPO) learns from preference pairs (chosen vs. rejected responses) without a separate reward model.

## How DPO differs from GRPO

| Aspect | DPO | GRPO |
|--------|-----|------|
| **Trainer jobs** | 2 (policy + frozen reference) | 2 (policy + frozen reference) |
| **Data** | Preference pairs (chosen/rejected) | Prompts + reward function |
| **Reference logprobs** | Cached once at initialization | Computed every step |
| **Loss** | `-log(sigmoid(beta * margin))` | Advantage-weighted policy gradient + KL |

## Using the recipe

```python
from training.recipes.dpo_loop import Config, main
from training.utils import DeployConfig, InfraConfig, WandBConfig

cfg = Config(
    log_path="./dpo_logs",
    base_model="accounts/fireworks/models/qwen3-8b",
    dataset="/path/to/preference_data.jsonl",
    tokenizer_model="Qwen/Qwen3-8B",
    beta=0.1,
    epochs=1,
    batch_size=4,
    max_seq_len=4096,
    infra=InfraConfig(
        training_shape_id="accounts/fireworks/trainingShapes/qwen3-8b-128k-h200",
        ref_training_shape_id="accounts/fireworks/trainingShapes/qwen3-8b-128k-h200-forward",
    ),
    deployment=DeployConfig(
        deployment_id="dpo-serving",
    ),
    wandb=WandBConfig(entity="my-team", project="dpo-experiment"),
)

main(cfg)
```

## Dataset format

DPO expects preference pairs. Supported formats:

### Format 1 — chosen/rejected messages

```json
{
  "chosen": {"messages": [{"role": "user", "content": "..."}, {"role": "assistant", "content": "good response"}]},
  "rejected": {"messages": [{"role": "user", "content": "..."}, {"role": "assistant", "content": "bad response"}]}
}
```

### Format 2 — input/output split

```json
{
  "input": {"messages": [{"role": "user", "content": "..."}]},
  "preferred_output": [{"role": "assistant", "content": "good"}],
  "non_preferred_output": [{"role": "assistant", "content": "bad"}]
}
```

## Step-by-step (API-level)

### 1. Provision trainers with `setup_infra`

DPO needs both a policy trainer and a forward-only reference trainer. `training.utils.rl.setup_infra` handles shape resolution, parallel provisioning of both trainers, and the LoRA shared-reference shortcut (when `lora_rank > 0`, no separate reference trainer is needed).

```python
import os
from fireworks.training.sdk import TrainerJobManager, DeploymentManager
from training.utils import InfraConfig, ResourceCleanup
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

with ResourceCleanup(rlor_mgr) as cleanup:
    infra = setup_infra(
        rlor_mgr=rlor_mgr,
        deploy_mgr=None,
        base_model=base_model,
        infra_cfg=infra_cfg,
        lora_rank=0,
        needs_reference=True,    # DPO always needs reference
        needs_inference=False,   # no rollouts in DPO
        role_prefix="dpo",
        api_key=api_key,
        cleanup=cleanup,
    )

policy_client = infra.policy
reference_client = infra.reference
```

### 2. Cache reference logprobs

Reference logprobs are computed once at initialization and reused throughout training:

```python
ref_cache = {}
for i, (chosen_tokens, rejected_tokens, prompt_len) in enumerate(dataset):
    chosen_datum, rejected_datum = build_dpo_datums(
        chosen_tokens, rejected_tokens, prompt_len, max_seq_len=4096,
    )
    fwd = reference_client.forward([chosen_datum, rejected_datum], "cross_entropy")
    ref_cache[i] = {
        "ref_chosen": fwd.loss_fn_outputs[0]["logprobs"].data,
        "ref_rejected": fwd.loss_fn_outputs[1]["logprobs"].data,
        "chosen_tokens": chosen_tokens,
        "rejected_tokens": rejected_tokens,
        "prompt_len": prompt_len,
    }
```

### 3. DPO loss function

```python
import torch
import torch.nn.functional as F

def make_dpo_loss_fn(ref_chosen_logprobs, ref_rejected_logprobs, beta=0.1):
    ref_chosen_t = torch.tensor(ref_chosen_logprobs, dtype=torch.float32)
    ref_rejected_t = torch.tensor(ref_rejected_logprobs, dtype=torch.float32)

    def loss_fn(data, logprobs_list):
        pi_chosen, pi_rejected = logprobs_list[0], logprobs_list[1]
        chosen_weights = torch.tensor(data[0].loss_fn_inputs["weights"].data, dtype=torch.float32)
        rejected_weights = torch.tensor(data[1].loss_fn_inputs["weights"].data, dtype=torch.float32)

        pi_chosen_sum = torch.dot(pi_chosen.float(), chosen_weights)
        pi_rejected_sum = torch.dot(pi_rejected.float(), rejected_weights)
        ref_chosen_sum = torch.dot(ref_chosen_t.float(), chosen_weights)
        ref_rejected_sum = torch.dot(ref_rejected_t.float(), rejected_weights)

        margin = (pi_chosen_sum - ref_chosen_sum) - (pi_rejected_sum - ref_rejected_sum)
        dpo_loss = -F.logsigmoid(beta * margin)

        with torch.no_grad():
            accuracy = 1.0 if margin.item() > 0 else 0.0

        return dpo_loss, {"dpo_loss": dpo_loss.item(), "margin": margin.item(), "accuracy": accuracy}

    return loss_fn
```

### 4. Training loop

```python
step = 0
accum_count = 0
grad_accum = 4

for idx in ref_cache:
    cached = ref_cache[idx]
    chosen_datum, rejected_datum = build_dpo_datums(
        cached["chosen_tokens"], cached["rejected_tokens"],
        cached["prompt_len"], max_seq_len=4096,
    )
    loss_fn = make_dpo_loss_fn(
        ref_chosen_logprobs=cached["ref_chosen"],
        ref_rejected_logprobs=cached["ref_rejected"],
        beta=0.1,
    )
    result = policy_client.forward_backward_custom([chosen_datum, rejected_datum], loss_fn)
    accum_count += 1

    if accum_count >= grad_accum:
        policy_client.optim_step(
            tinker.AdamParams(learning_rate=1e-5, beta1=0.9, beta2=0.999, eps=1e-8, weight_decay=0.01)
        )
        step += 1
        accum_count = 0
        print(f"Step {step}: {result.metrics}")
```

## Operational guidance

- **Set `infra.training_shape_id` and `infra.ref_training_shape_id`** — DPO launches both a policy trainer and a reference trainer
- **DPO uses 2 RLOR jobs** — policy trainer + frozen reference trainer
- **DPO defaults `weight_sync_interval=0`** (no weight sync by default), unlike GRPO
- **Keep a versioned reference cache** tied to tokenizer + base model revision. If the base model changes, recompute reference logprobs
- **Monitor margin statistics** — increasing margins indicate the policy is learning preferences
- **DCP checkpoints are disabled by default** (`dcp_save_interval=0`). If you need to resume, explicitly set `dcp_save_interval` to a positive value in `WeightSyncConfig`

## Common pitfalls

- **Mismatched formatting** between chosen/rejected sequences corrupts preference signals — ensure identical prompt prefixes
- **Stale reference cache**: If you warm-start from a different model, cached reference logprobs are invalid

## Related

- [[051-fine-tuning-training-api-cookbook-rl|Cookbook RL (GRPO)]] — reinforcement learning recipes
- [[054-fine-tuning-training-api-loss-functions|Loss Functions]] — API-level DPO loss details

#dpo #direct-preference-optimization #rl-training #policy-gradient #cookbook #preference-tuning
