---
title: Fine Tuning Full Parameter Rl Tuning
url: https://docs.fireworks.ai/fine-tuning/full-parameter-rl-tuning
source: sitemap
fetched_at: 2026-04-27T20:15:34.964491157-03:00
rendered_js: false
word_count: 147
summary: Full parameter RL tuning mode for reinforcement learning that trains all model weights while maintaining a Tinker-style loop structure, with a complete Python starter script.
tags:
    - full-parameter-rl
    - reinforcement-learning
    - tinker-loop
    - rlor-trainer
    - custom-loss
    - service-mode
category: tutorial
optimized: true
optimized_at: 2026-04-27T00:00:00Z
---
# Full Parameter RL Tuning

Full parameter RL tuning updates all model weights (`loraRank=0`) while keeping a familiar Tinker-style training loop. Current preview scope is reinforcement training via RLOR trainer jobs.

## What this unlocks

- **Custom RL objectives**: Implement GRPO, DPO, PPO, or custom reward shaping logic in Python.
- **Tinker-compatible primitives**: Use `forward()`, `forward_backward_custom()`, and `optim_step()` directly.
- **Service-mode trainers**: Run the trainer as an API service and iterate quickly from your own script.
- **Checkpoint-to-serving path**: Save checkpoints and optionally hot-load them into inference deployments.

## Workflow

1. Create serving infrastructure (inference deployment).
2. Create the RLOR trainer job.
3. Connect with [[311-fine-tuning-training-api-reference-service-client|FiretitanServiceClient]].

## Single-file starter script

```python
#!/usr/bin/env python3
"""Single-file starter for full parameter RL tuning with Tinker."""

import os
import time
import requests
import tinker
from fireworks.client import LLM

API_BASE = "https://api.fireworks.ai/v1"
API_KEY = os.environ["FIREWORKS_API_KEY"]
ACCOUNT_ID = os.environ["FIREWORKS_ACCOUNT_ID"]
BASE_MODEL = "accounts/fireworks/models/kimi-k2-5-instruct"
DEPLOYMENT_ID = "fp-rft-serving"


def auth_headers():
    return {"Authorization": f"Bearer {API_KEY}"}


def ensure_inference_deployment() -> None:
    llm = LLM(
        model=BASE_MODEL,
        id=DEPLOYMENT_ID,
        deployment_type="on-demand",
        min_replica_count=0,
        max_replica_count=1,
    )
    llm.apply()


def create_rlor_service_job() -> str:
    payload = {
        "displayName": "fp-rft-trainer",
        "serviceMode": True,
        "hotLoadDeploymentId": DEPLOYMENT_ID,
        "trainingConfig": {
            "baseModel": BASE_MODEL,
            "loraRank": 0,
            "learningRate": 1e-5,
            "maxContextLength": 4096,
            "gradientAccumulationSteps": 4,
        },
    }
    resp = requests.post(
        f"{API_BASE}/accounts/{ACCOUNT_ID}/rlorTrainerJobs",
        headers=auth_headers(),
        json=payload,
        timeout=60,
    )
    resp.raise_for_status()
    return resp.json()["name"].split("/")[-1]


def wait_for_trainer_url(job_id: str) -> str:
    while True:
        resp = requests.get(
            f"{API_BASE}/accounts/{ACCOUNT_ID}/rlorTrainerJobs/{job_id}",
            headers=auth_headers(),
            timeout=30,
        )
        resp.raise_for_status()
        job = resp.json()
        state = job.get("state")
        trainer_url = job.get("directRouteHandle")

        if state == "JOB_STATE_RUNNING" and trainer_url:
            return trainer_url
        if state in {"JOB_STATE_FAILED", "JOB_STATE_CANCELLED", "JOB_STATE_EXPIRED"}:
            raise RuntimeError(f"trainer failed in state={state}")
        time.sleep(10)


def custom_loss_fn(data, logprobs_list):
    # Replace with your GRPO / DPO / PPO objective.
    loss = compute_custom_loss(logprobs_list)
    return loss, {"loss": float(loss.item())}


def compute_custom_loss(logprobs_list):
    raise NotImplementedError("Implement your RL loss (GRPO/DPO/PPO/custom).")


def build_training_batches():
    raise NotImplementedError("Build and return iterable batches of tinker.Datum objects.")


def main() -> None:
    ensure_inference_deployment()
    job_id = create_rlor_service_job()
    trainer_url = wait_for_trainer_url(job_id)

    from fireworks.training.sdk import FiretitanServiceClient
    service = FiretitanServiceClient(base_url=trainer_url, api_key=API_KEY)
    training_client = service.create_training_client(base_model=BASE_MODEL, lora_rank=0)

    # Build your own list of tinker.Datum batches.
    training_batches = build_training_batches()

    for step, batch in enumerate(training_batches):
        training_client.forward_backward_custom(batch, custom_loss_fn).result()
        if (step + 1) % 4 == 0:
            training_client.optim_step(tinker.AdamParams(learning_rate=1e-5)).result()

    result = training_client.save_weights_for_sampler_ext("checkpoint_step_final", checkpoint_type="base")
    print("checkpoint:", result.snapshot_name)


if __name__ == "__main__":
    main()
```

## Architecture

| Responsibility | Owner |
|---------------|-------|
| Data prep, reward/loss logic, sampling strategy, experiment tracking | You |
| Distributed trainer orchestration, service endpoint management, checkpoint persistence, deployment integration | Fireworks |

#full-parameter-rl #tinker-loop #rlor-trainer
