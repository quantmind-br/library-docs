---
title: Generic API Callback (Webhook) | liteLLM
url: https://docs.litellm.ai/docs/observability/generic_api
source: sitemap
fetched_at: 2026-01-21T19:46:07.179757717-03:00
rendered_js: false
word_count: 231
summary: This document explains how to configure and use LiteLLM's generic HTTP callbacks to send logs to external endpoints with support for various log formats and batching settings.
tags:
    - litellm
    - http-callbacks
    - logging
    - api-integration
    - log-formatting
    - batching
    - ndjson
category: configuration
---

Send LiteLLM logs to any HTTP endpoint.

## Quick Start[​](#quick-start "Direct link to Quick Start")

```
model_list:
-model_name: gpt-3.5-turbo
litellm_params:
model: openai/gpt-3.5-turbo
api_key: os.environ/OPENAI_API_KEY

litellm_settings:
callbacks:["custom_api_name"]

callback_settings:
custom_api_name:
callback_type: generic_api
endpoint: https://your-endpoint.com/logs
headers:
Authorization: Bearer sk-1234
```

## Configuration[​](#configuration "Direct link to Configuration")

### Basic Setup[​](#basic-setup "Direct link to Basic Setup")

```
callback_settings:
<callback_name>:
callback_type: generic_api
endpoint: https://your-endpoint.com  # required
headers:# optional
Authorization: Bearer <token>
Custom-Header: value
event_types:# optional, defaults to all events
- llm_api_success
- llm_api_failure
```

### Parameters[​](#parameters "Direct link to Parameters")

ParameterTypeRequiredDescription`callback_type`stringYesMust be `generic_api``endpoint`stringYesHTTP endpoint to send logs to`headers`dictNoCustom headers for the request`event_types`listNoFilter events: `llm_api_success`, `llm_api_failure`. Defaults to all events.`log_format`stringNoOutput format: `json_array` (default), `ndjson`, or `single`. Controls how logs are batched and sent.

## Pre-configured Callbacks[​](#pre-configured-callbacks "Direct link to Pre-configured Callbacks")

Use built-in configurations from `generic_api_compatible_callbacks.json`:

```
litellm_settings:
callbacks:["rubrik"]# loads pre-configured settings

callback_settings:
rubrik:
callback_type: generic_api
endpoint: https://your-endpoint.com  # override defaults
headers:
Authorization: Bearer ${RUBRIK_API_KEY}
```

## Payload Format[​](#payload-format "Direct link to Payload Format")

Logs are sent as `StandardLoggingPayload` [objects](https://docs.litellm.ai/docs/proxy/logging_spec) in JSON format:

```
[
{
"id":"chatcmpl-123",
"call_type":"litellm.completion",
"model":"gpt-3.5-turbo",
"messages":[...],
"response":{...},
"usage":{...},
"cost":0.0001,
"startTime":"2024-01-01T00:00:00",
"endTime":"2024-01-01T00:00:01",
"metadata":{...}
}
]
```

## Environment Variables[​](#environment-variables "Direct link to Environment Variables")

Set via environment variables instead of config:

```
export GENERIC_LOGGER_ENDPOINT=https://your-endpoint.com
export GENERIC_LOGGER_HEADERS="Authorization=Bearer token,Custom-Header=value"
```

## Batch Settings[​](#batch-settings "Direct link to Batch Settings")

Control batching behavior (inherits from `CustomBatchLogger`):

```
callback_settings:
my_api:
callback_type: generic_api
endpoint: https://your-endpoint.com
batch_size:100# default: 100
flush_interval:60# seconds, default: 60
```

## Log Format Options[​](#log-format-options "Direct link to Log Format Options")

Control how logs are formatted and sent to your endpoint.

### JSON Array (Default)[​](#json-array-default "Direct link to JSON Array (Default)")

```
callback_settings:
my_api:
callback_type: generic_api
endpoint: https://your-endpoint.com
log_format: json_array  # default if not specified
```

Sends all logs in a batch as a single JSON array `[{log1}, {log2}, ...]`. This is the default behavior and maintains backward compatibility.

**When to use**: Most HTTP endpoints expecting batched JSON data.

### NDJSON (Newline-Delimited JSON)[​](#ndjson-newline-delimited-json "Direct link to NDJSON (Newline-Delimited JSON)")

```
callback_settings:
my_api:
callback_type: generic_api
endpoint: https://your-endpoint.com
log_format: ndjson
```

Sends logs as newline-delimited JSON (one record per line):

**When to use**: Log aggregation services like Sumo Logic, Splunk, or Datadog that support field extraction on individual records.

**Benefits**:

- Each log is ingested as a separate message
- Field Extraction Rules work at ingest time
- Better parsing and querying performance

### Single[​](#single "Direct link to Single")

```
callback_settings:
my_api:
callback_type: generic_api
endpoint: https://your-endpoint.com
log_format: single
```

Sends each log as an individual HTTP request in parallel when the batch is flushed.

**When to use**: Endpoints that expect individual records, or when you need maximum compatibility.

**Note**: This mode sends N HTTP requests per batch (more overhead). Consider using `ndjson` instead if your endpoint supports it.