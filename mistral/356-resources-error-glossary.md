---
title: Error glossary | Mistral Docs
url: https://docs.mistral.ai/resources/error-glossary
source: sitemap
fetched_at: 2026-04-26T04:11:37.74989458-03:00
rendered_js: false
word_count: 94
summary: This document provides a comprehensive overview of Mistral API error codes, the structure of error responses, and recommended strategies for handling transient failures using exponential backoff.
tags:
    - api-errors
    - http-status-codes
    - error-handling
    - exponential-backoff
    - mistral-api
category: reference
optimized: true
optimized_at: 2026-04-26T00:00:00Z
---

This page lists the HTTP status codes returned by the Mistral API, their meanings, and how to resolve them.

## Client Errors (4xx)

| Code | Description |
|------|-------------|
| 400 | Bad Request |
| 401 | Authentication Error |
| 403 | Permission Denied |
| 404 | Not Found |
| 422 | Invalid Request |
| 429 | Rate Limit Error |

## Server Errors (5xx)

| Code | Description |
|------|-------------|
| 500 | Internal Server Error |
| 502 | Bad Gateway |
| 503 | Service Unavailable |
| 504 | Gateway Timeout |

## Error Response Format

All errors return a JSON body with this structure:

```json
{"object":"error","message":"A human-readable description of the error.","type":"invalid_request_error","param":"model","code":"unknown_model"}
```

| Field | Description |
|-------|-------------|
| `message` | Human-readable error description |
| `type` | Error category (`invalid_request_error`, `authentication_error`, `rate_limit_error`, `server_error`) |
| `param` | The parameter that caused the error (if applicable) |
| `code` | Machine-readable error code (if applicable) |

## Recommended Retry Strategy

For transient errors (429, 500, 502, 503, 504), implement exponential backoff:

```python
import time
import random
from mistralai import Mistral

client = Mistral(api_key="YOUR_API_KEY")

def call_with_retry(func, max_retries=5):
    for attempt in range(max_retries):
        try:
            return func()
        except Exception as e:
            if attempt == max_retries - 1:
                raise
            wait = (2 ** attempt) + random.uniform(0, 1)
            time.sleep(wait)
```

> [!tip] The official Python and TypeScript SDKs include built-in retry logic with exponential backoff. Use the SDKs to avoid implementing this yourself.