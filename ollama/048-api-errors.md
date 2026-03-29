---
title: Errors
url: https://docs.ollama.com/api/errors.md
source: llms
fetched_at: 2026-02-04T11:33:18.021133766-03:00
rendered_js: false
word_count: 163
summary: This document outlines how the API handles errors, covering standard HTTP status codes, JSON error response structures, and error reporting for streaming responses.
tags:
    - error-handling
    - http-status-codes
    - api-errors
    - streaming
    - json-format
    - ndjson
category: reference
---

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.ollama.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Errors

## Status codes

Endpoints return appropriate HTTP status codes based on the success or failure of the request in the HTTP status line (e.g. `HTTP/1.1 200 OK` or `HTTP/1.1 400 Bad Request`). Common status codes are:

* `200`: Success
* `400`: Bad Request (missing parameters, invalid JSON, etc.)
* `404`: Not Found (model doesn't exist, etc.)
* `429`: Too Many Requests (e.g. when a rate limit is exceeded)
* `500`: Internal Server Error
* `502`: Bad Gateway (e.g. when a cloud model cannot be reached)

## Error messages

Errors are returned in the `application/json` format with the following structure, with the error message in the `error` property:

```json  theme={"system"}
{
  "error": "the model failed to generate a response"
}
```

## Errors that occur while streaming

If an error occurs mid-stream, the error will be returned as an object in the `application/x-ndjson` format with an `error` property. Since the response has already started, the status code of the response will not be changed.

```json  theme={"system"}
{"model":"gemma3","created_at":"2025-10-26T17:21:21.196249Z","response":" Yes","done":false}
{"model":"gemma3","created_at":"2025-10-26T17:21:21.207235Z","response":".","done":false}
{"model":"gemma3","created_at":"2025-10-26T17:21:21.219166Z","response":"I","done":false}
{"model":"gemma3","created_at":"2025-10-26T17:21:21.231094Z","response":"can","done":false}
{"error":"an error was encountered while running the model"}
```