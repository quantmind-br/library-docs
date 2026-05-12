---
title: Set Up Codex CLI | Guides | Warp
url: https://docs.warp.dev/guides/external-tools-and-integrations/how-to-set-up-codex-cli
source: sitemap
fetched_at: 2026-04-29T15:06:41.115751771-03:00
rendered_js: false
word_count: 426
summary: This document provides a comprehensive guide on installing, authenticating, and configuring the Codex CLI coding agent to automate development tasks within a terminal environment.
tags:
    - codex-cli
    - ai-coding-agent
    - developer-tools
    - terminal-automation
    - workflow-configuration
category: guide
optimized: true
optimized_at: 2026-04-29T15:06:41.115751771-03:00
---
Codex CLI is OpenAI's open-source coding agent. It reads your codebase, edits files, and executes commands from natural language prompts.

## Prerequisites

- **A ChatGPT account with Codex access** — Included with paid ChatGPT plans, or use an OpenAI API key
- **Node.js 18+** (for npm) or **Homebrew** (for macOS)
- **macOS or Linux** — Windows support is experimental; use WSL for best Windows experience

## 1. Install Codex CLI

Install globally with npm or Homebrew:

**npm:**
```bash
npm install -g @openai/codex
```

**Homebrew (macOS):**
```bash
brew install codex
```

Verify installation:
```bash
codex --version
```

You can also download platform-specific binaries from the [GitHub releases](https://github.com/openai/codex/releases).

## 2. Authenticate

Run Codex for the first time:
```bash
codex
```

Select **Sign in with ChatGPT** and authenticate. Your Codex usage is included in your ChatGPT plan.

For API key authentication (useful for CI/CD or automation):
```bash
export OPENAI_API_KEY=your_key_here
```

## 3. Start your first session

Navigate to a project directory and launch Codex:
```bash
codex
```

Try giving it a task:
```
Fix the authentication bug in login.ts
```

Codex reads relevant files, proposes changes, and asks for confirmation before modifying anything. Review changes in diff view and accept or reject each one.

## 4. Configure model and approval mode

Switch between models during a session with the `/model` command. See [Codex CLI documentation](https://developers.openai.com/codex/cli/) for the current model list.

Codex has three approval modes that control autonomy:

| Mode | Behavior |
|------|----------|
| **Auto** (default) | Read, edit, and run commands within working directory; asks for anything outside scope |
| **Read-only** | Consultative only |
| **Full Access** | Broader autonomy including network access |

Use `/permissions` inside a session to switch modes.

## 5. Customize with a configuration file

Create a `codex.md` or `AGENTS.md` file at your project root to teach Codex your project's conventions. Codex reads this file at the start of every session.

> [!tip]
> Warp supports agent notifications for Codex. Add `notification_condition = "always"` under `[tui]` in `~/.codex/config.toml` and restart Codex.

## Productivity Tips

| Feature | How to Use |
|---------|------------|
| **Voice input** | Dictate complex instructions; Warp's voice transcription works with any CLI agent |
| **Images as context** | Paste screenshots of bugs, designs, or error messages into prompts |
| **Visual diffs** | Open Code Review panel (`⌘+Shift++`) after changes to see visual diffs |
| **Run alongside Claude Code** | Use [vertical tabs](https://docs.warp.dev/warp/terminal/windows/vertical-tabs) to compare outputs |
| **Rich input** | Press `Ctrl+G` for full text editor experience when composing prompts |

## Next Steps

You installed Codex CLI, authenticated, started your first session, and configured it for your project. Codex is now set up as a working AI coding agent in Warp.

#codex-cli #ai-coding-agent #developer-tools #terminal-automation #workflow-configuration
