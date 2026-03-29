---
title: 热更新 | CLIProxyAPI
url: https://help.router-for.me/cn/configuration/hot-reloading
source: crawler
fetched_at: 2026-01-14T22:10:09.953570164-03:00
rendered_js: false
word_count: 21
summary: This document explains how the service automatically reloads client configurations and tokens without requiring a restart. It monitors changes in configuration files and the auth-dir directory for hot updates.
tags:
    - hot-update
    - configuration-reload
    - client-tokens
    - service-restart
    - auth-dir
category: concept
---

## 热更新 [​](#%E7%83%AD%E6%9B%B4%E6%96%B0)

服务会监听配置文件与 `auth-dir` 目录的变化并自动重新加载客户端与配置。

您可以在运行中新增或移除 `Gemini CLI` / `Codex` / `Cluade Code` / `Qwen Code` / `iFlow` 的令牌 JSON 文件，无需重启服务。