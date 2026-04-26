---
title: CONFIGURATION
url: https://github.com/gsd-build/get-shit-done/blob/main/docs/CONFIGURATION.md
source: git
fetched_at: 2026-04-16T16:20:04.615479212-03:00
rendered_js: false
word_count: 3379
summary: This document provides a comprehensive reference for the GSD project configuration, detailing the schema for settings, workflow toggles, and environment parameters.
tags:
    - configuration-schema
    - workflow-toggles
    - project-settings
    - gsd-reference
    - automation-config
category: reference
optimized: true
optimized_at: 2026-04-26T00:00:00Z
---

# GSD Configuration Reference

> Full configuration schema, workflow toggles, model profiles, and git branching options. For feature context, see [[002-docs-FEATURES|Feature Reference]].

---

## Configuration File

GSD stores project settings in `.planning/config.json`. Created during `/gsd-new-project`, updated via `/gsd-settings`.

### Full Schema

```json
{
  "mode": "interactive",
  "granularity": "standard",
  "model_profile": "balanced",
  "model_overrides": {},
  "planning": {
    "commit_docs": true,
    "search_gitignored": false
  },
  "context_profile": null,
  "workflow": {
    "research": true,
    "plan_check": true,
    "verifier": true,
    "auto_advance": false,
    "nyquist_validation": true,
    "ui_phase": true,
    "ui_safety_gate": true,
    "node_repair": true,
    "node_repair_budget": 2,
    "research_before_questions": false,
    "discuss_mode": "discuss",
    "skip_discuss": false,
    "tdd_mode": false,
    "text_mode": false,
    "use_worktrees": true,
    "code_review": true,
    "code_review_depth": "standard",
    "plan_bounce": false,
    "plan_bounce_script": null,
    "plan_bounce_passes": 2,
    "code_review_command": null,
    "cross_ai_execution": false,
    "cross_ai_command": null,
    "cross_ai_timeout": 300
  },
  "hooks": {
    "context_warnings": true,
    "workflow_guard": false
  },
  "parallelization": {
    "enabled": true,
    "plan_level": true,
    "task_level": false,
    "skip_checkpoints": true,
    "max_concurrent_agents": 3,
    "min_plans_for_parallel": 2
  },
  "git": {
    "branching_strategy": "none",
    "phase_branch_template": "gsd/phase-{phase}-{slug}",
    "milestone_branch_template": "gsd/{milestone}-{slug}",
    "quick_branch_template": null
  },
  "gates": {
    "confirm_project": true,
    "confirm_phases": true,
    "confirm_roadmap": true,
    "confirm_breakdown": true,
    "confirm_plan": true,
    "execute_next_plan": true,
    "issues_review": true,
    "confirm_transition": true
  },
  "safety": {
    "always_confirm_destructive": true,
    "always_confirm_external_services": true
  },
  "project_code": null,
  "security_enforcement": true,
  "security_asvs_level": 1,
  "security_block_on": "high",
  "agent_skills": {},
  "response_language": null,
  "features": {
    "thinking_partner": false,
    "global_learnings": false
  },
  "learnings": {
    "max_inject": 10
  },
  "intel": {
    "enabled": false
  },
  "claude_md_path": null
}
```

---

## Core Settings

| Setting | Type | Options | Default | Description |
|---------|------|---------|---------|-------------|
| `mode` | enum | `interactive`, `yolo` | `interactive` | `yolo` auto-approves; `interactive` confirms at each step |
| `granularity` | enum | `coarse`, `standard`, `fine` | `standard` | Controls phase count: `coarse` (3-5), `standard` (5-8), `fine` (8-12) |
| `model_profile` | enum | `quality`, `balanced`, `budget`, `inherit` | `balanced` | Model tier per agent (see [Model Profiles](#model-profiles)) |
| `project_code` | string | any short string | (none) | Prefix for phase directory names (e.g., `"ABC"` produces `ABC-01-setup/`). Added v1.31 |
| `response_language` | string | language code | (none) | Language for agent responses. Propagates to all spawned agents. Added v1.32 |
| `context_profile` | string | `dev`, `research`, `review` | (none) | Execution context preset bundle. Added v1.34 |
| `claude_md_path` | string | any file path | (none) | Custom output path for CLAUDE.md in monorepos. Added v1.36 |

> [!note]
> `granularity` was renamed from `depth` in v1.22.3. Existing configs are auto-migrated.

---

## Workflow Toggles

All workflow toggles follow the **absent = enabled** pattern. Missing keys default to `true`.

| Setting | Type | Default | Description |
|---------|------|---------|-------------|
| `workflow.research` | boolean | `true` | Domain investigation before planning each phase |
| `workflow.plan_check` | boolean | `true` | Plan verification loop (up to 3 iterations) |
| `workflow.verifier` | boolean | `true` | Post-execution verification against phase goals |
| `workflow.auto_advance` | boolean | `false` | Auto-chain discuss → plan → execute without stopping |
| `workflow.nyquist_validation` | boolean | `true` | Test coverage mapping during plan-phase research |
| `workflow.ui_phase` | boolean | `true` | Generate UI design contracts for frontend phases |
| `workflow.ui_safety_gate` | boolean | `true` | Prompt to run /gsd-ui-phase for frontend phases |
| `workflow.node_repair` | boolean | `true` | Autonomous task repair on verification failure |
| `workflow.node_repair_budget` | number | `2` | Max repair attempts per failed task |
| `workflow.research_before_questions` | boolean | `false` | Run research before discussion questions |
| `workflow.discuss_mode` | string | `'discuss'` | `'discuss'` (one-by-one) or `'assumptions'` (codebase-first). Added v1.28 |
| `workflow.skip_discuss` | boolean | `false` | Bypass discuss-phase for `/gsd-autonomous`. Added v1.28 |
| `workflow.text_mode` | boolean | `false` | Replace TUI menus with plain-text lists for remote sessions. Added v1.28 |
| `workflow.use_worktrees` | boolean | `true` | Disable git worktree isolation for parallel execution. Added v1.31 |
| `workflow.code_review` | boolean | `true` | Enable `/gsd-code-review` and `/gsd-code-review-fix`. Added v1.34 |
| `workflow.code_review_depth` | string | `standard` | Review depth: `quick`, `standard`, or `deep`. Added v1.34 |
| `workflow.plan_bounce` | boolean | `false` | Run external validation script against generated plans. Added v1.36 |
| `workflow.plan_bounce_script` | string | (none) | Path to external script for plan bounce. Required when `plan_bounce` is `true`. Added v1.36 |
| `workflow.plan_bounce_passes` | number | `2` | Number of sequential bounce passes. Added v1.36 |
| `workflow.code_review_command` | string | (none) | Shell command for external code review integration. Added v1.36 |
| `workflow.tdd_mode` | boolean | `false` | Enable TDD pipeline as first-class execution mode. Added v1.37 |
| `workflow.cross_ai_execution` | boolean | `false` | Delegate phase execution to external AI CLI. Added v1.36 |
| `workflow.cross_ai_command` | string | (none) | Shell command template for cross-AI execution. Added v1.36 |
| `workflow.cross_ai_timeout` | number | `300` | Timeout in seconds for cross-AI execution. Added v1.36 |

### Recommended Presets

| Scenario | mode | granularity | profile | research | plan_check | verifier |
|----------|------|------------|---------|----------|------------|----------|
| Prototyping | `yolo` | `coarse` | `budget` | `false` | `false` | `false` |
| Normal development | `interactive` | `standard` | `balanced` | `true` | `true` | `true` |
| Production release | `interactive` | `fine` | `quality` | `true` | `true` | `true` |

---

## Planning Settings

| Setting | Type | Default | Description |
|---------|------|---------|-------------|
| `planning.commit_docs` | boolean | `true` | Whether `.planning/` files are committed to git |
| `planning.search_gitignored` | boolean | `false` | Add `--no-ignore` to broad searches |

> [!note]
> If `.planning/` is in `.gitignore`, `commit_docs` is automatically `false` regardless of config.

---

## Hook Settings

| Setting | Type | Default | Description |
|---------|------|---------|-------------|
| `hooks.context_warnings` | boolean | `true` | Show context window usage warnings |
| `hooks.workflow_guard` | boolean | `false` | Warn when file edits happen outside GSD workflow context |

The prompt injection guard hook (`gsd-prompt-guard.js`) is always active and cannot be disabled.

### Private Planning Setup

To keep planning artifacts out of git:
1. Set `planning.commit_docs: false` and `planning.search_gitignored: true`
2. Add `.planning/` to `.gitignore`
3. If previously tracked: `git rm -r --cached .planning/ && git commit -m "chore: stop tracking planning docs"`

---

## Agent Skills Injection

Inject custom skill files into GSD subagent prompts. Skills are read at spawn time, giving agents project-specific instructions.

| Setting | Type | Default | Description |
|---------|------|---------|-------------|
| `agent_skills` | object | `{}` | Map of agent types to skill directory paths |

### Configuration

```json
{
  "agent_skills": {
    "gsd-executor": ["skills/testing-standards", "skills/api-conventions"],
    "gsd-planner": ["skills/architecture-rules"],
    "gsd-verifier": ["skills/acceptance-criteria"]
  }
}
```

Each path must be a directory containing a `SKILL.md` file. Paths are validated for safety.

### Supported Agent Types

- `gsd-executor` — executes implementation plans
- `gsd-planner` — creates phase plans
- `gsd-checker` — verifies plan quality
- `gsd-verifier` — post-execution verification
- `gsd-researcher` — phase research
- `gsd-project-researcher` — new-project research
- `gsd-debugger` — diagnostic agents
- `gsd-codebase-mapper` — codebase analysis
- `gsd-advisor` — discuss-phase advisors
- `gsd-ui-researcher` — UI design contract creation
- `gsd-ui-checker` — UI spec verification
- `gsd-roadmapper` — roadmap creation
- `gsd-synthesizer` — research synthesis

### How It Works

At spawn time, workflows call `node gsd-tools.cjs agent-skills <type>` to load configured skills:

```xml
<agent_skills>
Read these user-configured skills:
- @skills/testing-standards/SKILL.md
- @skills/api-conventions/SKILL.md
</agent_skills>
```

If no skills are configured, the block is omitted (zero overhead).

### CLI

```bash
node gsd-tools.cjs config-set agent_skills.gsd-executor '["skills/my-skill"]'
```

---

## Feature Flags

Toggle optional capabilities via `features.*`. Feature flags default to `false` (disabled).

| Setting | Type | Default | Description |
|---------|------|---------|-------------|
| `features.thinking_partner` | boolean | `false` | Enable thinking partner analysis at workflow decision points |
| `features.global_learnings` | boolean | `false` | Enable cross-project learnings pipeline |
| `intel.enabled` | boolean | `false` | Enable queryable codebase intelligence system (`/gsd-intel`). Added v1.34 |

### Usage

```bash
node gsd-tools.cjs config-set features.global_learnings true
node gsd-tools.cjs config-set features.thinking_partner false
```

The `features.*` namespace is dynamic — new feature flags can be added without modifying `VALID_CONFIG_KEYS`.

---

## Parallelization Settings

| Setting | Type | Default | Description |
|---------|------|---------|-------------|
| `parallelization.enabled` | boolean | `true` | Run independent plans simultaneously |
| `parallelization.plan_level` | boolean | `true` | Parallelize at plan level |
| `parallelization.task_level` | boolean | `false` | Parallelize tasks within a plan |
| `parallelization.skip_checkpoints` | boolean | `true` | Skip checkpoints during parallel execution |
| `parallelization.max_concurrent_agents` | number | `3` | Maximum simultaneous agents |
| `parallelization.min_plans_for_parallel` | number | `2` | Minimum plans to trigger parallel execution |

> [!warning]
> When parallelization is enabled, executor agents commit with `--no-verify` to avoid build lock contention. STATE.md writes are protected by file-level locking.

---

## Git Branching

| Setting | Type | Default | Description |
|---------|------|---------|-------------|
| `git.branching_strategy` | enum | `none` | `none`, `phase`, or `milestone` |
| `git.phase_branch_template` | string | `gsd/phase-{phase}-{slug}` | Branch name for phase strategy |
| `git.milestone_branch_template` | string | `gsd/{milestone}-{slug}` | Branch name for milestone strategy |
| `git.quick_branch_template` | string or null | `null` | Optional branch name for `/gsd-quick` tasks |

### Strategy Comparison

| Strategy | Creates Branch | Scope | Merge Point | Best For |
|----------|---------------|-------|-------------|----------|
| `none` | Never | N/A | N/A | Solo development, simple projects |
| `phase` | At `execute-phase` start | One phase | User merges after phase | Code review per phase |
| `milestone` | At first `execute-phase` | All phases in milestone | At `complete-milestone` | Release branches, PR per version |

### Template Variables

| Variable | Available In | Example |
|----------|-------------|---------|
| `{phase}` | `phase_branch_template` | `03` (zero-padded) |
| `{slug}` | Both templates | `user-authentication` |
| `{milestone}` | `milestone_branch_template` | `v1.0` |
| `{num}` / `{quick}` | `quick_branch_template` | `260317-abc` |

### Merge Options at Milestone Completion

| Option | Git Command | Result |
|--------|-------------|--------|
| Squash merge (recommended) | `git merge --squash` | Single clean commit per branch |
| Merge with history | `git merge --no-ff` | Preserves all individual commits |
| Delete without merging | `git branch -D` | Discard branch work |
| Keep branches | (none) | Manual handling later |

---

## Gate Settings

Control confirmation prompts during workflows.

| Setting | Type | Default | Description |
|---------|------|---------|-------------|
| `gates.confirm_project` | boolean | `true` | Confirm project details before finalizing |
| `gates.confirm_phases` | boolean | `true` | Confirm phase breakdown |
| `gates.confirm_roadmap` | boolean | `true` | Confirm roadmap before proceeding |
| `gates.confirm_breakdown` | boolean | `true` | Confirm task breakdown |
| `gates.confirm_plan` | boolean | `true` | Confirm each plan before execution |
| `gates.execute_next_plan` | boolean | `true` | Confirm before executing next plan |
| `gates.issues_review` | boolean | `true` | Review issues before creating fix plans |
| `gates.confirm_transition` | boolean | `true` | Confirm phase transition |

---

## Safety Settings

| Setting | Type | Default | Description |
|---------|------|---------|-------------|
| `safety.always_confirm_destructive` | boolean | `true` | Confirm destructive operations |
| `safety.always_confirm_external_services` | boolean | `true` | Confirm external service interactions |

---

## Security Settings

Settings for security enforcement feature (v1.31). All follow **absent = enabled** pattern.

| Setting | Type | Default | Description |
|---------|------|---------|-------------|
| `security_enforcement` | boolean | `true` | Enable threat-model-anchored security verification via `/gsd-secure-phase` |
| `security_asvs_level` | number (1-3) | `1` | OWASP ASVS verification level: 1=opportunistic, 2=standard, 3=comprehensive |
| `security_block_on` | string | `"high"` | Minimum severity that blocks phase advancement: `"high"`, `"medium"`, `"low"` |

---

## Review Settings

Configure per-CLI model selection for `/gsd-review`.

| Setting | Type | Default | Description |
|---------|------|---------|-------------|
| `review.models.gemini` | string | (CLI default) | Model for `--gemini` reviewer |
| `review.models.claude` | string | (CLI default) | Model for `--claude` reviewer |
| `review.models.codex` | string | (CLI default) | Model for `--codex` reviewer |
| `review.models.opencode` | string | (CLI default) | Model for `--opencode` reviewer |
| `review.models.qwen` | string | (CLI default) | Model for `--qwen` reviewer |
| `review.models.cursor` | string | (CLI default) | Model for `--cursor` reviewer |

```json
{
  "review": {
    "models": {
      "gemini": "gemini-2.5-pro",
      "qwen": "qwen-max"
    }
  }
}
```

Added in v1.35.0.

---

## Manager Passthrough Flags

Configure per-step flags that `/gsd-manager` appends to each dispatched command.

| Setting | Type | Default | Description |
|---------|------|---------|-------------|
| `manager.flags.discuss` | string | (none) | Flags for discuss-phase commands |
| `manager.flags.plan` | string | (none) | Flags for plan-phase commands |
| `manager.flags.execute` | string | (none) | Flags for execute-phase commands |

```json
{
  "manager": {
    "flags": {
      "discuss": "--auto",
      "plan": "--skip-research",
      "execute": "--validate"
    }
  }
}
```

---

## Model Profiles

### Profile Definitions

| Agent | `quality` | `balanced` | `budget` | `inherit` |
|-------|-----------|------------|----------|-----------|
| gsd-planner | Opus | Opus | Sonnet | Inherit |
| gsd-roadmapper | Opus | Sonnet | Sonnet | Inherit |
| gsd-executor | Opus | Sonnet | Sonnet | Inherit |
| gsd-phase-researcher | Opus | Sonnet | Haiku | Inherit |
| gsd-project-researcher | Opus | Sonnet | Haiku | Inherit |
| gsd-research-synthesizer | Sonnet | Sonnet | Haiku | Inherit |
| gsd-debugger | Opus | Sonnet | Sonnet | Inherit |
| gsd-codebase-mapper | Sonnet | Haiku | Haiku | Inherit |
| gsd-verifier | Sonnet | Sonnet | Haiku | Inherit |
| gsd-plan-checker | Sonnet | Sonnet | Haiku | Inherit |
| gsd-integration-checker | Sonnet | Sonnet | Haiku | Inherit |
| gsd-nyquist-auditor | Sonnet | Sonnet | Haiku | Inherit |

### Per-Agent Overrides

```json
{
  "model_profile": "balanced",
  "model_overrides": {
    "gsd-executor": "opus",
    "gsd-planner": "haiku"
  }
}
```

Valid override values: `opus`, `sonnet`, `haiku`, `inherit`, or fully-qualified model ID (e.g., `"openai/o3"`).

### Non-Claude Runtimes

When GSD is installed for a non-Claude runtime, the installer automatically sets `resolve_model_ids: "omit"` in `~/.gsd/defaults.json`. This causes GSD to return an empty model parameter for all agents.

```json
{
  "resolve_model_ids": "omit",
  "model_overrides": {
    "gsd-planner": "o3",
    "gsd-executor": "o4-mini",
    "gsd-debugger": "o3",
    "gsd-codebase-mapper": "o4-mini"
  }
}
```

### `resolve_model_ids` Values

| Value | Behavior | Use When |
|-------|----------|----------|
| `false` (default) | Returns Claude aliases (`opus`, `sonnet`, `haiku`) | Claude Code with native Anthropic API |
| `true` | Maps aliases to full Claude model IDs (`claude-opus-4-6`) | Claude Code with API requiring full IDs |
| `"omit"` | Returns empty string (runtime picks default) | Non-Claude runtimes (Codex, OpenCode, Gemini CLI, Kilo) |

### Profile Philosophy

| Profile | Philosophy | When to Use |
|---------|-----------|-------------|
| `quality` | Opus for all decision-making, Sonnet for verification | Quota available, critical architecture work |
| `balanced` | Opus for planning only, Sonnet for everything else | Normal development (default) |
| `budget` | Sonnet for code-writing, Haiku for research/verification | High-volume work, less critical phases |
| `inherit` | All agents use current session model | Dynamic model switching, **non-Anthropic providers** |

---

## Environment Variables

| Variable | Purpose |
|----------|---------|
| `CLAUDE_CONFIG_DIR` | Override default config directory (`~/.claude/`) |
| `GEMINI_API_KEY` | Detected by context monitor to switch hook event name |
| `WSL_DISTRO_NAME` | Detected by installer for WSL path handling |
| `GSD_SKIP_SCHEMA_CHECK` | Skip schema drift detection during execute-phase (v1.31) |
| `GSD_PROJECT` | Override project root for multi-project workspace support (v1.32) |

---

## Global Defaults

Save settings as global defaults for future projects.

**Location:** `~/.gsd/defaults.json`

When `/gsd-new-project` creates a new `config.json`, it reads global defaults and merges them. Per-project settings always override globals.

#configuration-schema #workflow-toggles #project-settings #gsd-reference #automation-config
