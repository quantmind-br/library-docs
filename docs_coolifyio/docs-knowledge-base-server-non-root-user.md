---
title: Non-root user
url: https://coolify.io/docs/knowledge-base/server/non-root-user.md
source: llms
fetched_at: 2026-02-17T14:40:56.998975-03:00
rendered_js: false
word_count: 130
summary: This document provides instructions for configuring a non-root user with passwordless sudo permissions to manage server resources.
tags:
    - server-management
    - non-root-user
    - sudo-permissions
    - linux-administration
    - ssh-keys
category: guide
---

# Non-root user

You could have a server with a non-root user that will manage your resources instead of the root user.

For this to work, you need to set up the server correctly.

::: danger Caution
**This is an experimental feature.**
:::

## Requirements

* The non-root user needs to have the SSH key added to the server.
* Sudos permissions for the non-root user.

## Sudo permissions

You need to add the following lines to the `/etc/sudoers` file:

```bash
# Allow the your-non-root-user to run commands as root without a password
your-non-root-user ALL=(ALL) NOPASSWD: ALL
```

This will allow the non-root user to any command as root without a password.
Note: you need to replace "your-non-root-user" with your user.

::: warning Caution
This is not the most secure way to set up a non-root user, but we will improve
this in the future, by adding more granular permissions on binaries.
:::