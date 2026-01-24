---
title: Use docker logs with remote logging drivers
url: https://docs.docker.com/engine/logging/dual-logging/
source: llms
fetched_at: 2026-01-24T14:24:09.474544457-03:00
rendered_js: false
word_count: 649
summary: This document explains Docker's dual logging mechanism, which allows the retrieval of container logs via the CLI even when using remote logging drivers by maintaining a local cache.
tags:
    - docker-logs
    - dual-logging
    - logging-drivers
    - log-caching
    - docker-engine
    - log-configuration
category: guide
---

You can use the `docker logs` command to read container logs regardless of the configured logging driver or plugin. Docker Engine uses the [`local`](https://docs.docker.com/engine/logging/drivers/local/) logging driver to act as cache for reading the latest logs of your containers. This is called dual logging. By default, the cache has log-file rotation enabled, and is limited to a maximum of 5 files of 20 MB each (before compression) per container.

Refer to the [configuration options](#configuration-options) section to customize these defaults, or to the [disable dual logging](#disable-the-dual-logging-cache) section to disable this feature.

Docker Engine automatically enables dual logging if the configured logging driver doesn't support reading logs.

The following examples show the result of running a `docker logs` command with and without dual logging availability:

### [Without dual logging capability](#without-dual-logging-capability)

When a container is configured with a remote logging driver such as `splunk`, and dual logging is disabled, an error is displayed when attempting to read container logs locally:

- Step 1: Configure Docker daemon
- Step 2: Start the container
- Step 3: Read the container logs

### [With dual logging capability](#with-dual-logging-capability)

With the dual logging cache enabled, the `docker logs` command can be used to read logs, even if the logging driver doesn't support reading logs. The following example shows a daemon configuration that uses the `splunk` remote logging driver as a default, with dual logging caching enabled:

- Step 1: Configure Docker daemon
- Step 2: Start the container
- Step 3: Read the container logs

> For logging drivers that support reading logs, such as the `local`, `json-file` and `journald` drivers, there is no difference in functionality before or after the dual logging capability became available. For these drivers, Logs can be read using `docker logs` in both scenarios.

### [Configuration options](#configuration-options)

The dual logging cache accepts the same configuration options as the [`local` logging driver](https://docs.docker.com/engine/logging/drivers/local/), but with a `cache-` prefix. These options can be specified per container, and defaults for new containers can be set using the [daemon configuration file](https://docs.docker.com/reference/cli/dockerd/#daemon-configuration-file).

By default, the cache has log-file rotation enabled, and is limited to a maximum of 5 files of 20MB each (before compression) per container. Use the configuration options described below to customize these defaults.

OptionDefaultDescription`cache-disabled``"false"`Disable local caching. Boolean value passed as a string (`true`, `1`, `0`, or `false`).`cache-max-size``"20m"`The maximum size of the cache before it is rotated. A positive integer plus a modifier representing the unit of measure (`k`, `m`, or `g`).`cache-max-file``"5"`The maximum number of cache files that can be present. If rotating the logs creates excess files, the oldest file is removed. A positive integer.`cache-compress``"true"`Enable or disable compression of rotated log files. Boolean value passed as a string (`true`, `1`, `0`, or `false`).

Use the `cache-disabled` option to disable the dual logging cache. Disabling the cache can be useful to save storage space in situations where logs are only read through a remote logging system, and if there is no need to read logs through `docker logs` for debugging purposes.

Caching can be disabled for individual containers or by default for new containers, when using the [daemon configuration file](https://docs.docker.com/reference/cli/dockerd/#daemon-configuration-file).

The following example uses the daemon configuration file to use the [`splunk`](https://docs.docker.com/engine/logging/drivers/splunk/) logging driver as a default, with caching disabled:

> For logging drivers that support reading logs, such as the `local`, `json-file` and `journald` drivers, dual logging isn't used, and disabling the option has no effect.

- If a container using a logging driver or plugin that sends logs remotely has a network issue, no `write` to the local cache occurs.
- If a write to `logdriver` fails for any reason (file system full, write permissions removed), the cache write fails and is logged in the daemon log. The log entry to the cache isn't retried.
- Some logs might be lost from the cache in the default configuration because a ring buffer is used to prevent blocking the stdio of the container in case of slow file writes. An admin must repair these while the daemon is shut down.