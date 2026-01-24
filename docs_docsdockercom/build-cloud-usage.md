---
title: Usage
url: https://docs.docker.com/build-cloud/usage/
source: llms
fetched_at: 2026-01-24T14:14:57.630231112-03:00
rendered_js: false
word_count: 724
summary: This document explains how to configure and use Docker Build Cloud to perform builds, manage default builders, and handle multi-platform builds. It also covers collaboration features, secret management, and cache maintenance for teams.
tags:
    - docker-build-cloud
    - docker-buildx
    - multi-platform-builds
    - cache-management
    - build-secrets
    - docker-desktop
    - cloud-builder
category: guide
---

## Building with Docker Build Cloud

To build using Docker Build Cloud, invoke a build command and specify the name of the builder using the `--builder` flag.

If you want to use Docker Build Cloud without having to specify the `--builder` flag each time, you can set it as the default builder.

Run the following command:

1. Open the Docker Desktop settings and navigate to the **Builders** tab.
2. Find the cloud builder under **Available builders**.
3. Open the drop-down menu and select **Use**.
   
   ![Selecting the cloud builder as default using the Docker Desktop GUI](https://docs.docker.com/build/images/set-default-builder-gui.webp)
   
   ![Selecting the cloud builder as default using the Docker Desktop GUI](https://docs.docker.com/build/images/set-default-builder-gui.webp)

Changing your default builder with `docker buildx use` only changes the default builder for the `docker buildx build` command. The `docker build` command still uses the `default` builder, unless you specify the `--builder` flag explicitly.

If you use build scripts, such as `make`, that use the `docker build` command, we recommend updating your build commands to `docker buildx build`. Alternatively, you can set the [`BUILDX_BUILDER` environment variable](https://docs.docker.com/build/building/variables/#buildx_builder) to specify which builder `docker build` should use.

To build with Docker Build Cloud using `docker compose build`, first set the cloud builder as your selected builder, then run your build.

> Make sure you're using a supported version of Docker Compose, see [Prerequisites](https://docs.docker.com/build-cloud/setup/#prerequisites).

In addition to `docker buildx use`, you can also use the `docker compose build --builder` flag or the [`BUILDX_BUILDER` environment variable](https://docs.docker.com/build/building/variables/#buildx_builder) to select the cloud builder.

Building with `--tag` loads the build result to the local image store automatically when the build finishes. To build without a tag and load the result, you must pass the `--load` flag.

Loading the build result for multi-platform images is not supported. Use the `docker buildx build --push` flag when building multi-platform images to push the output to a registry.

If you want to build with a tag, but you don't want to load the results to your local image store, you can export the build results to the build cache only:

To run multi-platform builds, you must specify all of the platforms that you want to build for using the `--platform` flag.

If you don't specify the platform, the cloud builder automatically builds for the architecture matching your local environment.

To learn more about building for multiple platforms, refer to [Multi-platform builds](https://docs.docker.com/build/building/multi-platform/).

The Docker Desktop [Builds view](https://docs.docker.com/desktop/use-desktop/builds/) works with Docker Build Cloud out of the box. This view can show information about not only your own builds, but also builds initiated by your team members using the same builder.

Teams using a shared builder get access to information such as:

- Ongoing and completed builds
- Build configuration, statistics, dependencies, and results
- Build source (Dockerfile)
- Build logs and errors

This lets you and your team work collaboratively on troubleshooting and improving build speeds, without having to send build logs and benchmarks back and forth between each other.

To use build secrets with Docker Build Cloud, such as authentication credentials or tokens, use the `--secret` and `--ssh` CLI flags for the `docker buildx` command. The traffic is encrypted and secrets are never stored in the build cache.

> If you're misusing build arguments to pass credentials, authentication tokens, or other secrets, you should refactor your build to pass the secrets using [secret mounts](https://docs.docker.com/reference/cli/docker/buildx/build/#secret) instead. Build arguments are stored in the cache and their values are exposed through attestations. Secret mounts don't leak outside of the build and are never included in attestations.

For more information, refer to:

- [`docker buildx build --secret`](https://docs.docker.com/reference/cli/docker/buildx/build/#secret)
- [`docker buildx build --ssh`](https://docs.docker.com/reference/cli/docker/buildx/build/#ssh)

You don't need to manage Docker Build Cloud cache manually. The system manages it for you through [garbage collection](https://docs.docker.com/build/cache/garbage-collection/).

Old cache is automatically removed if you hit your storage limit. You can check your current cache state using the [`docker buildx du` command](https://docs.docker.com/reference/cli/docker/buildx/du/).

To clear the builder's cache manually, use the [`docker buildx prune` command](https://docs.docker.com/reference/cli/docker/buildx/prune/). This works like pruning the cache for any other builder.

> Pruning a cloud builder's cache also removes the cache for other team members using the same builder.

If you've set a cloud builder as the default builder and want to revert to the default `docker` builder, run the following command:

This doesn't remove the builder from your system. It only changes the builder that's automatically selected to run your builds.

It is possible to use Docker Build Cloud with a [private registry](https://docs.docker.com/build-cloud/builder-settings/#private-resource-access) or registry mirror on an internal network.