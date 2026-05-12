---
title: Set Up Gemini CLI | Guides | Warp
url: https://docs.warp.dev/guides/external-tools-and-integrations/how-to-set-up-gemini-cli
source: sitemap
fetched_at: 2026-04-29T15:06:42.987951579-03:00
rendered_js: false
word_count: 477
summary: This document provides a comprehensive guide for installing, authenticating, and configuring the Gemini CLI tool within the Warp terminal environment.
tags:
    - gemini-cli
    - terminal-tools
    - coding-assistant
    - developer-setup
    - ai-productivity
    - node-js
category: guide
optimized: true
optimized_at: 2026-04-29T15:06:42.987951579-03:00
---
Gemini CLI is Google's open-source coding agent. It brings Gemini directly into your terminal with built-in tools for file operations, shell commands, web search, and MCP support.

## Prerequisites

- **A Google account** — Free tier includes 60 requests/minute and 1,000 requests/day. Alternatively, use a Gemini API key or Vertex AI
- **Node.js 20+** — Check with `node -v`

## 1. Install Gemini CLI

Install via npm or Homebrew:

**npm:**
```bash
npm install -g @google/gemini-cli
```

**Homebrew (macOS/Linux):**
```bash
brew install gemini-cli
```

Verify installation:
```bash
gemini --version
```

You can also run without installing using `npx @google/gemini-cli`.

When you launch Gemini CLI inside Warp, Warp auto-detects the agent session and surfaces integrated controls, including rich input, code review, vertical tab metadata, and more.

## 2. Authenticate

The first time you run Gemini CLI, it prompts you to choose an authentication method.

Select **Sign in with Google** and complete the browser authentication flow. Once authenticated, the token is stored locally.

For API key authentication (useful for CI/CD or higher rate limits):
```bash
export GOOGLE_API_KEY=your_key_here
```

For enterprise environments using Vertex AI, use Application Default Credentials (ADC):
```bash
gcloud auth application-default login
```

See the [Gemini CLI authentication guide](https://geminicli.com/docs/get-started/authentication/) for all Vertex AI auth methods.

## 3. Start your first session

Navigate to any project directory and launch Gemini CLI:
```bash
gemini
```

Try giving it a task:
```
Fix the authentication bug in login.ts
```

Gemini CLI reads relevant files, proposes changes, and asks for confirmation before modifying anything.

## 4. Configure for your project

Create a `GEMINI.md` file at your project root to teach Gemini CLI your project's conventions. Gemini CLI reads this file at the start of every session.

This prevents Gemini CLI from guessing your conventions and ensures it follows your team's standards from the first prompt.

## 5. Choose a model

Gemini CLI defaults to the latest Gemini model. To use a specific model:
```bash
gemini --model gemini-2.5-pro
```

Switch models during a session with the `/model` command. See the [Gemini CLI documentation](https://github.com/google-gemini/gemini-cli) for the current model list.

> [!warning]
> Gemini CLI does not currently support agent notifications in Warp. Keep the tab visible or check back periodically during longer tasks. All other Warp agent features work fully.

## Productivity Tips

| Feature | How to Use |
|---------|------------|
| **Voice input** | Dictate complex instructions; Warp's voice transcription works with any CLI agent |
| **Images as context** | Paste screenshots of bugs, designs, or error messages into prompts |
| **Visual diffs** | Open Code Review panel (`⌘+Shift++`) after changes to see visual diffs |
| **Run alongside other agents** | Use [vertical tabs](https://docs.warp.dev/warp/terminal/windows/vertical-tabs) to compare outputs |
| **Rich input** | Press `Ctrl+G` for full text editor experience when composing prompts |
| **Built-in Google Search** | Ask Gemini CLI to research current best practices or look up documentation |

## Next Steps

You installed Gemini CLI, authenticated with your Google account, started your first session, and configured it for your project. Gemini CLI is now set up as a working coding agent in Warp.

#gemini-cli #terminal-tools #coding-assistant #developer-setup #ai-productivity
