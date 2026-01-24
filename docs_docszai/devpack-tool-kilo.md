---
title: Kilo Code
url: https://docs.z.ai/devpack/tool/kilo.md
source: llms
fetched_at: 2026-01-24T11:22:50.426960074-03:00
rendered_js: false
word_count: 382
summary: This document provides a step-by-step guide for installing and configuring the Kilo Code VS Code extension to use the GLM Coding Plan and MCP servers.
tags:
    - vs-code-extension
    - kilo-code
    - glm-coding-plan
    - api-configuration
    - mcp-integration
category: tutorial
---

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.z.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# Kilo Code

> Methods for Using the GLM Coding Plan in Kilo Code plugin

Kilo Code is a powerful VS Code plugin with support for MCP (Model Context Protocol), enabling you to generate code, debug, and manage projects directly within the editor — delivering a more efficient and intelligent development experience.

Kilo Code’s performance is further enhanced with the [GLM Coding Plan](https://z.ai/subscribe?utm_source=zai\&utm_medium=link\&utm_term=devpack-integration\&utm_campaign=Platform_Ops&_channel_track_key=w3mNdY8g),, helping you achieve greater efficiency and stability in both code creation and project collaboration.

<Tip>
  **Christmas Deal:** Enjoy 50% off your first GLM Coding Plan purchase, **plus an extra 10%/20% off**! [Subscribe](https://z.ai/subscribe?utm_source=z.ai\&utm_medium=link\&utm_term=glm-devpack\&utm_campaign=Platform_Ops&_channel_track_key=jFgqJREK) now.
</Tip>

<Warning>
  Using the GLM Coding Plan, you need to configure the dedicated Coding API [https://api.z.ai/api/coding/paas/v4](https://api.z.ai/api/coding/paas/v4) instead of the General API [https://api.z.ai/api/paas/v4](https://api.z.ai/api/paas/v4)
</Warning>

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

## Step 2. Configuring API Settings

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

## Step 3. Getting Started

Once configured, you can enter prompts in the input box to leverage the AI model for various tasks, such as:

* Analyzing database table structures
* Calculating statistics and averages
* Generating and optimizing SQL queries
* Code generation and refactoring
* Project analysis and documentation writing

## Step 4: Vision Search Reader MCP

Refer to the [Vision MCP Server](../mcp/vision-mcp-server) , [Search MCP Server](../mcp/search-mcp-server) and [Web Reader MCP Server](../mcp/reader-mcp-server) documentation; once configured, you can use them in Kilo Code.