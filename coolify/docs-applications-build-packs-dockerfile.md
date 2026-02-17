---
title: Dockerfile Build Pack
url: https://coolify.io/docs/applications/build-packs/dockerfile.md
source: llms
fetched_at: 2026-02-17T14:39:10.43038-03:00
rendered_js: false
word_count: 661
summary: This document provides instructions on how to use custom Dockerfiles to deploy applications on Coolify, covering repository setup, build pack configuration, and advanced settings.
tags:
    - coolify
    - dockerfile
    - deployment
    - build-packs
    - containerization
    - devops
    - ci-cd
    - troubleshooting
category: guide
---

Dockerfile includes step-by-step instructions to build a Docker image that Coolify uses to deploy your application or website.

The Dockerfile build pack allows you to use your own Dockerfile to deploy your application, you have complete control over how your application is built and deployed on Coolify.

## How to use Dockerfile?

### 1. Create a New Resource in Coolify

On the Coolify dashboard, open your project and click the **Create New Resource** button.

### 2. Choose Your Deployment Option

**A.** If your Git repository is public, choose the **Public Repository** option.

**B.** If your repository is private, you can select **Github App** or **Deploy Key**. (These methods require extra configuration. You can check the guides on setting up a [Github App](/applications/ci-cd/github/integration#with-github-app-recommended) or [Deploy Key](/applications/ci-cd/github/integration#with-deploy-keys) if needed.)

### 3. Select Your Git Repository

If you are using a public repository, paste the URL of your GitHub repository when prompted. The steps are very similar for all other options.

### 4. Choose the Build Pack

Coolify defaults to using Nixpacks. Click the Nixpacks option and select **Dockerfile** as your build pack from the dropdown menu.

### 5. Configure the Build Pack

* **Branch:** Coolify will automatically detect the branch in your repository.
* **Base Directory:** Enter the directory that Coolify should use as the root. Use `/` if your files are at the root or specify a subfolder (like `/backend` for a monorepo).

Click on **Continue** button once you have set all the above settings to correct details.

### 6. Configure Network Settings

After clicking **Continue**, update settings like your domain and environment variables (if needed).

The important option is the port where your application runs.
Coolify sets the default port to 3000, so if your application listens on a different port, update the port number on the network section.

## Advanced Configuration

### Environment Variables

You can manage your environment variables from the Coolify UI.

Click on the **Environment Variables** tab to add or update them.

### Pre/Post Deployment Commands

### Build Arguments

Coolify automatically injects build arguments into your Dockerfile during the build process. These include environment variables you've configured and predefined system values like `SOURCE_COMMIT`.

You can configure these settings in the **Advanced** menu of your application.

#### Inject Build Args to Dockerfile

By default, Coolify injects Docker build arguments (`ARG` statements) into your Dockerfile. If you prefer to manage build arguments manually in your Dockerfile, you can disable this behavior in the Advanced menu.

* **Enabled (default):** Coolify automatically injects build arguments
* **Disabled:** You manage `ARG` statements yourself in the Dockerfile

#### Include Source Commit in Build

The `SOURCE_COMMIT` variable contains the Git commit hash of your source code. By default, this is excluded from the build to preserve Docker's build cache. You can enable this in the Advanced menu if needed.

* **Disabled (default):** `SOURCE_COMMIT` is not included, improving cache utilization
* **Enabled:** `SOURCE_COMMIT` is included as a build argument

::: warning Build Cache Optimization
Enabling "Include Source Commit in Build" will cause Docker's build cache to be invalidated on every commit, since the commit hash changes each time. Only enable this if your build process requires the commit hash.
:::

## Known Issues and Solutions

::: details 1. Visiting the Application Domain Shows "No Available Server"
If you see a "No Available Server" error when visiting your website, it is likely due to the health check for your container.

Run `docker ps` on your server terminal to check if your container is unhealthy or still starting.

To resolve this, fix the issue causing the container to be unhealthy or remove the health checks.
:::

::: details 2. App only works inside the Container
If your app works when you check it with a `curl localhost` inside the container but you receive a 404 or "No Available Server" error when accessing your domain, verify the port settings.

Make sure that the port in the network settings matches the port where your application is listening. Also, check the startup log to ensure the application is not only listening on localhost.

If needed, change it to listen on all interfaces (for example, `0.0.0.0`).
:::