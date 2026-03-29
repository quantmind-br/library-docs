---
title: Collect Docker metrics with Prometheus
url: https://docs.docker.com/engine/daemon/prometheus/
source: llms
fetched_at: 2026-01-24T14:23:00.886943341-03:00
rendered_js: false
word_count: 568
summary: This document provides instructions on how to configure the Docker daemon to expose metrics and set up a Prometheus container to monitor the Docker engine.
tags:
    - docker
    - prometheus
    - monitoring
    - metrics
    - docker-daemon
    - configuration
category: tutorial
---

[Prometheus](https://prometheus.io/) is an open-source systems monitoring and alerting toolkit. You can configure Docker as a Prometheus target.

> The available metrics and the names of those metrics are in active development and may change at any time.

Currently, you can only monitor Docker itself. You can't currently monitor your application using the Docker target.

The following example shows you how to configure your Docker daemon, set up Prometheus to run as a container on your local machine, and monitor your Docker instance using Prometheus.

### [Configure the daemon](#configure-the-daemon)

To configure the Docker daemon as a Prometheus target, you need to specify the `metrics-address` in the `daemon.json` configuration file. This daemon expects the file to be located at one of the following locations by default. If the file doesn't exist, create it.

- **Linux**: `/etc/docker/daemon.json`
- **Windows Server**: `C:\ProgramData\docker\config\daemon.json`
- **Docker Desktop**: Open the Docker Desktop settings and select **Docker Engine** to edit the file.

Add the following configuration:

Save the file, or in the case of Docker Desktop for Mac or Docker Desktop for Windows, save the configuration. Restart Docker.

Docker now exposes Prometheus-compatible metrics on port 9323 via the loopback interface. You can configure it to use the wildcard address `0.0.0.0` instead, but this will expose the Prometheus port to the wider network. Consider your threat model carefully when deciding which option best suits your environment.

### [Create a Prometheus configuration](#create-a-prometheus-configuration)

Copy the following configuration file and save it to a location of your choice, for example `/tmp/prometheus.yml`. This is a stock Prometheus configuration file, except for the addition of the Docker job definition at the bottom of the file.

### [Run Prometheus in a container](#run-prometheus-in-a-container)

Next, start a Prometheus container using this configuration.

If you're using Docker Desktop, the `--add-host` flag is optional. This flag makes sure that the host's internal IP gets exposed to the Prometheus container. Docker Desktop does this by default. The host IP is exposed as the `host.docker.internal` hostname. This matches the configuration defined in `prometheus.yml` in the previous step.

### [Open the Prometheus Dashboard](#open-the-prometheus-dashboard)

Verify that the Docker target is listed at `http://localhost:9090/targets/`.

![Prometheus targets page](https://docs.docker.com/engine/daemon/images/prometheus-targets.webp)

![Prometheus targets page](https://docs.docker.com/engine/daemon/images/prometheus-targets.webp)

> You can't access the endpoint URLs on this page directly if you use Docker Desktop.

### [Use Prometheus](#use-prometheus)

Create a graph. Select the **Graphs** link in the Prometheus UI. Choose a metric from the combo box to the right of the **Execute** button, and click **Execute**. The screenshot below shows the graph for `engine_daemon_network_actions_seconds_count`.

![Idle Prometheus report](https://docs.docker.com/engine/daemon/images/prometheus-graph_idle.webp)

![Idle Prometheus report](https://docs.docker.com/engine/daemon/images/prometheus-graph_idle.webp)

The graph shows a pretty idle Docker instance, unless you're already running active workloads on your system.

To make the graph more interesting, run a container that uses some network actions by starting downloading some packages using a package manager:

Wait a few seconds (the default scrape interval is 15 seconds) and reload your graph. You should see an uptick in the graph, showing the increased network traffic caused by the container you just ran.

![Prometheus report showing traffic](https://docs.docker.com/engine/daemon/images/prometheus-graph_load.webp)

![Prometheus report showing traffic](https://docs.docker.com/engine/daemon/images/prometheus-graph_load.webp)

The example provided here shows how to run Prometheus as a container on your local system. In practice, you'll probably be running Prometheus on another system or as a cloud service somewhere. You can set up the Docker daemon as a Prometheus target in such contexts too. Configure the `metrics-addr` of the daemon and add the address of the daemon as a scrape endpoint in your Prometheus configuration.

For more information about Prometheus, refer to the [Prometheus documentation](https://prometheus.io/docs/introduction/overview/)