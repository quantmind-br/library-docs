---
title: Build Server | Dokploy
url: https://docs.dokploy.com/docs/core/remote-servers/build-server
source: crawler
fetched_at: 2026-02-14T14:12:46.657963-03:00
rendered_js: true
word_count: 753
summary: This document provides instructions on setting up and configuring dedicated build servers in Dokploy to separate the application compilation process from deployment environments. It covers server setup, registry integration, and the workflow for building and pushing Docker images to remote servers.
tags:
    - dokploy
    - build-server
    - docker-registry
    - deployment-workflow
    - server-management
    - resource-optimization
    - ci-cd
category: guide
---

Learn how to configure a custom build server to compile your applications separately from your deployment servers.

Build servers allow you to separate the build process from your deployment servers. This is particularly useful when you want to compile your applications on a dedicated server with more resources, or when you want to keep your deployment servers lightweight.

Build servers are currently **only available for Applications**. This feature is not supported for Docker Compose deployments.

A **Build Server** is a remote server dedicated to building and compiling your applications. Instead of building your application on the deployment server, Dokploy will:

1. Connect to the build server
2. Clone your repository and build your application
3. Create a Docker image
4. Push the image to a registry
5. Deploy the image to your deployment server

This approach offers several benefits:

- **Resource Optimization**: Use powerful build servers without paying for expensive deployment servers
- **Security**: Keep your source code and build process separate from production
- **Flexibility**: Build once, deploy to multiple servers
- **Performance**: Dedicated build resources mean faster builds

Before setting up a build server, ensure you have:

1. A Dokploy instance running
2. A remote server for builds (VPS, cloud instance, or dedicated server)
3. SSH access to the build server
4. Docker installed on the build server (or use Dokploy's automatic setup)
5. A Docker registry to store your built images (Docker Hub, GitHub Container Registry, etc.)

You can use the same SSH key you created for deploy servers, or create a dedicated one for build servers.

### [Step 1: Add a New Server](#step-1-add-a-new-server)

Navigate to **Dashboard → Remote Servers → Add Server -&gt; Build Type (Build Server)** in your Dokploy dashboard.

Fill in the server details:

- **Name**: A descriptive name (e.g., "Build Server - EU")
- **IP Address**: The public IP address of your build server
- **Port**: SSH port (default is 22)
- **Username**: SSH username (usually `root` or your custom user)
- **SSH Key**: Select the SSH key to use for authentication

### [Step 2: Setup the Build Server](#step-2-setup-the-build-server)

After creating the server, you need to install Docker and configure it:

1. Click on the server you just created
2. Click on **Setup Server -&gt;**
3. Follow the setup instructions:
   
   - **Automatic Setup**: Copy the command and run it on your server
   - **Manual Setup**: Follow the step-by-step instructions if automatic setup fails

Make sure your build server has enough disk space for Docker images. Build processes can consume significant storage. To prevent disk space issues, you can:

- Enable **Docker Cleanup** in the server settings to automatically remove unused images
- Create a **Scheduled Job** to periodically clean up Docker images (e.g., `docker image prune -af`)

### [Step 3: Configure as Build Server](#step-3-configure-as-build-server)

Once you have access to the server, you need to configure it as a build server:

1. Go to the **Deployments** tab
2. Click on the **Setup Server** button
3. A modal will appear showing the commands being executed on the server to configure everything necessary
4. Once the setup process finishes, navigate to the **Validate** tab
5. Verify that all status items show as green, indicating the build server is ready

The build server setup only installs build dependencies and tools. No Docker containers or active processes are deployed. The following tools are installed: **Nixpacks**, **Docker**, **Railpack**, and **Heroku Buildpacks**.

### [Configure an Application to Use a Build Server](#configure-an-application-to-use-a-build-server)

When creating or editing an application:

1. Go to the **Advanced** tab
2. In the **Build Server** section:
   
   - **Enable Custom Build Server**: Toggle this on
   - **Select Build Server**: Choose your build server from the dropdown
3. **Configure Registry** (required for build servers):
   
   - Go to **Settings → Registries**
   - Add a Docker registry (Docker Hub, GHCR, etc.)
   - Configure your registry credentials
4. **Select Registry in Application**:
   
   - In your application's **Advanced** tab
   - Under **Cluster Settings**
   - Select the registry where built images will be pushed

A registry is required when using build servers because the built image needs to be stored somewhere accessible to your deployment servers.

### [Build Process Flow](#build-process-flow)

When you deploy an application with a custom build server:

1. **Build Phase**:
   
   - Dokploy connects to your build server via SSH
   - Clones your repository on the build server
   - Builds the Docker image on the build server
   - Pushes the image to your configured registry
2. **Deploy Phase**:
   
   - Dokploy connects to your deployment server(s)
   - Pulls the built image from the registry
   - Deploys the container on your deployment server(s)

After the build image is pushed to the registry, allow a few moments for your deployment server(s) to pull and cache the image before it becomes available for deployment.

Build servers require a Docker registry to store built images. For detailed instructions on configuring a registry, see the [Docker Registry](https://docs.dokploy.com/docs/core/registry) guide.