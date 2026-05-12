---
title: Coordinate Agents on Separate Tasks | Guides | Warp
url: https://docs.warp.dev/guides/agent-workflows/running-multiple-agents-at-once-with-warp
source: sitemap
fetched_at: 2026-04-29T15:06:30.259026391-03:00
rendered_js: false
word_count: 312
summary: This document explains the functionality of running multiple concurrent AI agents within the Warp workspace to manage simultaneous coding tasks and workflows efficiently.
tags:
    - ai-agents
    - productivity-tools
    - task-management
    - workspace-automation
    - concurrent-processing
category: concept
optimized: true
optimized_at: 2026-04-29T15:04:00Z
---
Warp lets you run multiple agent tasks simultaneously within one workspace, enabling you to work on several coding tasks at once — fix a PR, add a feature, debug a build — without losing context.

## How it works

Each agent runs in its own thread with:

- Progress tracking
- Notifications when blocked or completed
- Separate command histories

Because Warp is a desktop app, it sends system notifications to alert you when an agent finishes or needs review.

## Example: Reverting a PR and editing a shortcut

Ben uses voice mode to quickly start tasks:

> **Prompt:** "Find the PR where we added the keyboard shortcut to the UDI input and revert it."

The agent locates the relevant diff, reverts the change automatically, and pushes it to the correct branch. Warp notifies Ben when the task completes.

Then he runs another prompt:

> **Prompt:** "Change the keyboard shortcut to `Cmd + Shift + I`."

Warp modifies `input.rs`, previews the diff, and Ben applies the change directly from Warp.

## Managing multiple tasks

You can switch between concurrent agents:

- Each task appears in a Task List panel
- Completed, canceled, and running tasks are color-coded
- Toast notifications appear when tasks are blocked

You can even fast-forward agents to auto-approve all code diffs once you trust their trajectory.

## Parallel contexts

In another repo, Ben adds a new Eval test via a different agent:

> **Prompt:** "Create a Python hello world function and verify it prints 'Hello World.'"

Warp's second agent locates the correct file, writes the test code, and verifies execution. Meanwhile, the first agent continues working on the keyboard shortcut task.

## Reviewing all active agents

Open the Agent Mode Dashboard to see:

- Active tasks
- Completed tasks
- Logs and outputs

You can refine or cancel tasks mid-run if needed, or switch back to manual commands.