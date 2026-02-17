---
title: Nitropage
url: https://coolify.io/docs/services/nitropage.md
source: llms
fetched_at: 2026-02-17T14:46:25.677054-03:00
rendered_js: false
word_count: 129
summary: This document introduces Nitropage, a visual website builder based on SolidStart, detailing its feature set and available deployment configurations on Coolify.
tags:
    - nitropage
    - website-builder
    - solidstart
    - coolify
    - postgresql
    - sqlite
    - deployment
category: concept
---

## What is Nitropage?

Nitropage is an extensible, visual website builder based on SolidStart, offering a growing library of versatile building blocks.

## Deployment Variants

Nitropage is available in two deployment configurations in Coolify:

### Nitropage (Default)

* **Database:** SQLite (embedded)
* **Use case:** Simple deployments, testing, or small websites
* **Components:** Single Nitropage container with built-in SQLite database

### Nitropage with PostgreSQL

* **Database:** PostgreSQL
* **Use case:** Production deployments requiring better performance and scalability
* **Components:**
  * Nitropage container
  * PostgreSQL container
  * Automatic database configuration and health checks

## Features

* Reusable element **Presets** and **Layouts**
* Publishing workflow with **Revisions**
* Starter kit with dozens of Blueprints
* Multiple websites on a single instance
* Image optimization with **focal point** cropping
* API for your custom [SolidJS](https://www.solidjs.com/?utm_source=coolify.io) page elements
* Powerful developer architecture with [Vite](https://vitejs.dev/?utm_source=coolify.io)
* Automatic sitemap.xml and Atom-feed handling

## Video

## Links

* [The official website](https://nitropage.org/?utm_source=coolify.io)
* [GitHub](https://codeberg.org/nitropage/nitropage?utm_source=coolify.io)