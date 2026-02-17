---
title: Trigger
url: https://coolify.io/docs/services/trigger.md
source: llms
fetched_at: 2026-02-17T14:48:43.01254-03:00
rendered_js: false
word_count: 84
summary: This document describes the deployment options for Trigger.dev on the Coolify platform, outlining configurations for both internal and external PostgreSQL databases.
tags:
    - trigger-dev
    - coolify
    - background-jobs
    - typescript
    - deployment
    - postgresql
    - open-source
category: configuration
---

![Trigger](https://camo.githubusercontent.com/eab9fa8c4faf6ea7b868a38aea57abf375fc43233d257bc52314409f279ce541/68747470733a2f2f696d61676564656c69766572792e6e65742f3354627261666675445a34614566384b574f6d495f772f61343564316661322d306165382d346133392d343430392d6634663933346266616530302f7075626c6963)

## What is Trigger?

Trigger is an open source Background Jobs framework for TypeScript.

## Deployment Variants

Trigger.dev is available in two deployment configurations in Coolify:

### Trigger.dev (Default)

* **Database:** Built-in PostgreSQL
* **Use case:** Standard deployments with managed database
* **Components:**
  * Trigger.dev container
  * Built-in PostgreSQL container
  * Automatic database configuration and health checks

### Trigger.dev with External Database

* **Database:** External (user-provided)
* **Use case:** Advanced deployments with existing database infrastructure or custom database configurations
* **Components:**
  * Trigger.dev container
  * Requires `DATABASE_URL` environment variable pointing to your external database

## Links

* [Official Website](https://trigger.dev)
* [GitHub](https://github.com/triggerdotdev/trigger.dev)