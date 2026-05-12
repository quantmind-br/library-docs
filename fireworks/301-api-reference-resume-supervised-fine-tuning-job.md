---
title: Resume Supervised Fine-tuning Job
url: https://docs.fireworks.ai/api-reference/resume-supervised-fine-tuning-job
source: sitemap
fetched_at: 2026-04-27T20:13:43.732305193-03:00
rendered_js: false
word_count: 538
summary: This document provides a detailed JSON structure representing the metadata of a machine learning training job. It outlines various configuration parameters related to data sources, model settings, performance tracking, and resource allocation.
tags:
    - job-configuration
    - ml-metadata
    - training-run
    - aws-s3
    - azure-blob
    - model-params
category: reference
optimized: true
optimized_at: 2026-04-27T00:00:00Z
---
# Resume Supervised Fine-tuning Job

JSON schema for resuming a supervised fine-tuning (SFT) training job.

```json
{
  "dataset": "<string>",
  "name": "<string>",
  "displayName": "<string>",
  "createTime": "2023-11-07T05:31:56Z",
  "completedTime": "2023-11-07T05:31:56Z",
  "awsS3Config": {
    "credentialsSecret": "<string>",
    "iamRoleArn": "<string>"
  },
  "azureBlobStorageConfig": {
    "credentialsSecret": "<string>",
    "managedIdentityClientId": "<string>",
    "tenantId": "<string>"
  },
  "state": "JOB_STATE_UNSPECIFIED",
  "status": {
    "code": "OK",
    "message": "<string>"
  },
  "createdBy": "<string>",
  "outputModel": "<string>",
  "baseModel": "<string>",
  "warmStartFrom": "<string>",
  "jinjaTemplate": "<string>",
  "earlyStop": true,
  "epochs": 123,
  "learningRate": 123,
  "maxContextLength": 123,
  "loraRank": 123,
  "wandbConfig": {
    "enabled": true,
    "apiKey": "<string>",
    "project": "<string>",
    "entity": "<string>",
    "runId": "<string>",
    "url": "<string>"
  },
  "evaluationDataset": "<string>",
  "isTurbo": true,
  "evalAutoCarveout": true,
  "updateTime": "2023-11-07T05:31:56Z",
  "nodes": 123,
  "batchSize": 123,
  "mtpEnabled": true,
  "mtpNumDraftTokens": 123,
  "mtpFreezeBaseModel": true,
  "jobProgress": {
    "percent": 123,
    "epoch": 123,
    "totalInputRequests": 123,
    "totalProcessedRequests": 123,
    "successfullyProcessedRequests": 123,
    "failedRequests": 123,
    "outputRows": 123,
    "inputTokens": 123,
    "outputTokens": 123,
    "cachedInputTokenCount": 123
  },
  "metricsFileSignedUrl": "<string>",
  "trainerLogsSignedUrl": "<string>",
  "gradientAccumulationSteps": 123,
  "learningRateWarmupSteps": 123,
  "batchSizeSamples": 123,
  "estimatedCost": {
    "currencyCode": "<string>",
    "units": "<string>",
    "nanos": 123
  },
  "optimizerWeightDecay": 123,
  "purpose": "PURPOSE_UNSPECIFIED"
}
```

## Schema Fields

### Core Fields

| Field | Type | Description |
|-------|------|-------------|
| `dataset` | string | Training dataset. |
| `name` | string | Job name. |
| `displayName` | string | Display name. |
| `createTime` | string (ISO 8601) | Creation timestamp. |
| `completedTime` | string (ISO 8601) | Completion timestamp. |
| `updateTime` | string (ISO 8601) | Last update timestamp. |
| `state` | string | Job state enum. |
| `status` | object | Status with `code` and `message`. |
| `createdBy` | string | Creator identifier. |

### Model Configuration

| Field | Type | Description |
|-------|------|-------------|
| `outputModel` | string | Output model name. |
| `baseModel` | string | Base model name. |
| `warmStartFrom` | string | Checkpoint to warm start from. |
| `jinjaTemplate` | string | Jinja template for formatting. |
| `earlyStop` | boolean | Enable early stopping. |
| `isTurbo` | boolean | Turbo mode enabled. |

### Hyperparameters

| Field | Type | Description |
|-------|------|-------------|
| `epochs` | integer | Number of epochs. |
| `learningRate` | number | Learning rate. |
| `maxContextLength` | integer | Maximum context length. |
| `loraRank` | integer | LoRA rank. |
| `batchSize` | integer | Batch size. |
| `gradientAccumulationSteps` | integer | Gradient accumulation steps. |
| `learningRateWarmupSteps` | integer | Warmup steps. |
| `batchSizeSamples` | integer | Samples per batch. |
| `optimizerWeightDecay` | number | Weight decay. |

### Miscoded Target Prediction (MTP)

| Field | Type | Description |
|-------|------|-------------|
| `mtpEnabled` | boolean | MTP enabled. |
| `mtpNumDraftTokens` | integer | Number of draft tokens. |
| `mtpFreezeBaseModel` | boolean | Freeze base model during MTP. |

### Datasets

| Field | Type | Description |
|-------|------|-------------|
| `evaluationDataset` | string | Evaluation dataset. |
| `evalAutoCarveout` | boolean | Auto carveout for evaluation. |

### Progress Tracking

| Field | Type | Description |
|-------|------|-------------|
| `jobProgress.percent` | number | Completion percentage. |
| `jobProgress.epoch` | integer | Current epoch. |
| `jobProgress.totalInputRequests` | integer | Total input requests. |
| `jobProgress.totalProcessedRequests` | integer | Total processed requests. |
| `jobProgress.successfullyProcessedRequests` | integer | Successful requests. |
| `jobProgress.failedRequests` | integer | Failed requests. |
| `jobProgress.outputRows` | integer | Output rows generated. |
| `jobProgress.inputTokens` | integer | Input tokens processed. |
| `jobProgress.outputTokens` | integer | Output tokens generated. |
| `jobProgress.cachedInputTokenCount` | integer | Cached input tokens. |

### Infrastructure

| Field | Type | Description |
|-------|------|-------------|
| `nodes` | integer | Number of nodes. |
| `metricsFileSignedUrl` | string | Signed URL for metrics file. |
| `trainerLogsSignedUrl` | string | Signed URL for trainer logs. |
| `estimatedCost` | object | Estimated cost with `currencyCode`, `units`, `nanos`. |

### Logging

| Field | Type | Description |
|-------|------|-------------|
| `wandbConfig` | object | Weights & Biases configuration. |

### Storage

| Field | Type | Description |
|-------|------|-------------|
| `awsS3Config` | object | AWS S3 configuration with `credentialsSecret` and `iamRoleArn`. |
| `azureBlobStorageConfig` | object | Azure Blob configuration. |
