---
title: Named contexts
url: https://docs.docker.com/build/ci/github-actions/named-contexts/
source: llms
fetched_at: 2026-01-24T14:16:37.604206442-03:00
rendered_js: false
word_count: 159
summary: This document explains how to utilize named build contexts in GitHub Actions to manage image dependencies and reuse build outputs across workflow steps. It provides practical examples for pinning image tags and configuring build drivers to handle local registries.
tags:
    - docker
    - github-actions
    - docker-buildx
    - build-contexts
    - ci-cd
    - container-images
category: guide
---

## Named contexts with GitHub Actions

You can define [additional build contexts](https://docs.docker.com/reference/cli/docker/buildx/build/#build-context), and access them in your Dockerfile with `FROM name` or `--from=name`. When Dockerfile defines a stage with the same name it's overwritten.

This can be useful with GitHub Actions to reuse results from other builds or pin an image to a specific tag in your workflow.

## [Pin image to a tag](#pin-image-to-a-tag)

Replace `alpine:latest` with a pinned one:

```
# syntax=docker/dockerfile:1FROMalpineRUN echo "Hello World"
```

```
name:cion:push:jobs:docker:runs-on:ubuntu-lateststeps:- name:Set up Docker Buildxuses:docker/setup-buildx-action@v3- name:Builduses:docker/build-push-action@v6with:build-contexts:|            alpine=docker-image://alpine:3.21tags:myimage:latest
```

## [Use image in subsequent steps](#use-image-in-subsequent-steps)

By default, the [Docker Setup Buildx](https://github.com/marketplace/actions/docker-setup-buildx) action uses `docker-container` as a build driver, so built Docker images aren't loaded automatically.

With named contexts you can reuse the built image:

```
# syntax=docker/dockerfile:1FROMalpineRUN echo "Hello World"
```

```
name:cion:push:jobs:docker:runs-on:ubuntu-lateststeps:- name:Set up Docker Buildxuses:docker/setup-buildx-action@v3with:driver:docker- name:Build base imageuses:docker/build-push-action@v6with:context:"{{defaultContext}}:base"load:truetags:my-base-image:latest- name:Builduses:docker/build-push-action@v6with:build-contexts:|            alpine=docker-image://my-base-image:latesttags:myimage:latest
```

## [Using with a container builder](#using-with-a-container-builder)

As shown in the previous section we are not using the default [`docker-container` driver](https://docs.docker.com/build/builders/drivers/docker-container/) for building with named contexts. That's because this driver can't load an image from the Docker store as it's isolated. To solve this problem you can use a [local registry](https://docs.docker.com/build/ci/github-actions/local-registry/) to push your base image in your workflow:

```
# syntax=docker/dockerfile:1FROMalpineRUN echo "Hello World"
```

```
name:cion:push:jobs:docker:runs-on:ubuntu-latestservices:registry:image:registry:3ports:- 5000:5000steps:- name:Set up QEMUuses:docker/setup-qemu-action@v3- name:Set up Docker Buildxuses:docker/setup-buildx-action@v3with:# network=host driver-opt needed to push to local registrydriver-opts:network=host- name:Build base imageuses:docker/build-push-action@v6with:context:"{{defaultContext}}:base"tags:localhost:5000/my-base-image:latestpush:true- name:Builduses:docker/build-push-action@v6with:build-contexts:|            alpine=docker-image://localhost:5000/my-base-image:latesttags:myimage:latest
```