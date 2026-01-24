---
title: Migrate from Alpine or Debian
url: https://docs.docker.com/dhi/migration/migrate-from-doi/
source: llms
fetched_at: 2026-01-24T14:21:10.400221046-03:00
rendered_js: false
word_count: 643
summary: This guide provides instructions for migrating applications from standard Docker Official Images to Docker Hardened Images, detailing key architectural differences and best practices for multi-stage builds.
tags:
    - docker-hardened-images
    - container-security
    - migration-guide
    - multi-stage-builds
    - dockerfile-best-practices
category: guide
---

Docker Hardened Images (DHI) come in both [Alpine-based and Debian-based variants](https://docs.docker.com/dhi/explore/available/). In many cases, migrating from another image based on these distributions is as simple as changing the base image in your Dockerfile.

This guide helps you migrate from an existing Alpine-based or Debian-based Docker Official Image (DOI) to DHI.

If you're currently using a Debian-based Docker Official Image, migrate to the Debian-based DHI variant. If you're using an Alpine-based image, migrate to the Alpine-based DHI variant. This minimizes changes to package management and dependencies during migration.

When migrating from non-hardened images to DHI, be aware of these key differences:

ItemNon-hardened imagesDocker Hardened ImagesPackage managementPackage managers generally available in all images.Package managers generally only available in images with a `dev` tag. Runtime images don't contain package managers. Use multi-stage builds and copy necessary artifacts from the build stage to the runtime stage.Non-root userUsually runs as root by defaultRuntime variants run as the nonroot user by default. Ensure that necessary files and directories are accessible to the nonroot user.Multi-stage buildOptionalRecommended. Use images with a `dev` or `sdk` tags for build stages and non-dev images for runtime.TLS certificatesMay need to be installedContain standard TLS certificates by default. There is no need to install TLS certificates.PortsCan bind to privileged ports (below 1024) when running as rootRun as a nonroot user by default. Applications can't bind to privileged ports (below 1024) when running in Kubernetes or in Docker Engine versions older than 20.10. Configure your application to listen on port 1025 or higher inside the container.Entry pointVaries by imageMay have different entry points than Docker Official Images. Inspect entry points and update your Dockerfile if necessary.ShellShell generally available in all imagesRuntime images don't contain a shell. Use `dev` images in build stages to run shell commands and then copy artifacts to the runtime stage.

### [Step 1: Update the base image in your Dockerfile](#step-1-update-the-base-image-in-your-dockerfile)

Update the base image in your application's Dockerfile to a hardened image. This is typically going to be an image tagged as `dev` or `sdk` because it has the tools needed to install packages and dependencies.

The following example diff snippet from a Dockerfile shows the old base image replaced by the new hardened image.

> You must authenticate to `dhi.io` before you can pull Docker Hardened Images. Use your Docker ID credentials (the same username and password you use for Docker Hub). If you don't have a Docker account, [create one](https://docs.docker.com/accounts/create-account/) for free.
> 
> Run `docker login dhi.io` to authenticate.

Note that DHI does not have a `latest` tag in order to promote best practices around image versioning. Ensure that you specify the appropriate version tag for your image. To find the right tag, explore the available tags in the [DHI Catalog](https://hub.docker.com/hardened-images/catalog/). In addition, the distribution base is specified in the tag (for example, `-alpine3.22` or `-debian12`), so be sure to select the correct variant for your application.

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