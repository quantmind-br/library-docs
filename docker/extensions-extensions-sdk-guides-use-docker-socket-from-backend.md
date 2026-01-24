---
title: Use the Docker socket
url: https://docs.docker.com/extensions/extensions-sdk/guides/use-docker-socket-from-backend/
source: llms
fetched_at: 2026-01-24T14:28:03.467388538-03:00
rendered_js: false
word_count: 138
summary: This guide explains how to interact with the Docker Engine from an extension's backend by mounting the Docker socket inside the Docker Desktop virtual machine. It specifically recommends using the raw socket path to avoid host-level permission issues.
tags:
    - docker-desktop
    - extension-backend
    - docker-socket
    - socket-mounting
    - container-configuration
category: guide
---

## Use the Docker socket from the extension backend

Extensions can invoke Docker commands directly from the frontend with the SDK.

In some cases, it is useful to also interact with Docker Engine from the backend.

Extension backend containers can mount the Docker socket and use it to interact with Docker Engine from the extension backend logic. Learn more about the [Docker Engine socket](https://docs.docker.com/reference/cli/dockerd/#examples)

However, when mounting the Docker socket from an extension container that lives in the Desktop virtual machine, you want to mount the Docker socket from inside the VM, and not mount `/var/run/docker.sock` from the host filesystem (using the Docker socket from the host can lead to permission issues in containers).

In order to do so, you can use `/var/run/docker.sock.raw`. Docker Desktop mounts the socket that lives in the Desktop VM, and not from the host.

```
services:myExtension:image:${DESKTOP_PLUGIN_IMAGE}volumes:- /var/run/docker.sock.raw:/var/run/docker.sock
```