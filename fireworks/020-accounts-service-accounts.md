---
title: Service Accounts - Fireworks AI Docs
url: https://docs.fireworks.ai/accounts/service-accounts
source: sitemap
fetched_at: 2026-04-27T20:19:25.466384655-03:00
rendered_js: false
word_count: 142
summary: This document explains the concept of service accounts within Fireworks, detailing how they enable secure authentication for automated systems and outlining commands to create, manage, list, and assign roles to these accounts.
tags:
    - service-accounts
    - authentication
    - api-keys
    - fireworks-ai
    - user-management
    - audit-logs
category: guide
optimized: true
optimized_at: 2026-04-27T00:00:00Z
---
Service accounts enable applications, scripts, and automated systems to authenticate without human credentials. They are ideal for CI/CD pipelines, backend services, and automated workflows—avoiding shared credentials and providing clear audit trails. Service accounts can perform actions via API key (create deployments, run models, create datasets), but cannot log in via web UI or use OIDC tokens.

## Creating a Service Account

```bash
firectl user create --user-id "my-service-account" --service-account
```

## Creating an API Key for a Service Account

```bash
firectl api-key create --service-account "my-service-account"
```

## Roles

Assign a role at creation with the `--role` flag:

```bash
firectl user create --user-id "my-service-account" --service-account --role=contributor
```

Default role is `user`. To change an existing service account's role:

```bash
firectl user update my-service-account --role=inference-user
```

See [[022-accounts-users|Managing users]] for available roles.

## Listing Service Accounts

```bash
firectl user list --filter 'service_account=true'
```

## Billing

- Service accounts count toward the same account quotas and limits
- Usage is tracked by account, not individual users

## Auditing

- Users are referenced by email in audit logs
- Service accounts are referenced by `<user-id>@<account>.sa.fireworks.ai`
