---
title: operation_not_supported | Reference | Warp
url: https://docs.warp.dev/reference/api-and-sdk/troubleshooting/errors/operation-not-supported
source: sitemap
fetched_at: 2026-04-29T15:05:22.08851333-03:00
rendered_js: false
word_count: 184
summary: This document explains the causes and resolution steps for the operation-not-supported error encountered when attempting to perform restricted actions on specific agent run types.
tags:
    - error-codes
    - api-troubleshooting
    - agent-management
    - cancellation-logic
    - http-422
category: reference
optimized: true
optimized_at: 2026-04-29T00:00:00Z
---
The `operation_not_supported` error occurs when you attempt an operation that is not currently supported for the given resource or its current state.

## Details

| Field | Value |
|-------|-------|
| **HTTP Status** | `422 Unprocessable Entity` |
| **Retryable** | No |
| **Task State** | FAILED |

## When does this occur?

This error is returned when:

- You attempt to cancel a **self-hosted** agent run via the API (self-hosted runs must be cancelled through the hosting infrastructure)
- You attempt to cancel a **local** agent run via the API (local runs must be cancelled from the source client)
- You attempt to cancel a run triggered via **GitHub Actions** (these must be cancelled through the GitHub Actions workflow view)

## Example response

```json
{
"type":"https://docs.warp.dev/reference/api-and-sdk/troubleshooting/errors/operation-not-supported",
"title":"Self-hosted agent runs cannot be cancelled with the API.",
"status":422,
"instance":"/api/v1/agent/tasks/abc123/cancel",
"error":"Self-hosted agent runs cannot be cancelled with the API.",
"retryable":false
}
```

## How to resolve

1. Check the error message to understand which operation is unsupported and why.
2. Use the appropriate method for the operation:
   
   - **Self-hosted runs** — Cancel through your hosting infrastructure.
   - **Local runs** — Cancel from the Warp desktop app or terminal session.
   - **GitHub Actions runs** — Cancel via the GitHub Actions workflow view.