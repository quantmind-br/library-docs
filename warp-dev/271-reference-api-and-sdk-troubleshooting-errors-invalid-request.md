---
title: invalid_request | Reference | Warp
url: https://docs.warp.dev/reference/api-and-sdk/troubleshooting/errors/invalid-request
source: sitemap
fetched_at: 2026-04-29T15:05:15.876241578-03:00
rendered_js: false
word_count: 124
summary: This document explains the causes and resolution steps for the invalid_request error, which indicates that an API request was malformed or contained invalid parameters.
tags:
    - api-error
    - http-400
    - error-handling
    - troubleshooting
    - request-validation
category: reference
optimized: true
optimized_at: 2026-04-29T18:00:00Z
---
`invalid_request` occurs when the API request is malformed or contains invalid parameters.

## Details

| Field | Value |
|---|---|
| HTTP Status | `400 Bad Request` |
| Retryable | No |
| Task State | FAILED |

## When does this occur?

- Required fields missing from request body (e.g., `prompt` or `schedule_id`)
- Parameter values invalid or out of range
- Request body unparseable (malformed JSON)
- A referenced identifier in the wrong format
- A team-owned task references a personal environment (team tasks require team-scoped environments)

The `detail` field in the response describes the specific validation issue.

## How to resolve

1. Check the `detail` field for the specific validation issue.
2. Retry the request.

#api-error #http-400 #error-handling #troubleshooting #request-validation
