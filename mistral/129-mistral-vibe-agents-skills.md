---
title: Agents & Skills | Mistral Docs
url: https://docs.mistral.ai/mistral-vibe/agents-skills
source: sitemap
fetched_at: 2026-04-26T04:08:20.70718476-03:00
rendered_js: false
word_count: 469
summary: This document describes the architecture of Mistral Vibe, focusing on how to configure autonomous agents, utilize subagents for task delegation, and extend functionality through a modular skills system.
tags:
    - autonomous-agents
    - subagent-delegation
    - agent-skills
    - configuration-management
    - task-automation
category: concept
optimized: true
optimized_at: 2026-04-26T00:00:00Z
---

Build custom Agents for specific use cases and extend capabilities with Skills.

## Agents

Agents are autonomous entities capable of performing tasks, making decisions, and interacting with the environment. Mistral Vibe also supports `AGENTS.md` files in workspace roots.

### Selecting Agents

```bash
vibe --agent <agent_name>
```
Or use `Shift+Tab` in interactive mode.

### Built-in Agents

| Agent | Behavior |
|-------|----------|
| `default` | Requires approval for tool executions |
| `plan` | Read-only agent for exploration and planning (auto-approve) |
| `accept-edits` | Auto-approves file edits only |
| `auto-approve` | Auto-approves all tool executions |

### Built-in Subagents

| Subagent | Behavior |
|----------|----------|
| `explore` | Read-only subagent for codebase exploration |

### Custom Agents

Create profiles in `~/.vibe/agents/` as `.toml` files (see [[133-mistral-vibe-terminal-configuration|Configuration]]).

The `safety` field sets user input border color (visual only — does not implement safety measures):
- Pair with appropriate tool permissions: destructive agents = `destructive`, read-only = `safe`

## Subagents

Delegate tasks via the `task` tool:
- Subagents run independently, return results as text
- Useful for: parallel work, specialized tasks, safety (in-memory, no session logs)

> [!warning]
> Subagent limitations: cannot ask questions, results returned as text only.

## Interactive Questions

Agents can ask questions using `ask_user_question` tool:
- Multiple-choice or free-text input
- Displays as tabs for multi-question scenarios
- Automatically triggered when agent needs clarification

## Skills

Extend functionality through reusable components (tools, slash commands, specialized behaviors). Mistral Vibe follows the [Agent Skills specification](https://agentskills.io/specification).

### Skill Structure

Defined in directories with `SKILL.md` file containing YAML frontmatter metadata:
```
~/.vibe/skills/code-review/SKILL.md
```

### Skill Discovery

1. **Global skills**: `~/.vibe/skills/`
2. **Local project skills**: `.vibe/skills/` in your project
3. **Custom paths**: Configured in `config.toml`

Enable/disable skills with patterns (exact names, glob patterns, regex with `re:` prefix). #autonomous-agents #subagent-delegation #agent-skills