---
title: Built-in Observability
url: https://docs.getbifrost.ai/features/observability/default.md
source: llms
fetched_at: 2026-01-21T19:43:42.898539634-03:00
rendered_js: false
word_count: 912
summary: This document explains Bifrost's built-in observability system, which provides real-time tracing and performance monitoring for AI requests and responses. It details what data is captured, the asynchronous logging architecture, and how to enable or disable tracing through the UI and API.
tags:
    - observability
    - request-tracing
    - monitoring
    - performance-metrics
    - logging
    - llm-ops
category: guide
---

# Built-in Observability

> Monitor and analyze every AI request and response in real-time. Track performance, debug issues, and gain insights into your AI application's behavior with comprehensive request tracing.

## Overview

Bifrost includes **built-in observability**, a powerful feature that automatically captures and stores detailed information about every AI request and response that flows through your system. This provides structured, searchable data with real-time monitoring capabilities, making it easy to debug issues, analyze performance patterns, and understand your AI application's behavior at scale.

All LLM interactions are captured with comprehensive metadata including inputs, outputs, tokens, costs, and latency. The logging plugin operates **asynchronously** with zero impact on request latency.

<img src="https://mintcdn.com/bifrost/FIVhhIUMerbtYQ0u/media/ui-live-log-stream.gif?s=9a48141da59d5c357498fa35a62f4b16" alt="Live Log Stream Interface" data-og-width="1572" width="1572" data-og-height="1080" height="1080" data-path="media/ui-live-log-stream.gif" data-optimize="true" data-opv="3" />

***

## What's Captured

Bifrost traces comprehensive information for every request, without any changes to your application code.

<img src="https://mintcdn.com/bifrost/pg2nvSfno0tQR_mg/media/ui-request-tracing-overview.png?fit=max&auto=format&n=pg2nvSfno0tQR_mg&q=85&s=9d8ad2ff7ca77f03dc2288641113cf06" alt="Complete Request Tracing Overview" data-og-width="3492" width="3492" data-og-height="2358" height="2358" data-path="media/ui-request-tracing-overview.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/bifrost/pg2nvSfno0tQR_mg/media/ui-request-tracing-overview.png?w=280&fit=max&auto=format&n=pg2nvSfno0tQR_mg&q=85&s=e87577a5875d219abdf4dba15979a69c 280w, https://mintcdn.com/bifrost/pg2nvSfno0tQR_mg/media/ui-request-tracing-overview.png?w=560&fit=max&auto=format&n=pg2nvSfno0tQR_mg&q=85&s=b449bbfe5d39dd14e0d2b30bcd14781f 560w, https://mintcdn.com/bifrost/pg2nvSfno0tQR_mg/media/ui-request-tracing-overview.png?w=840&fit=max&auto=format&n=pg2nvSfno0tQR_mg&q=85&s=ca0eb384f7803701133ff79aed78f7c1 840w, https://mintcdn.com/bifrost/pg2nvSfno0tQR_mg/media/ui-request-tracing-overview.png?w=1100&fit=max&auto=format&n=pg2nvSfno0tQR_mg&q=85&s=71a282d0ddc5bafbdb5925cad1f1b631 1100w, https://mintcdn.com/bifrost/pg2nvSfno0tQR_mg/media/ui-request-tracing-overview.png?w=1650&fit=max&auto=format&n=pg2nvSfno0tQR_mg&q=85&s=99bbd9a5cb4657c5edab55c06a3936f2 1650w, https://mintcdn.com/bifrost/pg2nvSfno0tQR_mg/media/ui-request-tracing-overview.png?w=2500&fit=max&auto=format&n=pg2nvSfno0tQR_mg&q=85&s=e7951ab4f669aec07c45db985a4754b8 2500w" />

### **Request Data**

* **Input Messages**: Complete conversation history and user prompts
* **Model Parameters**: Temperature, max tokens, tools, and all other parameters
* **Provider Context**: Which provider and model handled the request

### **Response Data**

* **Output Messages**: AI responses, tool calls, and function results
* **Performance Metrics**: Latency and token usage
* **Status Information**: Success or error details

### **Multimodal & Tool Support**

* **Audio Processing**: Speech synthesis and transcription inputs/outputs
* **Vision Analysis**: Image URLs and vision model responses
* **Tool Execution**: Function calling arguments and results

<img src="https://mintcdn.com/bifrost/FIVhhIUMerbtYQ0u/media/ui-multimodal-tracing.png?fit=max&auto=format&n=FIVhhIUMerbtYQ0u&q=85&s=54949c0574809ffbc79084076a96672a" alt="Multimodal Request Tracing" data-og-width="3412" width="3412" data-og-height="2278" height="2278" data-path="media/ui-multimodal-tracing.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/bifrost/FIVhhIUMerbtYQ0u/media/ui-multimodal-tracing.png?w=280&fit=max&auto=format&n=FIVhhIUMerbtYQ0u&q=85&s=17724996f3842a18f79a79fbcba6a0b6 280w, https://mintcdn.com/bifrost/FIVhhIUMerbtYQ0u/media/ui-multimodal-tracing.png?w=560&fit=max&auto=format&n=FIVhhIUMerbtYQ0u&q=85&s=15bf7815ca4a5200209981597f039a1f 560w, https://mintcdn.com/bifrost/FIVhhIUMerbtYQ0u/media/ui-multimodal-tracing.png?w=840&fit=max&auto=format&n=FIVhhIUMerbtYQ0u&q=85&s=ccb64fbcc9e3ce29c91a6c53d53d006c 840w, https://mintcdn.com/bifrost/FIVhhIUMerbtYQ0u/media/ui-multimodal-tracing.png?w=1100&fit=max&auto=format&n=FIVhhIUMerbtYQ0u&q=85&s=d2931c2d06eae1a575a1bc958dff8d8a 1100w, https://mintcdn.com/bifrost/FIVhhIUMerbtYQ0u/media/ui-multimodal-tracing.png?w=1650&fit=max&auto=format&n=FIVhhIUMerbtYQ0u&q=85&s=7a957c3f2fac7888f6d669fcd5626f24 1650w, https://mintcdn.com/bifrost/FIVhhIUMerbtYQ0u/media/ui-multimodal-tracing.png?w=2500&fit=max&auto=format&n=FIVhhIUMerbtYQ0u&q=85&s=0d2d24b907a5e0d3d3831de1ad0e81ce 2500w" />

***

## How It Works

The logging plugin intercepts all requests flowing through Bifrost using the plugin architecture, ensuring your LLM requests maintain optimal performance:

1. **PreHook**: Captures request metadata (provider, model, input messages, parameters).
2. **Async Processing**: Logs are written in background goroutines with `sync.Pool` optimization.
3. **PostHook**: Updates log entry with response data (output, tokens, cost, latency, errors).
4. **Real-time Updates**: WebSocket broadcasts keep the UI synchronized.

All logging operations are non-blocking, ensuring your LLM requests maintain optimal performance.

***

## Configuration

Configure request tracing to control what gets logged and where it's stored.

<Tabs group="tracing-config">
  <Tab title="Using Web UI">
        <img src="https://mintcdn.com/bifrost/haPSvjWru9cl-Jd-/media/ui-tracing-config.png?fit=max&auto=format&n=haPSvjWru9cl-Jd-&q=85&s=8be893a785c1d3720c791b75e0f1160a" alt="Tracing Configuration Interface" data-og-width="3492" width="3492" data-og-height="2358" height="2358" data-path="media/ui-tracing-config.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/bifrost/haPSvjWru9cl-Jd-/media/ui-tracing-config.png?w=280&fit=max&auto=format&n=haPSvjWru9cl-Jd-&q=85&s=ef544f23b386f2320ce659a152486dff 280w, https://mintcdn.com/bifrost/haPSvjWru9cl-Jd-/media/ui-tracing-config.png?w=560&fit=max&auto=format&n=haPSvjWru9cl-Jd-&q=85&s=61031b0525ebdeeaa41e83f77f5fe8d4 560w, https://mintcdn.com/bifrost/haPSvjWru9cl-Jd-/media/ui-tracing-config.png?w=840&fit=max&auto=format&n=haPSvjWru9cl-Jd-&q=85&s=71190f8b90a15e65a28365898eaed6ad 840w, https://mintcdn.com/bifrost/haPSvjWru9cl-Jd-/media/ui-tracing-config.png?w=1100&fit=max&auto=format&n=haPSvjWru9cl-Jd-&q=85&s=da03454d9245826469a7afbe647802fe 1100w, https://mintcdn.com/bifrost/haPSvjWru9cl-Jd-/media/ui-tracing-config.png?w=1650&fit=max&auto=format&n=haPSvjWru9cl-Jd-&q=85&s=80035e2f077b8131cedd1632af62e6fc 1650w, https://mintcdn.com/bifrost/haPSvjWru9cl-Jd-/media/ui-tracing-config.png?w=2500&fit=max&auto=format&n=haPSvjWru9cl-Jd-&q=85&s=28e4b204507e0c3779d181ac130413b3 2500w" />

    1. Navigate to **[http://localhost:8080](http://localhost:8080)**
    2. Go to **"Settings"**
    3. Toggle **"Enable Logs"**
  </Tab>

  <Tab title="Using API">
    **Enable/Disable Tracing:**

    ```bash  theme={null}
    curl --location 'http://localhost:8080/api/config' \
    --header 'Content-Type: application/json' \
    --method PUT \
    --data '{
        "client_config": {
            "enable_logging": true,
            "disable_content_logging": false,
            "drop_excess_requests": false,
            "initial_pool_size": 300,
            "enable_governance": true,
            "enforce_governance_header": false,
            "allow_direct_keys": false,
            "prometheus_labels": [],
            "allowed_origins": []
        }
    }'
    ```

    **Check Current Configuration:**

    ```bash  theme={null}
    curl --location 'http://localhost:8080/api/config'
    ```

    **Response includes tracing status:**

    ```json  theme={null}
    {
        "client_config": {
            "enable_logging": true,
            "disable_content_logging": false,
            "drop_excess_requests": false
        },
        "is_db_connected": true,
        "is_cache_connected": true, 
        "is_logs_connected": true
    }
    ```
  </Tab>

  <Tab title="Using config.json">
    In your `config.json` file, you can enable logging and configure the log store:

    ```json  theme={null}
    {
        "client": {
            "enable_logging": true,
            "disable_content_logging": false,
            "drop_excess_requests": false,
            "initial_pool_size": 300,
            "enable_governance": true,
            "allow_direct_keys": false
        },
        "logs_store": {
            "enabled": true,
            "type": "sqlite",
            "config": {
                "path": "./logs.db"
            }
        }
    }
    ```

    * **`enable_logging`**: Master toggle for request tracing.
    * **`disable_content_logging`**: Disable logging of request/response content, but still log usage metadata (latency, cost, token count, etc.).
    * **`logs_store`**: Check [Log Store Options](#log-store-options) for more details.
  </Tab>

  <Tab title="Using Go SDK">
    When using Bifrost as a Go SDK, initialize the logging plugin manually:

    ```go  theme={null}
    package main

    import (
        "context"
        bifrost "github.com/maximhq/bifrost/core"
        "github.com/maximhq/bifrost/core/schemas"
        "github.com/maximhq/bifrost/framework/logstore"
        "github.com/maximhq/bifrost/framework/pricing"
        "github.com/maximhq/bifrost/plugins/logging"
    )

    func main() {
        ctx := context.Background()
        logger := schemas.NewLogger()
        
        // Initialize log store (SQLite)
        store, err := logstore.NewLogStore(ctx, &logstore.Config{
            Enabled: true,
            Type:    logstore.LogStoreTypeSQLite,
            Config: &logstore.SQLiteConfig{
                Path: "./logs.db",
            },
        }, logger)
        if err != nil {
            panic(err)
        }
        
        // Initialize pricing manager (required for cost calculation)
        pricingManager := pricing.NewPricingManager(logger)
        
        // Initialize logging plugin
        loggingPlugin, err := logging.Init(ctx, logger, store, pricingManager)
        if err != nil {
            panic(err)
        }
        
        // Initialize Bifrost with logging plugin
        client, err := bifrost.Init(ctx, schemas.BifrostConfig{
            Account: &yourAccount,
            Plugins: []schemas.Plugin{loggingPlugin},
        })
        if err != nil {
            panic(err)
        }
        defer client.Shutdown()
        
        // All requests are now logged automatically
    }
    ```
  </Tab>
</Tabs>

***

## Accessing & Filtering Logs

Retrieve and analyze logs with powerful filtering capabilities via the UI, API, and WebSockets.

<img src="https://mintlify.s3.us-west-1.amazonaws.com/bifrost/media/ui-log-filtering.gif" alt="Advanced Log Filtering Interface" />

### Web UI

When running the Gateway, access the built-in dashboard at `http://localhost:8080`. The UI provides:

* Real-time log streaming
* Advanced filtering and search
* Detailed request/response inspection
* Token and cost analytics

### API Endpoints

Query logs programmatically using the `GET` request.

```bash  theme={null}
curl 'http://localhost:8080/api/logs?' \
'providers=openai,anthropic&' \
'models=gpt-4o-mini&' \
'status=success,error&' \
'start_time=2024-01-15T00:00:00Z&' \
'end_time=2024-01-15T23:59:59Z&' \
'min_latency=1000&' \
'max_latency=5000&' \
'min_tokens=10&' \
'max_tokens=1000&' \
'min_cost=0.001&' \
'max_cost=10&' \
'content_search=python&' \
'limit=100&' \
'offset=0'
```

**Available Filters:**

| Filter                        | Description               | Example                       |
| ----------------------------- | ------------------------- | ----------------------------- |
| `providers`                   | Filter by AI providers    | `openai,anthropic`            |
| `models`                      | Filter by specific models | `gpt-4o-mini,claude-3-sonnet` |
| `status`                      | Request status            | `success,error,processing`    |
| `objects`                     | Request types             | `chat.completion,embedding`   |
| `start_time` / `end_time`     | Time range (RFC3339)      | `2024-01-15T10:00:00Z`        |
| `min_latency` / `max_latency` | Response time (ms)        | `1000` to `5000`              |
| `min_tokens` / `max_tokens`   | Token usage range         | `10` to `1000`                |
| `min_cost` / `max_cost`       | Cost range (USD)          | `0.001` to `10`               |
| `content_search`              | Search in messages        | `"error handling"`            |
| `limit` / `offset`            | Pagination                | `100`, `200`                  |

**Response Format**

```json  theme={null}
{
    "logs": [...],
    "pagination": {
        "limit": 100,
        "offset": 0,
        "sort_by": "timestamp",
        "order": "desc"
    },
    "stats": {
        "total_requests": 1234,
        "success_rate": 0.85,
        "average_latency": 100,
        "total_tokens": 10000,
        "total_cost": 100
    }
}
```

Perfect for analytics, debugging specific issues, or building custom monitoring dashboards.

### WebSocket

Subscribe to real-time log updates for live monitoring:

```javascript  theme={null}
const ws = new WebSocket('ws://localhost:8080/ws')

ws.onmessage = (event) => {
  const logUpdate = JSON.parse(event.data)
  console.log('New log entry:', logUpdate)
}
```

***

## Log Store Options

Choose the right storage backend for your scale and requirements.

The logging plugin is **automatically enabled** in Gateway mode with SQLite storage by default. You can configure it to use PostgreSQL by setting the `logs_store` configuration in your `config.json` file.

### **Current Support**

<Tabs group="log-store-types">
  <Tab title="SQLite (Default)">
    * **Best for**: Development, small-medium deployments
    * **Performance**: Excellent for read-heavy workloads
    * **Setup**: Zero configuration, single file storage
    * **Limits**: Single-writer, local filesystem only

    ```json  theme={null}
    {
        "logs_store": {
            "enabled": true,
            "type": "sqlite",
            "config": {
                "path": "./logs.db"
            }
        }
    }
    ```
  </Tab>

  <Tab title="PostgreSQL">
    * **Best for**: High-volume production deployments
    * **Performance**: Excellent concurrent writes and complex queries
    * **Features**: Advanced indexing, partitioning, replication

    ```json  theme={null}
    {
        "logs_store": {
            "enabled": true,
            "type": "postgres",
            "config": {
                "host": "localhost",
                "port": "5432",
                "user": "bifrost",
                "password": "postgres",
                "db_name": "bifrost",
                "ssl_mode": "disable"
            }
        }
    }
    ```
  </Tab>
</Tabs>

### **Planned Support**

* **MySQL**: For traditional MySQL environments.
* **ClickHouse**: For large-scale analytics and time-series workloads.

***

## Supported Request Types

The logging plugin captures all Bifrost request types:

* Text Completion (streaming and non-streaming)
* Chat Completion (streaming and non-streaming)
* Responses (streaming and non-streaming)
* Embeddings
* Speech Generation (streaming and non-streaming)
* Transcription (streaming and non-streaming)

***

## When to Use

### Built-in Observability

Use the built-in logging plugin for:

* **Local Development**: Quick setup with SQLite, no external dependencies
* **Self-hosted Deployments**: Full control over your data with PostgreSQL
* **Simple Use Cases**: Basic monitoring and debugging needs
* **Privacy-sensitive Workloads**: Keep all logs on your infrastructure

### vs. Maxim Plugin

Switch to the [Maxim plugin](./maxim) for:

* Advanced evaluation and testing workflows
* Prompt engineering and experimentation
* Multi-team governance and collaboration
* Production monitoring with alerts and SLAs
* Dataset management and annotation pipelines

### vs. OTel Plugin

Switch to the [OTel plugin](./otel) for:

* Integration with existing observability infrastructure
* Correlation with application traces and metrics
* Custom collector configurations
* Compliance and enterprise requirements

***

## Performance

The logging plugin is designed for **zero-impact observability**:

* **Async Operations**: All database writes happen in background goroutines
* **Sync.Pool**: Reuses memory allocations for LogMessage and UpdateLogData structs
* **Batch Processing**: Efficiently handles high request volumes
* **Automatic Cleanup**: Removes stale processing logs every 30 seconds

In benchmarks, the logging plugin adds **\< 0.1ms overhead** to request processing time.

***

## Next Steps

* **[Maxim Plugin](./maxim)** - Advanced observability with evaluation and monitoring
* **[OTel Plugin](./otel)** - OpenTelemetry integration for distributed tracing
* **[Gateway Setup](../../quickstart/gateway/setting-up)** - Get Bifrost running with tracing enabled
* **[Provider Configuration](../../quickstart/gateway/provider-configuration)** - Configure multiple providers for better insights
* **[Telemetry](../telemetry)** - Prometheus metrics and dashboards
* **[Governance](../governance)** - Virtual keys and usage limits


---

> To find navigation and other pages in this documentation, fetch the llms.txt file at: https://docs.getbifrost.ai/llms.txt