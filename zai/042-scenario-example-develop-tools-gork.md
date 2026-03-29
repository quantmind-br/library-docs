---
title: Grok CLI
url: https://docs.z.ai/scenario-example/develop-tools/gork.md
source: llms
fetched_at: 2026-01-24T11:23:41.929368673-03:00
rendered_js: false
word_count: 129
summary: This guide provides step-by-step instructions for installing, configuring, and using the Grok CLI tool to interact with Z.AI's GLM models.
tags:
    - grok-cli
    - z-ai
    - glm-models
    - command-line-interface
    - cli-installation
    - environment-setup
category: tutorial
---

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.z.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# Grok CLI

> Quick Start Guide for Connecting to Z.AI GLM Models Using Grok CLI

Grok CLI is a streamlined command-line AI assistant that enables quick access to Z.AI's GLM models for conversation and code generation.

## Step 1: Installing Grok CLI

Install Grok CLI globally via npm:

```bash  theme={null}
npm install -g @vibe-kit/grok-cli  
```

## Step 2: Environment Configuration

Set the API base URL and API Key:

```bash  theme={null}
export GROK_BASE_URL="https://api.z.ai/api/coding/paas/v4"  
export GROK_API_KEY="your_api_key"  
```

## Step 3: Getting Started

Launch Grok CLI with a specified model:

```bash  theme={null}
grok --model glm-4.7
```

![Description](https://cdn.bigmodel.cn/markdown/1753631674840gemini-4.png?attname=gemini-4.png)

## Notes

> **Important Note**: Grok CLI currently has limited compatibility with thinking models, and thinking content will be displayed in full. Recommendations:
>
> * Wait for Grok CLI to improve compatibility with thinking models
> * Or use non-thinking versions of the models