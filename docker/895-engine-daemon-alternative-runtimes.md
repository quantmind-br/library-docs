---
title: Alternative container runtimes
url: https://docs.docker.com/engine/daemon/alternative-runtimes/
source: llms
fetched_at: 2026-01-24T14:22:50.8578402-03:00
rendered_js: false
word_count: 632
summary: This document explains how to integrate and use alternative container runtimes with Docker Engine using containerd shims or runc drop-in replacements. It provides instructions for registering these runtimes in the daemon configuration and executing containers with non-default runtimes.
tags:
    - docker-engine
    - containerd
    - container-runtime
    - runc
    - wasmtime
    - daemon-configuration
    - containerd-shim
category: guide
---

Docker Engine uses containerd for managing the container lifecycle, which includes creating, starting, and stopping containers. By default, containerd uses runc as its container runtime.

You can use any runtime that implements the containerd [shim API](https://github.com/containerd/containerd/blob/main/core/runtime/v2/README.md). Such runtimes ship with a containerd shim, and you can use them without any additional configuration. See [Use containerd shims](#use-containerd-shims).

Examples of runtimes that implement their own containerd shims include:

- [Wasmtime](https://wasmtime.dev/)
- [gVisor](https://github.com/google/gvisor)
- [Kata Containers](https://katacontainers.io/)

You can also use runtimes designed as drop-in replacements for runc. Such runtimes depend on the runc containerd shim for invoking the runtime binary. You must manually register such runtimes in the daemon configuration.

[youki](https://github.com/youki-dev/youki) is one example of a runtime that can function as a runc drop-in replacement. Refer to the [youki example](#youki) explaining the setup.

containerd shims let you use alternative runtimes without having to change the configuration of the Docker daemon. To use a containerd shim, install the shim binary on `PATH` on the system where the Docker daemon is running.

To use a shim with `docker run`, specify the fully qualified name of the runtime as the value to the `--runtime` flag:

### [Use a containerd shim without installing on PATH](#use-a-containerd-shim-without-installing-on-path)

You can use a shim without installing it on `PATH`, in which case you need to register the shim in the daemon configuration as follows:

To use the shim, specify the name that you assigned to it:

### [Configure shims](#configure-shims)

If you need to pass additional configuration for a containerd shim, you can use the `runtimes` option in the daemon configuration file.

1. Edit the daemon configuration file by adding a `runtimes` entry for the shim you want to configure.
   
   - Specify the fully qualified name for the runtime in `runtimeType` key
   - Add your runtime configuration under the `options` key
2. Reload the daemon's configuration.
3. Use the customized runtime using the `--runtime` flag for `docker run`.

For more information about the configuration options for containerd shims, see [Configure containerd shims](https://docs.docker.com/reference/cli/dockerd/#configure-containerd-shims).

The following examples show you how to set up and use alternative container runtimes with Docker Engine.

- [youki](#youki)
- [Wasmtime](#wasmtime)

### [youki](#youki)

youki is a container runtime written in Rust. youki claims to be faster and use less memory than runc, making it a good choice for resource-constrained environments.

youki functions as a drop-in replacement for runc, meaning it relies on the runc shim to invoke the runtime binary. When you register runtimes acting as runc replacements, you configure the path to the runtime executable, and optionally a set of runtime arguments. For more information, see [Configure runc drop-in replacements](https://docs.docker.com/reference/cli/dockerd/#configure-runc-drop-in-replacements).

To add youki as a container runtime:

1. Install youki and its dependencies.
   
   For instructions, refer to the [official setup guide](https://youki-dev.github.io/youki/user/basic_setup.html).
2. Register youki as a runtime for Docker by editing the Docker daemon configuration file, located at `/etc/docker/daemon.json` by default.
   
   The `path` key should specify the path to wherever you installed youki.
3. Reload the daemon's configuration.

Now you can run containers that use youki as a runtime.

### [Wasmtime](#wasmtime)

Availability: Experimental

Wasmtime is a [Bytecode Alliance](https://bytecodealliance.org/) project, and a Wasm runtime that lets you run Wasm containers. Running Wasm containers with Docker provides two layers of security. You get all the benefits from container isolation, plus the added sandboxing provided by the Wasm runtime environment.

To add Wasmtime as a container runtime, follow these steps:

1. Turn on the [containerd image store](https://docs.docker.com/engine/storage/containerd/) feature in the daemon configuration file.
2. Restart the Docker daemon.
3. Install the Wasmtime containerd shim on `PATH`.
   
   The following command Dockerfile builds the Wasmtime binary from source and exports it to `./containerd-shim-wasmtime-v1`.
   
   Put the binary in a directory on `PATH`.

Now you can run containers that use Wasmtime as a runtime.

- To learn more about the configuration options for container runtimes, see [Configure container runtimes](https://docs.docker.com/reference/cli/dockerd/#configure-container-runtimes).
- You can configure which runtime that the daemon should use as its default. Refer to [Configure the default container runtime](https://docs.docker.com/reference/cli/dockerd/#configure-the-default-container-runtime).