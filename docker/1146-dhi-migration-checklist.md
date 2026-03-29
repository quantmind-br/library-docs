---
title: Migration checklist
url: https://docs.docker.com/dhi/migration/checklist/
source: llms
fetched_at: 2026-01-24T14:21:05.816568372-03:00
rendered_js: false
word_count: 221
summary: This document provides a comprehensive checklist and actionable steps for migrating applications to Docker Hardened Images, focusing on security best practices like non-root execution and multi-stage builds.
tags:
    - docker
    - hardened-images
    - container-security
    - migration-checklist
    - multi-stage-builds
    - non-root-user
category: guide
---

Use this checklist to ensure you address key considerations when migrating to Docker Hardened Images.

ItemAction requiredBase imageUpdate your Dockerfile `FROM` statements to reference a Docker Hardened Image instead of your current base image.Package managementInstall packages only in `dev`-tagged images during build stages. Use `apk` for Alpine-based images or `apt` for Debian-based images. Copy the necessary artifacts to your runtime stage, as runtime images don't include package managers.Non-root userVerify that all files and directories your application needs are readable and writable by the nonroot user (UID 65532), as runtime images run as nonroot by default.Multi-stage buildUse `dev` or `sdk`-tagged images for build stages where you need build tools and package managers. Use non-dev images for your final runtime stage.TLS certificatesRemove any steps that install ca-certificates, as DHIs include ca-certificates by default.PortsConfigure your application to listen on port 1025 or higher inside the container, as the nonroot user can't bind to privileged ports (below 1024) in Kubernetes or Docker Engine versions older than 20.10.Entry pointCheck the entry point of your chosen DHI using `docker inspect` or the image documentation. Update your Dockerfile's `ENTRYPOINT` or `CMD` instructions if your application relies on a different entry point.No shellMove any shell commands (`RUN`, `SHELL`) to build stages using `dev`-tagged images. Runtime images don't include a shell, so copy all necessary artifacts from the build stage.