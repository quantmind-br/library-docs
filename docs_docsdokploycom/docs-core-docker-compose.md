---
title: Docker Compose | Dokploy
url: https://docs.dokploy.com/docs/core/docker-compose
source: crawler
fetched_at: 2026-02-14T14:18:09.431934-03:00
rendered_js: true
word_count: 820
summary: This guide explains how to integrate and manage applications using Docker Compose and Docker Stack within Dokploy, covering configuration, environment variables, and deployment.
tags:
    - dokploy
    - docker-compose
    - docker-stack
    - container-orchestration
    - deployment-management
    - volume-persistence
    - devops
category: guide
---

Learn how to use Docker Compose with Dokploy

Dokploy integrates with Docker Compose and Docker Stack to provide flexible deployment solutions. Whether you are developing locally or deploying at scale, Dokploy facilitates application management through these powerful Docker tools.

### [Configuration Methods](#configuration-methods)

Dokploy provides two methods for creating Docker Compose configurations:

- **Docker Compose**: Ideal for standard Docker Compose configurations.
- **Stack**: Geared towards orchestrating applications using Docker Swarm. Note that some Docker Compose features, such as `build`, are not available in this mode.

### [General](#general)

Configure the source of your code, the way your application is built, and also manage actions like deploying, updating, and deleting your application, and stopping it.

### [Enviroment](#enviroment)

A code editor within Dokploy allows you to specify environment variables for your Docker Compose file. By default, Dokploy creates a `.env` file in the specified Docker Compose file path.

### [Monitoring](#monitoring)

Monitor each service individually within Dokploy. If your application consists of multiple services, each can be monitored separately to ensure optimal performance.

### [Logs](#logs)

Access detailed logs for each service through the Dokploy log viewer, which can help in troubleshooting and ensuring the stability of your services.

### [Deployments](#deployments)

You can view the last 10 deployments of your application. When you deploy your application in real time, a new deployment record will be created and it will gradually show you how your application is being built.

We also offer a button to cancel deployments that are in queue. Note that those in progress cannot be canceled.

We provide a webhook so that you can trigger your own deployments by pushing to your GitHub, Gitea, GitLab, Bitbucket repository.

### [Advanced](#advanced)

This section provides advanced configuration options for experienced users. It includes tools for custom commands within the container and volumes.

- **Command**: Dokploy has a defined command to run the Docker Compose file, ensuring complete control through the UI. However, you can append flags or options to the command.
  
  Using Private Registries with Docker Stack
  
  If you're deploying with **Docker Stack** (Docker Swarm mode) using **replicas** and a **private registry**, you need to add the `--with-registry-auth` flag to ensure that registry credentials are properly distributed to all nodes in your swarm.
  
  Without this flag, worker nodes may fail to pull images from private registries, resulting in authentication errors like "no such image" or "docker authentication failed".
  
  This flag ensures that Docker shares the registry credentials with all swarm nodes during deployment, enabling them to authenticate and pull images from your private registry (GitHub Container Registry, Docker Hub private repos, etc.).
- **Volumes**: To ensure data persistence across deployments, configure storage volumes for your application.

![home og image](https://docs.dokploy.com/_next/image?url=%2Fassets%2Fimages%2Fcompose%2Foverview.png&w=3840&q=75)

Volumes

Docker volumes are a way to persist data generated and used by Docker containers. They are particularly useful for maintaining data between container restarts or for sharing data among different containers.

Dokploy supports two methods for data persistence in Docker Compose:

### [Method 1: Bind Mounts (../files folder)](#method-1-bind-mounts-files-folder)

Use bind mounts for simple persistence needs, configuration files, or when you need direct access to files on the host. This method maps a directory from the host machine into the container.

**Important:** Avoid using absolute host paths, as they will be cleaned up during deployments:

```
volumes:
  - "/folder:/path/in/container" ❌
```

Instead, use the `../files` folder to ensure your data persists between deployments:

```
volumes:
  - "../files/my-database:/var/lib/mysql" ✅
  - "../files/my-configs:/etc/my-app/config" ✅
```

**Use bind mounts when:**

- You need simple data persistence
- You're mounting configuration files or small datasets
- You want direct file access on the host
- You don't need automated backups via Dokploy's Volume Backups feature

### [Method 2: Docker Named Volumes](#method-2-docker-named-volumes)

Use Docker named volumes when you need automated backups, better portability, or Docker-managed storage. Named volumes are managed by Docker and can be backed up automatically using Dokploy's [Volume Backups](https://docs.dokploy.com/docs/core/volume-backups) feature.

```
services:
  app:
    image: dokploy/dokploy:latest
    volumes:
      - my-database:/var/lib/mysql
      - my-app-data:/app/data

volumes:
  my-database:
  my-app-data:
```

**Use named volumes when:**

- You need automated backups to S3 (via Volume Backups)
- You want Docker-managed storage (better portability)
- You're storing databases or large datasets
- You need backup and restore capabilities

**Note:** Volume Backups only work with Docker named volumes, not with bind mounts (`../files`). If you need backup functionality, use named volumes instead of bind mounts.

### [Choosing the Right Method](#choosing-the-right-method)

FeatureBind Mounts (../files)Named VolumesSimple persistence✅ Yes✅ YesDirect host access✅ Yes❌ NoAutomated backups❌ No✅ YesDocker-managed❌ No✅ YesBest for config files✅ Yes⚠️ Possible but less commonBest for databases⚠️ Possible✅ Recommended

**Important:** If you need to use files from your repository (configuration files, scripts, etc.), you must move them to Dokploy's File Mounts (via Advanced → Mounts) instead of mounting them directly from the repository. When using AutoDeploy, Dokploy performs a `git clone` on each deployment, which clears the repository directory. Mounting files directly from your repository using relative paths (e.g., `./` or `./config/file.conf`) will cause them to be lost or empty in subsequent deployments. See the [Troubleshooting guide](https://docs.dokploy.com/docs/core/troubleshooting#using-files-from-your-repository) for more details.

To help speed up navigating there are some built in keyboard shortcuts for navigating tabs on docker compose pages. Similar to GitHub these are all prefixed with the `g` key so to use them press `g` and then the shortcut key.

KeyTab`g`General`e`Environment`u`Domains`d`Deployments`b`Backups`s`Schedules`v`Volume Backups`l`Logs`m`Monitoring`a`Advanced