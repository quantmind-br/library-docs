---
title: Create Evaluation Job - Fireworks AI Docs
url: https://docs.fireworks.ai/api-reference/create-evaluation-job
source: sitemap
fetched_at: 2026-04-27T20:14:57.890965323-03:00
rendered_js: false
word_count: 202
summary: This document details various aspects of a Fireworks API resource, including required bearer token authorization, supported path parameters, and several fields describing the state and metadata of an asynchronous evaluation job.
tags:
    - api-authentication
    - job-status
    - resource-name
    - bearer-token
    - evaluation-job
    - dataset-metadata
category: reference
optimized: true
optimized_at: 2026-04-27T00:00:00Z
---
# Create Evaluation Job

## Authorization

Bearer authentication using your Fireworks API key.

Format: `Bearer <API_KEY>`

## Path Parameters

None.

## Request Body

None.

## Response Fields

| Field | Type | Description |
|-------|------|-------------|
| `evaluator` | string | Fully-qualified resource name of the Evaluation used by this job. Format: `accounts/{account_id}/evaluators/{evaluator_id}` |
| `input_dataset` | string | Fully-qualified resource name of the input Dataset used by this job. Format: `accounts/{account_id}/datasets/{dataset_id}` |
| `output_dataset` | string | Fully-qualified resource name of the output Dataset created by this job. Format: `accounts/{account_id}/datasets/{output_dataset_id}` |
| `createTime` | string (date-time) | Creation time (read-only). |
| `state` | enum (string) | Current job state. Default: `JOB_STATE_UNSPECIFIED` (read-only). |
| `status` | object | Mimics [google.rpc.Status](https://github.com/googleapis/googleapis/blob/master/google/rpc/status.proto) (read-only). |
| `aws_config` | object | AWS configuration for S3 dataset access. |
| `updateTime` | string (date-time) | Last update time (read-only). |

## JobState Enum Values

- `JOB_STATE_UNSPECIFIED`
- `JOB_STATE_CREATING`
- `JOB_STATE_RUNNING`
- `JOB_STATE_COMPLETED`
- `JOB_STATE_FAILED`
- `JOB_STATE_CANCELLED`
- `JOB_STATE_DELETING`
- `JOB_STATE_WRITING_RESULTS`
- `JOB_STATE_VALIDATING`
- `JOB_STATE_DELETING_CLEANING_UP`
- `JOB_STATE_PENDING`
- `JOB_STATE_EXPIRED`
- `JOB_STATE_RE_QUEUEING`
- `JOB_STATE_CREATING_INPUT_DATASET`
- `JOB_STATE_IDLE`
- `JOB_STATE_CANCELLING`
- `JOB_STATE_EARLY_STOPPED`
- `JOB_STATE_PAUSED` — Job paused, typically due to account suspension or manual intervention.
- `JOB_STATE_DELETED`

#api-reference #evaluation-job #job-status