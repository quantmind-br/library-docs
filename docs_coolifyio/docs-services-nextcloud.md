---
title: NextCloud
url: https://coolify.io/docs/services/nextcloud.md
source: llms
fetched_at: 2026-02-17T14:46:24.282698-03:00
rendered_js: false
word_count: 169
summary: This document provides an overview of NextCloud and describes the four available deployment configurations on Coolify, categorized by their supported database backends.
tags:
    - nextcloud
    - coolify
    - self-hosting
    - cloud-storage
    - deployment-options
    - database-configuration
category: reference
---

![NextCloud](https://nextcloud.com/c/uploads/2022/11/logo_nextcloud_white.svg)

## What is NextCloud?

NextCloud is an open-source productivity platform that provides a secure and private alternative to popular cloud storage services like Google Drive and Dropbox. It allows you to store, sync, and share files, photos, and videos across multiple devices, and offers features like file versioning, password-protected sharing, and collaboration tools.

## Deployment Variants

Nextcloud is available in four deployment configurations in Coolify:

### Nextcloud (Default)

* **Database:** SQLite (embedded)
* **Use case:** Simple deployments, testing, or personal file storage
* **Components:** Single Nextcloud container with built-in SQLite database

### Nextcloud with PostgreSQL

* **Database:** PostgreSQL
* **Use case:** Production deployments requiring better performance and scalability
* **Components:**
  * Nextcloud container
  * PostgreSQL container
  * Automatic database configuration and health checks

### Nextcloud with MySQL

* **Database:** MySQL
* **Use case:** Production deployments with MySQL preference
* **Components:**
  * Nextcloud container
  * MySQL container
  * Automatic database configuration and health checks

### Nextcloud with MariaDB

* **Database:** MariaDB
* **Use case:** Production deployments with MariaDB preference (recommended for most users)
* **Components:**
  * Nextcloud container
  * MariaDB container
  * Automatic database configuration and health checks

## Screenshots

![NextCloud preview](https://raw.githubusercontent.com/nextcloud/screenshots/master/nextcloud-hub-files-25-preview.png)

## Links

* [The official website](https://nextcloud.com/)
* [GitHub](https://github.com/nextcloud/server)