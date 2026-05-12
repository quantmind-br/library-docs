---
title: Create Reinforcement Fine-tuning Step - Fireworks AI Docs
url: https://docs.fireworks.ai/api-reference/create-reinforcement-fine-tuning-step
source: sitemap
fetched_at: 2026-04-27T20:14:52.379532107-03:00
rendered_js: false
optimized: true
optimized_at: 2026-04-27T00:00:00Z
tags:
    - reinforcement-learning
    - fine-tuning
    - api-call
    - job-creation
    - training-config
    - rlor
category: reference
word_count: 557
---
Creates a reinforcement learning optimization (RLOR) fine-tuning step via `POST /v1/accounts/{account_id}/rlorTrainerJobs`.

## Authorization

Bearer authentication using your Fireworks API key. Format: `Bearer <API_KEY>`

## Query Parameters

| Parameter | Type | Description |
|-----------|------|-------------|
| `rlorTrainerJobId` | string | ID of the RLOR trainer job; a random UUID is generated if not specified |
| `trainingShapeSelector` | string | Optional validated training-shape selector for service-mode launches. Accepted formats: `accounts/{account}/trainingShapes/{shape}`, `accounts/{account}/trainingShapes/{shape}/versions/{version}`, `accounts/{account}/trainingShapes/{shape}/versions/latest` |

## Request Body

| Field | Type | Description |
|-------|------|-------------|
| `dataset` | string | Name of the dataset used for training |
| `evalDataset` | string | Name of a separate dataset to use for evaluation |
| `autoCarveEval` | boolean | Whether to auto-carve the dataset for eval |
| `trainingConfig` | object | Common training configurations shared across job types |
| `rewardMetrics` | array | List of reward metrics in format `<reward_name>=` |
| `wandbTeam` | string | Weights & Biases team/user account for logging |
| `awsConfig` | object | AWS configuration for S3 dataset access |
| `azureConfig` | object | Azure configuration for Blob Storage dataset access |
| `rolloutDeployment` | string | Rollout deployment name; optional. If not set, trainer will not trigger weight sync to rollout engine |
| `rlConfig` | object | Reinforcement learning loss method + hyperparameters for the underlying trainer |
| `nodeCount` | integer | Number of nodes; default 1 |
| `hotLoadDeployment` | string | Deployment ID for hot loading; checkpoints are saved to this deployment's hot load bucket, enabling weight swaps on inference. Only valid for service-mode or keep-alive jobs |
| `purpose` | enum | Scheduling purpose: `PURPOSE_UNSPECIFIED`, `PURPOSE_PILOT` (default `PURPOSE_UNSPECIFIED`) |
| `forwardOnlyMode` | boolean | Run the trainer in forward-only mode (no backward/optimizer). Used for reference models in GRPO |
| `reserved` | boolean | For managed service use only |

## Response

| Field | Type | Description |
|-------|------|-------------|
| `createTime` | string (date-time) | Creation time (read-only) |
| `completedTime` | string (date-time) | Completion time (read-only) |
| `dataset` | string | Training dataset name |
| `evalDataset` | string | Evaluation dataset name |
| `autoCarveEval` | boolean | Whether auto-carve was applied |
| `state` | enum | Job state (read-only): `JOB_STATE_UNSPECIFIED`, `JOB_STATE_CREATING`, `JOB_STATE_RUNNING`, `JOB_STATE_COMPLETED`, `JOB_STATE_FAILED`, `JOB_STATE_CANCELLED`, `JOB_STATE_DELETING`, `JOB_STATE_WRITING_RESULTS`, `JOB_STATE_VALIDATING`, `JOB_STATE_DELETING_CLEANING_UP`, `JOB_STATE_PENDING`, `JOB_STATE_EXPIRED`, `JOB_STATE_RE_QUEUEING`, `JOB_STATE_CREATING_INPUT_DATASET`, `JOB_STATE_IDLE`, `JOB_STATE_CANCELLING`, `JOB_STATE_EARLY_STOPPED`, `JOB_STATE_PAUSED`, `JOB_STATE_DELETED` |
| `status` | object | RPC status per [google/rpc/status.proto](https://github.com/googleapis/googleapis/blob/master/google/rpc/status.proto) (read-only) |
| `createdByEmail` | string | Email of the user who initiated the job (read-only) |
| `trainingConfig` | object | Common training configurations |
| `rewardMetrics` | array | List of reward metrics |
| `wandbTeam` | string | Weights & Biases team/user account |
| `awsConfig` | object | AWS configuration for S3 |
| `azureConfig` | object | Azure configuration for Blob Storage |
| `rolloutDeployment` | string | Rollout deployment name |
| `rlConfig` | object | Reinforcement learning loss + hyperparameters |
| `nodeCount` | integer | Number of nodes |
| `acceleratorSecondsUsed` | object | Accelerator seconds used, keyed by accelerator type (e.g. `NVIDIA_H100_80GB`); updated periodically |
| `hotLoadDeployment` | string | Deployment ID for hot loading |
| `purpose` | enum | Scheduling purpose |
| `forwardOnlyMode` | boolean | Forward-only mode |
| `reserved` | boolean | Managed service field |
