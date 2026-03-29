---
title: 陆：新人最爱GUI | CLIProxyAPI
url: https://help.router-for.me/cn/hands-on/tutorial-6
source: crawler
fetched_at: 2026-01-14T22:10:18.26750625-03:00
rendered_js: false
word_count: 63
summary: This document explains how to enable and access the WebUI for CLIProxyAPI, which simplifies configuration and management. It details the necessary configuration changes and how to access the interface via a web browser.
tags:
    - cli-proxy-api
    - webui
    - configuration
    - remote-management
    - access
category: guide
---

在之前的文章中，我们已经介绍了如何通过命令行逐步运行 CLIProxyAPI。其实 CLIProxyAPI 还有配套的两个项目：EasyCLI 和 WebUI。

- **EasyCLI 仓库地址**：`https://github.com/router-for-me/EasyCLI`
- **WebUI 仓库地址**：`https://github.com/router-for-me/Cli-Proxy-API-Management-Center`

这两个项目旨在降低普通用户的使用门槛。EasyCLI 是桌面客户端，而 WebUI 是 Web 管理界面，它们都通过连接 CLIProxyAPI 来工作。

我此前未提供 GUI 教程，是因为旧版本需要用户自行部署或安装，操作相对繁琐。从 `6.0.19` 版本开始，作者已将 WebUI 集成到主程序中。因此，用户现在可以直接通过内置的 Web 界面进行配置。

本文将简要介绍如何启用并访问 WebUI。关于 EasyCLI 的使用方法，将在后续关于容器云部署的文章中详细介绍。

#### 一、启用 WebUI [​](#%E4%B8%80%E3%80%81%E5%90%AF%E7%94%A8-webui)

首先，我们需要在原有的基础配置上进行调整，添加远程管理部分。完整的示例配置如下：

yaml

```
port: 8317
auth-dir: "~/.cli-proxy-api"
request-retry: 3
quota-exceeded:
  switch-project: true
  switch-preview-model: true
api-keys:
- "ABC-123456"

# 本次添加的远程管理部分
remote-management:
  allow-remote: true
  # 用于远程管理的KEY，和上边的api-keys要区分开
  secret-key: "MGT-123456"
  disable-control-panel: false
```

**请注意**：修改配置后，需要重启程序才能生效（新版本支持自动热重载）。

#### 二、访问 WebUI [​](#%E4%BA%8C%E3%80%81%E8%AE%BF%E9%97%AE-webui)

程序成功启动后，在浏览器中访问 `http://YOUR_SERVER_IP:8317/management.html` ，在管理密钥中输入之前设置的密码 `MGT-123456` 即可打开 WebUI 界面。

![](https://img.072899.xyz/2025/10/37b12b67193ec67774e2f657e38eefc9.png)

#### 三、重要注意事项 [​](#%E4%B8%89%E3%80%81%E9%87%8D%E8%A6%81%E6%B3%A8%E6%84%8F%E4%BA%8B%E9%A1%B9)

WebUI 的界面设计直观，你可以自行探索各项功能。但需要特别注意的是，WebUI 中的 OAuth 认证功能仅支持本地运行（例如 `localhost` 或 `127.0.0.1`）的 CLIProxyAPI 实例。对于部署在远程服务器上的实例，由于 OAuth 服务商的安全策略限制，将无法通过 WebUI 直接完成认证。