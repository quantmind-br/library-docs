---
title: Get Supervised Fine-tuning Job
optimized: true
optimized_at: 2026-04-27T00:00:00Z
word_count: 136
---
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
