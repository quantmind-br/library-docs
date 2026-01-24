---
title: Use WSL
url: https://docs.docker.com/desktop/features/wsl/use-wsl/
source: llms
fetched_at: 2026-01-24T14:18:41.505888818-03:00
rendered_js: false
word_count: 177
summary: This document explains how to set up a development environment using Docker Desktop with WSL 2 and Visual Studio Code.
tags:
    - docker
    - wsl2
    - vs-code
    - linux-development
    - remote-wsl
    - workflow-setup
category: tutorial
---

Table of contents

* * *

The following section describes how to start developing your applications using Docker and WSL 2. We recommend that you have your code in your default Linux distribution for the best development experience using Docker and WSL 2. After you have turned on the WSL 2 feature on Docker Desktop, you can start working with your code inside the Linux distribution and ideally with your IDE still in Windows. This workflow is straightforward if you are using [VS Code](https://code.visualstudio.com/download).

## [Develop with Docker and WSL 2](#develop-with-docker-and-wsl-2)

1. Open VS Code and install the [Remote - WSL](https://marketplace.visualstudio.com/items?itemName=ms-vscode-remote.remote-wsl) extension. This extension lets you work with a remote server in the Linux distribution and your IDE client still on Windows.
2. Open your terminal and type:
3. Navigate to your project directory and then type:
   
   This opens a new VS Code window connected remotely to your default Linux distribution which you can check in the bottom corner of the screen.

Alternatively, you can open your default Linux distribution from the **Start** menu, navigate to your project directory, and then run `code .`