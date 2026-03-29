---
title: Migrate from Wolfi
url: https://docs.docker.com/dhi/migration/migrate-from-wolfi/
source: llms
fetched_at: 2026-01-24T14:21:12.170867489-03:00
rendered_js: false
word_count: 397
summary: This guide provides instructions for migrating containerized applications from Wolfi-based images to Docker Hardened Images (DHI). It covers updating base images, using multi-stage builds for security, and authenticating with the DHI registry.
tags:
    - docker-hardened-images
    - migration-guide
    - wolfi-migration
    - container-security
    - multi-stage-builds
    - image-hardening
category: guide
---

This guide helps you migrate from Wolfi-based images to Docker Hardened Images (DHI). Generally, the migration process is straightforward since Wolfi is Alpine-like and DHI provides an Alpine-based hardened image.

Like other hardened images, DHI provides comprehensive [attestations](https://docs.docker.com/dhi/core-concepts/attestations/) including SBOMs and provenance, allowing you to [verify](https://docs.docker.com/dhi/how-to/verify/) image signatures and [scan](https://docs.docker.com/dhi/how-to/scan/) for vulnerabilities to ensure the security and integrity of your images.

The following example demonstrates how to migrate a Dockerfile from a Wolfi-based image to an Alpine-based Docker Hardened Image.

### [Step 1: Update the base image in your Dockerfile](#step-1-update-the-base-image-in-your-dockerfile)

Update the base image in your application's Dockerfile to a hardened image. This is typically going to be an image tagged as `dev` or `sdk` because it has the tools needed to install packages and dependencies.

The following example diff snippet from a Dockerfile shows the old base image replaced by the new hardened image.

> You must authenticate to `dhi.io` before you can pull Docker Hardened Images. Use your Docker ID credentials (the same username and password you use for Docker Hub). If you don't have a Docker account, [create one](https://docs.docker.com/accounts/create-account/) for free.
> 
> Run `docker login dhi.io` to authenticate.

Note that DHI does not have a `latest` tag in order to promote best practices around image versioning. Ensure that you specify the appropriate version tag for your image. To find the right tag, explore the available tags in the [DHI Catalog](https://hub.docker.com/hardened-images/catalog/).

### [Step 2: Update the runtime image in your Dockerfile](#step-2-update-the-runtime-image-in-your-dockerfile)

> Multi-stage builds are recommended to keep your final image minimal and secure. Single-stage builds are supported, but they include the full `dev` image and therefore result in a larger image with a broader attack surface.

To ensure that your final image is as minimal as possible, you should use a [multi-stage build](https://docs.docker.com/build/building/multi-stage/). All stages in your Dockerfile should use a hardened image. While intermediary stages will typically use images tagged as `dev` or `sdk`, your final runtime stage should use a runtime image.

Utilize the build stage to compile your application and copy the resulting artifacts to the final runtime stage. This ensures that your final image is minimal and secure.

The following example shows a multi-stage Dockerfile with a build stage and runtime stage:

After updating your Dockerfile, build and test your application. If you encounter issues, see the [Troubleshoot](https://docs.docker.com/dhi/troubleshoot/) guide for common problems and solutions.

See the examples section for language-specific migration examples:

- [Go](https://docs.docker.com/dhi/migration/examples/go/)
- [Python](https://docs.docker.com/dhi/migration/examples/python/)
- [Node.js](https://docs.docker.com/dhi/migration/examples/node/)