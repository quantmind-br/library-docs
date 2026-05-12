---
title: Resume Rlor Trainer Job
url: https://docs.fireworks.ai/api-reference/resume-reinforcement-fine-tuning-step
source: sitemap
fetched_at: 2026-04-27T20:13:34.043896169-03:00
rendered_js: false
word_count: 659
summary: This document provides a comprehensive snapshot of a training job's metadata, detailing its configuration parameters, status updates, resource allocation, and performance metrics.
tags:
    - training-job
    - configuration
    - job-status
    - hyperparameters
    - mlops
    - resource-metrics
category: reference
optimized: true
optimized_at: 2026-04-27T00:00:00Z
---
# Resume Rlor Trainer Job

JSON schema for resuming a Reinforcement Learning with Reinforcement (RLoR) trainer job.

```json
{
  "name": "<string>",
  "displayName": "<string>",
  "createTime": "2023-11-07T05:31:56Z",
  "completedTime": "2023-11-07T05:31:56Z",
  "dataset": "<string>",
  "evaluationDataset": "<string>",
  "evalAutoCarveout": true,
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
  "rewardWeights": [
    "<string>"
  ],
  "wandbConfig": {
    "enabled": true,
    "apiKey": "<string>",
    "project": "<string>",
    "entity": "<string>",
    "runId": "<string>",
    "url": "<string>"
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
  "keepAlive": true,
  "rolloutDeploymentName": "<string>",
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
  "nodeCount": 123,
  "acceleratorSeconds": {},
  "serviceMode": true,
  "directRouteHandle": "<string>",
  "hotLoadDeploymentId": "<string>",
  "purpose": "PURPOSE_UNSPECIFIED",
  "forwardOnly": true,
  "managedBy": "<string>"
}
```

## Schema Fields

### Core Fields

| Field | Type | Description |
|-------|------|-------------|
| `name` | string | Job name. |
| `displayName` | string | Display name. |
| `createTime` | string (ISO 8601) | Creation timestamp. |
| `completedTime` | string (ISO 8601) | Completion timestamp. |
| `dataset` | string | Training dataset. |
| `evaluationDataset` | string | Evaluation dataset. |
| `evalAutoCarveout` | boolean | Auto carveout for evaluation. |
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

### Reinforcement Learning

| Field | Type | Description |
|-------|------|-------------|
| `rewardWeights` | array[string] | Weights for reward signals. |
| `keepAlive` | boolean | Keep job alive for incremental training. |
| `rolloutDeploymentName` | string | Deployment for rollouts. |

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
| `nodeCount` | integer | Number of nodes. |
| `acceleratorSeconds` | object | Accelerator time metrics. |
| `serviceMode` | boolean | Service mode enabled. |
| `directRouteHandle` | string | Direct routing handle. |
| `hotLoadDeploymentId` | string | Hot-loaded deployment ID. |
| `forwardOnly` | boolean | Forward-only mode. |
| `managedBy` | string | Manager identifier. |

### Logging

| Field | Type | Description |
|-------|------|-------------|
| `wandbConfig` | object | Weights & Biases configuration. |

### Storage

| Field | Type | Description |
|-------|------|-------------|
| `awsS3Config` | object | AWS S3 configuration. |
| `azureBlobStorageConfig` | object | Azure Blob configuration. |

### Loss Configuration

| Field | Type | Description |
|-------|------|-------------|
| `lossConfig.method` | string | Loss method enum. |
| `lossConfig.klBeta` | number | KL beta. |
| `lossConfig.dpo.beta` | number | DPO beta. |
| `lossConfig.dpo.refCacheConcurrency` | integer | Reference cache concurrency. |
| `lossConfig.dpo.refCacheBatchSize` | integer | Reference cache batch size. |
| `lossConfig.orpo.lambda` | number | ORPO lambda. |

### Trainer Sharding Scheme

| Field | Type | Description |
|-------|------|-------------|
| `tensorParallelism` | integer | Tensor parallelism degree. |
| `pipelineParallelism` | integer | Pipeline parallelism degree. |
| `contextParallelism` | integer | Context parallelism degree. |
| `expertParallelism` | integer | Expert parallelism degree. |
| `sequenceParallelism` | boolean | Enable sequence parallelism. |
