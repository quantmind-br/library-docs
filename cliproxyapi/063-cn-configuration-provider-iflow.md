---
title: 'iFlow (iFlow OAuth 登录): | CLIProxyAPI'
url: https://help.router-for.me/cn/configuration/provider/iflow
source: crawler
fetched_at: 2026-01-14T22:10:12.492598648-03:00
rendered_js: false
word_count: 8
summary: This document explains how to use the `cli-proxy-api` command with the `--iflow-login` option for authentication, including how to prevent the browser from opening automatically and the default callback port.
tags:
    - cli-proxy-api
    - authentication
    - login
    - oauth
    - callback-port
    - bash
category: tutorial
---

[跳转到内容](#VPContent)

bash

```
./cli-proxy-api --iflow-login
```

选项：加上 `--no-browser` 可打印登录地址而不自动打开浏览器。本地 OAuth 回调端口为 `11451`。