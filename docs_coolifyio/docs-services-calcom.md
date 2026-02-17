---
title: Calcom
url: https://coolify.io/docs/services/calcom.md
source: llms
fetched_at: 2026-02-17T14:42:40.653496-03:00
rendered_js: false
word_count: 42
summary: This document provides instructions for deploying Calcom scheduling infrastructure on x86 (amd64) architectures using Docker Compose. it details the necessary image and platform configuration changes required for compatibility.
tags:
    - calcom
    - scheduling-infrastructure
    - docker-compose
    - deployment
    - x86
    - amd64
category: guide
---

# Calcom

## What is Calcom

Scheduling infrastructure for everyone.

## Deploying on x86 (amd64)

You need to change default docker compose to the following to make cal.com work on x86 (amd64):

```yaml
services:
  calcom:
    image: 'calcom/cal.com:<VERSION compatible with amd64>
    platform: linux/amd64
    (... same ...)
```

You can check the latest amd64 compatible version [here](https://hub.docker.com/r/calcom/cal.com/tags).

Example:

```yaml
services:
  calcom:
    image: 'calcom/cal.com:v5.9.0
    platform: linux/amd64
    (... same ...)
```

## Links

* [Official Documentation](https://cal.com/docs/developing/introduction?utm_source=coolify.io)