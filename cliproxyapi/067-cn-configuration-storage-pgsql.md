---
title: PostgreSQL 支持的配置与令牌存储 | CLIProxyAPI
url: https://help.router-for.me/cn/configuration/storage/pgsql
source: crawler
fetched_at: 2026-01-14T22:10:09.628572069-03:00
rendered_js: false
word_count: 40
summary: This document explains how to use PostgreSQL to store configuration and tokens in a hosted environment, detailing environment variables, the underlying mechanism, and the initialization and synchronization processes.
tags:
    - postgresql
    - configuration-storage
    - token-storage
    - hosted-environment
    - environment-variables
    - data-synchronization
category: configuration
---

在托管环境中运行服务时，可以选择使用 PostgreSQL 来保存配置与令牌，借助托管数据库减轻本地文件管理压力。

**环境变量**

变量必需默认值描述`MANAGEMENT_PASSWORD`是管理面板密码（启用远程管理时必需）。`PGSTORE_DSN`是PostgreSQL 连接串，例如 `postgresql://user:pass@host:5432/db`。`PGSTORE_SCHEMA`否public创建表时使用的 schema；留空则使用默认 schema。`PGSTORE_LOCAL_PATH`否当前工作目录本地镜像根目录，服务将在 `<值>/pgstore` 下写入缓存；若无法获取工作目录则退回 `/tmp/pgstore`。

**工作原理**

1. **初始化：** 启动时通过 `PGSTORE_DSN` 连接数据库，确保 schema 存在，并在缺失时创建 `config_store` 与 `auth_store`。
2. **本地镜像：** 在 `<PGSTORE_LOCAL_PATH 或当前工作目录>/pgstore` 下建立可写缓存，复用 `config/config.yaml` 与 `auths/` 目录。
3. **引导：** 若数据库中无配置记录，会使用 `config.example.yaml` 初始化，并以固定标识 `config` 写入。
4. **令牌同步：** 配置与令牌的更改会写入 PostgreSQL，同时数据库中的内容也会反向同步至本地镜像，便于文件监听与管理接口继续工作。