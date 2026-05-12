---
title: Memories
url: https://developers.openai.com/codex/memories.md
source: llms
fetched_at: 2026-04-30T10:15:50.8020128-03:00
rendered_js: false
word_count: 433
summary: This document explains how to enable, configure, and manage the Memories feature in Codex, which allows the assistant to maintain context across multiple user sessions.
tags:
    - codex
    - memories
    - context-management
    - configuration
    - feature-flags
    - data-privacy
category: configuration
optimized: true
optimized_at: 2026-04-30T13:30:00Z
---
# Memories

> [!info]
> Off by default. Not available in the European Economic Area, United Kingdom, or Switzerland at launch.

Memories let Codex carry useful context from earlier threads into future work: stable preferences, recurring workflows, tech stacks, project conventions, known pitfalls.

Keep required team guidance in `AGENTS.md` or checked-in documentation. Treat memories as a helpful local recall layer, not the only source for rules that must always apply.

[[031-memories-chronicle|Chronicle]] helps Codex recover recent working context from your screen to build up memory.

## Enable

In the Codex app: enable Memories in settings.

Config-based:
```toml
[features]
memories = true
```

See [[055-config-basic|Config basics]] for `config.toml` locations and loading.

## How memories work

After enabling, Codex can turn useful context from eligible prior threads into local memory files. Skips active or short-lived sessions, redacts secrets, and updates in the background instead of immediately at the end of every thread.

Updates may not happen right away — Codex waits until a thread has been idle long enough to avoid summarizing work still in progress.

Memory generation can also skip when your Codex rate-limit remaining percentage is below the configured threshold, so Codex doesn't spend quota when you're near a limit.

## Storage

Stored under your Codex home directory (default `~/.codex`). See [[054-config-advanced#config-and-state-locations|Config and state locations]] for `CODEX_HOME` usage.

Main memory files under `~/.codex/memories/` include summaries, durable entries, recent inputs, and supporting evidence from prior threads.

Treat as generated state. You can inspect them when troubleshooting or before sharing your Codex home directory, but don't rely on editing by hand as the primary control surface.

## Control per thread

In the Codex app and TUI, use `/memories` to control memory behavior for the current thread:
- Whether the thread can use existing memories
- Whether Codex can use the thread to generate future memories

Thread-level choices don't change global settings.

## Configuration

Enable in app settings or set `memories = true` in `[features]`.

Common memory-specific settings (see [[067-config-reference|configuration reference]] for full list):

| Setting | Description |
|---------|-------------|
| `memories.generate_memories` | Whether new threads can be stored as memory-generation inputs |
| `memories.use_memories` | Whether Codex injects existing memories into future sessions |
| `memories.disable_on_external_context` | Keep threads using MCP/web search/tool search out of memory generation. Legacy alias: `no_memories_if_mcp_or_web_search` |
| `memories.min_rate_limit_remaining_percent` | Minimum remaining rate-limit % before memory generation starts |
| `memories.extract_model` | Model for per-thread memory extraction |
| `memories.consolidation_model` | Model for global memory consolidation |

## Review memories

Don't store secrets. Codex redacts secrets from generated memory fields, but review memory files before sharing your Codex home directory or generated artifacts.

#memories #context #configuration #privacy #codex