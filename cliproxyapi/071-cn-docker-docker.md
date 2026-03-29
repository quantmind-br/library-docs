---
title: 使用 Docker 运行 | CLIProxyAPI
url: https://help.router-for.me/cn/docker/docker
source: crawler
fetched_at: 2026-01-14T22:10:15.177233775-03:00
rendered_js: false
word_count: 29
summary: This document provides Docker commands to run a CLI proxy API, including instructions for logging in with various OAuth providers (Gemini, OpenAI, Claude, Qwen, iFlow, Antigravity) and starting the server.
tags:
    - docker
    - cli-proxy-api
    - oauth
    - gemini
    - openai
    - claude
    - qwen
    - iflow
    - antigravity
    - server
category: tutorial
---

## 使用 Docker 运行 [​](#%E4%BD%BF%E7%94%A8-docker-%E8%BF%90%E8%A1%8C)

运行以下命令进行登录（Gemini OAuth，端口 8085）：

bash

```
docker run --rm -p 8085:8085 -v /path/to/your/config.yaml:/CLIProxyAPI/config.yaml -v /path/to/your/auth-dir:/root/.cli-proxy-api eceasy/cli-proxy-api:latest /CLIProxyAPI/CLIProxyAPI --login
```

运行以下命令进行登录（OpenAI OAuth，端口 1455）：

bash

```
docker run --rm -p 1455:1455 -v /path/to/your/config.yaml:/CLIProxyAPI/config.yaml -v /path/to/your/auth-dir:/root/.cli-proxy-api eceasy/cli-proxy-api:latest /CLIProxyAPI/CLIProxyAPI --codex-login
```

运行以下命令进行登录（Claude OAuth，端口 54545）：

bash

```
docker run --rm -p 54545:54545 -v /path/to/your/config.yaml:/CLIProxyAPI/config.yaml -v /path/to/your/auth-dir:/root/.cli-proxy-api eceasy/cli-proxy-api:latest /CLIProxyAPI/CLIProxyAPI --claude-login
```

运行以下命令进行登录（Qwen OAuth）：

bash

```
docker run -it -rm -v /path/to/your/config.yaml:/CLIProxyAPI/config.yaml -v /path/to/your/auth-dir:/root/.cli-proxy-api eceasy/cli-proxy-api:latest /CLIProxyAPI/CLIProxyAPI --qwen-login
```

运行以下命令进行登录（iFlow OAuth，端口 11451）：

bash

```
docker run --rm -p 11451:11451 -v /path/to/your/config.yaml:/CLIProxyAPI/config.yaml -v /path/to/your/auth-dir:/root/.cli-proxy-api eceasy/cli-proxy-api:latest /CLIProxyAPI/CLIProxyAPI --iflow-login
```

运行以下命令进行登录（Antigravity OAuth，端口 51121）：

bash

```
docker run --rm -p 51121:51121 -v /path/to/your/config.yaml:/CLIProxyAPI/config.yaml -v /path/to/your/auth-dir:/root/.cli-proxy-api eceasy/cli-proxy-api:latest /CLIProxyAPI/CLIProxyAPI --antigravity-login
```

运行以下命令启动服务器：

bash

```
docker run --rm -p 8317:8317 -v /path/to/your/config.yaml:/CLIProxyAPI/config.yaml -v /path/to/your/auth-dir:/root/.cli-proxy-api eceasy/cli-proxy-api:latest
```