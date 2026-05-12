---
title: integration_disabled | Reference | Warp
url: https://docs.warp.dev/reference/api-and-sdk/troubleshooting/errors/integration-disabled
source: sitemap
fetched_at: 2026-04-29T15:05:19.391044307-03:00
rendered_js: false
word_count: 121
summary: This document explains the integration_disabled error, which occurs when a task triggers an integration that has been turned off in the Oz settings.
tags:
    - error-handling
    - integration-management
    - troubleshooting
    - api-errors
    - access-control
category: reference
optimized: true
optimized_at: 2026-04-29T15:05:19.391044307-03:00
---
The `integration_disabled` error occurs when a task targets an integration that is currently disabled in the Oz settings.

## Details

| Field | Value |
|-------|-------|
| HTTP Status | `403 Forbidden` |
| Retryable | No |
| Task State | FAILED |

## When does this occur?

This error is returned when:

- A Slack message, Linear issue, or other integration event triggers a cloud agent, but the corresponding integration has been disabled in the Oz settings
- The integration was previously active but has been turned off by a team admin

## Example response

```json
{
  "type": "https://docs.warp.dev/reference/api-and-sdk/troubleshooting/errors/integration-disabled",
  "title": "This integration is disabled. Please enable it in Oz.",
  "status": 403,
  "instance": "/api/v1/agent/tasks",
  "error": "This integration is disabled. Please enable it in Oz.",
  "retryable": false
}
```

## How to resolve

1. Enable the integration that was disabled.
2. Retry the triggering event or task.

## Related

- [[269-reference-api-and-sdk-troubleshooting-errors-integration-not-configured|integration_not_configured]]
- [[262-reference-api-and-sdk-troubleshooting-errors-budget-exceeded|budget_exceeded]]
