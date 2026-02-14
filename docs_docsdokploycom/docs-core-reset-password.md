---
title: Reset Password & 2FA | Dokploy
url: https://docs.dokploy.com/docs/core/reset-password
source: crawler
fetched_at: 2026-02-14T14:12:36.493945-03:00
rendered_js: true
word_count: 118
summary: This document provides step-by-step instructions for resetting a Dokploy account password and disabling two-factor authentication through the command-line interface of the Docker container.
tags:
    - dokploy
    - password-reset
    - 2fa-disabling
    - docker-exec
    - account-recovery
    - security-management
category: guide
---

Reset your password to access your Dokploy account and disable 2FA.

To reset your password, follow these steps:

Log in to your VPS.

Run the command below to get the container ID of the dokploy container.

```
docker ps
```

Run command below to open a shell in the dokploy container.

```
 docker exec -it <container-id> bash -c "pnpm run reset-password"
```

It will display a random password. Copy it and use it to access again to the dashboard.

To disable 2FA, follow these steps:

To reset your 2FA, follow these steps:

Log in to your VPS.

Run the command below to get the container ID of the dokploy container.

```
docker ps
```

Run command below to open a shell in the dokploy container.

```
 docker exec -it <container-id> bash -c "pnpm run reset-2fa"
```

You can now login again without having to supply a 2FA code.