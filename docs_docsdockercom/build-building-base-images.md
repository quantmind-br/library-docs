---
title: Base images
url: https://docs.docker.com/build/building/base-images/
source: llms
fetched_at: 2026-01-24T14:15:30.321725653-03:00
rendered_js: false
word_count: 500
summary: This document explains the concept of Docker base images and provides instructions for selecting existing images or creating custom ones using scratch or Linux distribution root filesystems. It details the process of building minimal images and handling runtime dependencies.
tags:
    - docker
    - dockerfile
    - base-image
    - container-build
    - scratch-image
    - image-creation
    - devops
    - containerization
category: guide
---

All Dockerfiles start from a base image. A base is the image that your image extends. It refers to the contents of the `FROM` instruction in the Dockerfile.

For most cases, you don't need to create your own base image. Docker Hub contains a vast library of Docker images that are suitable for use as a base image in your build. [Docker Official Images](https://docs.docker.com/docker-hub/image-library/trusted-content/#docker-official-images) have clear documentation, promote best practices, and are regularly updated. There are also [Docker Verified Publisher](https://docs.docker.com/docker-hub/image-library/trusted-content/#verified-publisher-images) images, created by trusted publishing partners, verified by Docker.

If you need to completely control the contents of your image, you can create your own base image from a Linux distribution of your choosing, or use the special `FROM scratch` base:

The `scratch` image is typically used to create minimal images containing only just what an application needs. See [Create a minimal base image using scratch](#create-a-minimal-base-image-using-scratch).

To create a distribution base image, you can use a root filesystem, packaged as a `tar` file, and import it to Docker with `docker import`. The process for creating your own base image depends on the Linux distribution you want to package. See [Create a full image using tar](#create-a-full-image-using-tar).

The reserved, minimal `scratch` image serves as a starting point for building containers. Using the `scratch` image signals to the build process that you want the next command in the `Dockerfile` to be the first filesystem layer in your image.

While `scratch` appears in Docker's [repository on Docker Hub](https://hub.docker.com/_/scratch), you can't pull it, run it, or tag any image with the name `scratch`. Instead, you can refer to it in your `Dockerfile`. For example, to create a minimal container using `scratch`:

Assuming an executable binary named `hello` exists at the root of the [build context](https://docs.docker.com/build/concepts/context/). You can build this Docker image using the following `docker build` command:

To run your new image, use the `docker run` command:

This example image can only be successfully executed as long as the `hello` binary doesn't have any runtime dependencies. Computer programs tend to depend on certain other programs or resources to exist in the runtime environment. For example:

- Programming language runtimes
- Dynamically linked C libraries
- CA certificates

When building a base image, or any image, this is an important aspect to consider. And this is why creating a base image using `FROM scratch` can be difficult, for anything other than small, simple programs. On the other hand, it's also important to include only the things you need in your image, to reduce the image size and attack surface.

In general, start with a working machine that is running the distribution you'd like to package as a base image, though that is not required for some tools like Debian's [Debootstrap](https://wiki.debian.org/Debootstrap), which you can also use to build Ubuntu images.

For example, to create an Ubuntu base image:

There are more example scripts for creating base images in [the Moby GitHub repository](https://github.com/moby/moby/blob/master/contrib).

For more information about building images and writing Dockerfiles, see:

- [Dockerfile reference](https://docs.docker.com/reference/dockerfile/)
- [Dockerfile best practices](https://docs.docker.com/build/building/best-practices/)
- [Docker Official Images](https://docs.docker.com/docker-hub/image-library/trusted-content/#docker-official-images)