---
title: Getting started with Warp and Oz | Warp
url: https://docs.warp.dev
source: sitemap
fetched_at: 2026-04-29T15:01:59.715967599-03:00
rendered_js: false
word_count: 355
summary: Warp is an agentic development environment that integrates a high-performance terminal with AI agents powered by the Oz orchestration platform. It supports both local interactive coding and automated cloud-based workflows through a unified, multi-model infrastructure.
tags:
    - agentic-development
    - terminal-emulator
    - ai-orchestration
    - workflow-automation
    - dev-tools
    - cloud-agents
category: concept
optimized: true
optimized_at: 2026-04-29T00:00:00Z
---
Warp is an [open source](https://github.com/warpdotdev/warp) **Agentic Development Environment**: a modern terminal combined with agents that help you build, test, deploy, and debug code. Warp's AI is powered by **Oz**, the orchestration platform for cloud agents.

## Warp

Warp is a fast, modern terminal built for coding with agents.

**Key capabilities:**

- [**Modern terminal UX**](https://docs.warp.dev/terminal/editor): cursor movement, block-based navigation, multi-line editing, syntax highlighting, rich completions. Built with Rust.
- [**Code editor**](https://docs.warp.dev/code/overview): file tree, LSP support, interactive code review.
- [**Third-party CLI agents**](https://docs.warp.dev/agent-platform/third-party-agents): run Claude Code, Codex, OpenCode with Warp's agent toolbelt.

→ [Get started with local agents](https://docs.warp.dev/agent-platform/warp-agents)

## Oz: Orchestration platform for cloud agents

Oz coordinates agents at scale—understanding your codebase, executing tasks autonomously, adapting to workflows. Oz is multi-model by design.

### Local agents

Run directly in the Warp app for real-time, interactive coding assistance:

- Write and refactor code across your codebase
- Debug issues and fix errors
- Run commands and interpret results
- Plan and execute multi-step tasks

### Cloud agents

Oz Cloud Agents run in the background on Warp's infrastructure (or your own):

- **Triggers**: react to events from Slack, Linear, GitHub, or custom webhooks
- **Schedules**: recurring tasks like dependency updates or dead code removal
- **Parallelism**: many agents concurrently across repos or tasks
- **Observability**: every run is tracked, auditable, shareable

→ [Learn about cloud agents](https://docs.warp.dev/agent-platform/cloud-agents/overview)

## How they work together

- **Same agent, anywhere**: interactive in Warp or cloud—same underlying capabilities
- **Seamless handoff**: start in cloud, take over locally without losing context
- **Team collaboration**: share sessions, review actions, steer running tasks

## Multi-model support

[Choose your preferred LLM](https://docs.warp.dev/agent-platform/warp-agents/model-choice) from a curated set of top models.

## Open source

Warp's client is open source under [AGPL v3](https://github.com/warpdotdev/warp/blob/master/LICENSE). Development happens in the open with an agent-first workflow managed by Oz.

→ [Contributing to Warp](https://docs.warp.dev/support-and-community/community/contributing)

## Privacy and security

- Warp is **SOC 2 compliant**
- **Zero Data Retention** with all contracted LLM providers
- No customer AI data retained, stored, or used for training

Disable AI features globally in **Settings** > **Agents** > **Warp Agent**.

→ [Data privacy](https://www.warp.dev/privacy)

## Next steps

- [**Quickstart**](https://docs.warp.dev/getting-started/quickstart): install Warp and start coding
