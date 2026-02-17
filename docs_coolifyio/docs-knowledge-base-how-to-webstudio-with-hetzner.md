---
title: Deploy Webstudio Projects using Coolify
url: https://coolify.io/docs/knowledge-base/how-to/webstudio-with-hetzner.md
source: llms
fetched_at: 2026-02-17T14:40:47.617097-03:00
rendered_js: false
word_count: 706
summary: This guide provides step-by-step instructions for deploying Webstudio projects to a server using Coolify and GitHub. It covers project export, server setup, and establishing a continuous deployment workflow.
tags:
    - webstudio
    - coolify
    - deployment
    - self-hosting
    - docker
    - hetzner
    - ci-cd
category: guide
---

# Deploy Webstudio Projects using Coolify

Coolify makes deploying your Webstudio projects to Hetzner as simple as it is powerful.

In this guide, you’ll learn how to set up your project, deploy it on a Hetzner server, and keep your infrastructure fully under your control, all with a few straightforward steps.

::: warning HEADS UP!
In this guide, we are using servers from Hetzner.

However, if you're using a different hosting provider, you can still follow this guide with their servers as well.

If you prefer watching a video instead of reading, you can check out the [tutorial video](https://youtu.be/OnHLO2Plt2E?si=yDM77oK7Xd5UsRSP)
:::

## What You’ll Need

Before you start, make sure you have:

* A [GitHub account](https://github.com?utm_source=coolify.io) to host your code.
* A [Hetzner account](https://coolify.io/hetzner) to provision your server (or an account with any other hosting provider).
* The [Webstudio CLI](https://docs.webstudio.is/university/self-hosting/cli?utm_source=coolify.io) installed locally to manage your project exports.

## 1. Create Your GitHub Repository

Start by [creating a new repository](https://docs.github.com/en/repositories/creating-and-managing-repositories/creating-a-new-repository) on GitHub where you’ll store your Webstudio project code.

Once the repository is created, [clone the repository](https://docs.github.com/en/repositories/creating-and-managing-repositories/cloning-a-repository) to your local machine to start developing locally.

## 2. Export Your Webstudio Project

Using the Webstudio [CLI](https://docs.webstudio.is/university/self-hosting/cli), export your project and select the "**Docker**" option.

This prepares your project for deployment via Coolify without the need for additional dependency installations.

## 3. Push Your Code to GitHub

With your project exported locally, [push your code](https://docs.github.com/en/get-started/using-git/pushing-commits-to-a-remote-repository) to the GitHub repository you created. This makes your project accessible for deployment.

## 4. Set Up Your Hetzner Server

::: warning HEADS UP!
If you already have a server, you don't need to purchase a new one.

**Webstudio recommends** that your server should have at least **1 CPU and 2GB of RAM** for smooth operation.

Skip to [Step 6](#_6-configure-your-project-on-coolify) if your server is already connected to Coolify.
:::
Follow these steps to prepare your Hetzner server:

1. **Create a New Server:** Log into [Hetzner Cloud Dashboard ↗](https://console.hetzner.cloud/) and create a new server.

2. **Choose Your Region:** Select the region that best suits your needs.

3. **Select Ubuntu:** Pick an Ubuntu image (make sure it’s a Docker-supported version, check the [Docker Ubuntu requirements](https://docs.docker.com/engine/install/ubuntu/#os-requirements)).

4. **Configure Resources:** A shared CPU with at least 2 GB RAM is recommended.

5. **Allocate an IPv4 Address:** Make sure your server has a dedicated IPv4 address.

6. **Finalize Setup:** Click **Create and Buy Now** and wait until your server is provisioned.

7. **Save the IP:** Copy your server’s IPv4 address, it will be needed shortly.

## 5. Connect Coolify to Your Server

::: warning HEADS UP!
If your server is already connected to Coolify, skip to the [next step](#_6-configure-your-project-on-coolify).
:::

1. **Add Private Key:** Login to your Coolify account (or create one if you’re new) and Add a new private key

2) **Add a Server:** Navigate to the **Servers** tab and add a new server by entering your Hetzner server’s IPv4 address.

3. **Validate Server:** Click **Validate Server & Install Docker Engine**. Coolify will automatically install all necessary components on your server.

4. **Check Status:** Once finished, you should see a green **Proxy Running** status indicating everything is set up.

## 6. Configure Your Project on Coolify

1. **Create a New Project:** Head to the **Projects** section and create a new project.

2. **Add a Resource:** Add a new resource, selecting your GitHub repository as the source.

3. **Connect Your Repository:** Use the GitHub app integration to grant access to your repository.

4. **Select Build Pack:** Change the Build Pack to **Dockerfile** and click on continue button.

5. **Configure Domains & Deploy:** Enter your domain in the domains field and Click **Deploy** and wait as Coolify builds and deploys your project.

6. **Successful Deployment:** When deployment is complete, you’ll see a “Deployment is Finished” message.

7. **Access Your Site:** Use the **links** button at the top of the project dashboard to visit your live site.

8. **Optional – Third-Party Domains:** If your project loads images from external sources, add those domains as a comma-separated list under the environment variable `DOMAINS`. (make sure to restart the application after adding the variable)

## 7. Update Your Webstudio Site

To publish updates and keep your site up to date, follow these steps:

1. **Publish Changes:** In the Webstudio builder, click **Publish** to generate the latest build data.
2. **Sync and Build:** Run the following commands in your terminal:
   ```bash
   webstudio sync
   webstudio build --template docker
   ```
3. **Push Updates:** Commit and push your changes to GitHub. Coolify will detect the update and automatically trigger a new deployment.

Now you’re all set!