---
title: Custom Docker Registry
url: https://coolify.io/docs/knowledge-base/custom-docker-registry.md
source: llms
fetched_at: 2026-02-17T14:40:17.634169-03:00
rendered_js: false
word_count: 150
summary: This document explains how to configure or switch Coolify's default Docker registry between GitHub Container Registry and Docker Hub using environment variables during or after installation.
tags:
    - coolify
    - docker-registry
    - installation
    - environment-variables
    - docker-hub
    - ghcr
category: configuration
---

# Custom Docker Registry

If you would like to get Coolify's images from `dockerhub` instead of the default `ghcr.io`, you can do it by setting the `REGISTRY_URL` environment variable to `docker.io`.

## Registry URL (`REGISTRY_URL`)

* Valid values: `docker.io` & `ghcr.io`.

## Automated Installation Method

1. **Run Installation Command**

   Execute the automated installation script with your prepared credentials:

   ```bash
   env REGISTRY_URL=docker.io bash -c 'curl -fsSL https://cdn.coollabs.io/coolify/install.sh | bash'
   ```

   > View the [Scripts Source Code](https://github.com/coollabsio/coolify/blob/main/scripts/install.sh)

::: info
The installation script must be run as `root`. If you're not logged in as `root`, the script will use `sudo` to elevate privileges.

```bash
sudo -E env REGISTRY_URL=docker.io bash -c 'curl -fsSL https://cdn.coollabs.io/coolify/install.sh | bash'
```

:::

## Manual Installation Method

1. **Configure Environment Variables**

   Edit the environment variables file:

   ```bash
   nano /data/coolify/source/.env
   ```

   Add the following variables with your prepared credentials:

   ```bash
   REGISTRY_URL=docker.io
   ```

## Switch after installation

If you want to switch the registry after installation, you can do it by running the following command:

```bash
env REGISTRY_URL=docker.io bash -c 'curl -fsSL https://cdn.coollabs.io/coolify/install.sh | bash'
```

::: info
The installation script must be run as `root`. If you're not logged in as `root`, the script will use `sudo` to elevate privileges.

```bash
sudo -E env REGISTRY_URL=docker.io bash -c 'curl -fsSL https://cdn.coollabs.io/coolify/install.sh | bash'
```