---
title: Setup OpenTelemetry POC - vLLM
url: https://docs.vllm.ai/en/latest/examples/observability/opentelemetry/
source: sitemap
fetched_at: 2026-05-07T21:13:09.73106573-03:00
rendered_js: false
word_count: 206
summary: This document explains how to set up and configure OpenTelemetry integration with vLLM to enable distributed tracing, including instrumentation options and exporter protocols.
tags:
    - vllm
    - opentelemetry
    - observability
    - distributed-tracing
    - jaeger
    - fastapi-instrumentation
category: tutorial
---

[](https://github.com/vllm-project/vllm/edit/main/docs/examples/observability/opentelemetry.md "Edit this page")

Source [https://github.com/vllm-project/vllm/tree/main/examples/observability/opentelemetry](https://github.com/vllm-project/vllm/tree/main/examples/observability/opentelemetry).

> **Note:** The core OpenTelemetry packages (`opentelemetry-sdk`, `opentelemetry-api`, `opentelemetry-exporter-otlp`, `opentelemetry-semantic-conventions-ai`) are bundled with vLLM. Manual installation is not required.

1. Start Jaeger in a docker container:
   
   ```
   # From: https://www.jaegertracing.io/docs/1.57/getting-started/
   dockerrun--rm--namejaeger\
   -eCOLLECTOR_ZIPKIN_HOST_PORT=:9411\
   -p6831:6831/udp\
   -p6832:6832/udp\
   -p5778:5778\
   -p16686:16686\
   -p4317:4317\
   -p4318:4318\
   -p14250:14250\
   -p14268:14268\
   -p14269:14269\
   -p9411:9411\
   jaegertracing/all-in-one:1.57
   ```
2. In a new shell, export Jaeger IP:
   
   ```
   exportJAEGER_IP=$(dockerinspect--format'{{ .NetworkSettings.IPAddress }}'jaeger)
   exportOTEL_EXPORTER_OTLP_TRACES_ENDPOINT=grpc://$JAEGER_IP:4317
   ```
   
   Then set vLLM's service name for OpenTelemetry, enable insecure connections to Jaeger and run vLLM:
   
   ```
   exportOTEL_SERVICE_NAME="vllm-server"
   exportOTEL_EXPORTER_OTLP_TRACES_INSECURE=true
   vllmservefacebook/opt-125m--otlp-traces-endpoint="$OTEL_EXPORTER_OTLP_TRACES_ENDPOINT"
   ```
3. In a new shell, send requests with trace context from a dummy client
   
   ```
   exportJAEGER_IP=$(dockerinspect--format'{{ .NetworkSettings.IPAddress }}'jaeger)
   exportOTEL_EXPORTER_OTLP_TRACES_ENDPOINT=grpc://$JAEGER_IP:4317
   exportOTEL_EXPORTER_OTLP_TRACES_INSECURE=true
   exportOTEL_SERVICE_NAME="client-service"
   pythondummy_client.py
   ```
4. Open Jaeger webui: [http://localhost:16686/](http://localhost:16686/)
   
   In the search pane, select `vllm-server` service and hit `Find Traces`. You should get a list of traces, one for each request. [![Traces](https://i.imgur.com/GYHhFjo.png)](https://i.imgur.com/GYHhFjo.png)
5. Clicking on a trace will show its spans and their tags. In this demo, each trace has 2 spans. One from the dummy client containing the prompt text and one from vLLM containing metadata about the request. [![Spans details](https://i.imgur.com/OPf6CBL.png)](https://i.imgur.com/OPf6CBL.png)

## Exporter Protocol[¶](#exporter-protocol "Permanent link")

OpenTelemetry supports either `grpc` or `http/protobuf` as the transport protocol for trace data in the exporter. By default, `grpc` is used. To set `http/protobuf` as the protocol, configure the `OTEL_EXPORTER_OTLP_TRACES_PROTOCOL` environment variable as follows:

```
exportOTEL_EXPORTER_OTLP_TRACES_PROTOCOL=http/protobuf
exportOTEL_EXPORTER_OTLP_TRACES_ENDPOINT=http://$JAEGER_IP:4318/v1/traces
vllmservefacebook/opt-125m--otlp-traces-endpoint="$OTEL_EXPORTER_OTLP_TRACES_ENDPOINT"
```

## Instrumentation of FastAPI[¶](#instrumentation-of-fastapi "Permanent link")

OpenTelemetry allows automatic instrumentation of FastAPI.

1. Install the instrumentation library
   
   ```
   pipinstallopentelemetry-instrumentation-fastapi
   ```
2. Run vLLM with `opentelemetry-instrument`
   
   ```
   opentelemetry-instrumentvllmservefacebook/opt-125m
   ```
3. Send a request to vLLM and find its trace in Jaeger. It should contain spans from FastAPI.

[![FastAPI Spans](https://i.imgur.com/hywvoOJ.png)](https://i.imgur.com/hywvoOJ.png)

## Example materials[¶](#example-materials "Permanent link")

dummy\_client.py

```
# SPDX-License-Identifier: Apache-2.0
# SPDX-FileCopyrightText: Copyright contributors to the vLLM project

importrequests
fromopentelemetry.exporter.otlp.proto.grpc.trace_exporterimport OTLPSpanExporter
fromopentelemetry.sdk.traceimport TracerProvider
fromopentelemetry.sdk.trace.exportimport BatchSpanProcessor, ConsoleSpanExporter
fromopentelemetry.traceimport SpanKind, set_tracer_provider
fromopentelemetry.trace.propagation.tracecontextimport TraceContextTextMapPropagator

trace_provider = TracerProvider()
set_tracer_provider(trace_provider)

trace_provider.add_span_processor(BatchSpanProcessor(OTLPSpanExporter()))
trace_provider.add_span_processor(BatchSpanProcessor(ConsoleSpanExporter()))

tracer = trace_provider.get_tracer("dummy-client")

url = "http://localhost:8000/v1/completions"
with tracer.start_as_current_span("client-span", kind=SpanKind.CLIENT) as span:
    prompt = "San Francisco is a"
    span.set_attribute("prompt", prompt)
    headers = {}
    TraceContextTextMapPropagator().inject(headers)
    payload = {
        "model": "facebook/opt-125m",
        "prompt": prompt,
        "max_tokens": 10,
        "n": 3,
        "use_beam_search": "true",
        "temperature": 0.0,
        # "stream": True,
    }
    response = requests.post(url, headers=headers, json=payload)
```