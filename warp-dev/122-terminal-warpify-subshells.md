---
title: Warpify subshells | Warp
url: https://docs.warp.dev/terminal/warpify/subshells
source: sitemap
fetched_at: 2026-04-29T15:02:59.405848669-03:00
rendered_js: false
word_count: 370
summary: This document explains how to use and configure Warpification to enable advanced IDE features within nested shell sessions like SSH, Docker, and local subshells.
tags:
    - warp-terminal
    - subshell
    - shell-integration
    - ssh
    - docker
    - terminal-configuration
category: guide
optimized: true
optimized_at: 2026-04-29T00:00:00Z
---
Warpification enables advanced IDE features within nested shell sessions like SSH, Docker, and local subshells.

## What is a subshell?

A Warp "subshell" is any nested interactive shell spawned within an existing running shell — local, Docker, or SSH. This differs from the Unix definition of any child shell process.

## How to Warpify the subshell

Warp auto-recognizes these subshell-compatible commands:

- `bash`, `fish`, `zsh`
- `docker exec`
- `gcloud compute ssh`
- `eb ssh`
- `poetry shell`

When you run a compatible command, Warp prompts you to "Warpify." The list is configurable in Subshell settings.

> [!info]
> bash, zsh, or fish (3.6+) must be set as the default shell within containers and SSH sessions for Warpification to work.

### Configuring subshell-compatible commands

Navigate to **Settings** > **Warpify** > **Subshells**.

#### Adding compatible commands

Add any command that spawns a bash, fish, or zsh subshell to `Added commands`. Regex patterns are also supported — any command matching an added regex becomes eligible for Warpification.

#### Blocklisting commands

Add commands to the Blocklist to prevent Warp from prompting you to Warpify those subshells.

### Automatically Warpify subshells

Paste the provided snippet to the end of your shell's RC file (bash, fish, or zsh). Warp will automatically Warpify subsequent subshell sessions on that machine.

The snippet outputs a Device Control String (DCS) read by Warp, signaling a subshell is ready. Warp then executes a setup script enabling blocks, completions, and the input editor.

Add the snippet at the **end** of the RC file so the shell finishes sourcing before Warp runs the setup script. To disable, remove the snippet.

Report RC file sourcing issues on [GitHub](https://github.com/warpdotdev/Warp/issues/new/choose).

## Background commands

Background commands power completions, syntax highlighting, and command corrections. In local subshells, they run in forked shell processes isolated from your session. In remote sessions, Warp runs them during idle time in a non-interactive subshell to avoid modifying session state.

### Show/hide background blocks

Background command blocks are hidden by default. Enable them via the **Blocks** menu in the macOS menu bar.

### Disable background commands in remote sessions

Set the following in `dev.warp.Warp-Stable`:

```json
"DisableInBandCommands": "true"
```

This disables tab completions, syntax highlighting, command corrections, and the git status prompt indicator in remote subshells.

#subshell
