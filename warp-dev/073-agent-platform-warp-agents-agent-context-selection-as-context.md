---
title: Selection as context | Agents | Warp
url: https://docs.warp.dev/agent-platform/warp-agents/agent-context/selection-as-context
source: sitemap
fetched_at: 2026-04-29T15:04:07.406342984-03:00
rendered_js: false
word_count: 247
summary: This document explains how to attach specific code snippets, file selections, and diff hunks from Warp's editor and review tools as context for AI agent sessions.
tags:
    - warp-terminal
    - ai-agent
    - context-injection
    - code-editor
    - developer-productivity
category: guide
optimized: true
optimized_at: 2026-04-29T00:00:00Z
---
# Selection as Context

Attach code snippets, file selections, and diff hunks as context for AI agent sessions using Warp's built-in tools.

## Attaching Selections from Warp's Native Code Editor

When Warp's [native code editor](https://docs.warp.dev/code/code-editor/) is open beside a regular pane:

1. **Select text** in the editor — a tooltip appears in the bottom-right corner
2. **Add as context** by clicking the tooltip or using `Cmd + L` (macOS) / `CTRL + SHIFT + L` (Windows/Linux)
3. Warp automatically adds the relative file path, context, and line numbers as a formatted string into the prompt

## Attaching Selections from Warp's Code Review Panel

Attach context directly from the [Code Review panel](https://docs.warp.dev/code/code-review/):

1. Hover over any **diff hunk** to reveal the option to attach it as context
2. Attaching a diff inserts the relevant file path and changed lines into your prompt

This helps the Agent understand exactly what was modified, making it easier to request explanations, feedback, or follow-up edits.

## Attaching Code to a Third-Party Agent Session

Feed code, files, or snippets to a running third-party CLI agent session without copy-pasting.

When a third-party agent (Claude Code, Codex, OpenCode, etc.) is running in a Warp tab:
- Select text in Warp's code editor or Code Review panel
- Attach it as context using `Cmd + L` (macOS) / `CTRL + SHIFT + L` (Windows/Linux)

This works the same way as attaching context to Warp's built-in Agent.

For more on third-party agent support, see [Third-Party CLI Agents](https://docs.warp.dev/agent-platform/third-party-agents/overview).
