---
title: OpenAI Compatibility Providers | CLIProxyAPI
url: https://help.router-for.me/configuration/provider/openai-compatibility
source: crawler
fetched_at: 2026-01-14T22:09:59.766634088-03:00
rendered_js: false
word_count: 89
summary: This document explains how to configure upstream OpenAI-compatible providers, such as OpenRouter, using the `openai-compatibility` setting. It details the required fields like name, base-url, API key entries, and model mappings, including an example with per-key proxy configuration.
tags:
    - openai-compatibility
    - provider-configuration
    - api-keys
    - model-mapping
    - proxy-configuration
category: configuration
---

Configure upstream OpenAI-compatible providers (e.g., OpenRouter) via `openai-compatibility`.

- name: provider identifier used internally
- base-url: provider base URL
- api-key-entries: list of API key entries with optional per-key proxy configuration (recommended and persisted)
- models: list of mappings from upstream model `name` to local `alias`

> Compatibility: legacy `api-keys` are migrated into `api-key-entries` on load and removed when the config is saved; use `api-key-entries` going forward.

Example with per-key proxy support:

yaml

```
openai-compatibility:
  - name: "openrouter"
    base-url: "https://openrouter.ai/api/v1"
    api-key-entries:
      - api-key: "sk-or-v1-...b780"
        proxy-url: "socks5://proxy.example.com:1080"
      - api-key: "sk-or-v1-...b781"
    models:
      - name: "moonshotai/kimi-k2:free"
        alias: "kimi-k2"
```

Usage:

Call OpenAI's endpoint `/v1/chat/completions` with `model` set to the alias (e.g., `kimi-k2`). The proxy routes to the configured provider/model automatically.