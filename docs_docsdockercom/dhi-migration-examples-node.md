---
title: Node.js
url: https://docs.docker.com/dhi/migration/examples/node/
source: llms
fetched_at: 2026-01-24T14:21:06.984104735-03:00
rendered_js: false
word_count: 97
summary: This document provides instructions on migrating Node.js applications to Docker Hardened Images, covering build configurations and authentication requirements.
tags:
    - node-js
    - docker
    - hardened-images
    - container-security
    - migration-guide
    - dockerfile
category: guide
---

This example shows how to migrate a Node.js application to Docker Hardened Images.

The following examples show Dockerfiles before and after migration to Docker Hardened Images. Each example includes five variations:

Multi-stage builds are recommended for most use cases. Single-stage builds are supported for simplicity, but come with tradeoffs in size and security.

You must authenticate to `dhi.io` before you can pull Docker Hardened Images. Use your Docker ID credentials (the same username and password you use for Docker Hub). If you don't have a Docker account, [create one](https://docs.docker.com/accounts/create-account/) for free.

Run `docker login dhi.io` to authenticate.