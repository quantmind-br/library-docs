---
title: metrics - vLLM
url: https://docs.vllm.ai/en/latest/api/vllm/entrypoints/serve/instrumentator/metrics/
source: sitemap
fetched_at: 2026-05-07T21:21:31.569696219-03:00
rendered_js: false
word_count: 22
summary: This document provides the implementation for integrating Prometheus monitoring metrics into a FastAPI application, including specific configuration for response handling and path routing.
tags:
    - fastapi
    - prometheus
    - monitoring
    - instrumentation
    - metrics
    - asgi-middleware
category: configuration
---

Mount prometheus metrics to a FastAPI app.

Source code in `vllm/entrypoints/serve/instrumentator/metrics.py`

```
defattach_router(app: FastAPI):
"""Mount prometheus metrics to a FastAPI app."""

    registry = get_prometheus_registry()

    # `response_class=PrometheusResponse` is needed to return an HTTP response
    # with header "Content-Type: text/plain; version=0.0.4; charset=utf-8"
    # instead of the default "application/json" which is incorrect.
    # See https://github.com/trallnag/prometheus-fastapi-instrumentator/issues/163#issue-1296092364
    Instrumentator(
        excluded_handlers=[
            "/metrics",
            "/health",
            "/load",
            "/ping",
            "/version",
            "/server_info",
        ],
        registry=registry,
    ).add().instrument(app).expose(app, response_class=PrometheusResponse)

    # Add prometheus asgi middleware to route /metrics requests
    metrics_route = Mount("/metrics", make_asgi_app(registry=registry))

    # Workaround for 307 Redirect for /metrics
    metrics_route.path_regex = re.compile("^/metrics(?P<path>.*)$")
    app.routes.append(metrics_route)
```