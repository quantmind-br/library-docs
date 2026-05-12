---
title: insufficient_credits | Reference | Warp
url: https://docs.warp.dev/reference/api-and-sdk/troubleshooting/errors/insufficient-credits
source: sitemap
fetched_at: 2026-04-29T15:05:12.708435809-03:00
rendered_js: false
word_count: 134
summary: This document explains the causes and resolution steps for the insufficient_credits error, which occurs when a team has exhausted their available cloud agent and integration credits.
tags:
    - error-handling
    - billing-issues
    - cloud-agents
    - http-403
    - troubleshooting
    - account-management
category: reference
optimized: true
optimized_at: 2026-04-29T15:05:12.708435809-03:00
---
The `insufficient_credits` error occurs when your team has no remaining Add-on Credits to run cloud agents or integrations.

## Details

| Field | Value |
|-------|-------|
| HTTP Status | `403 Forbidden` |
| Retryable | No |
| Task State | FAILED |

## When does this occur?

This error is returned when:

- Your team's Add-on Credits balance has reached zero
- A cloud agent task, scheduled run, or integration-triggered run (Slack, Linear) attempts to start but cannot be billed

Cloud agent runs consume credits based on usage. When credits are depleted, no new runs can start until credits are replenished.

## Example response

```json
{
  "type": "https://docs.warp.dev/reference/api-and-sdk/troubleshooting/errors/insufficient-credits",
  "title": "Your team has run out of Add-on Credits. Purchase more credits in your team's billing settings to continue.",
  "status": 403,
  "instance": "/api/v1/agent/tasks",
  "error": "Your team has run out of add-on credits. Purchase more credits in your team's billing settings to continue.",
  "retryable": false
}
```

## How to resolve

1. Purchase additional Add-on Credits.
2. Retry the failed operation.

If you are not a team admin, contact your team admin to purchase credits.
