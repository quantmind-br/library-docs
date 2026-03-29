---
title: 管理 API | CLIProxyAPI
url: https://help.router-for.me/cn/management/api
source: crawler
fetched_at: 2026-01-14T22:10:14.523924232-03:00
rendered_js: false
word_count: 2
summary: This document provides a JSON configuration example for setting up various API keys, proxy URLs, and model exclusions for services like Gemini, Claude, Codex, and OpenAI compatibility.
tags:
    - api-keys
    - configuration
    - json
    - proxy
    - models
    - gemini
    - claude
    - openai
category: configuration
---

响应:

json

```
{"debug":true,"proxy-url":"","api-keys":["1...5","JS...W"],"ampcode":{"upstream-url":"https://ampcode.com","restrict-management-to-localhost":true},"quota-exceeded":{"switch-project":true,"switch-preview-model":true},"gemini-api-key":[{"api-key":"AI...01","base-url":"https://generativelanguage.googleapis.com","headers":{"X-Custom-Header":"custom-value"},"proxy-url":"","excluded-models":["gemini-1.5-pro","gemini-1.5-flash"]},{"api-key":"AI...02","proxy-url":"socks5://proxy.example.com:1080","excluded-models":["gemini-pro-vision"]}],"request-log":true,"request-retry":3,"claude-api-key":[{"api-key":"cr...56","base-url":"https://example.com/api","proxy-url":"socks5://proxy.example.com:1080","models":[{"name":"claude-3-5-sonnet-20241022","alias":"claude-sonnet-latest"}],"excluded-models":["claude-3-opus"]},{"api-key":"cr...e3","base-url":"http://example.com:3000/api","proxy-url":""},{"api-key":"sk-...q2","base-url":"https://example.com","proxy-url":""}],"codex-api-key":[{"api-key":"sk...01","base-url":"https://example/v1","proxy-url":"","excluded-models":["gpt-4o-mini"]}],"openai-compatibility":[{"name":"openrouter","base-url":"https://openrouter.ai/api/v1","api-key-entries":[{"api-key":"sk...01","proxy-url":""}],"models":[{"name":"moonshotai/kimi-k2:free","alias":"kimi-k2"}]},{"name":"iflow","base-url":"https://apis.iflow.cn/v1","api-key-entries":[{"api-key":"sk...7e","proxy-url":"socks5://proxy.example.com:1080"}],"models":[{"name":"deepseek-v3.1","alias":"deepseek-v3.1"},{"name":"glm-4.5","alias":"glm-4.5"},{"name":"kimi-k2","alias":"kimi-k2"}]}]}
```