---
title: Codex IDE extension features
url: https://developers.openai.com/codex/ide/features.md
source: llms
fetched_at: 2026-04-30T10:15:42.592273064-03:00
rendered_js: false
word_count: 508
summary: This document provides an overview of the features and functionality available in the Codex IDE extension, including model selection, agent settings, cloud task management, and integrated AI tools.
tags:
    - codex
    - ide-extension
    - ai-assistant
    - cloud-delegation
    - image-generation
    - web-search
category: guide
optimized: true
optimized_at: 2026-04-30T13:30:00Z
---
# Codex IDE extension features

Access Codex directly in VS Code, Cursor, Windsurf, and other VS Code-compatible editors. Uses the same agent as the Codex CLI and shares configuration.

## Prompting Codex

Chat, edit, and preview changes seamlessly. When Codex has context from open files and selected code, you can write shorter prompts and get faster, more relevant results.

Reference any file by tagging it in your prompt:
```text
Use @example.tsx as a reference to add a new page named "Resources" to the app that contains a list of resources defined in @resources.ts
```

## Switch between models

Use the switcher under the chat input.

## Adjust reasoning effort

Control how long Codex thinks before responding. Higher effort helps on complex tasks but takes longer, uses more tokens, and consumes rate limits faster — especially with higher-capability models.

Choose `low`, `medium`, or `high` in the model switcher. Start with `medium`; switch to `high` only when you need more depth.

## Choose an approval mode

| Mode | Behavior |
|------|----------|
| **Agent** (default) | Read files, make edits, run commands in working directory automatically. Needs approval for outside workspace or network access. |
| **Chat** | Just chat or plan before making changes. |
| **Agent (Full Access)** | Read, edit, run commands with network access without approval. Use with caution. |

## Cloud delegation

Offload larger jobs to Codex Cloud, then track progress and review results without leaving your IDE.

1. Set up a [cloud environment](https://chatgpt.com/codex/settings/environments).
2. Pick your environment and select **Run in the cloud**.

You can run from `main` (useful for starting new ideas) or from local changes (useful for finishing a task). When starting from a local conversation, Codex retains context.

## Cloud task follow-up

Preview cloud changes, ask for follow-ups, and apply resulting diffs locally to test and finish. Codex retains context when you continue locally. View cloud tasks at [chatgpt.com/codex](https://chatgpt.com/codex).

## Web search

First-party web search tool enabled by default for local tasks. Serves results from an OpenAI-maintained web search cache (pre-indexed results, not live pages). Reduces exposure to prompt injection from arbitrary live content, but still treat results as untrusted.

If sandbox is configured for [[041-agent-approvals-security|full access]], web search defaults to live results. See [[055-config-basic|Config basics]] to disable web search or switch to live results.

`web_search` items appear in transcript or `codex exec --json` output whenever Codex looks something up.

## Drag and drop images

Drag and drop images into the prompt composer. Hold `Shift` while dropping — VS Code otherwise prevents extensions from accepting drops.

## Image generation

Generate or edit images without leaving your editor. Useful for UI assets, layouts, illustrations, sprite sheets, and placeholders. Add a reference image to transform or extend an existing asset.

Ask in natural language or include `$imagegen` in your prompt.

Built-in image generation uses `gpt-image-2`, counts toward general Codex usage limits, and consumes included limits 3-5x faster on average than similar turns without image generation (depending on quality and size). See [[075-pricing|Pricing]] and [image generation guide](https://developers.openai.com/api/docs/guides/image-generation).

For larger batches, set `OPENAI_API_KEY` in environment variables and ask Codex to generate images through the API so API pricing applies.

## See also

- [[057-ide-settings|Codex IDE extension settings]]

#ide #vscode #features #codex