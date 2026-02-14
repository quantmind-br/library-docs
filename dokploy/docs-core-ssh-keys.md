---
title: SSH Keys | Dokploy
url: https://docs.dokploy.com/docs/core/ssh-keys
source: crawler
fetched_at: 2026-02-14T14:18:06.41813-03:00
rendered_js: true
word_count: 184
summary: This document explains how to configure and manage SSH keys in Dokploy for accessing private repositories and remote servers.
tags:
    - ssh-keys
    - dokploy
    - private-repositories
    - server-access
    - security
    - git
category: configuration
---

Configure your SSH keys to access your servers or clone Private Repositories.

Dokploy provides a section exclusively for SSH keys, allowing you to manage your SSH keys in a centralized location.

SSH Keys can be used for two purposes:

- **Private Repositories**: You can use SSH Keys, to access to private repositories, this is only for `Git` provider in your application or docker compose.
- **Multi Server**: You can use SSH Keys, to access remotely to your servers via SSH.

To create a SSH Key, is a very easy process, just click on `Create SSH Key`

We offer two SSH Keys Generation types:

1. **RSA Key**: This is the most commonly used key type, and generates a 2048-bit RSA key.
2. **Ed25519 Key**: This is a newer key type that generates a 256-bit Ed25519 key.

You can also create or paste your own SSH Key, you can edit the `Private Key` and `Public Key` fields without restrictions, make sure to use the correct format for the key type you are using.

Once you create a SSH Key you will not be able to read the `Private Key` anymore.