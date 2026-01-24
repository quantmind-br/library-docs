---
title: Cache management
url: https://docs.docker.com/build/ci/github-actions/cache/
source: llms
fetched_at: 2026-01-24T14:16:22.001598275-03:00
rendered_js: false
word_count: 355
summary: This document explains how to configure various Docker build cache backends within GitHub Actions and provides instructions for upgrading tools to support the GitHub Cache service API v2.
tags:
    - docker-build
    - github-actions
    - cache-backends
    - buildkit
    - docker-cache
    - continuous-integration
category: guide
---

This page contains examples on using the cache storage backends with GitHub Actions.

In most cases you want to use the [inline cache exporter](https://docs.docker.com/build/cache/backends/inline/). However, note that the `inline` cache exporter only supports `min` cache mode. To use `max` cache mode, push the image and the cache separately using the registry cache exporter with the `cache-to` option, as shown in the [registry cache example](#registry-cache).

You can import/export cache from a cache manifest or (special) image configuration on the registry with the [registry cache exporter](https://docs.docker.com/build/cache/backends/registry/).

The [GitHub Actions cache exporter](https://docs.docker.com/build/cache/backends/gha/) backend uses the [GitHub Cache service API](https://github.com/tonistiigi/go-actions-cache) to fetch and upload cache blobs. That's why you should only use this cache backend in a GitHub Action workflow, as the `url` (`$ACTIONS_RESULTS_URL`) and `token` (`$ACTIONS_RUNTIME_TOKEN`) attributes only get populated in a workflow context.

Starting [April 15th, 2025, only GitHub Cache service API v2 will be supported](https://gh.io/gha-cache-sunset).

If you encounter the following error during your build:

You're probably using outdated tools that only support the legacy GitHub Cache service API v1. Here are the minimum versions you need to upgrade to depending on your use case:

- Docker Buildx &gt;= v0.21.0
- BuildKit &gt;= v0.20.0
- Docker Compose &gt;= v2.33.1
- Docker Engine &gt;= v28.0.0 (if you're building using the Docker driver with containerd image store enabled)

If you're building using the `docker/build-push-action` or `docker/bake-action` actions on GitHub hosted runners, Docker Buildx and BuildKit are already up to date but on self-hosted runners, you may need to update them yourself. Alternatively, you can use the `docker/setup-buildx-action` action to install the latest version of Docker Buildx:

If you're building using Docker Compose, you can use the `docker/setup-compose-action` action:

If you're building using the Docker Engine with the containerd image store enabled, you can use the `docker/setup-docker-action` action:

BuildKit doesn't preserve cache mounts in the GitHub Actions cache by default. To put your cache mounts into GitHub Actions cache and reuse it between builds, you can use a workaround provided by [`reproducible-containers/buildkit-cache-dance`](https://github.com/reproducible-containers/buildkit-cache-dance).

This GitHub Action creates temporary containers to extract and inject the cache mount data with your Docker build steps.

The following example shows how to use this workaround with a Go project.