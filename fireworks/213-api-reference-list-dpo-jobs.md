---
title: List Dpo Jobs - Fireworks AI Docs
url: https://docs.fireworks.ai/api-reference/list-dpo-jobs
source: sitemap
fetched_at: 2026-04-27T20:13:53.080658162-03:00
rendered_js: false
word_count: 0
summary: This document presents a JSON structure defining job details for training tasks, encapsulating various configuration parameters like model architecture, training hyperparameters, and logging settings.
tags:
    - job-details
    - training-config
    - dpo-jobs
    - hyperparameters
    - aws-s3
    - azure-blob
category: reference
optimized: true
optimized_at: 2026-04-27T00:00:00Z
---
```
{
  "dpoJobs": [
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
  ],
  "nextPageToken": "<string>",
  "totalSize": 123
}
```
