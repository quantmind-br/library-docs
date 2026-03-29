---
title: Uninstall | Dokploy
url: https://docs.dokploy.com/docs/core/uninstall
source: crawler
fetched_at: 2026-02-08T04:01:25.449389966-03:00
rendered_js: false
word_count: 57
summary: This document provides step-by-step instructions to completely remove Dokploy, its Docker services, volumes, networks, and associated files from a server.
tags:
    - dokploy
    - uninstallation
    - docker-cleanup
    - server-management
    - self-hosting
category: guide
---

Learn how to uninstall Dokploy on your server

Follow these steps to completely remove Dokploy and its components from your server.

Remove the docker swarm services created by Dokploy:

```
docker service remove dokploy dokploy-traefik dokploy-postgres dokploy-redis
docker container remove -f dokploy-traefik
```

Remove the docker volumes created by Dokploy:

```
docker volume remove -f dokploy dokploy-postgres dokploy-redis
```

Remove the docker network created by Dokploy:

```
docker network remove -f dokploy-network
```

Docker cleanup to remove leftovers:

```
docker container prune --force
docker image prune --all --force
docker volume prune --all --force
docker builder prune --all --force
docker system prune --all --volumes --force
```

Remove the dokploy files and directories from your server:

```
sudo rm -rf /etc/dokploy
```