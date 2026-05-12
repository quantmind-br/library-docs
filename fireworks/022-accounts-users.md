---
title: Managing users - Fireworks AI Docs
url: https://docs.fireworks.ai/accounts/users
source: sitemap
fetched_at: 2026-04-27T20:19:20.734741799-03:00
rendered_js: false
word_count: 285
summary: This document outlines the various user roles available within an account, detailing what each role (Admin, User, Contributor, Inference User) can do regarding resource management and API key access. It also provides commands for adding, updating, and deleting users.
tags:
    - user-roles
    - account-management
    - role-permissions
    - fireworks-ai
    - cli-commands
category: guide
optimized: true
optimized_at: 2026-04-27T00:00:00Z
---
Each user is assigned a role determining their access level. See the [[007-getting-started-concepts|concepts page]] for account/user definitions.

## User Roles

| Role | Description |
|------|-------------|
| **Admin** | Full administrative control over resources, users, and access settings |
| **User** (default) | Can manage all resources but cannot manage users or access settings |
| **Contributor** | Can run inference and manage own resources only |
| **Inference User** | Can view resources and run inference only |

## Resource Management Permissions

| Permission | Inference User | Contributor | User | Admin |
|------------|:--------------:|:-----------:|:----:|:-----:|
| Execute inference on any deployment | ✅ | ✅ | ✅ | ✅ |
| View all resources | ✅ | ✅ | ✅ | ✅ |
| Create new resources | ❌ | ✅ | ✅ | ✅ |
| Manage own resources | ❌ | ✅ | ✅ | ✅ |
| Manage others' resources | ❌ | ❌ | ✅ | ✅ |

## API Key & Account Management Permissions

| Permission | Inference User | Contributor | User | Admin |
|------------|:-------------:|:-----------:|:----:|:-----:|
| Manage self-owned API keys | ✅ | ✅ | ✅ | ✅ |
| View all users and service accounts | ✅ | ✅ | ✅ | ✅ |
| Create service account API keys | ❌ | ❌ | ❌ | ✅ |
| Delete others' API keys | ❌ | ❌ | ❌ | ✅ |
| Add/modify/delete users | ❌ | ❌ | ❌ | ✅ |

## Adding Users

```bash
firectl user create --email="alice@example.com"
```

Create an admin:

```bash
firectl user create --email="alice@example.com" --role=admin
```

Manage users via the Fireworks web UI at [app.fireworks.ai/account/users](https://app.fireworks.ai/account/users).

## Updating a User's Role

```bash
firectl user update <USER_ID> --role=<ROLE>
```

Where `<ROLE>` is: `admin`, `user`, `contributor`, or `inference-user`.

## Deleting Users

```bash
firectl user delete <USER_ID>
```
