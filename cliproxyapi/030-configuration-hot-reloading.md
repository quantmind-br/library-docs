---
title: Hot Reloading | CLIProxyAPI
url: https://help.router-for.me/configuration/hot-reloading
source: crawler
fetched_at: 2026-01-14T22:09:57.947262945-03:00
rendered_js: false
word_count: 46
summary: This document explains how the server automatically reloads client configurations and settings when changes are detected in the config file or auth directory, allowing for dynamic updates without a server restart.
tags:
    - server-configuration
    - automatic-reload
    - client-settings
    - token-management
    - dynamic-updates
category: configuration
---

The server watches the config file and the `auth-dir` for changes and reloads clients and settings automatically.

You can add or remove `Gemini CLI` / `Codex` / `Cluade Code` / `Qwen Code` / `iFlow` token JSON files while the server is running; no restart is required.