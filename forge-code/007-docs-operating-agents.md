---
title: "Operating Agents in ForgeCode"
url: https://forgecode.dev/docs/operating-agents/
source: sitemap
fetched_at: 2026-04-30T14:09:13.677005273-03:00
rendered_js: false
word_count: 217
summary: "Choose the right ForgeCode agent for your task: muse (planning), forge (implementation), or sage (research)."
tags:
  - forgecode
  - agent-management
  - workflow-optimization
  - software-development
  - ai-tools
category: guide
optimized: true
---
# Operating Agents in ForgeCode

> **TL;DR**
> Use `:agent` to switch between `muse` (planning), `forge` (implementation), and custom agents.

## Agent Overview

| Agent | Access | Purpose | Best For |
|-------|--------|---------|----------|
| `muse` | Read + Write | Planning & analysis | Refactoring, impact review |
| `forge` | Read + Write | Implementation | Bug fixes, feature dev |
| `sage` | Read | Research | Codebase understanding |

> **Workflow**: `muse` → plan → `forge` → implement.

## Switching Agents

1. Type `:agent`
2. Select with ↑/↓ + Enter

> **Tip**: Use `:muse` or `:forge` for direct access.

## When to Use Each

| Agent | Use Case | Example Prompts |
|-------|---------|------------------|
| `muse` | Planning, analysis | "How would you redesign this API?" |
| `forge` | Implementation | "Fix the null pointer in UserService" |
| `sage` | Research (auto-used) | N/A (internal) |

## Pro Tips
- **Context preserved**: Switch agents without losing history.
- **Combine with models**: Use `:model` to tune intelligence.
- **Version control**: Commit before major `forge` changes.

## Common Patterns
1. **Plan first**: Use `muse` for critical systems.
2. **Implement**: Switch to `forge` for execution.
3. **Research**: `sage` is auto-invoked as needed.

## Related Guides
- [Plan and Act Guide](https://forgecode.dev/docs/plan-and-act-guide/)
- [Model Selection Guide](https://forgecode.dev/docs/model-selection-guide/)