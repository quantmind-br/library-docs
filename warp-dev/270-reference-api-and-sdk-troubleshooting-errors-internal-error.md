---
title: internal_error | Reference | Warp
url: https://docs.warp.dev/reference/api-and-sdk/troubleshooting/errors/internal-error
source: sitemap
fetched_at: 2026-04-29T15:05:26.860385666-03:00
rendered_js: false
word_count: 115
summary: This document defines the internal_error status, explaining its triggers as unexpected server-side failures and detailing the platform's automatic retry behavior.
tags:
    - internal-error
    - server-error
    - error-handling
    - api-troubleshooting
    - http-500
category: reference
optimized: true
optimized_at: 2026-04-29T18:00:00Z
---
`internal_error` is a catch-all for unexpected server-side errors. The platform automatically retries these before marking the task as failed.

## Details

| Field | Value |
|---|---|
| HTTP Status | `500 Internal Server Error` |
| Retryable | Yes (automatic) |
| Task State | ERROR |

## When does this occur?

- An unexpected condition on the server not matching any specific error category
- An internal service dependency failed or timed out
- An unclassified error during task processing

## Example response

```json
{
  "type": "https://docs.warp.dev/reference/api-and-sdk/troubleshooting/errors/internal-error",
  "title": "An unexpected error occurred. Please try again later. If the issue persists, contact support.",
  "status": 500,
  "instance": "/api/v1/agent/tasks",
  "error": "An unexpected error occurred. Please try again later. If the issue persists, contact support.",
  "retryable": true,
  "trace_id": "abc123..."
}
```

## How to resolve

No action is typically needed — the platform retries automatically. If the error persists, wait a few minutes and try again.

#internal-error #server-error #error-handling #api-troubleshooting #http-500
