---
title: Why Docker Build Cloud?
url: https://docs.docker.com/guides/docker-build-cloud/why/
source: llms
fetched_at: 2026-01-24T14:04:15.43217624-03:00
rendered_js: false
word_count: 125
summary: This document introduces Docker Build Cloud, a managed service designed to speed up container image builds using cloud infrastructure and shared remote caching.
tags:
    - docker-build-cloud
    - container-images
    - build-acceleration
    - cloud-infrastructure
    - shared-cache
    - multi-platform-builds
category: concept
---

Docker Build Cloud is a service that lets you build container images faster, both locally and in CI. Builds run on cloud infrastructure optimally dimensioned for your workloads, with no configuration required. The service uses a remote build cache, ensuring fast builds anywhere and for all team members.

Docker Build Cloud provides several benefits over local builds:

- Improved build speed
- Shared build cache
- Native multi-platform builds

There’s no need to worry about managing builders or infrastructure — simply connect to your builders and start building. Each cloud builder provisioned to an organization is completely isolated to a single Amazon EC2 instance, with a dedicated EBS volume for build cache and encryption in transit. That means there are no shared processes or data between cloud builders.