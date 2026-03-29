---
title: fly.io
url: https://docs.getbifrost.ai/deployment-guides/fly.md
source: llms
fetched_at: 2026-01-21T19:43:15.294194555-03:00
rendered_js: false
word_count: 119
summary: This document provides step-by-step instructions for deploying Bifrost to Fly.io using either a cloned repository with a custom build process or a pre-built Docker Hub image.
tags:
    - bifrost
    - fly-io
    - deployment
    - docker
    - cloud-hosting
    - devops
category: guide
---

# fly.io

> This guide explains how to deploy Bifrost on fly.io

As `Bifrost` uses multiple sub-modules (`core`, `framework`, etc.) and also embeds the front-end into a single binary (embed.FS), we use a custom Docker build step before we hand over the deployment to flyctl.

There are two ways to deploy Bifrost on Fly.io:

1. By cloning the repo
2. Using flyctl + Docker Hub image

## By cloning the repo

1. Clone [https://github.com/maximhq/bifrost](https://github.com/maximhq/bifrost)
2. Ensure [Make](/deployment-guides/how-to/install-make) is installed.
3. Run `make deploy-to-fly-io APP_NAME=<your-fly-app-name>`

## Using flyctl + Docker Hub image

1. Update your `fly.toml` to specify the Bifrost Docker Hub image.

```toml  theme={null}
[build]
image = "maximhq/bifrost:latest"
```

2. Or you can specify the Docker Hub image path in the command:

```
fly deploy --app <your-app-name> --image docker.io/maximhq/bifrost:latest
```


---

> To find navigation and other pages in this documentation, fetch the llms.txt file at: https://docs.getbifrost.ai/llms.txt