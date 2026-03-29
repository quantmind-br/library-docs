---
title: OpenCode
url: https://docs.ollama.com/integrations/opencode.md
source: llms
fetched_at: 2026-02-04T11:34:42.996553752-03:00
rendered_js: false
word_count: 129
summary: This document explains how to install the OpenCode CLI and configure it to use local or cloud-based models via Ollama. It includes quick setup commands and manual configuration examples for connecting to various providers.
tags:
    - opencode
    - ollama
    - ai-assistant
    - cli-tool
    - configuration-guide
    - open-source-ai
category: configuration
---

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.ollama.com/llms.txt
> Use this file to discover all available pages before exploring further.

# OpenCode

OpenCode is an open-source AI coding assistant that runs in your terminal.

## Install

Install the [OpenCode CLI](https://opencode.ai):

```bash  theme={"system"}
curl -fsSL https://opencode.ai/install | bash
```

<Note>OpenCode requires a larger context window. It is recommended to use a context window of at least 64k tokens. See [Context length](/context-length) for more information.</Note>

## Usage with Ollama

### Quick setup

```bash  theme={"system"}
ollama launch opencode
```

To configure without launching:

```shell  theme={"system"}
ollama launch opencode --config
```

### Manual setup

Add a configuration block to `~/.config/opencode/opencode.json`:

```json  theme={"system"}
{
  "$schema": "https://opencode.ai/config.json",
  "provider": {
    "ollama": {
      "npm": "@ai-sdk/openai-compatible",
      "name": "Ollama",
      "options": {
        "baseURL": "http://localhost:11434/v1"
      },
      "models": {
        "qwen3-coder": {
          "name": "qwen3-coder"
        }
      }
    }
  }
}
```

## Cloud Models

`glm-4.7:cloud` is the recommended model for use with OpenCode.

Add the cloud configuration to `~/.config/opencode/opencode.json`:

```json  theme={"system"}
{
  "$schema": "https://opencode.ai/config.json",
  "provider": {
    "ollama": {
      "npm": "@ai-sdk/openai-compatible",
      "name": "Ollama",
      "options": {
        "baseURL": "http://localhost:11434/v1"
      },
      "models": {
        "glm-4.7:cloud": {
          "name": "glm-4.7:cloud"
        }
      }
    }
  }
}
```

## Connecting to ollama.com

1. Create an [API key](https://ollama.com/settings/keys) from ollama.com and export it as `OLLAMA_API_KEY`.
2. Update `~/.config/opencode/opencode.json` to point to ollama.com:

```json  theme={"system"}
{
  "$schema": "https://opencode.ai/config.json",
  "provider": {
    "ollama": {
      "npm": "@ai-sdk/openai-compatible",
      "name": "Ollama Cloud",
      "options": {
        "baseURL": "https://ollama.com/v1"
      },
      "models": {
        "glm-4.7:cloud": {
          "name": "glm-4.7:cloud"
        }
      }
    }
  }
}
```

Run `opencode` in a new terminal to load the new settings.