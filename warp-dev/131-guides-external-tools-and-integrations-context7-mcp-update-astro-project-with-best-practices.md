---
title: 'Context7 MCP: Update with Best Practices | Guides | Warp'
url: https://docs.warp.dev/guides/external-tools-and-integrations/context7-mcp-update-astro-project-with-best-practices
source: sitemap
fetched_at: 2026-04-29T15:06:58.722123954-03:00
rendered_js: false
word_count: 139
summary: This document explains how to integrate the Context7 MCP server with Warp to automate codebase updates and migrations using live, web-based documentation.
tags:
    - mcp-server
    - warp-terminal
    - code-migration
    - astro-framework
    - automated-refactoring
    - documentation-retrieval
category: guide
optimized: true
optimized_at: 2026-04-29T15:06:58.722123954-03:00
---
The **Context7 MCP Server** fetches live documentation from across the web. In this example, the agent updates an older **Astro** project to align with Astro 5.

## Add the Context7 Server

1. Open Warp's **MCP Panel** via the Command Palette.
2. Add the **Context7 JSON config** and click **Save**.

```json
{
  "Context7": {
    "command": "npx",
    "args": [
      "-y",
      "@upstash/context7-mcp"
    ],
    "env": {},
    "working_directory": null
  }
}
```

This enables the endpoint `getLibraryDocs`, which retrieves live documentation directly from official sources.

## Run the Update Prompt

```
Create a new git branch called update and in that branch update this Astro project to follow all the latest best practices based on all Astro and developer documentation.
```

## Review the Automatic Code Changes

The transcript shows Warp automatically:

- Updates Tailwind import syntax
- Improves TypeScript configuration
- Optimizes build settings
- Enhances accessibility rules

These edits happen across multiple files without manually searching docs or changelogs.

## Best Use Cases

- Migrating old Astro, React, or Vue projects
- Refreshing codebases to reflect recent standards
- Saving time otherwise spent reading version notes

#mcp-server #warp-terminal #code-migration #astro-framework #automated-refactoring
