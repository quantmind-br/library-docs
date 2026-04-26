---
title: Managing Connectors | Mistral Docs
url: https://docs.mistral.ai/studio-api/knowledge-rag/connectors/management
source: sitemap
fetched_at: 2026-04-26T04:13:00.482719957-03:00
rendered_js: false
word_count: 395
summary: This document outlines the full lifecycle of an MCP Connector, covering registration, authentication, management, and tool discovery processes.
tags:
    - mcp-connector
    - api-integration
    - auth-flow
    - tool-discovery
    - lifecycle-management
category: guide
optimized: true
optimized_at: 2026-04-26T00:00:00Z
---

# Managing Connectors

Before using a Connector in conversations or calling its tools, you need to register it.

## Connector Lifecycle

1. **Create** a Connector with the MCP server URL and visibility scope.
2. **Authenticate** (if the MCP server requires OAuth).
3. **List tools** to discover what the Connector exposes.
4. **Use** the Connector in [conversations](https://docs.mistral.ai/studio-api/knowledge-rag/connectors/conversations) or via [direct tool calls](https://docs.mistral.ai/studio-api/knowledge-rag/connectors/tool_calling).
5. **Update** or **delete** when the Connector is no longer needed.

## Creating a Connector

Register a new MCP Connector by providing a name, MCP server URL, and visibility scope:

| Scope | Access |
|-------|--------|
| `private` | Only the creator can use it |
| `shared_workspace` | Anyone in the same Workspace |
| `shared_org` | Anyone in the organization (admins only) |

- Connector names are unique within a Workspace. Reference by name or UUID.
- `name` accepts up to 64 characters, alphanumeric with underscores and dashes only.

## Authentication (OAuth)

If the MCP server requires OAuth:

1. Retrieve the authorization URL from the `create` endpoint.
2. Redirect the user to grant access.
3. After auth flow completes, the user is redirected to `app_return_url`.

> [!warning]
> Passing tokens programmatically is not supported. Use [AI Studio](https://console.mistral.ai/build/connectors) to authenticate Connectors.

Response includes:
- `auth_url`: URL to redirect the user to
- `ttl`: how long the URL remains valid (seconds)

## Getting a Connector

Retrieve a Connector by name or UUID. Response includes a `tools` array with MCP tools if already discovered.

## Listing All Connectors

List Connectors with cursor-based pagination. Use `next_cursor` to fetch subsequent pages.

Pass `query_filters` to filter results (e.g., `active: true` returns only active Connectors for your user and Workspace).

## Listing Tools

List the tools a Connector exposes. Helps verify available tool names before using them.

> [!warning]
> If the Connector requires authentication, the user must complete the auth flow before listing or calling its tools.

## Updating a Connector

Update fields: `name`, `description`, `server`, `icon_url`, `system_prompt`, `headers`, `auth_data`.

> [!note]
> `connector_id` must be the UUID, not the name.

## Deleting a Connector

Delete a Connector permanently. Any Agents referencing it lose access to its tools.

#mcp-connector #api-integration #auth-flow #tool-discovery
