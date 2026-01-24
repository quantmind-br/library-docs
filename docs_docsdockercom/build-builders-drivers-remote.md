---
title: Remote driver
url: https://docs.docker.com/build/builders/drivers/remote/
source: llms
fetched_at: 2026-01-24T14:15:28.574912655-03:00
rendered_js: false
word_count: 616
summary: This document explains how to configure and use the Docker Buildx remote driver to connect to externally managed BuildKit instances across different environments like Unix sockets, Docker containers, and Kubernetes.
tags:
    - docker-buildx
    - remote-driver
    - buildkit
    - kubernetes
    - unix-socket
    - tls-configuration
category: guide
---

The Buildx remote driver allows for more complex custom build workloads, allowing you to connect to externally managed BuildKit instances. This is useful for scenarios that require manual management of the BuildKit daemon, or where a BuildKit daemon is exposed from another source.

The following table describes the available driver-specific options that you can pass to `--driver-opt`:

ParameterTypeDefaultDescription`key`StringSets the TLS client key.`cert`StringAbsolute path to the TLS client certificate to present to `buildkitd`.`cacert`StringAbsolute path to the TLS certificate authority used for validation.`servername`StringEndpoint hostname.TLS server name used in requests.`default-load`Boolean`false`Automatically load images to the Docker Engine image store.

This guide shows you how to create a setup with a BuildKit daemon listening on a Unix socket, and have Buildx connect through it.

1. Ensure that [BuildKit](https://github.com/moby/buildkit) is installed.
   
   For example, you can launch an instance of buildkitd with:
   
   Alternatively, refer to the [Rootless Buildkit documentation](https://github.com/moby/buildkit/blob/master/docs/rootless.md) for running buildkitd in rootless mode, or [the BuildKit systemd examples](https://github.com/moby/buildkit/tree/master/examples/systemd) for running it as a systemd service.
2. Check that you have a Unix socket that you can connect to.
3. Connect Buildx to it using the remote driver:
4. List available builders with `docker buildx ls`. You should then see `remote-unix` among them:

You can switch to this new builder as the default using `docker buildx use remote-unix`, or specify it per build using `--builder`:

Remember that you need to use the `--load` flag if you want to load the build result into the Docker daemon.

This guide will show you how to create setup similar to the `docker-container` driver, by manually booting a BuildKit Docker container and connecting to it using the Buildx remote driver. This procedure will manually create a container and access it via it's exposed port. (You'd probably be better of just using the `docker-container` driver that connects to BuildKit through the Docker daemon, but this is for illustration purposes.)

1. Generate certificates for BuildKit.
   
   You can use this [bake definition](https://github.com/moby/buildkit/blob/master/examples/create-certs) as a starting point:
   
   Note that while it's possible to expose BuildKit over TCP without using TLS, it's not recommended. Doing so allows arbitrary access to BuildKit without credentials.
2. With certificates generated in `.certs/`, startup the container:
   
   This command starts a BuildKit container and exposes the daemon's port 1234 to localhost.
3. Connect to this running container using Buildx:
   
   Alternatively, use the `docker-container://` URL scheme to connect to the BuildKit container without specifying a port:

This guide will show you how to create a setup similar to the `kubernetes` driver by manually creating a BuildKit `Deployment`. While the `kubernetes` driver will do this under-the-hood, it might sometimes be desirable to scale BuildKit manually. Additionally, when executing builds from inside Kubernetes pods, the Buildx builder will need to be recreated from within each pod or copied between them.

1. Create a Kubernetes deployment of `buildkitd` by following the instructions [in the BuildKit documentation](https://github.com/moby/buildkit/tree/master/examples/kubernetes).
   
   Create certificates for the BuildKit daemon and client using the [create-certs.sh](https://github.com/moby/buildkit/blob/master/examples/kubernetes/create-certs.sh), script and create a deployment of BuildKit pods with a service that connects to them.
2. Assuming that the service is called `buildkitd`, create a remote builder in Buildx, ensuring that the listed certificate files are present:

Note that this only works internally, within the cluster, since the BuildKit setup guide only creates a `ClusterIP` service. To access a builder remotely, you can set up and use an ingress, which is outside the scope of this guide.

### [Debug a remote builder in Kubernetes](#debug-a-remote-builder-in-kubernetes)

If you're having trouble accessing a remote builder deployed in Kubernetes, you can use the `kube-pod://` URL scheme to connect directly to a BuildKit pod through the Kubernetes API. Note that this method only connects to a single pod in the deployment.

Alternatively, use the port forwarding mechanism of `kubectl`:

Then you can point the remote driver at `tcp://localhost:1234`.