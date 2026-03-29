---
title: Manage builders
url: https://docs.docker.com/build/builders/manage/
source: llms
fetched_at: 2026-01-24T14:15:29.588682121-03:00
rendered_js: false
word_count: 277
summary: This document explains how to create, inspect, and manage Docker Buildx builders using CLI commands and Docker Desktop.
tags:
    - docker-buildx
    - builder-management
    - build-drivers
    - buildkit
    - docker-cli
    - container-drivers
category: guide
---

You can create, inspect, and manage builders using `docker buildx` commands, or [using Docker Desktop](#manage-builders-with-docker-desktop).

The default builder uses the [`docker` driver](https://docs.docker.com/build/builders/drivers/docker/). You can't manually create new `docker` builders, but you can create builders that use other drivers, such as the [`docker-container` driver](https://docs.docker.com/build/builders/drivers/docker-container/), which runs the BuildKit daemon in a container.

Use the [`docker buildx create`](https://docs.docker.com/reference/cli/docker/buildx/create/) command to create a builder.

Buildx uses the `docker-container` driver by default if you omit the `--driver` flag. For more information about available drivers, see [Build drivers](https://docs.docker.com/build/builders/drivers/).

Use `docker buildx ls` to see builder instances available on your system, and the drivers they're using.

The asterisk (`*`) next to the builder name indicates the [selected builder](https://docs.docker.com/build/builders/#selected-builder).

To inspect a builder with the CLI, use `docker buildx inspect <name>`. You can only inspect a builder if the builder is active. You can add the `--bootstrap` flag to the command to start the builder.

If you want to see how much disk space a builder is using, use the `docker buildx du` command. By default, this command shows the total disk usage for all available builders. To see usage for a specific builder, use the `--builder` flag.

Use the [`docker buildx remove`](https://docs.docker.com/reference/cli/docker/buildx/create/) command to remove a builder.

If you remove your currently selected builder, the default `docker` builder is automatically selected. You can't remove the default builder.

Local build cache for the builder is also removed.

### [Removing remote builders](#removing-remote-builders)

Removing a remote builder doesn't affect the remote build cache. It also doesn't stop the remote BuildKit daemon. It only removes your connection to the builder.

If you have turned on the [Docker Desktop Builds view](https://docs.docker.com/desktop/use-desktop/builds/), you can inspect builders in [Docker Desktop settings](https://docs.docker.com/desktop/settings-and-maintenance/settings/#builders).