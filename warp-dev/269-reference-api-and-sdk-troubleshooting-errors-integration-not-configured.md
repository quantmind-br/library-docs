---
title: integration_not_configured | Reference | Warp
url: https://docs.warp.dev/reference/api-and-sdk/troubleshooting/errors/integration-not-configured
source: sitemap
fetched_at: 2026-04-29T15:05:20.176751904-03:00
rendered_js: false
word_count: 177
summary: This document explains the integration_not_configured error, providing details on why it occurs, the associated metadata fields, and the steps required to resolve it.
tags:
    - error-handling
    - integration-configuration
    - api-errors
    - troubleshooting
    - oauth-credentials
category: reference
optimized: true
optimized_at: 2026-04-29T15:05:20.176751904-03:00
---
The `integration_not_configured` error occurs when a task requires an integration whose setup has not been completed (for example, missing OAuth tokens or unfinished configuration steps).

## Details

| Field | Value |
|-------|-------|
| HTTP Status | `400 Bad Request` |
| Retryable | No |
| Task State | FAILED |

## When does this occur?

This error is returned when:

- An integration (Slack, Linear, etc.) was partially set up but the configuration was not completed
- Required OAuth tokens or credentials for the integration are missing or expired
- The integration was installed but additional setup steps were not finished

## Additional metadata fields

This error includes extra fields beyond the standard response format:

| Field | Description |
|-------|-------------|
| `integration_name` | The name of the integration that needs configuration |
| `setup_url` | A URL to the integration setup page where you can complete configuration |

## Example response

```json
{
  "type": "https://docs.warp.dev/reference/api-and-sdk/troubleshooting/errors/integration-not-configured",
  "title": "Slack integration is not configured",
  "status": 400,
  "instance": "/api/v1/agent/tasks",
  "error": "Slack integration is not configured",
  "integration_name": "slack",
  "setup_url": "https://app.warp.dev/integrations/slack/setup",
  "retryable": false
}
```

## How to resolve

1. Complete all setup steps for the integration.
2. Retry the triggering event or task.

## Related

- [[268-reference-api-and-sdk-troubleshooting-errors-integration-disabled|integration_disabled]]
