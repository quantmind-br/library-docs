---
title: Introduction | Dokploy
url: https://docs.dokploy.com/docs/core/remote-servers
source: crawler
fetched_at: 2026-02-14T14:12:46.147225-03:00
rendered_js: true
word_count: 466
summary: This document explains how to configure and use remote servers in Dokploy for application deployment and build processes, distinguishing between deployment and build server types.
tags:
    - dokploy
    - remote-deployment
    - server-management
    - docker-containers
    - build-servers
    - deployment-servers
category: guide
---

Deploy your apps to multiple servers remotely.

Remote servers allows you to deploy your apps remotely to different servers without needing to build and run them where the Dokploy UI is installed.

To use the remote servers feature, you need to have Dokploy UI installed either locally or on a remote server. We recommend using a remote server for better connectivity, security, and isolation, for remote instances we install only a traefik instance.

If you plan to only deploy apps to remote servers and use Dokploy UI for managing deployments, Dokploy will use around 250 MB of RAM and minimal CPU, so a low-resource server should be sufficient.

All the features we have documented previously are supported by Dokploy Remote Servers. The only feature not supported is remote server monitoring, due to performance reasons. However, all functionalities should work the same as when deploying on the same server where Dokploy UI is installed.

Dokploy supports two types of remote servers:

### [Deployment Servers](#deployment-servers)

**Deployment servers** are used to run and host your applications. These servers:

- Run your containerized applications
- Handle traffic routing through Traefik
- Manage application deployments and updates
- Store application data and volumes

When you deploy an application, it runs on a deployment server. You can have multiple deployment servers to distribute your applications across different locations or for redundancy.

### [Build Servers](#build-servers)

**Build servers** are dedicated servers used to compile and build your applications. These servers:

- Clone your repository
- Build Docker images from your source code
- Push built images to a Docker registry
- Do not run any containers or active processes

Build servers are particularly useful when you want to:

- Separate the build process from deployment
- Use powerful build resources without paying for expensive deployment servers
- Build once and deploy to multiple servers
- Keep your deployment servers lightweight

Build servers are currently **only available for Applications**. This feature is not supported for Docker Compose deployments.

You can configure an application to use a build server by selecting it in the application's **Advanced** settings. The built image will be pushed to a Docker registry, and then pulled by your deployment server(s) for deployment.

1. **Enter the terminal**: Allows you to access the terminal of the remote server.
2. **Setup Server**: Allows you to configure the remote server.
   
   - **SSH Keys**: Steps to add SSH keys to the remote server.
   - **Deployments**: Steps to configure the remote server for deploying applications.
3. **Edit Server**: Allows you to modify the remote server's details, such as SSH key, name, description, IP, etc.
4. **View Actions**: Lets you perform actions like managing the Traefik instance, storage, and activating Docker cleanup.
5. **Show Traefik File System**: Displays the contents of the remote server's directory.
6. **Show Docker Containers**: Shows the Docker containers running on the remote server.
7. **Show Docker Swarm Overview**: Shows the Docker Swarm overview of the remote server.