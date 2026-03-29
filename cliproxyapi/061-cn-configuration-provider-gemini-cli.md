---
title: 'Gemini CLI (Gemini OAuth 登录):'
url: https://help.router-for.me/cn/configuration/provider/gemini-cli
source: crawler
fetched_at: 2026-01-14T22:10:10.586907822-03:00
rendered_js: false
word_count: 16
summary: This document explains how to log in to the Gemini Code CLI using the `--login` command, with an option to specify a project ID and disable automatic browser opening.
tags:
    - cli
    - login
    - authentication
    - project-id
    - oauth
category: tutorial
---

bash

```
./cli-proxy-api --login
```

如果您是现有的 `Gemini Code` 用户，可能需要指定一个项目ID：

bash

```
./cli-proxy-api --login --project_id <your_project_id>
```

本地 OAuth 回调端口为 `8085`。

选项：加上 `--no-browser` 可打印登录地址而不自动打开浏览器。本地 OAuth 回调端口为 `8085`。