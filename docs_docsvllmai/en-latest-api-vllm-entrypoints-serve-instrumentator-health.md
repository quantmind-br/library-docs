---
title: health - vLLM
url: https://docs.vllm.ai/en/latest/api/vllm/entrypoints/serve/instrumentator/health/
source: sitemap
fetched_at: 2026-05-07T21:21:30.809066718-03:00
rendered_js: false
word_count: 9
summary: This document defines the health check endpoint for the vLLM serving infrastructure, which verifies the status of the underlying engine.
tags:
    - api-endpoint
    - health-check
    - vllm-server
    - engine-status
    - http-response
category: api
---

## health `async` [¶](#vllm.entrypoints.serve.instrumentator.health.health "Permanent link")

```
health(raw_request: Request) -> Response
```

Health check.

Source code in `vllm/entrypoints/serve/instrumentator/health.py`

```
@router.get("/health", response_class=Response)
async defhealth(raw_request: Request) -> Response:
"""Health check."""
    client = engine_client(raw_request)
    if client is None:
        # Render-only servers have no engine; they are always healthy.
        return Response(status_code=200)
    try:
        await client.check_health()
        return Response(status_code=200)
    except EngineDeadError:
        return Response(status_code=503)
```