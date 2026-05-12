---
title: Warp quickstart | Warp
url: https://docs.warp.dev/getting-started/quickstart
source: sitemap
fetched_at: 2026-04-29T15:01:59.559542913-03:00
rendered_js: false
word_count: 704
summary: This document provides an introductory guide for installing the Warp terminal, utilizing its core features like command blocks and the input editor, and interacting with the integrated AI agent.
tags:
    - terminal-emulator
    - warp-setup
    - command-line-interface
    - ai-agent
    - developer-productivity
    - getting-started
category: guide
optimized: true
optimized_at: 2026-04-29T00:00:00Z
---
This guide walks you through installing Warp, trying the terminal features you'll use every day, and firing off your first agent prompt. After completing the steps in this guide, you'll have a working Warp setup and a clear picture of how terminal commands and agents work together.

## Prerequisites

- **macOS, Windows, or Linux** — See [[015-getting-started-installation-and-setup|Installation and setup]] for minimum requirements per platform.

## 1. Install Warp

Download Warp from [warp.dev](https://www.warp.dev/download) and follow the installer for your platform.

Download and drag Warp into your Applications folder, or install with Homebrew:

```bash
brew install warp-cli
```

When you launch Warp, you'll see a terminal session ready for input. You can optionally sign up for an account (top right), or skip and start using Warp immediately.

## 2. Run a command and see Blocks

Run any command you'd normally use, for example:

```bash
echo "Hello, Warp"
```

You'll notice the output looks different from a traditional terminal. Every command and its output is grouped into a **Block** — a contained unit you can copy, search, filter, and navigate independently. Blocks are the foundation of how Warp organizes your terminal.

**What you can do with Blocks:**

- Click a Block to select it, then press `⌘C` (macOS) or `Ctrl+Shift+C` (Windows/Linux) to copy the output
- Use `⌘↑`/`⌘↓` (macOS) or `Ctrl+↑`/`Ctrl+↓` (Windows/Linux) to navigate between Blocks
- Click the filter icon on a Block to search within its output

Learn more about navigating, selecting, and acting on output in [[093-terminal-blocks-block-basics|Block basics]].

## 3. Try the input editor

Warp's input isn't a standard terminal prompt, it's a real text editor. Try the following functionality:

- **Multi-line editing** — Press `Shift+Enter` to add a new line. Try typing three separate `echo` lines, pressing `Shift+Enter` between each, then `Enter` to run them all at once.
- **Click to place your cursor** — Click anywhere in your input to move the cursor, just like a text editor.
- **Select and edit** — Click and drag to select text, then type to replace it.

All three commands run in sequence, and each produces its own Block. No need to run commands one at a time.

Learn more about cursor movement, selections, and multi-line input in [[242-terminal-editor|Modern text editing]].

## 4. See autosuggestions and completions

Start typing a command you've run before. You'll see a faded suggestion appear inline based on your shell history. Press `→` to accept it instantly.

Press `Tab` while typing to see completions for commands, flags, and file paths. Warp provides enhanced completions beyond what your shell offers natively.

If you mistype a command, Warp detects the error and suggests a correction. Accept the fix or dismiss it and continue.

Learn more about [[241-terminal-command-completions-autosuggestions|autosuggestions]] and [[099-terminal-command-completions-completions|tab completions]].

## 5. Ask your first agent question

Everything you've done so far has been in **terminal mode**, running shell commands the way you normally would. Warp also has **Agent Mode**, a dedicated conversation view where you interact with Oz, Warp's built-in agent, using natural language.

Start an agent conversation by pressing `⌘↩` (macOS) or `Ctrl+Shift+Enter` (Windows/Linux). Then type a prompt:

> Explain what this code does: [paste code]

Oz reads your codebase, understands its structure, and responds with a context-aware explanation. From here you can ask follow-up questions, have Oz write or refactor code, debug errors, or run commands on your behalf — all within the same conversation.

> [!tip]
> You don't always need to switch modes manually. If you type a natural-language prompt in terminal mode, Warp auto-detects it and offers to send it to an agent.

Warp also works with third-party CLI agents like Claude Code and Codex. Learn more about [[065-agent-platform-third-party-agents-claude-code|third-party CLI agents]].

To learn more about switching between modes, see [[213-agent-platform-warp-agents-interacting-with-agents-terminal-and-agent-modes|Terminal and Agent modes]].

## What to explore next

Now that you have the basics, check out the features that make Warp a full development environment:

- [[014-getting-started-customizing-warp|**Customizing Warp**]] — Pick a theme, configure your prompt, choose your AI model, and import keybindings from another terminal.
- [[037-agent-platform-warp-agents-capabilities-overview-codebase-context|**Codebase Context**]] — Index your Git repositories so agents understand your code and give context-aware answers across large, multi-repo systems.
- [[194-agent-platform-cloud-agents-overview|**Oz cloud agents**]] — Run agents in the background for PR review, issue triage, dependency updates, and other tasks that don't need your immediate attention.

#terminal-emulator #warp-setup #ai-agent #getting-started