---
title: docker container pause
url: https://docs.docker.com/reference/cli/docker/container/pause/
source: llms
fetched_at: 2026-01-24T14:35:13.644935116-03:00
rendered_js: false
word_count: 100
summary: This document explains the usage and technical implementation of the docker pause command, which suspends all processes within specified containers.
tags:
    - docker
    - container-management
    - docker-pause
    - freezer-cgroup
    - process-suspension
category: reference
---

DescriptionPause all processes within one or more containersUsage`docker container pause CONTAINER [CONTAINER...]`Aliases

An alias is a short or memorable alternative for a longer command.

`docker pause`

## [Description](#description)

The `docker pause` command suspends all processes in the specified containers. On Linux, this uses the freezer cgroup. Traditionally, when suspending a process the `SIGSTOP` signal is used, which is observable by the process being suspended. With the freezer cgroup the process is unaware, and unable to capture, that it is being suspended, and subsequently resumed. On Windows, only Hyper-V containers can be paused.

See the [freezer cgroup documentation](https://www.kernel.org/doc/Documentation/cgroup-v1/freezer-subsystem.txt) for further details.

## [Examples](#examples)

```
$ docker pause my_container
```