---
title: Resume Dpo Job
url: https://docs.fireworks.ai/api-reference/resume-dpo-job
source: sitemap
fetched_at: 2026-04-27T20:13:50.697109804-03:00
rendered_js: false
word_count: 445
summary: This document provides a detailed JSON structure representing the configuration and status of a training job, detailing aspects like model setup, hyperparameter tuning, logging integration, and storage configurations.
tags:
    - job-status
    - training-config
    - hyperparameters
    - aws-s3
    - azure-blob
    - model-training
category: reference
optimized: true
optimized_at: 2026-04-27T00:00:00Z
---
# Resume Dpo Job

JSON schema for resuming a DPO (Direct Preference Optimization) training job.

```json
{
  "dataset": "<string>",
  "name": "<string>",
  "displayName": "<string>",
  "createTime": "2023-11-07T05:31:56Z",
  "completedTime": "2023-11-07T05:31:56Z",
  "state": "JOB_STATE_UNSPECIFIED",
  "status": {
    "code": "OK",
    "message": "<string>"
  },
  "createdBy": "<string>",
  "trainingConfig": {
    "outputModel": "<string>",
    "baseModel": "<string>",
    "warmStartFrom": "<string>",
    "jinjaTemplate": "<string>",
    "learningRate": 123,
    "maxContextLength": 123,
    "loraRank": 123,
    "epochs": 123,
    "batchSize": 123,
    "gradientAccumulationSteps": 123,
    "learningRateWarmupSteps": 123,
    "batchSizeSamples": 123,
    "optimizerWeightDecay": 123,
    "trainerShardingScheme": {
      "tensorParallelism": 123,
      "pipelineParallelism": 123,
      "contextParallelism": 123,
      "expertParallelism": 123,
      "sequenceParallelism": true
    },
    "loraAlpha": 123,
    "loraDropout": 123,
    "loraTargetModules": [
      "<string>"
    ]
  },
  "wandbConfig": {
    "enabled": true,
    "apiKey": "<string>",
    "project": "<string>",
    "entity": "<string>",
    "runId": "<string>",
    "url": "<string>"
  },
  "trainerLogsSignedUrl": "<string>",
  "lossConfig": {
    "method": "METHOD_UNSPECIFIED",
    "klBeta": 123,
    "dpo": {
      "beta": 123,
      "refCacheConcurrency": 123,
      "refCacheBatchSize": 123
    },
    "orpo": {
      "lambda": 123
    }
  },
  "awsS3Config": {
    "credentialsSecret": "<string>",
    "iamRoleArn": "<string>"
  },
  "azureBlobStorageConfig": {
    "credentialsSecret": "<string>",
    "managedIdentityClientId": "<string>",
    "tenantId": "<string>"
  },
  "purpose": "PURPOSE_UNSPECIFIED"
}
```

## Schema Fields

### Core Fields

| Field | Type | Description |
|-------|------|-------------|
| `dataset` | string | Dataset for training. |
| `name` | string | Job name. |
| `displayName` | string | Display name. |
| `createTime` | string (ISO 8601) | Creation timestamp. |
| `completedTime` | string (ISO 8601) | Completion timestamp. |
| `state` | string | Job state enum. |
| `status` | object | Status with `code` and `message`. |
| `createdBy` | string | Creator identifier. |

### Training Configuration

| Field | Type | Description |
|-------|------|-------------|
| `outputModel` | string | Output model name. |
| `baseModel` | string | Base model name. |
| `warmStartFrom` | string | Checkpoint to warm start from. |
| `jinjaTemplate` | string | Jinja template for formatting. |
| `learningRate` | number | Learning rate. |
| `maxContextLength` | integer | Maximum context length. |
| `loraRank` | integer | LoRA rank. |
| `epochs` | integer | Number of epochs. |
| `batchSize` | integer | Batch size. |
| `gradientAccumulationSteps` | integer | Gradient accumulation steps. |
| `learningRateWarmupSteps` | integer | Warmup steps. |
| `batchSizeSamples` | integer | Samples per batch. |
| `optimizerWeightDecay` | number | Weight decay. |
| `trainerShardingScheme` | object | Parallelism settings. |
| `loraAlpha` | integer | LoRA alpha. |
| `loraDropout` | number | LoRA dropout. |
| `loraTargetModules` | array[string] | Target modules for LoRA. |

### Logging

| Field | Type | Description |
|-------|------|-------------|
| `wandbConfig` | object | Weights & Biases configuration. |
| `trainerLogsSignedUrl` | string | Signed URL for trainer logs. |

### Loss Configuration

| Field | Type | Description |
|-------|------|-------------|
| `lossConfig.method` | string | Loss method enum. |
| `lossConfig.klBeta` | number | KL beta. |
| `lossConfig.dpo.beta` | number | DPO beta. |
| `lossConfig.dpo.refCacheConcurrency` | integer | Reference cache concurrency. |
| `lossConfig.dpo.refCacheBatchSize` | integer | Reference cache batch size. |
| `lossConfig.orpo.lambda` | number | ORPO lambda. |

### Storage

| Field | Type | Description |
|-------|------|-------------|
| `awsS3Config` | object | AWS S3 configuration with `credentialsSecret` and `iamRoleArn`. |
| `azureBlobStorageConfig` | object | Azure Blob configuration. |

### Trainer Sharding Scheme

| Field | Type | Description |
|-------|------|-------------|
| `tensorParallelism` | integer | Tensor parallelism degree. |
| `pipelineParallelism` | integer | Pipeline parallelism degree. |
| `contextParallelism` | integer | Context parallelism degree. |
| `expertParallelism` | integer | Expert parallelism degree. |
| `sequenceParallelism` | boolean | Enable sequence parallelism. |
