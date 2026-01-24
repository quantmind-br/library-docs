---
title: Docker terminology
url: https://docs.docker.com/contribute/style/terminology/
source: llms
fetched_at: 2026-01-24T14:02:13.839540891-03:00
rendered_js: false
word_count: 242
summary: This document provides a glossary of terms and stylistic guidelines for terminology used within the Docker and Docker Compose ecosystem.
tags:
    - docker
    - docker-compose
    - glossary
    - terminology
    - documentation-standards
category: reference
---

#### [`compose.yaml`](#composeyaml)

The current designation for the Compose file, as it's a file, format as code.

#### [Compose plugin](#compose-plugin)

The compose plugin as an add-on (for Docker CLI) that can be enabled/disabled.

#### [Digest](#digest)

A long string that’s automatically created every time you push an image. You can pull an image by Digest or by Tag.

#### [Docker Compose](#docker-compose)

Use when we talk about the application, or all the functionality associated with the application.

#### [`docker compose`](#docker-compose-1)

Use code formatting for referring to the commands in text and command usage examples/code samples.

#### [Docker Compose CLI](#docker-compose-cli)

Use when referring to family of Compose commands as offered from the Docker CLI.

#### [K8s](#k8s)

Don't use. Use `Kubernetes` instead.

#### [Multi-platform](#multi-platform)

(broad meaning) Mac vs Linux vs Microsoft but also pair of platform architecture such as in Linux/amd64 and Linux/arm64; (narrow meaning) Windows/Linux/macOS.

#### [Multi-architecture / multi-arch](#multi-architecture--multi-arch)

To use when referring specifically to CPU architecture or something that is hardware-architecture-based. Avoid using it as meaning the same as multi-platform.

#### [Member](#member)

A user of Docker Hub that is a part of an organization

#### [Namespace](#namespace)

Organization or User name. Every image needs a namespace to live under.

#### [Node](#node)

A node is a physical or virtual machine running an instance of the Docker Engine in swarm mode. Manager nodes perform swarm management and orchestration duties. By default manager nodes are also worker nodes. Worker nodes invoke tasks.

#### [Registry](#registry)

Online storage for Docker images.

#### [Repository](#repository)

Lets users share container images with their team, customers, or Docker community.