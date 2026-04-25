---
title: Skills - Factory Documentation
url: https://docs.factory.ai/cli/configuration/skills
source: sitemap
fetched_at: 2026-04-15T09:00:42.01126395-03:00
rendered_js: false
word_count: 1212
summary: This document explains how to create, configure, and organize reusable Droid skills using Markdown files and YAML frontmatter to standardize engineering workflows and agent capabilities.
tags:
    - droid-skills
    - automation-workflows
    - agent-configuration
    - markdown-metadata
    - yaml-frontmatter
    - project-standardization
category: guide
---

Skills are **reusable capabilities** that extend what your Droid can do. Create a `SKILL.md` file with instructions, and the Droid adds it to its toolkit. The Droid uses skills when relevant, or you can invoke one directly with `/skill-name`.

**Key properties:**

- **Flexible invocation** – Both you and the Droid can invoke skills. Type `/skill-name` or let the Droid decide when to use them.
- **Composable** – can be chained together as part of larger workflows
- **Token-efficient** – lightweight and focused, not bloated with unused tools or repeated instructions

**A skill can be:**

- **A workflow** – step-by-step instructions (e.g., “navigate to URL, take screenshot, extract data”)
- **Expertise** – domain knowledge and conventions (e.g., “how we implement frontend features with our design system”)
- **Both** – instructions + tools + best practices bundled together

**Example skills:**

- `browser` – automate Chrome with CDP tools (navigate, screenshot, evaluate JS)
- `linear` – manage Linear issues with CLI tools (list, update status, move teams)
- `frontend-ui-integration` – implement typed React flows following team conventions

## What is a skill?

A skill is a **directory** (e.g. `.factory/skills/frontend-ui-integration/`) containing:

- `SKILL.md` or `skill.mdx` with YAML frontmatter and markdown instructions
- Optional supporting files (scripts, schemas, checklists)

Each skill defines what problem it solves, what inputs it expects, and what success looks like. The Droid automatically invokes matching skills when they apply to the current task.

## Skill file format

Skills are defined in Markdown with YAML frontmatter. A small, focused skill can be just a short `SKILL.md`:

```
---
name: summarize-diff
description: Summarize the staged git diff in 3–5 bullets. Use when the user asks for a summary of pending changes.
---

# Summarize Diff

## Instructions

1. Run `git diff --staged`.
2. Summarize the changes in 3–5 bullets, focusing on user-visible behavior.
3. Call out any migrations, risky areas, or tests that should be run.
```

You can also include additional frontmatter fields to control behavior. See [Frontmatter reference](#frontmatter-reference) for all available options.

## Where skills live

Skills are discovered from a small set of well-known locations:

ScopeLocationPurpose**Workspace**`<repo>/.factory/skills/`Project skills shared with teammates; checked into git.**Personal**`~/.factory/skills/`Private skills that follow you across projects on your machine.**Compatibility**`<repo>/.agent/skills/`Discovered for compatibility with `.agent` folder conventions.

Each **skill** lives in its own directory under one of these roots:

- Workspace: `<repo>/.factory/skills/<skill-name>/SKILL.md`
- Personal: `~/.factory/skills/<skill-name>/SKILL.md`

In large monorepos, you can either:

- Keep a **single, shared** skills folder at the root:
  
  ```
  .factory/skills/
    frontend/
      SKILL.md
    payments-service/
      SKILL.md
    data-warehouse-querying/
      SKILL.md
  ```
- Or add **per-project** `.factory` folders so skills live alongside each subproject:
  
  ```
  services/payments/.factory/skills/
    payments-service/
      SKILL.md
  apps/frontend/.factory/skills/
    dashboard-ui/
      SKILL.md
  ```

Project skills are the primary way to share and standardize capabilities inside an engineering org; personal skills are ideal for individual workflows or experiments.

## Frontmatter reference

Skills support YAML frontmatter fields between `---` markers at the top of your `SKILL.md` file:

```
---
name: my-skill
description: What this skill does and when to use it
user-invocable: true
disable-model-invocation: false
---

Your skill instructions here...
```

FieldRequiredDefaultDescription`name`NoDirectory nameDisplay name for the skill. Lowercase letters, numbers, and hyphens only.`description`Recommended—What the skill does and when to use it. The Droid uses this to decide when to apply the skill.`user-invocable`No`true`Set to `false` to hide from the `/` slash command menu. Use for background knowledge users shouldn’t invoke directly.`disable-model-invocation`No`false`Set to `true` to prevent the Droid from automatically loading this skill. Use for workflows you want to trigger manually with `/skill-name`.

## Control who invokes a skill

By default, both you and the Droid can invoke any skill. You can type `/skill-name` to invoke it directly, and the Droid can load it automatically when relevant to your conversation. Two frontmatter fields let you restrict this:

- **`disable-model-invocation: true`** : Only you can invoke the skill. Use this for workflows with side effects or that you want to control timing, like `/deploy` or `/send-notification`. You don’t want the Droid deciding to deploy because your code looks ready.
- **`user-invocable: false`** : Only the Droid can invoke the skill. Use this for background knowledge that isn’t actionable as a command. A `legacy-system-context` skill explains how an old system works. The Droid should know this when relevant, but `/legacy-system-context` isn’t a meaningful action for users to take.

### Invocation summary

FrontmatterUser can `/invoke`Droid can invoke(default)YesYes`disable-model-invocation: true`YesNo`user-invocable: false`NoYes

## Quickstart

## How skills differ from other configuration

Skills sit alongside other ways of shaping Droid behavior:

- **Custom droids** – define *which* model and tools to use and at what autonomy level; they are full agent configurations.
- **Legacy slash commands** (`.factory/commands/`) – user-invoked macros that still work but are now superseded by skills. Skills offer the same `/command` functionality plus optional Droid invocation and supporting files.
- **MCP servers** – expose external systems (APIs, databases, SaaS tools) as tools; they are about *connecting* resources, not encoding your workflow.

Skills are different because they:

- Package **how work should be done** (your engineering playbook) as reusable capabilities.
- Support **flexible invocation** – both you (via `/skill-name`) and the Droid can trigger them, with [fine-grained control](#control-who-invokes-a-skill) over who can invoke what.
- Are **discoverable and composable** – the Droid can chain multiple skills inside a plan.
- Can sit on top of tools, custom droids, and MCP servers to orchestrate them safely.

In practice you might:

- Use MCP to expose your internal deployment API.
- Use a custom droid to define which tools/models are allowed in CI.
- Use a skill to encode “how to safely roll out a canary deployment” using that API and droid configuration.

## Why skills matter in enterprise codebases

Skills are especially valuable in enterprise environments where you need to:

- Standardize how Droids do **frontend implementation, service integrations, data querying, and internal tools**.
- Encode **team conventions, safety rules, and SLAs** once, then reuse them across projects.
- Make automation **discoverable, auditable, and shareable** via git, not just “whatever happened in one chat”.

You can create skills from scratch for Factory, or reuse existing skills you already invested in for other agents by importing them and wiring them into your droid configuration.

## Best practices

## Cookbook

The cookbook provides opinionated skill templates aimed at common enterprise software workflows. We focus on nine families of skills:

1. [**Frontend implementation skills**](https://docs.factory.ai/guides/skills/frontend-ui-integration) – building UI surfaces that integrate with existing APIs
2. [**Integration skills for complex codebases**](https://docs.factory.ai/cli/configuration/skills/service-integration) – extending or wiring together services in large monorepos
3. [**Internal data querying skills**](https://docs.factory.ai/cli/configuration/skills/data-querying) – safe, auditable access to internal analytics or data services
4. [**Internal tools skills**](https://docs.factory.ai/cli/configuration/skills/internal-tools) – building small but robust internal apps that improve developer and operator workflows
5. [**Vibe coding skills**](https://docs.factory.ai/cli/configuration/skills/vibe-coding) – rapidly prototyping and building complete modern web applications from scratch (Lovable/Bolt/v0 replacement)
6. [**AI data analyst skills**](https://docs.factory.ai/cli/configuration/skills/ai-data-analyst) – comprehensive data analysis, visualization, and statistical modeling (data analyst tool replacement)
7. [**Product management skills**](https://docs.factory.ai/cli/configuration/skills/product-management) – assisting with PRDs, feature analysis, and PM workflows (PM tool augmentation)
8. [**Browser automation skills**](https://docs.factory.ai/cli/configuration/skills/browser) – launching Chrome via CDP, navigating live tabs, evaluating DOM state, and collecting screenshots or selectors without running an MCP server
9. [**Automated QA skills**](https://docs.factory.ai/guides/skills/automated-qa) – end-to-end quality assurance that tests your application as a real user would, with visual evidence, CI integration, and failure learning

In practice, each skill folder can also contain **supporting utilities** the agent may use alongside the core prompt template – for example:

- `SKILL.md` or `skill.mdx` – the main skill specification
- `references.md` – links and pointers to types, APIs, and modules that already exist in your codebase
- `schemas/` – JSON/YAML schemas or OpenAPI snippets referenced by the skill (not the source-of-truth service code)
- `checklists.md` – reusable validation or rollout checklists

These co-located files give the agent a predictable, structured bundle of context to work from when the skill is invoked, without duplicating or relocating production code. Use these as starting points and adapt the inputs, constraints, and verification steps to match your stack and governance requirements.