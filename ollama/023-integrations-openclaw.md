---
title: OpenClaw
url: https://docs.ollama.com/integrations/openclaw.md
source: llms
fetched_at: 2026-02-04T11:34:40.254814316-03:00
rendered_js: false
word_count: 149
summary: This document provides instructions for installing and configuring OpenClaw, a personal AI assistant gateway that connects messaging services to AI coding agents using Ollama.
tags:
    - openclaw
    - ollama-integration
    - installation-guide
    - ai-assistant
    - coding-agents
    - gateway-setup
category: guide
---

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.ollama.com/llms.txt
> Use this file to discover all available pages before exploring further.

# OpenClaw

OpenClaw is a personal AI assistant that runs on your own devices. It bridges messaging services (WhatsApp, Telegram, Slack, Discord, iMessage, and more) to AI coding agents through a centralized gateway.

## Install

Install [OpenClaw](https://openclaw.ai/)

```bash  theme={"system"}
npm install -g openclaw@latest
```

Then run the onboarding wizard:

```bash  theme={"system"}
openclaw onboard --install-daemon
```

<Note>OpenClaw requires a larger context window. It is recommended to use a context window of at least 64k tokens. See [Context length](/context-length) for more information.</Note>

## Usage with Ollama

### Quick setup

```bash  theme={"system"}
ollama launch openclaw
```

<Note>Previously known as Clawdbot. `ollama launch clawdbot` still works as an alias.</Note>

This configures OpenClaw to use Ollama and starts the gateway.
If the gateway is already running, no changes need to be made as the gateway will auto-reload the changes.

To configure without launching:

```shell  theme={"system"}
ollama launch openclaw --config
```

## Recommended Models

* `qwen3-coder`
* `glm-4.7`
* `gpt-oss:20b`
* `gpt-oss:120b`

Cloud models are also available at [ollama.com/search?c=cloud](https://ollama.com/search?c=cloud).