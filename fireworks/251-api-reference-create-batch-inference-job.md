---
title: Create Batch Inference Job
optimized: true
optimized_at: 2026-04-27T00:00:00Z
word_count: 295
---
> [!info] Auth: Bearer token required. Format: `Bearer <API_KEY>`

## Request

### Query Parameters

| Param | Type | Description |
|---|---|---|
| `id` | string | ID of the batch inference job. |

### Body

| Param | Type | Default | Description |
|---|---|---|---|
| `model` | string | — | Model name for inference. Required unless `continued_from_job_name` is specified. |
| `dataset` | string | — | Dataset name for inference. Required unless `continued_from_job_name` is specified. |
| `resultsDataset` | string | — | Dataset name for storing results (includes error file). |
| `inferenceParameters` | object | — | Parameters controlling the inference process. |
| `precision` | enum | `PRECISION_UNSPECIFIED` | Serving precision. Default chosen based on model. |
| `continued_from_job_name` | string | — | Continuation job ID for lineage tracking. |

### Precision Options

`PRECISION_UNSPECIFIED`, `FP16`, `FP8`, `FP8_MM`, `FP8_AR`, `FP8_MM_KV_ATTN`, `FP8_KV`, `FP8_MM_V2`, `FP8_V2`, `FP8_MM_KV_ATTN_V2`, `NF4`, `FP4`, `BF16`, `FP4_BLOCKSCALED_MM`, `FP4_MX_MOE`

## Response

| Field | Type | Description |
|---|---|---|
| `createTime` | string (date-time) | Job creation time. |
| `email` | string | User who initiated the job. |
| `state` | enum | Job state. Default: `JOB_STATE_UNSPECIFIED`. |
| `status` | object | Mirrors [google/rpc/status.proto](https://github.com/googleapis/googleapis/blob/master/google/rpc/status.proto). |
| `model` | string | Model name for inference. |
| `dataset` | string | Dataset name for inference. |
| `resultsDataset` | string | Results dataset name. |
| `inferenceParameters` | object | Inference process parameters. |
| `updateTime` | string (date-time) | Last update time. |
| `precision` | enum | Serving precision. |
| `continued_from_job_name` | string | Continuation job for lineage tracking. |

### Job State Options

`JOB_STATE_UNSPECIFIED`, `JOB_STATE_CREATING`, `JOB_STATE_RUNNING`, `JOB_STATE_COMPLETED`, `JOB_STATE_FAILED`, `JOB_STATE_CANCELLED`, `JOB_STATE_DELETING`, `JOB_STATE_WRITING_RESULTS`, `JOB_STATE_VALIDATING`, `JOB_STATE_DELETING_CLEANING_UP`, `JOB_STATE_PENDING`, `JOB_STATE_EXPIRED`, `JOB_STATE_RE_QUEUEING`, `JOB_STATE_CREATING_INPUT_DATASET`, `JOB_STATE_IDLE`, `JOB_STATE_CANCELLING`, `JOB_STATE_EARLY_STOPPED`, `JOB_STATE_PAUSED`, `JOB_STATE_DELETED`
