---
title: Wasm workloads
url: https://docs.docker.com/desktop/features/wasm/
source: llms
fetched_at: 2026-01-24T14:18:36.927922333-03:00
rendered_js: false
word_count: 670
summary: This document provides instructions for configuring and running WebAssembly (Wasm) workloads in Docker Desktop using the containerd image store. It covers setup procedures, running modules with Docker CLI and Compose, building Wasm images, and troubleshooting common runtime errors.
tags:
    - docker-desktop
    - webassembly
    - wasm
    - containerd
    - docker-compose
    - runtime-configuration
    - wasi
category: guide
---

> Wasm workloads will be deprecated and removed in a future Docker Desktop release. It is no longer actively maintained.

WebAssembly (Wasm) is a fast, light alternative to Linux and Windows containers. With Docker Desktop, you can now run Wasm workloads side by side with traditional containers.

This page provides information about the ability to run Wasm applications alongside your Linux containers in Docker.

> Learn more about Wasm use cases and tradeoffs in the [Docker Wasm technical preview blog post](https://www.docker.com/blog/docker-wasm-technical-preview/).

Wasm workloads require the [containerd image store](https://docs.docker.com/desktop/features/containerd/) feature to be turned on. If you’re not already using the containerd image store, then pre-existing images and containers will be inaccessible.

1. Navigate to **Settings** in Docker Desktop.
2. In the **General** tab, check **Use containerd for pulling and storing images**.
3. Go to **Features in development** and check the **Enable Wasm** option.
4. Select **Apply** to save the settings.
5. In the confirmation dialog, select **Install** to install the Wasm runtimes.

Docker Desktop downloads and installs the following runtimes:

- `io.containerd.slight.v1`
- `io.containerd.spin.v2`
- `io.containerd.wasmedge.v1`
- `io.containerd.wasmtime.v1`
- `io.containerd.lunatic.v1`
- `io.containerd.wws.v1`
- `io.containerd.wasmer.v1`

### [Running a Wasm application with `docker run`](#running-a-wasm-application-with-docker-run)

The following `docker run` command starts a Wasm container on your system:

After running this command, you can visit [http://localhost:8080/](http://localhost:8080/) to see the "Hello world" output from this example module.

If you are receiving an error message, see the [troubleshooting section](#troubleshooting) for help.

Note the `--runtime` and `--platform` flags used in this command:

- `--runtime=io.containerd.wasmedge.v1`: Informs the Docker engine that you want to use the Wasm containerd shim instead of the standard Linux container runtime
- `--platform=wasi/wasm`: Specifies the architecture of the image you want to use. By leveraging a Wasm architecture, you don’t need to build separate images for the different machine architectures. The Wasm runtime takes care of the final step of converting the Wasm binary to machine instructions.

### [Running a Wasm application with Docker Compose](#running-a-wasm-application-with-docker-compose)

The same application can be run using the following Docker Compose file:

Start the application using the normal Docker Compose commands:

### [Running a multi-service application with Wasm](#running-a-multi-service-application-with-wasm)

Networking works the same as you'd expect with Linux containers, giving you the flexibility to combine Wasm applications with other containerized workloads, such as a database, in a single application stack.

In the following example, the Wasm application leverages a MariaDB database running in a container.

1. Clone the repository.
2. Navigate into the cloned project and start the project using Docker Compose.
   
   If you run `docker image ls` from another terminal window, you can see the Wasm image in your image store.
   
   Inspecting the image shows the image has a `wasi/wasm` platform, a combination of OS and architecture:
3. Open the URL `http://localhost:8090` in a browser and create a few sample orders. All of these are interacting with the Wasm server.
4. When you're all done, tear everything down by hitting `Ctrl+C` in the terminal you launched the application.

### [Building and pushing a Wasm module](#building-and-pushing-a-wasm-module)

1. Create a Dockerfile that builds your Wasm application.
   
   Exactly how to do this varies depending on the programming language you use.
2. In a separate stage in your `Dockerfile`, extract the module and set it as the `ENTRYPOINT`.
3. Build and push the image specifying the `wasi/wasm` architecture. Buildx makes this easy to do in a single command.

This section contains instructions on how to resolve common issues.

### [Unknown runtime specified](#unknown-runtime-specified)

If you try to run a Wasm container without the [containerd image store](https://docs.docker.com/desktop/features/containerd/), an error similar to the following displays:

[Turn on the containerd feature](https://docs.docker.com/desktop/features/containerd/#enable-the-containerd-image-store) in Docker Desktop settings and try again.

### [Failed to start shim: failed to resolve runtime path](#failed-to-start-shim-failed-to-resolve-runtime-path)

If you use an older version of Docker Desktop that doesn't support running Wasm workloads, you will see an error message similar to the following:

Update your Docker Desktop to the latest version and try again.

- Docker Compose may not exit cleanly when interrupted. As a workaround, clean up `docker-compose` processes by sending them a SIGKILL (`killall -9 docker-compose`).
- Pushes to Docker Hub might give an error stating `server message: insufficient_scope: authorization failed`, even after signing in through Docker Desktop. As a workaround, run `docker login` in the CLI