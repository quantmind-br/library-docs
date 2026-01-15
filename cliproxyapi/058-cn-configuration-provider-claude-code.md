---
title: 'Claude Code (Anthropic OAuth 登录):'
url: https://help.router-for.me/cn/configuration/provider/claude-code
source: crawler
fetched_at: 2026-01-14T22:10:10.6053241-03:00
rendered_js: false
word_count: 8
summary: This document explains how to use the `cli-proxy-api` command with the `--claude-login` option for authentication, and provides a flag to disable automatic browser opening.
tags:
    - cli-proxy-api
    - claude-login
    - authentication
    - oauth
    - command-line
category: reference
---

[跳转到内容](#VPContent)

bash

```
./cli-proxy-api --claude-login
```

选项：加上 `--no-browser` 可打印登录地址而不自动打开浏览器。本地 OAuth 回调端口为 `54545`。