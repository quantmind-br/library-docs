---
title: Knowledge Connectors | Mistral Docs
url: https://docs.mistral.ai/le-chat/knowledge-integrations/connectors/knowledge-connectors
source: sitemap
fetched_at: 2026-04-26T04:07:53.724483163-03:00
rendered_js: false
word_count: 739
summary: This document explains how administrators can configure and index Google Drive and SharePoint as Knowledge Connectors to enable secure, natural language querying of organizational files within Le Chat.
tags:
    - knowledge-connectors
    - google-drive
    - sharepoint
    - data-indexing
    - selective-sync
    - permissions-management
    - enterprise-administration
category: guide
optimized: true
optimized_at: 2026-04-26T00:00:00Z
---

# Knowledge Connectors

Google Drive and Microsoft SharePoint work differently from other [Connectors](https://docs.mistral.ai/le-chat/knowledge-integrations/connectors). Instead of fetching data in real time, they **index your files** (process and catalog them for fast search) and store them on our platform so Le Chat can search them instantly, similar to how [Libraries](https://docs.mistral.ai/le-chat/knowledge-integrations/libraries) work.

Knowledge Connectors are available on **Team and Enterprise plans**. An administrator must set up indexing before users can connect.

## How It Works

1. An **administrator** configures the Connector and initiates indexing of your organization's files.
2. Files are indexed and stored in our European data centers.
3. **Users** connect with their own accounts and start querying indexed content from the chat.
4. The index syncs regularly with the source. Edits, new files, and deletions are reflected during each scheduled sync.

> [!note]
> This is a one-time process. Once indexing is complete, your team can connect and start using the Connector.

## Administrator Setup

1. Go to the `Connectors` page and open the `Admin Controls` tab.
2. Find **Google Drive** or **SharePoint** and click `Setup`.
3. Review the indexing information modal and click `Setup`.
4. Follow the setup flow: sign in with your Google admin account and grant the required permissions.
5. Monitor indexing progress on the `Admin Controls` tab.

Indexing can take minutes to several hours depending on the volume of data.

### Selective Sync

Use **selective sync** to index only specific folders instead of the entire drive.

1. Open the `Admin Controls` tab on the `Connectors` page.
2. Click on the Connector card.
3. Browse and check/uncheck individual folders or sites to include in indexing.

To add new folders to an existing index, re-run the indexing process. New content is added to the existing index.

### Updating the Index

The platform monitors changes at the source (creation, modification, deletion) and updates the index during each scheduled sync. Deleted files are removed from the index.

## User Connection

1. Open the `Connectors` page from the sidebar.
2. Find the Google Drive or SharePoint card and click `Connect`.
3. Sign in with your own Google or Microsoft account.
4. Confirm the connection.

A green `Connected` indicator confirms you're set. You can now query indexed content from any conversation by enabling the Connector as a tool.

> [!warning]
> If you try to connect before indexing is complete, you'll see an error. Check with your administrator.

## Permissions

We replicate user, group, and permission structures from the source system. If you don't have access to a file in Google Drive or SharePoint, you can't access it through Le Chat either.

### Google Drive Specifics

- Permissions are based on explicit sharing (user, group, or domain level).
- Files shared as "anyone with the link" are **not** automatically visible to your entire organization through Le Chat.

### SharePoint Specifics

- Permissions rely on **Microsoft Entra ID** groups. Older SharePoint-only groups may not be recognized.
- Files shared exclusively with external guests are generally **not** indexed.

## Disconnecting

| Who Disconnects | Effect |
|-----------------|--------|
| **User** (from `My Connectors`) | Your ability to query the data is removed. The index stays intact for other users. |
| **Admin** (from `Admin Controls`) | Connector is disabled organization-wide and indexed data is **scheduled for permanent deletion**. |

Re-enabling after an admin disconnection requires a full re-setup and re-indexing.

## Data Privacy

- Files are indexed and stored in our **European data centers**.
- The index is retained only while the knowledge Connector is active.
- Data accessed through Connectors is **never used to train or improve our models**.
- Conversations that reference Connector data follow your plan's [data policies](https://mistral.ai/terms#privacy-policy).

## Related

- [[143-le-chat-knowledge-integrations-connectors|Connectors]]: overview of all available Connectors.
- [[145-le-chat-knowledge-integrations-connectors-mcp-connectors|MCP Connectors]]: browse the directory or connect your own MCP-compatible servers.
- [[147-le-chat-knowledge-integrations-libraries|Libraries]]: build knowledge bases from manually uploaded documents.
- [[142-le-chat-knowledge-integrations-agents|Agents]]: attach knowledge Connectors to Agents for context-aware assistants.

#knowledge-connectors #google-drive #sharepoint #data-indexing #selective-sync
