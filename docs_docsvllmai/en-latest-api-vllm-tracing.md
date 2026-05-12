---
title: tracing - vLLM
url: https://docs.vllm.ai/en/latest/api/vllm/tracing/
source: sitemap
fetched_at: 2026-05-07T21:36:35.050741291-03:00
rendered_js: false
word_count: 200
summary: This document provides an overview of the tracing utilities and instrumentation tools available for tracking application performance using OpenTelemetry-based conventions.
tags:
    - opentelemetry
    - tracing
    - instrumentation
    - span-attributes
    - performance-monitoring
    - distributed-tracing
category: reference
---

Modules:

Name Description `otel` `utils`

## SpanAttributes [¶](#vllm.tracing.SpanAttributes "Permanent link")

Standard attributes for spans.

These are largely based on OpenTelemetry Semantic Conventions but are defined here as constants so they can be used by any backend or logger.

Source code in `vllm/tracing/utils.py`

```
classSpanAttributes:
"""
    Standard attributes for spans.

    These are largely based on OpenTelemetry Semantic Conventions but are defined
    here as constants so they can be used by any backend or logger.
    """

    # Attribute names copied from OTel semantic conventions to avoid version conflicts
    GEN_AI_USAGE_COMPLETION_TOKENS = "gen_ai.usage.completion_tokens"
    GEN_AI_USAGE_PROMPT_TOKENS = "gen_ai.usage.prompt_tokens"
    GEN_AI_REQUEST_MAX_TOKENS = "gen_ai.request.max_tokens"
    GEN_AI_REQUEST_TOP_P = "gen_ai.request.top_p"
    GEN_AI_REQUEST_TEMPERATURE = "gen_ai.request.temperature"
    GEN_AI_RESPONSE_MODEL = "gen_ai.response.model"

    # Custom attributes added until they are standardized
    GEN_AI_REQUEST_ID = "gen_ai.request.id"
    GEN_AI_REQUEST_N = "gen_ai.request.n"
    GEN_AI_USAGE_NUM_SEQUENCES = "gen_ai.usage.num_sequences"
    GEN_AI_LATENCY_TIME_IN_QUEUE = "gen_ai.latency.time_in_queue"
    GEN_AI_LATENCY_TIME_TO_FIRST_TOKEN = "gen_ai.latency.time_to_first_token"
    GEN_AI_LATENCY_E2E = "gen_ai.latency.e2e"
    GEN_AI_LATENCY_TIME_IN_SCHEDULER = "gen_ai.latency.time_in_scheduler"

    # Latency breakdowns
    GEN_AI_LATENCY_TIME_IN_MODEL_FORWARD = "gen_ai.latency.time_in_model_forward"
    GEN_AI_LATENCY_TIME_IN_MODEL_EXECUTE = "gen_ai.latency.time_in_model_execute"
    GEN_AI_LATENCY_TIME_IN_MODEL_PREFILL = "gen_ai.latency.time_in_model_prefill"
    GEN_AI_LATENCY_TIME_IN_MODEL_DECODE = "gen_ai.latency.time_in_model_decode"
    GEN_AI_LATENCY_TIME_IN_MODEL_INFERENCE = "gen_ai.latency.time_in_model_inference"
```

Check if the provided headers dictionary contains trace context.

Source code in `vllm/tracing/utils.py`

```
defcontains_trace_headers(headers: Mapping[str, str]) -> bool:
"""Check if the provided headers dictionary contains trace context."""
    return any(h in headers for h in TRACE_HEADERS)

extract_trace_context(
    headers: Mapping[str, str] | None,
) -> Context | None
```

Extracts context from HTTP headers.

Source code in `vllm/tracing/otel.py`

```
defextract_trace_context(headers: Mapping[str, str] | None) -> Context | None:
"""Extracts context from HTTP headers."""
    if _IS_OTEL_AVAILABLE and headers:
        return TraceContextTextMapPropagator().extract(headers)
    return None
```

Extract only trace-related headers from a larger header dictionary. Useful for logging or passing context to a non-OTel client.

Source code in `vllm/tracing/utils.py`

```
defextract_trace_headers(headers: Mapping[str, str]) -> Mapping[str, str]:
"""
    Extract only trace-related headers from a larger header dictionary.
    Useful for logging or passing context to a non-OTel client.
    """
    return {h: headers[h] for h in TRACE_HEADERS if h in headers}
```

## instrument [¶](#vllm.tracing.instrument "Permanent link")

```
instrument(
    obj: Callable | None = None,
    *,
    span_name: str = "",
    attributes: dict[str, str] | None = None,
    record_exception: bool = True,
)
```

Generic decorator to instrument functions.

Source code in `vllm/tracing/__init__.py`

```
definstrument(
    obj: Callable | None = None,
    *,
    span_name: str = "",
    attributes: dict[str, str] | None = None,
    record_exception: bool = True,
):
"""
    Generic decorator to instrument functions.
    """
    if obj is None:
        return functools.partial(
            instrument,
            span_name=span_name,
            attributes=attributes,
            record_exception=record_exception,
        )

    # Dispatch to OTel (and potentially others later)
    is_available, _, _, otel_instrument, _ = _REGISTERED_TRACING_BACKENDS["otel"]
    if is_available():
        return otel_instrument(
            func=obj,
            span_name=span_name,
            attributes=attributes,
            record_exception=record_exception,
        )
    else:
        return obj
```

## instrument\_manual [¶](#vllm.tracing.instrument_manual "Permanent link")

```
instrument_manual(
    span_name: str,
    start_time: int,
    end_time: int | None = None,
    attributes: dict[str, Any] | None = None,
    context: Any = None,
    kind: Any = None,
)
```

Manually create a span with explicit timestamps.

Parameters:

Name Type Description Default `span_name` `str`

Name of the span to create.

*required* `start_time` `int`

Start time in nanoseconds since epoch.

*required* `end_time` `int | None`

Optional end time in nanoseconds. If None, ends immediately.

`None` `attributes` `dict[str, Any] | None`

Optional dict of span attributes.

`None` `context` `Any`

Optional trace context (e.g., from extract\_trace\_context).

`None` `kind` `Any`

Optional SpanKind (e.g., SpanKind.SERVER).

`None`

Source code in `vllm/tracing/__init__.py`

```
definstrument_manual(
    span_name: str,
    start_time: int,
    end_time: int | None = None,
    attributes: dict[str, Any] | None = None,
    context: Any = None,
    kind: Any = None,
):
"""Manually create a span with explicit timestamps.

    Args:
        span_name: Name of the span to create.
        start_time: Start time in nanoseconds since epoch.
        end_time: Optional end time in nanoseconds. If None, ends immediately.
        attributes: Optional dict of span attributes.
        context: Optional trace context (e.g., from extract_trace_context).
        kind: Optional SpanKind (e.g., SpanKind.SERVER).
    """
    is_available, _, _, _, manual_instrument_fn = _REGISTERED_TRACING_BACKENDS["otel"]
    if is_available():
        return manual_instrument_fn(
            span_name, start_time, end_time, attributes, context, kind
        )
    else:
        return None
```

## is\_tracing\_available [¶](#vllm.tracing.is_tracing_available "Permanent link")

```
is_tracing_available() -> bool
```

Returns True if any tracing backend (OTel, Profiler, etc.) is available. Use this to guard expensive tracing logic in the main code.

Source code in `vllm/tracing/__init__.py`

```
defis_tracing_available() -> bool:
"""
    Returns True if any tracing backend (OTel, Profiler, etc.) is available.
    Use this to guard expensive tracing logic in the main code.
    """
    check_available = [
        is_available
        for is_available, _, _, _, _ in _REGISTERED_TRACING_BACKENDS.values()
    ]
    return any(check_available)
```