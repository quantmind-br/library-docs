---
title: Setup
url: https://docs.docker.com/build-cloud/setup/
source: llms
fetched_at: 2026-01-24T14:14:55.838418286-03:00
rendered_js: false
word_count: 382
summary: This document provides instructions for setting up Docker Build Cloud in a local environment using either the CLI or Docker Desktop, including prerequisite software and firewall requirements.
tags:
    - docker-build-cloud
    - buildx
    - docker-desktop
    - cloud-builder
    - setup-guide
    - firewall-configuration
category: guide
---

## Docker Build Cloud setup

Table of contents

* * *

Before you can start using Docker Build Cloud, you must add the builder to your local environment.

## [Prerequisites](#prerequisites)

To get started with Docker Build Cloud, you need to:

- Download and install Docker Desktop version 4.26.0 or later.
- Create a cloud builder on the [Docker Build Cloud Dashboard](https://app.docker.com/build/).
  
  - When you create the builder, choose a name for it (for example, `default`). You will use this name as `BUILDER_NAME` in the CLI steps below.

### [Use Docker Build Cloud without Docker Desktop](#use-docker-build-cloud-without-docker-desktop)

To use Docker Build Cloud without Docker Desktop, you must download and install a version of Buildx with support for Docker Build Cloud (the `cloud` driver). You can find compatible Buildx binaries on the releases page of [this repository](https://github.com/docker/buildx-desktop).

If you plan on building with Docker Build Cloud using the `docker compose build` command, you also need a version of Docker Compose that supports Docker Build Cloud. You can find compatible Docker Compose binaries on the releases page of [this repository](https://github.com/docker/compose-desktop).

## [Steps](#steps)

You can add a cloud builder using the CLI, with the `docker buildx create` command, or using the Docker Desktop settings GUI.

1. Sign in to your Docker account.
2. Add the cloud builder endpoint.
   
   ```
   $ docker buildx create --driver cloud <ORG>/<BUILDER_NAME>
   ```
   
   Replace `<ORG>` with the Docker Hub namespace of your Docker organization (or your username if you are using a personal account), and `<BUILDER_NAME>` with the name you chose when creating the builder in the dashboard.
   
   This creates a local instance of the cloud builder named `cloud-ORG-BUILDER_NAME`.
   
   > Note
   > 
   > If your organization is `acme` and you named your builder `default`, use:
   > 
   > ```
   > $ docker buildx create --driver cloud acme/default
   > ```

<!--THE END-->

1. Sign in to your Docker account using the **Sign in** button in Docker Desktop.
2. Open the Docker Desktop settings and navigate to the **Builders** tab.
3. Under **Available builders**, select **Connect to builder**.

The builder has native support for the `linux/amd64` and `linux/arm64` architectures. This gives you a high-performance build cluster for building multi-platform images natively.

## [Firewall configuration](#firewall-configuration)

To use Docker Build Cloud behind a firewall, ensure that your firewall allows traffic to the following addresses:

- 3.211.38.21
- [https://auth.docker.io](https://auth.docker.io)
- [https://build-cloud.docker.com](https://build-cloud.docker.com)
- [https://hub.docker.com](https://hub.docker.com)

## [What's next](#whats-next)

- See [Building with Docker Build Cloud](https://docs.docker.com/build-cloud/usage/) for examples on how to use Docker Build Cloud.
- See [Use Docker Build Cloud in CI](https://docs.docker.com/build-cloud/ci/) for examples on how to use Docker Build Cloud with CI systems.