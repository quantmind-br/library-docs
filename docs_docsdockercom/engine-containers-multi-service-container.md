---
title: Run multiple processes in a container
url: https://docs.docker.com/engine/containers/multi-service_container/
source: llms
fetched_at: 2026-01-24T14:22:37.652033807-03:00
rendered_js: false
word_count: 384
summary: This document explains best practices and various methods for managing single or multiple processes within a Docker container, including lifecycle handling and process management tools.
tags:
    - docker-containers
    - process-management
    - dockerfile-best-practices
    - container-init
    - supervisord
    - multi-service-containers
category: guide
---

A container's main running process is the `ENTRYPOINT` and/or `CMD` at the end of the `Dockerfile`. It's best practice to separate areas of concern by using one service per container. That service may fork into multiple processes (for example, Apache web server starts multiple worker processes). It's ok to have multiple processes, but to get the most benefit out of Docker, avoid one container being responsible for multiple aspects of your overall application. You can connect multiple containers using user-defined networks and shared volumes.

The container's main process is responsible for managing all processes that it starts. In some cases, the main process isn't well-designed, and doesn't handle "reaping" (stopping) child processes gracefully when the container exits. If your process falls into this category, you can use the `--init` option when you run the container. The `--init` flag inserts a tiny init-process into the container as the main process, and handles reaping of all processes when the container exits. Handling such processes this way is superior to using a full-fledged init process such as `sysvinit` or `systemd` to handle process lifecycle within your container.

If you need to run more than one service within a container, you can achieve this in a few different ways.

Put all of your commands in a wrapper script, complete with testing and debugging information. Run the wrapper script as your `CMD`. The following is a naive example. First, the wrapper script:

Next, the Dockerfile:

If you have one main process that needs to start first and stay running but you temporarily need to run some other processes (perhaps to interact with the main process) then you can use bash's job control. First, the wrapper script:

Use a process manager like `supervisord`. This is more involved than the other options, as it requires you to bundle `supervisord` and its configuration into your image (or base your image on one that includes `supervisord`), along with the different applications it manages. Then you start `supervisord`, which manages your processes for you.

The following Dockerfile example shows this approach. The example assumes that these files exist at the root of the build context:

- `supervisord.conf`
- `my_first_process`
- `my_second_process`

If you want to make sure both processes output their `stdout` and `stderr` to the container logs, you can add the following to the `supervisord.conf` file: