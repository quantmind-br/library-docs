---
title: 快速开始 | CLIProxyAPI
url: https://help.router-for.me/cn/introduction/quick-start
source: crawler
fetched_at: 2026-01-14T22:09:56.31667682-03:00
rendered_js: false
word_count: 35
summary: This document provides instructions on how to install and run the CLIProxyAPI tool on various operating systems including macOS, Linux, Windows, and via Docker, as well as how to compile it from source.
tags:
    - installation
    - macos
    - linux
    - windows
    - docker
    - source-build
    - cli-proxy-api
category: tutorial
---

## 快速开始 [​](#%E5%BF%AB%E9%80%9F%E5%BC%80%E5%A7%8B)

## macOS [​](#macos)

bash

```
brew install cliproxyapi
brew services start cliproxyapi
```

## Linux [​](#linux)

bash

```
curl -fsSL https://raw.githubusercontent.com/brokechubb/cliproxyapi-installer/refs/heads/master/cliproxyapi-installer | bash
```

感谢 [brokechubb](https://github.com/brokechubb) 开发的 Linux 安装器！

## Windows [​](#windows)

你可以在 [这里](https://github.com/router-for-me/CLIProxyAPI/releases) 下载最新版本并直接运行。

或者

你可以在 [这里](https://github.com/router-for-me/EasyCLI/releases) 下载我们的桌面图形程序并直接运行。

## Docker [​](#docker)

bash

```
docker run --rm -p 8317:8317 -v /path/to/your/config.yaml:/CLIProxyAPI/config.yaml -v /path/to/your/auth-dir:/root/.cli-proxy-api eceasy/cli-proxy-api:latest
```

## 源码编译 [​](#%E6%BA%90%E7%A0%81%E7%BC%96%E8%AF%91)

1. 克隆仓库:
   
   bash
   
   ```
   git clone https://github.com/router-for-me/CLIProxyAPI.git
   cd CLIProxyAPI
   ```
2. 构建程序:
   
   Linux, macOS:
   
   bash
   
   ```
   go build -o cli-proxy-api ./cmd/server
   ```
   
   Windows:
   
   bash
   
   ```
   go build -o cli-proxy-api.exe ./cmd/server
   ```