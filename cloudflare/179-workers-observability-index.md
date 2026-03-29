---
title: Observability · Cloudflare Workers docs
url: https://developers.cloudflare.com/workers/observability/index.md
source: llms
fetched_at: 2026-01-24T15:26:32.319142141-03:00
rendered_js: false
word_count: 334
summary: This document provides an overview of Cloudflare Workers' observability features, including logging, tracing, metrics, and debugging tools. It explains how to monitor application performance and export telemetry data to third-party platforms.
tags:
    - cloudflare-workers
    - observability
    - logging
    - tracing
    - metrics
    - debugging
    - opentelemetry
    - monitoring
category: guide
---

Cloudflare Workers provides comprehensive observability tools to help you understand how your applications are performing, diagnose issues, and gain insights into request flows. Whether you want to use Cloudflare's native observability platform or export telemetry data to your existing monitoring stack, Workers has you covered.

## Logs

Logs are essential for troubleshooting and understanding your application's behavior. Cloudflare offers several ways to access and manage your Worker logs.

[Workers Logs ](https://developers.cloudflare.com/workers/observability/logs/workers-logs/)Automatically collect, store, filter, and analyze logs in the Cloudflare dashboard.

[Real-time logs ](https://developers.cloudflare.com/workers/observability/logs/real-time-logs/)Access log events in near real-time for immediate feedback during development and deployments.

[Tail Workers ](https://developers.cloudflare.com/workers/observability/logs/tail-workers/)Apply custom filtering, sampling, and transformation logic to your telemetry data.

[Workers Logpush ](https://developers.cloudflare.com/workers/observability/logs/logpush/)Send Workers Trace Event Logs to supported destinations like R2, S3, or logging providers.

## Traces

[Tracing](https://developers.cloudflare.com/workers/observability/traces/) gives you end-to-end visibility into the life of a request as it travels through your Workers application and connected services. With automatic instrumentation, Cloudflare captures telemetry data for fetch calls, binding operations (KV, R2, Durable Objects), and handler invocations - no code changes required.

## Metrics and analytics

[Metrics and analytics](https://developers.cloudflare.com/workers/observability/metrics-and-analytics/) let you monitor your Worker's health with built-in metrics including request counts, error rates, CPU time, wall time, and execution duration. View metrics per Worker or aggregated across all Workers on a zone.

## Query Builder

The [Query Builder](https://developers.cloudflare.com/workers/observability/query-builder/) helps you write structured queries to investigate and visualize your telemetry data. Build queries with filters, aggregations, and groupings to analyze logs and identify patterns.

## Exporting data

[Export OpenTelemetry-compliant traces and logs](https://developers.cloudflare.com/workers/observability/exporting-opentelemetry-data/) from Workers to your existing observability stack. Workers supports exporting to any destination with an OTLP endpoint, including Honeycomb, Grafana Cloud, Axiom, and Sentry.

## Debugging

[Errors and exceptions ](https://developers.cloudflare.com/workers/observability/errors/)Understand Workers error codes and debug common issues.

[Source maps and stack traces ](https://developers.cloudflare.com/workers/observability/source-maps/)Get readable stack traces that map back to your original source code.

[DevTools ](https://developers.cloudflare.com/workers/observability/dev-tools/)Use Chrome DevTools for breakpoints, CPU profiling, and memory debugging during local development.

## Additional resources

[MCP server ](https://github.com/cloudflare/mcp-server-cloudflare/tree/main/apps/workers-observability)Query Workers observability data using the Model Context Protocol.

[Third-party integrations ](https://developers.cloudflare.com/workers/observability/third-party-integrations/)Integrate Workers with third-party observability platforms.