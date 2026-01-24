---
title: Roo Code
url: https://docs.z.ai/devpack/tool/roo.md
source: llms
fetched_at: 2026-01-24T11:22:54.481729493-03:00
rendered_js: false
word_count: 374
summary: This guide provides instructions for installing and configuring the Roo Code VS Code plugin to work with the GLM Coding Plan for AI-assisted development.
tags:
    - roo-code
    - vs-code-extension
    - glm-coding-plan
    - api-setup
    - ai-coding
category: guide
---

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.z.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# Roo Code

> Methods for Using the GLM Coding Plan in Roo Code Plugin

Roo Code is an intelligent VS Code plugin that assists with project analysis, code generation, and refactoring—making the development process smoother and more efficient.

Roo Code becomes even more powerful with the [GLM Coding Plan](https://z.ai/subscribe?utm_source=zai\&utm_medium=link\&utm_term=devpack-integration\&utm_campaign=Platform_Ops&_channel_track_key=w3mNdY8g) — giving you greater efficiency and stability in project management and code optimization.

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

## Step 1: Installing the Roo Code Plugin

### 1. Open the Extensions Marketplace

a. Launch VS Code

b. Click the Extensions Marketplace icon on the left sidebar

c. Enter `Roo Code` in the search bar

d. Locate the `Roo Code` plugin

![Description](https://cdn.bigmodel.cn/markdown/1753687765281r1.png?attname=r1.png)

### 2. Install the Plugin

a. Click the `Install` button to begin installation

b. After installation, select "Trust the Author"

## Step 2: Configuring API Settings

### Configuration Details

Fill in the following information as specified:

> If your Roo Code version is lower and does not have the `China Coding Plan` option, please update the plugin to the latest version first.

* **API Provider**: Select `Z AI`
* **Z AI Entrypoint**：Select `International Coding Plan (https://api.z.ai/api/coding/paas/v4/)`
* **Z AI API Key**: Input your Z.AI API Key
* **Model**: Select `glm-4.7` or other model in the list

![Description](https://cdn.bigmodel.cn/markdown/1760942980972image.png?attname=image.png)

## Step 3: Permission Setup and Usage

### 1. Configure Permissions

Select the permissions you wish to enable based on your needs:

* File read/write operations
* Auto-approve execution
* Project access permissions

![Description](https://cdn.bigmodel.cn/markdown/1753687800340r4.png?attname=r4.png)

### 2. Start Coding

Enter your requirements in the input box, and Roo Code will assist with:

* Summarizing the current project structure
* Analyzing key modules and functionalities
* Code refactoring and optimization
* Generating documentation and comments
* Issue diagnosis and repair suggestions

## Step 4: Vision Search Reader MCP

Refer to the [Vision MCP Server](../mcp/vision-mcp-server) , [Search MCP Server](../mcp/search-mcp-server) and [Web Reader MCP Server](../mcp/reader-mcp-server) documentation; once configured, you can use them in Roo Code.