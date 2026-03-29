---
title: Cline
url: https://docs.z.ai/scenario-example/develop-tools/cline.md
source: llms
fetched_at: 2026-01-24T11:23:39.471600017-03:00
rendered_js: false
word_count: 295
summary: This guide provides instructions for installing and configuring the Cline VS Code extension to use Z.AI's GLM models via an OpenAI-compatible API. It covers plugin setup, API parameter configuration, and integration with additional MCP servers for enhanced functionality.
tags:
    - cline
    - vs-code-extension
    - glm-4
    - api-configuration
    - coding-assistant
    - z-ai
category: guide
---

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.z.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# Cline

> A complete guide to using the Cline plugin in VS Code to connect to the Z.AI GLM model

Cline is a powerful VS Code plugin that allows you to directly use AI models in the editor for tasks such as code generation and file operations.

<Warning>
  For users who have used the service before 2025-12-22: \
  The default model has been upgraded to GLM-4.7. Please update your config accordingly.
</Warning>

## Step 1: Installing the Cline Plugin

### 1. Open the Extensions Marketplace

a. Open VS Code

b. Click the Extensions Marketplace icon on the left

c. Enter `cline` in the search box

d. Locate the `Cline` extension

![Description](https://cdn.bigmodel.cn/markdown/1753688113562c1.png?attname=c1.png)

### 2. Install the Plugin

a. Click the `Install` button to install

b. After installation, choose to trust the developer

![Description](https://cdn.bigmodel.cn/markdown/1753688124582c2.jpg?attname=c2.jpg)

## Step 2: Configuring API Settings

### 1. Select API Key Method

Choose `Use your own API Key`

![Description](https://cdn.bigmodel.cn/markdown/1753688131403c3.png?attname=c3.png)

### 2. Enter Configuration Information

Fill in the relevant information according to the following settings:

* **API Provider**: Select `OpenAI Compatible`
* **Base URL**: Enter `https://api.z.ai/api/coding/paas/v4`
* **API Key**: Enter your Z.AI API Key
* **Model**: Select "Use custom" and enter the model name (e.g., `glm-4.7`)
* **Other Configurations**:
  * Unchecking **Support Images**
  * Adjust **Context Window Size** to `204800`
  * Adjust `temperature` and other params according to your task requirements.

![Description](https://cdn.bigmodel.cn/markdown/1759418929636image.png?attname=image.png)

## Step 3: Getting Started

Once configured, you can enter your requirements in the input box to let the model assist you with various tasks, such as:

* Creating and editing files
* Generating code
* Refactoring code
* Explaining code logic
* Debugging issues

![Description](https://cdn.bigmodel.cn/markdown/1753688145687c5.png?attname=c5.png)

## Step 4: Vision Search Reader MCP

Refer to the [Vision Understanding MCP Server](/devpack/mcp/vision-mcp-server) [Web Search MCP Server](/devpack/mcp/search-mcp-server) [Web Reader MCP Server](/devpack/mcp/reader-mcp-server) documentation; once configured, you can use them in Cline.