---
title: Get Reinforcement Fine-tuning Step
url: https://docs.fireworks.ai/api-reference/get-reinforcement-fine-tuning-step
source: sitemap
fetched_at: 2026-04-27T20:14:10.175964432-03:00
rendered_js: false
optimized: true
optimized_at: 2026-04-27T00:00:00Z
word_count: 18
---
# Get Reinforcement Fine-tuning Step

Returns the configuration and status of a reinforcement fine-tuning step within a job.

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
