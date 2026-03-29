---
title: Debug a container
url: https://docs.docker.com/dhi/how-to/debug/
source: llms
fetched_at: 2026-01-24T14:20:34.487866467-03:00
rendered_js: false
word_count: 244
summary: This guide explains how to troubleshoot Docker Hardened Images by using the Docker Debug command to attach an ephemeral container with necessary tools.
tags:
    - docker
    - docker-hardened-images
    - debugging
    - troubleshooting
    - container-security
    - docker-debug
category: guide
---

## Debug a Docker Hardened Image container

Docker Hardened Images (DHI) prioritize minimalism and security, which means they intentionally leave out many common debugging tools (like shells or package managers). This makes direct troubleshooting difficult without introducing risk. To address this, you can use [Docker Debug](https://docs.docker.com/reference/cli/docker/debug/), a secure workflow that temporarily attaches an ephemeral debug container to a running service or image without modifying the original image.

This guide shows how to debug Docker Hardened Images locally during development. You can also debug containers remotely using the `--host` option.

The following example uses a mirrored `python:3.13` image, but the same steps apply to any image.

## [Step 1: Run a container from a Hardened Image](#step-1-run-a-container-from-a-hardened-image)

Start with a DHI-based container that simulates an issue:

```
$ docker run -d --name myapp dhi.io/python:3.13 python -c "import time; time.sleep(300)"
```

This container doesn't include a shell or tools like `ps`, `top`, or `cat`.

If you try:

```
$ docker exec -it myapp sh
```

You'll see:

```
exec: "sh": executable file not found in $PATH
```

## [Step 2: Use Docker Debug to inspect the container](#step-2-use-docker-debug-to-inspect-the-container)

Use the `docker debug` command to attach a temporary, tool-rich debug container to the running instance.

From here, you can inspect running processes, network status, or mounted files.

For example, to check running processes:

Exit the debug session with:

## [What's next](#whats-next)

Docker Debug helps you troubleshoot hardened containers without compromising the integrity of the original image. Because the debug container is ephemeral and separate, it avoids introducing security risks into production environments.

If you encounter issues related to permissions, ports, missing shells, or package managers, see [Troubleshoot Docker Hardened Images](https://docs.docker.com/dhi/troubleshoot/) for recommended solutions and workarounds.