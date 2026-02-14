---
title: GHCR | Dokploy
url: https://docs.dokploy.com/docs/core/registry/ghcr
source: crawler
fetched_at: 2026-02-14T14:12:52.294199-03:00
rendered_js: true
word_count: 124
summary: This document provides step-by-step instructions for configuring the GitHub Container Registry within the Dokploy platform, including authentication and token generation.
tags:
    - github-container-registry
    - ghcr
    - dokploy
    - authentication
    - docker-registry
    - container-images
category: configuration
---

Configure GitHub Container Registry to store your images and artifacts.

To configure a GitHub Container Registry, you need to fill the form with the following details:

01. Insert the Registry Name eg. `My Registry`.
02. Insert the Username eg. `github_username`.
03. Insert the Password, you can use your own github password or generate a token here `https://github.com/settings/tokens`
04. Click on Generate Token (Classic).
05. Insert the Note Description eg. `github_token`.
06. In permissions make sure to select `write:packages`.
07. Click on `Create`.
08. Copy the `access token` and paste it in Dokploy Modal as a Password field.
09. (Optional) If you pretend to use Cluster Feature, make sure to set a `Image Prefix`.
10. Registry URL: set `ghcr.io`
11. Click on `Test` to make sure everything is working.
12. Click on `Create` to save the registry.