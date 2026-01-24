---
title: docker container rm
url: https://docs.docker.com/reference/cli/docker/container/rm/
source: llms
fetched_at: 2026-01-24T14:35:19.048758694-03:00
rendered_js: false
word_count: 357
summary: This document provides a reference for the docker container rm command, explaining how to delete containers along with their links and associated volumes.
tags:
    - docker-cli
    - container-management
    - docker-rm
    - resource-cleanup
    - volumes
category: reference
---

DescriptionRemove one or more containersUsage`docker container rm [OPTIONS] CONTAINER [CONTAINER...]`Aliases

An alias is a short or memorable alternative for a longer command.

`docker container remove` `docker rm`

Remove one or more containers

OptionDefaultDescription[`-f, --force`](#force)Force the removal of a running container (uses SIGKILL)[`-l, --link`](#link)Remove the specified link[`-v, --volumes`](#volumes)Remove anonymous volumes associated with the container

### [Remove a container](#remove-a-container)

This removes the container referenced under the link `/redis`.

### [Remove a link specified with `--link` on the default bridge network (--link)](#link)

This removes the underlying link between `/webapp` and the `/redis` containers on the default bridge network, removing all network communication between the two containers. This does not apply when `--link` is used with user-specified networks.

### [Force-remove a running container (--force)](#force)

This command force-removes a running container.

The main process inside the container referenced under the link `redis` will receive `SIGKILL`, then the container will be removed.

### [Remove all stopped containers](#remove-all-stopped-containers)

Use the [`docker container prune`](https://docs.docker.com/reference/cli/docker/container/prune/) command to remove all stopped containers, or refer to the [`docker system prune`](https://docs.docker.com/reference/cli/docker/system/prune/) command to remove unused containers in addition to other Docker resources, such as (unused) images and networks.

Alternatively, you can use the `docker ps` with the `-q` / `--quiet` option to generate a list of container IDs to remove, and use that list as argument for the `docker rm` command.

Combining commands can be more flexible, but is less portable as it depends on features provided by the shell, and the exact syntax may differ depending on what shell is used. To use this approach on Windows, consider using PowerShell or Bash.

The example below uses `docker ps -q` to print the IDs of all containers that have exited (`--filter status=exited`), and removes those containers with the `docker rm` command:

Or, using the `xargs` Linux utility:

### [Remove a container and its volumes (-v, --volumes)](#volumes)

This command removes the container and any volumes associated with it. Note that if a volume was specified with a name, it will not be removed.

### [Remove a container and selectively remove volumes](#remove-a-container-and-selectively-remove-volumes)

In this example, the volume for `/foo` remains intact, but the volume for `/bar` is removed. The same behavior holds for volumes inherited with `--volumes-from`.