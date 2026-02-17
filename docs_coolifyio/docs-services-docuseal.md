---
title: Docuseal
url: https://coolify.io/docs/services/docuseal.md
source: llms
fetched_at: 2026-02-17T14:43:28.965263-03:00
rendered_js: false
word_count: 90
summary: This document introduces Docuseal, an open-source document signing platform, and details its available deployment configurations using either SQLite or PostgreSQL within the Coolify ecosystem.
tags:
    - docuseal
    - document-signing
    - open-source
    - deployment-options
    - coolify
    - postgresql
    - sqlite
category: configuration
---

## What is Docuseal?

Document Signing for Everyone free forever for individuals, extensible for businesses and developers. Open Source Alternative to DocuSign, PandaDoc and more.

## Deployment Variants

DocuSeal is available in two deployment configurations in Coolify:

### DocuSeal (Default)

* **Database:** SQLite (embedded)
* **Use case:** Simple deployments, testing, or low-volume document signing
* **Components:** Single DocuSeal container with built-in SQLite database

### DocuSeal with PostgreSQL

* **Database:** PostgreSQL
* **Use case:** Production deployments requiring better performance, scalability, and concurrent access
* **Components:**
  * DocuSeal container
  * PostgreSQL container
  * Automatic database configuration and health checks

## Screenshots

## Links

* [The official website](https://www.docuseal.co?utm_source=coolify.io)
* [GitHub](https://github.com/docusealco/docuseal?utm_source=coolify.io)