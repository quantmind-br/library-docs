---
title: Run Multiple AI Coding Agents | Guides | Warp
url: https://docs.warp.dev/guides/agent-workflows/how-to-run-multiple-ai-coding-agents
source: sitemap
fetched_at: 2026-04-29T15:06:23.676084157-03:00
rendered_js: false
word_count: 532
summary: This guide explains how to configure a multi-agent development environment in Warp by utilizing vertical tabs, Git worktrees, and tab configurations to run and monitor multiple AI coding agents in parallel.
tags:
    - multi-agent-workflow
    - warp-terminal
    - ai-coding-agents
    - git-worktrees
    - productivity-tools
    - workspace-management
category: guide
optimized: true
optimized_at: 2026-04-29T00:00:00Z
---
# Run Multiple AI Coding Agents

Configure a multi-agent development environment by running different agents in parallel, comparing their outputs, or having one agent build while another reviews. Estimated time: 15 minutes.

## Prerequisites

- **Any coding agent** — Warp's built-in agent, [Claude Code](https://docs.warp.dev/guides/external-tools-and-integrations/how-to-set-up-claude-code), [Codex CLI](https://docs.warp.dev/guides/external-tools-and-integrations/how-to-set-up-codex-cli), or others (Oz, OpenCode, Gemini CLI, Amp, Pi, Droid)
- **Git-tracked project** — Notifications and code review work best in a Git repository

## Step 1: Switch to Vertical Tabs

Vertical tabs show rich metadata for each session: running agent, branch, directory, and status.

Enable vertical tabs:
1. Go to **Settings** > **Appearance** > **Tabs**
2. Select **Use vertical tab layout**

Configure display per tab:
- The running agent (Oz, Claude Code, Codex, etc.)
- The current Git branch
- The working directory
- Status indicator (active, waiting for input, or idle)

## Step 2: Launch Agents in Separate Tabs

Open a new tab for each agent session. Navigate to your project directory and start an agent:

| Tab | Agent |
|-----|-------|
| Tab 1 | Claude Code |
| Tab 2 | Codex |

Give each agent a different task, or the same task to compare approaches.

## Step 3: Monitor Agents with Notifications

You don't need to watch each tab. Warp sends notifications when an agent needs attention:
- Permission to run a command
- Approval to apply a code diff

Look for the attention-needed indicator on the tab in the vertical sidebar. Click to jump directly to that agent.

- **Codex** — Warp automatically sets up notifications on first run

## Step 4: Compare Outputs from Different Agents

Run the same task in different Git worktrees with different agents to compare approaches. After both agents complete, open the [Code Review panel](https://docs.warp.dev/warp/code/code-review) (`⌘+Shift++`) in each tab to compare diffs side-by-side.

## Step 5: Save Your Workspace with Tab Configs

Save multi-agent setups as tab configs to recreate with one click:

1. Hover over the tab and click the three dots
2. Click **Save as new config**

Tab configs are TOML files defining directory, startup commands, and layout. Example: two panes side-by-side, drops into project repo, starts Claude Code in one pane and Codex in the other.

> [!info]
> Tab configs pair well with [Git worktrees](https://docs.warp.dev/warp/code/git-worktrees). Create a worktree for each agent so they work on isolated branches, then merge the best results.

## Step 6: Use Git Worktrees for Isolated Workspaces

Git worktrees prevent conflicts by giving each agent its own copy of the repo on a separate branch.

1. Create worktrees for each agent
2. Point each agent tab at its own worktree directory
3. Define worktree directories and agent startup commands in tab configs
4. Recreate the full setup with one click
5. Compare branches and merge the best results

## Productivity Tips

- **Agent Management Panel** — See all active agents across tabs in a dashboard view
- **Color-code tabs** — Assign different themes or colors to distinguish agent tabs at a glance
- **Compose with `Ctrl+G`** — Use Warp's rich input editor for click-to-edit instead of arrow-key navigation
- **Review all changes before committing** — Open the Code Review panel to see the combined diff across all files
