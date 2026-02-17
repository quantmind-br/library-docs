---
title: Commands
url: https://coolify.io/docs/knowledge-base/commands.md
source: llms
fetched_at: 2026-02-17T14:40:10.795707-03:00
rendered_js: false
word_count: 90
summary: This document provides administrative CLI commands for managing a Coolify instance, including resetting root passwords, updating root email addresses, and deleting stuck services.
tags:
    - coolify
    - cli-commands
    - root-password-reset
    - artisan-commands
    - server-management
category: reference
---

# Commands

## Root password reset without SMTP

You can use the following method to reset the root user's password, in case you forgot and do not have an SMTP server set, so you cannot request a forgot password.

Login to your server through SSH and execute the following command:

```bash
docker exec -ti coolify sh -c "php artisan root:reset-password"
```

## Root email change

You can change root user's email.

Login to your server through SSH and execute the following command:

```bash
docker exec -ti coolify sh -c "php artisan root:change-email"
```

## Delete a stuck service

You can easily delete a stuck service.

Login to your server through SSH and execute the following command:

```bash
docker exec -ti coolify sh -c "php artisan services:delete"
```