---
title: Known issues
url: https://docs.docker.com/desktop/troubleshoot-and-support/troubleshoot/known-issues/
source: llms
fetched_at: 2026-01-24T14:19:16.722460255-03:00
rendered_js: false
word_count: 178
summary: This document outlines known issues and limitations when running Docker on Apple silicon, specifically regarding Rosetta 2 requirements, ARM64 compatibility, and emulation constraints.
tags:
    - docker-desktop
    - apple-silicon
    - arm64
    - rosetta-2
    - qemu-emulation
    - multi-arch
category: reference
---

- Some command line tools do not work when Rosetta 2 is not installed.
  
  - The old version 1.x of `docker-compose`. Use Compose V2 instead - type `docker compose`.
  - The `docker-credential-ecr-login` credential helper.
- Some images do not support the ARM64 architecture. You can add `--platform linux/amd64` to run (or build) an Intel image using emulation.
  
  However, attempts to run Intel-based containers on Apple silicon machines under emulation can crash as QEMU sometimes fails to run the container. In addition, filesystem change notification APIs (`inotify`) do not work under QEMU emulation. Even when the containers do run correctly under emulation, they will be slower and use more memory than the native equivalent.
  
  In summary, running Intel-based containers on Arm-based machines should be regarded as "best effort" only. We recommend running `arm64` containers on Apple silicon machines whenever possible, and encouraging container authors to produce `arm64`, or multi-arch, versions of their containers. This issue should become less common over time, as more and more images are rebuilt [supporting multiple architectures](https://www.docker.com/blog/multi-arch-build-and-images-the-simple-way/).
- Users may occasionally experience data drop when a TCP stream is half-closed.