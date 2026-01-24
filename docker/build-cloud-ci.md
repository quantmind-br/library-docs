---
title: Continuous integration
url: https://docs.docker.com/build-cloud/ci/
source: llms
fetched_at: 2026-01-24T14:14:51.117187639-03:00
rendered_js: false
word_count: 569
summary: This document explains how to integrate Docker Build Cloud into CI/CD pipelines to speed up image building and streamline workflows across various automation platforms.
tags:
    - docker-build-cloud
    - ci-cd
    - automation
    - buildx
    - containerization
    - devops
    - cloud-build
category: guide
---

## Use Docker Build Cloud in CI

Using Docker Build Cloud in CI can speed up your build pipelines, which means less time spent waiting and context switching. You control your CI workflows as usual, and delegate the build execution to Docker Build Cloud.

Building with Docker Build Cloud in CI involves the following steps:

1. Sign in to a Docker account.
2. Set up Buildx and connect to the builder.
3. Run the build.

When using Docker Build Cloud in CI, it's recommended that you push the result to a registry directly, rather than loading the image and then pushing it. Pushing directly speeds up your builds and avoids unnecessary file transfers.

If you just want to build and discard the output, export the results to the build cache or build without tagging the image. When you use Docker Build Cloud, Buildx automatically loads the build result if you build a tagged image. See [Loading build results](https://docs.docker.com/build-cloud/usage/#loading-build-results) for details.

> Builds on Docker Build Cloud have a timeout limit of 90 minutes. Builds that run for longer than 90 minutes are automatically cancelled.

To enable your CI/CD system to build and push images using Docker Build Cloud, provide both an access token and a username. The type of token and the username you use depend on your account type and permissions.

- If you are an organization administrator or have permission to create [organization access tokens (OAT)](https://docs.docker.com/enterprise/security/access-tokens/), use an OAT and set `DOCKER_ACCOUNT` to your Docker Hub organization name.
- If you do not have permission to create OATs or are using a personal account, use a [personal access token (PAT)](https://docs.docker.com/security/access-tokens/) and set `DOCKER_ACCOUNT` to your Docker Hub username.

### [Creating access tokens](#creating-access-tokens)

#### [For organization accounts](#for-organization-accounts)

If you are an organization administrator:

- Create an [organization access token (OAT)](https://docs.docker.com/enterprise/security/access-tokens/). The token must have these permissions:
  
  1. **cloud-connect** scope
  2. **Read public repositories** permission
  3. **Repository access** with **Image push** permission for the target repository:
     
     - Expand the **Repository** drop-down.
     - Select **Add repository** and choose your target repository.
     - Set the **Image push** permission for the repository.

If you are not an organization administrator:

- Ask your organization administrator for an access token with the permissions listed above, or use a personal access token.

#### [For personal accounts](#for-personal-accounts)

- Create a [personal access token (PAT)](https://docs.docker.com/security/access-tokens/) with the following permissions:
  
  1. **Read & write** access.
     
     - Note: Building with Docker Build Cloud only requires read access, but you need write access to push images to a Docker Hub repository.

> In your CI/CD configuration, set the following variables/secrets:
> 
> - `DOCKER_ACCESS_TOKEN` — your access token (PAT or OAT). Use a secret to store the token.
> - `DOCKER_ACCOUNT` — your Docker Hub organization name (for OAT) or username (for PAT)
> - `CLOUD_BUILDER_NAME` — the name of the cloud builder you created in the [Docker Build Cloud Dashboard](https://app.docker.com/build/)
> 
> This ensures your builds authenticate correctly with Docker Build Cloud.

### [GitHub Actions](#github-actions)

The example above uses `docker/build-push-action`, which automatically uses the builder set up by `setup-buildx-action`. If you need to use the `docker build` command directly instead, you have two options:

- Use `docker buildx build` instead of `docker build`
- Set the `BUILDX_BUILDER` environment variable to use the cloud builder:

For more information about the `BUILDX_BUILDER` environment variable, see [Build variables](https://docs.docker.com/build/building/variables/#buildx_builder).

### [GitLab](#gitlab)

### [Circle CI](#circle-ci)

### [Buildkite](#buildkite)

The following example sets up a Buildkite pipeline using Docker Build Cloud. The example assumes that the pipeline name is `build-push-docker` and that you manage the Docker access token using environment hooks, but feel free to adapt this to your needs.

Add the following `environment` hook agent's hook directory:

Create a `pipeline.yml` that uses the `docker-login` plugin:

Create the `build.sh` script:

### [Jenkins](#jenkins)

### [Travis CI](#travis-ci)

### [BitBucket Pipelines](#bitbucket-pipelines)

### [Shell script](#shell-script)

### [Docker Compose](#docker-compose)

Use this implementation if you want to use `docker compose build` with Docker Build Cloud in CI.