---
title: Progressive Disclosure in Skills
url: https://bmad-builder-docs.bmad-method.org/explanation/progressive-disclosure/
source: sitemap
fetched_at: 2026-04-08T11:33:02.051841471-03:00
rendered_js: false
word_count: 396
summary: This document explains progressive disclosure techniques for designing agent skills by introducing four layers of context loading (Frontmatter/Body, On-Demand Resources, Dynamic Routing, and Step Files). It also details the 'document-as-cache' pattern for maintaining state in long workflows.
tags:
    - agent-skill-design
    - progressive-disclosure
    - llm-context-management
    - workflow-structuring
    - layering-system
category: guide
---

Progressive disclosure is what separates basic skills from powerful ones. The core idea: never load more context than the agent needs *right now*. This keeps token usage low, prevents context pollution, and lets skills survive long conversations.

Skills can use any combination of these layers. Most production skills use Layers 1-3. Layer 4 is reserved for strict sequential processes.

LayerWhat It DoesToken Cost**1. Frontmatter vs Body**Frontmatter is always in context; body loads only when triggered~100 tokens always, body on demand**2. On-Demand Resources**SKILL.md points to resources and scripts loaded only when relevantZero until needed**3. Dynamic Routing**SKILL.md acts as a router, dispatching to entirely different prompt flowsOnly the chosen path loads**4. Step Files**Agent reads one step at a time, never sees aheadOne step’s worth at a time

## Layer 1: Frontmatter vs Body

[Section titled “Layer 1: Frontmatter vs Body”](#layer-1-frontmatter-vs-body)

Frontmatter (name + description) is **always in context**. It is how the LLM decides whether to load the skill. The body only loads when the skill triggers.

This means frontmatter must be precise and include trigger phrases. The body stays under 500 lines and pushes detail into Layers 2-3.

```markdown

---
name: bmad-my-skill
description: Validates API contracts against OpenAPI specs. Use when user says 'validate API' or 'check contract'.
---
# Body loads only when triggered
...
```

## Layer 2: On-Demand Resources

[Section titled “Layer 2: On-Demand Resources”](#layer-2-on-demand-resources)

SKILL.md points to resources loaded only when relevant. This includes both **reference files** (context for the LLM) and **scripts** (offload work from the LLM entirely).

```markdown

## Which Guide to Read
- Python project → Read `resources/python.md`
- TypeScript project → Read `resources/typescript.md`
- Need validation → Run `scripts/validate.py` (don't read the script, just run it)
```

Scripts are particularly powerful here: the LLM does not process the logic, it just calls the script and receives structured output. This offloads deterministic work and saves tokens.

## Layer 3: Dynamic Routing

[Section titled “Layer 3: Dynamic Routing”](#layer-3-dynamic-routing)

The skill body acts as a **router** that dispatches to entirely different prompt flows, scripts, or external skills based on what the user is asking for.

```markdown

## What Are You Trying To Do?
### "Build a new workflow"
→ Read `prompts/create-flow.md` and follow its instructions
### "Review an existing workflow"
→ Read `prompts/review-flow.md` and follow its instructions
### "Run analysis"
→ Run `scripts/analyze.py --target <path>` and present results
```

The key difference from Layer 2: Layer 2 loads supplementary resources alongside the skill body. Layer 3 **branches the entire execution path**: different prompts, different scripts, different skills. The skill body becomes a dispatcher, not an instruction set.

## Layer 4: Step Files

[Section titled “Layer 4: Step Files”](#layer-4-step-files)

The most restrictive pattern. The agent reads **one step file at a time**, does not know what is next, and waits for user confirmation before proceeding.

```plaintext

prompts/
├── step-01.md  ← agent reads ONLY current step
├── step-02.md  ← loaded after user confirms step 1
├── step-03a.md ← branching path A
└── step-03b.md ← branching path B
```

**When to use:** Only when you need exact sequential progression with no skipping, compaction-resistance (each step is self-contained), or the agent deliberately constrained from looking ahead.

**Trade-off:** Very rigid. Limits the agent’s ability to adapt, combine steps, or be creative. Do not use for exploratory or creative tasks. Do not use when Layer 3 routing would suffice. Try to follow level 1-3 first! The lowest level needed is best.

## Compaction Survival

[Section titled “Compaction Survival”](#compaction-survival)

Long-running workflows risk losing context when the conversation compresses. The **document-as-cache pattern** solves this: the output document itself stores the workflow’s state.

ComponentPurpose**YAML front matter**Paths to input files, current stage status, timestamps**Draft sections**Progressive content built across stages**Status marker**Which stage is complete, for resumption

Each stage reads the output document to restore context, does its work, and writes results back to the same document. If context compacts mid-workflow, the next stage recovers by reading the document and reloading the input files listed in front matter.

```markdown

---
title: 'Analysis: Research Topic'
status: 'analysis'
inputs:
- '{project_root}/docs/brief.md'
- '{project_root}/data/sources.json'
---
```

This avoids separate cache files, file collisions when running multiple workflows, and state synchronization complexity.

## Choosing the Right Layer

[Section titled “Choosing the Right Layer”](#choosing-the-right-layer)

SituationRecommended LayerSingle-purpose utility with one pathLayer 1-2Skill with conditional reference dataLayer 2Skill that does multiple distinct thingsLayer 3Skill with stages that depend on each otherLayer 3 + compaction survivalStrict sequential process, no skipping allowedLayer 4Long-running workflow producing a documentLayer 3 + document-as-cache