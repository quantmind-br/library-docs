---
title: Conversation forking | Agents | Warp
url: https://docs.warp.dev/agent-platform/warp-agents/interacting-with-agents/conversation-forking
source: sitemap
fetched_at: 2026-04-29T15:04:03.407626276-03:00
rendered_js: false
optimized: true
optimized_at: 2026-04-29T18:15:00.000Z
tags:
    - warp-terminal
    - conversation-management
    - ai-workflow
    - branching-threads
    - productivity-tools
category: guide
word_count: 304
---
Fork conversations to create new threads that inherit all context, messages, and history from an existing conversation. Follow-ups in the fork do not impact the original, and vice versa. Selected model and execution profile are preserved.

## How to fork a conversation

| Method | Action |
|--------|--------|
| Command Palette | `CMD+Y` (macOS) / `CTRL+SHIFT+Y` (Windows/Linux); hover over any conversation to see a fork button |
| AI block footer | Click the fork button in the footer of the most recent AI block |
| `/fork` slash command | Fork current conversation; optionally include a prompt after the command |
| `/fork-and-compact` slash command | Fork and automatically compact the forked version (combined with context window management) |
| `/fork-from` slash command | Open searchable menu of all queries; select a query to fork from that specific point |

**Keyboard behavior for slash commands:**
- `Enter` — open fork in new pane (default)
- `⌘+Enter` (macOS) / `Ctrl+Enter` (Windows/Linux) — open fork in current pane

### Fork from anywhere in a conversation

Right-click any agent response block (or click the three-dot menu) and select **Fork conversation from here**. The new conversation includes everything up to and including that response, excluding subsequent messages.

**Use cases:**
- **Exploring alternate paths** — return to a point on track and try a different approach
- **Managing context window** — fork from an earlier point to continue with only relevant context
- **Preventing context pollution** — fork from before errors occurred to start fresh

## Settings

**Settings** → **Features** → **Open forked conversation layout**:

| Option | Behavior |
|--------|----------|
| Split Pane (default) | Opens forked conversation in a new pane alongside current view |
| New Tab | Opens forked conversation in a new tab |

## Related pages

- [[079-agent-platform-warp-agents-interacting-with-agents|Interacting with Agents]]
- [[040-agent-platform-warp-agents-capabilities-overview-planning|Planning]]
