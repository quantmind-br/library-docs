---
title: Docker Hub | Dokploy
url: https://docs.dokploy.com/docs/core/registry/dockerhub
source: crawler
fetched_at: 2026-02-14T14:12:53.21452-03:00
rendered_js: true
word_count: 122
summary: This document provides a step-by-step guide for configuring a Docker Hub registry within the Dokploy platform, including how to set up access tokens and verify the connection.
tags:
    - docker-hub
    - dokploy
    - registry-configuration
    - access-tokens
    - container-storage
    - devops
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