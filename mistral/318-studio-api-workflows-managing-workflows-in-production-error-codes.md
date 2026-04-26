---
title: API Error Codes | Mistral Docs
url: https://docs.mistral.ai/studio-api/workflows/managing-workflows-in-production/error_codes
source: sitemap
fetched_at: 2026-04-26T04:14:28.923437601-03:00
rendered_js: false
word_count: 759
summary: This document provides a comprehensive reference for Workflows API error codes, explaining the meaning of various HTTP status codes and providing recommended resolutions for troubleshooting.
tags:
    - api-errors
    - workflows-api
    - error-codes
    - troubleshooting
    - http-status-codes
category: reference
optimized: true
optimized_at: 2026-04-26T00:00:00Z
---

When a request to the Workflows API fails, the response includes a structured error code in `WF_XXXX` format.

For **4xx** errors, `detail` contains a specific message describing what went wrong. For **5xx** errors, `detail` is always `"An error occurred"` — the actual cause is logged server-side.

## Client Errors (4xx)

| Code | Status | Description | Resolution |
|------|--------|-------------|------------|
| `WF_1001` | 422 Unprocessable Entity | Invalid event ID during workflow reset | The response includes a `valid_reset_events` field listing valid alternatives |
| `WF_1100` | 404 Not Found | Workflow execution doesn't exist | Verify the execution ID; check the [Workflows Dashboard](https://console.mistral.ai/build/workflows) for the correct ID |
| `WF_1200` | 409 Conflict | Workflow execution with same ID is already running | Use a different execution ID, or wait for existing execution to complete |
| `WF_1201` | 409 Conflict | Action attempted on workflow that is no longer running | Check the workflow's current status; start a new execution if needed |
| `WF_1300` | 422 / 500 / 503 | Schedule creation or management failed | For 422: check cron expression and input payload size; For 503: retry after a few seconds; For 500: check server logs |
| `WF_1301` | 404 Not Found | Schedule ID doesn't exist | List existing schedules to find the correct ID |

## Server Errors (5xx)

| Code | Status | Description | Resolution |
|------|--------|-------------|------------|
| `WF_2000` | 500 Internal Server Error | Catch-all for unmapped errors | Check server logs or contact the platform team |
| `WF_2100` | 500 / 504 | Platform RPC call failed (connection issues, timeouts, unexpected errors) | Retry the request; contact platform team if persistent |
| `WF_2101` | 500 Internal Server Error | Worker registration failed (workflow specs mismatch) | Check worker logs for registration errors; verify workflow definitions are valid |
| `WF_2102` | 500 Internal Server Error | Expected execution could not be found (internal inconsistency) | Report to platform team if persistent |
| `WF_2200` | 500 Internal Server Error | Failed to construct platform client (bad address, invalid credentials) | Check connection configuration (host, port, TLS settings) |
| `WF_2201` | 500 Internal Server Error | Search attribute registration failed during platform initialization | Contact the platform team if persistent |
| `WF_2202` | 500 Internal Server Error | Payload encoding required but input not encoded | Ensure client is using the payload codec; see payload encoding documentation |
| `WF_2300` | 500 Internal Server Error | Streaming operation failed | Check streaming connectivity; see [Streaming](https://docs.mistral.ai/studio-api/workflows/building-workflows/streaming) |
| `WF_2301` | 500 Internal Server Error | Failed to retrieve/parse traces from Tempo backend | Check Tempo/tracing backend health; wait and retry if traces not yet emitted |
| `WF_2302` | 500 Internal Server Error | Database consistency error in event store | Retry the operation; report to platform team if persistent |

> [!info] The Python SDK (`mistralai-workflows`) has its own set of error codes for worker-side errors (invalid workflow definitions, activity configuration issues, etc.). These are different from the API error codes above and are documented in the [Workflows Exception](https://docs.mistral.ai/studio-api/workflows/building-workflows/workflow_exception) guide.