---
title: Containerize your app using a multi-stage build
url: https://docs.docker.com/guides/cpp/multistage/
source: llms
fetched_at: 2026-01-24T14:03:45.799344317-03:00
rendered_js: false
word_count: 367
summary: This document explains how to implement multi-stage Docker builds for C++ applications to optimize final image size and isolate build-time dependencies from the runtime environment.
tags:
    - docker
    - c-plus-plus
    - multi-stage-build
    - containerization
    - image-optimization
    - dockerfile
category: tutorial
---

## Create a multi-stage build for your C++ application

- You have a [Git client](https://git-scm.com/downloads). The examples in this section use a command-line based Git client, but you can use any client.

This section walks you through creating a multi-stage Docker build for a C++ application. A multi-stage build is a Docker feature that allows you to use different base images for different stages of the build process, so you can optimize the size of your final image and separate build dependencies from runtime dependencies.

The standard practice for compiled languages like C++ is to have a build stage that compiles the code and a runtime stage that runs the compiled binary, because the build dependencies are not needed at runtime.

Let's use a simple C++ application that prints `Hello, World!` to the terminal. To do so, clone the sample repository to use with this guide:

The example for this section is under the `hello` directory in the repository. Get inside it and take a look at the files:

You should see the following files:

Open the `Dockerfile` in an IDE or text editor. The `Dockerfile` contains the instructions for building the Docker image.

The `Dockerfile` has two stages:

1. **Build stage**: This stage uses the `ubuntu:latest` image to compile the C++ code and create a static binary.
2. **Runtime stage**: This stage uses the `scratch` image, which is an empty image, to copy the static binary from the build stage and run it.

To build the Docker image, run the following command in the `hello` directory:

The `-t` flag tags the image with the name `hello`.

To run the Docker container, use the following command:

You should see the output `Hello, World!` in the terminal.

In this section, you learned how to create a multi-stage build for a C++ application. Multi-stage builds help you optimize the size of your final image and separate build dependencies from runtime dependencies. In this example, the final image only contains the static binary and doesn't include any build dependencies.

As the image has an empty base, the usual OS tools are also absent. So, for example, you can't run a simple `ls` command in the container:

This makes the image very lightweight and secure.