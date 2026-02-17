---
title: Vvveb
url: https://coolify.io/docs/services/vvveb.md
source: llms
fetched_at: 2026-02-17T14:49:03.725783-03:00
rendered_js: false
word_count: 98
summary: This document provides an overview of the Vvveb CMS and describes its various deployment configurations and database options available on the Coolify platform.
tags:
    - vvveb
    - cms
    - coolify
    - deployment-options
    - database-configuration
    - ecommerce
category: configuration
---

# Vvveb

## What is Vvveb

Powerful and easy to use cms to build websites, blogs or ecommerce stores.

## Deployment Variants

Vvveb is available in three deployment configurations in Coolify:

### Vvveb (Default)

* **Database:** SQLite (embedded)
* **Use case:** Simple deployments, testing, or small websites
* **Components:** Single Vvveb container with built-in SQLite database

### Vvveb with MySQL

* **Database:** MySQL
* **Use case:** Production deployments with MySQL preference
* **Components:**
  * Vvveb container
  * MySQL container
  * Automatic database configuration and health checks

### Vvveb with MariaDB

* **Database:** MariaDB
* **Use case:** Production deployments with MariaDB preference
* **Components:**
  * Vvveb container
  * MariaDB container
  * Automatic database configuration and health checks

## Links

* [Official Documentation](https://docs.vvveb.com?utm_source=coolify.io)