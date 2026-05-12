---
title: Full terminal use | Agents | Warp
url: https://docs.warp.dev/agent-platform/warp-agents/capabilities-overview/full-terminal-use
source: sitemap
fetched_at: 2026-04-29T15:03:54.328821695-03:00
rendered_js: false
word_count: 832
summary: This document explains how to use Warp's Full Terminal Use feature, which allows the AI agent to interact directly with terminal applications by reading output and executing commands.
tags:
    - warp-terminal
    - ai-agent
    - interactive-shell
    - terminal-automation
    - productivity-tools
category: guide
optimized: true
optimized_at: 2026-04-29T00:00:00Z
---
Full Terminal Use lets Warp's agent attach to interactive terminal applications (database shells, debuggers, text editors, long-running servers), read the live terminal buffer, write to the PTY, respond to prompts, and continue working inside the running process.

## Overview

The agent can attach to interactive tools like `psql`, `vim`, `python`, `gdb`, `top`, or your dev server, read the terminal output as it changes, and interact with the application as if you were typing.

## How Full Terminal Use works

### Start an interactive command

**Ask the agent to start an interactive tool:**

- "Open a Postgres shell and help me inspect the orders table."
- "Start the dev server and debug this 500 error."

**Or start the command yourself, then tag the agent in:**

1. Launch an interactive tool (e.g., `psql` or `npm run dev`)
2. Tag the agent into the running session via "Use Agent" button or `CMD + I`
3. Follow up with natural language requests

Warp attaches the agent to the running PTY so it can see the current terminal buffer and propose actions.

### Agents propose actions inside the session

Once attached, the agent turns your requests into concrete terminal actions. For example, in a Postgres shell:

- You: "Show me all the tables and describe the orders table."
- Agent: proposes running `\dt` then `\d+ orders`

You see a request to run the specific command and optionally enable auto-approval for similar commands in this session.

### Switching control between user and the agent

**Take over:**

- Use the Takeover control to stop the agent from typing or performing actions
- The shell stays open; type directly into the same session

**Hand back control:**

- Click the control again to resume
- Agent resumes where you left off with full access to current terminal state

This enables:

- Letting the agent do mechanical work (paging output, trying command variants)
- Stepping in for delicate or security-sensitive actions
- Resuming agent work once the critical step is done

### Long-running commands in terminal vs agent view

| Step | Action |
|------|--------|
| 1 | Run an interactive command (e.g., `python`, `psql`) |
| 2 | Press `⌘↩` (macOS) or `Ctrl+Shift+Enter` (Windows/Linux), or use `⌘I` / `Ctrl+I` to tag in the agent |
| 3 | Input switches to Agent Mode with full controls |
| 4 | When you exit, an agent conversation block appears in your terminal blocklist |
| 5 | Click the block to reopen the full conversation with your LRC interaction context |

> [!note]
> Use `CMD + I` (macOS) or `CTRL + I` (Windows/Linux) to toggle agent control in either view.

### Showing and hiding agent responses

**Toggle visibility:** Use the `Hide responses` or `Show responses` button, or `CMD + G`, in the interactive command footer.

**Behavior when hidden:**

- Your own agent requests auto-dismiss after **4 seconds** to keep the terminal clear
- Manually dismiss any user query by hovering and clicking X

## Configuring agent permissions and autonomy

### Session-level approvals

Each time the agent wants to take an action inside an interactive shell, you see:

- The agent's reasoning and proposed command
- Options:
  - **Allow once** (e.g., approve or press `ENTER`)
  - **Auto-approve similar commands** in this session (e.g., `CMD + SHIFT + I`)
  - **Refine** with `CTRL + C` (clears proposed action, lets you follow up)
  - **Take over** manually with `CMD + I`

**Guidelines:**

- Exploratory work: use **Always allow** to reduce friction
- Production systems or sensitive operations: use **Allow once** and review each step

### Global permission settings

Configure in [[035-agent-platform-warp-agents-capabilities-overview-agent-profiles-permissions|Agent Profiles & Permissions]]:

| Setting | Behavior |
|---------|----------|
| **Ask on first write** | First write requires approval; subsequent writes for that process/command are auto-approved |
| **Always ask** | Every write requires explicit approval |
| **Always allow** | Agent writes to shell without prompting |

You can still override these per-session when prompted, or switch to a different AI profile for specific conversations.

> [!note]
> [[https://docs.warp.dev/support-and-community/privacy-and-security/secret-redaction|Secret Redaction]] features still apply during Full Terminal Use — sensitive values in your environment or output remain protected.

## Credits usage

All AI interactions from Full Terminal Use consume [[https://docs.warp.dev/support-and-community/plans-and-billing/credits|credits]].

**Interactive sessions consume more credits when:**

- The agent runs many commands in an interactive shell
- There is significant terminal output to read and summarize

**To manage credit usage:**

- Use tighter scopes: "Describe just the orders table." instead of "Explain the entire database."
- Pause autonomy for high-volume tasks: Take over manual control when running large batches or long logs.
- Use stricter permissions: Set global permissions to "Ask on first write" or "Always ask", then approve only what you need.

## Example workflows

Demo from engineer Maggie walking through Full Terminal Use examples:

**Tools where Full Terminal Use is particularly useful:**

- Database shells (Postgres, MySQL, SQLite)
- Debuggers (gdb)
- Language-specific REPLs (python, node)
- Text editors and file explorers
- Long-running dev servers or monitoring tools (top, htop)