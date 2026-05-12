---
title: Rules | Agents | Warp
url: https://docs.warp.dev/agent-platform/warp-agents/capabilities-overview/rules
source: sitemap
fetched_at: 2026-04-29T15:03:53.131143503-03:00
rendered_js: false
word_count: 430
summary: This document explains how to configure and manage Global and Project rules in Warp to influence agent behavior and ensure coding standard consistency.
tags:
    - warp-agents
    - prompt-engineering
    - project-configuration
    - coding-standards
    - ai-assistant
    - workflow-automation
category: guide
optimized: true
optimized_at: 2026-04-29T00:00:00Z
---
Rules are reusable guidelines that inform how agents respond to prompts. They tailor responses to match your coding standards, project conventions, and personal preferences.

## Global Rules

Global Rules apply across all projects and contexts. Ideal for:

- Coding standards and best practices
- Workspace-wide guidelines
- Tool configurations or preferences you want applied everywhere

Warp may also suggest Global Rules based on your usage patterns.

## Project Rules

Project Rules live in your codebase and apply automatically when working within that project. Stored in an `AGENTS.md` file (or `WARP.md` for backwards compatibility).

| File | Behavior |
|------|----------|
| `AGENTS.md` | Default project rules file |
| `WARP.md` | Still fully supported; if both exist in same directory, `WARP.md` takes priority |

> [!warning]
> The filename must be in **all caps** (e.g., `AGENTS.md`, not `agents.md` or `Agents.md`). Recommended for new projects.

**File locations:**

- Root of your repository
- Subdirectories for more targeted guidance

**When you're in a directory:**

- Warp automatically applies `AGENTS.md` (or `WARP.md`) in the root and current directory
- Best-effort include of subdirectory rules when editing files there

**Example project structure:**

```
project/
├── AGENTS.md          # Root rules (always applied)
├── ui/
│   └── AGENTS.md      # UI-specific rules (auto-applied when in ui/)
└── api/
    └── AGENTS.md      # API-specific rules (auto-applied when in api/)
```

### Rules precedence

When multiple rules apply, Warp follows this order:

1. Rules in the current subdirectory's project rules file
2. Rules in the root directory's project rules file
3. Global Rules

The most specific, project-relevant rules take priority.

## How to access Rules

| Method | Path |
|--------|------|
| Settings panel | **Settings** > **Agents** > **Knowledge** > **Manage Rules** |
| macOS Menu | `AI > Open Rules` |
| Slash Commands | `/open-project-rules` |

## How to create, edit, or delete Rules

### Global Rules

- **From Warp Drive Rules pane:** **Personal** > **Rules** > **Global** — add, edit, or delete rules with optional name and description
- **From Slash Commands menu:** `/add-rule` in Auto or Agent input modes (opens Warp Drive Rules pane)

### Project Rules

- **Use `/init` in Auto-Detection or Agent Mode** when in a directory to:
  - Begin indexing your codebase or display indexing status
  - Generate an `AGENTS.md` file with initial context
  - Link an existing Rules file to `AGENTS.md`

Warp supports linking these external Rules files: `CLAUDE.md`, `.cursorrules`, `AGENT.md`, `GEMINI.md`, `.clinerules`, `.windsurfrules`, `.github/copilot-instructions.md`

View Project Rules via: **Personal** > **Rules** > **Project-based**

## Rules as Agent context

When relevant, Agents automatically pull in applicable rules to guide responses. Rules used in an interaction appear in the conversation under **References** or marked as derived from a specific rule.

## Rules privacy

See our [[https://docs.warp.dev/support-and-community/privacy-and-security/privacy|Privacy Page]] for information on how we handle data with Rules.