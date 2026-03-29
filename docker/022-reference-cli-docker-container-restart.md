---
title: docker container restart
url: https://docs.docker.com/reference/cli/docker/container/restart/
source: llms
fetched_at: 2026-01-24T14:35:17.856993794-03:00
rendered_js: false
word_count: 255
summary: This document provides the technical reference for the docker container restart command, detailing its usage, aliases, and configuration options for signals and timeouts.
tags:
    - docker
    - container-management
    - cli-reference
    - docker-restart
    - signal-handling
    - timeout-configuration
category: reference
---

DescriptionRestart one or more containersUsage`docker container restart [OPTIONS] CONTAINER [CONTAINER...]`Aliases

An alias is a short or memorable alternative for a longer command.

`docker restart`

## [Description](#description)

Restart one or more containers

## [Options](#options)

OptionDefaultDescription[`-s, --signal`](#signal)Signal to send to the container[`-t, --timeout`](#timeout)Seconds to wait before killing the container

## [Examples](#examples)

```
$ docker restart my_container
```

### [Stop container with signal (-s, --signal)](#signal)

The `--signal` flag sends the system call signal to the container to exit. This signal can be a signal name in the format `SIG<NAME>`, for instance `SIGKILL`, or an unsigned number that matches a position in the kernel's syscall table, for instance `9`. Refer to [signal(7)](https://man7.org/linux/man-pages/man7/signal.7.html) for available signals.

The default signal to use is defined by the image's [`StopSignal`](https://github.com/opencontainers/image-spec/blob/v1.1.0/config.md), which can be set through the [`STOPSIGNAL`](https://docs.docker.com/reference/dockerfile/#stopsignal) Dockerfile instruction when building the image, or configured using the [`--stop-signal`](https://docs.docker.com/reference/cli/docker/container/run/#stop-signal) option when creating the container. If no signal is configured for the container, `SIGTERM` is used as default.

### [Stop container with timeout (-t, --timeout)](#timeout)

The `--timeout` flag sets the number of seconds to wait for the container to stop after sending the pre-defined (see [`--signal`](#signal)) system call signal. If the container does not exit after the timeout elapses, it's forcibly killed with a `SIGKILL` signal.

If you set `--timeout` to `-1`, no timeout is applied, and the daemon waits indefinitely for the container to exit.

The default timeout can be specified using the [`--stop-timeout`](https://docs.docker.com/reference/cli/docker/container/run/#stop-timeout) option when creating the container. If no default is configured for the container, the Daemon determines the default, and is 10 seconds for Linux containers, and 30 seconds for Windows containers.