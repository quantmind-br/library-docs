---
title: Set Coding Preferences with Rules | Guides | Warp
url: https://docs.warp.dev/guides/configuration/how-to-set-coding-preferences-with-rules
source: sitemap
fetched_at: 2026-04-29T15:06:33.568380709-03:00
rendered_js: false
word_count: 143
summary: This document explains how to configure persistent rules in Warp to standardize environment preferences and tool usage for AI-assisted coding sessions.
tags:
    - warp-terminal
    - ai-agent
    - environment-configuration
    - development-setup
    - productivity-tools
    - workflow-automation
category: tutorial
optimized: true
optimized_at: 2026-04-29T00:00:00Z
---
Learn how to use Warp's Rules to define your personal environment and tool preferences for every coding session.

## The Problem

When using AI tools to write or modify code, they often default to outdated or undesired tools. For example, many agents still use **npm** instead of **pnpm** — or **pip** instead of **miniconda**.

Warp fixes this by letting you define preferences once, then applying them automatically whenever your agent runs.

## The Rule Setup

Set Rules for how the AI should handle environments, dependencies, and commands.

**Example Rule:**

```
Rule: Environment Preferences
- Always use pnpm for Node.js projects unless the project already uses npm.
- Default to miniconda for Python environments.
- Use the Tauri CLI when building desktop apps.
```

This ensures the agent automatically chooses the right package manager or environment — no extra prompts required.

## Supported Use Cases

You can apply Rules to:

- Package managers (e.g., npm → pnpm)
- Environment tools (e.g., virtualenv → miniconda)
- Framework defaults (e.g., Next.js over React)
- CLI utilities or custom build tools
