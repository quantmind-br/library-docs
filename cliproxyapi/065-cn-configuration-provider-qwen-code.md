---
title: 'Qwen (Qwen Chat OAuth 登录):'
url: https://help.router-for.me/cn/configuration/provider/qwen-code
source: crawler
fetched_at: 2026-01-14T22:10:11.692951909-03:00
rendered_js: false
word_count: 10
summary: This document explains how to use the Qwen Chat OAuth device login flow via the CLI proxy API, including an option to prevent automatic browser opening.
tags:
    - cli-proxy-api
    - qwen-chat
    - oauth
    - device-login
    - bash
category: tutorial
---

[跳转到内容](#VPContent)

bash

```
./cli-proxy-api --qwen-login
```

选项：加上 `--no-browser` 可打印登录地址而不自动打开浏览器。使用 Qwen Chat 的 OAuth 设备登录流程。