---
title: Neon Extension | goose
url: https://block.github.io/goose/docs/mcp/neon-mcp
source: github_pages
fetched_at: 2026-01-22T22:15:31.125861742-03:00
rendered_js: true
word_count: 239
summary: This document provides instructions for integrating the Neon MCP Server with the goose extension to manage Neon Postgres projects, branches, and databases using AI agents. It covers both remote and local configuration methods along with practical usage examples for database interaction.
tags:
    - neon-postgres
    - mcp-server
    - goose-extension
    - database-management
    - ai-agents
    - postgresql-integration
category: tutorial
---

This tutorial covers how to add the [Neon MCP Server](https://github.com/neondatabase/mcp-server-neon) as a goose extension to interact with your Neon Postgres databases and manage your projects, branches, and more.

Neon offers two versions of the MCP server:

1. **Remote MCP server** hosted by Neon, which redirects you to neon.com to sign in to your Neon account.
2. **Local MCP server** that you can run on your own machine using an API key to connect with a specific organization or your personal account.

Security Note

The Neon MCP Server grants powerful database management capabilities and is intended for local development only - always review LLM-requested actions before execution and avoid using in production environments.

## Configuration[​](#configuration "Direct link to Configuration")

- Neon Remote MCP
- Neon Local MCP

TLDR

- goose Desktop
- goose CLI

OAUTH FLOW

An OAuth window will open in your browser. Follow the prompts to authorize access to your Neon account.

- goose Desktop
- goose CLI

<!--THE END-->

1. [Launch the installer](goose://extension?type=streamable_http&url=https%3A%2F%2Fmcp.neon.tech%2Fmcp&id=neon&name=Neon&description=Manage%20Neon%20Postgres%20databases%2C%20projects%2C%20and%20branches)
2. Click `Yes` to confirm the installation
3. Click the button in the top-left to open the sidebar
4. Navigate to the chat

For all setup and configuration options, see the [official Neon MCP Server documentation](https://neon.com/docs/ai/neon-mcp-server).

## Example Usage 1[​](#example-usage-1 "Direct link to Example Usage 1")

Get an overview of all your Neon database projects and their configurations.

### goose Prompt[​](#goose-prompt "Direct link to goose Prompt")

### goose Output[​](#goose-output "Direct link to goose Output")

```
I'll help you list your Neon projects using the neon__list_projects tool. By default, it will show the first 10 projects.

Here are your Neon projects:

1. laravel-test (ID: mute-mountain-08595850)
- Region: AWS US East 2
- Created: July 23, 2025
- PostgreSQL: v17

2. rls-test (ID: noisy-hill-99207787)
- Region: AWS US East 2
- Created: July 20, 2025
- PostgreSQL: v17

3. neon-auth-test (ID: rapid-pond-81053507)
- Region: Azure East US 2
- Created: July 7, 2025
- PostgreSQL: v17

4. saas-starter-kit-nextjs (ID: misty-poetry-78149700)
- Region: AWS US West 2
- Created: June 23, 2025
- PostgreSQL: v17
- Note: Has logical replication enabled

5. neon-auth-mcp-oauth (ID: gentle-base-21700263)
- Region: AWS US West 2
- Created: June 4, 2025
- PostgreSQL: v17

All projects are running PostgreSQL 17 and have autoscaling configured between 1-2 compute units. Would you like more detailed information about any specific project?
```

## Example Usage 2[​](#example-usage-2 "Direct link to Example Usage 2")

Discover what tables and schemas exist within a specific project.

### goose Prompt[​](#goose-prompt-1 "Direct link to goose Prompt")

```
What tables do I have in my neon-auth-mcp-oauth project?
```

### goose Output[​](#goose-output-1 "Direct link to goose Output")

```
In your neon-auth-mcp-oauth project, there is one table:

users_sync in the neon_auth schema
```

## Example Usage 3[​](#example-usage-3 "Direct link to Example Usage 3")

Run queries against your database tables to retrieve and analyze your data.

### goose Prompt[​](#goose-prompt-2 "Direct link to goose Prompt")

```
Count the rows in the users_sync table.
```

### goose Output[​](#goose-output-2 "Direct link to goose Output")

```
I'll count the rows in the neon_auth.users_sync table using a COUNT query.

Total Records: 1 row
Table Location: Schema neon_auth, Table users_sync
Project: neon-auth-mcp-oauth (Project ID: gentle-base-21700263)
Content: Contains one user record
```