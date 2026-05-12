---
title: URLs as context | Agents | Warp
url: https://docs.warp.dev/agent-platform/warp-agents/agent-context/urls-as-context
source: sitemap
fetched_at: 2026-04-29T15:04:07.075375639-03:00
rendered_js: false
word_count: 87
summary: This document explains how to provide webpage content as context for AI prompts by attaching public URLs to the Warp agent.
tags:
    - warp-agent
    - url-context
    - web-scraping
    - prompt-engineering
    - data-input
category: guide
optimized: true
optimized_at: 2026-04-29T00:00:00Z
---
Attach a public URL to any prompt to feed page content directly into the model as context.

- Only publicly accessible pages are supported.
- The full page is added to the model's context, increasing credit usage for long documents.
- Only the specific URL provided is processed — no crawling or link-following.

> [!warning]
> URL attachments differ from web search. For real-time lookups, multiple sources, or broad discovery, use [[044-agent-platform-warp-agents-capabilities-overview-web-search|Web Search]] instead.

## Referencing websites via URLs

![](https://docs.warp.dev/~gitbook/image?url=https%3A%2F%2F769506432-files.gitbook.io%2F~%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FAULCelT4yIUOcSwWWvPk%252Fuploads%252Fgit-blob-176c44d1b3c99c2e2f5dbc7b87ff754a9fa38c26%252Furl-as-context.png%3Falt%3Dmedia&width=768&dpr=3&quality=100&sign=8f9744eb&sv=2)

Example of referencing docs via a URL
