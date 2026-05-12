---
title: Errors | Reference | Warp
url: https://docs.warp.dev/reference/api-and-sdk/troubleshooting/errors
source: sitemap
fetched_at: 2026-04-29T15:05:11.650332181-03:00
rendered_js: false
word_count: 357
summary: This document outlines the standardized error response format for the Oz platform API based on RFC 7807, including field definitions and error classification.
tags:
    - api-errors
    - problem-details
    - rfc-7807
    - error-handling
    - debugging
    - trace-id
category: reference
optimized: true
optimized_at: 2026-04-29T00:00:00Z
---
When the Oz platform API encounters an error, it returns a structured JSON response following [RFC 7807 (Problem Details for HTTP APIs)](https://datatracker.ietf.org/doc/html/rfc7807). Every error response includes a machine-readable error code, a human-readable message, and metadata to help you diagnose and resolve the issue.

## Response format

All error responses share this structure:

```json
{
  "type": "https://docs.warp.dev/reference/api-and-sdk/troubleshooting/errors/invalid-request",
  "title": "The request contains invalid or missing parameters.",
  "status": 400,
  "detail": "schedule_id is required",
  "instance": "/api/v1/agent/tasks",
  "error": "The request contains invalid or missing parameters. (schedule_id is required)",
  "retryable": false,
  "trace_id": "abc123def456..."
}
```

Error responses use the `application/problem+json` content type per RFC 7807.

### Field reference

| Field | Description |
|-------|-------------|
| `type` | A URI identifying the error type. Links to the documentation page for that error. |
| `title` | A short, human-readable summary of the problem. |
| `status` | The HTTP status code for this response. |
| `detail` | Additional context specific to this occurrence of the error. Not always present. |
| `instance` | The request path that produced the error. |
| `error` | A backward-compatible field combining `title` and `detail` (for older clients). When `detail` is present, formatted as `"title (detail)"`. |
| `retryable` | Whether this request can be retried. If `true`, the platform may automatically retry the operation. |
| `trace_id` | An OpenTelemetry trace ID, included when available. Reference this when contacting support. |

Some errors include additional metadata fields (for example, `auth_url`, `provider`, or `inaccessible_repos`). These are documented on each error's page.

## Error categories

Errors are split into two categories based on what caused the failure:

### User errors

These indicate something the caller needs to fix. When a cloud agent task encounters a user error, the task transitions to the **FAILED** state.

- [`not_authorized`](https://docs.warp.dev/reference/api-and-sdk/troubleshooting/errors/not-authorized) — Insufficient permissions for the operation
- [`conflict`](https://docs.warp.dev/reference/api-and-sdk/troubleshooting/errors/conflict) — Request conflicts with the current resource state (retryable)

### Platform errors

These indicate a Warp-side issue. When a cloud agent task encounters a platform error, the task transitions to the **ERROR** state. Retryable errors are automatically retried before the task is marked as failed.

- [`internal_error`](https://docs.warp.dev/reference/api-and-sdk/troubleshooting/errors/internal-error) — Unexpected server-side error (retryable)

## Using the `trace_id`

When an error response includes a `trace_id`, you can include it when [contacting Warp support](https://docs.warp.dev/support-and-community/troubleshooting-and-support/sending-us-feedback) to help the team locate the specific request in internal logs. This is especially useful for `internal_error` and `resource_unavailable` errors.