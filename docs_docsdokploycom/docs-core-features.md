---
title: Features | Dokploy
url: https://docs.dokploy.com/docs/core/features
source: crawler
fetched_at: 2026-02-14T14:18:00.106253-03:00
rendered_js: true
word_count: 478
summary: This document provides a comprehensive overview of Dokploy's features for managing application deployments, Docker Compose configurations, and database lifecycle operations.
tags:
    - dokploy
    - application-deployment
    - docker-compose
    - database-management
    - monitoring
    - devops
    - containerization
category: reference
---

Explore the comprehensive suite of features available in Dokploy for optimized application deployment and management.

Dokploy provides a comprehensive suite of features designed to simplify and enhance the application deployment process.

Dokploy supports two primary methods for deploying applications:

1. **Applications**: This straightforward method allows for effortless deployment. Ideal for single applications, it offers a near plug-and-play experience.
2. **Docker Compose**: A more advanced option, requiring the creation of Dockerfiles and `docker-compose.yml`. This method provides greater control over deployment settings and full utilization of Docker Compose capabilities.

### [Applications Management](#applications-management)

Manage your applications through a range of features:

**Basic Operations**:

1. Deploy, stop, and delete applications.
2. Open a terminal directly in the application container.

**Source and Build Configuration**:

1. Choose source providers (GitHub, Git, Docker).
2. Select build types (Docker, Nixpacks, Heroku Buildpacks, Paketo Buildpacks).

**Environment Management**:

1. Add and manage environment variables.

**Monitoring Tools**:

1. Monitor CPU, memory, disk, and network usage.

**Logs**:

1. Access real-time logs.

**Deployments**:

1. View and manage deployments, you can see the logs of the building application.
2. Cancel queued deployments in case you have a lot of deployments in the queue, the most common is when you push alot of times in your repository, you can cancel the incoming queues, not the deployments that are already running.

**Domain Management**:

1. Add, delete, and generate domains.

**Advanced Settings**:

1. Customize initial commands and cluster settings.
2. Set resource limits and manage volumes for data persistence.
3. Configure redirects, security headers, and port settings.
4. Detailed Traefik configuration for specific needs.

### [Docker Compose Management](#docker-compose-management)

Enhance your Docker Compose experience with these advanced functionalities:

**Lifecycle Management**:

1. Deploy, stop, and delete Docker Compose setups.
2. Open a terminal with service selection capability.

**Source Configuration**:

1. Choose source providers (GitHub, Git, Raw).

**Environment Management**:

1. Add and manage environment variables.

**Monitoring Tools**:

1. Monitor CPU, memory, disk, and network usage of each service.

**Logs**:

1. View real-time logs of each service.

**Deployments**:

1. View and manage deployments, you can see the logs of the building application.
2. Cancel queued deployments in case you have a lot of deployments in the queue, the most common is when you push alot of times in your repository, you can cancel the incoming queues, not the deployments that are already running.

**Advanced Settings**:

1. Append command, by default we use a internal command to build the docker compose however, you can append a command to the existing one.
2. Manage volumes and mounts.

Deploy and manage a variety of databases:

**Supported Databases**:

1. MySQL, PostgreSQL, MongoDB, Redis, MariaDB.

**General Management**:

1. Deploy, stop, and delete databases.
2. Open a terminal within the database container.

**Environment and Monitoring**:

1. Manage environment variables.
2. Monitor CPU, memory, disk, and network usage.

**Backups and Logs**:

1. Configure manual and scheduled backups.
2. View real-time logs.

**Advanced Configuration**:

1. Use custom Docker images and initial commands.
2. Configure volumes and resource limits.

These features are designed to offer flexibility and control over your deployment environments, ensuring that Dokploy meets the diverse needs of modern application deployment and management.