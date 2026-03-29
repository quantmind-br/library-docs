---
title: Datadog
url: https://docs.getbifrost.ai/enterprise/datadog-connector.md
source: llms
fetched_at: 2026-01-21T19:43:26.185333285-03:00
rendered_js: false
word_count: 1752
summary: This document provides a guide for integrating and configuring the Datadog plugin to monitor LLM operations using APM traces, metrics, and native LLM observability. It details the setup for both agent-based and agentless deployment modes along with a complete reference of configuration parameters.
tags:
    - datadog
    - observability
    - apm-traces
    - llm-monitoring
    - metrics
    - configuration
    - deployment-modes
category: guide
---

# Datadog

> Native Datadog integration for APM traces, LLM Observability, and metrics

## Overview

<Frame>
  <img src="https://mintcdn.com/bifrost/HE3esZlo6PW0-gsx/media/dd-trace.png?fit=max&auto=format&n=HE3esZlo6PW0-gsx&q=85&s=0cdb006e115843fd17c76077b219fc2e" alt="Datadog LLM Observability dashboard" data-og-width="2200" width="2200" data-og-height="1218" height="1218" data-path="media/dd-trace.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/bifrost/HE3esZlo6PW0-gsx/media/dd-trace.png?w=280&fit=max&auto=format&n=HE3esZlo6PW0-gsx&q=85&s=838f28d230a2046b4c6e0c1cc7a6b2e9 280w, https://mintcdn.com/bifrost/HE3esZlo6PW0-gsx/media/dd-trace.png?w=560&fit=max&auto=format&n=HE3esZlo6PW0-gsx&q=85&s=c03031f579fcf74cce6784bbe712492f 560w, https://mintcdn.com/bifrost/HE3esZlo6PW0-gsx/media/dd-trace.png?w=840&fit=max&auto=format&n=HE3esZlo6PW0-gsx&q=85&s=c4c0e38eaf1e33779abf0289edd6e899 840w, https://mintcdn.com/bifrost/HE3esZlo6PW0-gsx/media/dd-trace.png?w=1100&fit=max&auto=format&n=HE3esZlo6PW0-gsx&q=85&s=77228a36d1734b4cbc2cacf6669f9b96 1100w, https://mintcdn.com/bifrost/HE3esZlo6PW0-gsx/media/dd-trace.png?w=1650&fit=max&auto=format&n=HE3esZlo6PW0-gsx&q=85&s=d1e800f9ecd8e745f260c43338272f2f 1650w, https://mintcdn.com/bifrost/HE3esZlo6PW0-gsx/media/dd-trace.png?w=2500&fit=max&auto=format&n=HE3esZlo6PW0-gsx&q=85&s=e8cf2a810a2a50f061d046edd5201025 2500w" />
</Frame>

The **Datadog plugin** provides native integration with the Datadog observability platform, offering three pillars of observability for your LLM operations:

* **APM Traces** - Distributed tracing via dd-trace-go v2 with W3C Trace Context support for end-to-end request visibility
* **LLM Observability** - Native Datadog LLM Obs integration for AI/ML-specific monitoring
* **Metrics** - Operational metrics via DogStatsD or the Metrics API

Unlike the [OTel plugin](/features/observability/otel) which sends generic OpenTelemetry data, the Datadog plugin leverages Datadog's native SDKs for richer integration with Datadog-specific features like LLM Observability dashboards and ML App grouping.

***

## Deployment Modes

<Frame>
  <img src="https://mintcdn.com/bifrost/HE3esZlo6PW0-gsx/media/dd-mode.png?fit=max&auto=format&n=HE3esZlo6PW0-gsx&q=85&s=c907bef2a9c33c241a04572ec73723c6" alt="Datadog LLM Observability dashboard" data-og-width="2294" width="2294" data-og-height="1086" height="1086" data-path="media/dd-mode.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/bifrost/HE3esZlo6PW0-gsx/media/dd-mode.png?w=280&fit=max&auto=format&n=HE3esZlo6PW0-gsx&q=85&s=e35590376ddb79c50512935924159b95 280w, https://mintcdn.com/bifrost/HE3esZlo6PW0-gsx/media/dd-mode.png?w=560&fit=max&auto=format&n=HE3esZlo6PW0-gsx&q=85&s=2697bdf7d32e8ddc553564127ffa0aa4 560w, https://mintcdn.com/bifrost/HE3esZlo6PW0-gsx/media/dd-mode.png?w=840&fit=max&auto=format&n=HE3esZlo6PW0-gsx&q=85&s=944a1b2c67cf6786667cffa622853540 840w, https://mintcdn.com/bifrost/HE3esZlo6PW0-gsx/media/dd-mode.png?w=1100&fit=max&auto=format&n=HE3esZlo6PW0-gsx&q=85&s=dbb0d6aad0b788f94f53ecba0bf95541 1100w, https://mintcdn.com/bifrost/HE3esZlo6PW0-gsx/media/dd-mode.png?w=1650&fit=max&auto=format&n=HE3esZlo6PW0-gsx&q=85&s=5f8044c4dd0243b88ffee8b469723ade 1650w, https://mintcdn.com/bifrost/HE3esZlo6PW0-gsx/media/dd-mode.png?w=2500&fit=max&auto=format&n=HE3esZlo6PW0-gsx&q=85&s=8c8262a70fad6e82f7e6c4faaa904b15 2500w" />
</Frame>

The plugin supports two deployment modes:

| Mode                | Description                              | Requirements                  | Best For                                                  |
| ------------------- | ---------------------------------------- | ----------------------------- | --------------------------------------------------------- |
| **Agent** (default) | Sends data through a local Datadog Agent | Datadog Agent running on host | Production deployments with existing agent infrastructure |
| **Agentless**       | Sends data directly to Datadog APIs      | API key only                  | Serverless, containers, or simplified deployments         |

### Agent Mode

In agent mode, the plugin communicates with a locally running Datadog Agent:

* **APM Traces** → Agent at `localhost:8126`
* **Metrics** → DogStatsD at `localhost:8125`

The agent handles batching, retries, and provides lower latency. This is the recommended mode for production deployments where you already have the Datadog Agent installed.

### Agentless Mode

In agentless mode, the plugin sends data directly to Datadog's intake APIs:

* **APM Traces** → `https://trace.agent.{site}`
* **LLM Observability** → Direct API submission
* **Metrics** → Datadog Metrics API

This mode requires an API key but simplifies deployment by eliminating the need for a local agent. Ideal for serverless environments, Kubernetes pods, or quick testing.

***

## Configuration

### Required Fields

| Field            | Type     | Required       | Default               | Description                                        |
| ---------------- | -------- | -------------- | --------------------- | -------------------------------------------------- |
| `service_name`   | `string` | No             | `bifrost`             | Service name displayed in Datadog APM              |
| `ml_app`         | `string` | No             | (uses `service_name`) | ML application name for LLM Observability grouping |
| `agent_addr`     | `string` | No             | `localhost:8126`      | Datadog Agent address (agent mode only)            |
| `dogstatsd_addr` | `string` | No             | `localhost:8125`      | DogStatsD server address (agent mode only)         |
| `env`            | `string` | No             | -                     | Environment tag (e.g., `production`, `staging`)    |
| `version`        | `string` | No             | -                     | Service version tag                                |
| `custom_tags`    | `object` | No             | -                     | Additional tags for all traces and metrics         |
| `enable_metrics` | `bool`   | No             | `true`                | Enable metrics emission                            |
| `enable_traces`  | `bool`   | No             | `true`                | Enable APM traces                                  |
| `enable_llm_obs` | `bool`   | No             | `true`                | Enable LLM Observability                           |
| `agentless`      | `bool`   | No             | `false`               | Use agentless mode (direct API)                    |
| `api_key`        | `EnvVar` | Agentless only | -                     | Datadog API key (supports `env.VAR_NAME`)          |
| `site`           | `string` | No             | `datadoghq.com`       | Datadog site/region                                |

### Environment Variable Substitution

The `api_key` and `custom_tags` fields support environment variable substitution using the `env.` prefix:

```json  theme={null}
{
  "api_key": "env.DD_API_KEY",
  "custom_tags": {
    "team": "env.TEAM_NAME",
    "cost_center": "env.COST_CENTER"
  }
}
```

***

## Setup

<Tabs group="setup-method">
  <Tab title="UI">
    <Frame>
      <img src="https://mintcdn.com/bifrost/HE3esZlo6PW0-gsx/media/dd-config-page.png?fit=max&auto=format&n=HE3esZlo6PW0-gsx&q=85&s=8894478ffe39d1b749407276a7721796" alt="Datadog LLM Observability dashboard" data-og-width="3504" width="3504" data-og-height="2130" height="2130" data-path="media/dd-config-page.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/bifrost/HE3esZlo6PW0-gsx/media/dd-config-page.png?w=280&fit=max&auto=format&n=HE3esZlo6PW0-gsx&q=85&s=4aa48655214d1856064afae4586bd8ef 280w, https://mintcdn.com/bifrost/HE3esZlo6PW0-gsx/media/dd-config-page.png?w=560&fit=max&auto=format&n=HE3esZlo6PW0-gsx&q=85&s=fd65fc32d86316b241d1cb25c1b5a2ae 560w, https://mintcdn.com/bifrost/HE3esZlo6PW0-gsx/media/dd-config-page.png?w=840&fit=max&auto=format&n=HE3esZlo6PW0-gsx&q=85&s=3d7c802fbba6e9341336bddf4d3bfc9b 840w, https://mintcdn.com/bifrost/HE3esZlo6PW0-gsx/media/dd-config-page.png?w=1100&fit=max&auto=format&n=HE3esZlo6PW0-gsx&q=85&s=d27ede66db408f8633e47daba051678e 1100w, https://mintcdn.com/bifrost/HE3esZlo6PW0-gsx/media/dd-config-page.png?w=1650&fit=max&auto=format&n=HE3esZlo6PW0-gsx&q=85&s=c186e29bff29e1c91008a0e9b87c33e2 1650w, https://mintcdn.com/bifrost/HE3esZlo6PW0-gsx/media/dd-config-page.png?w=2500&fit=max&auto=format&n=HE3esZlo6PW0-gsx&q=85&s=12e7ea85972cd39e9c6446e65ebaf6ec 2500w" />
    </Frame>

    Configure the Datadog plugin through the Bifrost UI:

    1. Navigate to **Settings** → **Plugins**
    2. Enable the **Datadog** plugin
    3. Configure the required fields based on your deployment mode
  </Tab>

  <Tab title="Go SDK">
    ```go  theme={null}
    package main

    import (
        "context"
        bifrost "github.com/maximhq/bifrost/core"
        "github.com/maximhq/bifrost/core/schemas"
        "github.com/maximhq/bifrost/framework/modelcatalog"
        datadog "github.com/maximhq/bifrost-enterprise/plugins/datadog"
    )

    func main() {
        ctx := context.Background()
        logger := schemas.NewLogger()
        
        // Initialize model catalog (required for cost calculation)
        modelCatalog := modelcatalog.NewModelCatalog(logger)
        
        // Agent mode configuration
        ddPlugin, err := datadog.Init(ctx, &datadog.Config{
            ServiceName: "my-llm-service",
            Env:         "production",
            Version:     "1.0.0",
            CustomTags: map[string]string{
                "team": "platform",
            },
        }, logger, modelCatalog, "1.0.0")
        if err != nil {
            panic(err)
        }
        
        // Initialize Bifrost with the plugin
        client, err := bifrost.Init(ctx, schemas.BifrostConfig{
            Account: &yourAccount,
            Plugins: []schemas.Plugin{ddPlugin},
        })
        if err != nil {
            panic(err)
        }
        defer client.Shutdown()
        
        // All requests are now traced to Datadog
    }
    ```

    For agentless mode:

    ```go  theme={null}
    // Agentless mode configuration
    enableAgentless := true
    ddPlugin, err := datadog.Init(ctx, &datadog.Config{
        ServiceName: "my-llm-service",
        Env:         "production",
        Agentless:   &enableAgentless,
        APIKey:      &schemas.EnvVar{EnvVarName: "DD_API_KEY"},
        Site:        "datadoghq.com",
    }, logger, modelCatalog, "1.0.0")
    ```
  </Tab>

  <Tab title="config.json">
    ### Agent Mode (Minimal)

    ```json  theme={null}
    {
      "plugins": [
        {
          "enabled": true,
          "name": "datadog",
          "config": {
            "service_name": "bifrost",
            "env": "production"
          }
        }
      ]
    }
    ```

    ### Agent Mode (Full Configuration)

    ```json  theme={null}
    {
      "plugins": [
        {
          "enabled": true,
          "name": "datadog",
          "config": {
            "service_name": "my-llm-gateway",
            "ml_app": "my-ml-application",
            "agent_addr": "localhost:8126",
            "dogstatsd_addr": "localhost:8125",
            "env": "production",
            "version": "1.2.3",
            "custom_tags": {
              "team": "platform",
              "cost_center": "env.COST_CENTER"
            },
            "enable_metrics": true,
            "enable_traces": true,
            "enable_llm_obs": true
          }
        }
      ]
    }
    ```

    ### Agentless Mode

    ```json  theme={null}
    {
      "plugins": [
        {
          "enabled": true,
          "name": "datadog",
          "config": {
            "service_name": "my-llm-gateway",
            "env": "production",
            "agentless": true,
            "api_key": "env.DD_API_KEY",
            "site": "datadoghq.com"
          }
        }
      ]
    }
    ```

    Set the environment variable:

    ```bash  theme={null}
    export DD_API_KEY="your-datadog-api-key"
    ```
  </Tab>
</Tabs>

***

## Datadog Sites

The plugin supports all Datadog regional sites. Set the `site` field to match your Datadog account region:

| Site          | Region                   | Value               |
| ------------- | ------------------------ | ------------------- |
| US1 (default) | United States            | `datadoghq.com`     |
| US3           | United States            | `us3.datadoghq.com` |
| US5           | United States            | `us5.datadoghq.com` |
| EU1           | Europe                   | `datadoghq.eu`      |
| AP1           | Asia Pacific (Japan)     | `ap1.datadoghq.com` |
| AP2           | Asia Pacific (Australia) | `ap2.datadoghq.com` |
| US1-FED       | US Government            | `ddog-gov.com`      |

<Note>
  Ensure your API key corresponds to the selected site. API keys from one region will not work with another.
</Note>

***

## LLM Observability

<Frame>
  <img src="https://mintcdn.com/bifrost/HE3esZlo6PW0-gsx/media/dd-llmobs.png?fit=max&auto=format&n=HE3esZlo6PW0-gsx&q=85&s=293326662ec84536b8fd6f2c35be2db7" alt="Datadog LLM Observability dashboard" data-og-width="3504" width="3504" data-og-height="2126" height="2126" data-path="media/dd-llmobs.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/bifrost/HE3esZlo6PW0-gsx/media/dd-llmobs.png?w=280&fit=max&auto=format&n=HE3esZlo6PW0-gsx&q=85&s=55a0e56b6a8d5c72219477c2facea251 280w, https://mintcdn.com/bifrost/HE3esZlo6PW0-gsx/media/dd-llmobs.png?w=560&fit=max&auto=format&n=HE3esZlo6PW0-gsx&q=85&s=824c531267ceb1db09a4b24837885a3f 560w, https://mintcdn.com/bifrost/HE3esZlo6PW0-gsx/media/dd-llmobs.png?w=840&fit=max&auto=format&n=HE3esZlo6PW0-gsx&q=85&s=d2edae7488796f1f9461d184a30ca151 840w, https://mintcdn.com/bifrost/HE3esZlo6PW0-gsx/media/dd-llmobs.png?w=1100&fit=max&auto=format&n=HE3esZlo6PW0-gsx&q=85&s=8e68f6fdece669e0c56644880f82232f 1100w, https://mintcdn.com/bifrost/HE3esZlo6PW0-gsx/media/dd-llmobs.png?w=1650&fit=max&auto=format&n=HE3esZlo6PW0-gsx&q=85&s=29ca525f6147ad1161b8f418fa8506b7 1650w, https://mintcdn.com/bifrost/HE3esZlo6PW0-gsx/media/dd-llmobs.png?w=2500&fit=max&auto=format&n=HE3esZlo6PW0-gsx&q=85&s=30cc4b4c88a336914f917c9afea3d577 2500w" />
</Frame>

The Datadog plugin integrates with [Datadog LLM Observability](https://docs.datadoghq.com/llm_observability/) to provide AI/ML-specific monitoring capabilities.

### ML App Grouping

LLM traces are grouped under an **ML App** in Datadog. By default, this uses your `service_name`, but you can specify a dedicated ML App name:

```json  theme={null}
{
  "service_name": "bifrost-gateway",
  "ml_app": "customer-support-ai"
}
```

This allows you to:

* Group related LLM operations across multiple services
* Track costs and performance by application
* Apply ML-specific alerts and dashboards

### Session Tracking

The plugin supports session tracking via the `x-bf-session-id` header. Include this header in your requests to group related LLM calls into a conversation session:

```bash  theme={null}
curl -X POST https://your-bifrost-gateway/v1/chat/completions \
  -H "Authorization: Bearer $API_KEY" \
  -H "x-bf-session-id: user-123-session-456" \
  -d '{...}'
```

Sessions appear in Datadog LLM Observability, allowing you to trace entire conversation flows.

### W3C Distributed Tracing

The plugin supports [W3C Trace Context](https://www.w3.org/TR/trace-context/) for distributed tracing across services. When your upstream service sends a `traceparent` header, Bifrost automatically links its spans as children of the parent trace.

```bash  theme={null}
curl -X POST https://your-bifrost-gateway/v1/chat/completions \
  -H "Authorization: Bearer $API_KEY" \
  -H "traceparent: 00-0af7651916cd43dd8448eb211c80319c-b7ad6b7169203331-01" \
  -d '{...}'
```

This enables:

* **End-to-end visibility** - See LLM calls in the context of your full application trace
* **Cross-service correlation** - Link frontend requests → backend services → Bifrost → LLM providers
* **Latency attribution** - Understand how LLM latency contributes to overall request time

The `traceparent` header format follows the W3C standard:

```
traceparent: {version}-{trace-id}-{parent-id}-{trace-flags}
```

All Datadog APM spans created by Bifrost will be linked to the parent span, appearing as children in the Datadog trace view.

### What's Captured

For each LLM operation, the plugin sends to LLM Observability:

* **Input/Output Messages** - Full conversation history with role attribution
* **Token Usage** - Input, output, and total token counts
* **Cost** - Calculated cost in USD based on model pricing
* **Latency** - Request duration and time-to-first-token for streaming
* **Model Info** - Provider, model name, and request parameters
* **Tool Calls** - Function/tool call details for agentic workflows

***

## Metrics Reference

The plugin emits the following metrics to Datadog:

| Metric                               | Type      | Description                        | Tags                                   |
| ------------------------------------ | --------- | ---------------------------------- | -------------------------------------- |
| `bifrost.requests.total`             | Counter   | Total LLM requests                 | provider, model, request\_type         |
| `bifrost.success.total`              | Counter   | Successful requests                | provider, model, request\_type         |
| `bifrost.errors.total`               | Counter   | Failed requests                    | provider, model, request\_type, reason |
| `bifrost.latency.seconds`            | Histogram | Request latency distribution       | provider, model, request\_type         |
| `bifrost.tokens.input`               | Counter   | Input/prompt tokens consumed       | provider, model                        |
| `bifrost.tokens.output`              | Counter   | Output/completion tokens generated | provider, model                        |
| `bifrost.tokens.total`               | Counter   | Total tokens (input + output)      | provider, model                        |
| `bifrost.cost.usd`                   | Gauge     | Request cost in USD                | provider, model                        |
| `bifrost.cache.hits`                 | Counter   | Cache hits                         | provider, model, cache\_type           |
| `bifrost.stream.first_token_latency` | Histogram | Time to first token (streaming)    | provider, model                        |
| `bifrost.stream.inter_token_latency` | Histogram | Inter-token latency (streaming)    | provider, model                        |

### Custom Tags

All metrics include your configured `custom_tags` plus automatic tags for:

* `provider` - LLM provider (openai, anthropic, etc.)
* `model` - Model name
* `request_type` - Type of request (chat, embedding, etc.)
* `env` - Environment from configuration

***

## Captured Data

Each APM trace includes comprehensive LLM operation metadata:

### Span Attributes

* **Span Name** - Based on request type (`genai.chat`, `genai.embedding`, etc.)
* **Service Info** - `service.name`, `service.version`, `env`
* **Provider & Model** - `gen_ai.provider.name`, `gen_ai.request.model`

### Request Parameters

* Temperature, max\_tokens, top\_p, stop sequences
* Presence/frequency penalties
* Tool configurations and parallel tool calls
* Custom parameters via `ExtraParams`

### Input/Output Data

* Complete chat history with role-based messages
* Prompt text for completions
* Response content with role attribution
* Tool calls and results
* Reasoning and refusal content (when present)

### Performance Metrics

* Token usage (prompt, completion, total)
* Cost calculations in USD
* Latency and timing (start/end timestamps)
* Time to first token (streaming)
* Error details with status codes

### Bifrost Context

* Virtual key ID and name
* Selected key ID and name
* Team ID and name
* Customer ID and name
* Retry count and fallback index

***

## Supported Request Types

The Datadog plugin captures all Bifrost request types:

| Request Type                  | Span Name             | LLM Obs Type   |
| ----------------------------- | --------------------- | -------------- |
| Chat Completion               | `genai.chat`          | LLM Span       |
| Chat Completion (streaming)   | `genai.chat`          | LLM Span       |
| Text Completion               | `genai.text`          | LLM Span       |
| Text Completion (streaming)   | `genai.text`          | LLM Span       |
| Embeddings                    | `genai.embedding`     | Embedding Span |
| Speech Generation             | `genai.speech`        | Task Span      |
| Speech Generation (streaming) | `genai.speech`        | Task Span      |
| Transcription                 | `genai.transcription` | Task Span      |
| Transcription (streaming)     | `genai.transcription` | Task Span      |
| Responses API                 | `genai.responses`     | LLM Span       |
| Responses API (streaming)     | `genai.responses`     | LLM Span       |

***

## When to Use

### Datadog Plugin

Choose the Datadog plugin when you:

* Use Datadog as your primary observability platform
* Want native LLM Observability integration with ML App grouping
* Need seamless correlation with existing Datadog APM traces via W3C distributed tracing
* Require Datadog-specific features like notebooks and dashboards
* Want session tracking for conversation flows

### vs. OTel Plugin

Use the [OTel plugin](/features/observability/otel) when you:

* Need multi-vendor observability (send to multiple backends)
* Are using Datadog via an OpenTelemetry Collector
* Want vendor flexibility to switch backends without code changes
* Prefer standardized OpenTelemetry semantic conventions

<Note>
  You can use both plugins simultaneously if needed. The Datadog plugin provides native integration while OTel can send to additional backends.
</Note>

### vs. Built-in Observability

Use [Built-in Observability](/features/observability/default) for:

* Local development and testing
* Simple self-hosted deployments
* No external dependencies required
* Direct database access to logs

***

## Troubleshooting

### Agent Connectivity Issues

Verify the Datadog Agent is running and accessible:

```bash  theme={null}
# Check agent status
datadog-agent status

# Test APM endpoint
curl -v http://localhost:8126/info

# Test DogStatsD (should accept UDP packets)
echo "test.metric:1|c" | nc -u -w1 localhost 8125
```

### Agentless Mode Not Working

1. Verify your API key is valid:

```bash  theme={null}
curl -X GET "https://api.datadoghq.com/api/v1/validate" \
  -H "DD-API-KEY: $DD_API_KEY"
```

2. Ensure the `site` matches your API key's region

3. Check that the API key environment variable is set:

```bash  theme={null}
echo $DD_API_KEY
```

### Missing Traces

1. Enable debug logging in Bifrost:

```bash  theme={null}
bifrost-http --log-level debug
```

2. Verify traces are enabled in your configuration:

```json  theme={null}
{
  "enable_traces": true,
  "enable_llm_obs": true
}
```

3. Check for errors in the Bifrost logs related to the Datadog plugin

### Missing Metrics

1. Verify DogStatsD is running (agent mode):

```bash  theme={null}
datadog-agent status | grep DogStatsD
```

2. Ensure metrics are enabled:

```json  theme={null}
{
  "enable_metrics": true
}
```

3. For agentless mode, verify your API key has metrics submission permissions

### LLM Observability Not Appearing

1. LLM Observability requires `enable_llm_obs: true` (default)
2. Verify your Datadog plan includes LLM Observability
3. Check the ML App name in Datadog under **LLM Observability** → **Applications**

***

## Next Steps

* **[OTel Plugin](/features/observability/otel)** - OpenTelemetry integration for multi-vendor observability
* **[Built-in Observability](/features/observability/default)** - Local logging for development
* **[Telemetry](/features/telemetry)** - Prometheus metrics and dashboards


---

> To find navigation and other pages in this documentation, fetch the llms.txt file at: https://docs.getbifrost.ai/llms.txt