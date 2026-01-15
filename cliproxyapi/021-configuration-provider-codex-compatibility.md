---
title: Codex Compatibility Providers | CLIProxyAPI
url: https://help.router-for.me/configuration/provider/codex-compatibility
source: crawler
fetched_at: 2026-01-14T22:09:59.944666392-03:00
rendered_js: false
word_count: 29
summary: This document explains how to configure upstream Codex compatible providers by specifying their API key, base URL, and an optional proxy URL.
tags:
    - codex
    - api-key
    - configuration
    - provider
    - base-url
    - proxy-url
category: configuration
---

[Skip to content](#VPContent)

Configure upstream Codex compatible providers via `codex-api-key`.

- api-key: API key for the provider
- base-url: provider base URL
- proxy-url: optional proxy URL for the provider

Example:

yaml

```
codex-api-key:
  - api-key: "sk-atSM..."
    base-url: "https://www.example.com" # use the custom codex API endpoint
    proxy-url: "socks5://proxy.example.com:1080" # optional: per-key proxy override
```