---
title: Gemini Compatibility Providers | CLIProxyAPI
url: https://help.router-for.me/configuration/provider/gemini-compatibility
source: crawler
fetched_at: 2026-01-14T22:10:01.482194219-03:00
rendered_js: false
word_count: 66
summary: This document explains how to configure upstream Gemini compatible providers using the `gemini-api-key` setting, detailing the required and optional parameters such as api-key, base-url, proxy-url, and headers.
tags:
    - configuration
    - gemini-api-key
    - provider-setup
    - api-key
    - base-url
category: configuration
---

Configure upstream Gemini compatible providers via `gemini-api-key`.

- api-key: API key for the provider
- base-url: provider base URL
- proxy-url: optional proxy URL for the provider
- headers: optional extra HTTP headers sent to the overridden Gemini endpoint only

Example:

yaml

```
gemini-api-key:
  - api-key: "AIzaSy...01"
    base-url: "https://generativelanguage.googleapis.com"
    headers:
      X-Custom-Header: "custom-value"
    proxy-url: "socks5://proxy.example.com:1080"
  - api-key: "AIzaSy...02" # use the official Gemini API key, no need to set the base url
```

NOTE

If you set the `api-key` only, the `base-url` will be set to `https://generativelanguage.googleapis.com` automatically.  
The `base-url` is only needed if you are using a third-party Gemini-compatible provider.