---
title: Roo Code
url: https://docs.ollama.com/integrations/roo-code.md
source: llms
fetched_at: 2026-02-04T11:34:45.812114393-03:00
rendered_js: false
word_count: 162
summary: This document provides step-by-step instructions for installing the Roo Code VS Code extension and configuring it to work with Ollama as an AI provider.
tags:
    - vs-code-extension
    - roo-code
    - ollama-configuration
    - ai-coding-assistant
    - ide-integration
category: guide
---

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.ollama.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Roo Code

## Install

Install [Roo Code](https://marketplace.visualstudio.com/items?itemName=RooVeterinaryInc.roo-cline) from the VS Code Marketplace.

## Usage with Ollama

1. Open Roo Code in VS Code and click the **gear icon** on the top right corner of the Roo Code window to open **Provider Settings**
2. Set `API Provider` to `Ollama`
3. (Optional) Update `Base URL` if your Ollama instance is running remotely. The default is `http://localhost:11434`
4. Enter a valid `Model ID` (for example `qwen3` or `qwen3-coder:480b-cloud`)
5. Adjust the `Context Window` to at least 32K tokens for coding tasks

<Note>Coding tools require a larger context window. It is recommended to use a context window of at least 32K tokens. See [Context length](/context-length) for more information.</Note>

## Connecting to ollama.com

1. Create an [API key](https://ollama.com/settings/keys) from ollama.com
2. Enable `Use custom base URL` and set it to `https://ollama.com`
3. Enter your **Ollama API Key**
4. Select a model from the list

### Recommended Models

* `qwen3-coder:480b`
* `deepseek-v3.1:671b`