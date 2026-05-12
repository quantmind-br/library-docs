---
title: Cleanup and Teardown - Fireworks AI Docs
url: https://docs.fireworks.ai/fine-tuning/training-api/reference/cleanup
source: sitemap
fetched_at: 2026-04-27T20:15:57.148466242-03:00
rendered_js: false
word_count: 194
summary: This document provides operational guidance on how to manage and clean up GPU resources utilized by RLOR trainer jobs and deployments, offering methods for manual deletion, scaling down to zero, and automatic cleanup via a context manager.
tags:
    - rlor-training
    - resource-cleanup
    - gpu-management
    - job-deletion
    - deployment-scaling
    - fireworks-ai
category: guide
optimized: true
optimized_at: 2026-04-27T00:00:00Z
---
RLOR trainer jobs and hotload-enabled deployments hold GPU resources. Always clean up after experiments — especially if jobs terminate unexpectedly.

## Cleaning Up RLOR Trainer Jobs

```python
import os
from fireworks.training.sdk import TrainerJobManager, DeploymentManager

api_key = os.environ["FIREWORKS_API_KEY"]
base_url = os.environ.get("FIREWORKS_BASE_URL", "https://api.fireworks.ai")

rlor_mgr = TrainerJobManager(api_key=api_key, base_url=base_url)
deploy_mgr = DeploymentManager(api_key=api_key, base_url=base_url)

# Delete known trainer jobs from this run
for job_id in ["<policy-job-id>", "<reference-job-id>"]:
    rlor_mgr.delete(job_id=job_id)
```

## Cleaning Up Deployments

```python
deploy_mgr.delete(deployment_id="<deployment-id>")
```

To release GPUs while keeping the deployment available for future scale-up:

```python
deploy_mgr.scale_to_zero(deployment_id="<deployment-id>")
```

This sets both `minReplicaCount` and `maxReplicaCount` to `0`.

## Automatic Cleanup with ResourceCleanup

The cookbook provides `ResourceCleanup`, a context manager that automatically deletes registered trainers and deployments on scope exit — including on exceptions and Ctrl+C:

```python
from training.utils.infra import ResourceCleanup

with ResourceCleanup(rlor_mgr, deploy_mgr) as cleanup:
    # Create trainer first (trainer owns the hot-load bucket)
    endpoint = rlor_mgr.create_and_wait(config)
    cleanup.trainer(endpoint.job_id)

    # Create deployment linked to the trainer's bucket
    deploy_config.hot_load_trainer_job = endpoint.job_name
    deploy_mgr.create_or_get(deploy_config)
    cleanup.deployment("research-loop-serving")

    run_training_loop()
```

Resources are deleted in reverse creation order. Deployments can be scaled to zero instead of deleted:

```python
cleanup.deployment("research-loop-serving", action="scale_to_zero")
```

## Manual Cleanup with try/finally

```python
policy_job_id = "<policy-job-id>"
reference_job_id = "<reference-job-id>"
deployment_id = "research-loop-serving"

try:
    run_training_loop()
finally:
    rlor_mgr.delete(policy_job_id)
    rlor_mgr.delete(reference_job_id)
    deploy_mgr.delete(deployment_id)
```

## Checking for Leaked Resources

Track the IDs you create (trainer job IDs + deployment ID) and clean those explicitly. For broad account-wide discovery, use the Fireworks console or the managed `fw.*.list()` APIs.

## Operational Guidance

- **Delete both policy and reference trainers** when running GRPO (uses 2 RLOR jobs).
- **Register cleanup on `atexit`** in your training scripts for automatic cleanup on Ctrl+C or exceptions.
- **Don't delete a trainer** while a `save_weights_for_sampler_ext` operation is in progress — wait for it to complete first.

## See Also

- [[056-fine-tuning-training-api-reference-deployment-manager|TrainerJobManager]]
- [[056-fine-tuning-training-api-reference-deployment-manager|DeploymentManager]]

#rlor-training #resource-cleanup #gpu-management #job-deletion
