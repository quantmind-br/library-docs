---
title: Registry | Dokploy
url: https://docs.dokploy.com/docs/core/registry
source: crawler
fetched_at: 2026-02-14T14:12:40.509371-03:00
rendered_js: true
word_count: 148
summary: This document explains how to configure and connect a Docker Registry to Dokploy to manage image storage and authentication credentials.
tags:
    - dokploy
    - docker-registry
    - image-storage
    - authentication
    - configuration
category: configuration
---

Configure your registry settings to store your images and artifacts.

Dokploy offers a UI to connect to any Docker Registry.

You need to fill the form with the following details:

- **Registry Name**: Enter a name for your registry eg. `My Registry`.
- **Username**: Enter the username you want to use to connect to your registry.
- **Password**: Enter the password you want to use to connect to your registry.
- **Image Prefix(Optional)**: Useful when using Cluster feature, to tag your images with a prefix eg. `dokploy` will convert to `dokploy/my-app:latest`.
- **Registry URL**: Enter the URL of your registry eg. `https://index.docker.io/v1`.

This approach allows you to authenticate and store your credentials on the machine, making it convenient when using multiple applications. You won't need to provide credentials for each one individually. It also enables seamless login to remote servers. If no server is selected, Dokploy will default to using its own server.