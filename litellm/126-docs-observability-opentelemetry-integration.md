---
title: OpenTelemetry - Tracing LLMs with any observability tool | liteLLM
url: https://docs.litellm.ai/docs/observability/opentelemetry_integration
source: sitemap
fetched_at: 2026-01-21T19:46:25.231115367-03:00
rendered_js: false
word_count: 383
summary: This document provides instructions for integrating OpenTelemetry with LiteLLM to enable observability and trace logging across various providers. It covers setup procedures, configuration options for redacting sensitive data, and troubleshooting common integration issues.
tags:
    - opentelemetry
    - litellm
    - observability
    - tracing
    - python-sdk
    - data-redaction
    - troubleshooting
category: guide
---

OpenTelemetry is a CNCF standard for observability. It connects to any observability tool, such as Jaeger, Zipkin, Datadog, New Relic, Traceloop, Levo AI and others.

Change in v1.81.0

From v1.81.0, the request/response will be set as attributes on the parent "Received Proxy Server Request" span by default. This allows you to see the request/response in the parent span in your observability tool.

**Note:** When making multiple LLM calls within an external OTEL span context, the last call's attributes will overwrite previous calls' attributes on the parent span.

To use the older behavior with nested "litellm\_request" spans (which creates separate spans for each call), set the following environment variable:

```
USE_OTEL_LITELLM_REQUEST_SPAN=true
```

## Getting Started[​](#getting-started "Direct link to Getting Started")

Install the OpenTelemetry SDK:

```
pip install opentelemetry-api opentelemetry-sdk opentelemetry-exporter-otlp
```

Set the environment variables (different providers may require different variables):

- Log to Traceloop Cloud
- Log to OTEL HTTP Collector
- Log to OTEL GRPC Collector
- Log to Laminar

```
OTEL_EXPORTER="otlp_http"
OTEL_ENDPOINT="https://api.traceloop.com"
OTEL_HEADERS="Authorization=Bearer%20<your-api-key>"
```

Use just 1 line of code, to instantly log your LLM responses **across all providers** with OpenTelemetry:

```
litellm.callbacks =["otel"]
```

## Redacting Messages, Response Content from OpenTelemetry Logging[​](#redacting-messages-response-content-from-opentelemetry-logging "Direct link to Redacting Messages, Response Content from OpenTelemetry Logging")

### Redact Messages and Responses from all OpenTelemetry Logging[​](#redact-messages-and-responses-from-all-opentelemetry-logging "Direct link to Redact Messages and Responses from all OpenTelemetry Logging")

Set `litellm.turn_off_message_logging=True` This will prevent the messages and responses from being logged to OpenTelemetry, but request metadata will still be logged.

### Redact Messages and Responses from specific OpenTelemetry Logging[​](#redact-messages-and-responses-from-specific-opentelemetry-logging "Direct link to Redact Messages and Responses from specific OpenTelemetry Logging")

In the metadata typically passed for text completion or embedding calls you can set specific keys to mask the messages and responses for this call.

Setting `mask_input` to `True` will mask the input from being logged for this call

Setting `mask_output` to `True` will make the output from being logged for this call.

Be aware that if you are continuing an existing trace, and you set `update_trace_keys` to include either `input` or `output` and you set the corresponding `mask_input` or `mask_output`, then that trace will have its existing input and/or output replaced with a redacted message.

## Support[​](#support "Direct link to Support")

For any question or issue with the integration you can reach out to the OpenLLMetry maintainers on [Slack](https://traceloop.com/slack) or via [email](mailto:dev@traceloop.com).

## Troubleshooting[​](#troubleshooting "Direct link to Troubleshooting")

### Trace LiteLLM Proxy user/key/org/team information on failed requests[​](#trace-litellm-proxy-userkeyorgteam-information-on-failed-requests "Direct link to Trace LiteLLM Proxy user/key/org/team information on failed requests")

LiteLLM emits the user\_api\_key\_metadata

- key hash
- key\_alias
- org\_id
- user\_id
- team\_id

for successful + failed requests

click under `litellm_request` in the trace

### Not seeing traces land on Integration[​](#not-seeing-traces-land-on-integration "Direct link to Not seeing traces land on Integration")

If you don't see traces landing on your integration, set `OTEL_DEBUG="True"` in your LiteLLM environment and try again.

This will emit any logging issues to the console.