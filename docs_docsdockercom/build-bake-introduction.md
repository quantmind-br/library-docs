---
title: Introduction
url: https://docs.docker.com/build/bake/introduction/
source: llms
fetched_at: 2026-01-24T14:15:14.493352189-03:00
rendered_js: false
word_count: 343
summary: This document introduces Bake, a tool within Docker Buildx designed to simplify and manage complex container build configurations through structured HCL, YAML, or JSON files.
tags:
    - bake
    - docker-buildx
    - containerization
    - build-management
    - hcl
    - docker-build
category: concept
---

## Introduction to Bake

Bake is an abstraction for the `docker build` command that lets you more easily manage your build configuration (CLI flags, environment variables, etc.) in a consistent way for everyone on your team.

Bake is a command built into the Buildx CLI, so as long as you have Buildx installed, you also have access to bake, via the `docker buildx bake` command.

Here's a simple example of a `docker build` command:

This command builds the Dockerfile in the current directory and tags the resulting image as `myapp:latest`.

To express the same build configuration using Bake:

Bake provides a structured way to manage your build configuration, and it saves you from having to remember all the CLI flags for `docker build` every time. With this file, building the image is as simple as running:

For simple builds, the difference between `docker build` and `docker buildx bake` is minimal. However, as your build configuration grows more complex, Bake provides a more structured way to manage that complexity, that would be difficult to manage with CLI flags for the `docker build`. It also provides a way to share build configurations across your team, so that everyone is building images in a consistent way, with the same configuration.

You can write Bake files in HCL, YAML (Docker Compose files), or JSON. In general, HCL is the most expressive and flexible format, which is why you'll see it used in most of the examples in this documentation, and in projects that use Bake.

The properties that can be set for a target closely resemble the CLI flags for `docker build`. For instance, consider the following `docker build` command:

The Bake equivalent would be:

> Want a better editing experience for Bake files in VS Code? Check out the [Docker VS Code Extension (Beta)](https://marketplace.visualstudio.com/items?itemName=docker.docker) for linting, code navigation, and vulnerability scanning.

To learn more about using Bake, see the following topics:

- Learn how to define and use [targets](https://docs.docker.com/build/bake/targets/) in Bake
- To see all the properties that can be set for a target, refer to the [Bake file reference](https://docs.docker.com/build/bake/reference/).