---
title: Agent Skills
url: https://developers.openai.com/codex/skills.md
source: llms
fetched_at: 2026-04-30T10:16:07.73480062-03:00
rendered_js: false
word_count: 508
summary: This document explains how to create, configure, and manage reusable agent skills in Codex to extend its task-specific capabilities through instructions and scripts.
tags:
    - agent-skills
    - codex-platform
    - workflow-automation
    - plugin-development
    - context-management
category: guide
optimized: true
optimized_at: 2026-04-30T13:30:00Z
---
# Agent Skills

Extend Codex with task-specific capabilities. A skill packages instructions, resources, and optional scripts so Codex follows a workflow reliably. Builds on the [open agent skills standard](https://agentskills.io).

Skills = authoring format for reusable workflows.
Plugins = installable distribution unit for skills + apps.

Available in CLI, IDE extension, and Codex app.

Skills use **progressive disclosure**: Codex starts with `name`, `description`, and file path. Full `SKILL.md` instructions load only when Codex decides to use the skill.

The initial skills list is capped at ~2% of model context window (or 8,000 characters when unknown). If many skills are installed, Codex shortens descriptions first; very large sets may omit some skills with a warning. This budget applies only to the initial list — when selected, the full `SKILL.md` is still read.

## Structure

A skill is a directory with `SKILL.md` plus optional scripts and references. `SKILL.md` must include `name` and `description`.

```
my-skill/
  SKILL.md          # Required: instructions + metadata
  scripts/          # Optional: executable code
  references/       # Optional: documentation
  assets/           # Optional: templates, resources
  agents/
    openai.yaml     # Optional: appearance and dependencies
```

## How Codex uses skills

1. **Explicit invocation** — include skill in prompt. In CLI/IDE, run `/skills` or type `$` to mention a skill.
2. **Implicit invocation** — Codex chooses a skill when your task matches its `description`.

Because implicit matching depends on `description`, write concise descriptions with clear scope and boundaries. Front-load key use case and trigger words.

## Create a skill

Built-in creator:
```text
$skill-creator
```

Asks what the skill does, when it should trigger, and whether to include scripts. Instruction-only is the default.

Manual creation: create a folder with `SKILL.md`:
```md
---
name: skill-name
description: Explain exactly when this skill should and should not trigger.
---

Skill instructions for Codex to follow.
```

Codex detects changes automatically. Restart if an update doesn't appear.

## Where to save skills

| Scope | Location | Suggested use |
|-------|----------|---------------|
| **REPO** | `$CWD/.agents/skills` | Skills relevant to current working folder (microservice, module) |
| **REPO** | `$CWD/../.agents/skills` | Shared area in parent folder |
| **REPO** | `$REPO_ROOT/.agents/skills` | Root skills available to any subfolder |
| **USER** | `$HOME/.agents/skills` | User-curated skills for any repo |
| **ADMIN** | `/etc/codex/skills` | SDK scripts, automation, default admin skills |
| **SYSTEM** | Bundled with Codex | Broad-audience skills (skill-creator, plan skills) |

If two skills share the same `name`, Codex doesn't merge them; both can appear in selectors.

Codex supports symlinked skill folders.

## Distribute with plugins

Direct skill folders are best for local authoring and repo-scoped workflows. For distribution across teams or bundling with app integrations, package as a [[034-plugins-build|plugin]].

## Install curated skills

Add curated skills beyond built-ins:
```bash
$skill-installer linear
```

You can also prompt the installer to download skills from other repositories. Codex detects newly installed skills automatically; restart if one doesn't appear.

## Enable or disable

```toml
[[skills.config]]
path = "/path/to/skill/SKILL.md"
enabled = false
```

Restart Codex after changing `~/.codex/config.toml`.

## Optional metadata (`agents/openai.yaml`)

Configure UI metadata, invocation policy, and tool dependencies:

```yaml
interface:
  display_name: "Optional user-facing name"
  short_description: "Optional user-facing description"
  icon_small: "./assets/small-logo.svg"
  icon_large: "./assets/large-logo.png"
  brand_color: "#3B82F6"
  default_prompt: "Optional surrounding prompt to use the skill with"

policy:
  allow_implicit_invocation: false

dependencies:
  tools:
    - type: "mcp"
      value: "openaiDeveloperDocs"
      description: "OpenAI Docs MCP server"
      transport: "streamable_http"
      url: "https://developers.openai.com/mcp"
```

`allow_implicit_invocation` (default `true`): when `false`, Codex won't implicitly invoke based on prompt; explicit `$skill` still works.

## Best practices

- Keep each skill focused on one job.
- Prefer instructions over scripts unless you need deterministic behavior or external tooling.
- Write imperative steps with explicit inputs and outputs.
- Test prompts against the skill description to confirm trigger behavior.

For examples: [github.com/openai/skills](https://github.com/openai/skills) and [agentskills.io/specification](https://agentskills.io/specification).

#skills #workflows #plugins #codex