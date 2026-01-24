---
title: Go
url: https://docs.docker.com/dhi/migration/examples/go/
source: llms
fetched_at: 2026-01-24T14:21:06.722441408-03:00
rendered_js: false
word_count: 97
summary: This document provides instructions for migrating Go applications to Docker Hardened Images, covering build strategies and authentication requirements.
tags:
    - go
    - docker
    - hardened-images
    - migration
    - container-security
    - multi-stage-builds
category: guide
---

This example shows how to migrate a Go application to Docker Hardened Images.

The following examples show Dockerfiles before and after migration to Docker Hardened Images. Each example includes five variations:

Multi-stage builds are recommended for most use cases. Single-stage builds are supported for simplicity, but come with tradeoffs in size and security.

You must authenticate to `dhi.io` before you can pull Docker Hardened Images. Use your Docker ID credentials (the same username and password you use for Docker Hub). If you don't have a Docker account, [create one](https://docs.docker.com/accounts/create-account/) for free.

Run `docker login dhi.io` to authenticate.