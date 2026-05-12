---
title: Interacting with agents | Agents | Warp
url: https://docs.warp.dev/agent-platform/warp-agents/interacting-with-agents
source: sitemap
fetched_at: 2026-04-29T15:04:00.598949553-03:00
rendered_js: false
word_count: 810
summary: This document explains how to manage AI-driven conversations in Warp, including tips for maintaining context, utilizing the conversation panel, and managing token usage within the context window.
tags:
    - warp-terminal
    - ai-agent
    - conversation-management
    - context-window
    - developer-productivity
    - terminal-workflow
category: guide
optimized: true
optimized_at: 2026-04-29T15:04:00.598949553-03:00
---
# Interacting with agents

Conversations are sequences of AI queries and blocks tied to sessions. Run multiple Agent Mode conversations simultaneously in different windows, tabs, or panes. Unrelated questions should start new conversations to keep context relevant.

> [!warning]
> Long conversations cause slower performance and lower-quality answers. When working on a separate task or question, start fresh rather than relying on context from earlier interactions.

Enable [[036-agent-platform-warp-agents-capabilities-overview-cloud-conversations]] to access conversations across devices, share them with teammates, or restore past cloud agent conversations.

## Staying in a conversation (follow-ups)

By default, an AI query immediately after interacting in Agent Mode is sent as a **follow-up** to the current conversation.

| Input Mode | Indicator |
|------------|------------|
| **Classic Input** | Pink highlight bar + bent follow-up arrow (↳) + conversation chip |
| **Terminal/Agent modes** | Conversation panel shows which conversation you're in |

**To follow up on a previous conversation:**
- Continue prompting if already in an active conversation
- Open **Conversations menu** (`CMD + Y` macOS / `CTRL + SHIFT + Y` Windows/Linux), select a conversation, then query
- Click the pink conversation chip in the input field to resume

### Agent tips in the input

Warp surfaces short tips under the Warping indicator while the agent processes your request. Enable/disable via:

- **Settings** → **Agents** → **Warp Agent** → **Input** → **Show agent tips**
- **Command Palette** (`CMD + P` / `CTRL + SHIFT + P`) → "Show Agent Tips" or "Hide Agent Tips"

## Managing conversations

View previous conversations or start a new one via the **Conversations Menu** (`CMD + Y` / `CTRL + SHIFT + Y`).

> [!info]
> The "New Conversation" item disappears once you start searching for an actual conversation.

### Starting a new conversation

Warp auto-creates a new conversation when you ask an AI query after running a shell command, or after three hours of inactivity.

| Input Mode | Visual Indicator | Manual Start |
|------------|------------------|---------------|
| **Classic Input** | No follow-up arrow (↳) | `CMD + I` or `BACKSPACE` while in follow-up mode |
| **Terminal/Agent modes** | Fresh conversation view | `CMD + ↵` or `/new` slash command |

Or: open **Conversations Menu** (`CMD + Y`) and select "New Conversation".

## Context window management

Every conversation consumes tokens in a **context window** — the amount of text an LLM can process at one time. Context window size depends on the model.

As tokens accumulate, performance degrades. When the limit is exceeded, Warp automatically summarizes the conversation.

### Context window usage indicator

- **< 20%**: No indicator shown
- **20-80%**: Usage bar progresses
- **Approaching limit**: Indicator turns red
- **Exceeded**: Warp auto-summarizes

> [!info]
> Switching models mid-conversation updates the indicator only after your next message.

## Conversation segmentation

Warp detects topic shifts and suggests starting a new conversation instead of continuing in the same context.

Keyboard shortcuts:
- `CMD + SHIFT + N` — Start new conversation
- `CMD + T` — Open new tab
- `CMD + D` — Open new pane

## Conversation Panel

The **Conversation Panel** (left side) browses and switches between agent conversations.

### Panel layout

Two collapsible dropdowns:

- **Active** — Conversations where you've sent at least one query. Click to switch. Cloud agent conversations and Oz runs appear here while open.
- **Past** — Recent conversation history. Each row shows: title, timestamp ("8 min ago", "3 days ago"), working directory. Click to reopen in a new pane.

### Conversation storage

**Local storage** is default. Enable **cloud-synced conversations** to:

- Access history across devices
- Share with teammates
- Retain conversations when switching machines

Enable via **Settings** → **Privacy** → toggle **"Store AI conversations in the cloud"**. Cloud agent conversations are always stored in the cloud.

### Search

Type in the search field to filter conversations by title (and directory/context in some builds).

### New conversation

Click **New conversation** at the bottom of the **Active** list to create a fresh thread without deleting previous ones.

### Navigation behavior

| Action | Result |
|--------|--------|
| Click active conversation | Switch directly |
| Click past conversation | Opens in a new pane |
| `⌘Y` conversation selector | Shows all conversations |
| `esc` or back button | Return to terminal mode |
| `⌘↩` | Start new conversation |

**Command Palette** — type `conversations:` to filter and navigate directly.

**Up-arrow history**:
- Terminal view: past shell commands + recent conversations
- Agent view: past prompts only

### Exit confirmation for in-progress conversations

Exiting an in-progress conversation **cancels** the agent's current work.

1. First exit attempt → hint changes to "Press again to exit"
2. 2-second window to press `esc` or `^C` again to confirm
3. Confirmed → Warp exits and cancels the request

> [!info]
> Empty new conversations (no messages sent) can be exited immediately without confirmation.

#tags #ai-agent #conversation-management #context-window
