---
title: Edit Agent-Generated Code in Warp | Guides | Warp
url: https://docs.warp.dev/guides/agent-workflows/how-to-edit-agent-code-in-warp
source: sitemap
fetched_at: 2026-04-29T15:06:27.201921194-03:00
rendered_js: false
word_count: 189
summary: This document outlines the workflow for using Warp to manage AI-driven code modifications, from initiating agent tasks and reviewing diffs to verifying code fixes.
tags:
    - ai-coding-assistant
    - code-diffs
    - workflow-automation
    - debugging-tools
    - developer-productivity
category: guide
optimized: true
optimized_at: 2026-04-29T00:00:00Z
---
Warp lets you see, edit, and refine AI-generated code diffs directly within the app, making debugging fast and transparent.

## Starting an Agent Task

When you start an agent task, Warp:

1. Uses your prompt and context to build a task list
2. Searches across your codebase using Grep, codebase embeddings, and semantic search
3. Shows progress step-by-step, including which files are being modified

## Reviewing Diffs

Warp generates diffs for every proposed change. You can:

- **Accept** changes
- **Refine** them with a follow-up prompt (`Cmd + R`)
- **Directly edit** in the inline editor view (a lightweight IDE for quick corrections)

## Applying or Skipping Changes

Once satisfied with a diff:

- Click **Apply Changes** to accept it
- Click **Fast-Forward** to let Warp automatically continue the rest of the fix sequence

Control autonomy globally at **Settings → AI → Autonomy**.

## Compiling and Verifying Fixes

After applying changes, immediately test your build. Warp monitors compilation, verifies results, and runs post-checks automatically.

## Visual Verification

After the agent's fix, verify the UI behaves as expected — e.g., checkbox logic works, model picker toggles correctly, UI renders correctly.
