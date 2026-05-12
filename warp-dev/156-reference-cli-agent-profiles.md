---
title: Agent Profiles | Reference | Warp
url: https://docs.warp.dev/reference/cli/agent-profiles
source: sitemap
fetched_at: 2026-04-29T15:04:58.354833521-03:00
rendered_js: false
word_count: 149
summary: This document explains how to configure and use agent profiles in Warp to manage permissions, model settings, and execution scope for CLI-based agent tasks.
tags:
    - agent-profiles
    - warp-cli
    - permissions-management
    - mcp-servers
    - command-execution
category: guide
optimized: true
optimized_at: 2026-04-29T00:00:00Z
---
Agent profiles control three things:

- **What** — file access, command execution, MCP server usage
- **How** — model selection, autonomy level, response style
- **Where** — directory allowlists and denylists

Create and configure profiles in the Warp app (see [Agent Profiles & Permissions](https://docs.warp.dev/agent-platform/warp-agents/agent-profiles-permissions)). Profiles auto-sync to each host where Warp is installed.

> [!tip]
> For CLI usage, create a dedicated profile that allows the directories, commands, and MCP servers you plan to use. The CLI will fail if the agent tries to execute a prohibited action.

> [!warning]
> The default profile is broadly permissive (read/write files, apply diffs, execute commands with a default denylist). MCP servers are disabled by default.

> [!info]
> Cloud runs (`oz agent run-cloud`) do not use agent profiles.

## Use a profile with the CLI

1. Find the profile ID:

```bash
oz agent profile list
+--------------+------------------------+
| Name         | ID                     |
+--------------+------------------------+
| Default      | AnTb02PZfrkVC9l4V15eH1 |
| Coding      | CWhozDJPdPCsjJ1pSG0HCN |
| CommandLine | hV6n5dNm7ThQVlOiPF8DLS |
+--------------+------------------------+
```

2. Pass the ID with `--profile`:

```bash
oz agent run --profile CWhozDJPdPCsjJ1pSG0HCN --prompt "update my CI pipeline to use nextest"
```

#agent-profiles #warp-cli #permissions-management #mcp-servers #command-execution
