---
title: Gemini 兼容供应商 | CLIProxyAPI
url: https://help.router-for.me/cn/configuration/provider/gemini-compatibility
source: crawler
fetched_at: 2026-01-14T22:10:13.59459103-03:00
rendered_js: false
word_count: 30
summary: This document explains how to configure upstream Gemini-compatible providers using the `gemini-api-key` setting, detailing required and optional parameters like api-key, base-url, proxy-url, and headers.
tags:
    - gemini-api-key
    - configuration
    - api-key
    - base-url
    - proxy-url
    - headers
category: configuration
---

通过 `gemini-api-key` 配置上游 Gemini 兼容供应商。

- api-key: 上游供应商的API key
- base-url: 上游供应商的端点覆盖地址
- proxy-url: 代理服务器地址（可选）
- headers: 可选的额外 HTTP 头部，仅在访问覆盖后的 Gemini 端点时发送。

Example:

yaml

```
gemini-api-key:
  - api-key: "AIzaSy...01"
    base-url: "https://generativelanguage.googleapis.com"
    headers:
      X-Custom-Header: "custom-value"
    proxy-url: "socks5://proxy.example.com:1080"
  - api-key: "AIzaSy...02" # 如果是使用官方 Gemini API,无需设置 base-url
```

NOTE

如果您只设置了 `api-key`，则 `base-url` 将自动设置为 `https://generativelanguage.googleapis.com`。  
`base-url` 仅仅在您使用第三方 Gemini 兼容供应商时才需要设置。