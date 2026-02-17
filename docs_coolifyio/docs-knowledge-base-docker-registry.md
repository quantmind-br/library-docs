---
title: Docker Registry
url: https://coolify.io/docs/knowledge-base/docker/registry.md
source: llms
fetched_at: 2026-02-17T14:41:14.41907-03:00
rendered_js: false
word_count: 344
summary: This document explains how to configure and use Docker registries within Coolify for pushing built images, managing credentials, and hosting a private registry.
tags:
    - docker-registry
    - coolify
    - image-deployment
    - authentication
    - docker-swarm
    - private-registry
category: configuration
---

# Docker Registry

You can easily push your built docker images to any docker registries with Coolify.

You just need to fill the `Docker Registry` fields in your service `General` configurations.

## Configuration

### Docker Image

If this field is set, Coolify will automatically push your built docker image to the specified docker registry.

> If the image is empty, Coolify won't push your built image.

### Docker Image Tag

If this field is set, Coolify will automatically push your built docker image with the specified tag to the specified docker registry + the git commit sha tag.

> If the tag is empty, Coolify only push your built image with the git commit sha tag.

## Docker Credentials

Docker credentials (from v4.0.0-beta.88) are used to authenticate with Docker registries to pull/push images.

If you want to authenticate Coolify with a Docker Registry:

1. Login to your server
   Login on the server through SSH with the same user that configured for your server.

2. Authenticate to Docker Registry
   Login to the Docker Registry, normally execute `docker login` command.

   > You will be prompted to enter your Docker registry username and password/token - this can be varied depending on the Docker registry you are using.

Once you logged in, Coolify will automatically detect your credentials and use them.

## Swarm Mode

If you are deploying to a Swarm cluster, you need to make sure that your Docker Registry is accessible from all nodes in the cluster, workers and managers.

## Host your own registry

You can easily host your own registry, however, it will consume a lot of storages as by default it stores images locally on the server.

More info on how to set other storage drivers can be found in the [official documentation](https://distribution.github.io/distribution/storage-drivers/).

You can find the one-click service in Coolify.

### Setup

You need to generate an user / password for the registry.

You can generate one with the [htpasswd](https://httpd.apache.org/docs/current/programs/htpasswd.html) command:

```bash
htpasswd -nbB test test
```

Then go to `Storages` menu, and in the `/auth/registry.password` file, simply add the generated user / password. One line per user.

::: warning Caution
Do not forget to restart the registry service.
:::