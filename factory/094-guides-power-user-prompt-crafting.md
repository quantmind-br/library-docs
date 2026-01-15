---
title: Prompt Crafting for Different Models - Factory Documentation
url: https://docs.factory.ai/guides/power-user/prompt-crafting
source: sitemap
fetched_at: 2026-01-13T19:03:34.791270742-03:00
rendered_js: false
word_count: 557
summary: A guide explaining model-specific prompting techniques for Claude, GPT, and Gemini, including instructions for creating custom prompt refiner skills and strategies for selecting the appropriate AI model for different tasks.
tags:
    - prompt-engineering
    - ai-models
    - claude
    - gpt
    - gemini
    - skills
    - best-practices
category: guide
---

Different AI models respond better to different prompting styles. This guide covers model-specific techniques and provides ready-to-use prompt refiner skills.

* * *

## Universal Prompting Principles

These principles work across all models:

* * *

## Claude Models (Opus, Sonnet, Haiku)

Claude models excel with structured, explicit instructions and respond particularly well to certain formatting patterns.

### Key Techniques for Claude

### Claude Prompt Refiner Skill

Create `~/.factory/skills/prompt-refiner-claude/SKILL.md`:

```
---
name: prompt-refiner-claude
description: Refine prompts for Claude models (Opus, Sonnet, Haiku) using Anthropic's best practices. Use when preparing complex tasks for Claude.
---

# Claude Prompt Refiner

## When to Use
Invoke this skill when you have a task for Claude that:
- Involves multiple steps or files
- Requires specific output formatting
- Needs careful reasoning or analysis
- Would benefit from structured context

## Refinement Process

### 1. Analyze the Draft Prompt
Review the user's prompt for:
- [ ] Clear outcome definition
- [ ] Sufficient context
- [ ] Explicit constraints
- [ ] Success criteria

### 2. Apply Claude-Specific Patterns

**Structure with XML tags:**
- `<context>` - Background information, codebase state
- `<task>` - The specific action to take
- `<requirements>` - Must-have criteria
- `<constraints>` - Limitations and boundaries
- `<examples>` - Sample inputs/outputs if helpful

**Ordering matters:**
1. Context first (what exists)
2. Task second (what to do)
3. Requirements third (how to do it)
4. Examples last (clarifying edge cases)

### 3. Enhance for Reasoning
For complex tasks, add:
- "Think through the approach before implementing"
- "Consider these edge cases: ..."
- "Explain your reasoning for key decisions"

### 4. Output the Refined Prompt
Present the improved prompt with:
- Clear section headers
- XML tags where beneficial
- Specific, measurable criteria

## Example Transformation

**Before:**
"Add caching to the API"

**After:**
```

* * *

## GPT Models (GPT-5, GPT-5.1, Codex)

GPT models excel with clear system-level context and benefit from explicit role framing.

### Key Techniques for GPT

### GPT Prompt Refiner Skill

Create `~/.factory/skills/prompt-refiner-gpt/SKILL.md`:

```
---
name: prompt-refiner-gpt
description: Refine prompts for GPT models (GPT-5, GPT-5.1, Codex) using OpenAI's best practices. Use when preparing complex tasks for GPT.
---

# GPT Prompt Refiner

## When to Use
Invoke this skill when you have a task for GPT that:
- Requires a specific persona or expertise
- Involves procedural steps
- Needs structured output
- Benefits from explicit examples

## Refinement Process

### 1. Analyze the Draft Prompt
Review for:
- [ ] Clear role/persona definition
- [ ] Step-by-step breakdown (if procedural)
- [ ] Output format specification
- [ ] Concrete examples

### 2. Apply GPT-Specific Patterns

**Role framing:**
Start with "You are a [specific role] working on [specific context]..."

**Numbered procedures:**
Break complex tasks into numbered steps that build on each other.

**Output specification:**
Be explicit: "Return as JSON", "Format as markdown with headers", etc.

**Chain of thought:**
For reasoning tasks, add: "Think through this step by step."

### 3. Structure the Prompt

**Effective order for GPT:**
1. Role definition (who/what)
2. Context (background info)
3. Task (what to do)
4. Steps (how to do it, if procedural)
5. Output format (what to return)
6. Examples (optional clarification)

### 4. Output the Refined Prompt
Present with:
- Clear role statement
- Numbered steps where applicable
- Explicit output requirements

## Example Transformation

**Before:**
"Review this code for security issues"

**After:**
```

You are a senior security engineer conducting a security audit of a Node.js payment processing service. Context: This service handles credit card transactions and communicates with Stripe’s API. It runs in AWS ECS. Task: Review the code in src/payments/ for security vulnerabilities. Steps:

1. Check for proper input validation on all endpoints
2. Verify secrets are not hardcoded or logged
3. Review authentication and authorization logic
4. Check for SQL injection and XSS vulnerabilities
5. Verify proper error handling that doesn’t leak sensitive info

Output format: Return a security report in markdown with:

- **Critical**: Issues that must be fixed before deployment
- **High**: Significant risks that should be addressed soon
- **Medium**: Improvements to consider
- **Recommendations**: General security enhancements

For each issue, include:

- File and line number
- Description of the vulnerability
- Recommended fix with code example

* * *

## Gemini Models

Gemini models handle long context well and work effectively with structured reasoning.

### Key Techniques for Gemini

* * *

## Model Selection Strategy

Match the model to the task:

Task TypeRecommended ModelReasoning Level**Complex architecture**Opus 4.5Medium-High**Feature implementation**Sonnet 4.5 or GPT-5.1-CodexMedium**Quick edits, formatting**Haiku 4.5Off/Low**Code review**GPT-5.1-Codex-MaxHigh**Bulk automation**GLM-4.6 (Droid Core)None**Research/analysis**Gemini 3 ProHigh

* * *

## Creating Your Own Prompt Refiner

For team-specific needs, create a custom prompt refiner:

```
---
name: prompt-refiner-team
description: Refine prompts using our team's conventions and project context.
---

# Team Prompt Refiner

## Our Conventions
- We use the repository pattern
- All services have interfaces defined first
- Tests use our custom test utilities from @/test-utils

## Checklist for Prompts
1. [ ] References relevant existing code
2. [ ] Specifies which layer (API, service, repository)
3. [ ] Mentions related tests to update
4. [ ] Includes acceptance criteria

## Template
```

Context: \[What exists, what module/layer] Task: \[Specific action] Patterns to follow: \[Reference existing similar code] Tests: \[What tests to add/update] Done when: \[Acceptance criteria]

* * *

## Quick Reference Card

### Claude (Opus/Sonnet/Haiku)

- ✅ XML tags for structure
- ✅ Context before instructions
- ✅ Examples in dedicated sections
- ✅ “Think through…” for reasoning

### GPT (GPT-5/Codex)

- ✅ Role framing (“You are a…”)
- ✅ Numbered step procedures
- ✅ Explicit output format
- ✅ “Step by step” for reasoning

### Gemini

- ✅ Extensive context inclusion
- ✅ Low/High reasoning levels
- ✅ Structured output requests

* * *

## Next Steps