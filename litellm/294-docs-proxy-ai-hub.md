---
title: AI Hub | liteLLM
url: https://docs.litellm.ai/docs/proxy/ai_hub
source: sitemap
fetched_at: 2026-01-21T19:51:10.325133883-03:00
rendered_js: false
word_count: 278
summary: This document explains how administrators can share and manage models, agents, and MCP servers across an organization by making them discoverable through a public AI Hub.
tags:
    - ai-hub
    - model-sharing
    - agent-discovery
    - mcp-servers
    - admin-ui
    - resource-management
category: guide
---

Share models and agents with your organization. Show developers what's available without needing to rebuild them.

This feature is **available in v1.74.3-stable and above**.

## Overview[​](#overview "Direct link to Overview")

Admin can select models/agents to expose on public AI hub → Users go to the public url and see what's available.

## Models[​](#models "Direct link to Models")

### How to use[​](#how-to-use "Direct link to How to use")

#### 1. Go to the Admin UI[​](#1-go-to-the-admin-ui "Direct link to 1. Go to the Admin UI")

Navigate to the Model Hub page in the Admin UI (`PROXY_BASE_URL/ui/?login=success&page=model-hub-table`)

#### 2. Select the models you want to expose[​](#2-select-the-models-you-want-to-expose "Direct link to 2. Select the models you want to expose")

Click on `Select Models to Make Public` and select the models you want to expose.

#### 3. Confirm the changes[​](#3-confirm-the-changes "Direct link to 3. Confirm the changes")

#### 4. Success\![​](#4-success "Direct link to 4. Success!")

Go to the public url (`PROXY_BASE_URL/ui/model_hub_table`) and see available models.

### API Endpoints[​](#api-endpoints "Direct link to API Endpoints")

- `GET /public/model_hub` – returns the list of public model groups. Requires a valid user API key.
- `GET /public/model_hub/info` – returns metadata (docs title, version, useful links) for the public model hub.

## Agents[​](#agents "Direct link to Agents")

info

Agents are only available in v1.79.4-stable and above.

Share pre-built agents (A2A spec) across your organization. Users can discover and use agents without rebuilding them.

[**Demo Video**](https://drive.google.com/file/d/1r-_Rtiu04RW5Fwwu3_eshtA1oZtC3_DH/view?usp=sharing)

### 1. Create an agent[​](#1-create-an-agent "Direct link to 1. Create an agent")

Create an agent that follows the [A2A spec](https://a2a.dev/).

- UI
- API

### 2. Make agent public[​](#2-make-agent-public "Direct link to 2. Make agent public")

Make the agent discoverable on the AI Hub.

- UI
- API

Navigate to the Agents Tab on the AI Hub page

Select the agents you want to make public and click on `Make Public` button.

### 3. View public agents[​](#3-view-public-agents "Direct link to 3. View public agents")

Users can now discover the agent via the public endpoint.

- UI
- API

## MCP Servers[​](#mcp-servers "Direct link to MCP Servers")

### How to use[​](#how-to-use-1 "Direct link to How to use")

#### 1. Add MCP Server[​](#1-add-mcp-server "Direct link to 1. Add MCP Server")

Go here for instructions: [MCP Overview](https://docs.litellm.ai/docs/mcp#adding-your-mcp)

#### 2. Make MCP server public[​](#2-make-mcp-server-public "Direct link to 2. Make MCP server public")

- UI
- API

Navigate to AI Hub page, and select the MCP tab (`PROXY_BASE_URL/ui/?login=success&page=mcp-server-table`)

#### 3. View public MCP servers[​](#3-view-public-mcp-servers "Direct link to 3. View public MCP servers")

Users can now discover the MCP server via the public endpoint (`PROXY_BASE_URL/ui/model_hub_table`)

- UI
- API