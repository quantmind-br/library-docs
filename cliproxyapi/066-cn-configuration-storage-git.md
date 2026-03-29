---
title: Git 支持的配置与令牌存储 | CLIProxyAPI
url: https://help.router-for.me/cn/configuration/storage/git
source: crawler
fetched_at: 2026-01-14T22:10:09.326146992-03:00
rendered_js: false
word_count: 52
summary: This document explains how to configure an application to use a Git repository as a backend for storing configuration files and authentication tokens, enabling centralized management and version control.
tags:
    - git-store
    - configuration
    - authentication
    - environment-variables
    - version-control
category: configuration
---

应用程序可配置为使用 Git 仓库作为后端，用于存储 `config.yaml` 配置文件和来自 `auth-dir` 目录的身份验证令牌。这允许对您的配置进行集中管理和版本控制。

要启用此功能，请将 `GITSTORE_GIT_URL` 环境变量设置为您的 Git 仓库的 URL。

**环境变量**

变量必需默认值描述`MANAGEMENT_PASSWORD`是管理面板密码`GITSTORE_GIT_URL`是要使用的 Git 仓库的 HTTPS URL。`GITSTORE_LOCAL_PATH`否当前工作目录将克隆 Git 仓库的本地路径。在 Docker 内部，此路径默认为 `/CLIProxyAPI`。`GITSTORE_GIT_USERNAME`否用于 Git 身份验证的用户名。`GITSTORE_GIT_TOKEN`否用于 Git 身份验证的个人访问令牌（或密码）。

**工作原理**

1. **克隆：** 启动时，应用程序会将远程 Git 仓库克隆到 `GITSTORE_LOCAL_PATH`。
2. **配置：** 然后，它会在克隆的仓库内的 `config` 目录中查找 `config.yaml` 文件。
3. **引导：** 如果仓库中不存在 `config/config.yaml`，应用程序会将本地的 `config.example.yaml` 复制到该位置，然后提交并推送到远程仓库作为初始配置。您必须确保 `config.example.yaml` 文件可用。
4. **令牌同步：** `auth-dir` 也在此仓库中管理。对身份验证令牌的任何更改（例如，通过新的登录）都会自动提交并推送到远程 Git 仓库。