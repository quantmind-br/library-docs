---
title: api_router - vLLM
url: https://docs.vllm.ai/en/latest/api/vllm/entrypoints/serve/cache/api_router/
source: sitemap
fetched_at: 2026-05-07T21:21:19.786274018-03:00
rendered_js: false
word_count: 113
summary: This document provides the API reference for vLLM cache management endpoints used to clear encoder, multi-modal, and prefix caches.
tags:
    - vllm
    - cache-management
    - api-endpoint
    - server-operations
    - prefix-cache
    - multimodal-cache
category: api
---

## vllm.entrypoints.serve.cache.api\_router [¶](#vllm.entrypoints.serve.cache.api_router "Permanent link")

## reset\_encoder\_cache `async` [¶](#vllm.entrypoints.serve.cache.api_router.reset_encoder_cache "Permanent link")

```
reset_encoder_cache(raw_request: Request)
```

Reset the encoder cache. Note that we currently do not check if the encoder cache is successfully reset in the API server.

Source code in `vllm/entrypoints/serve/cache/api_router.py`

```
@router.post("/reset_encoder_cache")
async defreset_encoder_cache(raw_request: Request):
"""
    Reset the encoder cache. Note that we currently do not check if the
    encoder cache is successfully reset in the API server.
    """
    logger.info("Resetting encoder cache...")
    await engine_client(raw_request).reset_encoder_cache()
    return Response(status_code=200)
```

## reset\_mm\_cache `async` [¶](#vllm.entrypoints.serve.cache.api_router.reset_mm_cache "Permanent link")

```
reset_mm_cache(raw_request: Request)
```

Reset the multi-modal cache. Note that we currently do not check if the multi-modal cache is successfully reset in the API server.

Source code in `vllm/entrypoints/serve/cache/api_router.py`

```
@router.post("/reset_mm_cache")
async defreset_mm_cache(raw_request: Request):
"""
    Reset the multi-modal cache. Note that we currently do not check if the
    multi-modal cache is successfully reset in the API server.
    """
    logger.info("Resetting multi-modal cache...")
    await engine_client(raw_request).reset_mm_cache()
    return Response(status_code=200)
```

## reset\_prefix\_cache `async` [¶](#vllm.entrypoints.serve.cache.api_router.reset_prefix_cache "Permanent link")

```
reset_prefix_cache(
    raw_request: Request,
    reset_running_requests: bool = Query(default=False),
    reset_external: bool = Query(default=False),
)
```

Reset the local prefix cache.

Optionally, if the query parameter `reset_external=true` also resets the external (connector-managed) prefix cache.

Note that we currently do not check if the prefix cache is successfully reset in the API server.

Example

POST /reset\_prefix\_cache?reset\_external=true

Source code in `vllm/entrypoints/serve/cache/api_router.py`

```
@router.post("/reset_prefix_cache")
async defreset_prefix_cache(
    raw_request: Request,
    reset_running_requests: bool = Query(default=False),
    reset_external: bool = Query(default=False),
):
"""
    Reset the local prefix cache.

    Optionally, if the query parameter `reset_external=true`
    also resets the external (connector-managed) prefix cache.

    Note that we currently do not check if the prefix cache
    is successfully reset in the API server.

    Example:
       POST /reset_prefix_cache?reset_external=true
    """
    logger.info("Resetting prefix cache...")

    await engine_client(raw_request).reset_prefix_cache(
        reset_running_requests, reset_external
    )
    return Response(status_code=200)
```