---
title: Supertokens
url: https://coolify.io/docs/services/supertokens.md
source: llms
fetched_at: 2026-02-17T14:48:28.644687-03:00
rendered_js: false
word_count: 99
summary: This document describes SuperTokens, an open-source authentication solution, and its available deployment configurations using MySQL or PostgreSQL within Coolify.
tags:
    - authentication
    - supertokens
    - coolify
    - mysql
    - postgresql
    - session-management
    - deployment
category: reference
---

# Supertokens

## What is Supertokens

An open-source authentication solution that simplifies the implementation of secure user authentication and session management for web and mobile applications.

## Deployment Variants

SuperTokens is available in two deployment configurations in Coolify:

### SuperTokens with MySQL

* **Database:** MySQL
* **Use case:** Production deployments with MySQL preference
* **Components:**
  * SuperTokens container
  * MySQL container
  * Automatic database configuration and health checks

### SuperTokens with PostgreSQL

* **Database:** PostgreSQL
* **Use case:** Production deployments with PostgreSQL preference
* **Components:**
  * SuperTokens container
  * PostgreSQL container
  * Automatic database configuration and health checks

Both variants provide equivalent functionality - choose based on your database preference or existing infrastructure.

## Links

* [Official Documentation](https://supertokens.com/docs/guides?utm_source=coolify.io)