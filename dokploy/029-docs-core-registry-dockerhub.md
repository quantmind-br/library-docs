---
title: Docker Hub | Dokploy
url: https://docs.dokploy.com/docs/core/registry/dockerhub
source: crawler
fetched_at: 2026-02-14T14:18:16.094707-03:00
rendered_js: true
word_count: 122
summary: This document provides step-by-step instructions for configuring a Docker Hub registry to store images and artifacts, including how to generate and use access tokens.
tags:
    - docker-hub
    - registry-configuration
    - dokploy
    - access-token
    - container-images
    - artifact-storage
category: configuration
---

Configure Docker Hub to store your images and artifacts.

To configure a Docker Hub registry, you need to fill the form with the following details:

01. Insert the Registry Name eg. `My Registry`.
02. Insert the Username eg. `dockerhub_username`.
03. Insert the Password, you can use your own dockerhub password or generate a token here `https://app.docker.com/settings/personal-access-tokens`
04. Click on Generate Token.
05. Insert the Token Description eg. `dockerhub_token`.
06. In permissions make sure to select `Read` and `Write`.
07. Click on `Create`.
08. Copy the `access token` and paste it in Dokploy `Docker Hub` Modal section.
09. (Optional) If you pretend to use Cluster Feature, make sure to set a `Image Prefix` and `Registry URL`.
10. Click on `Test` to make sure everything is working.
11. Click on `Create` to save the registry.