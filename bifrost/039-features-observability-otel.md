---
title: OpenTelemetry (OTel)
url: https://docs.getbifrost.ai/features/observability/otel.md
source: llms
fetched_at: 2026-01-21T19:43:46.454980514-03:00
rendered_js: false
word_count: 958
summary: This document explains how to integrate Bifrost with OpenTelemetry collectors to enable distributed tracing and observability for LLM operations using various trace formats.
tags:
    - opentelemetry
    - otel
    - distributed-tracing
    - observability
    - monitoring
    - tracing-plugin
category: configuration
---

# OpenTelemetry (OTel)

> Integrate with OpenTelemetry collectors for enterprise observability and distributed tracing

## Overview

<Frame>
  <img src="https://mintcdn.com/bifrost/HE3esZlo6PW0-gsx/media/grafana-otel-traces.png?fit=max&auto=format&n=HE3esZlo6PW0-gsx&q=85&s=59f4d1f541a4ff90c8c3a9949de316a4" alt="Okta Applications page" data-og-width="2196" width="2196" data-og-height="1214" height="1214" data-path="media/grafana-otel-traces.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/bifrost/HE3esZlo6PW0-gsx/media/grafana-otel-traces.png?w=280&fit=max&auto=format&n=HE3esZlo6PW0-gsx&q=85&s=256b07b5c87932063fbf4d44cd8cfcb0 280w, https://mintcdn.com/bifrost/HE3esZlo6PW0-gsx/media/grafana-otel-traces.png?w=560&fit=max&auto=format&n=HE3esZlo6PW0-gsx&q=85&s=a63c81ac56bc15a76da5d59f37b1a67f 560w, https://mintcdn.com/bifrost/HE3esZlo6PW0-gsx/media/grafana-otel-traces.png?w=840&fit=max&auto=format&n=HE3esZlo6PW0-gsx&q=85&s=b2bc5757ef1d7714a07a1e944fb140ce 840w, https://mintcdn.com/bifrost/HE3esZlo6PW0-gsx/media/grafana-otel-traces.png?w=1100&fit=max&auto=format&n=HE3esZlo6PW0-gsx&q=85&s=653cd0cd76576cd9a7cb944f84d1a721 1100w, https://mintcdn.com/bifrost/HE3esZlo6PW0-gsx/media/grafana-otel-traces.png?w=1650&fit=max&auto=format&n=HE3esZlo6PW0-gsx&q=85&s=cde889056c84791e490419d12861d611 1650w, https://mintcdn.com/bifrost/HE3esZlo6PW0-gsx/media/grafana-otel-traces.png?w=2500&fit=max&auto=format&n=HE3esZlo6PW0-gsx&q=85&s=db620b9ba5a580c1b5a23ff88178c9aa 2500w" />
</Frame>

The **OTel plugin** enables seamless integration with OpenTelemetry Protocol (OTLP) collectors, allowing you to send LLM traces to your existing observability infrastructure. Connect Bifrost to platforms like Grafana Cloud, Datadog, New Relic, Honeycomb, or self-hosted collectors.

All traces follow OpenTelemetry semantic conventions, making it easy to correlate LLM operations with your broader application telemetry.

***

## Supported Trace Formats

The plugin supports multiple trace formats to match your observability platform:

| Format            | Description                              | Use Case                                                      | Status         |
| ----------------- | ---------------------------------------- | ------------------------------------------------------------- | -------------- |
| `genai_extension` | OpenTelemetry GenAI semantic conventions | **Recommended** - Standard OTel format with rich LLM metadata | ✅ Released     |
| `vercel`          | Vercel AI SDK format                     | For Vercel AI SDK compatibility                               | 🔄 Coming soon |
| `open_inference`  | Arize OpenInference format               | For Arize Phoenix and OpenInference tools                     | 🔄 Coming soon |

***

## Configuration

### Required Fields

| Field           | Type     | Required | Description                                                                                  |
| --------------- | -------- | -------- | -------------------------------------------------------------------------------------------- |
| `service_name`  | `string` | ❌ No     | Service name to be used for tracing, defaults to `bifrost`                                   |
| `collector_url` | `string` | ✅ Yes    | OTLP collector endpoint URL                                                                  |
| `trace_type`    | `string` | ✅ Yes    | One of: `genai_extension`, `vercel`, `open_inference`                                        |
| `protocol`      | `string` | ✅ Yes    | Transport protocol: `http` or `grpc`                                                         |
| `headers`       | `object` | ❌ No     | Custom headers for authentication (supports `env.VAR_NAME`)                                  |
| `tls_ca_cert`   | `string` | ❌ No     | File path to client CA certificate for TLS. Optional. Works with both gRPC and HTTP protocol |

### Environment Variable Substitution

Headers support environment variable substitution using the `env.` prefix:

```json  theme={null}
{
  "headers": {
    "Authorization": "env.OTEL_API_KEY",
    "X-Custom-Header": "env.CUSTOM_VALUE"
  }
}
```

### Resource Attributes

The plugin supports the standard `OTEL_RESOURCE_ATTRIBUTES` environment variable. Any attributes defined in this variable will be automatically attached to every span emitted by the plugin.

```bash  theme={null}
export OTEL_RESOURCE_ATTRIBUTES="deployment.environment=production,service.version=1.2.3,team.name=platform"
```

These attributes appear as resource-level metadata on all traces:

```json  theme={null}
{
  "resource": {
    "attributes": {
      "service.name": "bifrost",
      "deployment.environment": "production",
      "service.version": "1.2.3",
      "team.name": "platform"
    }
  }
}
```

This is useful for:

* **Environment identification** - Distinguish between production, staging, and development traces
* **Service versioning** - Track which version of your service generated the trace
* **Team attribution** - Tag traces with team ownership for filtering and alerting
* **Custom metadata** - Add any key-value pairs relevant to your observability needs

***

## Setup

<Tabs group="setup-method">
  <Tab title="UI">
        <img src="https://mintcdn.com/bifrost/pMEtHOAW182_aOFs/media/otel-ui-setup.png?fit=max&auto=format&n=pMEtHOAW182_aOFs&q=85&s=0282ac132402686f6ce3febeac6ae6db" alt="Otel UI setup" data-og-width="2140" width="2140" data-og-height="936" height="936" data-path="media/otel-ui-setup.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/bifrost/pMEtHOAW182_aOFs/media/otel-ui-setup.png?w=280&fit=max&auto=format&n=pMEtHOAW182_aOFs&q=85&s=cd961a18df123dfc26e8de6dbd9a4b59 280w, https://mintcdn.com/bifrost/pMEtHOAW182_aOFs/media/otel-ui-setup.png?w=560&fit=max&auto=format&n=pMEtHOAW182_aOFs&q=85&s=32ed32c2cb2986eba86eb1473478e315 560w, https://mintcdn.com/bifrost/pMEtHOAW182_aOFs/media/otel-ui-setup.png?w=840&fit=max&auto=format&n=pMEtHOAW182_aOFs&q=85&s=0665ed14cbb19270960350611efaaddd 840w, https://mintcdn.com/bifrost/pMEtHOAW182_aOFs/media/otel-ui-setup.png?w=1100&fit=max&auto=format&n=pMEtHOAW182_aOFs&q=85&s=575ebfffb693caf661bf43c133d09dfd 1100w, https://mintcdn.com/bifrost/pMEtHOAW182_aOFs/media/otel-ui-setup.png?w=1650&fit=max&auto=format&n=pMEtHOAW182_aOFs&q=85&s=11b85eede2f7641e1a39cef915de17ca 1650w, https://mintcdn.com/bifrost/pMEtHOAW182_aOFs/media/otel-ui-setup.png?w=2500&fit=max&auto=format&n=pMEtHOAW182_aOFs&q=85&s=aacd632c31f718f548e0c36d8f6fe8b3 2500w" />
  </Tab>

  <Tab title="Go SDK">
    ```go  theme={null}
    package main

    import (
        "context"
        bifrost "github.com/maximhq/bifrost/core"
        "github.com/maximhq/bifrost/core/schemas"
        "github.com/maximhq/bifrost/framework/pricing"
        otel "github.com/maximhq/bifrost/plugins/otel"
    )

    func main() {
        ctx := context.Background()
        logger := schemas.NewLogger()
        
        // Initialize pricing manager (required for cost calculation)
        pricingManager := pricing.NewPricingManager(logger)
        
        // Initialize OTel plugin
        otelPlugin, err := otel.Init(ctx, &otel.Config{
            ServiceName:  "bifrost",
            CollectorURL: "http://localhost:4318",
            TraceType:    otel.TraceTypeGenAIExtension,
            Protocol:     otel.ProtocolHTTP,
            Headers: map[string]string{
                "Authorization": "env.OTEL_API_KEY",
            },
        }, logger, pricingManager)
        if err != nil {
            panic(err)
        }
        
        // Initialize Bifrost with the plugin
        client, err := bifrost.Init(ctx, schemas.BifrostConfig{
            Account: &yourAccount,
            Plugins: []schemas.Plugin{otelPlugin},
        })
        if err != nil {
            panic(err)
        }
        defer client.Shutdown()
        
        // All requests are now traced to OTel collector
    }
    ```
  </Tab>

  <Tab title="config.json">
    For Gateway mode, configure via `config.json`:

    ```json  theme={null}
    {
      "plugins": [
        {
          "enabled": true,
          "name": "otel",
          "config": {
            "service_name": "bifrost",
            "collector_url": "http://localhost:4318",
            "trace_type": "genai_extension",
            "protocol": "http",
            "headers": {
              "Authorization": "env.OTEL_API_KEY"
            }
          }
        }
      ]
    }
    ```

    If you need to connect to an OTEL collector that requires TLS, configure `tls_ca_cert`:

    ```json  theme={null}
    {
      "plugins": [
        {
          "enabled": true,
          "name": "otel",
          "config": {
            "service_name": "bifrost",
            "collector_url": "localhost:4317",
            "trace_type": "genai_extension",
            "protocol": "grpc",
            "tls_ca_cert": "/path/to/your/ca.cert",
            "headers": {
              "Authorization": "env.OTEL_API_KEY"
            }
          }
        }
      ]
    }
    ```
  </Tab>
</Tabs>

***

## Quick Start with Docker

Get started quickly with a complete observability stack using the included Docker Compose configuration:

```yml  theme={null}
services:
  otel-collector:
    image: otel/opentelemetry-collector-contrib:latest
    container_name: otel-collector
    command: ["--config=/etc/otelcol/config.yaml"]
    configs:
      - source: otel-collector-config
        target: /etc/otelcol/config.yaml
    ports:
      - "4317:4317"   # OTLP gRPC
      - "4318:4318"   # OTLP HTTP
      - "8888:8888"   # Collector /metrics
      - "9464:9464"   # Prometheus scrape endpoint
      - "13133:13133" # Health check
      - "1777:1777"   # pprof
      - "55679:55679" # zpages
    restart: unless-stopped
    depends_on:
      - tempo

  tempo:
    image: grafana/tempo:latest
    container_name: tempo
    command: [ "-config.file=/etc/tempo.yaml" ]
    configs:
      - source: tempo-config
        target: /etc/tempo.yaml
    ports:
      - "3200:3200"   # tempo HTTP API
    expose:
      - "4317"        # OTLP gRPC (internal)
    volumes:
      - tempo-data:/var/tempo
    restart: unless-stopped

  prometheus:
    image: prom/prometheus:latest
    container_name: prometheus
    depends_on:
      - otel-collector
    command:
      - "--config.file=/etc/prometheus/prometheus.yml"
      - "--storage.tsdb.path=/prometheus"
      - "--web.console.libraries=/usr/share/prometheus/console_libraries"
      - "--web.console.templates=/usr/share/prometheus/consoles"
      - "--web.enable-remote-write-receiver"
    ports:
      - "9090:9090"
    volumes:
      - prometheus-data:/prometheus
    configs:
      - source: prometheus-config
        target: /etc/prometheus/prometheus.yml
    restart: unless-stopped

  grafana:
    image: grafana/grafana:latest
    container_name: grafana
    depends_on:
      - prometheus
      - tempo
    environment:
      GF_SECURITY_ADMIN_USER: admin
      GF_SECURITY_ADMIN_PASSWORD: admin
      GF_AUTH_ANONYMOUS_ENABLED: "true"
      GF_AUTH_ANONYMOUS_ORG_ROLE: Viewer
      GF_PLUGINS_ALLOW_LOADING_UNSIGNED_PLUGINS: "grafana-pyroscope-app,grafana-exploretraces-app,grafana-metricsdrilldown-app"
      GF_PLUGINS_ENABLE_ALPHA: "true"
      GF_INSTALL_PLUGINS: ""
    ports:
      - "4000:3000"
    volumes:
      - grafana-data:/var/lib/grafana
    configs:
      - source: grafana-datasources
        target: /etc/grafana/provisioning/datasources/datasources.yml
    restart: unless-stopped

configs:
  otel-collector-config:
    content: |
      receivers:
        otlp:
          protocols:
            grpc:
              endpoint: 0.0.0.0:4317
            http:
              endpoint: 0.0.0.0:4318

      processors:
        batch:

      exporters:
        prometheus:
          endpoint: 0.0.0.0:9464
          namespace: otel
          const_labels:
            source: otelcol
            
        otlp/tempo:
          endpoint: tempo:4317
          tls:
            insecure: true
            
        debug:
          verbosity: detailed

      extensions:
        health_check:
          endpoint: 0.0.0.0:13133
        pprof:
          endpoint: 0.0.0.0:1777
        zpages:
          endpoint: 0.0.0.0:55679

      service:
        extensions: [health_check, pprof, zpages]
        telemetry:
          logs:
            level: debug
          metrics:
            level: detailed
        pipelines:
          traces:
            receivers: [otlp]
            processors: [batch]
            exporters: [debug, otlp/tempo]
          metrics:
            receivers: [otlp]
            processors: [batch]
            exporters: [debug, prometheus]
          logs:
            receivers: [otlp]
            processors: [batch]
            exporters: [debug]

  tempo-config:
    content: |
      server:
        http_listen_port: 3200
        log_level: info

      distributor:
        receivers:
          otlp:
            protocols:
              grpc:
                endpoint: 0.0.0.0:4317

      ingester:
        max_block_duration: 5m
        trace_idle_period: 10s

      compactor:
        compaction:
          block_retention: 1h

      storage:
        trace:
          backend: local
          wal:
            path: /var/tempo/wal
          local:
            path: /var/tempo/blocks

      metrics_generator:
        registry:
          external_labels:
            source: tempo
        storage:
          path: /var/tempo/generator/wal
          remote_write:
            - url: http://prometheus:9090/api/v1/write

  prometheus-config:
    content: |
      global:
        scrape_interval: 15s
      scrape_configs:
        - job_name: "otelcol-internal"
          static_configs:
            - targets: ["otel-collector:8888"]
        - job_name: "otelcol-exporter"
          static_configs:
            - targets: ["otel-collector:9464"]
        - job_name: "tempo"
          static_configs:
            - targets: ["tempo:3200"]

  grafana-datasources:
    content: |
      apiVersion: 1
      datasources:
        - name: Prometheus
          uid: prometheus
          type: prometheus
          access: proxy
          orgId: 1
          url: http://prometheus:9090
          isDefault: true
          editable: true
        - name: Tempo
          uid: tempo
          type: tempo
          access: proxy
          orgId: 1
          url: http://tempo:3200
          editable: true
          jsonData:
            tracesToMetrics:
              datasourceUid: prometheus
            nodeGraph:
              enabled: true

volumes:
  prometheus-data:
  grafana-data:
  tempo-data:
```

This launches:

* **OTel Collector** - Receives traces on ports 4317 (gRPC) and 4318 (HTTP)
* **Tempo** - Distributed tracing backend
* **Prometheus** - Metrics collection
* **Grafana** - Visualization dashboard

Access Grafana at `http://localhost:3000` (default credentials: admin/admin)

<Frame>
  <img src="https://mintcdn.com/bifrost/HE3esZlo6PW0-gsx/media/grafana-otel-traces.png?fit=max&auto=format&n=HE3esZlo6PW0-gsx&q=85&s=59f4d1f541a4ff90c8c3a9949de316a4" alt="Okta Applications page" data-og-width="2196" width="2196" data-og-height="1214" height="1214" data-path="media/grafana-otel-traces.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/bifrost/HE3esZlo6PW0-gsx/media/grafana-otel-traces.png?w=280&fit=max&auto=format&n=HE3esZlo6PW0-gsx&q=85&s=256b07b5c87932063fbf4d44cd8cfcb0 280w, https://mintcdn.com/bifrost/HE3esZlo6PW0-gsx/media/grafana-otel-traces.png?w=560&fit=max&auto=format&n=HE3esZlo6PW0-gsx&q=85&s=a63c81ac56bc15a76da5d59f37b1a67f 560w, https://mintcdn.com/bifrost/HE3esZlo6PW0-gsx/media/grafana-otel-traces.png?w=840&fit=max&auto=format&n=HE3esZlo6PW0-gsx&q=85&s=b2bc5757ef1d7714a07a1e944fb140ce 840w, https://mintcdn.com/bifrost/HE3esZlo6PW0-gsx/media/grafana-otel-traces.png?w=1100&fit=max&auto=format&n=HE3esZlo6PW0-gsx&q=85&s=653cd0cd76576cd9a7cb944f84d1a721 1100w, https://mintcdn.com/bifrost/HE3esZlo6PW0-gsx/media/grafana-otel-traces.png?w=1650&fit=max&auto=format&n=HE3esZlo6PW0-gsx&q=85&s=cde889056c84791e490419d12861d611 1650w, https://mintcdn.com/bifrost/HE3esZlo6PW0-gsx/media/grafana-otel-traces.png?w=2500&fit=max&auto=format&n=HE3esZlo6PW0-gsx&q=85&s=db620b9ba5a580c1b5a23ff88178c9aa 2500w" />
</Frame>

***

## Popular Platform Integrations

<Tabs group="platforms">
  <Tab title="Grafana Cloud">
    ```json  theme={null}
    {
      "plugins": [
        {
          "enabled": true,
          "name": "otel",
          "config": {
            "service_name": "bifrost",
            "collector_url": "https://otlp-gateway-prod-us-central-0.grafana.net/otlp",
            "trace_type": "genai_extension",
            "protocol": "http",
            "headers": {
              "Authorization": "env.GRAFANA_CLOUD_API_KEY"
            }
          }
        }
      ]
    }
    ```

    Set environment variable:

    ```bash  theme={null}
    export GRAFANA_CLOUD_API_KEY="Basic <your-base64-encoded-token>"
    ```
  </Tab>

  <Tab title="Datadog">
    ```json  theme={null}
    {
      "plugins": [
        {
          "enabled": true,
          "name": "otel",
          "config": {
            "service_name": "bifrost",
            "collector_url": "https://trace.agent.datadoghq.com",
            "trace_type": "genai_extension",
            "protocol": "http",
            "headers": {
              "DD-API-KEY": "env.DATADOG_API_KEY"
            }
          }
        }
      ]
    }
    ```

    Set environment variable:

    ```bash  theme={null}
    export DATADOG_API_KEY="your-datadog-api-key"
    ```
  </Tab>

  <Tab title="New Relic">
    ```json  theme={null}
    {
      "plugins": [
        {
          "enabled": true,
          "name": "otel",
          "config": {
            "service_name": "bifrost",
            "collector_url": "https://otlp.nr-data.net:4318",
            "trace_type": "genai_extension",
            "protocol": "http",
            "headers": {
              "api-key": "env.NEW_RELIC_LICENSE_KEY"
            }
          }
        }
      ]
    }
    ```

    Set environment variable:

    ```bash  theme={null}
    export NEW_RELIC_LICENSE_KEY="your-license-key"
    ```
  </Tab>

  <Tab title="Honeycomb">
    ```json  theme={null}
    {
      "plugins": [
        {
          "enabled": true,
          "name": "otel",
          "config": {
            "service_name": "bifrost",
            "collector_url": "https://api.honeycomb.io",
            "trace_type": "genai_extension",
            "protocol": "http",
            "headers": {
              "x-honeycomb-team": "env.HONEYCOMB_API_KEY",
              "x-honeycomb-dataset": "bifrost-traces"
            }
          }
        }
      ]
    }
    ```

    Set environment variable:

    ```bash  theme={null}
    export HONEYCOMB_API_KEY="your-api-key"
    ```
  </Tab>

  <Tab title="Langfuse">
    [Langfuse](https://langfuse.com) is an open-source LLM observability platform that accepts OpenTelemetry traces via its OTLP endpoint.

    <Tabs>
      <Tab title="UI">
        Configure the OTel plugin with the following settings:

        | Field             | Value                                                                                                     |
        | ----------------- | --------------------------------------------------------------------------------------------------------- |
        | **Collector URL** | `https://cloud.langfuse.com/api/public/otel` (EU) or `https://us.cloud.langfuse.com/api/public/otel` (US) |
        | **Trace Type**    | `genai_extension`                                                                                         |
        | **Protocol**      | `http` (required - Langfuse does not support gRPC)                                                        |
        | **Headers**       | `Authorization`: `env.LANGFUSE_AUTH`                                                                      |
      </Tab>

      <Tab title="config.json">
        ```json  theme={null}
        {
          "plugins": [
            {
              "enabled": true,
              "name": "otel",
              "config": {
                "service_name": "bifrost",
                "collector_url": "https://cloud.langfuse.com/api/public/otel",
                "trace_type": "genai_extension",
                "protocol": "http",
                "headers": {
                  "Authorization": "env.LANGFUSE_AUTH"
                }
              }
            }
          ]
        }
        ```

        For US region, use `https://us.cloud.langfuse.com/api/public/otel` instead.
      </Tab>
    </Tabs>

    Set up the environment variable with your Langfuse API keys:

    ```bash  theme={null}
    # Generate base64 auth string from your Langfuse API keys
    export LANGFUSE_AUTH="Basic $(echo -n 'pk-lf-xxx:sk-lf-xxx' | base64)"
    ```

    Replace `pk-lf-xxx` and `sk-lf-xxx` with your Langfuse public and secret keys from your project settings.

    <Note>
      Langfuse only supports HTTP protocol. Do not use gRPC.
    </Note>

    See the [Langfuse OpenTelemetry documentation](https://langfuse.com/integrations/native/opentelemetry) for more details.
  </Tab>

  <Tab title="Self-Hosted">
    Use the included Docker Compose stack or point to your own collector:

    ```json  theme={null}
    {
      "plugins": [
        {
          "enabled": true,
          "name": "otel",
          "config": {
            "service_name": "bifrost",
            "collector_url": "http://your-collector:4318",
            "trace_type": "genai_extension",
            "protocol": "http"
          }
        }
      ]
    }
    ```
  </Tab>
</Tabs>

***

## Captured Data

Each trace includes comprehensive LLM operation metadata following OpenTelemetry semantic conventions:

### Span Attributes

* **Span Name**: Based on request type (`gen_ai.chat`, `gen_ai.text`, `gen_ai.embedding`, etc.)
* **Service Info**: `service.name=bifrost`, `service.version`
* **Provider & Model**: `gen_ai.provider.name`, `gen_ai.request.model`

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

### Performance Metrics

* Token usage (prompt, completion, total)
* Cost calculations in dollars
* Latency and timing (start/end timestamps)
* Error details with status codes

### Example Span

```json  theme={null}
{
  "name": "gen_ai.chat",
  "attributes": {
    "gen_ai.provider.name": "openai",
    "gen_ai.request.model": "gpt-4",
    "gen_ai.request.temperature": 0.7,
    "gen_ai.request.max_tokens": 1000,
    "gen_ai.usage.prompt_tokens": 45,
    "gen_ai.usage.completion_tokens": 128,
    "gen_ai.usage.total_tokens": 173,
    "gen_ai.usage.cost": 0.0052
  }
}
```

<Frame>
  <img src="https://mintcdn.com/bifrost/HE3esZlo6PW0-gsx/media/grafana-otel-span-details.png?fit=max&auto=format&n=HE3esZlo6PW0-gsx&q=85&s=d0d071e7209de2370bb756ef7214ce9d" alt="Okta Applications page" data-og-width="2200" width="2200" data-og-height="1216" height="1216" data-path="media/grafana-otel-span-details.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/bifrost/HE3esZlo6PW0-gsx/media/grafana-otel-span-details.png?w=280&fit=max&auto=format&n=HE3esZlo6PW0-gsx&q=85&s=6509631aa794a8f08db18e7b7145f734 280w, https://mintcdn.com/bifrost/HE3esZlo6PW0-gsx/media/grafana-otel-span-details.png?w=560&fit=max&auto=format&n=HE3esZlo6PW0-gsx&q=85&s=02c8f2d42695aad5dfc884b884fec771 560w, https://mintcdn.com/bifrost/HE3esZlo6PW0-gsx/media/grafana-otel-span-details.png?w=840&fit=max&auto=format&n=HE3esZlo6PW0-gsx&q=85&s=28d812245d2df8b60e23b8d30e8d8f75 840w, https://mintcdn.com/bifrost/HE3esZlo6PW0-gsx/media/grafana-otel-span-details.png?w=1100&fit=max&auto=format&n=HE3esZlo6PW0-gsx&q=85&s=2c391dc880d1788896c4722762ed2269 1100w, https://mintcdn.com/bifrost/HE3esZlo6PW0-gsx/media/grafana-otel-span-details.png?w=1650&fit=max&auto=format&n=HE3esZlo6PW0-gsx&q=85&s=af17519d18220bc3b93b04cc7f594934 1650w, https://mintcdn.com/bifrost/HE3esZlo6PW0-gsx/media/grafana-otel-span-details.png?w=2500&fit=max&auto=format&n=HE3esZlo6PW0-gsx&q=85&s=2608735582f36b6440fabbf5f8daa2e8 2500w" />
</Frame>

***

## Supported Request Types

The OTel plugin captures all Bifrost request types:

* **Chat Completion** (streaming and non-streaming) → `gen_ai.chat`
* **Text Completion** (streaming and non-streaming) → `gen_ai.text`
* **Embeddings** → `gen_ai.embedding`
* **Speech Generation** (streaming and non-streaming) → `gen_ai.speech`
* **Transcription** (streaming and non-streaming) → `gen_ai.transcription`
* **Responses API** → `gen_ai.responses`

***

## Protocol Support

### HTTP (OTLP/HTTP)

Uses HTTP/1.1 or HTTP/2 with JSON or Protobuf encoding:

```json  theme={null}
{
  "collector_url": "http://localhost:4318",
  "protocol": "http"
}
```

Default port: **4318**

### gRPC (OTLP/gRPC)

Uses gRPC with Protobuf encoding for lower latency:

```json  theme={null}
{
  "collector_url": "http://localhost:4317",
  "protocol": "grpc"
}
```

Default port: **4317**

***

## Advanced Features

### Automatic Span Management

* Spans are tracked with a **20-minute TTL** using an efficient sync.Map implementation
* Automatic cleanup prevents memory leaks for long-running processes
* Handles streaming requests with accumulator for chunked responses

### Async Emission

All span emissions happen asynchronously in background goroutines:

```go  theme={null}
// Zero impact on request latency
go func() {
    p.client.Emit(ctx, spans)
}()
```

### Streaming Support

The plugin accumulates streaming chunks and emits a single complete span when the stream finishes, providing accurate token counts and costs.

### Environment Variable Security

Sensitive credentials never appear in config files:

```json  theme={null}
{
  "headers": {
    "Authorization": "env.OTEL_API_KEY"
  }
}
```

The plugin reads `OTEL_API_KEY` from the environment at runtime.

***

## When to Use

### OTel Plugin

Choose the OTel plugin when you:

* Have existing OpenTelemetry infrastructure
* Need to correlate LLM traces with application traces
* Require compliance with enterprise observability standards
* Want vendor flexibility (switch backends without code changes)
* Need multi-service distributed tracing

### vs. Built-in Observability

Use [Built-in Observability](./default) for:

* Local development and testing
* Simple self-hosted deployments
* No external dependencies
* Direct database access to logs

### vs. Maxim Plugin

Use the [Maxim Plugin](./maxim) for:

* Advanced LLM evaluation and testing
* Prompt engineering and experimentation
* Team collaboration and governance
* Production monitoring with alerts
* Dataset management and curation

***

## Troubleshooting

### Connection Issues

Verify collector is reachable:

```bash  theme={null}
# Test HTTP endpoint
curl -v http://localhost:4318/v1/traces

# Test gRPC endpoint (requires grpcurl)
grpcurl -plaintext localhost:4317 list
```

### Missing Traces

Check Bifrost logs for emission errors:

```bash  theme={null}
# Enable debug logging
bifrost-http --log-level debug
```

### Authentication Failures

Verify environment variables are set:

```bash  theme={null}
echo $OTEL_API_KEY
```

***

## Next Steps

* **[Built-in Observability](./default)** - Local logging for development
* **[Maxim Plugin](./maxim)** - Advanced LLM evaluation and monitoring
* **[Telemetry](../telemetry)** - Prometheus metrics and dashboards


---

> To find navigation and other pages in this documentation, fetch the llms.txt file at: https://docs.getbifrost.ai/llms.txt