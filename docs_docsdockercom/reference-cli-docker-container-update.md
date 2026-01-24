---
title: docker container update
url: https://docs.docker.com/reference/cli/docker/container/update/
source: llms
fetched_at: 2026-01-24T14:35:33.605148271-03:00
rendered_js: false
word_count: 522
summary: This document provides a reference for the docker container update command, which allows users to dynamically modify resource constraints and configuration settings for running or stopped containers.
tags:
    - docker-cli
    - container-management
    - resource-limits
    - cpu-allocation
    - memory-management
    - docker-update
category: reference
---

DescriptionUpdate configuration of one or more containersUsage`docker container update [OPTIONS] CONTAINER [CONTAINER...]`Aliases

An alias is a short or memorable alternative for a longer command.

`docker update`

The `docker update` command dynamically updates container configuration. You can use this command to prevent containers from consuming too many resources from their Docker host. With a single command, you can place limits on a single container or on many. To specify more than one container, provide space-separated list of container names or IDs.

With the exception of the `--kernel-memory` option, you can specify these options on a running or a stopped container. On kernel version older than 4.6, you can only update `--kernel-memory` on a stopped container or on a running container with kernel memory initialized.

> The `docker update` and `docker container update` commands are not supported for Windows containers.

OptionDefaultDescription`--blkio-weight`Block IO (relative weight), between 10 and 1000, or 0 to disable (default 0)  
`--cpu-period`Limit CPU CFS (Completely Fair Scheduler) period`--cpu-quota`Limit CPU CFS (Completely Fair Scheduler) quota`--cpu-rt-period`API 1.25+ Limit the CPU real-time period in microseconds`--cpu-rt-runtime`API 1.25+ Limit the CPU real-time runtime in microseconds[`-c, --cpu-shares`](#cpu-shares)CPU shares (relative weight)`--cpus`API 1.29+ Number of CPUs`--cpuset-cpus`CPUs in which to allow execution (0-3, 0,1)`--cpuset-mems`MEMs in which to allow execution (0-3, 0,1)[`-m, --memory`](#memory)Memory limit`--memory-reservation`Memory soft limit`--memory-swap`Swap limit equal to memory plus swap: -1 to enable unlimited swap`--pids-limit`API 1.40+ Tune container pids limit (set -1 for unlimited)[`--restart`](#restart)Restart policy to apply when a container exits

The following sections illustrate ways to use this command.

### [Update a container's cpu-shares (--cpu-shares)](#cpu-shares)

To limit a container's cpu-shares to 512, first identify the container name or ID. You can use `docker ps` to find these values. You can also use the ID returned from the `docker run` command. Then, do the following:

### [Update a container with cpu-shares and memory (-m, --memory)](#memory)

To update multiple resource configurations for multiple containers:

### [Update a container's kernel memory constraints (--kernel-memory)](#kernel-memory)

You can update a container's kernel memory limit using the `--kernel-memory` option. On kernel version older than 4.6, this option can be updated on a running container only if the container was started with `--kernel-memory`. If the container was started without `--kernel-memory` you need to stop the container before updating kernel memory.

> The `--kernel-memory` option has been deprecated since Docker 20.10.

For example, if you started a container with this command:

You can update kernel memory while the container is running:

If you started a container without kernel memory initialized:

Update kernel memory of running container `test2` will fail. You need to stop the container before updating the `--kernel-memory` setting. The next time you start it, the container uses the new value.

Kernel version newer than (include) 4.6 does not have this limitation, you can use `--kernel-memory` the same way as other options.

### [Update a container's restart policy (--restart)](#restart)

You can change a container's restart policy on a running container. The new restart policy takes effect instantly after you run `docker update` on a container.

To update restart policy for one or more containers:

Note that if the container is started with `--rm` flag, you cannot update the restart policy for it. The `AutoRemove` and `RestartPolicy` are mutually exclusive for the container.