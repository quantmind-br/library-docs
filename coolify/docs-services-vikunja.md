---
title: Vikunja
url: https://coolify.io/docs/services/vikunja.md
source: llms
fetched_at: 2026-02-17T14:48:59.300843-03:00
rendered_js: false
word_count: 80
summary: This document introduces Vikunja, an open-source task manager, and outlines its deployment configurations on Coolify, specifically comparing SQLite and PostgreSQL setups.
tags:
    - vikunja
    - task-management
    - coolify
    - self-hosted
    - deployment-options
    - postgresql
    - sqlite
category: guide
---

![Vikunja](https://vikunja.cloud/images/vikunja-logo.svg)

## What is Vikunja?

Vikunja is an open source, self-hosted, task management application.

## Deployment Variants

Vikunja is available in two deployment configurations in Coolify:

### Vikunja (Default)

* **Database:** SQLite (embedded)
* **Use case:** Simple deployments, testing, or personal task management
* **Components:** Single Vikunja container with built-in SQLite database

### Vikunja with PostgreSQL

* **Database:** PostgreSQL
* **Use case:** Production deployments requiring better performance, concurrent access, and scalability
* **Components:**
  * Vikunja container
  * PostgreSQL container
  * Automatic database configuration and health checks

## Screenshots

![Vikunja Preview](https://vikunja.io/_astro/09-task-detail-dark.ppLbej6M_ZzaSch.avif)

## Links

* [Official Website](https://vikunja.io)
* [GitHub](https://kolaente.dev/vikunja/vikunja)