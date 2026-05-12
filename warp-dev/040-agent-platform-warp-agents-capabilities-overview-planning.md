---
title: Planning | Agents | Warp
url: https://docs.warp.dev/agent-platform/warp-agents/capabilities-overview/planning
source: sitemap
fetched_at: 2026-04-29T15:03:48.644532398-03:00
rendered_js: false
word_count: 427
summary: This document explains how to utilize Warp's native planning functionality to break down, edit, execute, and manage complex engineering tasks through an integrated AI-driven workflow.
tags:
    - warp-terminal
    - ai-agent
    - task-planning
    - workflow-automation
    - code-collaboration
    - version-control
category: guide
optimized: true
optimized_at: 2026-04-29T00:00:00Z
---
Warp's native planning functionality breaks down complex engineering tasks into structured, executable steps with a persistent plan editor, version history, selective execution, and deep links into your workspace.

## Creating a plan

Generate a plan using the `/plan` [[043-agent-platform-warp-agents-capabilities-overview-slash-commands|slash command]] or by asking the agent in natural language.

The agent creates a structured plan in Warp's native rich text editor with clean formatting, inline code blocks, and clickable file paths to open referenced files immediately.

## Reviewing and editing

Review the plan, reorganize steps, or refine details. Edit manually or ask the agent to revise sections.

Any update **creates a new version**. Version history lets you compare past iterations and restore an older version, preserving a clear decision trail as the plan evolves.

## Executing a plan

Prompt the agent to run the plan — execute the full set of steps or only a specific section (e.g., "Implement phase 1 of the plan").

The agent applies changes incrementally and updates files as it proceeds. This makes it easy to:

- Validate early steps before moving forward
- Adjust the plan mid-run
- Try alternative paths without committing to the full workflow

If you revise the plan while the agent is running, notify it directly and the agent adjusts execution based on your updates.

## Monitoring progress

Reopen the plan at any time by selecting **View plan** in the input. Follow changes in real time through the [[182-code-code-review|Code Review]] panel and add comments using [[080-agent-platform-warp-agents-interactive-code-review|Interactive Code Review]].

## Saving and sharing

Plans auto-save in the **Plans** folder in [[144-knowledge-and-collaboration-warp-drive|Warp Drive]]. You'll see a confirmation when synced.

Export any plan as Markdown, check it into your repository, or share a link for GitHub PRs, design reviews, or async collaboration.

Plans persist in Warp Drive, so you can return to them, reuse them for new work, or use them as documentation for ongoing projects. Plans are also passed to the agent as context.

> [!note]
> Configure auto-add and sync in [[035-agent-platform-warp-agents-capabilities-overview-agent-profiles-permissions|Agent Profiles & Permissions]] under **Settings** > **Agents** > **Profiles**.

## Using plans across conversations

Plans are reusable across tasks and sessions. Reference them in future prompts, continue where you left off, or build follow-up plans.

Use the **@plans** command to quickly search for and reopen previously saved plans. Learn more about attaching context with @ [[070-agent-platform-warp-agents-agent-context-blocks-as-context|here]].

## Next steps

- [[080-agent-platform-warp-agents-interactive-code-review|Interactive Code Review]] — Leave inline comments on agent-generated diffs and have the agent revise in one pass
- [[004-agent-platform-cloud-agents-quickstart|Cloud Agents quickstart]] — Run agents in the cloud for longer tasks, background automation, or parallel work across repos