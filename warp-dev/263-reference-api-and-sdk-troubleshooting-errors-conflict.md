---
title: conflict | Reference | Warp
url: https://docs.warp.dev/reference/api-and-sdk/troubleshooting/errors/conflict
source: sitemap
fetched_at: 2026-04-29T15:05:23.955240547-03:00
rendered_js: false
word_count: 137
summary: This document explains the 409 Conflict error, identifying the conditions under which it occurs and providing steps for resolution through request retries.
tags:
    - http-409
    - conflict-error
    - api-errors
    - troubleshooting
    - task-management
    - retry-strategy
category: reference
optimized: true
optimized_at: 2026-04-29T15:05:23.955240547-03:00
---
The `conflict` error occurs when a request cannot be completed because the resource is in a conflicting state with the requested operation.

## Details

| Field | Value |
|-------|-------|
| HTTP Status | `409 Conflict` |
| Retryable | Yes |
| Task State | FAILED |

## When does this occur?

This error is returned when:

- You attempt to cancel a task that is still in the **pending** state (the task has not yet been claimed by a worker)

The operation can typically succeed once the resource transitions to the expected state.

## Example response

```json
{
  "type": "https://docs.warp.dev/reference/api-and-sdk/troubleshooting/errors/conflict",
  "title": "Pending agent runs cannot be cancelled, retry after a moment.",
  "status": 409,
  "instance": "/api/v1/agent/tasks/abc123/cancel",
  "error": "Pending agent runs cannot be cancelled, retry after a moment.",
  "retryable": true
}
```

## How to resolve

1. Wait a moment for the resource to transition to the expected state.
2. Retry the request.

For task cancellation specifically, wait until the task moves from **pending** to **in progress** before attempting to cancel.
