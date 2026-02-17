---
title: Expired GitHub Personal Access Token (PAT)
url: https://coolify.io/docs/troubleshoot/docker/expired-github-personal-access-token.md
source: llms
fetched_at: 2026-02-17T14:41:49.892501-03:00
rendered_js: false
word_count: 55
summary: This document provides troubleshooting steps for authentication errors encountered when using Docker with the GitHub Container Registry due to expired Personal Access Tokens. It outlines solutions such as logging out of the registry or renewing the access token to restore connectivity.
tags:
    - github-container-registry
    - ghcr-io
    - docker-authentication
    - personal-access-token
    - troubleshooting
    - error-handling
category: guide
---

# Expired GitHub Personal Access Token (PAT)

If you encounter the following errors, it means Docker cannot authenticate with the GitHub Container Registry (ghcr.io):

## Error

```sh
  Error response from daemon: Head "https://ghcr.io/v2/coollabsio/coolify-helper/manifests/1.0.1": unauthorized: authentication required
```

> or

```sh
  Unable to find image 'ghcr.io/coollabsio/coolify-helper:latest' locally
  docker: Error response from daemon: Head "https://ghcr.io/v2/coollabsio/coolify-helper/manifests/latest": denied: denied
```

## Solution

You have two options:

* Log out of GitHub Container Registry (ghcr.io) by running:
  ```sh
    docker logout ghcr.io
  ```
* Renew your GitHub Personal Access Token (PAT) if you need to maintain authenticated access for deployments.