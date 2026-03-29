---
title: Agents - OpenClaw
url: https://docs.openclaw.ai/cli/agents
source: sitemap
fetched_at: 2026-01-30T20:36:02.724741556-03:00
rendered_js: false
word_count: 79
summary: This document explains how to manage isolated agents including workspace configuration, authentication, and identity settings within the OpenClaw system.
tags:
    - agent-management
    - workspace-configuration
    - identity-settings
    - multi-agent
    - agent-workspace
    - authentication
category: guide
---

Manage isolated agents (workspaces + auth + routing). Related:

- Multi-agent routing: [Multi-Agent Routing](https://docs.openclaw.ai/concepts/multi-agent)
- Agent workspace: [Agent workspace](https://docs.openclaw.ai/concepts/agent-workspace)

## Examples

```
openclaw agents list
openclaw agents add work --workspace ~/.openclaw/workspace-work
openclaw agents set-identity --workspace ~/.openclaw/workspace --from-identity
openclaw agents set-identity --agent main --avatar avatars/openclaw.png
openclaw agents delete work
```

## Identity files

Each agent workspace can include an `IDENTITY.md` at the workspace root:

- Example path: `~/.openclaw/workspace/IDENTITY.md`
- `set-identity --from-identity` reads from the workspace root (or an explicit `--identity-file`)

Avatar paths resolve relative to the workspace root.

## Set identity

`set-identity` writes fields into `agents.list[].identity`:

- `name`
- `theme`
- `emoji`
- `avatar` (workspace-relative path, http(s) URL, or data URI)

Load from `IDENTITY.md`:

```
openclaw agents set-identity --workspace ~/.openclaw/workspace --from-identity
```

Override fields explicitly:

```
openclaw agents set-identity --agent main --name "OpenClaw" --emoji "🦞" --avatar avatars/openclaw.png
```

Config sample:

```
{
  agents: {
    list: [
      {
        id: "main",
        identity: {
          name: "OpenClaw",
          theme: "space lobster",
          emoji: "🦞",
          avatar: "avatars/openclaw.png"
        }
      }
    ]
  }
}
```