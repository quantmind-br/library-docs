---
title: Automations
url: https://developers.openai.com/codex/app/automations.md
source: llms
fetched_at: 2026-04-30T10:15:04.796200301-03:00
rendered_js: false
word_count: 830
summary: This document explains how to configure and manage recurring background automations in Codex, including task triage, project-scoped execution, thread-based workflows, and security considerations.
tags:
    - automation
    - background-tasks
    - workflow-optimization
    - git-worktrees
    - sandbox-security
    - codex-features
category: guide
optimized: true
optimized_at: 2026-04-30T13:30:00Z
---
# Automations

Automate recurring tasks in the background. Codex adds findings to the inbox or archives the task if there's nothing to report. Combine with [[037-skills|skills]] for complex tasks.

For project-scoped automations, the app must be running and the selected project available on disk.

In Git repositories, choose whether an automation runs in your local project or on a new [[008-app-worktrees|worktree]]. Worktrees keep automation changes separate from unfinished local work; local mode can modify files you're actively editing. In non-version-controlled projects, automations run directly in the project directory.

## Managing tasks

Find all automations and their runs in the automations pane in the Codex app sidebar.

The **Triage** section acts as your inbox. Automation runs with findings show up there; filter to show all runs or only unread ones.

Standalone automations start fresh runs on a schedule and report results in Triage. Use them when each run should be independent or when one automation should run across one or more projects. For custom cadence, choose a custom schedule and enter cron syntax.

For Git repositories, each automation can run in your local project or on a dedicated background worktree. Use worktrees to isolate changes from unfinished local work; use local mode when you want the automation to work directly in your main checkout. In non-version-controlled projects, automations run directly in the project directory. The same automation can run on more than one project.

Automations use your default sandbox settings. In read-only mode, tool calls fail if they require modifying files, network access, or working with apps on your computer. With full access enabled, background automations carry elevated risk. Adjust sandbox settings in [[051-app-settings|Settings]] and selectively allowlist commands with [[061-rules|rules]].

Automations can use the same plugins and skills available to Codex. To keep them maintainable and shareable, use skills to define the action and provide tools and context. Trigger a skill explicitly in an automation with `$skill-name`.

## Create or update from a thread

Describe the task, schedule, and whether the automation should stay attached to the current thread or start fresh runs. Codex drafts the prompt, chooses the automation type, and updates it when scope or cadence changes.

Examples:
- Remind you in this thread while a deployment finishes
- Create a standalone automation that checks a project on a recurring schedule

Skills can also create or update automations. For example, a skill for babysitting a PR could set up a recurring automation that checks PR status with the GitHub plugin and fixes new review feedback.

## Thread automations

Heartbeat-style recurring wake-up calls attached to the current thread. Use them when scheduled work should preserve thread context instead of starting from a new prompt each time.

Intervals: minute-based for active follow-up loops, daily/weekly for check-ins at specific times.

Use cases:
- checking a long-running command until it finishes
- polling Slack, GitHub, or another connected source when results should stay in the same thread
- reminding Codex to continue a review loop at a fixed cadence
- running a skill-driven workflow (e.g., checking PR status and addressing new feedback)
- keeping a chat focused on ongoing research or triage

Use a standalone or project automation when each run should be independent, when it should run across multiple projects, or when findings should appear as separate runs in Triage.

Make the prompt durable: describe what Codex should do each wake-up, how to decide whether there's anything important to report, and when to stop or ask for input.

## Test automations

Before scheduling, test the prompt manually in a regular thread to confirm:
- The prompt is clear and scoped correctly.
- The selected/default model, reasoning effort, and tools behave as expected.
- The resulting diff is reviewable.

Review the first few scheduled outputs and adjust prompt or cadence as needed.

## Worktree cleanup

Frequent schedules with worktrees can create many worktrees over time. Archive runs you no longer need and avoid pinning runs unless you intend to keep their worktrees.

## Permissions and security

Automations run unattended with your default sandbox settings.

| Sandbox mode | Behavior |
|--------------|----------|
| **read-only** | Tool calls fail if they require modifying files, network access, or app interaction |
| **workspace-write** | Tool calls fail if they require modifying files outside workspace, network access, or app interaction. Allowlist commands outside sandbox with [[061-rules|rules]] |
| **full access** | Elevated risk — Codex may change files, run commands, and access network without asking. Consider workspace-write + [[061-rules|rules]] instead |

In managed environments, admins can restrict behaviors using admin-enforced requirements (e.g., disallow `approval_policy = "never"`, constrain sandbox modes). See [[018-enterprise-managed-configuration|Admin-enforced requirements]].

Automations use `approval_policy = "never"` when organization policy allows. If disallowed, automations fall back to the approval behavior of your selected mode.

## Examples

### Automatically create new skills

```markdown
Scan all of the `~/.codex/sessions` files from the past day and if there have been any issues using particular skills, update the skills to be more helpful. Personal skills only, no repo skills.

If there's anything we've been doing often and struggle with that we should save as a skill to speed up future work, let's do it.

Definitely don't feel like you need to update any- only if there's a good reason!

Let me know if you make any.
```

### Stay up-to-date with your project

```markdown
Look at the latest remote origin/master or origin/main . Then produce an exec briefing for the last 24 hours of commits that touch <DIRECTORY>

Formatting + structure:
- Use rich Markdown (H1 workstream sections, italics for the subtitle, horizontal rules as needed).
- Preamble can read something like "Here's the last 24h brief for <directory>:"
- Subtitle should read: "Narrative walkthrough with owners; grouped by workstream."
- Group by workstream rather than listing each commit. Workstream titles should be H1.
- Write a short narrative per workstream that explains the changes in plain language.
- Use bullet points and bolding when it makes things more readable
- Feel free to make bullets per person, but bold their name

Content requirements:
- Include PR links inline (e.g., [#123](...)) without a "PRs:" label.
- Do NOT include commit hashes or a "Key commits" section.
- It's fine if multiple PRs appear under one workstream, but avoid per-commit bullet lists.

Scope rules:
- Only include changes within the current cwd (or main checkout equivalent)
- Only include the last 24h of commits.
- Use `gh` to fetch PR titles and descriptions if it helps.
  Also feel free to pull PR reviews and comments
```

### Combining automations with skills to fix your own bugs

Create a new skill `$recent-code-bugfix` and [store it in your personal skills](https://developers.openai.com/codex/skills#where-to-save-skills):

```markdown
---
name: recent-code-bugfix
description: Find and fix a bug introduced by the current author within the last week in the current working directory. Use when a user wants a proactive bugfix from their recent changes, when the prompt is empty, or when asked to triage/fix issues caused by their recent commits. Root cause must map directly to the author's own changes.
---

# Recent Code Bugfix

## Overview

Find a bug introduced by the current author in the last week, implement a fix, and verify it when possible. Operate in the current working directory, assume the code is local, and ensure the root cause is tied directly to the author's own edits.

## Workflow

### 1) Establish the recent-change scope

Use Git to identify the author and changed files from the last week.
- Determine the author from `git config user.name`/`user.email`. If unavailable, use the current user's name from the environment or ask once.
- Use `git log --since=1.week --author=<author>` to list recent commits and files. Focus on files touched by those commits.
- If the user's prompt is empty, proceed directly with this default scope.

### 2) Find a concrete failure tied to recent changes

Prioritize defects directly attributable to the author's edits.
- Look for recent failures (tests, lint, runtime errors) if logs or CI outputs are available locally.
- If no failures are provided, run the smallest relevant verification (single test, file-level lint, or targeted repro) that touches the edited files.
- Confirm the root cause is directly connected to the author's changes, not unrelated legacy issues. If only unrelated failures are found, stop and report that no qualifying bug was detected.

### 3) Implement the fix

Make a minimal fix aligned with project conventions.
- Update only the files needed to resolve the issue.
- Avoid extra defensive checks or unrelated refactors.
- Keep changes consistent with local style and tests.

### 4) Verify

Attempt verification when possible.
- Prefer the smallest validation step (targeted test, focused lint, or direct repro command).
- If verification cannot be run, state what would be run and why it wasn't executed.

### 5) Report

Summarize root cause, fix, and verification. Make explicit how the root cause ties to the author's recent changes.
```

Afterward, create an automation:
```markdown
Check my commits from the last 24h and submit a $recent-code-bugfix.
```

#automations #background-tasks #skills #codex