---
title: Quick Start | CLIProxyAPI
url: https://help.router-for.me/introduction/quick-start
source: crawler
fetched_at: 2026-01-14T22:09:55.474670576-03:00
rendered_js: false
word_count: 61
summary: This document provides instructions on how to install and run the CLIProxyAPI on various operating systems including macOS, Linux, Windows, and via Docker, as well as how to build it from source.
tags:
    - installation
    - macos
    - linux
    - windows
    - docker
    - build-from-source
category: tutorial
---

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

Thanks to [brokechubb](https://github.com/brokechubb) for building the Linux installer!

## Windows [​](#windows)

You can download the latest release from [here](https://github.com/router-for-me/CLIProxyAPI/releases) and run it directly.

Or

You can download our desktop GUI app from [here](https://github.com/router-for-me/EasyCLI/releases) and run it directly.

## Docker [​](#docker)

bash

```
docker run --rm -p 8317:8317 -v /path/to/your/config.yaml:/CLIProxyAPI/config.yaml -v /path/to/your/auth-dir:/root/.cli-proxy-api eceasy/cli-proxy-api:latest
```

## Building from Source [​](#building-from-source)

1. Clone the repository:
   
   bash
   
   ```
   git clone https://github.com/router-for-me/CLIProxyAPI.git
   cd CLIProxyAPI
   ```
2. Build the application:
   
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