---
title: content_policy_violation | Reference | Warp
url: https://docs.warp.dev/reference/api-and-sdk/troubleshooting/errors/content-policy-violation
source: sitemap
fetched_at: 2026-04-29T15:05:23.024430545-03:00
rendered_js: false
word_count: 143
summary: This document explains the causes and resolution steps for the content_policy_violation error occurring within the platform.
tags:
    - error-handling
    - troubleshooting
    - content-policy
    - api-reference
    - security-compliance
category: reference
optimized: true
optimized_at: 2026-04-29T15:05:23.024430545-03:00
---
The `content_policy_violation` error occurs when the task prompt or environment setup commands are flagged by the platform's automated content policy checks.

## Details

| Field | Value |
|-------|-------|
| HTTP Status | `403 Forbidden` |
| Retryable | No |
| Task State | FAILED |

## When does this occur?

This error is returned when:

- The task prompt contains content that violates Warp's usage policies
- The environment setup commands contain patterns flagged as potentially harmful
- The automated content classifier determines the task should be blocked

> [!note]
> For security reasons, the error message is intentionally generic and does not describe what specifically was flagged.

## Example response

```json
{
  "type": "https://docs.warp.dev/reference/api-and-sdk/troubleshooting/errors/content-policy-violation",
  "title": "Content policy violation",
  "status": 403,
  "instance": "/api/v1/agent/tasks",
  "error": "Content policy violation",
  "retryable": false
}
```

## How to resolve

1. If you believe this was flagged in error, contact [Warp support](https://docs.warp.dev/support-and-community/troubleshooting-and-support/sending-us-feedback) and include the `trace_id` from the error response.

## Related

- [[259-reference-api-and-sdk-troubleshooting-errors-environment-setup-failed|environment_setup_failed]]
- [[263-reference-api-and-sdk-troubleshooting-errors-conflict|conflict]]
