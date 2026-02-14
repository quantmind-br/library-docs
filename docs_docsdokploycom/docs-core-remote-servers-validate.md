---
title: Validate | Dokploy
url: https://docs.dokploy.com/docs/core/remote-servers/validate
source: crawler
fetched_at: 2026-02-14T14:12:48.615677-03:00
rendered_js: true
word_count: 290
summary: This document outlines the specific system requirements and validation steps necessary to configure deployment and build servers within the Dokploy platform.
tags:
    - dokploy
    - server-validation
    - deployment-server
    - build-server
    - docker-swarm
    - remote-deployment
category: configuration
---

Validate your remote server deployment

Dokploy validates different components depending on the type of remote server you're configuring. The validation requirements differ between **Deployment Servers** and **Build Servers**.

For **Deployment Servers**, Dokploy requires the following 7 components to be properly configured:

1. **Docker Installed**: Docker must be installed on the remote server.
2. **RClone Installed**: RClone must be installed on the remote server.
3. **Nixpacks Installed**: Nixpacks must be installed on the remote server.
4. **Railpack Installed**: Railpack must be installed on the remote server.
5. **Buildpacks Installed**: Buildpacks must be installed on the remote server.
6. **Docker Swarm Initialized**: Docker Swarm must be initialized on the remote server.
7. **Dokploy Network Created**: A Docker network for Dokploy must be created on the remote server.
8. **Main Directory Created**: A directory must be created on the remote server to store applications.

Deployment servers are used to run and host your applications. They require Docker Swarm and network configuration since they need to run containers and manage deployments.

For **Build Servers**, Dokploy only validates the following components:

1. **Docker Installed**: Docker must be installed on the remote server.
2. **RClone Installed**: RClone must be installed on the remote server.
3. **Nixpacks Installed**: Nixpacks must be installed on the remote server.
4. **Railpack Installed**: Railpack must be installed on the remote server.
5. **Buildpacks Installed**: Buildpacks must be installed on the remote server.
6. **Main Directory Created**: A directory must be created on the remote server to store applications.

Build servers are dedicated to building and compiling applications. They don't require Docker Swarm or network configuration since they only build images and push them to a registry, without running any containers.

Once all requirements are met for your server type, you will see a green checkmark next to each item in the validation section.

![Multi-Server Setup](https://docs.dokploy.com/_next/image?url=%2Fassets%2Fimages%2Fserver-validate.png&w=3840&q=75)