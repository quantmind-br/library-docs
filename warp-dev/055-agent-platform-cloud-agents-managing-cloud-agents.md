---
title: Managing cloud agents | Agents | Warp
url: https://docs.warp.dev/agent-platform/cloud-agents/managing-cloud-agents
source: sitemap
fetched_at: 2026-04-29T15:04:36.249834503-03:00
rendered_js: false
optimized: true
optimized_at: 2026-04-29T00:00:00Z
word_count: 480
summary: This document describes the Warp management view, which provides a centralized interface for monitoring, filtering, and inspecting the activity and status of both interactive and cloud-based agents.
tags:
    - agent-management
    - warp-platform
    - cloud-agents
    - monitoring-tools
    - activity-tracking
    - workflow-automation
category: guide
---
Warp provides a centralized management view where you can monitor agent activity across your account and (where applicable) your team. Access this view in the Warp app or through the [[056-agent-platform-cloud-agents-oz-web-app|Oz web app]] at [oz.warp.dev](https://oz.warp.dev), which works on mobile devices.

The management view is designed to answer, at a glance:

- Which agents have been running recently (and what's running right now)
- Which runs succeeded, failed, or were canceled
- Where an agent run was triggered from (a local agent conversation, the Oz CLI, Slack, etc.)
- How many credits those runs consumed

This view includes your **local (interactive) agents** and [[194-agent-platform-cloud-agents-overview|cloud agent]] runs.

## What appears in the management view

The management view includes two categories of agent activity.

### Interactive agents

- Initiated from the Warp desktop app.
- The conversation is owned by you. It opens locally in Warp, and can be shared via a link when needed.
- Credit usage reflects inference.

### Cloud agent runs

- Background executions initiated by triggers such as integrations and automations (for example: Slack, Linear, schedules, GitHub Actions, or API/CLI invocations).
- Each run produces a shared session that can be inspected after completion (including logs, messages, and outputs).
- Credit usage reflects inference + compute, shown as a single combined value in this view.

In the **Personal** tab, you can view all of the interactive and cloud agent conversations that you own. In the **All** tab, you can see everything from the personal tab, as well as any cloud agent sessions that are shared with you by your teammates.

## The agents list

Each row represents a single item in the management view (either an interactive conversation or a cloud agent run). The list is intended to be scannable: you should be able to understand "what happened" without opening anything.

### Fields you'll see

**Source**

Where the agent was launched from. Common sources include:

**Status**

Warp uses a small set of statuses to help you quickly identify what needs attention:

**Duration (for cloud agent tasks)**

- Shown for cloud agent runs to indicate how long the task executed.
- Note: Interactive conversations generally don't map cleanly to a single "run duration," so this is currently omitted.

## Inspecting an agent

- Clicking a cloud agent row opens the [[064-agent-platform-cloud-agents-viewing-cloud-agent-runs|shared session]] for that run (logs/messages/output).
- Clicking an interactive row opens the conversation locally in the Warp app.

This makes the management view a navigation surface: find the thing you care about, click once, and you're in the right context to inspect or continue work.

## Filtering

In both *Personal* and *All* views, you can open the filter menu and filter by:

- Source (interactive, API, CLI, Slack/Linear, scheduled)
- Day of creation
- Creator
- Status

This is the fastest way to isolate "everything that failed today," "runs from Slack," or "what a specific teammate triggered via integrations."