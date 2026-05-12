---
title: Set Up Claude Code | Guides | Warp
url: https://docs.warp.dev/guides/external-tools-and-integrations/how-to-set-up-claude-code
source: sitemap
fetched_at: 2026-04-29T15:06:39.867559578-03:00
rendered_js: false
word_count: 442
summary: This document provides a step-by-step guide for installing, authenticating, and configuring the Claude Code AI agent specifically within the Warp terminal environment.
tags:
    - claude-code
    - warp-terminal
    - ai-coding-agent
    - developer-productivity
    - cli-tools
    - configuration
category: guide
optimized: true
optimized_at: 2026-04-29T15:06:39.867559578-03:00
---
Claude Code is Anthropic's AI coding agent. It reads your codebase, writes and edits code, runs commands, and handles complex refactors using natural language prompts.

## Prerequisites

## 1. Install Claude Code

Follow Anthropic's [official installation guide](https://docs.anthropic.com/en/docs/claude-code/quickstart) to install Claude Code. The native installer (recommended) requires no dependencies and auto-updates in the background.

When you launch Claude Code inside Warp, Warp auto-detects the agent session and surfaces integrated controls, including rich input, code review, vertical tab metadata, and more.

## 2. Authenticate

The first time you run Claude Code, it opens your browser for login. Sign in with your Claude account. Once authenticated, the token is stored locally.

For headless environments or CI/CD, set an API key instead.

## 3. Start your first session

Navigate to any project directory and launch Claude Code:

```bash
claude
```

Try giving it a task:

```
Fix the authentication bug in login.ts
```

Claude Code finds the relevant files, shows proposed changes, and asks for confirmation before modifying anything.

## 4. Configure for your project

Create a `CLAUDE.md` file at your project root to teach Claude Code your project's conventions. Claude Code reads this file at the start of every session.

This prevents Claude Code from guessing your conventions and ensures it follows your team's standards from the first prompt.

## 5. Choose a model and permissions

Claude Code uses the latest Claude model by default. To use a specific model:

```bash
claude --model sonnet-4
```

By default, Claude Code asks for permission before every file write and command execution. Pre-approve safe operations in `.claude/settings.json`:

```json
{
  "permissions": {
    "allow": ["Read", "Edit", "Bash"]
  }
}
```

This lets Claude read files and run your test/lint commands without prompting, while still asking before writing files.

## 6. Set up agent notifications

Warp supports agent notifications for Claude Code through a plugin. When you run Claude Code in Warp without the plugin installed, a notification chip appears offering one-click installation. Once installed, Warp surfaces in-app and desktop alerts when Claude Code needs your input.

> [!tip]
> For manual installation steps, troubleshooting, and SSH/remote setup, see [Claude Code in Warp](https://docs.warp.dev/agent-platform/cli-agents/claude-code#setting-up-notifications).

## Productivity Tips

| Feature | How to Use |
|---------|------------|
| **Voice input** | Press the microphone icon or `fn` key to dictate instructions |
| **Images as context** | Paste screenshots of bug reports or mockups directly into prompts |
| **Visual diffs** | Open Code Review panel (`⌘+Shift++`) after changes to see visual diffs |
| **Parallel sessions** | Use [vertical tabs](https://docs.warp.dev/warp/terminal/windows/vertical-tabs) to run multiple sessions side by side |
| **Rich input** | Press `Ctrl+G` for full text editor experience when composing prompts |

## Next Steps

You installed Claude Code, authenticated, started your first session, configured it for your project, and learned key productivity features.

#claude-code #warp-terminal #ai-coding-agent #developer-productivity #cli-tools
