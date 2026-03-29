---
title: Migrate from Ubuntu
url: https://docs.docker.com/dhi/migration/migrate-from-ubuntu/
source: llms
fetched_at: 2026-01-24T14:21:10.557329476-03:00
rendered_js: false
word_count: 616
summary: This document provides instructions for migrating from Ubuntu-based container images to Debian-based Docker Hardened Images, outlining key security differences and recommended build practices.
tags:
    - docker-hardened-images
    - container-security
    - migration-guide
    - ubuntu-to-debian
    - multi-stage-build
    - dockerfile
category: guide
---

Docker Hardened Images (DHI) come in [Alpine-based and Debian-based variants](https://docs.docker.com/dhi/explore/available/). When migrating from an Ubuntu-based image, you should migrate to the Debian-based DHI variant, as both Ubuntu and Debian share the same package management system (APT) and underlying architecture, making migration straightforward.

This guide helps you migrate from an existing Ubuntu-based image to DHI.

When migrating from Ubuntu-based images to DHI Debian, be aware of these key differences:

ItemUbuntu-based imagesDocker Hardened ImagesPackage managementVaries by image. Some include APT package manager, others don'tPackage managers generally only available in images with a `dev` tag. Runtime images don't contain package managers. Use multi-stage builds and copy necessary artifacts from the build stage to the runtime stage.Non-root userVaries by image. Some run as root, others as non-rootRuntime variants run as the non-root user by default. Ensure that necessary files and directories are accessible to the non-root user.Multi-stage buildRecommendedRecommended. Use images with a `dev` or `sdk` tags for build stages and non-dev images for runtime.PortsCan bind to privileged ports (under 1024) when running as rootRun as a non-root user by default. Applications can't bind to privileged ports (under 1024) when running in Kubernetes or in Docker Engine versions older than 20.10. Configure your application to listen on port 1025 and up inside the container.Entry pointVaries by imageMay have different entry points than Ubuntu-based images. Inspect entry points and update your Dockerfile if necessary.ShellVaries by image. Some include a shell, others don'tRuntime images don't contain a shell. Use `dev` images in build stages to run shell commands and then copy artifacts to the runtime stage.Package repositoriesUses Ubuntu package repositoriesUses Debian package repositories. Most packages have similar names, but some may differ.

### [Step 1: Update the base image in your Dockerfile](#step-1-update-the-base-image-in-your-dockerfile)

Update the base image in your application's Dockerfile to a hardened image. This is typically going to be an image tagged as `dev` or `sdk` because it has the tools needed to install packages and dependencies.

The following example diff snippet from a Dockerfile shows the old Ubuntu-based image replaced by the new DHI Debian image.

> You must authenticate to `dhi.io` before you can pull Docker Hardened Images. Use your Docker ID credentials (the same username and password you use for Docker Hub). If you don't have a Docker account, [create one](https://docs.docker.com/accounts/create-account/) for free.
> 
> Run `docker login dhi.io` to authenticate.

To find the right tag, explore the available tags in the [DHI Catalog](https://hub.docker.com/hardened-images/catalog/).

### [Step 2: Update package installation commands](#step-2-update-package-installation-commands)

Since Ubuntu and Debian both use APT for package management, most package installation commands remain similar. However, you need to ensure that package installations only occur in `dev` or `sdk` images, as runtime images don't contain package managers.

Most Ubuntu packages are available in Debian with the same names. If you encounter missing packages, you can search for equivalent packages using the [Debian package search](https://packages.debian.org/) website.

### [Step 3: Update the runtime image in your Dockerfile](#step-3-update-the-runtime-image-in-your-dockerfile)

> Multi-stage builds are recommended to keep your final image minimal and secure. Single-stage builds are supported, but they include the full `dev` image and therefore result in a larger image with a broader attack surface.

To ensure that your final image is as minimal as possible, you should use a [multi-stage build](https://docs.docker.com/build/building/multi-stage/). All stages in your Dockerfile should use a hardened image. While intermediary stages will typically use images tagged as `dev` or `sdk`, your final runtime stage should use a runtime image.

Utilize the build stage to install dependencies and prepare your application, then copy the resulting artifacts to the final runtime stage. This ensures that your final image is minimal and secure.

The following example shows a multi-stage Dockerfile migrating from Ubuntu to DHI Debian:

See the examples section for language-specific migration examples:

- [Go](https://docs.docker.com/dhi/migration/examples/go/)
- [Python](https://docs.docker.com/dhi/migration/examples/python/)
- [Node.js](https://docs.docker.com/dhi/migration/examples/node/)