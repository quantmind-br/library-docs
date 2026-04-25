---
title: Skill Authoring Best Practices
url: https://bmad-builder-docs.bmad-method.org/explanation/skill-authoring-best-practices/
source: sitemap
fetched_at: 2026-04-08T11:33:05.706220734-03:00
rendered_js: false
word_count: 869
summary: This document provides detailed best practices for writing robust and adaptable AI agent instructions, covering core principles like informed autonomy, structuring workflows with soft gates, managing context flow, and designing multi-faceted outputs.
tags:
    - ai-agent-design
    - prompt-engineering
    - workflow-guidelines
    - llm-best-practices
    - context-management
    - system-architecture
category: guide
---

Practical guidance for writing skills that work reliably and adapt gracefully. These patterns apply to agents, workflows, and utilities alike.

## Core Principle: Informed Autonomy

[Section titled “Core Principle: Informed Autonomy”](#core-principle-informed-autonomy)

Give the executing agent enough context to make good judgment calls, not just enough to follow steps. The test for every piece of content: “Would the agent make *better decisions* with this context?” If yes, keep it. If it is genuinely redundant, cut it.

Simple utilities need minimal context; input/output is self-explanatory. Interactive workflows need domain understanding, user perspective, and rationale for non-obvious choices. When in doubt, explain *why*. An agent that understands the mission improvises better than one following blind steps.

Match specificity to task fragility.

FreedomWhen to UseExample**High** (text instructions)Multiple valid approaches, context-dependent”Analyze structure, check for issues, suggest improvements”**Medium** (pseudocode/templates)Preferred pattern exists, some variation OK`def generate_report(data, format="markdown"):`**Low** (exact scripts)Fragile operations, consistency critical`python scripts/migrate.py --verify --backup` (do not modify)

**Analogy:** Narrow bridge with cliffs = low freedom. Open field = high freedom.

## Quality Dimensions

[Section titled “Quality Dimensions”](#quality-dimensions)

Six dimensions to keep in mind during the build phase. The quality scanners check these automatically during optimization.

DimensionWhat It Means**Informed Autonomy**Overview establishes domain framing, theory of mind, and design rationale, enough for judgment calls**Intelligence Placement**Scripts handle plumbing (fetch, transform, validate). Prompts handle judgment (interpret, classify, decide). If a script contains an `if` that decides what content *means*, intelligence has leaked**Progressive Disclosure**SKILL.md stays focused; stage instructions go in `prompts/`, reference data in `resources/`**Description Format**Two parts: `[5-8 word summary]. [Use when user says 'X' or 'Y'.]`. Default to conservative triggering**Path Construction**Never use `{skill-root}`. Use `{project-root}` for any project-scope path, `./` for skill-internal. Config variables used directly; they already contain `{project-root}`**Token Efficiency**Remove genuine waste (repetition, defensive padding). Preserve context that enables judgment (domain framing, rationale)

### Soft Gate Elicitation

[Section titled “Soft Gate Elicitation”](#soft-gate-elicitation)

For guided workflows, use “anything else?” soft gates at natural transition points instead of hard menus.

```markdown

Present what you've captured so far, then:
"Anything else you'd like to add, or shall we move on?"
```

Users almost always remember one more thing when given a graceful exit ramp rather than a hard stop. This consistently produces richer artifacts than rigid section-by-section questioning. Use at every natural transition in collaborative discovery workflows. Skip in autonomous/headless execution.

### Intent-Before-Ingestion

[Section titled “Intent-Before-Ingestion”](#intent-before-ingestion)

Never scan artifacts or project context until you understand WHY the user is here. Without knowing intent, you cannot judge what is relevant in a 100-page document.

```markdown

1. Greet and understand intent
2. Accept whatever inputs the user offers
3. Ask if they have additional context
4. ONLY THEN scan artifacts, scoped to relevance
```

### Capture-Don’t-Interrupt

[Section titled “Capture-Don’t-Interrupt”](#capture-dont-interrupt)

When users provide information beyond the current scope (dropping requirements during a product brief, mentioning platforms during vision discovery), capture it silently for later use rather than redirecting them.

Users in creative flow share their best insights unprompted. Interrupting to say “we’ll cover that later” kills momentum and may lose the insight entirely.

### Dual-Output: Human Artifact + LLM Distillate

[Section titled “Dual-Output: Human Artifact + LLM Distillate”](#dual-output-human-artifact--llm-distillate)

Any artifact-producing workflow can output two complementary documents: a polished human-facing artifact AND a token-conscious, structured distillate optimized for downstream LLM consumption.

OutputPurpose**Primary**Human-facing document: concise, well-structured**Distillate**Dense, structured summary for downstream LLM workflows: captures overflow, rejected ideas (so downstream does not re-propose them), detail bullets with enough context to stand alone

The distillate bridges the gap between what belongs in the human document and what downstream workflows need. Always offered to the user, never forced.

### Three-Mode Architecture

[Section titled “Three-Mode Architecture”](#three-mode-architecture)

Interactive workflows can offer three execution modes matching different user contexts.

ModeTriggerBehavior**Guided**DefaultSection-by-section with soft gates; drafts from what it knows, questions what it doesn’t**YOLO**`--yolo` or “just draft it”Ingests everything, drafts complete artifact upfront, then walks user through refinement**Headless (Autonomous)**`--headless` / `-H`Headless; takes inputs, produces artifact, no interaction

Not every workflow needs all three, but considering them during design prevents painting yourself into a single interaction model.

### Parallel Review Lenses

[Section titled “Parallel Review Lenses”](#parallel-review-lenses)

Before finalizing any significant artifact, fan out multiple reviewers with different perspectives.

ReviewerFocus**Skeptic**What is missing? What assumptions are untested?**Opportunity Spotter**What adjacent value? What angles?**Contextual**LLM picks the best third lens for the domain (regulatory risk for healthtech, DX critic for devtools)

Graceful degradation: if subagents are unavailable, the main agent does a single critical self-review pass.

### Graceful Degradation

[Section titled “Graceful Degradation”](#graceful-degradation)

Every subagent-dependent feature should have a fallback path. Skills run across different platforms, models, and configurations. A skill that hard-fails without subagents is fragile. One that falls back to sequential processing works everywhere.

### Verifiable Intermediate Outputs

[Section titled “Verifiable Intermediate Outputs”](#verifiable-intermediate-outputs)

For complex tasks: plan, validate, execute, verify.

1. Analyze inputs
2. Create `changes.json` with planned updates
3. Validate with script before executing
4. Execute changes
5. Verify output

Catches errors early, is machine-verifiable, and makes planning reversible.

## Writing Guidelines

[Section titled “Writing Guidelines”](#writing-guidelines)

DoAvoidConsistent terminology: one term per conceptSwitching between “workflow” and “process” for the same thingThird person in descriptions: “Processes files”First person: “I help process files”Descriptive file names: `form_validation_rules.md`Sequence names: `doc2.md`Forward slashes in all pathsBackslashes or platform-specific pathsOne level deep for references: SKILL.md → resource.mdNested references: SKILL.md → A.md → B.mdTable of contents for files over 100 linesLong files without navigation

Anti-PatternFixToo many options upfrontOne default with escape hatch for edge casesDeep reference nesting (A→B→C)Keep references one level from SKILL.mdInconsistent terminologyChoose one term per conceptVague file namesName by content, not sequenceScripts that classify meaning via regexIntelligence belongs in prompts, not scriptsOver-optimization that flattens personalityPreserve phrasing that captures the intended voiceHard-failing when subagents are unavailableAlways include a sequential fallback path