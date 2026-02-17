---
title: Yamtrack
url: https://coolify.io/docs/services/yamtrack.md
source: llms
fetched_at: 2026-02-17T14:49:17.658203-03:00
rendered_js: false
word_count: 85
summary: This document provides an overview of Yamtrack, a self-hosted media tracker, and details its available deployment configurations on the Coolify platform.
tags:
    - yamtrack
    - media-tracker
    - self-hosted
    - coolify
    - deployment-options
    - postgresql
    - sqlite
category: reference
---

## What is Yamtrack?

Yamtrack is a self hosted media tracker for movies, tv shows, anime, manga, video games and books.

## Deployment Variants

Yamtrack is available in two deployment configurations in Coolify:

### Yamtrack (Default)

* **Database:** SQLite (embedded)
* **Use case:** Simple deployments, testing, or personal media tracking
* **Components:** Single Yamtrack container with built-in SQLite database

### Yamtrack with PostgreSQL

* **Database:** PostgreSQL
* **Use case:** Production deployments requiring better performance and data reliability
* **Components:**
  * Yamtrack container
  * PostgreSQL container
  * Automatic database configuration and health checks

## Screenshots

## Links

* [The official website](https://github.com/FuzzyGrim/Yamtrack/wiki?utm_source=coolify.io)
* [GitHub](https://github.com/FuzzyGrim/Yamtrack?utm_source=coolify.io)