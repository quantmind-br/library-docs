---
title: Configure BuildKit
url: https://docs.docker.com/build/buildkit/configure/
source: llms
fetched_at: 2026-01-24T14:15:51.321212731-03:00
rendered_js: false
word_count: 430
summary: This document explains how to apply custom BuildKit configurations to Docker Buildx builders, including registry mirrors, certificates, CNI networking, and resource limits.
tags:
    - docker-buildx
    - buildkit
    - registry-mirror
    - certificates
    - cni-networking
    - parallelism
    - toml-configuration
category: guide
---

If you create a `docker-container` or `kubernetes` builder with Buildx, you can apply a custom [BuildKit configuration](https://docs.docker.com/build/buildkit/toml-configuration/) by passing the [`--buildkitd-config` flag](https://docs.docker.com/reference/cli/docker/buildx/create/#buildkitd-config) to the `docker buildx create` command.

You can define a registry mirror to use for your builds. Doing so redirects BuildKit to pull images from a different hostname. The following steps exemplify defining a mirror for `docker.io` (Docker Hub) to `mirror.gcr.io`.

1. Create a TOML at `/etc/buildkitd.toml` with the following content:
   
   > `debug = true` turns on debug requests in the BuildKit daemon, which logs a message that shows when a mirror is being used.
2. Create a `docker-container` builder that uses this BuildKit configuration:
3. Build an image:

The BuildKit logs for this builder now shows that it uses the GCR mirror. You can tell by the fact that the response messages include the `x-goog-*` HTTP headers.

If you specify registry certificates in the BuildKit configuration, the daemon copies the files into the container under `/etc/buildkit/certs`. The following steps show adding a self-signed registry certificate to the BuildKit configuration.

1. Add the following configuration to `/etc/buildkitd.toml`:
   
   This tells the builder to push images to the `myregistry.com` registry using the certificates in the specified location (`/etc/certs`).
2. Create a `docker-container` builder that uses this configuration:
3. Inspect the builder's configuration file (`/etc/buildkit/buildkitd.toml`), it shows that the certificate configuration is now configured in the builder.
4. Verify that the certificates are inside the container:

Now you can push to the registry using this builder, and it will authenticate using the certificates:

CNI networking for builders can be useful for dealing with network port contention during concurrent builds. CNI is [not yet](https://github.com/moby/buildkit/issues/28) available in the default BuildKit image. But you can create your own image that includes CNI support.

The following Dockerfile example shows a custom BuildKit image with CNI support. It uses the [CNI config for integration tests](https://github.com/moby/buildkit/blob/master//hack/fixtures/cni.json) in BuildKit as an example. Feel free to include your own CNI configuration.

Now you can build this image, and create a builder instance from it using [the `--driver-opt image` option](https://docs.docker.com/reference/cli/docker/buildx/create/#driver-opt):

### [Max parallelism](#max-parallelism)

You can limit the parallelism of the BuildKit solver, which is particularly useful for low-powered machines, using a [BuildKit configuration](https://docs.docker.com/build/buildkit/toml-configuration/) while creating a builder with the [`--buildkitd-config` flag](https://docs.docker.com/reference/cli/docker/buildx/create/#buildkitd-config).

Now you can [create a `docker-container` builder](https://docs.docker.com/build/builders/drivers/docker-container/) that will use this BuildKit configuration to limit parallelism.

### [TCP connection limit](#tcp-connection-limit)

TCP connections are limited to 4 simultaneous connections per registry for pulling and pushing images, plus one additional connection dedicated to metadata requests. This connection limit prevents your build from getting stuck while pulling images. The dedicated metadata connection helps reduce the overall build time.

More information: [moby/buildkit#2259](https://github.com/moby/buildkit/pull/2259)