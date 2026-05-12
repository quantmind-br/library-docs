---
title: List Evaluation Jobs - Fireworks AI Docs
url: https://docs.fireworks.ai/api-reference/list-evaluation-jobs
source: sitemap
fetched_at: 2026-04-27T20:13:49.432072282-03:00
rendered_js: false
word_count: 0
summary: This document presents a structured JSON object detailing the metadata for multiple evaluation jobs. It provides comprehensive information about each job, including its status, associated datasets, and AWS S3 configuration details.
tags:
    - evaluation-jobs
    - json-structure
    - job-metadata
    - aws-s3
    - dataset-management
category: reference
optimized: true
optimized_at: 2026-04-27T00:00:00Z
---
```
{
  "evaluationJobs": [
    {
      "evaluator": "<string>",
      "inputDataset": "<string>",
      "outputDataset": "<string>",
      "name": "<string>",
      "displayName": "<string>",
      "createTime": "2023-11-07T05:31:56Z",
      "createdBy": "<string>",
      "state": "JOB_STATE_UNSPECIFIED",
      "status": {
        "code": "OK",
        "message": "<string>"
      },
      "metrics": {},
      "outputStats": "<string>",
      "updateTime": "2023-11-07T05:31:56Z",
      "awsS3Config": {
        "credentialsSecret": "<string>",
        "iamRoleArn": "<string>"
      }
    }
  ],
  "nextPageToken": "<string>",
  "totalSize": 123
}
```
