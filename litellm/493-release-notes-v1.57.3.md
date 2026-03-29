---
title: v1.57.3 - New Base Docker Image
url: https://docs.litellm.ai/release_notes/v1.57.3
source: sitemap
fetched_at: 2026-01-21T19:43:15.382877348-03:00
rendered_js: false
word_count: 120
summary: This document announces the migration of the LiteLLM base Docker image to a Chainguard Python image to ensure zero critical vulnerabilities and provides instructions for updating custom Dockerfiles.
tags:
    - docker-image
    - security
    - vulnerability-management
    - litellm
    - migration-guide
    - chainguard
category: guide
---

`docker image`, `security`, `vulnerability`

## What changed?[​](#what-changed "Direct link to What changed?")

- LiteLLMBase image now uses `cgr.dev/chainguard/python:latest-dev`

## Why the change?[​](#why-the-change "Direct link to Why the change?")

To ensure there are 0 critical/high vulnerabilities on LiteLLM Docker Image

## Migration Guide[​](#migration-guide "Direct link to Migration Guide")

- If you use a custom dockerfile with litellm as a base image + `apt-get`

Instead of `apt-get` use `apk`, the base litellm image will no longer have `apt-get` installed.

**You are only impacted if you use `apt-get` in your Dockerfile**

```
# Use the provided base image
FROM docker.litellm.ai/berriai/litellm:main-latest

# Set the working directory
WORKDIR /app

# Install dependencies - CHANGE THIS to `apk`
RUN apt-get update && apt-get install -y dumb-init 
```

Before Change

```
RUN apt-get update && apt-get install -y dumb-init
```

After Change

```
RUN apk update && apk add --no-cache dumb-init
```

- [What changed?](#what-changed)
- [Why the change?](#why-the-change)
- [Migration Guide](#migration-guide)