---
title: Rich input editor | Agents | Warp
url: https://docs.warp.dev/agent-platform/third-party-agents/rich-input
source: sitemap
fetched_at: 2026-04-29T15:04:16.614705303-03:00
rendered_js: false
optimized: true
optimized_at: 2026-04-29T18:15:00.000Z
tags:
    - warp-terminal
    - cli-agents
    - prompt-engineering
    - ide-features
    - text-editor
    - workflow-automation
category: guide
word_count: 359
---
The rich input editor lets you write prompts for CLI coding agents with IDE-like features — mouse support, context attachment, voice, and more. Press `Ctrl+G` (configurable) or click **Rich Input** in the agent utility bar to open it.

## Key capabilities

- **IDE-style editing** — click, select, navigate with mouse; copy, cut, paste, undo, word-level navigation; multi-line prompts with soft wrapping; Vim keybindings supported
- **Rich context with @mentions** — reference files, folders, and code symbols; attach images; search for symbols directly
- **Voice input** — dictate prompts instead of typing
- **Slash commands and skills** — access saved `/prompts`, `/skills`, and Warp Drive content with `/`; shows agent-specific skills (e.g., Claude-specific skills when running Claude Code)
- **Agent toolbar** — browse files, view code changes, manage the session

## How to open

| Method | Action |
|--------|--------|
| Keyboard shortcut | Press `Ctrl+G` (configurable) while a supported agent is running |
| Rich Input button | Click **Rich Input** in the agent utility bar at the bottom of the pane |

The editor also auto-opens when an agent resumes from a blocked state (e.g., after approving a command). Toggle **Auto show/hide based on agent status** in Settings to control this.

When the rich input editor is active, Warp hides the cursor inside the CLI agent and moves focus to the editor input. Submit your prompt and it goes directly to the running agent.

## Rich input settings

**Settings** → **Agents** → **Third party CLI agents**:

| Setting | Description |
|---------|-------------|
| Auto show/hide based on agent status | Open editor when agent needs input, hide when agent is working (requires plugin support: Claude Code, OpenCode) |
| Auto open on session start | Open editor when a CLI agent session starts |
| Auto dismiss after submission | Close editor after sending a prompt |
| Keyboard shortcut | Default is `Ctrl-G`; customize in **Settings** → **Keyboard shortcuts** |
| Disable the Rich Input button | Right-click the agent utility bar to remove the chip, or disable the footer entirely |

## Related pages

- [[242-terminal-editor|Modern text editing]]
- [[212-agent-platform-warp-agents-agent-context|Agent Context]]
- [[078-agent-platform-warp-agents-interacting-with-agents-voice|Voice]]
- [[043-agent-platform-warp-agents-capabilities-overview-slash-commands|Slash Commands]]
