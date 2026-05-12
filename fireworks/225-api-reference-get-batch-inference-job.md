---
title: Get Batch Inference Job - Fireworks AI Docs
url: https://docs.fireworks.ai/api-reference/get-batch-inference-job
source: sitemap
fetched_at: 2026-04-27T20:14:22.164539287-03:00
rendered_js: false
word_count: 14
summary: This document provides a JSON structure template representing the metadata and operational status of a machine learning job execution. It details parameters like input/output datasets, model configuration, inference settings, and real-time progress metrics.
tags:
    - json-schema
    - job-metadata
    - model-status
    - inference-parameters
    - data-pipeline
    - progress-tracking
category: reference
optimized: true
optimized_at: 2026-04-27T00:00:00Z
---
# Get Batch Inference Job

Response schema for a batch inference job.

```json
{
  "name": "<string>",
  "displayName": "<string>",
  "createTime": "2023-11-07T05:31:56Z",
  "createdBy": "<string>",
  "state": "JOB_STATE_UNSPECIFIED",
  "status": {
    "code": "OK",
    "message": "<string>"
  },
  "model": "<string>",
  "inputDatasetId": "<string>",
  "outputDatasetId": "<string>",
  "inferenceParameters": {
    "maxTokens": 123,
    "temperature": 123,
    "topP": 123,
    "n": 123,
    "extraBody": "<string>",
    "topK": 123
  },
  "updateTime": "2023-11-07T05:31:56Z",
  "precision": "PRECISION_UNSPECIFIED",
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
  "continuedFromJobName": "<string>"
}
```

#api-reference #batch-inference
