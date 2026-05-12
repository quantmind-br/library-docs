---
title: List Batch Inference Jobs - Fireworks AI Docs
url: https://docs.fireworks.ai/api-reference/list-batch-inference-jobs
source: sitemap
fetched_at: 2026-04-27T20:14:03.257891486-03:00
rendered_js: false
optimized: true
optimized_at: 2026-04-27T00:00:00Z
tags:
    - batch-inference
    - job-details
    - data-pipeline
    - status-tracking
    - model-management
    - progress-metrics
category: reference
word_count: 63
---
# List Batch Inference Jobs

`GET /batch_inference_jobs` — Returns a paginated list of batch inference jobs.

## Response Schema

```json
{
  "batchInferenceJobs": [
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
  ],
  "nextPageToken": "<string>",
  "totalSize": 123
}
```

## Fields

| Field | Type | Description |
|-------|------|-------------|
| `batchInferenceJobs` | array | List of batch inference job objects. |
| `nextPageToken` | string | Token for fetching the next page. |
| `totalSize` | integer | Total number of jobs. |