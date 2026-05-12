---
title: Authentication - Fireworks AI Docs
url: https://docs.fireworks.ai/tools-sdks/firectl/commands/authentication
source: sitemap
fetched_at: 2026-04-27T20:18:06.899656993-03:00
rendered_js: false
word_count: 47
summary: This document explains the different methods users can employ to sign into a system and authenticate operations using an API key. It details how to specify custom SSO accounts and persist keys for ongoing command usage.
tags:
    - google-sso
    - api-key
    - authentication
    - signin
    - firectl
    - account-id
category: guide
optimized: true
optimized_at: 2026-04-27T00:00:00Z
---
## Signing in

Users using Google SSO can run:

If you are using [[021-accounts-sso|custom SSO]], also specify the account ID:

```bash
firectl signin my-enterprise-account
```

## Authenticate with API Key

To authenticate with an API key, append `--api-key` to any firectl command:

```bash
firectl --api-key API_KEY <command>
```

To persist the API key for all subsequent commands, run:

```bash
firectl set-api-key API_KEY
```
