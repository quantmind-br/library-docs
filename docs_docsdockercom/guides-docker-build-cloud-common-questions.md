---
title: Common challenges and questions
url: https://docs.docker.com/guides/docker-build-cloud/common-questions/
source: llms
fetched_at: 2026-01-24T14:04:13.612067792-03:00
rendered_js: false
word_count: 413
summary: This document provides answers to frequently asked questions about Docker Build Cloud, covering its integration with Docker Desktop, CI/CD platforms, and subscription plans.
tags:
    - docker-build-cloud
    - container-images
    - cloud-computing
    - ci-cd
    - docker-desktop
    - docker-compose
category: reference
---

### [Is Docker Build Cloud a standalone product or a part of Docker Desktop?](#is-docker-build-cloud-a-standalone-product-or-a-part-of-docker-desktop)

Docker Build Cloud is a service that can be used both with Docker Desktop and standalone. It lets you build your container images faster, both locally and in CI, with builds running on cloud infrastructure. The service uses a remote build cache, ensuring fast builds anywhere and for all team members.

When used with Docker Desktop, the [Builds view](https://docs.docker.com/desktop/use-desktop/builds/) works with Docker Build Cloud out-of-the-box. It shows information about your builds and those initiated by your team members using the same builder, enabling collaborative troubleshooting.

To use Docker Build Cloud without Docker Desktop, you must [download and install](https://docs.docker.com/build-cloud/setup/#use-docker-build-cloud-without-docker-desktop) a version of Buildx with support for Docker Build Cloud (the `cloud` driver). If you plan on building with Docker Build Cloud using the `docker compose build` command, you also need a version of Docker Compose that supports Docker Build Cloud.

### [How does Docker Build Cloud work with Docker Compose?](#how-does-docker-build-cloud-work-with-docker-compose)

Docker Compose works out of the box with Docker Build Cloud. Install the Docker Build Cloud-compatible client (buildx) and it works with both commands.

### [How many minutes are included in Docker Build Cloud Team plans?](#how-many-minutes-are-included-in-docker-build-cloud-team-plans)

Pricing details for Docker Build Cloud can be found on the [pricing page](https://www.docker.com/pricing/).

### [I’m a Docker personal user. Can I try Docker Build Cloud?](#im-a-docker-personal-user-can-i-try-docker-build-cloud)

Docker subscribers (Pro, Team, Business) receive a set number of minutes each month, shared across the account, to use Build Cloud.

If you do not have a Docker subscription, you may sign up for a free Personal account and start a trial of Docker Build Cloud. Personal accounts are limited to a single user.

For teams to receive the shared cache benefit, they must either be on a Docker Team or Docker Business subscription.

### [Does Docker Build Cloud support CI platforms? Does it work with GitHub Actions?](#does-docker-build-cloud-support-ci-platforms-does-it-work-with-github-actions)

Yes, Docker Build Cloud can be used with various CI platforms including GitHub Actions, CircleCI, Jenkins, and others. It can speed up your build pipelines, which means less time spent waiting and context switching.

Docker Build Cloud can be used with GitHub Actions to automate your build, test, and deployment pipeline. Docker provides a set of official GitHub Actions that you can use in your workflows.

Using GitHub Actions with Docker Build Cloud is straightforward. With a one-line change in your GitHub Actions configuration, everything else stays the same. You don't need to create new pipelines. Learn more in the [CI documentation](https://docs.docker.com/build-cloud/ci/) for Docker Build Cloud.