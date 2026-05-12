---
title: authentication_required | Reference | Warp
url: https://docs.warp.dev/reference/api-and-sdk/troubleshooting/errors/authentication-required
source: sitemap
fetched_at: 2026-04-29T15:05:24.857757431-03:00
rendered_js: false
word_count: 137
summary: This document explains the causes and resolution steps for the authentication_required API error, which occurs due to missing or invalid credentials.
tags:
    - api-error
    - authentication
    - http-401
    - troubleshooting
    - api-key
category: reference
optimized: true
optimized_at: 2026-04-29T15:05:24.857757431-03:00
---
The `authentication_required` error occurs when the API request lacks valid authentication credentials.

> [!note]
> This is classified as a **platform error** (task state → ERROR) rather than a user error, because it typically indicates a configuration issue with the API key rather than a problem with the task itself.

## Details

| Field | Value |
|-------|-------|
| HTTP Status | `401 Unauthorized` |
| Retryable | No |
| Task State | ERROR |

## When does this occur?

This error is returned when:

- The `Authorization` header is missing from the request
- The API key has been revoked or has expired
- The API key is malformed or invalid

## Example response

```json
{
  "type": "https://docs.warp.dev/reference/api-and-sdk/troubleshooting/errors/authentication-required",
  "title": "Authentication required",
  "status": 401,
  "instance": "/api/v1/agent/tasks",
  "error": "Authentication required",
  "retryable": false
}
```

## How to resolve

1. Update your client configuration with the new key.
2. Retry the request.

## Related

- [[263-reference-api-and-sdk-troubleshooting-errors-conflict|conflict]]
