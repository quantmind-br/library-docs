---
title: middleware - vLLM
url: https://docs.vllm.ai/en/latest/api/vllm/entrypoints/serve/elastic_ep/middleware/
source: sitemap
fetched_at: 2026-05-07T21:21:27.936197496-03:00
rendered_js: false
word_count: 41
summary: This middleware intercepts incoming HTTP requests and returns a 503 Service Unavailable response when the model is in a scaling state.
tags:
    - middleware
    - http-requests
    - scaling-logic
    - service-availability
    - asgi-middleware
category: concept
---

Middleware that checks if the model is currently scaling and returns a 503 Service Unavailable response if it is.

This middleware applies to all HTTP requests and prevents processing when the model is in a scaling state.

Source code in `vllm/entrypoints/serve/elastic_ep/middleware.py`

```
classScalingMiddleware:
"""
    Middleware that checks if the model is currently scaling and
    returns a 503 Service Unavailable response if it is.

    This middleware applies to all HTTP requests and prevents
    processing when the model is in a scaling state.
    """

    def__init__(self, app: ASGIApp) -> None:
        self.app = app

    def__call__(self, scope: Scope, receive: Receive, send: Send) -> Awaitable[None]:
        if scope["type"] != "http":
            return self.app(scope, receive, send)

        # Check global scaling state
        if get_scaling_elastic_ep():
            # Return 503 Service Unavailable response
            response = JSONResponse(
                content={
                    "error": "The model is currently scaling. Please try again later."
                },
                status_code=503,
            )
            return response(scope, receive, send)

        return self.app(scope, receive, send)
```