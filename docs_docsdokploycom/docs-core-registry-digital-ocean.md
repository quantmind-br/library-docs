---
title: Digital Ocean | Dokploy
url: https://docs.dokploy.com/docs/core/registry/digital-ocean
source: crawler
fetched_at: 2026-02-14T14:12:53.135124-03:00
rendered_js: true
word_count: 151
summary: This document provides step-by-step instructions for configuring and connecting a Digital Ocean Container Registry to Dokploy using API tokens and Docker credentials.
tags:
    - digital-ocean
    - container-registry
    - dokploy
    - configuration-guide
    - docker-credentials
    - api-tokens
category: configuration
---

Configure a Digital Ocean Container Registry to store your images and artifacts.

To configure a Digital Ocean Container Registry, you need to fill the form with the following details:

01. Insert the Registry Name eg. `My Registry`.
02. Go to `https://cloud.digitalocean.com/registry/new` and click on `Create a Container Registry`.
03. Insert a lowercase name eg. `dokploy-username`.
04. Click on `Create Registry`.
05. Click on `Actions` and then `Download Docker Credentials`.
06. In Permissions select `Read` and `Write`.
07. Open the downloaded file and copy the auth value and type as `Password` in Dokploy Modal.
08. Go to `https://cloud.digitalocean.com/account/api/tokens` and click on `Generate New Token`.
09. In permissions select `Registry`.
10. Click on `Create`.
11. Copy the `access token` and paste it in Dokploy Modal as a `Username` field.
12. (Optional) If you pretend to use Cluster Feature, make sure to set a `Image Prefix`.
13. Registry URL: set `registry.digitalocean.com`
14. Click on `Test` to make sure everything is working.
15. Click on `Create` to save the registry.