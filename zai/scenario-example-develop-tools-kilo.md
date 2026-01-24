---
title: Kilo Code
url: https://docs.z.ai/scenario-example/develop-tools/kilo.md
source: llms
fetched_at: 2026-01-24T11:23:44.789279515-03:00
rendered_js: false
word_count: 318
summary: This guide provides step-by-step instructions for installing and configuring the Kilo Code VS Code plugin to integrate Z.AI's GLM models for AI-assisted development.
tags:
    - vs-code
    - kilo-code
    - z-ai
    - glm-model
    - mcp-protocol
    - plugin-configuration
    - ai-coding-assistant
category: tutorial
---

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.z.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# Kilo Code

> A complete guide to integrating the GLM model from  Z.AI using the Kilo Code plugin in VS Code

Kilo Code is a powerful VS Code plugin that supports MCP (Model Context Protocol), enabling you to leverage AI models for efficient code development directly in your editor.

<Warning>
  For users who have used the service before 2025-12-22: \
  The default model has been upgraded to GLM-4.7. Please update your config accordingly.
</Warning>

## Step 1: Installing the Kilo Code Plugin

### 1. Open the Extensions Marketplace

a. Launch VS Code

b. Click the Extensions Marketplace icon on the left sidebar

c. Search for `Kilo Code` in the search bar

d. Locate the `Kilo Code` plugin

![Description](https://cdn.bigmodel.cn/markdown/1753687809443k1.jpg?attname=k1.jpg)

### 2. Install the Plugin

a. Click the `Install` button to begin installation

b. After installation, choose to trust the developer

![Description](https://cdn.bigmodel.cn/markdown/1753687816703k2.jpg?attname=k2.jpg)

## Step 2: Configuring API Settings

### 1. Select API Key Authentication

Choose `Use your own API key`

![Description](https://cdn.bigmodel.cn/markdown/1753687824352k3.jpg?attname=k3.jpg)

### 2. Enter Configuration Details

Fill in the following information as specified:

> If your Kilo Code version is outdated and lacks the `International Coding Plan` option, please update the plugin to the latest version.

* **API Provider**: Select `Z AI`
* **Z AI Entrypoint**: Select `International Coding Plan (https://api.z.ai/api/coding/paas/v4/)`
* **Z AI API Key**: Input your Z.AI API Key
* **Model**: Select `glm-4.7` or any other model from the list

![Description](https://cdn.bigmodel.cn/markdown/1760943118846image.png?attname=image.png)

## Step 3: Getting Started

Once configured, you can enter prompts in the input box to leverage the AI model for various tasks, such as:

* Analyzing database table structures
* Calculating statistics and averages
* Generating and optimizing SQL queries
* Code generation and refactoring
* Project analysis and documentation writing

## Step 4: Vision Search Reader MCP

Refer to the [Vision Understanding MCP Server](/devpack/mcp/vision-mcp-server) [Web Search MCP Server](/devpack/mcp/search-mcp-server) [Web Reader MCP Server](/devpack/mcp/reader-mcp-server) documentation; once configured, you can use them in Kilo Code.

### Demo

<video src="https://cdn.bigmodel.cn/agent-demos/kilo/demo.mp4" controls />