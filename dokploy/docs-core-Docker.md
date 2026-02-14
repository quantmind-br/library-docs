---
title: Docker Registry | Dokploy
url: https://docs.dokploy.com/docs/core/Docker
source: crawler
fetched_at: 2026-02-14T14:18:33.581246-03:00
rendered_js: true
word_count: 416
summary: This document explains how to configure and authenticate Docker Registry repositories in Dokploy for application deployments. It provides step-by-step instructions for connecting Docker Hub, GHCR, and public registries using various authentication methods.
tags:
    - docker-registry
    - dokploy
    - deployment-configuration
    - docker-hub
    - ghcr
    - container-images
    - authentication
category: configuration
---

Git Sources

Configure your Docker Registry repositories for deployments. This includes setting up access tokens, repository names, and authentication.

Dokploy provides seamless integration with Docker Registry repositories, allowing you to deploy applications directly from your container images. This feature is available for single applications and supports both public and private registries.

To connect a Docker Registry to your application:

1. Navigate to your application's **General** tab
2. Select **Docker** as the source
3. Configure the following settings:

SettingDescription**Docker Image**Full name of the Docker image (e.g., `nginx:latest`, `myorg/myapp:v1.0`)**Docker Registry URL**Registry URL (defaults to Docker Hub if not specified)**Docker Registry Username**Username for registry authentication**Docker Registry Password**Password or access token for authentication

For private registries, authentication is required. For public images, you can leave the username and password fields empty.

Docker Hub is the default registry and supports both username/password and token-based authentication.

### [Method 1: Username and Password](#method-1-username-and-password)

1. **Username**: Enter your Docker Hub username
2. **Password**: Enter your Docker Hub password

### [Method 2: Access Token (Recommended)](#method-2-access-token-recommended)

Using access tokens is more secure and allows fine-grained permissions:

1. **Create Access Token**:
   
   - Go to [Docker Hub Settings](https://hub.docker.com/settings/security) → **Personal Access Tokens**
   - Click **Generate New Token**
   - Set description: `Dokploy-Docker-Hub-Token`
   - Select **Read-only** permissions
   - Click **Generate**
2. **Configure in Dokploy**:
   
   - **Username**: Your Docker Hub username
   - **Password**: Paste the generated access token
   - **Registry URL**: Leave empty (defaults to Docker Hub)
3. **Deploy**: Click **Save** and then **Deploy** from the General tab

GHCR allows you to store container images alongside your GitHub repositories.

### [Prerequisites](#prerequisites)

- Your Docker image must already be published to GHCR
- You need a GitHub Personal Access Token with appropriate permissions

### [Setup Process](#setup-process)

1. **Create GitHub Personal Access Token**:
   
   - Go to [GitHub Settings](https://github.com/settings/tokens) → **Personal Access Tokens**
   - Click **Generate new token (classic)**
   - Set token name: `Dokploy-GHCR-Token`
   - Select the following scopes:
     
     - `repo` - Access to repositories
     - `workflow` - Access to GitHub Actions
     - `write:packages` - Upload packages
     - `delete:packages` - Delete packages
   - Click **Generate token**
2. **Configure in Dokploy**:
   
   - **Docker Image**: `ghcr.io/username/repository:tag`
   - **Registry URL**: `ghcr.io`
   - **Username**: Your GitHub username
   - **Password**: Paste the generated personal access token
3. **Deploy**: Click **Save** and then **Deploy** from the General tab

### [Public Images](#public-images)

For public images from any registry:

- **Docker Image**: Full image path (e.g., `quay.io/prometheus/prometheus:latest`)
- **Registry URL**: Registry domain (if not Docker Hub)
- **Username**: Leave empty
- **Password**: Leave empty

**Security Recommendations:**

- Use access tokens instead of passwords when possible
- Grant minimal required permissions to tokens
- Regularly rotate access tokens
- Use private registries for sensitive applications

Common issues and solutions:

- **Authentication Failed**: Verify your credentials and token permissions
- **Image Not Found**: Check the image name and tag spelling
- **Pull Rate Limits**: Consider using authenticated requests or private registries
- **Registry Timeout**: Verify the registry URL is accessible from your Dokploy instance