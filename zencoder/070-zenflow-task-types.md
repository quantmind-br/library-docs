---
title: Task Types and Custom Workflows - Zencoder Docs
url: https://docs.zencoder.ai/zenflow/task-types#custom-workflows
source: crawler
fetched_at: 2026-01-23T09:28:34.411582159-03:00
rendered_js: false
word_count: 550
summary: This document explains the process of creating and managing tasks in Zenflow, detailing the use of Git worktrees for workspace isolation and how to configure custom task workflows using markdown templates.
tags:
    - zenflow
    - task-management
    - git-worktrees
    - workflow-configuration
    - parallel-execution
    - custom-workflows
category: guide
---

## Overview

Every Zenflow project starts by picking a task type. When a project is empty you see four full-width cards—**Quick Change**, **Fix Bug**, **Spec and Build**, and **Full SDD Workflow**—each describing how the next task will run. Selecting a card launches the task creation modal and seeds the right workflow for the Task column.

* * *

## Creating a Task

The modal follows the same steps regardless of type:

![Zenflow task creation modal showing description, workspace, and automation settings](https://mintcdn.com/forgoodaiinc/7c2Qaq-Q86Otnmis/images/zenflow/zenflow-first-task-modal-full.png?fit=max&auto=format&n=7c2Qaq-Q86Otnmis&q=85&s=e76eb2b90c111b8a03292c250d5056bd)

* * *

## Understanding Git Worktrees in Zenflow

Every task in Zenflow runs in its own **isolated workspace** powered by Git worktrees. This is what enables true parallel execution—multiple agents working simultaneously without stepping on each other’s changes.

### The Basics

**Git worktrees** allow you to check out multiple branches from the same repository at once, each in its own directory. Instead of switching branches and stashing changes, you work in separate directories that all share the same Git history. When you create a task in Zenflow:

- A new worktree is created at `.zenflow/tasks/{task_id}`
- A dedicated branch is created for that task
- Agents work in this isolated directory without affecting your main workspace
- Changes remain completely separate until you merge

### Working with the IDE

Keep the agent and your editor aligned by following these patterns.

![Zenflow Changes page showing Commit and Discard buttons for manual edits](https://mintcdn.com/forgoodaiinc/dxvTNL2j2V_95Nst/images/zenflow/zenflow-changes-commit-buttons.png?fit=max&auto=format&n=dxvTNL2j2V_95Nst&q=85&s=057bc1d51dc89645ff6964bba9ac1154)

### Best Practices

### Common Issues

* * *

## Task Type Reference

Each type seeds `.zenflow/tasks/{task_id}` with artifacts and determines what appears in the middle column. Use the summaries below to pick the right fit.

### Quick Change

### Fix Bug

### Spec and Build

### Full SDD Workflow

> Picking the closest match upfront keeps reporting, Kanban views, and automation accurate. You can still change the type later if the work evolves.

* * *

Custom workflows let you design additional task templates beyond the four built-ins. Add a Markdown file describing the workflow steps to `.zenflow/workflows/` in your repo root and Zenflow will surface it alongside the default options when creating a task.

### Common Structure

Typical workflow files share these traits:

- **Title and configuration:** Start with an `#`-level heading plus a **Configuration** section that sets shared context—typically an `Artifacts Path` pointing to `{@artifacts_path}` (`.zenflow/tasks/{task_id}`).
- **Workflow steps:** Each step is written as `### [ ] Step: {Name}` so it slots into the Steps column with unchecked boxes.
- **Detailed instructions:** Under each step, describe objectives, acceptance criteria, and links to artifacts. The spec-focused steps output `spec.md`, optional planning uses `plan.md`, implementation steps create `report.md`, and review steps modify the prior artifact.
- **Optional reviews:** You can insert extra stages such as “Specification Review” between the spec and implementation to enforce approvals or QA.

```
# Example Custom Workflow

## Configuration
- **Artifacts Path**: {@artifacts_path} → `.zenflow/tasks/{task_id}`

---

## Workflow Steps

### [ ] Step: Planning
Describe what information belongs here (requirements, scope, links). Reference `{@artifacts_path}/plan.md` if you need a persistent doc.

### [ ] Step: Implementation
Outline how code should be written, tested, and saved. Mention deliverables such as `{@artifacts_path}/report.md` if useful.

### [ ] Step: Review & Wrap-Up
Explain what to double-check (tests, documentation, approvals) before marking the task complete.
```

- Scope steps so each represents a coherent milestone (e.g., “Technical Specification,” “Implementation,” “Review”).
- Reference artifact placeholders (`{@artifacts_path}/spec.md`) so Zenflow resolves per-task paths automatically.
- Use enumerated lists for actions and highlight decision criteria (approve vs. change requested) if the workflow requires loops.
- Keep wording imperative so agents understand expected deliverables and verification requirements.