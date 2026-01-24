---
title: BuildKit configuration
url: https://docs.docker.com/build/ci/github-actions/configure-builder/
source: llms
fetched_at: 2026-01-24T14:16:24.290592654-03:00
rendered_js: false
word_count: 632
summary: This document provides detailed instructions for configuring BuildKit instances and Docker Buildx builders within GitHub Actions, covering version pinning, authentication, and node management.
tags:
    - github-actions
    - docker-buildx
    - buildkit
    - ci-cd
    - builder-configuration
    - remote-builders
category: configuration
---

## Configuring your GitHub Actions builder

This page contains instructions on configuring your BuildKit instances when using our [Setup Buildx Action](https://github.com/docker/setup-buildx-action).

By default, the action will attempt to use the latest version of [Buildx](https://github.com/docker/buildx) available on the GitHub Runner (the build client) and the latest release of [BuildKit](https://github.com/moby/buildkit) (the build server).

To pin to a specific version of Buildx, use the `version` input. For example, to pin to Buildx v0.10.0:

To pin to a specific version of BuildKit, use the `image` option in the `driver-opts` input. For example, to pin to BuildKit v0.11.0:

To display BuildKit container logs when using the `docker-container` driver, you must either [enable step debug logging](https://docs.github.com/en/actions/monitoring-and-troubleshooting-workflows/enabling-debug-logging#enabling-step-debug-logging), or set the `--debug` buildkitd flag in the [Docker Setup Buildx](https://github.com/marketplace/actions/docker-setup-buildx) action:

Logs will be available at the end of a job:

![BuildKit container logs](https://docs.docker.com/build/ci/github-actions/images/buildkit-container-logs.png)

![BuildKit container logs](https://docs.docker.com/build/ci/github-actions/images/buildkit-container-logs.png)

You can provide a [BuildKit configuration](https://docs.docker.com/build/buildkit/toml-configuration/) to your builder if you're using the [`docker-container` driver](https://docs.docker.com/build/builders/drivers/docker-container/) (default) with the `config` or `buildkitd-config-inline` inputs:

### [Registry mirror](#registry-mirror)

You can configure a registry mirror using an inline block directly in your workflow with the `buildkitd-config-inline` input:

For more information about using a registry mirror, see [Registry mirror](https://docs.docker.com/build/buildkit/configure/#registry-mirror).

### [Max parallelism](#max-parallelism)

You can limit the parallelism of the BuildKit solver which is particularly useful for low-powered machines.

You can use the `buildkitd-config-inline` input like the previous example, or you can use a dedicated BuildKit config file from your repository if you want with the `config` input:

Buildx supports running builds on multiple machines. This is useful for building [multi-platform images](https://docs.docker.com/build/building/multi-platform/) on native nodes for more complicated cases that aren't handled by QEMU. Building on native nodes generally has better performance, and allows you to distribute the build across multiple machines.

You can append nodes to the builder you're creating using the `append` option. It takes input in the form of a YAML string document to remove limitations intrinsically linked to GitHub Actions: you can only use strings in the input fields:

NameTypeDescription`name`String[Name of the node](https://docs.docker.com/reference/cli/docker/buildx/create/#node). If empty, it's the name of the builder it belongs to, with an index number suffix. This is useful to set it if you want to modify/remove a node in an underlying step of you workflow.`endpoint`String[Docker context or endpoint](https://docs.docker.com/reference/cli/docker/buildx/create/#description) of the node to add to the builder`driver-opts`ListList of additional [driver-specific options](https://docs.docker.com/reference/cli/docker/buildx/create/#driver-opt)`buildkitd-flags`String[Flags for buildkitd](https://docs.docker.com/reference/cli/docker/buildx/create/#buildkitd-flags) daemon`platforms`StringFixed [platforms](https://docs.docker.com/reference/cli/docker/buildx/create/#platform) for the node. If not empty, values take priority over the detected ones.

Here is an example using remote nodes with the [`remote` driver](https://docs.docker.com/build/builders/drivers/remote/) and [TLS authentication](#tls-authentication):

The following examples show how to handle authentication for remote builders, using SSH or TLS.

### [SSH authentication](#ssh-authentication)

To be able to connect to an SSH endpoint using the [`docker-container` driver](https://docs.docker.com/build/builders/drivers/docker-container/), you have to set up the SSH private key and configuration on the GitHub Runner:

### [TLS authentication](#tls-authentication)

You can also [set up a remote BuildKit instance](https://docs.docker.com/build/builders/drivers/remote/#example-remote-buildkit-in-docker-container) using the remote driver. To ease the integration in your workflow, you can use an environment variables that sets up authentication using the BuildKit client certificates for the `tcp://`:

- `BUILDER_NODE_<idx>_AUTH_TLS_CACERT`
- `BUILDER_NODE_<idx>_AUTH_TLS_CERT`
- `BUILDER_NODE_<idx>_AUTH_TLS_KEY`

The `<idx>` placeholder is the position of the node in the list of nodes.

If you don't have the Docker CLI installed on the GitHub Runner, the Buildx binary gets invoked directly, instead of calling it as a Docker CLI plugin. This can be useful if you want to use the `kubernetes` driver in your self-hosted runner:

The following example shows how you can select different builders for different jobs.

An example scenario where this might be useful is when you are using a monorepo, and you want to pinpoint different packages to specific builders. For example, some packages may be particularly resource-intensive to build and require more compute. Or they require a builder equipped with a particular capability or hardware.

For more information about remote builder, see [`remote` driver](https://docs.docker.com/build/builders/drivers/remote/) and the [append builder nodes example](#append-additional-nodes-to-the-builder).