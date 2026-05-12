---
title: Customization
url: https://developers.openai.com/codex/concepts/customization.md
source: llms
fetched_at: 2026-04-30T10:15:21.904066116-03:00
rendered_js: false
word_count: 683
summary: This document outlines the customization architecture for Codex, explaining how to utilize project-specific guidance, reusable skills, and the Model Context Protocol to tailor the agent to team workflows.
tags:
    - codex
    - customization
    - agents-md
    - skills
    - mcp
    - workflow-automation
    - agent-configuration
category: concept
optimized: true
optimized_at: 2026-04-30T13:30:00Z
---
# Customization

Make Codex work the way your team works. Layers are complementary, not competing:

| Layer | Purpose |
|-------|---------|
| **AGENTS.md** | Persistent project instructions |
| **Memories** | Context learned from prior work |
| **Skills** | Reusable workflows and domain expertise |
| **MCP** | Access to external tools and shared systems |
| **Subagents** | Delegating work to specialized agents |

## AGENTS.md guidance

Durable project guidance that travels with your repository and applies before the agent starts work. Keep it small.

Use for rules Codex should follow every time:
- Build and test commands
- Review expectations
- Repo-specific conventions
- Directory-specific instructions

When Codex makes incorrect assumptions, correct them in `AGENTS.md` and ask the agent to update it so the fix persists. Treat it as a feedback loop.

### When to update

| Situation | Action |
|-----------|--------|
| Repeated mistakes | Add a rule |
| Too much reading | Add routing guidance (which directories/files to prioritize) |
| Recurring PR feedback | Codify it |
| In GitHub | Tag `@codex` in PR comment (e.g., `@codex add this to AGENTS.md`) |
| Automate drift checks | Use [[002-app-automations|automations]] to run recurring checks for guidance gaps |

Pair `AGENTS.md` with infrastructure that enforces rules: pre-commit hooks, linters, type checkers.

Codex loads guidance from multiple locations: global file in Codex home directory (for you as a developer) and repo-specific files (for teams). Files closer to working directory take precedence.

- **Global** (`~/.codex/AGENTS.md`) — shape how Codex communicates (review style, verbosity, defaults)
- **Repo** (`AGENTS.md` in repo root or nested) — team and codebase rules

[[020-guides-agents-md|Custom instructions with AGENTS.md]]

## Skills

Reusable capabilities for repeatable workflows. Support richer instructions, scripts, and references while staying reusable across tasks. Loaded and visible to the agent (at least metadata), so Codex can discover and choose them implicitly.

Use skill folders to author and iterate locally. If a plugin already exists for the workflow, install it first. When you want to distribute across teams or bundle with app integrations, package as a [[034-plugins-build|plugin]]. Skills remain the authoring format; plugins are the installable distribution unit.

Structure: `SKILL.md` plus optional `scripts/`, `references/`, `assets/`.

Example `SKILL.md`:
```md
---
name: commit
description: Stage and commit changes in semantic groups. Use when the user wants to commit, organize commits, or clean up a branch before pushing.
---

1. Do not run `git add .`. Stage files in logical groups by purpose.
2. Group into separate commits: feat → test → docs → refactor → chore.
3. Write concise commit messages that match the change scope.
4. Keep each commit focused and reviewable.
```

Use skills for:
- Repeatable workflows (release steps, review routines, docs updates)
- Team-specific expertise
- Procedures needing examples, references, or helper scripts

| Layer | Global | Repo |
|-------|--------|------|
| AGENTS | `~/.codex/AGENTS.md` | `AGENTS.md` in repo root or nested |
| Skills | `$HOME/.agents/skills` | `.agents/skills` in repo |

Progressive disclosure:
- Starts with metadata (`name`, `description`) for discovery
- Loads `SKILL.md` only when chosen
- Reads references or runs scripts only when needed

Can be invoked explicitly or chosen implicitly when task matches description.

[[037-skills|Agent Skills]]

## MCP

Model Context Protocol — standard way to connect Codex to external tools and context providers. Especially useful for remotely hosted systems: Figma, Linear, GitHub, internal knowledge services.

- **Host**: Codex
- **Client**: MCP connection inside Codex
- **Server**: external tool or context provider

MCP servers expose:
- **Tools** (actions)
- **Resources** (readable data)
- **Prompts** (reusable prompt templates)

Often most useful when paired with skills: a skill defines the workflow and names the MCP tools to use.

[[058-mcp|Model Context Protocol]]

## Subagents

Create different agents with different roles and prompt them to use tools differently. For example, one agent runs specific testing commands while another fetches production logs for debugging. Each subagent stays focused and uses the right tools for its job.

[[045-concepts-subagents|Subagent concepts]]

## Skills + MCP together

Skills define repeatable workflows; MCP connects them to external tools and systems. If a skill depends on MCP, declare that dependency in `agents/openai.yaml` so Codex can install and wire it automatically.

## Build in this order

1. [[020-guides-agents-md|AGENTS.md]] so Codex follows repo conventions. Add pre-commit hooks and linters.
2. Install a [[035-plugins|plugin]] when a reusable workflow exists. Otherwise create a [[037-skills|skill]] and package as a plugin to share.
3. [[058-mcp|MCP]] when workflows need external systems (Linear, GitHub, docs servers, design tools).
4. [[049-subagents|Subagents]] when ready to delegate noisy or specialized tasks.

#customization #agents #skills #mcp #subagents #codex