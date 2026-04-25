---
title: Workflow & Skill Patterns
url: https://bmad-builder-docs.bmad-method.org/reference/workflow-patterns/
source: sitemap
fetched_at: 2026-04-08T11:33:20.151386747-03:00
rendered_js: false
word_count: 297
summary: 'This document serves as a taxonomy and reference guide detailing how the BMad Builder classifies skills into three types: Simple Utility, Simple Workflow, and Complex Workflow. It outlines the structural patterns, defining signals, and applicable use cases for each skill type.'
tags:
    - skill-taxonomy
    - bmad-builder
    - workflow-types
    - skill-structure
    - headless-mode
    - simple-utility
category: reference
---

Reference for how the BMad Builder classifies and structures skills. Every skill falls into one of three types, each with a distinct structure and set of signals.

## Skill Type Taxonomy

[Section titled “Skill Type Taxonomy”](#skill-type-taxonomy)

TypeDescriptionStructure**Simple Utility**Input/output building block. Headless, composable, often script-driven. May opt out of config loading for true standalone useSKILL.md + `scripts/`**Simple Workflow**Multi-step process contained in a single SKILL.md. Loads config directly from module config.yaml. Minimal or no `prompts/`SKILL.md + optional `resources/`**Complex Workflow**Multi-stage with progressive disclosure, stage prompts in `prompts/`, config integration. May support headless modeSKILL.md (routing) + `prompts/` stages + `resources/`

```plaintext

1. Is it a composable building block with clear input/output?
└─ YES → Simple Utility
└─ NO ↓
2. Can it fit in a single SKILL.md without progressive disclosure?
└─ YES → Simple Workflow
└─ NO ↓
3. Does it need multiple stages, long-running process, or progressive disclosure?
└─ YES → Complex Workflow
```

## Classification Signals

[Section titled “Classification Signals”](#classification-signals)

- Clear input → processing → output pattern
- No user interaction needed during execution
- Other skills and workflows call it
- Deterministic or near-deterministic behavior
- Could be a script but needs LLM judgment
- Examples: JSON validator, format converter, file structure checker

<!--THE END-->

- 3-8 numbered steps
- User interaction at specific points
- Uses standard tools (gh, git, npm, etc.)
- Produces a single output artifact
- No need to track state across compactions
- Examples: PR creator, deployment checklist, code review

<!--THE END-->

- Multiple distinct phases or stages
- Long-running (likely to hit context compaction)
- Progressive disclosure needed (too much for one file)
- Routing logic in SKILL.md dispatches to stage prompts
- Produces multiple artifacts across stages
- May support headless/autonomous mode
- Examples: agent builder, module builder, project scaffolder

## Structure Patterns

[Section titled “Structure Patterns”](#structure-patterns)

```plaintext

bmad-my-utility/
├── SKILL.md              # Complete instructions, input/output spec
└── scripts/              # Core logic
├── process.py
└── tests/
```

```plaintext

bmad-my-workflow/
├── SKILL.md              # Steps inline, config loading, output spec
└── resources/            # Optional reference data
```

```plaintext

bmad-my-complex-workflow/
├── SKILL.md              # Routing logic, dispatches to prompts/
├── prompts/              # Stage instructions
│   ├── 01-discovery.md
│   ├── 02-planning.md
│   ├── 03-execution.md
│   └── 04-review.md
├── resources/            # Reference data, templates, schemas
├── agents/               # Subagent definitions for parallel work
└── scripts/              # Deterministic operations
└── tests/
```

ModelApplicable TypesDescription**Interactive**AllUser invokes skill and interacts conversationally**Headless / Autonomous**Simple Utility, Complex WorkflowRuns without user interaction; takes inputs, produces outputs**YOLO**Simple Workflow, Complex WorkflowUser brain-dumps; builder drafts the full artifact, then refines**Guided**Simple Workflow, Complex WorkflowSection-by-section discovery with soft gates at transitions

Module membership is orthogonal to skill type. Any type can be standalone or part of a module.

ContextNamingInit**Module-based**`{modulecode}-{skillname}`Loads config from module config.yaml**Standalone**`{skillname}`Loads config from module config.yaml; simple utilities may opt out