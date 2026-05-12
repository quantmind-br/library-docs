---
title: "Plan and Act Workflow in ForgeCode"
url: https://forgecode.dev/docs/plan-and-act-guide/
source: sitemap
fetched_at: 2026-04-30T14:09:15.476687648-03:00
rendered_js: false
word_count: 222
summary: "Use ForgeCode's dual-agent system: muse for planning, forge for implementation, to improve efficiency and safety."
tags:
  - ai-assisted-development
  - workflow-optimization
  - agent-collaboration
  - software-architecture
  - coding-best-practices
category: guide
optimized: true
---
# Plan and Act Workflow in ForgeCode

> **TL;DR**
> Plan with `muse` (read-only), implement with `forge` (read-write).

## Why Plan First?
- **Clarity**: Avoids mid-task confusion.
- **Safety**: Critical systems get reviewed before changes.
- **Efficiency**: Faster iteration with a solid plan.

## Agent Roles

| Agent | Mode | Purpose | When to Use |
|-------|------|---------|--------------|
| `muse` | Read-only | Analysis, planning | Before major changes |
| `forge` | Read-write | Implementation | After plan approval |

## Workflow Steps

1. **Plan with Muse**:
   ```bash
   :muse
   ```
   Prompt: "Create a detailed plan for [task]."

2. **Review the Plan**:
   - Check for gaps, edge cases, and integration points.

3. **Implement with Forge**:
   ```bash
   :forge
   ```
   Prompt: "Implement the plan from Muse."

4. **Iterate**: Switch back to `muse` for complex decisions.

## Best Practices
- **Specificity**: Include edge cases in planning requests.
- **Version Control**: Commit frequently.
- **Review**: Treat AI output like junior dev code.
- **Avoid Thrashing**: Minimize agent switching to preserve context.

## Benefits
- **Strategic Thinking**: `muse` focuses on analysis without implementation pressure.
- **Safety**: Critical systems reviewed before changes.
- **Speed**: `forge` implements quickly with a clear plan.

## Example Prompts
| Agent | Prompt Example |
|-------|----------------|
| `muse` | "Plan a refactor for the auth system, including edge cases." |
| `forge` | "Implement the refactor plan from Muse."