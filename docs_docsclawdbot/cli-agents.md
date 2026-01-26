---
title: "null"
url: https://docs.clawd.bot/cli/agents.md
source: llms
fetched_at: 2026-01-26T09:50:32.176432877-03:00
rendered_js: false
word_count: 103
summary: This document provides instructions and command examples for managing isolated agent workspaces and configuring their identities via the clawdbot CLI.
tags:
    - clawdbot-cli
    - agent-management
    - workspace-configuration
    - identity-setup
    - command-line-interface
category: reference
---

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.clawd.bot/llms.txt
> Use this file to discover all available pages before exploring further.

# null

# `clawdbot agents`

Manage isolated agents (workspaces + auth + routing).

Related:

* Multi-agent routing: [Multi-Agent Routing](/concepts/multi-agent)
* Agent workspace: [Agent workspace](/concepts/agent-workspace)

## Examples

```bash  theme={null}
clawdbot agents list
clawdbot agents add work --workspace ~/clawd-work
clawdbot agents set-identity --workspace ~/clawd --from-identity
clawdbot agents set-identity --agent main --avatar avatars/clawd.png
clawdbot agents delete work
```

## Identity files

Each agent workspace can include an `IDENTITY.md` at the workspace root:

* Example path: `~/clawd/IDENTITY.md`
* `set-identity --from-identity` reads from the workspace root (or an explicit `--identity-file`)

Avatar paths resolve relative to the workspace root.

## Set identity

`set-identity` writes fields into `agents.list[].identity`:

* `name`
* `theme`
* `emoji`
* `avatar` (workspace-relative path, http(s) URL, or data URI)

Load from `IDENTITY.md`:

```bash  theme={null}
clawdbot agents set-identity --workspace ~/clawd --from-identity
```

Override fields explicitly:

```bash  theme={null}
clawdbot agents set-identity --agent main --name "Clawd" --emoji "🦞" --avatar avatars/clawd.png
```

Config sample:

```json5  theme={null}
{
  agents: {
    list: [
      {
        id: "main",
        identity: {
          name: "Clawd",
          theme: "space lobster",
          emoji: "🦞",
          avatar: "avatars/clawd.png"
        }
      }
    ]
  }
}
```