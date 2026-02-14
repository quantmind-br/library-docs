---
title: Deployments | Dokploy
url: https://docs.dokploy.com/docs/core/remote-servers/deployments
source: crawler
fetched_at: 2026-02-14T14:18:12.903043-03:00
rendered_js: true
word_count: 157
summary: This document provides instructions for configuring and initializing a remote server deployment, detailing system requirements and the available setup actions.
tags:
    - remote-server
    - server-setup
    - deployment
    - bash-configuration
    - root-access
category: guide
---

Configure and set up your remote server deployment

To get started with remote servers, you'll need to configure the initial setup for your remote server.

The server setup process prepares the necessary environment for securely and efficiently deploying applications.

Important

Root access to the server is required. We currently do not support non-root deployments.

If your remote server is configured with a different shell (other than bash), you must configure bash as the default shell, as Dokploy has been developed and tested with bash.

![Remote Server Setup](https://docs.dokploy.com/_next/image?url=%2Fassets%2Fimages%2Fserver-deploy.png&w=3840&q=75)

We provide two main actions to configure your server:

- **Modify Script**: Allows you to view and customize the installation script that will be executed on your server. You can adjust it according to your specific needs.
- **Setup Server**: Initiates the configuration process on the remote server. When clicked, it will open a modal window showing real-time logs of the script execution.

Example of the server setup logs:

![Remote Server Setup](https://docs.dokploy.com/_next/image?url=%2Fassets%2Fimages%2Fserver-drawer.png&w=3840&q=75)