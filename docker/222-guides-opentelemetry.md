---
title: Instrumenting JS Apps with OpenTelemetry
url: https://docs.docker.com/guides/opentelemetry/
source: llms
fetched_at: 2026-01-24T14:11:02.119531286-03:00
rendered_js: false
word_count: 405
summary: This guide provides a step-by-step walkthrough for instrumenting a Node.js application with OpenTelemetry to collect and visualize traces using Docker and Jaeger.
tags:
    - opentelemetry
    - nodejs
    - docker-compose
    - distributed-tracing
    - jaeger
    - observability
    - instrumentation
category: tutorial
---

## Instrumenting a JavaScript App with OpenTelemetry

OpenTelemetry (OTel) is an open-source observability framework that provides a set of APIs, SDKs, and tools for collecting telemetry data, such as metrics, logs, and traces, from applications. With OpenTelemetry, developers can obtain valuable insights into how their services perform in production or during local development.

A key component of OpenTelemetry is the OpenTelemetry Protocol (OTLP) a general-purpose, vendor-agnostic protocol designed to transmit telemetry data efficiently and reliably. OTLP supports multiple data types (traces, metrics, logs) over HTTP or gRPC, making it the default and recommended protocol for communication between instrumented applications, the OpenTelemetry Collector, and backends such as Jaeger or Prometheus.

This guide walks you through how to instrument a simple Node.js application with OpenTelemetry and run both the app and a collector using Docker. This setup is ideal for local development and testing observability before integrating with external observability platforms like Prometheus, Jaeger, or Grafana.

In this guide, you'll learn how to:

- How to set up OpenTelemetry in a Node.js app.
- How to run an OpenTelemetry Collector in Docker.
- How to visualize traces with Jaeger.
- How to use Docker Compose to manage the full observability stack.

The [Docker Official Image for OpenTelemetry](https://hub.docker.com/r/otel/opentelemetry-collector-contrib) provides a convenient way to deploy and manage Dex instances. OpenTelemetry is available for various CPU architectures, including amd64, armv7, and arm64, ensuring compatibility with different devices and platforms. Same for the [Jaeger docekr image](https://hub.docker.com/r/jaegertracing/jaeger).

[Docker Compose](https://docs.docker.com/compose/): Recommended for managing multi-container Docker applications.

Basic knowledge of Node.js and Docker.

Create the project directory:

Initialize a basic Node.js app:

Now, add the application logic:

Create the tracer configuration file:

Create a collector-config.yaml file at the root:

Create the `docker-compose.yaml` file:

Now, add the `Dockerfile` inside the `app/` folder:

Start all services with Docker Compose:

Once the services are running:

Visit your app at [http://localhost:3000](http://localhost:3000)

View traces at [http://localhost:16686](http://localhost:16686) in the Jaeger UI

After visiting your app's root endpoint, open Jaeger’s UI, search for the service (default is usually `unknown_service` unless explicitly named), and check the traces.

You should see spans for the HTTP request, middleware, and auto-instrumented libraries.

You now have a fully functional OpenTelemetry setup using Docker Compose. You've instrumented a basic JavaScript app to export traces and visualized them using Jaeger. This architecture is extendable for more complex applications and observability pipelines using Prometheus, Grafana, or cloud-native exporters.

For advanced topics such as custom span creation, metrics, and logs, consult the OpenTelemetry JavaScript docs.