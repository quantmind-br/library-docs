---
title: Get DPO Job
url: https://docs.fireworks.ai/api-reference/get-dpo-job
source: sitemap
fetched_at: 2026-04-27T20:14:14.74170906-03:00
rendered_js: false
optimized: true
optimized_at: 2026-04-27T00:00:00Z
word_count: 17
---
# Get DPO Job

Returns the configuration and status of a DPO (Direct Preference Optimization) fine-tuning job.

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
