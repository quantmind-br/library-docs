---
title: Build multi-arch extensions
url: https://docs.docker.com/extensions/extensions-sdk/extensions/multi-arch/
source: llms
fetched_at: 2026-01-24T14:27:50.5240633-03:00
rendered_js: false
word_count: 431
summary: This document explains how to build and configure multi-platform Docker extensions to ensure compatibility across different system architectures and operating systems.
tags:
    - docker-extensions
    - multi-platform
    - arm64
    - amd64
    - docker-buildx
    - metadata-json
category: guide
---

It is highly recommended that, at a minimum, your extension is supported for the following architectures:

- `linux/amd64`
- `linux/arm64`

Docker Desktop retrieves the extension image according to the user’s system architecture. If the extension does not provide an image that matches the user’s system architecture, Docker Desktop is not able to install the extension. As a result, users can’t run the extension in Docker Desktop.

If you created an extension from the `docker extension init` command, the `Makefile` at the root of the directory includes a target with name `push-extension`.

You can run `make push-extension` to build your extension against both `linux/amd64` and `linux/arm64` platforms, and push them to Docker Hub.

For example:

Alternatively, if you started from an empty directory, use the command below to build your extension for multiple architectures:

You can then check the image manifest to see if the image is available for both architectures using the [`docker buildx imagetools` command](https://docs.docker.com/reference/cli/docker/buildx/imagetools/):

> If you're having trouble pushing the image, make sure you're signed in to Docker Hub. Otherwise, run `docker login` to authenticate.

For more information, see [Multi-platform images](https://docs.docker.com/build/building/multi-platform/) page.

If your extension includes some binaries that deploy to the host, it’s important that they also have the right architecture when building the extension against multiple architectures.

Currently, Docker does not provide a way to explicitly specify multiple binaries for every architecture in the `metadata.json` file. However, you can add architecture-specific binaries depending on the `TARGETARCH` in the extension’s `Dockerfile`.

The following example shows an extension that uses a binary as part of its operations. The extension needs to run both in Docker Desktop for Mac and Windows.

In the `Dockerfile`, download the binary depending on the target architecture:

In the `metadata.json` file, specify the path for every binary on every platform:

As a result, when `TARGETARCH` equals:

- `arm64`, the `kubectl` binary fetched corresponds to the `arm64` architecture, and is copied to `/darwin/kubectl` in the final stage.
- `amd64`, two `kubectl` binaries are fetched. One for Darwin and another for Windows. They are copied to `/darwin/kubectl` and `/windows/kubectl.exe` respectively, in the final stage.

> The binary destination path for Darwin is `darwin/kubectl` in both cases. The only change is the architecture-specific binary that is downloaded.

When the extension is installed, the extension framework copies the binaries from the extension image at `/darwin/kubectl` for Darwin, or `/windows/kubectl.exe` for Windows, to a specific location in the user’s host filesystem.

Although Docker Extensions is supported on Docker Desktop for Windows, Mac, and Linux, the extension framework only supports Linux containers. Therefore, you must target `linux` as the OS when you build your extension image.