---
title: metrics - vLLM
url: https://docs.vllm.ai/en/latest/api/vllm/entrypoints/openai/realtime/metrics/
source: sitemap
fetched_at: 2026-05-07T21:20:22.236873655-03:00
rendered_js: false
word_count: 84
summary: This document describes an ASGI middleware designed to transparently instrument WebSocket connections with Prometheus metrics for tracking activity and duration.
tags:
    - asgi-middleware
    - prometheus-metrics
    - websocket-instrumentation
    - server-monitoring
    - python-asyncio
category: reference
---

## vllm.entrypoints.openai.realtime.metrics [¶](#vllm.entrypoints.openai.realtime.metrics "Permanent link")

ASGI middleware for WebSocket Prometheus metrics.

Modeled after prometheus-fastapi-instrumentator, this middleware transparently instruments WebSocket endpoints with standard metrics without requiring changes to handler code.

NOTE: This module intentionally has zero vllm imports so that it can be extracted into a standalone package (similar to prometheus-fastapi-instrumentator) in the future. Please keep it that way.

## WebSocketMetricsMiddleware [¶](#vllm.entrypoints.openai.realtime.metrics.WebSocketMetricsMiddleware "Permanent link")

Pure ASGI middleware that instruments WebSocket connections.

Tracks active connections (gauge), total connections (counter), and connection duration (histogram) for all WebSocket endpoints.

Usage::

```
app.add_middleware(WebSocketMetricsMiddleware)
```

Source code in `vllm/entrypoints/openai/realtime/metrics.py`

```
classWebSocketMetricsMiddleware:
"""Pure ASGI middleware that instruments WebSocket connections.

    Tracks active connections (gauge), total connections (counter),
    and connection duration (histogram) for all WebSocket endpoints.

    Usage::

        app.add_middleware(WebSocketMetricsMiddleware)
    """

    def__init__(self, app: ASGIApp) -> None:
        self.app = app

    def__call__(self, scope: Scope, receive: Receive, send: Send) -> Awaitable[None]:
        if scope["type"] != "websocket":
            return self.app(scope, receive, send)

        return self._handle_websocket(scope, receive, send)

    async def_handle_websocket(
        self, scope: Scope, receive: Receive, send: Send
    ) -> None:
        start_time: float | None = None

        async defsend_wrapper(message: Message) -> None:
            nonlocal start_time
            if message["type"] == "websocket.accept":
                start_time = time.monotonic()
                _active_sessions.inc()
                _total_sessions.inc()
            await send(message)

        try:
            await self.app(scope, receive, send_wrapper)
        finally:
            if start_time is not None:
                _active_sessions.dec()
                _session_duration.observe(time.monotonic() - start_time)
```