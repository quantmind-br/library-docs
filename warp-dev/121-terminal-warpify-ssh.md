---
title: SSH with Warp features | Warp
url: https://docs.warp.dev/terminal/warpify/ssh
source: sitemap
fetched_at: 2026-04-29T15:02:59.169086289-03:00
rendered_js: false
word_count: 294
summary: This document explains the functionality of Warpifying an SSH session, which enables advanced terminal features on remote machines using tmux.
tags:
    - ssh
    - warpify
    - remote-connection
    - tmux
    - terminal-integration
    - shell-automation
category: guide
optimized: true
optimized_at: 2026-04-29T00:00:00Z
---
> [!warning]
> Some coding features (Codebase Context, code diffs, code editor, file tree) are unavailable over SSH. See [[105-terminal-ai-features|Feature support over SSH]].

> [!warning]
> This page covers SSH features powered by `tmux`. For legacy SSH, see [[124-terminal-warpify-ssh-legacy|SSH (Legacy)]].

## Overview

Warpify enables Warp features on remote machines: input editor, auto-completions, history search, and more. Commands run on the remote machine on your behalf.

> [!info]
> **Warpifying never makes lasting changes without explicit consent.**

## FAQs

### Will Warpifying make changes to the remote machine?

Only `tmux` installation, with explicit permission. If `tmux` is missing, Warp shows the commands to be run and offers installation; you can decline and continue without Warp features (or install `tmux` yourself).

### Why is `tmux` required?

`tmux` asynchronously runs commands on the remote without disrupting your session. It's a terminal multiplexer ([⭐ 35k+ on GitHub](https://github.com/tmux/tmux/wiki)) using [Control Mode](https://github.com/tmux/tmux/wiki/Control-Mode) for background tasks (autocomplete, custom prompts).

### Can I skip Warpification?

Yes—cancel at any prompt. You can also add hosts to a Denylist to never be asked again.

### Do I have to Warpify manually every time?

After manual Warpification, Warp provides a script to append to your shell's rcfile for automatic Warpification on future sessions.

### Supported shells and OSes?

- **Local:** macOS, Windows, Linux
- **Remote:** macOS, most Linux flavors
- **Shells:** `bash`, `zsh`

### What if Warp fails to detect my SSH session?

Use [[104-terminal-command-palette|Command Palette]] → "Warpify SSH Session" to warpify manually.

### What triggers SSH detection?

1. SSH session detection runs `ssh` with arguments suggesting an interactive session.
2. Aliased `ssh` or scripted usage skips detection.
3. After detecting `Last login:` or a prompt, Warp prompts to Warpify.

> [!info]
> If detection fails, you can always [[104-terminal-command-palette|Warpify manually]].

#ssh #warpify #remote-connection #tmux
