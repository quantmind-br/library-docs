---
title: Profiles & permissions | Agents | Warp
url: https://docs.warp.dev/agent-platform/warp-agents/capabilities-overview/agent-profiles-permissions
source: sitemap
fetched_at: 2026-04-29T15:03:55.371770778-03:00
rendered_js: false
word_count: 522
summary: This document explains how to configure Agent Profiles and permissions to manage autonomy, tool access, and command execution security. It details how to set up allowlists, denylists, and autonomous operation modes for intelligent agents.
tags:
    - agent-configuration
    - permissions-management
    - automation-security
    - command-allowlist
    - command-denylist
    - mcp-servers
category: guide
optimized: true
optimized_at: 2026-04-29T18:00:00Z
---
Agent Profiles configure how your Agent behaves. Configure in **Settings** → **Agents** → **Profiles**.

## Agent Profiles

| Profile Type | Description |
|--------------|-------------|
| **Default** | Every user starts with one; new profiles copy its settings |
| **Custom** | Different profiles for different workflows (e.g., "Safe & cautious", "YOLO mode") |

**Each profile configures:**
- Profile name
- **Base model** — core engine for most interactions; invokes other models as needed (e.g., code generation)
- Agent autonomy and permissions

> [!tip]
> You can configure a separate planning model, or use the base model by default. See [Planning](https://docs.warp.dev/agent-platform/warp-agents/capabilities-overview/planning).

## Agent Permissions

Configure in **Settings** → **Agents** → **Profiles** → **Permissions**. Control autonomy per action type:

| Permission | Always Ask | Agent Decides | Always Allow |
|------------|------------|---------------|--------------|
| Apply code diffs | Prompts for review | Prompts for review | Auto-apply |
| Read files | Prompts | Autonomous | Autonomous |
| Create plans | Prompts | Autonomous | Autonomous |
| Execute commands | Prompts | Autonomous | Autonomous |

> [!warning]
> **Still getting approval prompts?** Check your **Command denylist** in **Settings** → **Agents** → **Profiles**. The denylist always takes precedence. Remove commands from the denylist to allow auto-execution, or use [Run until completion](#run-until-completion) to bypass for the current task.

When all permissions are **Always allow**, the Agent has full autonomy ("YOLO mode")—denylist rules still apply.

## Command allowlist

Commands that auto-execute without confirmation. Empty by default. Example entries:

| Regex | Purpose |
|-------|---------|
| `which .*` | Find executable locations |
| `ls(\s.*)?` | List directory contents |
| `grep(\s.*)?` | Search file contents |
| `find .*` | Search for files |
| `echo(\s.*)?` | Print text output |

Add custom regex in **Settings** → **Agents** → **Profiles** → **Command allowlist**. Allowlist commands always auto-execute, even if not read-only.

## Command denylist

Commands that always require confirmation. Default entries:

| Regex | Purpose |
|-------|---------|
| `wget(\s.*)?` | Network downloads |
| `curl(\s.*)?` | Network requests |
| `rm(\s.*)?` | File deletion |
| `eval(\s.*)?` | Shell code execution |

> [!danger]
> The denylist takes precedence over both the allowlist and `Agent decides`. Add custom regex in **Settings** → **Agents** → **Profiles** → **Command denylist**.

## MCP permissions

Configure which MCP servers the Agent can call in **Settings** → **Agents** → **Profiles** → **MCP Permissions**:

| Setting | Behavior |
|---------|----------|
| **Allowlist** | Agent calls specific servers without asking |
| **Denylist** | Requires approval before calling certain servers |
| **Agent decides** | Autonomous when confident, asks when uncertain |

## Run until completion

Give the Agent full autonomy for the current task. When active, every command runs immediately until the task finishes or you stop with `Ctrl + C`.

**Shortcut:** `CMD + SHIFT + I`

> [!warning]
> *Run until completion* ignores the denylist entirely—pure "YOLO" mode where the Agent proceeds without confirmation.

## Next steps

- [**Planning**](https://docs.warp.dev/agent-platform/warp-agents/capabilities-overview/planning) — break down complex tasks into structured plans
- [**Code diffs**](https://docs.warp.dev/agent-platform/warp-agents/interacting-with-agents/code-diffs) — review and apply agent-generated changes
- [**Interactive Code Review**](https://docs.warp.dev/agent-platform/warp-agents/interactive-code-review) — leave inline comments and have the agent address feedback