---
title: Perplexity MCP Server
url: https://docs.perplexity.ai/docs/getting-started/integrations/mcp-server.md
source: llms
fetched_at: 2026-02-04T07:22:58.03675844-03:00
rendered_js: false
word_count: 186
summary: This document provides instructions for installing and configuring the Perplexity MCP Server to integrate web search and reasoning capabilities into AI assistants. It covers setup procedures for various clients and details specific tools for search, research, and deep reasoning.
tags:
    - perplexity-ai
    - mcp-server
    - model-context-protocol
    - search-api
    - installation-guide
    - ai-integration
    - configuration
category: guide
---

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.perplexity.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# Perplexity MCP Server

> Connect AI assistants to Perplexity's search and reasoning capabilities using the Model Context Protocol (MCP).

## Overview

The Perplexity MCP Server enables AI assistants to access Perplexity's powerful search and reasoning capabilities directly within their workflows. Using the Model Context Protocol (MCP), you can integrate real-time web search, conversational AI, and advanced reasoning into any MCP-compatible client.

<Info>
  The **Model Context Protocol (MCP)** is an open standard that connects AI assistants with external data sources and tools. Learn more at [modelcontextprotocol.io](https://modelcontextprotocol.io/introduction).
</Info>

## Installation

### One-Click Install

Get started instantly with these one-click installers:

<CardGroup cols={2}>
  <Card
    title="Install in Cursor"
    icon={
  <svg
    xmlns="http://www.w3.org/2000/svg"
    viewBox="0 0 466.73 532.09"
  >
    <path
      d="M457.43 125.94 244.42 2.96a22.127 22.127 0 0 0-22.12 0L9.3 125.94C3.55 129.26 0 135.4 0 142.05v247.99c0 6.65 3.55 12.79 9.3 16.11l213.01 122.98a22.127 22.127 0 0 0 22.12 0l213.01-122.98c5.75-3.32 9.3-9.46 9.3-16.11V142.05c0-6.65-3.55-12.79-9.3-16.11h-.01Zm-13.38 26.05L238.42 508.15c-1.39 2.4-5.06 1.42-5.06-1.36V273.58c0-4.66-2.49-8.97-6.53-11.31L24.87 145.67c-2.4-1.39-1.42-5.06 1.36-5.06h411.26c5.84 0 9.49 6.33 6.57 11.39h-.01Z"
      style={{ fill: "#22808C" }}
    />
  </svg>
}
    href="https://cursor.com/en/install-mcp?name=perplexity&config=eyJ0eXBlIjoic3RkaW8iLCJjb21tYW5kIjoibnB4IiwiYXJncyI6WyIteSIsIkBwZXJwbGV4aXR5LWFpL21jcC1zZXJ2ZXIiXSwiZW52Ijp7IlBFUlBMRVhJVFlfQVBJX0tFWSI6IiJ9fQ=="
  >
    Automatically configure the Perplexity MCP server in Cursor with one click.
  </Card>

  <Card
    title="Install in VS Code"
    icon={
  <svg
    xmlns="http://www.w3.org/2000/svg"
    viewBox="0 0 100 100"
  >
    <path
      d="M70.912 99.572a6.193 6.193 0 0 0 4.96-.191l20.588-9.958a6.285 6.285 0 0 0 3.54-5.661V16.239a6.286 6.286 0 0 0-3.54-5.662L75.873.62a6.2 6.2 0 0 0-7.104 1.216L29.355 37.98l-17.168-13.1a4.146 4.146 0 0 0-5.318.238l-5.506 5.035a4.205 4.205 0 0 0-.004 6.194L16.247 50 1.36 63.654a4.205 4.205 0 0 0 .004 6.194l5.506 5.034a4.145 4.145 0 0 0 5.318.238l17.168-13.1L68.77 98.166a6.205 6.205 0 0 0 2.143 1.407Zm4.103-72.39L45.11 50 75.015 72.82V27.18Z"
      fillRule="evenodd"
      style={{ fill: "#22808C" }}
    />
  </svg>
}
    href="https://vscode.dev/redirect/mcp/install?name=perplexity&config=%7B%22type%22%3A%22stdio%22%2C%22command%22%3A%22npx%22%2C%22args%22%3A%5B%22-y%22%2C%22%40perplexity-ai%2Fmcp-server%22%5D%2C%22env%22%3A%7B%22PERPLEXITY_API_KEY%22%3A%22%22%7D%7D"
  >
    Automatically configure the Perplexity MCP server in VS Code with one click.
  </Card>
</CardGroup>

### Manual Setup

<Steps>
  <Step title="Get Your API Key">
    <Card title="Generate API Key" icon="key" arrow="True" horizontal="True" iconType="solid" cta="Get Key" href="https://www.perplexity.ai/account/api/group">
      Navigate to the API Portal and generate a new key.
    </Card>
  </Step>

  <Step title="Configure Your Client">
    Add the MCP server to your client configuration:

    <Tabs>
      <Tab title="Claude Code">
        **Option 1: CLI Command (Recommended)**

        The easiest way to get started:

        ```bash  theme={null}
        claude mcp add perplexity --env PERPLEXITY_API_KEY="your_key_here" -- npx -y @perplexity-ai/mcp-server
        ```

        **Option 2: Plugin Install**

        Install via plugin:

        ```bash  theme={null}
        export PERPLEXITY_API_KEY="your_key_here"
        claude
        # Then run: /plugin marketplace add perplexityai/modelcontextprotocol
        # Then run: /plugin install perplexity
        ```

        **Option 3: Manual Configuration**

        Add to your `claude.json`:

        ```json  theme={null}
        {
          "mcpServers": {
            "perplexity": {
              "type": "stdio",
              "command": "npx",
              "args": ["-y", "perplexity-mcp"],
              "env": {
                "PERPLEXITY_API_KEY": "your_key_here"
              }
            }
          }
        }
        ```
      </Tab>

      <Tab title="Cursor">
        We recommend using the one-click install above for setting up the MCP server in Cursor.

        If you prefer to configure it manually, add the following to your `mcp.json`:

        ```json  theme={null}
        {
          "mcpServers": {
            "perplexity": {
              "command": "npx",
              "args": ["-y", "@perplexity-ai/mcp-server"],
              "env": {
                "PERPLEXITY_API_KEY": "your_key_here"
              }
            }
          }
        }
        ```
      </Tab>

      <Tab title="Codex">
        ```bash  theme={null}
        codex mcp add perplexity --env PERPLEXITY_API_KEY="your_key_here" -- npx -y @perplexity-ai/mcp-server
        ```
      </Tab>

      <Tab title="Other Clients">
        Most MCP-compatible clients (including Claude Desktop, VS Code, and Windsurf) use the `mcpServers` format. Configuration file locations:

        | Client             | Config File                             |
        | ------------------ | --------------------------------------- |
        | Cursor             | `~/.cursor/mcp.json`                    |
        | VS Code            | `.vscode/mcp.json`                      |
        | Claude Desktop     | `claude_desktop_config.json`            |
        | Windsurf           | `~/.codeium/windsurf/mcp_config.json`   |
        | Google Antigravity | `~/.gemini/antigravity/mcp_config.json` |

        **Standard `mcpServers` format:**

        ```json  theme={null}
        {
          "mcpServers": {
            "perplexity": {
              "command": "npx",
              "args": ["-y", "@perplexity-ai/mcp-server"],
              "env": {
                "PERPLEXITY_API_KEY": "your_key_here"
              }
            }
          }
        }
        ```

        **VS Code uses a slightly different format:**

        ```json  theme={null}
        {
          "servers": {
            "perplexity": {
              "type": "stdio",
              "command": "npx",
              "args": ["-y", "@perplexity-ai/mcp-server"],
              "env": {
                "PERPLEXITY_API_KEY": "your_key_here"
              }
            }
          }
        }
        ```

        If your client doesn't work with these formats, check its documentation for the correct wrapper format.
      </Tab>
    </Tabs>
  </Step>

  <Step title="Start Using">
    Restart your MCP client and start using Perplexity's tools in your AI workflows.
  </Step>
</Steps>

## Available Tools

<CardGroup cols={2}>
  <Card title="perplexity_search" icon="magnifying-glass">
    Direct web search using the Perplexity Search API. Returns ranked search results with titles, URLs, snippets, and metadata.

    **Best for:** Finding current information, news, facts, or specific web content.
  </Card>

  <Card title="perplexity_ask" icon="message">
    General-purpose conversational AI with real-time web search using the `sonar-pro` model.

    **Best for:** Quick questions, everyday searches, and conversational queries that benefit from web context.
  </Card>

  <Card title="perplexity_research" icon="book">
    Deep, comprehensive research using the `sonar-deep-research` model. Provides thorough analysis with citations.

    **Best for:** Complex topics requiring detailed investigation, comprehensive reports, and in-depth analysis.
  </Card>

  <Card title="perplexity_reason" icon="brain">
    Advanced reasoning and problem-solving using the `sonar-reasoning-pro` model.

    **Best for:** Logical problems, complex analysis, decision-making, and tasks requiring step-by-step reasoning.
  </Card>
</CardGroup>

<Info>
  For detailed setup instructions, troubleshooting, and proxy configuration, visit our [GitHub repository](https://github.com/perplexityai/modelcontextprotocol).
</Info>