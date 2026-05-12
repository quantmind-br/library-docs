---
title: budget_exceeded | Reference | Warp
url: https://docs.warp.dev/reference/api-and-sdk/troubleshooting/errors/budget-exceeded
source: sitemap
fetched_at: 2026-04-29T15:05:18.521460853-03:00
rendered_js: false
word_count: 156
summary: This document explains the budget_exceeded error, which occurs when team usage reaches the configured spending limit, and provides instructions for resolving it.
tags:
    - api-error
    - budget-limit
    - billing-constraints
    - troubleshooting
    - error-code-403
category: reference
optimized: true
optimized_at: 2026-04-29T15:05:18.521460853-03:00
---
The `budget_exceeded` error occurs when your team has reached the spending budget limit configured in team settings.

## Details

| Field | Value |
|-------|-------|
| HTTP Status | `403 Forbidden` |
| Retryable | No |
| Task State | FAILED |

## When does this occur?

This error is returned when:

- Your team has set a spending budget cap, and the current period's usage has reached that cap
- A cloud agent task, scheduled run, or integration-triggered run attempts to start but would exceed the budget

The `title` field in the response describes the specific budget constraint.

## Example response

```json
{
  "type": "https://docs.warp.dev/reference/api-and-sdk/troubleshooting/errors/budget-exceeded",
  "title": "Monthly spending budget of $50 has been reached.",
  "status": 403,
  "instance": "/api/v1/agent/tasks",
  "error": "Monthly spending budget of $50 has been reached.",
  "retryable": false
}
```

## How to resolve

1. Go to your team settings and increase the spending budget, or
2. Wait for the budget period to reset (for example, at the start of the next billing cycle).

If you are not a team admin, contact your team admin to adjust the budget.

## Related

- [[268-reference-api-and-sdk-troubleshooting-errors-integration-disabled|integration_disabled]]
