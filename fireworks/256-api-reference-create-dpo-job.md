---
title: Create dpo job
optimized: true
optimized_at: 2026-04-27T00:00:00Z
word_count: 419
---
> [!info] Auth: Bearer token required. Format: `Bearer <API_KEY>`

## Request

### Query Parameters

| Param | Type | Description |
|---|---|---|
| `id` | string | DPO job ID. Random ID generated if not specified. |

### Body

| Field | Type | Description |
|---|---|---|
| `dataset` | string | Dataset name used for training. |
| `trainingConfig` | object | BaseTrainingConfig: common configuration shared across training job types. |
| `wandbConfig` | object | Weights & Biases team/user account for logging job progress. |
| `lossConfig` | object | Loss configuration. Defaults to DPO loss. Set `method` to `ORPO` for ORPO training. |
| `awsS3Config` | object | AWS configuration for S3 dataset access. |
| `azureBlobStorageConfig` | object | Azure configuration for Azure Blob Storage dataset access. |
| `purpose` | enum | Scheduling purpose. Default: `PURPOSE_UNSPECIFIED`. Options: `PURPOSE_UNSPECIFIED`, `PURPOSE_PILOT`. |

## Response

| Field | Type | Description |
|---|---|---|
| `dataset` | string | Dataset name used for training. |
| `createTime` | string (date-time) | read-only. Job creation time. |
| `completedTime` | string (date-time) | read-only. Completion time. |
| `state` | enum | read-only. Job state. Default: `JOB_STATE_UNSPECIFIED`. |
| `status` | object | read-only. Mirrors [google/rpc/status.proto](https://github.com/googleapis/googleapis/blob/master/google/rpc/status.proto). |
| `email` | string | User who initiated the DPO job. |
| `trainingConfig` | object | Common training configurations. |
| `wandbConfig` | object | W&B team/user account for logging progress. |
| `trainerLogsSignedUrl` | string | Signed URL for trainer logs (stdout/stderr). Populated only if account has trainer log reading enabled. |
| `lossConfig` | object | Loss configuration. Defaults to DPO loss. |
| `awsS3Config` | object | AWS configuration for S3 dataset access. |
| `azureBlobStorageConfig` | object | Azure configuration for Azure Blob Storage. |
| `purpose` | enum | Scheduling purpose. Default: `PURPOSE_UNSPECIFIED`. |

### Job State Options

| State | Description |
|---|---|
| `JOB_STATE_UNSPECIFIED` | — |
| `JOB_STATE_CREATING` | — |
| `JOB_STATE_RUNNING` | — |
| `JOB_STATE_COMPLETED` | — |
| `JOB_STATE_FAILED` | — |
| `JOB_STATE_CANCELLED` | — |
| `JOB_STATE_DELETING` | — |
| `JOB_STATE_WRITING_RESULTS` | — |
| `JOB_STATE_VALIDATING` | — |
| `JOB_STATE_DELETING_CLEANING_UP` | — |
| `JOB_STATE_PENDING` | — |
| `JOB_STATE_EXPIRED` | — |
| `JOB_STATE_RE_QUEUEING` | — |
| `JOB_STATE_CREATING_INPUT_DATASET` | — |
| `JOB_STATE_IDLE` | — |
| `JOB_STATE_CANCELLING` | — |
| `JOB_STATE_EARLY_STOPPED` | — |
| `JOB_STATE_PAUSED` | Job paused (account suspension or manual intervention). |
| `JOB_STATE_DELETED` | Job deleted. |
