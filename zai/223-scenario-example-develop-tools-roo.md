---
title: Roo Code
url: https://docs.z.ai/scenario-example/develop-tools/roo.md
source: llms
fetched_at: 2026-01-24T11:23:50.344272424-03:00
rendered_js: false
word_count: 315
summary: This guide provides step-by-step instructions for installing and configuring the Roo Code VS Code plugin with the Z.AI GLM model for AI-powered coding assistance.
tags:
    - roo-code
    - vs-code
    - z-ai
    - glm-model
    - ide-plugin
    - api-configuration
    - coding-assistant
category: guide
---

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.z.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# Roo Code

> A complete guide to integrating the Roo Code plugin with the Z.AI GLM model in VS Code

Roo Code is an intelligent VS Code plugin that assists with project analysis, code generation, refactoring, and other tasks.

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

![Description](https://cdn.bigmodel.cn/markdown/1753687776740r2.png?attname=r2.png)

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

### 2. Start Using

Enter your requirements in the input box, and Roo Code will assist with:

* Summarizing the current project structure
* Analyzing key modules and functionalities
* Code refactoring and optimization
* Generating documentation and comments
* Issue diagnosis and repair suggestions

## Step 4: Vision Search Reader MCP

Refer to the [Vision Understanding MCP Server](/devpack/mcp/vision-mcp-server) [Web Search MCP Server](/devpack/mcp/search-mcp-server) [Web Reader MCP Server](/devpack/mcp/reader-mcp-server) documentation; once configured, you can use them in Roo Code.

### Demo

<video src="https://cdn.bigmodel.cn/agent-demos/roo/video%20demo.mp4" controls />