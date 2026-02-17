---
title: Freshrss
url: https://coolify.io/docs/services/freshrss.md
source: llms
fetched_at: 2026-02-17T14:44:10.714725-03:00
rendered_js: false
word_count: 117
summary: This document outlines the various deployment configurations for FreshRSS available on Coolify, detailing supported database options and their intended use cases.
tags:
    - freshrss
    - coolify
    - self-hosted
    - rss-aggregator
    - deployment-options
    - database-setup
category: guide
---

# Freshrss

## What is Freshrss

A free, self-hostable feed aggregator.

## Deployment Variants

FreshRSS is available in four deployment configurations in Coolify:

### FreshRSS (Default)

* **Database:** SQLite (embedded)
* **Use case:** Simple deployments, testing, or personal RSS feed reading
* **Components:** Single FreshRSS container with built-in SQLite database

### FreshRSS with PostgreSQL

* **Database:** PostgreSQL
* **Use case:** Production deployments requiring better performance and scalability
* **Components:**
  * FreshRSS container
  * PostgreSQL container
  * Automatic database configuration and health checks

### FreshRSS with MySQL

* **Database:** MySQL
* **Use case:** Production deployments with MySQL preference
* **Components:**
  * FreshRSS container
  * MySQL container
  * Automatic database configuration and health checks

### FreshRSS with MariaDB

* **Database:** MariaDB
* **Use case:** Production deployments with MariaDB preference
* **Components:**
  * FreshRSS container
  * MariaDB container
  * Automatic database configuration and health checks

## Links

* [Official Documentation](https://freshrss.org/index.html?utm_source=coolify.io)