---
title: Solve Complex Problems
url: https://cis-docs.bmad-method.org/how-to/problem-solving/
source: sitemap
fetched_at: 2026-04-08T11:33:53.336514386-03:00
rendered_js: false
word_count: 386
summary: This document outlines a structured, five-step workflow using an assistant persona (Dr. Quinn) to systematically diagnose complex problems, identify root causes through analytical frameworks, and generate actionable, evaluated solutions.
tags:
    - problem-solving
    - root-cause-analysis
    - diagnostic-workflow
    - analytical-frameworks
    - troubleshooting
category: guide
---

Use the `problem-solving` workflow to systematically diagnose problems, identify root causes, and develop effective solutions using proven analytical frameworks.

- Facing a complex, persistent challenge
- Need to understand root causes before fixing symptoms
- Multiple solution options exist and you need to choose
- Problems recur despite previous attempts to fix them
- Issues span multiple systems or components

## When to Skip This

[Section titled “When to Skip This”](#when-to-skip-this)

- Well-understood problems with obvious solutions
- Simple, isolated bugs or issues
- Time-critical situations requiring immediate action

### 1. Load Dr. Quinn

[Section titled “1. Load Dr. Quinn”](#1-load-dr-quinn)

Start a fresh chat and load the Problem Solver:

### 2. Describe Your Problem

[Section titled “2. Describe Your Problem”](#2-describe-your-problem)

Dr. Quinn will ask about your challenge. Be specific about symptoms:

**Good problem descriptions:**

- “Users abandon checkout after entering payment info 40% of the time”
- “The database query takes 30 seconds when user count exceeds 1000”
- “Customer support tickets increased 300% after the last release”

**Less effective:**

- “Fix performance” (too vague)
- “The app is slow” (no specifics)

### 3. Diagnose the Problem

[Section titled “3. Diagnose the Problem”](#3-diagnose-the-problem)

Dr. Quinn treats problems like puzzles and guides you through:

Diagnostic StepGoal**Symptom analysis**Separate what you see from what’s causing it**Boundary definition**Understand where the problem lives and doesn’t**History review**What changed, when, and what was attempted

### 4. Apply Analytical Frameworks

[Section titled “4. Apply Analytical Frameworks”](#4-apply-analytical-frameworks)

Dr. Quinn selects from his solving-methods library:

FrameworkBest For**Five Whys**Quick root cause drilling**TRIZ**Technical contradictions and inventive solutions**Theory of Constraints**System bottlenecks and flow**Systems Thinking**Interconnected, recurring issues**Root Cause Analysis**Comprehensive causal mapping

### 5. Generate and Evaluate Solutions

[Section titled “5. Generate and Evaluate Solutions”](#5-generate-and-evaluate-solutions)

Once root causes are identified:

1. **Diverge** — Generate multiple solution approaches
2. **Evaluate** — Assess pros, cons, and trade-offs
3. **Select** — Choose based on effectiveness and feasibility
4. **Plan** — Create implementation steps with risk mitigation

Output saved to `_bmad-output/problem-solution-{date}.md`:

SectionContents**Problem Statement**Clearly defined challenge with symptoms**Diagnosis**Root cause analysis using selected frameworks**Solution Options**Multiple approaches with pros/cons**Recommended Solution**Best option with rationale**Implementation Plan**Actionable steps and timeline**Risk Mitigation**What could go wrong and how to prevent it**Success Metrics**How to measure effectiveness

```text

You: /cis-problem-solving
Dr. Quinn: What puzzle are we solving today?
You: User engagement dropped 50% after our last release.
Dr. Quinn: Fascinating symptom. Let's drill down.
[Applies Five Whys]
Why did engagement drop?
You: Users aren't opening the app.
Dr. Quinn: Why aren't they opening it?
You: Push notifications stopped working.
Dr. Quinn: Why did notifications stop?
You: The API changed and we didn't update.
Dr. Quinn: Aha! Root cause: Missing API integration.
But why wasn't this caught in testing?
[Drills deeper into process issues]
[Identifies multiple root causes]
[Generates solution options]
[Creates implementation plan with safeguards]
```

After problem-solving:

- Use **brainstorming** (`/cis-brainstorm`) to generate creative solutions
- Apply **innovation strategy** (`/cis-innovation-strategy`) if the problem requires strategic pivots
- Use **design thinking** (`/cis-design-thinking`) if users are experiencing the problem

## Providing Context

[Section titled “Providing Context”](#providing-context)

For best results, provide problem context via the `--data` flag:

```bash

workflowcis-problem-solving--data/path/to/problem-brief.md
```

Dr. Quinn will use this context to accelerate the diagnostic phase.