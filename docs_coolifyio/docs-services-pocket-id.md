---
title: Pocket ID
url: https://coolify.io/docs/services/pocket-id.md
source: llms
fetched_at: 2026-02-17T14:47:18.344953-03:00
rendered_js: false
word_count: 232
summary: Pocket ID is a self-hosted OIDC provider that enables passwordless authentication using passkeys for secure access to various services. This document outlines its primary features, deployment configurations, and initial setup process.
tags:
    - pocket-id
    - oidc-provider
    - passkeys
    - passwordless-authentication
    - self-hosted
    - authentication
    - coolify
category: reference
---

# Pocket ID

## What is Pocket ID?

Pocket ID is a simple OIDC provider for passwordless authentication using [passkeys](https://www.passkeys.io/). It's designed to be straightforward and easy-to-use. It exclusively supports passkey authentication, allowing you to use hardware security keys like Yubikey for secure sign-ins across your self-hosted services.

## Deployment Variants

Pocket ID is available in two deployment configurations in Coolify:

### Pocket ID (Default)

* **Database:** SQLite (embedded)
* **Use case:** Simple deployments, testing, or personal authentication server
* **Components:** Single Pocket ID container with built-in SQLite database

### Pocket ID with PostgreSQL

* **Database:** PostgreSQL
* **Use case:** Production deployments requiring better performance and data reliability
* **Components:**
  * Pocket ID container
  * PostgreSQL container
  * Automatic database configuration and health checks

## Features

* **Passwordless Authentication**: Uses passkeys instead of passwords for better security
* **OIDC Provider**: Integrates with applications that support OpenID Connect
* **Simple Setup**: Easy to install and configure compared to complex alternatives
* **Wide Compatibility**: Works with [various services](https://pocket-id.org/docs/client-examples?utm_source=coolify.io) like Nextcloud, GitLab, and more
* **Passkey Support**: Full support for hardware security keys like Yubikey
* **Self-Hosted**: Maintain complete control over your authentication infrastructure

## Getting Started

Once deployed, you can sign in with the admin account at:

```
https://<your-app-url>/setup
```

Follow the Pocket ID setup wizard to configure your instance and create your first passkey.

## Demo

To see Pocket ID in action, visit the [live demo](https://demo.pocket-id.org/).

:::info
This demo is not affiliated with Coolify.
:::

## Links

* [Official Website](https://pocket-id.org?utm_source=coolify.io)
* [Documentation](https://pocket-id.org/docs/introduction?utm_source=coolify.io)
* [Installation Guide](https://pocket-id.org/docs/setup/installation?utm_source=coolify.io)
* [GitHub](https://github.com/pocket-id/pocket-id?utm_source=coolify.io)

## Additional Resources

* [Proxy Services Guide](https://pocket-id.org/docs/guides/proxy-services?utm_source=coolify.io)
* [Client Examples](https://pocket-id.org/docs/client-examples?utm_source=coolify.io)