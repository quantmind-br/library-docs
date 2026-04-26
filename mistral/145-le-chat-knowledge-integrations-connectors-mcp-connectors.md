---
title: MCP Connectors | Mistral Docs
url: https://docs.mistral.ai/le-chat/knowledge-integrations/connectors/mcp-connectors
source: sitemap
fetched_at: 2026-04-26T04:07:55.259811117-03:00
rendered_js: false
word_count: 748
summary: This document provides instructions for administrators to integrate third-party services into Le Chat using the Model Context Protocol (MCP), covering configuration, authentication, and security best practices.
tags:
    - mcp
    - connectors
    - le-chat
    - third-party-integration
    - administration
    - authentication
    - security
category: guide
optimized: true
optimized_at: 2026-04-26T00:00:00Z
---

# MCP Connectors

Beyond our [featured Connectors](https://docs.mistral.ai/le-chat/knowledge-integrations/connectors), you can connect Le Chat to third-party and custom services built on the [Model Context Protocol](https://modelcontextprotocol.io) (MCP).

There are two ways to add an MCP Connector: pick one from the **pre-configured directory**, or point Le Chat at **your own MCP-compatible server**. Both require an administrator.

> [!warning]
> MCP Connectors aren't Mistral products. We don't control third-party servers. Connect only to servers you trust.

## Adding from the Directory

1. Open the `Connectors` page.
2. Click `+ Add Connector`.
3. Browse the directory or search for a specific Connector.
4. Click a Connector to view its details and add it to your organization.
5. Complete the authentication flow if required.

Some Connectors in the directory require additional configuration (a custom URL or API key).

> [!info]
> This is an administrator-only feature. On Free, Pro, and Student plans, the account owner is the administrator by default.

## Adding a Custom Connector

1. Open the `Connectors` page.
2. Click `+ Add Connector` and switch to the `Custom MCP Connector` tab.
3. Fill in the required fields:
   - **Connector name**: unique identifier (no spaces or special characters).
   - **Server URL**: full URL of your MCP-compatible server.
   - **Description** (optional): short explanation of what this Connector does.
4. Click `Connect`. The platform detects the server's authentication method automatically.
5. Complete the authentication flow if prompted.

### Supported Authentication Methods

| Method | Use Case |
|--------|----------|
| **No authentication** | Publicly accessible or trusted internal servers |
| **HTTP Bearer Token / Basic Auth** | Servers requiring credentials in `Authorization` header |
| **OAuth 2.1** (with dynamic client registration) | Servers using standard OAuth 2.1 delegated access |

## Pre-authorizing Functions

After setup, every user can control whether Le Chat asks for permission each time it calls a Connector function:

1. Go to `Connectors` and select the `My Connectors` tab.
2. Click the Connector card to open its details.
3. Open the `Functions` tab.
4. Toggle `Always Allow` for each function you want to pre-authorize.

MCP Connectors expose two types of functions:
- **Read functions**: retrieve information (list events, search files, get data). Lower risk.
- **Write functions**: perform actions (send emails, create events, modify records). Higher risk.

> [!tip]
> Pre-authorize read functions you use frequently. Keep write functions on manual approval until you're confident.

## Security Best Practices

Since MCP Connectors connect Le Chat to servers we haven't reviewed:

- **Vet every server you connect.** Check the publisher, review documentation, and verify the server's purpose before adding it.
- **Watch for unexpected changes.** Server developers can update tools at any time.
- **Guard against prompt injection.** Review tool inputs and outputs for anything unexpected.
- **Grant only the permissions you need.** Start with manual approval and only pre-authorize functions you trust.

> [!danger]
> If you discover a malicious MCP server, report it to our support team.

## Troubleshooting

Custom MCP Connectors don't yet support all MCP capabilities. If you see *"MCP connection requires additional information or is invalid"*, check:

- **Endpoint URL**: make sure you're using the correct path (some servers use `/mcp` or `/sse`). Streamable HTTP is the current standard.
- **Server reachability**: the server must be accessible over HTTPS with a valid TLS certificate.
- **Authentication**: verify your credentials.
- **MCP handshake**: the server must respond correctly to the `initialize` JSON-RPC call.

Use the [MCP Inspector](https://modelcontextprotocol.io/docs/tools/inspector) to test your server's compatibility.

## Related

- [[143-le-chat-knowledge-integrations-connectors|Connectors]]: overview of all available Connectors.
- [[144-le-chat-knowledge-integrations-connectors-knowledge-connectors|Knowledge Connectors]]: set up Google Drive and Microsoft SharePoint.
- [[142-le-chat-knowledge-integrations-agents|Agents]]: attach MCP Connectors to Agents for context-aware assistants.

#mcp #connectors #le-chat #third-party-integration #security
