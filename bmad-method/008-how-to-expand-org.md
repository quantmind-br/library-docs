---
title: How to Expand BMad for Your Organization
url: https://docs.bmad-method.org//llms-full.txt
source: llms
fetched_at: 2026-05-19T08:33:05.038451722-03:00
rendered_js: false
summary: Customize BMad behavior org-wide using the three-layer mental model and advanced integration patterns.
tags:
    - bmad-method
    - organization
    - customization
    - enterprise
category: guide
optimized: true
optimized_at: 2026-05-19T11:33:00Z
word_count: 1547
---
# How to Expand BMad for Your Organization

Six recipes covering most enterprise customization needs. All compose — stack layers as needed without editing installed files or forking skills.

> [!info] Prerequisites
> - BMad installed ([[002-how-to-install-bmad|How to Install Bmad]])
> - Familiarity with customization model ([[007-how-to-customize|How to Customize BMad]])
> - Python 3.11+ on PATH (stdlib `tomllib` only)

> [!tip] Applying recipes
> Recipes 1–4 (per-skill) can be applied via the `bmad-customize` skill — it picks the right surface, authors the override, and verifies the merge. Recipe 5 (central-config agent roster) requires hand-authoring. The recipes here are the source of truth for *what* to override; `bmad-customize` handles the *how* for the agent/workflow surface.

## The Three-Layer Mental Model

| Layer | Override Location | Scope |
|---|---|---|
| **Agent** (Amelia, Mary, John) | `[agent]` in `_bmad/custom/bmad-agent-{role}.toml` | Travels into **every workflow the agent dispatches** |
| **Workflow** (product-brief, create-prd) | `[workflow]` in `_bmad/custom/{workflow-name}.toml` | Applies only to that workflow's run |
| **Central config** | `[agents.*]`, `[core]`, `[modules.*]` in `_bmad/custom/config.toml` | Agent roster, install settings pinned org-wide |

Rule of thumb: rule applies everywhere an engineer works → customize the **dev agent**. Rule applies only when writing a product brief → customize the **product-brief workflow**. Rule changes *who's in the room* → edit **central config**.

## Recipe 1: Shape an Agent Across Every Workflow

Standardize tool use and external integrations so every workflow dispatched through an agent inherits the behavior.

**Example — Amelia (dev agent) always uses Context7 for library docs, and falls back to Linear when a story isn't found in the epics list.**

```toml
# _bmad/custom/bmad-agent-dev.toml
[agent]
persistent_facts = [
  "For any library documentation lookup (React, TypeScript, Zod, Prisma, etc.), call the context7 MCP tool (`mcp__context7__resolve_library_id` then `mcp__context7__get_library_docs`) before relying on training-data knowledge. Up-to-date docs trump memorized APIs.",
  "When a story reference isn't found in {planning_artifacts}/epics-and-stories.md, search Linear via `mcp__linear__search_issues` using the story ID or title before asking the user to clarify. If Linear returns a match, treat it as the authoritative story source.",
]
```

**Why this works:** Two sentences reshape every dev workflow with no per-workflow duplication and no source changes. Every new engineer inherits the conventions automatically.

**Team file vs personal file:**
- `bmad-agent-dev.toml`: committed, whole team
- `bmad-agent-dev.user.toml`: gitignored, personal preferences layered on top

## Recipe 2: Enforce Organizational Conventions Inside a Workflow

Shape workflow output to meet compliance, audit, or downstream-consumer requirements.

**Example — every product brief must include compliance fields and knows org publishing conventions.**

```toml
# _bmad/custom/bmad-product-brief.toml
[workflow]
persistent_facts = [
  "Every brief must include an 'Owner' field, a 'Target Release' field, and a 'Security Review Status' field.",
  "Non-commercial briefs (internal tools, research projects) must still include a user-value section, but can omit market differentiation.",
  "file:{project-root}/docs/enterprise/brief-publishing-conventions.md",
]
```

Facts load during Step 3 of workflow activation. The shipped default (`file:{project-root}/**/project-context.md`) still loads — this is an append.

## Recipe 3: Publish Completed Outputs to External Systems

Once the workflow produces output, automatically publish to systems of record (Confluence, Notion, SharePoint) and open follow-up work (Jira, Linear, Asana).

**Example — briefs auto-publish to Confluence and offer optional Jira epic creation.**

```toml
# _bmad/custom/bmad-product-brief.toml
[workflow]
on_complete = """
Publish and offer follow-up:

1. Read the finalized brief file path from the prior step.
2. Call `mcp__atlassian__confluence_create_page` with:
   - space: "PRODUCT"
   - parent: "Product Briefs"
   - title: the brief's title
   - body: the brief's markdown contents
   Capture the returned page URL.
3. Tell the user: "Brief published to Confluence: <url>".
4. Ask: "Want me to open a Jira epic for this brief now?"
5. If yes, call `mcp__atlassian__jira_create_issue` with:
   - type: "Epic"
   - project: "PROD"
   - summary: the brief's title
   - description: a short summary plus a link back to the Confluence page.
   Report the epic key and URL.
6. If no, exit cleanly.

If either MCP tool fails, report the failure, print the brief path,
and ask the user to publish manually.
"""
```

**Why `on_complete` and not `activation_steps_append`:** `on_complete` runs once at the terminal stage, after the workflow's main output is written. `activation_steps_append` runs every activation, before the workflow does its work.

**Tradeoffs:**
- Confluence publication is non-destructive and always runs on completion
- Jira epic creation is visible to the whole team and kicks off sprint-planning signals, so gate it on user confirmation
- Graceful fallback: if MCP tools fail, hand off to the user rather than silently dropping the output

## Recipe 4: Swap in Your Own Output Template

Point the workflow at an enterprise-owned template when the default structure doesn't match org requirements.

```toml
# _bmad/custom/bmad-product-brief.toml
[workflow]
brief_template = "{project-root}/docs/enterprise/brief-template.md"
```

The workflow's `customize.toml` ships with `brief_template = "resources/brief-template.md"` (bare path, resolves from skill root). Your override points at a file under `{project-root}`, so the agent reads your template in Stage 4 instead of the shipped one.

**Template authoring tips:**
- Keep templates in `{project-root}/docs/` or `{project-root}/_bmad/custom/templates/` so they version alongside the override file
- Use the same structural conventions as the shipped template (section headings, frontmatter); the agent adapts to what's there
- For multi-org repos, use `.user.toml` to let individual teams point at their own templates without touching the committed team file

## Recipe 5: Customize the Agent Roster

Change *who's in the room* for roster-driven skills (`bmad-party-mode`, `bmad-retrospective`, `bmad-advanced-elicitation`) without editing source or forking.

### 5a. Rebrand a BMad Agent Org-Wide

```toml
# _bmad/custom/config.toml (committed)
[agents.bmad-agent-analyst]
description = "Mary the Regulatory-Aware Business Analyst — channels Porter and Minto, but lives and breathes FDA audit trails. Speaks like a forensic investigator presenting a case file."
```

Party-mode spawns Mary with the new description. The analyst activation itself still runs normally (behavior lives in her per-skill `customize.toml`). This changes how **external skills perceive and introduce her**, not how she works internally.

### 5b. Add a Fictional or Custom Agent

A full descriptor is enough for roster-based features, with no skill folder needed.

```toml
# _bmad/custom/config.user.toml (gitignored)
[agents.spock]
team = "startrek"
name = "Commander Spock"
title = "Science Officer"
icon = "🖖"
description = "Logic first, emotion suppressed. Begins observations with 'Fascinating.' Never rounds up. Counterpoint to any argument that relies on gut instinct."

[agents.mccoy]
team = "startrek"
name = "Dr. Leonard McCoy"
title = "Chief Medical Officer"
icon = "⚕️"
description = "Country doctor's warmth, short fuse. 'Dammit Jim, I'm a doctor not a ___.' Ethics-driven counterweight to Spock."
```

Ask party-mode to "invite the Enterprise crew." It filters by `team = "startrek"` and spawns Spock and McCoy. Real BMad agents can sit at the same table if you ask them to.

### 5c. Pin Team Install Settings

Pin shared answers so any developer's local prompt answer gets overridden at resolution time:

```toml
# _bmad/custom/config.toml
[modules.bmm]
planning_artifacts = "{project-root}/shared/planning"
implementation_artifacts = "{project-root}/shared/implementation"

[core]
document_output_language = "English"
```

Personal settings (user_name, communication_language, user_skill_level) stay under each developer's own `_bmad/config.user.toml`.

**Why central config vs per-agent customize.toml:** Per-agent files shape how *one* agent behaves when it activates. Central config shapes what roster consumers *see when they look at the field:* which agents exist, what they're called, what team they belong to, and shared install settings. Two surfaces, different jobs.

## Reinforce Global Rules in IDE Session File

BMad customizations load when a skill is activated. Many IDE tools also load a global instruction file at the **start of every session** before any skill runs (`CLAUDE.md`, `AGENTS.md`, `.cursor/rules/`, `.github/copilot-instructions.md`, etc.).

**When to double up:**
- Rule is important enough that a plain chat conversation (no skill active) should still follow it
- Belt-and-suspenders enforcement because training-data defaults might otherwise pull the model off-course
- Rule is concise enough to repeat without bloating the session file

**Example — one line in the repo's `CLAUDE.md` reinforcing the dev-agent rule from Recipe 1:**

```markdown
<!-- Any file-read of library docs goes through the context7 MCP tool
(`mcp__context7__resolve_library_id` then `mcp__context7__get_library_docs`)
before relying on training-data knowledge. -->
```

One sentence, loaded every session. Pairs with the `bmad-agent-dev.toml` customization so the rule applies both inside Amelia's workflows and during ad-hoc chats. Each layer owns its own scope:

| Layer | Scope | Use for |
|---|---|---|
| IDE session file (`CLAUDE.md` / `AGENTS.md`) | Every session, before any skill activates | Short, universal rules that should survive outside BMad |
| BMad agent customization | Every workflow the agent dispatches | Agent-persona-specific behavior |
| BMad workflow customization | One workflow run | Workflow-specific output shape, publishing hooks, templates |
| BMad central config | Agent roster + shared install settings | Who's in the room and what shared paths the team uses |

Keep the IDE file **succinct**. A dozen well-chosen lines are more effective than a sprawling list. Models read it every turn, and noise crowds out signal.

## Recipe 6: Advanced Integration Patterns

Several workflows expose richer configuration beyond Recipes 1–5. Check a workflow's `customize.toml` to see which fields it exposes. Examples below use `bmad-prd` because it exposes all of them, but the same patterns apply wherever the field appears.

### On-Demand Knowledge Sources (`external_sources`)

Connect the workflow to internal knowledge bases, competitive databases, or compliance references. The agent consults these on demand when the conversation surfaces a matching need — never preemptively.

```toml
# _bmad/custom/bmad-prd.toml
[workflow]
external_sources = [
  "When the user mentions a competitor or market segment, query corp:competitive_db (category={project_name}) before drafting the differentiation section.",
  "For regulatory domains (healthcare, fintech, education), consult corp:compliance_reference before drafting domain-specific sections.",
]
```

Each entry is a natural-language directive naming the MCP tool, trigger condition, and fields the tool needs. If unavailable at runtime, the workflow falls back to standard behavior and notes the gap.

### Automatic Output Publishing (`external_handoffs`)

Route completed artifacts to external systems of record after finalization. Unlike `on_complete` (Recipe 3), `external_handoffs` is a dedicated append array — team entries stack, and each handoff fires independently with graceful degradation if a tool is unavailable.

```toml
# _bmad/custom/bmad-prd.toml
[workflow]
external_handoffs = [
  "After finalize, upload prd.md and addendum.md to Confluence via corp:confluence_upload (space_key='PROD', parent_page='PRDs', label='prd', author={user_name}). Capture and surface the returned page URL.",
  "Mirror to Notion via notion:create_page (database_id='abc123', title='PRD: ' + {project_name}).",
]
```

If a named tool is unavailable, the handoff is skipped and flagged — local files always exist regardless.

### Finalize-Time Doc Standards (`doc_standards`)

Apply org writing standards to human-consumed documents at finalize, after content is complete but before the user sees the output. Each entry is a `skill:`, `file:`, or plain-text directive; passes run as parallel subagents.

```toml
# _bmad/custom/bmad-prd.toml
[workflow]
doc_standards = [
  "file:{project-root}/docs/enterprise/voice-and-tone.md",
  "All dates must use ISO 8601 format (YYYY-MM-DD).",
  "Replace any use of 'leverage' with 'use'.",
]
```

`doc_standards` is an append array — team entries stack on top of whatever defaults the workflow ships with. Broader structural passes should come before narrower prose passes.

### Swappable Templates and Checklists

Workflows that produce structured documents typically expose template and checklist paths as overridable scalars.

```toml
# _bmad/custom/bmad-prd.toml
[workflow]
prd_template = "{project-root}/docs/enterprise/prd-template-hipaa.md"
validation_checklist = "{project-root}/docs/enterprise/prd-checklist-regulated.md"
```

The agent adapts to whatever structure the template defines. Keep templates under `{project-root}/docs/` or `{project-root}/_bmad/custom/templates/` so they version alongside the override file. For multi-org repos, use `.user.toml` to let teams point at their own templates without touching the committed team file.

## Combining Recipes

All six recipes compose. A realistic enterprise override for `bmad-product-brief` might set `persistent_facts` (Recipe 2), `on_complete` (Recipe 3), and `brief_template` (Recipe 4) in one file. The agent-level rule (Recipe 1) lives in a separate file under the agent's name, central config (Recipe 5) pins the shared roster and team settings, advanced integration patterns (Recipe 6) configure external sources and handoffs, and all layers apply in parallel.

```toml
# _bmad/custom/bmad-product-brief.toml (workflow-level)
[workflow]
persistent_facts = ["..."]
brief_template = "{project-root}/docs/enterprise/brief-template.md"
on_complete = """ ... """
```

```toml
# _bmad/custom/bmad-agent-analyst.toml (agent-level)
[agent]
persistent_facts = ["Always include a 'Regulatory Review' section when the domain involves healthcare, finance, or children's data."]
```

Result: Mary loads the regulatory-review rule at persona activation. When the user picks the product-brief menu item, the workflow loads its own conventions on top, writes to the enterprise template, and publishes to Confluence on completion. Every layer contributes, and none required editing BMad source.

## Troubleshooting

**Override not taking effect?**
- Check that the file is under `_bmad/custom/` with the exact skill directory name (e.g. `bmad-agent-dev.toml`, not `bmad-dev.toml`). See [[007-how-to-customize#troubleshooting|How to Customize BMad — Troubleshooting]].

**MCP tool name unknown?**
- Use the exact name the MCP server exposes in the current session. Ask Claude Code to list available MCP tools if unsure. Hardcoded names in `persistent_facts` or `on_complete` won't work if the MCP server isn't connected.

**Pattern doesn't apply to my setup?**
- The recipes above are illustrative. The underlying machinery (three-layer merge, structural rules, agent-spans-workflow) supports many more patterns; compose them as needed.

#bmad-method #organization #customization #enterprise
