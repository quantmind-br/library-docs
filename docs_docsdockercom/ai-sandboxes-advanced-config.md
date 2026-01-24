---
title: Advanced
url: https://docs.docker.com/ai/sandboxes/advanced-config/
source: llms
fetched_at: 2026-01-24T14:14:23.010010597-03:00
rendered_js: false
word_count: 675
summary: This document provides advanced configuration instructions for Docker sandboxed agents, covering lifecycle management, Docker socket access, environment variables, and volume mounts. It also explains how to create custom sandbox templates using Dockerfiles to streamline specialized development environments.
tags:
    - docker-sandbox
    - agent-configuration
    - docker-socket
    - volume-mounts
    - environment-variables
    - sandbox-management
category: guide
---

## Advanced configurations

Availability: Experimental

Requires: Docker Desktop [4.50](https://docs.docker.com/desktop/release-notes/#4500) or later

This guide covers advanced configurations for sandboxed agents running locally.

### [Recreating sandboxes](#recreating-sandboxes)

Since Docker enforces one sandbox per workspace, the same sandbox is reused each time you run `docker sandbox run <agent>` in a given directory. To create a fresh sandbox, you need to remove the existing one first:

### [When to recreate sandboxes](#when-to-recreate-sandboxes)

Sandboxes remember their initial configuration and don't pick up changes from subsequent `docker sandbox run` commands. You must recreate the sandbox to modify:

- Environment variables (the `-e` flag)
- Volume mounts (the `-v` flag)
- Docker socket access (the `--mount-docker-socket` flag)
- Credentials mode (the `--credentials` flag)

### [Listing and inspecting sandboxes](#listing-and-inspecting-sandboxes)

View all your sandboxes:

Get detailed information about a specific sandbox:

This shows the sandbox's configuration, including environment variables, volumes, and creation time.

### [Removing sandboxes](#removing-sandboxes)

Remove a specific sandbox:

Remove all sandboxes at once:

This is useful for cleanup when you're done with a project or want to start fresh.

Mount the Docker socket to give agents access to Docker commands inside the container. The agent can build images, run containers, and work with Docker Compose setups.

> Mounting the Docker socket grants the agent full access to your Docker daemon, which has root-level privileges on your system. The agent can start or stop any container, access volumes, and potentially escape the sandbox. Only use this option when you fully trust the code the agent is working with.

### [Enable Docker socket access](#enable-docker-socket-access)

Use the `--mount-docker-socket` flag:

This mounts your host's Docker socket (`/var/run/docker.sock`) into the container, giving the agent access to Docker commands.

> The agent can see and interact with all containers on your host, not just those created within the sandbox.

### [Example: Testing a containerized application](#example-testing-a-containerized-application)

If your project has a Dockerfile, the agent can build and test it:

Example conversation:

### [What agents can do with Docker socket access](#what-agents-can-do-with-docker-socket-access)

With Docker access enabled, agents can:

- Start multi-container applications with Docker Compose
- Build images for multiple architectures
- Manage existing containers on your host
- Validate Dockerfiles and test build processes

Pass environment variables to configure the sandbox environment with the `-e` flag:

These variables are available to all processes in the container, including the agent and any commands it runs. Use multiple `-e` flags for multiple variables.

### [Example: Development environment setup](#example-development-environment-setup)

Set up a complete development environment:

Example conversation:

### [Common use cases](#common-use-cases)

API keys for testing:

> Only use test/development API keys in sandboxes, never production keys.

Loading from .env files:

Sandboxes don't automatically load `.env` files from your workspace, but you can ask Claude to use them:

Claude can use `dotenv` tools or source the file directly.

Mount additional directories or files to share data beyond your main workspace. Use the `-v` flag with the syntax `host-path:container-path`:

This makes `~/datasets` available at `/data` inside the container. The agent can read and write files in this location.

Read-only mounts:

Add `:ro` to prevent modifications:

Multiple mounts:

Use multiple `-v` flags to mount several locations:

### [Example: Machine learning workflow](#example-machine-learning-workflow)

Set up an ML environment with shared datasets, model storage, and persistent caches:

This provides read-only access to datasets (preventing accidental modifications), read-write access to save trained models, and a persistent pip cache for faster package installs across sessions.

Example conversation:

### [Common use cases](#common-use-cases-1)

Shared configuration files:

Build caches:

Custom tools:

Create custom sandbox templates to reuse configured environments. Instead of installing tools every time you start an agent, build a Docker image with everything pre-installed:

Build the image, and use the [`docker sandbox run --template`](https://docs.docker.com/reference/cli/docker/sandbox/run#template) flag to start a new sandbox based on the image.

### [Using standard images](#using-standard-images)

You can use standard Docker images as sandbox templates, but they don't include agent binaries, shell configuration, or runtime dependencies that Docker's sandbox templates provide. Using a standard Python image directly fails:

To use a standard image, create a Dockerfile that installs the agent binary, dependencies, and shell configuration on top of your base image. This approach makes sense when you need a specific base image (for example, an exact OS version or a specialized image with particular build tools).