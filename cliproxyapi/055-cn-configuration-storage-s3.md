---
title: 对象存储驱动的配置与令牌存储 | CLIProxyAPI
url: https://help.router-for.me/cn/configuration/storage/s3
source: crawler
fetched_at: 2026-01-14T22:10:09.566654234-03:00
rendered_js: false
word_count: 53
summary: This document explains how to configure object storage, specifically S3-compatible storage, for hosting configuration and authentication data. It details the necessary environment variables and outlines the workflow for initialization, local mirroring, and bidirectional synchronization between local storage and the object store.
tags:
    - object-storage
    - s3-compatible
    - configuration
    - authentication
    - environment-variables
    - workflow
category: configuration
---

## 对象存储驱动的配置与令牌存储 [​](#%E5%AF%B9%E8%B1%A1%E5%AD%98%E5%82%A8%E9%A9%B1%E5%8A%A8%E7%9A%84%E9%85%8D%E7%BD%AE%E4%B8%8E%E4%BB%A4%E7%89%8C%E5%AD%98%E5%82%A8)

可以选择使用 S3 兼容的对象存储来托管配置与鉴权数据。

**环境变量**

变量是否必填默认值说明`MANAGEMENT_PASSWORD`是管理面板密码（启用远程管理时必需）。`OBJECTSTORE_ENDPOINT`是对象存储访问端点。可带 `http://` 或 `https://` 前缀指定协议（省略则默认 HTTPS）。`OBJECTSTORE_BUCKET`是用于存放 `config/config.yaml` 与 `auths/*.json` 的 Bucket 名称。`OBJECTSTORE_ACCESS_KEY`是对象存储账号的访问密钥 ID。`OBJECTSTORE_SECRET_KEY`是对象存储账号的访问密钥 Secret。`OBJECTSTORE_LOCAL_PATH`否当前工作目录 (CWD)本地镜像根目录；服务会写入到 `<值>/objectstore`。

**工作流程**

1. **启动阶段：** 解析端点地址（识别协议前缀），创建 MinIO 兼容客户端并使用 Path-Style 模式，如 Bucket 不存在会自动创建。
2. **本地镜像：** 在 `<OBJECTSTORE_LOCAL_PATH 或当前工作目录>/objectstore` 维护可写缓存，同步 `config/config.yaml` 与 `auths/`。
3. **初始化：** 若 Bucket 中缺少配置文件，将以 `config.example.yaml` 为模板生成 `config/config.yaml` 并上传。
4. **双向同步：** 本地变更会上传到对象存储，同时远端对象也会拉回到本地，保证文件监听、管理 API 与 CLI 命令行为一致。