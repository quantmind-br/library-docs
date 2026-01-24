---
title: Gemini CLI
url: https://docs.z.ai/scenario-example/develop-tools/gemini.md
source: llms
fetched_at: 2026-01-24T11:23:41.74277015-03:00
rendered_js: false
word_count: 180
summary: This guide provides step-by-step instructions for installing and configuring a customized version of the Gemini CLI to access Z.AI GLM models. It covers repository setup, environment variable configuration, and terminal-based installation for Node.js environments.
tags:
    - gemini-cli
    - z-ai
    - glm-models
    - openrouter-compatibility
    - command-line-interface
    - node-js
    - cli-configuration
category: tutorial
---

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.z.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# Gemini CLI

> Complete Guide to Accessing Z.AI GLM Models Using a Customized Gemini CLI

Gemini CLI is a command-line interface tool that can be made compatible with Z.AI's GLM models by using a customized fork.

## Step 1: Obtaining the Custom Version

### 1. Cloning the Custom Repository

Since the official Gemini CLI repository only supports Google's Gemini models, we need to use a customized branch that supports OpenRouter compatibility:

```bash  theme={null}
git clone https://github.com/heartyguy/gemini-cli  
cd gemini-cli  
```

### 2. Switching to the Compatible Branch

```bash  theme={null}
git checkout feature/openrouter-support  
```

## Step 2: Environment Configuration

### 1. Setting Environment Variables

![Description](https://cdn.bigmodel.cn/markdown/1753631661971gemini-1.png?attname=gemini-1.png)

Configure the API base URL:

```bash  theme={null}
export OPENROUTER_BASE_URL="https://api.z.ai/api/coding/paas/v4"  
```

Configure the API Key:

```bash  theme={null}
export OPENROUTER_API_KEY="your_api_key"  
```

## Step 3: Installation and Launch

### 1. System Requirements

Ensure your Node.js version is >= 18.

### 2. Installing Dependencies

```bash  theme={null}
npm install  
```

### 3. Launch Process

![Description](https://cdn.bigmodel.cn/markdown/1753631666323gemini-2.png?attname=gemini-2.png)

After launching, complete the following steps:

1. Select a background color theme.
2. User login (recommended to use a Google account for authentication, which will redirect to a webpage for verification).

## Step 4: Usage Results

![Description](https://cdn.bigmodel.cn/markdown/1753631670672gemini-3.png?attname=gemini-3.png)

Once configured, you can use Z.AI's GLM models in the command line for conversations and code generation.