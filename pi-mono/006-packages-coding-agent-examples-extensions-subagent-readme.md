---
title: Subagent Extension
url: https://github.com/badlogic/pi-mono/blob/main/packages/coding-agent/examples/extensions/subagent/README.md
source: git
fetched_at: 2026-05-03T09:31:44.756263323-03:00
optimized: true
word_count: 461
summary: Delegate tasks to specialized subagents with isolated context windows, parallel processing, chained workflows, and project-specific configurations.
tags:
    - subagent
    - ai-agents
    - workflow-automation
    - parallel-processing
    - agent-framework
category: configuration
---
# Subagent Extension

Delegate tasks to specialized subagents with isolated context windows.

## Features

- **Isolated context**: Each subagent runs in separate `pi` process
- **Streaming output**: See tool calls and progress live
- **Parallel streaming**: All parallel tasks stream simultaneously
- **Markdown rendering**: Formatted final output
- **Usage tracking**: Turns, tokens, cost, context per agent
- **Abort support**: Ctrl+C propagates to kill subagents

## Structure

```
subagent/
├── index.ts             # Extension entry point
├── agents.ts            # Agent discovery logic
├── agents/              # Sample agent definitions
│   ├── scout.md         # Fast recon, compressed context
│   ├── planner.md       # Implementation plans
│   ├── reviewer.md      # Code review
│   └── worker.md        # General-purpose
└── prompts/             # Workflow presets
    ├── implement.md     # scout → planner → worker
    ├── scout-and-plan.md # scout → planner
    └── implement-and-review.md  # worker → reviewer → worker
```

## Installation

```bash
# Symlink extension
mkdir -p ~/.pi/agent/extensions/subagent
ln -sf "$(pwd)/packages/coding-agent/examples/extensions/subagent/index.ts" ~/.pi/agent/extensions/subagent/index.ts
ln -sf "$(pwd)/packages/coding-agent/examples/extensions/subagent/agents.ts" ~/.pi/agent/extensions/subagent/agents.ts

# Symlink agents
mkdir -p ~/.pi/agent/agents
for f in packages/coding-agent/examples/extensions/subagent/agents/*.md; do
  ln -sf "$(pwd)/$f" ~/.pi/agent/agents/$(basename "$f")
done

# Symlink workflow prompts
mkdir -p ~/.pi/agent/prompts
for f in packages/coding-agent/examples/extensions/subagent/prompts/*.md; do
  ln -sf "$(pwd)/$f" ~/.pi/agent/prompts/$(basename "$f")
done
```

## Security Model

> [!WARNING]
> **Project-local agents** (`.pi/agents/*.md`) are repo-controlled prompts. Only enable for trusted repositories.

- **Default**: Only loads user-level agents from `~/.pi/agent/agents/`
- **With `agentScope: "both"`**: Also loads project-local agents
- **Interactive confirmation** prompts before running project-local agents (set `confirmProjectAgents: false` to disable)

## Usage

### Natural Language

```
Use scout to find all authentication code
Run 2 scouts in parallel: one to find models, one to find providers
Use a chain: first have scout find the read tool, then have planner suggest improvements
/implement add Redis caching to the session store
/scout-and-plan refactor auth to support OAuth
/implement-and-review add input validation to API endpoints
```

### Tool Modes

| Mode | Parameter | Description |
|------|-----------|-------------|
| Single | `{ agent, task }` | One agent, one task |
| Parallel | `{ tasks: [...] }` | Multiple concurrent (max 8, 4 concurrent) |
| Chain | `{ chain: [...] }` | Sequential with `{previous}` placeholder |

## Output Display

**Collapsed** (default):
- Status icon (✓/✗/⏳) + agent name
- Last 5-10 items (tool calls, text)
- Usage: `3 turns ↑input ↓output RcacheRead WcacheWrite $cost ctx:contextTokens model`

**Expanded** (Ctrl+O):
- Full task text
- All tool calls with formatted args
- Final Markdown output
- Per-task usage for chain/parallel

**Parallel streaming**: Live status updates (⏳ running, ✓ done, ✗ failed)

**Tool formatting**:
- `$ command` for bash
- `read ~/path:1-10` for read
- `grep /pattern/ in ~/path` for grep

## Agent Definitions

Agents are markdown with YAML frontmatter:

```markdown
---
name: my-agent
description: What this agent does
tools: read, grep, find, ls
model: claude-haiku-4-5
---

System prompt for the agent goes here.
```

**Locations**:
- `~/.pi/agent/agents/*.md` - User-level (always loaded)
- `.pi/agents/*.md` - Project-level (only with `agentScope: "project"` or `"both"`)

Project agents override user agents with same name when `agentScope: "both"`.

## Sample Agents

| Agent | Purpose | Model | Tools |
|-------|---------|-------|-------|
| `scout` | Fast recon | Haiku | read, grep, find, ls, bash |
| `planner` | Plans | Sonnet | read, grep, find, ls |
| `reviewer` | Review | Sonnet | read, grep, find, ls, bash |
| `worker` | General | Sonnet | (all default) |

## Workflow Prompts

| Prompt | Flow |
|--------|------|
| `/implement <query>` | scout → planner → worker |
| `/scout-and-plan <query>` | scout → planner |
| `/implement-and-review <query>` | worker → reviewer → worker |

## Error Handling

| Scenario | Behavior |
|----------|----------|
| Exit code != 0 | Returns error with stderr/output |
| `stopReason "error"` | Propagates with error message |
| `stopReason "aborted"` | Kills subprocess, throws error |
| Chain mode failure | Stops at first failing step |

## Limitations

- Collapsed view: last 10 items only
- Agents discovered fresh per invocation
- Parallel mode: max 8 tasks, 4 concurrent
