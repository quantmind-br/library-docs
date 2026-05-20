---
title: How to Customize BMad
url: https://docs.bmad-method.org//llms-full.txt
source: llms
fetched_at: 2026-05-19T08:33:05.038451722-03:00
rendered_js: false
summary: Tailor agent personas, inject domain context, add capabilities, and customize workflows in BMad.
tags:
    - bmad-method
    - customization
    - agents
    - workflows
category: guide
optimized: true
optimized_at: 2026-05-19T11:33:00Z
word_count: 1280
---
# How to Customize BMad

Customize agent personas, domain context, capabilities, and workflows without touching installed files. Changes survive updates.

> [!tip] Use `bmad-customize` skill
> Guided authoring helper for per-skill agent/workflow overrides. Scans installed skills, picks the right surface, writes the file, and verifies the merge. Central-config overrides (`_bmad/custom/config.toml`) still require hand-authoring.

## When to Use This

| Situation | Action |
|---|---|
| Change agent personality or style | Override `[agent]` scalars |
| Inject persistent org facts | `persistent_facts` array |
| Add startup steps every session | `activation_steps_prepend` / `activation_steps_append` |
| Add custom menu items | `[[agent.menu]]` keyed by `code` |
| Share team conventions via git | `_bmad/custom/{skill}.toml` |
| Layer personal preferences | `_bmad/custom/{skill}.user.toml` |

> [!info] Prerequisites
> - BMad installed ([[002-how-to-install-bmad|How to Install Bmad]])
> - Python 3.11+ on PATH (stdlib `tomllib` only)

## How It Works

Every customizable skill ships a `customize.toml` defining its full override surface. You never edit this file. Instead, create sparse override files containing only the fields you want to change.

### Three-Layer Override Model

```text
Priority 1 (wins): _bmad/custom/{skill-name}.user.toml   # personal, gitignored
Priority 2:        _bmad/custom/{skill-name}.toml      # team, committed
Priority 3 (last):  skill's own customize.toml           # defaults
```

### Merge Rules (by shape)

| Shape | Rule |
|---|---|
| Scalar | Override wins |
| Table | Deep merge (recursive) |
| Array of tables with same identifier field (`code` or `id` on every item) | Merge by that key — matching keys replace in place, new keys append |
| Any other array | Append (base → team → user) |

> [!warning] No removal mechanism
> Overrides cannot delete base items. To suppress a default menu item, override its `code` with a no-op. To restructure an array deeply, fork the skill.

> [!warning] `code`/`id` convention
> Pick one convention across an entire array. Mixing `code` on some items and `id` on others falls back to append.

### Read-Only Identity Fields

`agent.name` and `agent.title` are hardcoded in SKILL.md; overrides have no effect. To rename an agent, copy the skill folder and ship it as a custom skill.

## Steps

### 1. Find the Skill's `customize.toml`

Path varies by IDE:
- Claude: `.claude/skills/{skill}/customize.toml`
- Cursor: `.cursor/skills/{skill}/customize.toml`
- Cline: `.cline/skills/{skill}/customize.toml`

This file is the canonical schema — every field shown is customizable (except `name`/`title`).

### 2. Create Override File

```text
_bmad/custom/
  bmad-agent-pm.toml        # team overrides (committed)
  bmad-agent-pm.user.toml   # personal (gitignored)
```

> [!warning] Sparse overrides only
> Include only changed fields. Copying the full `customize.toml` locks in old defaults and silently drifts on every update.

**Example — change icon and append one principle**:

```toml
[agent]
icon = "🏥"
principles = ["Ship nothing that can't pass an FDA audit."]
```

### 3. Customize

All examples use BMad's flat `[agent]` schema. Fields sit directly under `[agent]` — no nested `metadata` or `persona` sub-tables.

**Scalars** (icon, role, identity, communication_style):

```toml
[agent]
icon = "🏥"
role = "Drives product discovery for a regulated healthcare domain."
communication_style = "Precise, regulatory-aware, asks compliance-shaped questions early."
```

**Append arrays** (persistent_facts, principles, activation hooks):

```toml
[agent]
persistent_facts = [
  "Our org is AWS-only — do not propose GCP or Azure.",
  "All PRDs require legal sign-off before engineering kickoff.",
  "Target users are clinicians, not patients.",
  "file:{project-root}/docs/compliance/hipaa-overview.md",
  "file:{project-root}/_bmad/custom/company-glossary.md",
]
principles = [
  "Ship nothing that can't pass an FDA audit.",
  "User value first, compliance always.",
]
activation_steps_prepend = [
  "Scan {project-root}/docs/compliance/ and load any HIPAA-related documents as context.",
]
activation_steps_append = [
  "Read {project-root}/_bmad/custom/company-glossary.md if it exists.",
]
```

- `activation_steps_prepend`: runs BEFORE standard activation (persona, facts, config, greet). Use for pre-flight loads or compliance checks that must be in context before the greeting.
- `activation_steps_append`: runs AFTER greet, BEFORE menu. Use for heavy setup so the user sees a greeting first.

**Menu customization** (merge by `code`):

```toml
# Replace existing CE item with custom skill
[[agent.menu]]
code = "CE"
description = "Create Epics using our delivery framework"
skill = "custom-create-epics"

# Add new item
[[agent.menu]]
code = "RC"
description = "Run compliance pre-check"
prompt = """
Read {project-root}/_bmad/custom/compliance-checklist.md
and scan all documents in {planning_artifacts} against it.
Report any gaps and cite the relevant regulatory section.
"""
```

Each menu item has exactly one of `skill` (invokes a registered skill) or `prompt` (executes text directly). Unlisted items keep defaults.

**File references**: Use `{project-root}`-rooted paths even for files next to the override: `{project-root}/_bmad/custom/info.md`. The agent resolves `{project-root}` at runtime.

### 4. Personal vs Team

| File | Git | Scope |
|---|---|---|
| `{skill}.toml` | Committed | Team compliance, company persona, shared capabilities |
| `{skill}.user.toml` | Gitignored | Tone, personal workflow preferences, private facts |

```toml
# _bmad/custom/bmad-agent-pm.user.toml
[agent]
persistent_facts = [
  "Always include a rough complexity estimate (low/medium/high) when presenting options.",
]
```

## How Resolution Works

A shared Python script does the three-layer merge and returns JSON. Uses stdlib `tomllib` — no `pip install`, no `uv`, no virtualenv.

```bash
python3 {project-root}/_bmad/scripts/resolve_customization.py \
  --skill {skill-root} \
  --key agent
```

| Flag | Purpose |
|---|---|
| `--key agent` | Resolve full `[agent]` block |
| `--key agent.icon` | Resolve single field |
| (no `--key`) | Full dump |

**Requirements**: Python 3.11+ (earlier versions lack `tomllib`). On systems defaulting to 3.10 (macOS without Homebrew, Ubuntu 22.04), install 3.11+ separately.

If the script is unavailable, SKILL.md tells the agent to read the three TOML files directly and apply the same merge rules.

## Workflow Customization

Workflows use the same override mechanism under `[workflow]` instead of `[agent]`.

```toml
# _bmad/custom/bmad-product-brief.toml
[workflow]
activation_steps_prepend = [
  "Load {project-root}/docs/product/north-star-principles.md as context.",
]
activation_steps_append = []
persistent_facts = [
  "All briefs must include an explicit regulatory-risk section.",
  "file:{project-root}/docs/compliance/product-brief-checklist.md",
]
on_complete = "Summarize the brief in three bullets and offer to email it via the gws-gmail-send skill."
```

Same conventions cross the boundary: `activation_steps_prepend`/`append`, `persistent_facts` (with `file:` refs), `[[…]]` tables with `code`/`id` for keyed merge. SKILL.md references follow the namespace: `{workflow.activation_steps_prepend}`, `{workflow.persistent_facts}`, `{workflow.on_complete}`.

### Activation Order

1. Resolve `[workflow]` block (base → team → user)
2. Execute `activation_steps_prepend`
3. Load `persistent_facts` as foundational context
4. Load config (`_bmad/bmm/config.yaml`) and resolve standard variables
5. Greet user
6. Execute `activation_steps_append`

After step 6, workflow body begins.

### Scope of Initial Pass

The fields above (`activation_steps_prepend`, `activation_steps_append`, `persistent_facts`, `on_complete`) are the **baseline surface** every customizable workflow exposes, and they remain stable across versions. Individual workflows will add targeted customization points (step toggles, stage flags, output template paths, review gates) over time; these stack on top rather than replacing baseline fields.

## Central Configuration

Per-skill `customize.toml` covers deep behavior for one agent/workflow. Central config covers cross-cutting state — install answers and the agent roster consumed by `bmad-party-mode`, `bmad-retrospective`, and `bmad-advanced-elicitation`.

```text
_bmad/config.toml               # installer-owned, team scope: install answers + agent roster
_bmad/config.user.toml          # installer-owned, user scope: user_name, language, skill level
_bmad/custom/config.toml        # human-authored, team overrides (committed)
_bmad/custom/config.user.toml   # human-authored, personal overrides (gitignored)
```

### Four-Layer Merge

```text
Priority 1 (wins): _bmad/custom/config.user.toml
Priority 2:        _bmad/custom/config.toml
Priority 3:        _bmad/config.user.toml
Priority 4 (base): _bmad/config.toml
```

Same structural rules as per-skill customize.

### What Lives Where

- `[core]` and `[modules.<code>]` — install answers. Scope `team` → `_bmad/config.toml`; scope `user` → `_bmad/config.user.toml`.
- `[agents.<code>]` — agent essence (code, name, title, icon, description, team) from `module.yaml` `agents:` block. Always team-scoped.

### Editing Rules

- `_bmad/config.toml` and `_bmad/config.user.toml` are **regenerated every install** — treat as read-only. To change an install answer durably, re-run the installer or shadow the value in `_bmad/custom/config.toml`.
- `_bmad/custom/config.toml` and `_bmad/custom/config.user.toml` are **never touched** by the installer — correct surface for custom agents, descriptor overrides, team-enforced settings, and pinned values.

### Examples

**Rebrand an agent org-wide**:

```toml
# _bmad/custom/config.toml
[agents.bmad-agent-pm]
description = "Healthcare PM — regulatory-aware, stakeholder-driven, FDA-shaped questions first."
icon = "🏥"
```

Roster consumers (party-mode, etc.) pick up the new description automatically. The agent's internal behavior still comes from its per-skill `customize.toml`.

**Add a fictional agent**:

```toml
# _bmad/custom/config.user.toml
[agents.kirk]
team = "startrek"
name = "Captain James T. Kirk"
title = "Starship Captain"
icon = "🖖"
description = "Bold, rule-bending commander. Speaks in dramatic pauses. Thinks aloud about the weight of command."
```

No skill folder required — the essence alone is enough for party-mode to spawn the voice. Filter by `team` to invite subsets.

**Pin team install settings**:

```toml
# _bmad/custom/config.toml
[modules.bmm]
planning_artifacts = "/shared/org-planning-artifacts"
```

Overrides whatever each developer answered locally during install.

### When to Use Which Surface

| Need | Surface |
|---|---|
| Add MCP tool calls to every dev workflow | Per-skill: `_bmad/custom/bmad-agent-dev.toml` `persistent_facts` |
| Add a menu item to an agent | Per-skill: `_bmad/custom/bmad-agent-{role}.toml` `[[agent.menu]]` |
| Swap a workflow's output template | Per-skill: `_bmad/custom/{workflow}.toml` scalar override |
| Rebrand an agent's public descriptor | Central: `_bmad/custom/config.toml` `[agents.<code>]` |
| Add a custom/fictional agent to roster | Central: `_bmad/custom/config.*.toml` `[agents.<code>]` |
| Pin team-enforced install settings | Central: `_bmad/custom/config.toml` `[modules.<code>]` or `[core]` |

Use both surfaces in the same project as needed.

## Worked Examples

For enterprise recipes (shaping an agent across every workflow, enforcing org conventions, publishing to Confluence/Jira, customizing the agent roster, swapping output templates), see [[008-how-to-expand-org|How to Expand BMad for Your Organization]].

## Troubleshooting

**Customization not appearing?**
- Verify file is in `_bmad/custom/` with exact skill directory name (e.g. `bmad-agent-pm.toml`, not `bmad-dev.toml`)
- Check TOML syntax: quoted strings, `[section]` for tables, `[[section]]` for array-of-tables, scalar/array keys must appear *before* any `[[subtables]]`
- Agent fields live under `[agent]` — fields below that header belong to `agent` until another table header begins
- `agent.name` and `agent.title` are read-only; overrides there have no effect

**Updates broke my customization?**
- Did you copy the full `customize.toml` into the override? **Don't.** Override files should contain only changed fields. A full copy locks in old defaults and silently drifts every release. Trim back to deltas.

**Need to see what's customizable?**
- Run the `bmad-customize` skill — enumerates every customizable skill, shows existing overrides, and walks you through adding/updating one
- Or read the skill's `customize.toml` directly — every field there is customizable (except `name` and `title`)

**Need to reset?**
- Delete the override file from `_bmad/custom/` — the skill falls back to built-in defaults

#bmad-method #customization #agents #workflows
