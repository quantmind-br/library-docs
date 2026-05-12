---
title: Get Evaluation Job - Fireworks AI
url: https://docs.fireworks.ai/api-reference/get-evaluation-job
source: sitemap
fetched_at: 2026-04-27T20:14:13.720628226-03:00
rendered_js: false
word_count: 151
summary: Response schema for the GET /accounts/{account_id}/evaluationJobs/{evaluation_job_id} endpoint.
tags:
    - api-reference
    - evaluation
    - response-schema
optimized: true
optimized_at: 2026-04-27T00:00:00Z
---
GET `v1/accounts/{account_id}/evaluationJobs/{evaluation_job_id}`

## Response

| Field | Type | Description |
|---|---|---|
| `name` | string | Resource name |
| `displayName` | string | Display name |
| `evaluator` | string | Evaluator resource name |
| `inputDataset` | string | Input dataset resource name |
| `outputDataset` | string | Output dataset resource name |
| `createTime` | string (RFC3339) | Creation timestamp |
| `createdBy` | string | Creator user ID |
| `state` | string | Job state (e.g. `JOB_STATE_UNSPECIFIED`) |
| `status.code` | string | Status code (e.g. `OK`) |
| `status.message` | string | Status message |
| `metrics` | object | Evaluation metrics |
| `outputStats` | string | Output statistics |
| `updateTime` | string (RFC3339) | Last update timestamp |
| `awsS3Config.credentialsSecret` | string | AWS credentials secret name |
| `awsS3Config.iamRoleArn` | string | IAM role ARN for S3 access |

```json
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
```