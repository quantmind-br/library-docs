---
title: ClassicPress
url: https://coolify.io/docs/services/classicpress.md
source: llms
fetched_at: 2026-02-17T14:42:58.665926-03:00
rendered_js: false
word_count: 143
summary: This document provides an overview of ClassicPress, a community-led CMS fork of WordPress, and details its available deployment configurations with MariaDB or MySQL.
tags:
    - classicpress
    - cms
    - deployment-options
    - mariadb
    - mysql
    - coolify
category: reference
---

![ClassicPress](https://raw.githubusercontent.com/ClassicPress/ClassicPress/develop/src/wp-admin/images/classicpress-logo.png)

## What is ClassicPress?

ClassicPress is a community-led open source content management system for creators. It is a fork of WordPress 6.2 that preserves the TinyMCE classic editor as the default option. It is half the size of WordPress, contains less bloat improving performance, and has no block editor (Gutenberg/Full Site Editing).

## Deployment Variants

ClassicPress is available in two deployment configurations in Coolify:

### ClassicPress with MariaDB

* **Database:** MariaDB
* **Use case:** Production deployments with MariaDB preference (recommended for most users)
* **Components:**
  * ClassicPress container
  * MariaDB container
  * Automatic database configuration and health checks

### ClassicPress with MySQL

* **Database:** MySQL
* **Use case:** Production deployments with MySQL preference
* **Components:**
  * ClassicPress container
  * MySQL container
  * Automatic database configuration and health checks

Both variants provide equivalent functionality - choose based on your database preference or existing infrastructure.

For more information, see:

* [The official website](https://www.classicpress.net?utm_source=coolify.io)
* [The ClassicPress documentation](https://docs.classicpress.net?utm_source=coolify.io)
* [The ClassicPress governance](https://www.classicpress.net/governance?utm_source=coolify.io)
* [Suggest features](https://github.com/ClassicPress/ClassicPress/issues?utm_source=coolify.io)