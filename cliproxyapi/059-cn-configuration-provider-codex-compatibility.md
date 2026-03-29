---
title: Codex 兼容供应商 | CLIProxyAPI
url: https://help.router-for.me/cn/configuration/provider/codex-compatibility
source: crawler
fetched_at: 2026-01-14T22:10:12.069688845-03:00
rendered_js: false
word_count: 15
summary: This document explains how to configure an upstream Codex-compatible provider using the `codex-api-key` setting, including the API key, base URL, and an optional proxy URL.
tags:
    - codex
    - api-key
    - configuration
    - provider
    - upstream
    - proxy
category: configuration
---

[跳转到内容](#VPContent)

通过 `codex-api-key` 配置上游 Codex 兼容供应商。

- api-key: 上游供应商的API key
- base-url: 上游供应商的端点覆盖地址
- proxy-url: 代理服务器地址（可选）

Example:

yaml

```
codex-api-key:
  - api-key: "sk-atSM..."
    base-url: "https://www.example.com" # 使用第三方 Codex API 中转服务端点
    proxy-url: "socks5://proxy.example.com:1080" # 可选：针对该密钥的代理设置
```