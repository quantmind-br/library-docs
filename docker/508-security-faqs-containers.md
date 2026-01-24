---
title: Container
url: https://docs.docker.com/security/faqs/containers/
source: llms
fetched_at: 2026-01-24T14:29:41.257751745-03:00
rendered_js: false
word_count: 225
summary: This document explains how Docker Desktop handles container isolation from the host machine and manages filesystem access permissions. It details the security mechanisms involved, including the Linux virtual machine and Enhanced Container Isolation features.
tags:
    - docker-desktop
    - container-security
    - isolation
    - host-access
    - linux-vm
    - enhanced-container-isolation
category: reference
---

## Container security FAQs

Table of contents

* * *

## [How are containers isolated from the host in Docker Desktop?](#how-are-containers-isolated-from-the-host-in-docker-desktop)

Docker Desktop runs all containers inside a customized Linux virtual machine (except for native Windows containers). This adds strong isolation between containers and the host machine, even when containers run as root.

Important considerations include:

- Containers have access to host files configured for file sharing via Docker Desktop settings
- Containers run as root with limited capabilities inside the Docker Desktop VM by default
- Privileged containers (`--privileged`, `--pid=host`, `--cap-add`) run with elevated privileges inside the VM, giving them access to VM internals and Docker Engine

With Enhanced Container Isolation turned on, each container runs in a dedicated Linux user namespace inside the Docker Desktop VM. Even privileged containers only have privileges within their container boundary, not the VM. ECI uses advanced techniques to prevent containers from breaching the Docker Desktop VM and Docker Engine.

## [Which portions of the host filesystem can containers access?](#which-portions-of-the-host-filesystem-can-containers-access)

Containers can only access host files that are:

1. Shared using Docker Desktop settings
2. Explicitly bind-mounted into the container (e.g., `docker run -v /path/to/host/file:/mnt`)

## [Can containers running as root access admin-owned files on the host?](#can-containers-running-as-root-access-admin-owned-files-on-the-host)

No. Host file sharing uses a user-space file server (running in `com.docker.backend` as the Docker Desktop user), so containers can only access files that the Docker Desktop user already has permission to access.