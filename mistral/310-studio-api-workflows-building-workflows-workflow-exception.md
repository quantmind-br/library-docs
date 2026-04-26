---
title: WorkflowsException | Mistral Docs
url: https://docs.mistral.ai/studio-api/workflows/building-workflows/workflow_exception
source: sitemap
fetched_at: 2026-04-26T04:13:54.206764461-03:00
rendered_js: false
word_count: 133
summary: This document describes the WorkflowsException system, which provides a structured approach for standardizing error handling, mapping error codes, and serializing exceptions across workflows and activities.
tags:
    - error-handling
    - structured-exceptions
    - workflows-api
    - exception-mapping
    - api-design
category: concept
optimized: true
optimized_at: 2026-04-26T00:00:00Z
---

Workflows provides a structured exception system through `WorkflowsException` for consistent error handling across workflows and activities.

`WorkflowsException` is the standard exception class for handling errors in workflows. It provides:
- Structured error codes via `ErrorCode` enum
- HTTP status code mapping
- Serialization to JSON responses
- Factory methods for common error scenarios

## ErrorCode Enum

The `ErrorCode` enum provides structured error codes organized by category.

The following error codes are used to identify specific errors that can occur when interacting with the workflow API. These codes follow the `{HTTP_METHOD}_{ENDPOINT}_ERROR` naming convention and are returned in the `code` field of error responses.

## Factory Methods

Create an exception from platform errors:

```python
```

Handles specific error types:
- `RPCError` → Maps to appropriate error code based on RPC status
- `WorkflowQueryRejectedError` → `REJECTED_QUERY_ERROR`
- `WorkflowAlreadyStartedError` → `WORKFLOW_ALREADY_STARTED`

Create an exception from HTTP client errors:

```python
```