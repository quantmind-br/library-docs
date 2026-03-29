---
title: OpenAI 兼容供应商 | CLIProxyAPI
url: https://help.router-for.me/cn/configuration/provider/openai-compatibility
source: crawler
fetched_at: 2026-01-14T22:10:12.267769569-03:00
rendered_js: false
word_count: 29
summary: This document explains how to configure an upstream OpenAI-compatible provider using the `openai-compatibility` setting, including details on specifying provider names, base URLs, API keys with optional proxy configurations, and model mappings.
tags:
    - openai-compatibility
    - upstream-provider
    - configuration
    - api-key
    - proxy-settings
    - model-mapping
category: configuration
---

### OpenAI 兼容上游提供商 [​](#openai-%E5%85%BC%E5%AE%B9%E4%B8%8A%E6%B8%B8%E6%8F%90%E4%BE%9B%E5%95%86)

通过 `openai-compatibility` 配置上游 OpenAI 兼容提供商（例如 OpenRouter）。

- name：内部识别名
- base-url：提供商基础地址
- api-key-entries：API密钥条目列表，支持可选的每密钥代理配置（推荐且为持久化格式）
- models：将上游模型 `name` 映射为本地可用 `alias`

> 兼容说明：旧字段 `api-keys` 会在加载时自动迁移为 `api-key-entries`，保存配置时会被移除；请直接使用 `api-key-entries`。

支持每密钥代理配置的示例：

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

使用方式：在 `/v1/chat/completions` 中将 `model` 设为别名（如 `kimi-k2`），代理将自动路由到对应提供商与模型。