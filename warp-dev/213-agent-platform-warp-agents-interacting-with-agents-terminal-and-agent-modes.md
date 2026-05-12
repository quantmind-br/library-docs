---
title: Terminal and Agent modes | Agents | Warp
url: https://docs.warp.dev/agent-platform/warp-agents/interacting-with-agents/terminal-and-agent-modes
source: sitemap
fetched_at: 2026-04-29T15:03:59.726027941-03:00
rendered_js: false
word_count: 1977
summary: This document explains the distinction between Terminal mode and Agent conversation mode in the Warp terminal, describing their unique workflows, interface controls, and context management.
tags:
    - warp-terminal
    - ai-agent
    - cli-workflow
    - user-interface
    - terminal-modes
    - cloud-computing
category: concept
optimized: true
optimized_at: 2026-04-29T15:04:00Z
---
Warp provides two distinct modes: a clean terminal for commands, and a dedicated conversation view for multi-turn interactions with [Oz, Warp's agent](https://docs.warp.dev/agent-platform/warp-agents/interacting-with-agents).

## Key terminology

- **Terminal session** — Your shell environment for running commands. This is the default mode when opening Warp.
- **Oz agent conversation** — A multi-turn interaction with Oz. Conversations maintain context across exchanges with a dedicated view and richer controls.

Terminal and Agent modes separate these contexts while keeping them visually distinct.

## Why two modes

- **Clean terminal by default** — Minimal input when running commands. Agent controls appear only when needed.
- **Dedicated conversation view** — Full controls: model select, voice input, image attachments, conversation history.
- **Explicit mode switching** — Current mode is clearly visible for better workflow organization.

## Two distinct modes

### Terminal mode (default)

Terminal mode looks and behaves like a traditional terminal input. Agent controls are hidden, keeping the interface clean.

**Message bar hints:**

| Context | Hint shown |
|---------|------------|
| Empty input | `⌘↩ for new agent` |
| Text entered | `⌘↩ to send to agent` |
| Last command failed | `⌘↑ attach 'npm install...' output as agent context` |
| Context attached | `⌘↩ to send to agent with 'git status' attached` |
| Last item is agent block | `⌘Y to continue conversation` |

Auto-detection labels input as "agent" or "shell" before submission, showing "(autodetected)" in magenta. See [Understanding auto-detection](#understanding-auto-detection) for configuration.

**To hide the message bar:** Go to **Settings** > **Features** > **Terminal Input** and toggle off **Show terminal input message line**. This hides hints only—it does not disable AI functionality.

> [!warning]
> Disabling the message bar while auto-detection is enabled hides the visual indicator for shell vs. agent detection. Consider also disabling auto-detection (**Settings** > **Agents** > **Warp Agent** > **Input**).

### Oz agent conversation view (expanded UI)

A dedicated conversation view with richer agent controls including model select, voice input, image attachments, and conversation management. Familiar charms (current directory, git branch, diff view entry point) remain available.

**Key difference:** Agent controls appear only when in a conversation, keeping the terminal clean otherwise.

> [!info]
> Agent conversation views have an alternative background color and an input toolbelt showing model selector, voice input, and image attachment buttons.

#### Customizing the input toolbelt

Right-click the input in an agent conversation and select **Edit agent toolbelt** to reorder, hide, or move chips and buttons between the left and right sides. Your layout persists across app restarts.

Agent Mode-specific items: model selector, autodetection toggle, Context Usage, fast forward toggle. Shared items (voice input, file attachment, context chips) appear in both Agent Mode and the [CLI coding agent toolbelt](https://docs.warp.dev/agent-platform/third-party-agents/overview#customizing-the-toolbelt).

**Block origin and visibility:**

- **Terminal blocks** — Commands run directly in the terminal. Appear in terminal blocklist; can be attached as context to any conversation.
- **Agent conversation blocks** — Commands executed within an agent conversation (by you or the agent). Only appear within that conversation; don't appear in the terminal blocklist.

In agent conversations, context is managed automatically with optional manual attachment from terminal view.

#### Cloud agent conversations

Start **Oz cloud agent conversations** that run in an isolated cloud environment. Useful for:

- Running parallel agents across multiple tasks
- Running agents remotely on hosted computers
- Running agents autonomously in the cloud
- Checking in on agents from anywhere

**To start a cloud agent conversation:** Press `⌥⌘↩` (macOS) or `Ctrl+Alt+Enter` (Windows/Linux) from terminal mode, or use the welcome block's "Start cloud project" action.

Cloud agent conversations differ from local:

- **Credits indicator** — Shows remaining cloud agent credits
- **Different zero state** — Conversation header indicates "New Oz cloud agent conversation"

Cloud agent conversations are always stored in the cloud. See [Cloud-synced Conversations](https://docs.warp.dev/agent-platform/warp-agents/capabilities-overview/cloud-conversations) for access and sharing details.

**Accessing running or past cloud conversations:**

- **From the conversation list panel** — Cloud conversations appear alongside local conversations. Click to open.
- **From the management view** — Use the [Agent Management view](https://docs.warp.dev/agent-platform/cloud-agents/managing-cloud-agents) to see all cloud agent runs, filter by status, and click any row to open.
- **From the Oz web app** — Access cloud agents at [oz.warp.dev](https://oz.warp.dev) to manage runs from any browser.

See [Cloud Agents Overview](https://docs.warp.dev/agent-platform/cloud-agents/overview) for more.

## Understanding auto-detection

Auto-detection interprets each input as either a shell command or an agent request. When enabled, Warp shows an **inline indicator** (e.g., "(autodetected)" in magenta).

### How it works

**In terminal mode:** When you type natural language (e.g., "Summarize the dependencies in this project"), Warp labels it as "agent" and displays the "(autodetected)" indicator. Pressing Enter sends your input directly to the agent in a new conversation ("quicksend" workflow).

**In agent conversation view:** When auto-detection identifies your input as a shell command, Warp displays a distinct UI border to indicate the mode switch.

### Settings

> [!info]
> Control auto-detection separately for terminal mode and agent conversation view. Both toggles are in **Settings** > **Agents** > **Warp Agent** > **Input**:

- **Terminal mode:** Toggle **Autodetect agent prompts in terminal input**
- **Agent conversation view:** Toggle **Autodetect terminal commands in agent input**

### Override methods

- **Keyboard shortcut** — Press `⌘I` to switch between command and Agent Mode.
- `!` **prefix** — In agent view, prepend `!` to force shell command execution (e.g., `!ls` or `!git status`).

> [!info]
> After override, the selection is "sticky" for that entry.

### Defaults for new vs. existing users

Auto-detection is enabled by default for new Warp users. For users who had Warp before Terminal and Agent modes, auto-detection is disabled by default to preserve existing workflows.

## Entering and navigating conversations

### How to enter a conversation

**A) Use the `/agent` or `/new` slash command**

Type `/agent` or `/new` in terminal mode to enter the agent conversation view:

- `/agent` or `/new` — Opens a new agent conversation view with full controls
- `/agent <prompt>` — Sends your prompt directly to the agent in a new conversation

**B) Use the keyboard shortcut**

Press `⌘↩` (macOS) or `Ctrl+Shift+Enter` (Windows/Linux) to enter the conversation view immediately. Use when you want to attach an image, use voice input, or access other conversation-only controls before sending your first message.

**C) Quicksend with auto-detection**

1. Type a natural language request (e.g., "Summarize the dependencies in this project").
2. If Warp detects it as an agent request, it shows an "(autodetected)" indicator.
3. Press Enter to send directly to the agent in a new conversation.

**D) Continue from the up-arrow history menu**

Press `↑` (up arrow) to open an inline history menu. See [Navigation behavior](https://docs.warp.dev/agent-platform/warp-agents/interacting-with-agents#navigation-behavior) for details on how up-arrow works in terminal vs. agent view.

**E) Click an active AI suggestion**

When [Active AI Recommendations](https://docs.warp.dev/agent-platform/warp-agents/active-ai) is enabled, Warp displays contextual prompt suggestions based on recent activity. Clicking opens the agent conversation view and sends that prompt immediately.

### Navigating conversations

Use the **Conversation Panel** for browsing and managing agent conversations. See [Agent Conversations](https://docs.warp.dev/agent-platform/warp-agents/interacting-with-agents) for panel layout, navigation, and storage details.

### Using slash commands

**In an agent conversation:**

Type `/` in the input to access [slash commands](https://docs.warp.dev/agent-platform/warp-agents/capabilities-overview/slash-commands):

- Type `/` to open the command menu
- Keep typing to filter (e.g., `/conversations`, `/compact`)
- Use `↑` / `↓` to navigate and `Enter` to run
- Press `esc` to dismiss

**Key slash commands in Agent Mode:**

- `/new` or `/agent` — Start a new conversation
- `/plan` or `/plan <prompt>` — Start a planning conversation; agent creates an implementation plan before making changes
- `/conversations` — Open the conversation list panel
- `/compact` — Summarize and compact the current conversation to free context window space
- `/fork` — Fork the current conversation into a new thread. `Enter` forks in the existing pane; `⌘↩` forks in a new pane
- `/fork-and-compact` — Fork and automatically summarize the conversation
- `/fork from` — Choose a specific point in the conversation to fork from (shows previous queries)
- `/model` — Select or change the AI model

**In terminal mode:**

Terminal mode exposes a reduced set of slash commands focused on quick actions. Agent conversations expose the full set including `/fork`, `/compact`, and `/model`.

See [Slash Commands](https://docs.warp.dev/agent-platform/warp-agents/capabilities-overview/slash-commands) for the complete list.

### Forking conversations

Forking lets you branch from an existing conversation to explore a different direction without losing your original thread.

**To fork:**
1. Type `/fork` and press `Enter` in an agent conversation.
2. Choose where to open:
   - `Enter` — Fork in the current pane (replaces the current view)
   - `⌘↩` (Windows/Linux: `Ctrl+Shift+Enter`) — Fork in a new pane (keeps original visible)

**Fork and compact:** Use `/fork-and-compact` to fork and automatically summarize the conversation. Useful when context window is full but you want to continue on the same work.

**Fork from a specific point:** Use `/fork from` to choose exactly where to branch:
1. Type `/fork from` and press `Enter`.
2. Select the query you want to fork from.
3. Choose `Enter` (existing pane) or `⌘↩` / `Ctrl+Shift+Enter` (new pane).

See [Conversation Forking](https://docs.warp.dev/agent-platform/warp-agents/interacting-with-agents/conversation-forking) for more forking methods and use cases.

## Using Agent Mode as the default experience

Configure "default mode for new sessions" to type natural language at any point and have it automatically routed to an agent.

### Step 1 — Set new tabs to open in agent view

By default, new tabs and panes open in terminal mode. To launch directly into an Oz agent conversation:

1. Go to **Settings** > **Features** > **General**.
2. Change **Default mode for new sessions** to **Agent**.

### Step 2 — Enable auto-detection in Agent Mode

1. Go to **Settings** > **Agents** > **Warp Agent** > **Input**.
2. Toggle on **Autodetect terminal commands in agent input**.

Press `⌘I` (macOS) or `Ctrl+I` (Windows/Linux) to manually toggle between shell and Agent Mode at any time, overriding auto-detection.

> [!info]
> Auto-detection is enabled by default for new Warp users.

## Keyboard shortcuts (quick reference)

Press `?` in conversation view to show/hide the full shortcuts panel.

### Navigation and mode switching

| Action | macOS | Windows/Linux |
|--------|-------|---------------|
| Start new agent conversation (from terminal mode) | `⌘↩` | `Ctrl+Shift+Enter` |
| Start new cloud agent conversation (from terminal mode) | `⌥⌘↩` | `Ctrl+Alt+Enter` |
| Send to agent with attached context | `⌘↩` | `Ctrl+Shift+Enter` |
| Tag agent into long-running command | `⌘↩` | `Ctrl+Shift+Enter` |
| Exit conversation (back to terminal mode) | `esc` | `esc` |
| Stop agent / exit on empty input | `^C` | `Ctrl+C` |
| Open conversation selector | `⌘Y` | `Ctrl+Y` |
| Toggle conversation list panel | `⌘⇧H` | `Ctrl+Shift+H` |
| Override auto-detection (switch shell ↔ agent) | `⌘I` | `Ctrl+I` |

### Input modifiers

| Key | Function |
|-----|----------|
| `!` | Prepend to force shell mode (e.g., `!ls`) |
| `/` | Open slash command menu |
| `@` | Open context menu (attach files, symbols, etc.) |
| `?` | Show/hide keyboard shortcuts panel |

### Conversation actions

| Action | macOS | Windows/Linux |
|--------|-------|---------------|
| Resume a paused/cancelled conversation | `⌘⇧R` | `Ctrl+Alt+R` |
| Toggle auto-accept (for agent tool executions) | `⌘⇧I` | `Ctrl+Shift+I` |
| Open code review pane | `⌘⇧+` | `Ctrl+Shift++` |
| Toggle plan panel (if a plan exists) | `⌘⌥P` | `Ctrl+Alt+P` |

### In slash command / fork menus

| Key | Function |
|-----|----------|
| `↑` / `↓` | Navigate menu items |
| `Enter` | Select (fork in existing pane) |
| `⌘↩` / `Ctrl+Shift+Enter` | Select and open in new pane |
| `esc` | Dismiss menu |

### Customizing keybindings

Go to **Settings** > **Keyboard shortcuts** to assign your preferred key combinations to frequently used commands.

For example, to bind a keyboard shortcut to `/agent`:
1. Open **Settings** > **Keyboard shortcuts**
2. Search for "agent" or the slash command you want to bind
3. Click the shortcut field and press your desired key combination
4. The shortcut is saved automatically