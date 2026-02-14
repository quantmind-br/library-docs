---
title: Example | Dokploy
url: https://docs.dokploy.com/docs/core/docker-compose/example
source: crawler
fetched_at: 2026-02-14T14:18:26.967563-03:00
rendered_js: true
word_count: 354
summary: This tutorial explains how to deploy Docker Compose applications on Dokploy and manually configure domains using Traefik labels and external networks.
tags:
    - dokploy
    - docker-compose
    - traefik
    - deployment
    - networking
    - ssl-certificates
    - domain-configuration
category: tutorial
---

Learn how to use Docker Compose with Dokploy

In this tutorial, we will create a simple application using Docker Compose and route the traffic to an accessible domain.

**Note**: There are two ways to configure domains for Docker Compose applications:

1. **Using Dokploy Domains** (Recommended): Configure domains directly in the Dokploy UI through the **Domains** tab. See the [Domains guide](https://docs.dokploy.com/docs/core/domains) for details.
2. **Manual Configuration**: Configure domains using Traefik labels in your Docker Compose file (shown in this tutorial).

This tutorial demonstrates the manual method. For most users, we recommend using the Dokploy Domains feature as it's simpler and doesn't require editing your Docker Compose file.

### [Steps](#steps)

1. Create a new project.
2. Create a new service `Compose` and select the Compose Type `Docker Compose`.
3. Fork this repository: [Repo](https://github.com/Dokploy/docker-compose-test).
4. Select Provider type: GitHub or Git.
5. Select the repository: `Dokploy/docker-compose-test`.
6. Select the branch: `main`.
7. Set the Compose Path to `./docker-compose.yml` and save. ![Docker compose configuration](https://docs.dokploy.com/_next/image?url=%2F_next%2Fstatic%2Fmedia%2Fsetup.01d20533.png&w=3840&q=75)

### [Updating Your `docker-compose.yml`](#updating-your-docker-composeyml)

Add the following to your existing `docker-compose.yml` file:

1. Add the network `dokploy-network` to each service.
2. Add labels for Traefik to make the service accessible through the domain.

Example:

Let's modify the following compose file to make it work with Dokploy:

```
version: "3"

services:
  next-app:
    build:
      context: ./next-app
      dockerfile: prod.Dockerfile
      args:
        ENV_VARIABLE: ${ENV_VARIABLE}
        NEXT_PUBLIC_ENV_VARIABLE: ${NEXT_PUBLIC_ENV_VARIABLE}
    restart: always
    ports:
      - 3000:3000
    networks:
      - my_network
networks:
  my_network:
    external: true
```

Updated version with dokploy-network and Traefik labels:

Don't set container\_name property to the each service, it will cause issues with logs, metrics and other features

```
version: "3"

services:
  next-app:
    build:
      context: ./next-app
      dockerfile: prod.Dockerfile
      args:
        ENV_VARIABLE: ${ENV_VARIABLE}
        NEXT_PUBLIC_ENV_VARIABLE: ${NEXT_PUBLIC_ENV_VARIABLE}
    restart: always
    ports:
      - 3000
    networks:
      - dokploy-network
    labels:
      - "traefik.enable=true"
      - "traefik.http.routers.<unique-name>.rule=Host(`your-domain.com`)"
      - "traefik.http.routers.<unique-name>.entrypoints=websecure"
      - "traefik.http.routers.<unique-name>.tls.certResolver=letsencrypt"
      - "traefik.http.services.<unique-name>.loadbalancer.server.port=3000"
networks:
  dokploy-network:
    external: true
```

Make sure to point the A record to the domain you want to use for your service.

![home og image](https://docs.dokploy.com/_next/image?url=%2Fassets%2Fimages%2Fcompose%2Fdomain.png&w=3840&q=75)

Deploy the application by clicking on "deploy" and wait for the deployment to complete. Then give Traefik about 10 seconds to generate the certificates. You can then access the application through the domain you have set.

![home og image](https://docs.dokploy.com/_next/image?url=%2Fassets%2Fimages%2Fcompose%2Fapplication.png&w=3840&q=75)

**Tips**:

1. Set unique names for each router: `traefik.http.routers.<unique-name>`
2. Set unique names for each service: `traefik.http.services.<unique-name>`
3. Ensure the network is linked to the `dokploy-network`
4. Set the entry point to websecure and the certificate resolver to letsencrypt to generate certificates.
5. **For Docker Stack**: If you're using Docker Stack (Docker Swarm mode), place the labels under `deploy.labels` instead of directly under `labels`. See the [Domains guide](https://docs.dokploy.com/docs/core/docker-compose/domains) for the Docker Stack configuration example.