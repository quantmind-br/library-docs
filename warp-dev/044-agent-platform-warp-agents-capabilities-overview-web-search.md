---
title: Web search | Agents | Warp
url: https://docs.warp.dev/agent-platform/warp-agents/capabilities-overview/web-search
source: sitemap
fetched_at: 2026-04-29T15:03:58.6031718-03:00
rendered_js: false
word_count: 383
summary: This document explains how to utilize and configure the native web search functionality in Warp agents to improve response accuracy through real-time information retrieval.
tags:
    - web-search
    - warp-agents
    - ai-models
    - search-configuration
    - agent-tools
    - citation-tracking
category: guide
optimized: true
optimized_at: 2026-04-29T00:00:00Z
---
Warp includes native web search for models that support first-party search tools. When enabled, agents can look up information in real time, consult documentation, retrieve current version numbers, and cite the sources used to generate responses.

## When the Agent uses web search

Models initiate a web search when it improves answer quality or accuracy. **Common scenarios include:**

- Retrieving official documentation or API references
- Getting the latest version of a library or tool
- Checking error messages, GitHub issues, or StackOverflow discussions
- Looking up ongoing incidents or recent changes
- Answering questions where recency matters (e.g., "best approach in 2025 to…")

Web searches are automatically triggered when the model considers them useful. No special syntax required.

## How web search works in Warp

When a search occurs:

1. Warp shows a "Searching the web…" indicator inside the conversation.
2. Expand the search result to view the query issued and pages retrieved.
3. **The model reads results and produces a grounded response.**
   - Claude models cite sources in the references footer.
   - OpenAI models use inline citations and show references in the footer.

## Supported and unsupported models

Web search is available only for models with native web search integration.

**Supported models:**

- **Anthropic:** `Claude 4.6 Series`, `Claude 4.5 Series`, `Claude 4 Series`
- **OpenAI:** `GPT-5.4`, `GPT-5.3 Codex`, `GPT-5.2 Codex`, `GPT-5.2`

> [!note]
> Additional models will be added as their APIs support it.

## Viewing search results

Inspect the web search UI at any time:

- Expand the **Web Search** section in the agent response
- See the list of pages fetched, text used to answer, and citation metadata

This enables verifying accuracy, auditing reasoning, and validating sources.

## Enabling or disabling web search

Web search is controlled per [[035-agent-platform-warp-agents-capabilities-overview-agent-profiles-permissions|Profiles & Permissions]].

To configure:

1. Navigate to **Settings** > **Agents** > **Profiles**.
2. Click **Edit** next to the agent profile.
3. Scroll to **Call web tools** and toggle the setting.

Disabling prevents the agent from performing searches, even if a model would normally use them.

## Credit usage

Web search incurs:

1. A small fixed cost per search invocation
2. Additional cost proportional to retrieved content (passed to the model)

These appear itemized in the conversation's credit usage footer alongside model calls, planning calls, and other tool usage. #web-search #warp-agents