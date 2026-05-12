---
title: resource_not_found | Reference | Warp
url: https://docs.warp.dev/reference/api-and-sdk/troubleshooting/errors/resource-not-found
source: sitemap
fetched_at: 2026-04-29T15:05:16.871533853-03:00
rendered_js: false
word_count: 173
summary: This document explains the causes and resolution steps for the resource_not_found error, which indicates that a requested identifier does not exist or is inaccessible.
tags:
    - error-handling
    - api-errors
    - http-404
    - troubleshooting
    - resource-management
category: reference
optimized: true
optimized_at: 2026-04-29T00:00:00Z
---
The `resource_not_found` error occurs when a referenced resource cannot be found. This typically means the resource ID is incorrect, the resource has been deleted, or it belongs to a different team.

## Details

| Field | Value |
|-------|-------|
| **HTTP Status** | `404 Not Found` |
| **Retryable** | No |
| **Task State** | FAILED |

## When does this occur?

This error is returned when:

- A task ID, environment UID, schedule ID, or other resource identifier does not match any existing resource
- The referenced resource has been deleted
- The resource exists but belongs to a different team or user (and you don't have access)

The `detail` field in the response will describe which resource was not found.

## Example response

```json
{
  "type": "https://docs.warp.dev/reference/api-and-sdk/troubleshooting/errors/resource-not-found",
  "title": "The requested resource was not found.",
  "status": 404,
  "detail": "task abc123 was not found",
  "instance": "/api/v1/agent/tasks/abc123",
  "error": "The requested resource was not found.",
  "retryable": false
}
```

## How to resolve

1. Verify the resource ID is correct and properly formatted.
2. Check that the resource has not been deleted (for example, via the [Oz web app](https://oz.warp.dev) or CLI).
3. Confirm the resource belongs to your team or that you have access to it.