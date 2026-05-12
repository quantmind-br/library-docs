---
title: 'DeploymentManager - Fireworks AI Docs'
url: https://docs.fireworks.ai/fine-tuning/training-api/reference/deployment-manager
source: sitemap
fetched_at: 2026-04-27T20:15:41.983909887-03:00
rendered_js: false
optimized: true
optimized_at: 2026-04-27T00:00:00Z
tags:
    - deployment-manager
    - inference-lifecycle
    - hotloading
    - scaling
category: guide
word_count: 815
---
## Overview

`DeploymentManager` manages the lifecycle of inference deployments that serve as sampling and weight sync targets during training. For on-policy training (GRPO), the deployment is hotloaded with the latest policy weights.

```python
from fireworks.training.sdk import DeploymentManager, DeploymentConfig
```

## Constructor

```python
deploy_mgr = DeploymentManager(
    api_key="<FIREWORKS_API_KEY>",
    base_url="https://api.fireworks.ai",      # Control-plane URL (deployment CRUD)
    inference_url="https://api.fireworks.ai",  # Gateway URL for inference (defaults to base_url)
    hotload_api_url="https://api.fireworks.ai",# Gateway URL for hotload ops (defaults to base_url)
)
```

| Parameter | Type | Default | Description |
|---|---|---|---|
| `api_key` | `str` | — | Fireworks API key |
| `base_url` | `str` | `"https://api.fireworks.ai"` | Control-plane URL for deployment CRUD |
| `inference_url` | `str \| None` | `None` | Gateway URL for inference completions (defaults to `base_url`) |
| `hotload_api_url` | `str \| None` | `None` | Gateway URL for hotload operations (defaults to `base_url`) |
| `additional_headers` | `dict \| None` | `None` | Extra HTTP headers |
| `verify_ssl` | `bool \| None` | `None` | SSL verification override |

For most users, all three URLs default to `base_url`. Separate URLs are useful when the control-plane and gateway have different endpoints (e.g. personal dev gateways).

## Methods

### `create_or_get(config, force_recreate=False)`

Create a new deployment or retrieve an existing one. Set `force_recreate=True` to delete and recreate if it already exists:

```python
deploy_info = deploy_mgr.create_or_get(DeploymentConfig(
    deployment_id="research-loop-serving",
    base_model="accounts/fireworks/models/qwen3-8b",
    min_replica_count=0,
    max_replica_count=1,
))
```

Returns a `DeploymentInfo`.

### `wait_for_ready(deployment_id, timeout_s=600, poll_interval_s=15)`

Poll until the deployment is ready to serve:

```python
deploy_mgr.wait_for_ready("research-loop-serving")
```

Returns a `DeploymentInfo`.

### `get(deployment_id)`

Inspect deployment status. Returns a `DeploymentInfo` or `None` if not found:

```python
current = deploy_mgr.get("research-loop-serving")
print(current.state if current else "MISSING")
```

### `hotload_and_wait(deployment_id, base_model, snapshot_identity, ...)`

Load a checkpoint onto the deployment and wait for completion:

```python
deploy_mgr.hotload_and_wait(
    deployment_id="my-deployment",
    base_model="accounts/fireworks/models/qwen3-8b",
    snapshot_identity=result.snapshot_name,
    timeout_seconds=400,
)
```

For delta weight syncs, pass `incremental_snapshot_metadata`:

```python
deploy_mgr.hotload_and_wait(
    deployment_id="my-deployment",
    base_model="accounts/fireworks/models/qwen3-8b",
    snapshot_identity=delta_result.snapshot_name,
    incremental_snapshot_metadata={
        "previous_snapshot_identity": base_result.snapshot_name,
        "compression_format": "arc_v2",
        "checksum_format": "alder32",
    },
    timeout_seconds=400,
)
```

### `hotload_check_status(deployment_id, base_model, timeout=30)`

Current hotload status per replica — `current_snapshot_identity`, `readiness`, `loading_state.stage`. Use for ad-hoc inspection or to decide whether a weight sync is needed.

### `wait_for_hotload(deployment_id, base_model, expected_identity, timeout_seconds=400, poll_interval=5)`

Poll until every replica reports `readiness=true` and `current_snapshot_identity == expected_identity`. The "wait half" of `hotload_and_wait` — call directly when you kicked off a hotload via `hotload()` and want to block separately.

### `update(deployment_id, body, update_mask)`

Partial PATCH. `update_mask` is **required** (snake-case field paths); without it the server replaces all mutable fields, silently zeroing anything not in `body`. Returns `DeploymentInfo`:

```python
deploy_mgr.update("my-deployment",
    body={"minReplicaCount": 2, "maxReplicaCount": 8},
    update_mask="min_replica_count,max_replica_count")
```

### `warmup(model, max_retries=30, retry_interval_s=10.0)`

Send a warmup request to the deployment after weight sync. Retries until the deployment responds or the retry limit is reached. Returns `True` on success, `False` if all retries are exhausted.

### `scale_to_zero(deployment_id)`

Release GPU resources without deleting the deployment:

```python
deploy_mgr.scale_to_zero("research-loop-serving")
```

Sets both `minReplicaCount` and `maxReplicaCount` to `0`.

### `delete(deployment_id)`

Delete a deployment entirely:

```python
deploy_mgr.delete("research-loop-serving")
```

## DeploymentConfig

`DeploymentManager.create_or_get(...)` accepts a `DeploymentConfig` dataclass. When `deployment_shape` is set (the recommended path), the shape owns the deployment's hardware and serving configuration:

| Field | Type | Default | Description |
|---|---|---|---|
| `deployment_id` | `str` | — | Stable deployment identifier |
| `base_model` | `str` | — | Base model name. Must match the trainer's base model for weight sync compatibility. |
| `deployment_shape` | `str \| None` | `None` | Deployment shape resource name. When set, the shape owns GPU type, node count, and serving engine config. |
| `region` | `str \| None` | `None` | Region for the deployment |
| `min_replica_count` | `int` | `0` | Minimum replicas (set `0` to scale to zero when idle) |
| `max_replica_count` | `int` | `1` | Maximum replicas for autoscaling |
| `hot_load_bucket_type` | `str \| None` | `"FW_HOSTED"` | Weight sync storage backend |
| `hot_load_trainer_job` | `str \| None` | `None` | Trainer job name whose hot-load bucket this deployment should use. Format: `accounts/{account}/rlorTrainerJobs/{job_id}`. When set, the deployment shares the trainer's bucket for weight sync. |
| `disable_speculative_decoding` | `bool` | `False` | Disable speculative decoding |
| `extra_args` | `list[str] \| None` | `None` | Extra serving arguments |
| `extra_values` | `dict[str, str] \| None` | `None` | Extra deployment Helm values |

## DeploymentInfo

Returned by `create_or_get`, `wait_for_ready`, and `get`:

| Field | Type | Description |
|---|---|---|
| `deployment_id` | `str` | Deployment identifier |
| `name` | `str` | Full resource name |
| `state` | `str` | Deployment state (e.g. `"READY"`, `"CREATING"`) |
| `hot_load_bucket_url` | `str \| None` | URL for weight sync storage |
| `inference_model` | `str \| None` | Model string for completions API (`accounts/{account}/deployments/{id}`) |

## Deployment shape and training shapes

When using a training shape, the linked **deployment shape is determined by the training shape and cannot be changed**. The training shape's `deploymentShapeVersion` locks the GPU type, node count, and serving engine configuration. Only the **replica count** is user-adjustable:

```python
deploy_mgr.create_or_get(DeploymentConfig(
    deployment_id="rl-serving",
    base_model="accounts/fireworks/models/qwen3-8b",
    deployment_shape="accounts/fireworks/deploymentShapes/qwen3-8b-128k-h200",
    min_replica_count=1,
    max_replica_count=4,
))
```

## Operational guidance

- **Keep deployment IDs stable** per experiment family for easier rollbacks.
- **Use `min_replica_count=0`** for development to avoid idle GPU costs.
- **Create the trainer before the deployment** and link the deployment to the trainer's hot-load bucket via `hot_load_trainer_job`.
- **Use `deployment_shape`** when the control plane has a pre-validated shape for your model.
- **Do not treat shape-owned hardware as a user-facing override surface** — in normal flows, leave `accelerator_type` and placement decisions to the deployment shape and only tune replica counts.
- **Use `scale_to_zero`** after training as a lighter alternative to `delete`.

<!--THE END-->