---
title: Docker container driver
url: https://docs.docker.com/build/builders/drivers/docker-container/
source: llms
fetched_at: 2026-01-24T14:15:25.590364073-03:00
rendered_js: false
word_count: 435
summary: This document explains how to use and configure the Docker container driver for Buildx to create a managed BuildKit environment. It details the driver's advantages, such as multi-arch builds and cache persistence, and provides a reference for resource and network configuration parameters.
tags:
    - docker-buildx
    - buildkit
    - container-driver
    - multi-arch-builds
    - cache-persistence
    - docker-networking
    - resource-constraints
category: guide
---

The Docker container driver allows creation of a managed and customizable BuildKit environment in a dedicated Docker container.

Using the Docker container driver has a couple of advantages over the default Docker driver. For example:

- Specify custom BuildKit versions to use.
- Build multi-arch images, see [QEMU](#qemu)
- Advanced options for [cache import and export](https://docs.docker.com/build/cache/backends/)

Run the following command to create a new builder, named `container`, that uses the Docker container driver:

The following table describes the available driver-specific options that you can pass to `--driver-opt`:

ParameterTypeDefaultDescription`image`StringSets the BuildKit image to use for the container.`memory`StringSets the amount of memory the container can use.`memory-swap`StringSets the memory swap limit for the container.`cpu-quota`StringImposes a CPU CFS quota on the container.`cpu-period`StringSets the CPU CFS scheduler period for the container.`cpu-shares`StringConfigures CPU shares (relative weight) of the container.`cpuset-cpus`StringLimits the set of CPU cores the container can use.`cpuset-mems`StringLimits the set of CPU memory nodes the container can use.`default-load`Boolean`false`Automatically load images to the Docker Engine image store.`network`StringSets the network mode for the container.`cgroup-parent`String`/docker/buildx`Sets the cgroup parent of the container if Docker is using the "cgroupfs" driver.`restart-policy`String`unless-stopped`Sets the container's [restart policy](https://docs.docker.com/engine/containers/start-containers-automatically/#use-a-restart-policy).`env.<key>`StringSets the environment variable `key` to the specified `value` in the container.`provenance-add-gha`Boolean`true`Automatically writes GitHub Actions context into the builder for provenance.

Before you configure the resource limits for the container, read about [configuring runtime resource constraints for containers](https://docs.docker.com/engine/containers/resource_constraints/).

When you run a build, Buildx pulls the specified `image` (by default, [`moby/buildkit`](https://hub.docker.com/r/moby/buildkit)). When the container has started, Buildx submits the build submitted to the containerized build server.

The `docker-container` driver supports cache persistence, as it stores all the BuildKit state and related cache into a dedicated Docker volume.

To persist the `docker-container` driver's cache, even after recreating the driver using `docker buildx rm` and `docker buildx create`, you can destroy the builder using the `--keep-state` flag:

For example, to create a builder named `container` and then remove it while persisting state:

The `docker-container` driver supports using [QEMU](https://www.qemu.org/) (user mode) to build non-native platforms. Use the `--platform` flag to specify which architectures that you want to build for.

For example, to build a Linux image for `amd64` and `arm64`:

> Emulation with QEMU can be much slower than native builds, especially for compute-heavy tasks like compilation and compression or decompression.

You can customize the network that the builder container uses. This is useful if you need to use a specific network for your builds.

For example, let's [create a network](https://docs.docker.com/reference/cli/docker/network/create/) named `foonet`:

Now create a [`docker-container` builder](https://docs.docker.com/reference/cli/docker/buildx/create/) that will use this network:

Boot and [inspect `mybuilder`](https://docs.docker.com/reference/cli/docker/buildx/inspect/):

[Inspect the builder container](https://docs.docker.com/reference/cli/docker/inspect/) and see what network is being used:

For more information on the Docker container driver, see the [buildx reference](https://docs.docker.com/reference/cli/docker/buildx/create/#driver).