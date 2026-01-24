---
title: Use lifecycle hooks
url: https://docs.docker.com/compose/how-tos/lifecycle/
source: llms
fetched_at: 2026-01-24T14:17:37.119123235-03:00
rendered_js: false
word_count: 261
summary: This document explains how to implement and use service lifecycle hooks in Docker Compose to execute commands automatically after a container starts or before it stops.
tags:
    - docker-compose
    - lifecycle-hooks
    - post-start
    - pre-stop
    - container-orchestration
    - yaml-configuration
category: guide
---

## Using lifecycle hooks with Compose

Table of contents

* * *

Requires: Docker Compose [2.30.0](https://github.com/docker/compose/releases/tag/v2.30.0) and later

## [Services lifecycle hooks](#services-lifecycle-hooks)

When Docker Compose runs a container, it uses two elements, [ENTRYPOINT and COMMAND](https://docs.docker.com/engine/containers/run/#default-command-and-options), to manage what happens when the container starts and stops.

However, it can sometimes be easier to handle these tasks separately with lifecycle hooks - commands that run right after the container starts or just before it stops.

Lifecycle hooks are particularly useful because they can have special privileges (like running as the root user), even when the container itself runs with lower privileges for security. This means that certain tasks requiring higher permissions can be done without compromising the overall security of the container.

### [Post-start hooks](#post-start-hooks)

Post-start hooks are commands that run after the container has started, but there's no set time for when exactly they will execute. The hook execution timing is not assured during the execution of the container's `entrypoint`.

In the example provided:

- The hook is used to change the ownership of a volume to a non-root user (because volumes are created with root ownership by default).
- After the container starts, the `chown` command changes the ownership of the `/data` directory to user `1001`.

```
services:app:image:backenduser:1001volumes:- data:/data    post_start:- command:chown -R /data 1001:1001user:rootvolumes:data:{}# a Docker volume is created with root ownership
```

### [Pre-stop hooks](#pre-stop-hooks)

Pre-stop hooks are commands that run before the container is stopped by a specific command (like `docker compose down` or stopping it manually with `Ctrl+C`). These hooks won't run if the container stops by itself or gets killed suddenly.

In the following example, before the container stops, the `./data_flush.sh` script is run to perform any necessary cleanup.

```
services:app:image:backendpre_stop:- command:./data_flush.sh
```

## [Reference information](#reference-information)

- [`post_start`](https://docs.docker.com/reference/compose-file/services/#post_start)
- [`pre_stop`](https://docs.docker.com/reference/compose-file/services/#pre_stop)