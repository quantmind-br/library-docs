---
number: 30
category: reference
status: published
optimized: true
optimized_at: 2025-01-27T22:45:00Z
source_url: https://developers.openai.com/codex/llms-full.txt.md
note: Multi-topic concatenated page — see individual topic entries
word_count: 957
---
# Codex Reference Index (Concatenated)

> **BLUF:** This file consolidates multiple Codex documentation topics. Each section is complete and self-contained.

---

## Speed

### Fast Mode

Increases model speed at higher credit consumption.

| Model | Speed Multiplier | Credit Rate |
|-------|-----------------|-------------|
| GPT-5.5 | 1.5x | 2.5x standard |
| GPT-5.4 | 1.5x | 2x standard |

- Enable: `/fast on/off/status` in CLI
- Persist: `service_tier = "fast"` + `[features].fast_mode = true` in `config.toml`
- Available: IDE extension, CLI, App (ChatGPT auth required; API key uses standard pricing)

### Codex-Spark

`gpt-5.3-codex-spark` is a separate fast model for near-instant iteration.

- Different model choice (not just speed multiplier)
- Own usage limits
- Research preview: ChatGPT Pro subscribers only

---

## Agent Skills

### Overview

Skills package instructions + resources + optional scripts for task-specific capabilities. Build on [open agent skills standard](https://agentskills.io).

- Available in CLI, IDE extension, App
- Progressive disclosure: Codex starts with name + description + path; loads full `SKILL.md` on selection
- Skills list capped at ~2% of context window (~8,000 chars) for initial prompt; full instructions loaded on skill activation

### Structure

Skill = directory with `SKILL.md` (must include `name` + `description`) + optional scripts/references.

### Invocation

| Method | How |
|--------|-----|
| **Explicit** | `$skill-name` in prompt; `/skills` in CLI/IDE; type `$` |
| **Implicit** | Codex chooses when task matches `description` |

> Write concise descriptions with key use case front-loaded. Codex can still match if descriptions are shortened.

### Creation

```text
$skill-creator
```

Answer prompts about skill purpose, triggers, scripts vs. instructions-only.

Manual: create folder + `SKILL.md`:
```md
---
name: skill-name
description: Explain when this skill triggers and when not.
---

Skill instructions for Codex.
```

### Storage Locations

| Scope | Location | Use |
|-------|----------|-----|
| `REPO` | `$CWD/.agents/skills` | Folder-specific team skills |
| `REPO` | `$REPO_ROOT/.agents/skills` | Root-level team skills |
| `USER` | `$HOME/.agents/skills` | Personal skills |
| `ADMIN` | `/etc/codex/skills` | System-wide admin skills |
| `SYSTEM` | Bundled with Codex | Built-in skills (`$skill-creator`, `$plan`) |

Codex follows symlinks when scanning locations.

### Distribution: Plugins

Package skills as [[034-plugins-build|plugin]] for distribution beyond single repo. Plugins can bundle multiple skills + app integrations + MCP config + assets.

### Installation

```bash
$skill-installer linear        # Install curated skill
$skill-installer owner/repo   # Install from repository
```

Codex detects new skills automatically; restart if not visible.

### Enable/Disable

```toml
[[skills.config]]
path = "/path/to/skill/SKILL.md"
enabled = false
```

### Optional Metadata

`agents/openai.yaml` for app UI, invocation policy, tool dependencies:
```yaml
interface:
  display_name: "Skill Name"
  short_description: "What it does"
  icon_small: "./assets/small-logo.svg"
  brand_color: "#3B82F6"
policy:
  allow_implicit_invocation: false
dependencies:
  tools:
    - type: "mcp"
      value: "openaiDeveloperDocs"
      transport: "streamable_http"
      url: "https://developers.openai.com/mcp"
```

---

## Subagents

### Overview

Spawn specialized agents in parallel for complex tasks. Codex handles orchestration, routing, waiting, and consolidation.

- Available by default in current releases
- Only spawns when explicitly asked
- Consumes more tokens than comparable single-agent runs

### Common Use Cases

- Codebase exploration
- Multi-step feature implementation
- PR review (one agent per focus area)

Example prompt:
```
Review these points on the current PR (this branch vs main). Spawn one agent per point, wait for all, summarize each.
1. Security issue
2. Code quality
3. Bugs
4. Race conditions
5. Test flakiness
6. Maintainability
```

### Managing Subagents

- `/agent` in CLI → switch between agent threads
- Ask Codex to steer, stop, or close agent threads

### Approvals + Sandbox

- Inherit current sandbox policy
- In CLI: approval requests from inactive threads surface in main thread; press `o` to open source thread
- Runtime overrides (e.g., `/permissions`, `--yolo`) reapplied to child agents even if agent file has different defaults
- Override sandbox per custom agent (e.g., `sandbox_mode = "read-only"`)

### Built-in Agents

| Agent | Purpose |
|-------|---------|
| `default` | General-purpose fallback |
| `worker` | Execution-focused implementation/fixes |
| `explorer` | Read-heavy codebase exploration |

### Custom Agents

Add TOML files to `~/.codex/agents/` (personal) or `.codex/agents/` (project-scoped).

**Required fields:**
- `name` — identifier (source of truth)
- `description` — when to use
- `developer_instructions` — core behavior

**Optional:** `nickname_candidates`, `model`, `model_reasoning_effort`, `sandbox_mode`, `mcp_servers`, `skills.config`

**Global settings** (`[agents]` in config):
| Field | Default | Description |
|-------|---------|-------------|
| `max_threads` | 6 | Concurrent open thread cap |
| `max_depth` | 1 | Spawn nesting depth (0 = root session) |
| `job_max_runtime_seconds` | 1800 | Per-worker timeout for CSV jobs |

> Raise `max_depth` only if needed; deeper recursion increases token usage, latency, resource consumption.

### CSV Batch Processing (Experimental)

`spawn_agents_on_csv` — one worker per CSV row, wait for batch, export results.

Parameters: `csv_path`, `instruction` (with `{column_name}` placeholders), `id_column`, `output_schema`, `output_csv_path`, `max_concurrency`, `max_runtime_seconds`

Each worker must call `report_agent_job_result` exactly once.

### Example: PR Review

Three focused agents:
- `pr_explorer` — map codebase, gather evidence (fast model, read-only)
- `reviewer` — correctness, security, tests (strong model, read-only)
- `docs_researcher` — verify APIs via MCP (fast model, read-only)

Prompt:
```
Review branch vs main. Have pr_explorer map affected paths, reviewer find risks, docs_researcher verify framework APIs.
```

---

## Plugins

> Full guide: [[034-plugins-build|Build Plugins]]

Create with `$plugin-creator`. Distribute via marketplace (repo: `$REPO_ROOT/.agents/plugins/marketplace.json`; personal: `~/.agents/plugins/marketplace.json`).

---

## Windows

> Full guide: [[058-windows|Windows]]

Three modes:
1. **Native elevated** — preferred Windows sandbox
2. **Native unelevated** — fallback
3. **WSL2** — Linux sandbox on Windows

---

## Workflows

> Full guide: [[056-workflows|Workflows]]

CLI commands for:
- Explain codebase
- Fix bugs
- Write tests
- Prototype from screenshot
- Iterate on UI
- Delegate to cloud
- Code review (local + GitHub PR)

---

## Security: Threat Model

### What a Threat Model Is

Short security summary of how repository works. Used as scan context for prioritization and review.

Calls out:
- Entry points, untrusted inputs
- Trust boundaries, auth assumptions
- Sensitive data paths, privileged actions
- Priority review areas

Example:
> Public API for account changes. Accepts JSON + file uploads. Uses internal auth service. Focus: auth checks, upload parsing, service-to-service trust boundaries.

### Editing

Go to [Codex Security scans](https://chatgpt.com/codex/security/scans) → open repo → **Edit**. Changes future scan context.

Tip: copy current model → ask Codex to improve → paste back updated version.

### Auto-Validation

Reproduction phase in isolated container. Records success/failure + evidence (logs, commands, artifacts).

If validation fails: finding stays unvalidated; logs still captured for retry/investigation.

### Patch Output

Minimal diff with filename + line context when remediation can be generated. Does NOT directly modify PR branch — generates patch for maintainer/reviewer inspection.

---

*Source: [OpenAI Developers](https://developers.openai.com/codex/llms-full.txt.md)*