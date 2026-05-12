---
title: feature_not_available | Reference | Warp
url: https://docs.warp.dev/reference/api-and-sdk/troubleshooting/errors/feature-not-available
source: sitemap
fetched_at: 2026-04-29T15:05:13.242090697-03:00
rendered_js: false
word_count: 152
summary: This document explains the feature_not_available error, which indicates a request was denied because the current subscription plan does not support the requested feature.
tags:
    - error-handling
    - api-errors
    - billing-requirements
    - feature-gating
    - troubleshooting
category: reference
optimized: true
optimized_at: 2026-04-29T15:05:13.242090697-03:00
---
The `feature_not_available` error occurs when you attempt to use a feature or capability not included in your team's current plan.

## Details

| Field | Value |
|-------|-------|
| HTTP Status | `403 Forbidden` |
| Retryable | No |
| Task State | FAILED |

## When does this occur?

This error is returned when:

- You attempt to use a feature that requires a higher-tier plan (for example, certain integrations, advanced capabilities, or self-hosted execution)
- A cloud agent or integration trigger tries to access a feature gated behind a plan upgrade

The `title` field in the response describes the specific feature that is unavailable.

## Example response

```json
{
  "type": "https://docs.warp.dev/reference/api-and-sdk/troubleshooting/errors/feature-not-available",
  "title": "Slack integration requires a Build plan or higher.",
  "status": 403,
  "instance": "/api/v1/agent/tasks",
  "error": "Slack integration requires a Build plan or higher.",
  "retryable": false
}
```

## How to resolve

1. Check which plan your team is on in your team's billing settings.
2. Upgrade to a plan that includes the required feature.
3. Retry the operation.

For plan comparisons and feature availability, see [Access, Billing, and Identity](https://docs.warp.dev/agent-platform/cloud-agents/team-access-billing-and-identity).
