---
title: Unleash
url: https://coolify.io/docs/services/unleash.md
source: llms
fetched_at: 2026-02-17T14:48:51.047735-03:00
rendered_js: false
word_count: 79
summary: This document describes Unleash, an open-source feature flagging service, and details its two primary deployment configurations available within the Coolify platform.
tags:
    - feature-flagging
    - unleash
    - coolify
    - postgresql
    - self-hosted
    - deployment-options
category: configuration
---

![Unleash](https://raw.githubusercontent.com/Unleash/unleash/main/.github/github_header_opaque_landscape.svg)

## What is Unleash?

Unleash is an open source feature flagging service.

## Deployment Variants

Unleash is available in two deployment configurations in Coolify:

### Unleash with PostgreSQL

* **Database:** PostgreSQL
* **Use case:** Standard deployments with managed database
* **Components:**
  * Unleash container
  * PostgreSQL container
  * Automatic database configuration and health checks

### Unleash without Database

* **Database:** External (user-provided)
* **Use case:** Advanced deployments with existing database infrastructure or custom database configurations
* **Components:**
  * Unleash container
  * Requires external database connection configuration

## Screenshots

![Unleash Preview](https://raw.githubusercontent.com/Unleash/unleash/main/.github/github_online_demo.svg)

## Links

* [Official Website](https://getunleash.io)
* [GitHub](https://github.com/unleash/unleash)