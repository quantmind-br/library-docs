---
title: Observability | Mistral Docs
url: https://docs.mistral.ai/studio-api/workflows/observability
source: sitemap
fetched_at: 2026-04-26T04:14:36.252306391-03:00
rendered_js: false
word_count: 190
summary: This document explains how to utilize OpenTelemetry tracing for monitoring, debugging, and analyzing the performance of workflow executions.
tags:
    - opentelemetry
    - workflow-observability
    - distributed-tracing
    - execution-diagnostics
    - performance-monitoring
category: guide
optimized: true
optimized_at: 2026-04-26T00:00:00Z
---

This guide covers OpenTelemetry traces for execution-level diagnostics.

Traces capture execution details (spans, timings, errors) and are optimized for debugging and performance analysis. They are independent from custom task events.

## Activity Spans

Activities automatically generate spans. Use the `name` parameter to make them more readable:

```python
```

## Trace Sampling

Trace collection is sampled. By default the worker uses a parent-based sampler with a configurable sample rate, so upstream decisions can be honored.

> [!tip] For the finest control of sampling, pass a `traceparent` header at your workflow entry point (or API edge). This lets you force sampling on or off and propagate the parent trace consistently.

## Retrieving Traces

Three methods are available to retrieve trace data for a given execution:

| Method | Description |
|--------|-------------|
| `get_workflow_execution_trace_otel()` | Returns raw OpenTelemetry trace data (spans with timings, attributes, and parent-child relationships). Use this to feed traces into your own observability backend (Jaeger, Grafana Tempo, etc.). |
| `get_workflow_execution_trace_summary()` | Returns a high-level summary of the execution: total duration, activity count, error count. Useful for dashboards and quick status checks. |
| `get_workflow_execution_trace_events()` | Returns a chronological list of events in the execution. Set `include_internal_events=False` to filter out platform-internal events and see only your workflow and activity events. |