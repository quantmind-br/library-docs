---
title: Check Batch Status - Fireworks AI Docs
url: https://docs.fireworks.ai/api-reference/get-batch-status
source: sitemap
fetched_at: 2026-04-27T20:14:20.041696637-03:00
rendered_js: false
word_count: 184
summary: This document describes an API endpoint used to check the current status of a previously submitted batch request and retrieve its final result if the job has been completed.
tags:
    - api-endpoint
    - batch-status
    - request-check
    - fireworks-api
    - job-retrieval
category: reference
optimized: true
optimized_at: 2026-04-27T00:00:00Z
---
# Check Batch Status

Check the current status of a previously submitted batch request. Retrieve the final result if the job has completed.

## Endpoint

`GET /v1/batch/{batch_id}`

## Headers

| Header | Description |
|---|---|
| `Authorization` | Fireworks API key. Format: `Authorization=FIREWORKS_API_KEY`. Accepts query param as fallback. |

## Path Parameters

| Param | Type | Description |
|---|---|---|
| `account_id` | string | Fireworks account identifier. Must match the account used when the batch was submitted. |
| `batch_id` | string | Unique batch job identifier (matches `batch_id` returned on batch submission). |

## Response

| Field | Type | Description |
|---|---|---|
| `status` | string | Job status: `"completed"` or `"processing"`. |
| `batchId` | string | Batch job ID (matches the original request). |
| `message` | string | Human-readable state description. Typically `null` on successful completion. |
| `contentType` | string | Original content type of the response body. Use to determine how to parse `body`. |
| `body` | string | Serialized result — present only when `status` is `"completed"`. Format depends on `contentType`. |

#api-reference #batch-inference
