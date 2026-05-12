---
title: Create Reinforcement Fine-tuning Job - Fireworks AI Docs
url: https://docs.fireworks.ai/api-reference/create-reinforcement-fine-tuning-job
source: sitemap
fetched_at: 2026-04-27T20:14:52.298142438-03:00
rendered_js: false
optimized: true
optimized_at: 2026-04-27T00:00:00Z
tags:
    - reinforcement-fine-tuning
    - job-creation
    - api-parameters
    - training-config
    - rlor
    - job-status
category: reference
word_count: 542
---
Creates a reinforcement fine-tuning job via `POST /v1/accounts/{account_id}/reinforcementFineTuningJobs`.

## Authorization

Bearer authentication using your Fireworks API key. Format: `Bearer <API_KEY>`

## Query Parameters

| Parameter | Type | Description |
|-----------|------|-------------|
| `reinforcementFineTuningJobId` | string | ID of the job; a random UUID is generated if not specified |

## Request Body

| Field | Type | Description |
|-------|------|-------------|
| `dataset` | string | Name of the dataset used for training |
| `evaluator` | string | Evaluator resource name for RLOR fine-tuning |
| `evalDataset` | string | Name of a separate dataset to use for evaluation |
| `autoCarveEval` | boolean | Whether to auto-carve the dataset for eval |
| `trainingConfig` | object | Common training configurations shared across job types |
| `wandbTeam` | string | Weights & Biases team/user account for logging |
| `awsConfig` | object | AWS configuration for S3 dataset access |
| `azureConfig` | object | Azure configuration for Blob Storage dataset access |
| `inferenceParameters` | object | RFT inference parameters |
| `chunkSize` | integer | Data chunking for rollout; default 200, enabled when dataset > 300; valid range 1–10,000 |
| `nodeCount` | integer | Number of nodes for the fine-tuning job; default 1 |
| `rlConfig` | object | Reinforcement learning loss method + hyperparameters |
| `maxConcurrentRollouts` | integer | Maximum concurrent rollouts during the RFT job |
| `maxConcurrentEvals` | integer | Maximum concurrent evaluations during the RFT job |
| `purpose` | enum | Scheduling purpose: `PURPOSE_UNSPECIFIED`, `PURPOSE_PILOT` (default `PURPOSE_UNSPECIFIED`) |

## Response

| Field | Type | Description |
|-------|------|-------------|
| `dataset` | string | Training dataset name |
| `evaluator` | string | Evaluator resource name |
| `createTime` | string (date-time) | Creation time (read-only) |
| `completedTime` | string (date-time) | Completion time (read-only) |
| `evalDataset` | string | Evaluation dataset name |
| `autoCarveEval` | boolean | Whether auto-carve was applied |
| `state` | enum | Job state (read-only): `JOB_STATE_UNSPECIFIED`, `JOB_STATE_CREATING`, `JOB_STATE_RUNNING`, `JOB_STATE_COMPLETED`, `JOB_STATE_FAILED`, `JOB_STATE_CANCELLED`, `JOB_STATE_DELETING`, `JOB_STATE_WRITING_RESULTS`, `JOB_STATE_VALIDATING`, `JOB_STATE_DELETING_CLEANING_UP`, `JOB_STATE_PENDING`, `JOB_STATE_EXPIRED`, `JOB_STATE_RE_QUEUEING`, `JOB_STATE_CREATING_INPUT_DATASET`, `JOB_STATE_IDLE`, `JOB_STATE_CANCELLING`, `JOB_STATE_EARLY_STOPPED`, `JOB_STATE_PAUSED`, `JOB_STATE_DELETED` |
| `status` | object | RPC status per [google/rpc/status.proto](https://github.com/googleapis/googleapis/blob/master/google/rpc/status.proto) (read-only) |
| `createdByEmail` | string | Email of the user who initiated the job (read-only) |
| `trainingConfig` | object | Common training configurations |
| `wandbTeam` | string | Weights & Biases team/user account |
| `awsConfig` | object | AWS configuration for S3 |
| `azureConfig` | object | Azure configuration for Blob Storage |
| `evalMetrics` | object | Aggregated stats from the output dataset evaluation |
| `inferenceParameters` | object | RFT inference parameters |
| `chunkSize` | integer | Data chunking size for rollout |
| `nodeCount` | integer | Number of nodes |
| `rlConfig` | object | Reinforcement learning loss + hyperparameters |
| `trainerLogsFile` | string | Signed URL for trainer logs (stdout/stderr); only populated if account has trainer log reading enabled |
| `acceleratorSecondsUsed` | object | Accelerator seconds used, keyed by accelerator type (e.g. `NVIDIA_H100_80GB`); updated when job completes or is cancelled |
| `maxConcurrentRollouts` | integer | Maximum concurrent rollouts |
| `maxConcurrentEvals` | integer | Maximum concurrent evaluations |
| `purpose` | enum | Scheduling purpose |
