---
title: Claude Code 兼容供应商 | CLIProxyAPI
url: https://help.router-for.me/cn/configuration/provider/claude-code-compatibility
source: crawler
fetched_at: 2026-01-14T22:10:13.15610486-03:00
rendered_js: false
word_count: 32
summary: This document explains how to configure upstream Claude Code compatible providers using the `claude-api-key` setting, detailing the parameters for API keys, base URLs, proxy URLs, and model mappings.
tags:
    - claude-api-key
    - configuration
    - api-key
    - base-url
    - proxy-url
    - model-mapping
category: configuration
---

通过 `claude-api-key` 配置上游 Claude Code 兼容供应商。

- api-key: 上游供应商的API key
- base-url: 上游供应商的端点覆盖地址
- proxy-url: 代理服务器地址（可选）
- models: 从上游供应商模型 `名称` 映射到本地 `别名` 的列表

Example:

yaml

```
claude-api-key:
  - api-key: "sk-atSM..." # 如果是使用官方 Claude API,无需设置 base-url
  - api-key: "sk-atSM..."
    base-url: "https://www.example.com" # 使用第三方 Claude API 中转服务端点
    proxy-url: "socks5://proxy.example.com:1080" # 可选：针对该密钥的代理设置
    models:
      - name: "claude-3-5-sonnet-20241022" # 上游模型名称
        alias: "claude-sonnet-latest" # 上游模型的本地别名
```

NOTE

如果您只设置了 `api-key`，则 `base-url` 将自动设置为 `https://api.anthropic.com`。  
`base-url` 仅仅在您使用第三方 Claude Code 兼容供应商时才需要设置。