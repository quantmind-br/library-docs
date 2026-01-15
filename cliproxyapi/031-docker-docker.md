---
title: Run with Docker | CLIProxyAPI
url: https://help.router-for.me/docker/docker
source: crawler
fetched_at: 2026-01-14T22:10:04.154441273-03:00
rendered_js: false
word_count: 82
summary: This document provides Docker commands to run the CLIProxyAPI, including instructions for logging in with various OAuth providers and starting the server.
tags:
    - docker
    - cli-proxy-api
    - oauth
    - login
    - server-start
category: tutorial
---

## Run with Docker [​](#run-with-docker)

Run the following command to login (Gemini OAuth on port 8085):

bash

```
docker run --rm -p 8085:8085 -v /path/to/your/config.yaml:/CLIProxyAPI/config.yaml -v /path/to/your/auth-dir:/root/.cli-proxy-api eceasy/cli-proxy-api:latest /CLIProxyAPI/CLIProxyAPI --login
```

Run the following command to login (OpenAI OAuth on port 1455):

bash

```
docker run --rm -p 1455:1455 -v /path/to/your/config.yaml:/CLIProxyAPI/config.yaml -v /path/to/your/auth-dir:/root/.cli-proxy-api eceasy/cli-proxy-api:latest /CLIProxyAPI/CLIProxyAPI --codex-login
```

Run the following command to logi (Claude OAuth on port 54545):

bash

```
docker run -rm -p 54545:54545 -v /path/to/your/config.yaml:/CLIProxyAPI/config.yaml -v /path/to/your/auth-dir:/root/.cli-proxy-api eceasy/cli-proxy-api:latest /CLIProxyAPI/CLIProxyAPI --claude-login
```

Run the following command to login (Qwen OAuth):

bash

```
docker run -it -rm -v /path/to/your/config.yaml:/CLIProxyAPI/config.yaml -v /path/to/your/auth-dir:/root/.cli-proxy-api eceasy/cli-proxy-api:latest /CLIProxyAPI/CLIProxyAPI --qwen-login
```

Run the following command to login (iFlow OAuth on port 11451):

bash

```
docker run --rm -p 11451:11451 -v /path/to/your/config.yaml:/CLIProxyAPI/config.yaml -v /path/to/your/auth-dir:/root/.cli-proxy-api eceasy/cli-proxy-api:latest /CLIProxyAPI/CLIProxyAPI --iflow-login
```

Run the following command to login (Antigravity OAuth on port 51121):

bash

```
docker run --rm -p 51121:51121 -v /path/to/your/config.yaml:/CLIProxyAPI/config.yaml -v /path/to/your/auth-dir:/root/.cli-proxy-api eceasy/cli-proxy-api:latest /CLIProxyAPI/CLIProxyAPI --antigravity-login
```

Run the following command to start the server:

bash

```
docker run --rm -p 8317:8317 -v /path/to/your/config.yaml:/CLIProxyAPI/config.yaml -v /path/to/your/auth-dir:/root/.cli-proxy-api eceasy/cli-proxy-api:latest
```