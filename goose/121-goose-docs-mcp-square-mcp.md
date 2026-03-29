---
title: Square MCP Extension | goose
url: https://block.github.io/goose/docs/mcp/square-mcp
source: github_pages
fetched_at: 2026-01-22T22:15:49.876389946-03:00
rendered_js: true
word_count: 230
summary: This document provides instructions for setting up and using the Square MCP server with the goose AI agent to automate Square seller account tasks.
tags:
    - square-mcp
    - mcp-server
    - goose-ai
    - square-api
    - automation
    - configuration
category: tutorial
---

🎥 Square MCP Server Video Walkthrough

This tutorial will get you started with the [Square MCP server](https://developer.squareup.com/docs/mcp) to enable interactive and automated work for your Square seller account. The Square MCP server is an open source project that allows you to interact with the Square API using goose.

Square offers two versions of the MCP server:

1. **Remote MCP server** hosted by Square, which uses OAuth for authentication and allows fine-grained permissions on API usage.
2. **Local MCP server** that you can run on your own machine, which uses an access token for authentication and allows full API access.

info

Note that you'll need [Node.js](https://nodejs.org/) installed on your system to run installation commands, which use `npx`.

## Configuration[​](#configuration "Direct link to Configuration")

- Square Remote MCP
- Square Local MCP

TLDR

- goose Desktop
- goose CLI

<!--THE END-->

- goose Desktop
- goose CLI

<!--THE END-->

1. [Launch the installer](https://mcp.squareup.com/goose)
2. Click `OK` to confirm the installation
3. goose should open a browser tab to an OAuth permissions page. Double-check which permissions you want to allow, and click `Grant Access`.
4. It will ask you to login or reauthenticate to Square, and may ask you to confirm the permissions you want to allow.
5. In goose, navigate to the chat

## Example Usage[​](#example-usage "Direct link to Example Usage")

The Square MCP server allows you to interact with Square's connect API with an extensive [service catalog](https://github.com/square/square-mcp-server?tab=readme-ov-file#service-catalog) to access the Square API ecosystem.

#### goose Prompt[​](#goose-prompt "Direct link to goose Prompt")

```
( O)> Find my food menu from the following image and import these into my Square seller account. "my-burger-menu.png"
```

[Here's the menu image used in the demo.](https://block.github.io/goose/assets/files/square-mcp-goosin-menu-192f4e4ee8aad4c74a1ce35a5f09167f.png)

#### goose Output[​](#goose-output "Direct link to goose Output")

```
I'll help you import these menu items into your Square catalog. I'll use the Square API to create catalog items for each burger. Let me break this down into steps:

1. First, I'll check the catalog API service info and types
2. Then I'll create catalog items for each burger

Now let me check the type info for creating catalog objects

Now I'll start creating catalog items for each burger in your menu. I'll create them one by one using the catalog API. Let me process each burger:

(output truncated)

I've successfully created all the burger items from your menu in your Square catalog. Each burger has been added with:

- The exact name from your menu
- The full description
- The correct price
- A standard variation for ordering

Here's a summary of what was created:
- The Classic - $10.00
- Cheeseburger - $11.00
- Primetime Burger - $12.00
- Double Bacon - $14.00
- Texas Meatlover - $12.50
- Buffalo Burger - $12.00
- The Atomic - $12.50
- Little Bird - $11.00
- Mushroom Burger - $10.00

All items are now available in your Square catalog and ready for use in your point of sale system. Each burger includes its complete description and comes with a "Regular" variation at the specified price. The items are set as both sellable and stockable by default, and they're available at all locations.
```