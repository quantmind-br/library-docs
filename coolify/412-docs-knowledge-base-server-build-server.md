---
title: Build Server
url: https://coolify.io/docs/knowledge-base/server/build-server.md
source: llms
fetched_at: 2026-02-17T14:40:52.330418-03:00
rendered_js: false
word_count: 338
summary: This document explains how to set up and configure a dedicated build server in Coolify to offload project compilation tasks from hosting servers.
tags:
    - coolify
    - build-server
    - docker
    - deployment
    - server-management
    - container-registry
category: guide
---

A build server allows you to compile your projects separately from the server that hosts your live application.

This helps to keep the load on your hosting server low and ensures that your application's performance remains unaffected by the build process.

## Requirements

Before you set up a build server, make sure that:

* The final images are pushed to a container registry.
* The build server is authenticated with the container registry. See [this guide](/knowledge-base/docker/registry) for more details.
* The build server has access to your source code.
* Docker Engine is installed on the build server.
* The build server's architecture matches that of your deployment servers.

::: success Tip:
If you have multiple build servers, Coolify will select one at random.
:::

## How to Use a Build Server

To start using a build server with Coolify, follow these steps:

1. **Add a New Server to Coolify:**
   In your Coolify dashboard, go to the servers page and click the **+ Add** button.

   * If you have already connected a server to Coolify, you can skip this step and go to the next one.

2. **Enable the Build Server Feature:**
   In the popup modal, enable the **Build Server** feature.


   * If you have already connected your server, enable the Build Server feature as shown in the image below.

::: warning HEADS UP!
As of **Coolify v4.0.0-beta.408** you cannot deploy any application to a server that is marked as a build server.

If you want to deploy apps, uncheck the build server option on your server from the servers page in the Coolify dashboard.

## Configuring a Resource to Use a Build Server

To assign a build server to an existing resource, follow these steps:

1. **Go to Your Resource:**
   In your Coolify dashboard, navigate to the general settings of the application you want to use the build server for.

2. **Activate the Build Server Option:**
   Under the **Build** section, enable the `Use a Build Server ?` option.

3. **Set Up Your Container Registry:**
   Make sure that your build server is authenticated with the container registry. See [this guide](/knowledge-base/docker/registry) for more details.