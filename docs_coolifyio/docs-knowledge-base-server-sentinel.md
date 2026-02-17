---
title: Sentinel and Metrics
url: https://coolify.io/docs/knowledge-base/server/sentinel.md
source: llms
fetched_at: 2026-02-17T14:40:56.362035-03:00
rendered_js: false
word_count: 154
summary: This document explains how to enable and configure Sentinel to monitor server and container resource usage, including CPU and RAM consumption.
tags:
    - sentinel
    - resource-monitoring
    - metrics
    - server-metrics
    - container-metrics
    - system-api
category: guide
---

# Sentinel and Metrics

::: danger CAUTION
**This is an experimental feature.**
:::

# Sentinel Overview

[Sentinel](https://github.com/coollabsio/sentinel) is an open-source lightweight container that provides:

* Linux system API
* Server resource monitoring (CPU, RAM usage for now)
* Container resource monitoring (CPU, RAM usage for now)

## Screenshot

## Configuration

### Enable Sentinel

1. Navigate to `Servers` > `<YOUR_SERVER>` > `Configurations` > `General`
2. Find the `Sentinel` section
3. Toggle `Enable Sentinel`
4. Wait a few moments for the container to be downloaded and start.

### Enable Metrics (Optional)

In the same section, you can enable metrics. Once enabled, you will be able to view the following metrics:

* CPU usage
* Memory consumption (RAM Usage)

::: info Note
Metrics collection is currently NOT available for Docker Compose and Service Template based deployments.
:::

## Viewing Metrics

### Server Metrics

Access server-wide metrics at:

`Servers` > `<YOUR_SERVER>` > `Configurations` > `Metrics`

### Container Metrics

View individual container metrics:

1. Navigate to the specific resource
2. Go to the `Configurations` tab
3. Select the `Metrics` tab