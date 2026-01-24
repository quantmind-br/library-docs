---
title: Container Device Interface (CDI)
url: https://docs.docker.com/build/building/cdi/
source: llms
fetched_at: 2026-01-24T14:15:39.437722926-03:00
rendered_js: false
word_count: 675
summary: This document explains the Container Device Interface (CDI) specification and provides a step-by-step guide on configuring hardware devices like GPUs for use in container builds using Docker and Buildx.
tags:
    - cdi
    - docker-buildx
    - gpu-acceleration
    - container-device-interface
    - hardware-acceleration
    - buildkit
category: tutorial
---

The [Container Device Interface (CDI)](https://github.com/cncf-tags/container-device-interface/blob/main/SPEC.md) is a specification designed to standardize how devices (like GPUs, FPGAs, and other hardware accelerators) are exposed to and used by containers. The aim is to provide a more consistent and secure mechanism for using hardware devices in containerized environments, addressing the challenges associated with device-specific setups and configurations.

In addition to enabling the container to interact with the device node, CDI also lets you specify additional configuration for the device, such as environment variables, host mounts (such as shared objects), and executable hooks.

To get started with CDI, you need to have a compatible environment set up. This includes having Docker v27+ installed with [CDI configured](https://docs.docker.com/reference/cli/dockerd/#configure-cdi-devices) and Buildx v0.22+.

You also need to create the [device specifications using JSON or YAML files](https://github.com/cncf-tags/container-device-interface/blob/main/SPEC.md#cdi-json-specification) in one of the following locations:

- `/etc/cdi`
- `/var/run/cdi`
- `/etc/buildkit/cdi`

> Location can be changed by setting the `specDirs` option in the `cdi` section of the [`buildkitd.toml` configuration file](https://docs.docker.com/build/buildkit/configure/) if you are using BuildKit directly. If you're building using the Docker Daemon with the `docker` driver, see [Configure CDI devices](https://docs.docker.com/reference/cli/dockerd/#configure-cdi-devices) documentation.

> If you are creating a container builder on WSL, you need to ensure that [Docker Desktop](https://docs.docker.com/desktop/) is installed and [WSL 2 GPU Paravirtualization](https://docs.docker.com/desktop/features/gpu/#prerequisites) is enabled. Buildx v0.27+ is also required to mount the WSL libraries in the container.

Let's start with a simple CDI specification that injects an environment variable into the build environment and write it to `/etc/cdi/foo.yaml`:

Inspect the `default` builder to verify that `vendor1.com/device` is detected as a device:

Now let's create a Dockerfile to use this device:

Here we use the [`RUN --device` command](https://docs.docker.com/reference/dockerfile/#run---device) and set `vendor1.com/device` which requests the first device available in the specification. In this case it uses `foo`, which is the first device in `/etc/cdi/foo.yaml`.

> [`RUN --device` command](https://docs.docker.com/reference/dockerfile/#run---device) is only featured in [`labs` channel](https://docs.docker.com/build/buildkit/frontend/#labs-channel) since [Dockerfile frontend v1.14.0-labs](https://github.com/moby/buildkit/releases/tag/dockerfile%2F1.14.0-labs) and not yet available in stable syntax.

Now let's build this Dockerfile:

It fails because the device `vendor1.com/device=foo` is not automatically allowed by the build as shown in the `buildx inspect` output above:

To allow the device, you can use the [`--allow` flag](https://docs.docker.com/reference/cli/docker/buildx/build/#allow) with the `docker buildx build` command:

Or you can set the `org.mobyproject.buildkit.device.autoallow` annotation in the CDI specification to automatically allow the device for all builds:

Now running the build again with the `--allow device` flag:

The build is successful and the output shows that the `FOO` environment variable was injected into the build environment as specified in the CDI specification.

In this section, we will show you how to set up a [container builder](https://docs.docker.com/build/builders/drivers/docker-container/) using NVIDIA GPUs. Since Buildx v0.22, when creating a new container builder, a GPU request is automatically added to the container builder if the host has GPU drivers installed in the kernel. This is similar to using [`--gpus=all` with the `docker run`](https://docs.docker.com/reference/cli/docker/container/run/#gpus) command.

Now let's create a container builder named `gpubuilder` using Buildx:

> We made a specially crafted BuildKit image because the current BuildKit release image is based on Alpine that doesn't support NVIDIA drivers. The following image is based on Ubuntu and installs the NVIDIA client libraries and generates the CDI specification for your GPU in the container builder if a device is requested during a build.

Let's inspect this builder:

We can see `nvidia.com/gpu` vendor is detected as a device in the builder which means that drivers were detected.

Optionally you can check if NVIDIA GPU devices are available in the container using `nvidia-smi`:

Let's create a simple Dockerfile that will use the GPU device:

Now run the build using the `gpubuilder` builder we created earlier:

As you might have noticed, the step `#7` is preparing the `nvidia.com/gpu` device by installing client libraries and the toolkit to generate the CDI specifications for the GPU.

The `nvidia-smi -L` command is then executed in the container using the GPU device. The output shows the GPU UUID.

You can check the generated CDI specification within the container builder with the following command:

For the EC2 instance [`g4dn.xlarge`](https://aws.amazon.com/ec2/instance-types/g4/) used here, it looks like this:

Congrats on your first build using a GPU device with BuildKit and CDI.