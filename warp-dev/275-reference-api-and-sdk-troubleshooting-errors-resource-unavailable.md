---
title: resource_unavailable | Reference | Warp
url: https://docs.warp.dev/reference/api-and-sdk/troubleshooting/errors/resource-unavailable
source: sitemap
fetched_at: 2026-04-29T15:05:25.885685525-03:00
rendered_js: false
word_count: 150
summary: This document explains the causes and resolution steps for the resource_unavailable error, which occurs due to transient infrastructure capacity issues or sandbox creation failures.
tags:
    - error-handling
    - api-errors
    - troubleshooting
    - infrastructure-issues
    - transient-errors
category: reference
optimized: true
optimized_at: 2026-04-29T00:00:00Z
---
The `resource_unavailable` error indicates a transient infrastructure issue that prevented the cloud agent task from running. This is automatically retried by the platform.

## Details

| Field | Value |
|-------|-------|
| **HTTP Status** | `429 Too Many Requests` or `500 Internal Server Error` |
| **Retryable** | Yes (automatic) |
| **Task State** | ERROR |

## When does this occur?

This error is returned when:

- **Capacity full (429)** — Cloud agent capacity is temporarily saturated. Your task will be queued and retried automatically.
- **Sandbox creation failed (500)** — A sandbox instance could not be created for the agent. This is typically a transient issue.

## Example responses

### Capacity full

```json
{
"type":"https://docs.warp.dev/reference/api-and-sdk/troubleshooting/errors/resource-unavailable",
"title":"Agent capacity is temporarily full. Your task will be retried automatically, or you can try again later.",
"status":429,
"instance":"/api/v1/agent/tasks",
"error":"Agent capacity is temporarily full. Your task will be retried automatically, or you can try again later.",
"retryable":true,
"trace_id":"abc123..."
}
```

### Sandbox creation failed

```json
{
"type":"https://docs.warp.dev/reference/api-and-sdk/troubleshooting/errors/resource-unavailable",
"title":"Could not create sandbox for the agent run.",
"status":500,
"instance":"/api/v1/agent/tasks",
"error":"Could not create sandbox for the agent run.",
"retryable":true,
"trace_id":"abc123..."
}
```

## How to resolve

No action is typically needed — the platform will automatically retry the task.

If the error persists after retries:

1. Try again later when capacity has freed up.