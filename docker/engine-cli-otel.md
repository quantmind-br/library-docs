---
title: OpenTelemetry for the Docker CLI
url: https://docs.docker.com/engine/cli/otel/
source: llms
fetched_at: 2026-01-24T14:22:38.314473703-03:00
rendered_js: false
word_count: 513
summary: This document explains how to configure and use OpenTelemetry instrumentation in the Docker CLI to emit and collect metrics regarding command invocations. It provides a step-by-step guide for setting up an OpenTelemetry collector and a Prometheus backend to visualize CLI telemetry data.
tags:
    - docker-cli
    - opentelemetry
    - metrics
    - observability
    - instrumentation
    - telemetry-data
category: guide
---

Requires: Docker Engine [26.1.0](https://docs.docker.com/engine/release-notes/26.1/#2610) and later

The Docker CLI supports [OpenTelemetry](https://opentelemetry.io/docs/) instrumentation for emitting metrics about command invocations. This is disabled by default. You can configure the CLI to start emitting metrics to the endpoint that you specify. This allows you to capture information about your `docker` command invocations for more insight into your Docker usage.

Exporting metrics is opt-in, and you control where data is being sent by specifying the destination address of the metrics collector.

OpenTelemetry, or OTel for short, is an open observability framework for creating and managing telemetry data, such as traces, metrics, and logs. OpenTelemetry is vendor- and tool-agnostic, meaning that it can be used with a broad variety of Observability backends.

Support for OpenTelemetry instrumentation in the Docker CLI means that the CLI can emit information about events that take place, using the protocols and conventions defined in the Open Telemetry specification.

The Docker CLI doesn't emit telemetry data by default. Only if you've set an environment variable on your system will Docker CLI attempt to emit OpenTelemetry metrics, to the endpoint that you specify.

The variable specifies the endpoint of an OpenTelemetry collector, where telemetry data about `docker` CLI invocation should be sent. To capture the data, you'll need an OpenTelemetry collector listening on that endpoint.

The purpose of a collector is to receive the telemetry data, process it, and exports it to a backend. The backend is where the telemetry data gets stored. You can choose from a number of different backends, such as Prometheus or InfluxDB.

Some backends provide tools for visualizing the metrics directly. Alternatively, you can also run a dedicated frontend with support for generating more useful graphs, such as Grafana.

To get started capturing telemetry data for the Docker CLI, you'll need to:

- Set the `DOCKER_CLI_OTEL_EXPORTER_OTLP_ENDPOINT` environment variable to point to an OpenTelemetry collector endpoint
- Run an OpenTelemetry collector that receives the signals from CLI command invocations
- Run a backend for storing the data received from the collector

The following Docker Compose file bootstraps a set of services to get started with OpenTelemetry. It includes an OpenTelemetry collector that the CLI can send metrics to, and a Prometheus backend that scrapes the metrics off the collector.

This service assumes that the following two configuration files exist alongside `compose.yaml`:

With these files in place:

1. Start the Docker Compose services:
2. Configure Docker CLI to export telemetry to the OpenTelemetry collector.
3. Run a `docker` command to trigger the CLI into sending a metric signal to the OpenTelemetry collector.
4. To view telemetry metrics created by the CLI, open the Prometheus expression browser by going to [http://localhost:9091/graph](http://localhost:9091/graph).
5. In the **Query** field, enter `command_time_milliseconds_total`, and execute the query to see the telemetry data.

Docker CLI currently exports a single metric, `command.time`, which measures the execution duration of a command in milliseconds. This metric has the following attributes:

- `command.name`: the name of the command
- `command.status.code`: the exit code of the command
- `command.stderr.isatty`: true if stderr is attached to a TTY
- `command.stdin.isatty`: true if stdin is attached to a TTY
- `command.stdout.isatty`: true if stdout is attached to a TTY