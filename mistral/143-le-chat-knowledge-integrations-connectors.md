---
title: Connectors | Mistral Docs
url: https://docs.mistral.ai/le-chat/knowledge-integrations/connectors
source: sitemap
fetched_at: 2026-04-26T04:07:51.18459027-03:00
rendered_js: false
word_count: 575
summary: This document explains how to set up, authorize, and utilize Connectors in Le Chat to integrate external services for data retrieval and task automation.
tags:
    - le-chat
    - connectors
    - integration
    - oauth-authentication
    - data-privacy
    - automation-tools
category: guide
optimized: true
optimized_at: 2026-04-26T00:00:00Z
---

# Connectors

Connectors are **secure bridges** between Le Chat and your external tools and data sources. They let you retrieve, analyze, and act on data from services like Gmail, Google Drive, GitHub, or Notion directly from the chat.

All featured Connectors are **enabled by default** for your organization. Click `Connect` on the card and authenticate.

> [!warning]
> Administrators can disable specific Connectors for the whole organization if needed.

## Connecting a Featured Connector

1. Open the `Connectors` page from the sidebar.
2. Find the Connector card and click `Connect`.
3. Complete the authentication flow (typically OAuth 2.0). Your password is never shared with us.

A green `Connected` indicator confirms the connection. You can disconnect at any time.

> [!note]
> Google Drive and SharePoint require administrator setup before users can connect. See [Knowledge Connectors](https://docs.mistral.ai/le-chat/knowledge-integrations/connectors/knowledge-connectors).

## Using a Connector in Conversation

1. Click the `+` icon or type `/` in the chat window.
2. Select `Tools` then enable the Connector you want to use.
3. Ask your question naturally. Le Chat figures out which Connector to call based on your request.

Example prompts:
- *"What meetings do I have tomorrow?"*
- *"Find the latest Q3 revenue deck in Google Drive."*
- *"Create a calendar event for Friday at 2pm with the product team."*
- *"Check my unread emails from the legal team."*

## Approving Actions

When a Connector performs an action (sending an email, creating an event, modifying a file), Le Chat asks for your **approval before executing**:

- **Continue**: approve this specific action.
- **Always allow**: pre-authorize this function so Le Chat won't ask again.
- **Decline**: cancel the action.

> [!note]
> Read-only functions may also require approval depending on your Connector's configuration.

Manage per-function permissions at any time: go to `Connectors`, select `My Connectors`, open the Connector card, and toggle `Always Allow` for each function.

## Using Connectors with Agents

Enable Connectors alongside [Agents](https://docs.mistral.ai/le-chat/knowledge-integrations/agents) so the Agent can pull data from your connected services when answering.

> [!warning]
> Libraries and knowledge Connectors (Google Drive, SharePoint) can't be used together on the same Agent. Other Connectors (Gmail, Google Calendar) work alongside either option.

## Data Privacy

| Connector Type | Behavior |
|----------------|----------|
| **Regular Connectors** (Gmail, Google Calendar, etc.) | Data fetched in real time. We don't store it on our servers. |
| **Knowledge Connectors** (Google Drive, SharePoint) | Files indexed and stored in European data centers. |

> [!info]
> Data accessed through Connectors is **never used to train or fine-tune our models**, regardless of your plan.

## Related

- [[144-le-chat-knowledge-integrations-connectors-knowledge-connectors|Knowledge Connectors]]: set up Google Drive and Microsoft SharePoint.
- [[145-le-chat-knowledge-integrations-connectors-mcp-connectors|MCP Connectors]]: browse the directory or connect your own MCP-compatible servers.
- [[147-le-chat-knowledge-integrations-libraries|Libraries]]: build knowledge bases from uploaded documents.
- [[142-le-chat-knowledge-integrations-agents|Agents]]: attach Connectors to Agents for context-aware assistants.

#le-chat #connectors #integration #oauth-authentication #data-privacy
