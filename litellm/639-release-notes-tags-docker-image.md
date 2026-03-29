---
title: One post tagged with "docker image" | liteLLM
url: https://docs.litellm.ai/release_notes/tags/docker-image
source: sitemap
fetched_at: 2026-01-21T19:41:36.014144707-03:00
rendered_js: false
word_count: 113
summary: This document explains the update of the LiteLLM Docker base image to a Chainguard image to eliminate security vulnerabilities and provides migration steps for users to switch from apt-get to apk.
tags:
    - docker-image
    - security
    - vulnerability-management
    - litellm
    - migration-guide
    - package-management
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