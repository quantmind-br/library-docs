---
title: Known Issues | Support & Community | Warp
url: https://docs.warp.dev/support-and-community/troubleshooting-and-support/known-issues
source: sitemap
fetched_at: 2026-04-29T15:05:43.545117582-03:00
rendered_js: false
word_count: 645
summary: This document provides troubleshooting steps and known issues for the Warp terminal, including guidance on shell configurations, tool incompatibilities, and operating system permissions.
tags:
    - warp-terminal
    - troubleshooting
    - ssh-configuration
    - shell-integration
    - debugging
    - known-issues
category: guide
optimized: true
optimized_at: 2026-04-29T00:00:00Z
---
> [!info]
> For a complete list of Warp issues and feature requests, visit the [GitHub issues page](https://github.com/warpdotdev/Warp/issues?q=is%3Aissue%20is%3Aopen%20sort%3Acreated-desc).

## General

### SSH

To enable Blocks over SSH, Warp uses an SSH Wrapper function. Navigate to **Settings** > **Features** to disable if needed. See [[120-terminal-warpify-ssh-legacy]] for legacy SSH troubleshooting, or [[121-terminal-warpify-ssh]] for new SSH features.

### Online features don't work

Online features (Oz agent, Generate, Block Sharing, Refer a Friend) may break due to a stale login token (typically from a password change).

**Resolution:**
1. Remove Warp user login:
   ```bash
   rm -rf ~/Library/Application\ Support/warp/*
   ```
2. Restart Warp and sign in again.

### English-only UI

The UI currently only supports English, though character support for Chinese, Korean, and Japanese has been added.

### Abnormal rendering of Chinese characters

Add the following to your rc file to resolve:
```bash
export LANG=en_US.UTF-8
```

### Warp fails to render a window

This may occur due to corruption in the local SQLite database. Try renaming the database found at the [session restoration locations](https://docs.warp.dev/terminal/sessions/session-restoration#session-restoration-database).

### Misc

- When you SSH, Warp starts a bash shell on the remote host with a wrapper to enable Warp features.
- If your default shell is zsh, aliases typically do not transfer over.
- Warp may become unresponsive if it lacks permission to access folders.

## Agent Mode

- Agent Mode blocks are not shareable during [[146-knowledge-and-collaboration-session-sharing]]. Participants can share regular shell commands, but not AI interactions.
- Agents do not have up-to-date information on several commands' completion specs.
- Agent Mode works better with Warp's default prompt settings (prompt on a new line) than with same-line prompts. With same-line prompts, the cursor jumps from end of line to start of input box when switching to Agent Mode.

## Shells

### Fish shell `read` command

Fish shell version 3.6 and below has a bug causing the `read` built-in command to break Warp's integration. Upgrade fish to the most recent version to resolve.

### Warp shell loads slowly due to EDR

If commenting out rc files (`~/.zshrc`, `~/.bashrc`, `~/.config/fish/config.fish`) still causes slowdown, an Endpoint Detection and Response (EDR) tool (Sentinel One, CrowdStrike, Carbon Black) may be the cause. Restart your system. If the issue persists, [send feedback](https://github.com/warpdotdev/gitbook/blob/main/docs/README.md) with EDR, OS, shell details.

### Configuring and debugging your RC files

Warp builds custom support for shell functionality to enable Blocks, native Input Editor, AI blocks, etc. This leads to incompatibility with various tools and plugins.

**Debugging process:**
1. Move or comment out your `.bashrc` (for Bash)
2. If Warp starts working, something in your dotfiles is incompatible
3. Isolate the culprit by iteratively disabling sections with the `WarpTerminal` flag

**Example — comment out problematic tools for Warp only:**
```bash
# Only apply for Warp
if [[ "$TERM_PROGRAM" == "WarpTerminal" ]]; then
  # Disable conflicting plugin
  # plugin_that_breaks_warp
fi
```

## List of incompatible tools

> [!warning]
> Non-exhaustive list. If you find an incompatible tool, email [feedback@warp.dev](mailto:feedback@warp.dev).

- **BIND keys**
  - `bindkey '^j' down-line-or-beginning-search` — requires hitting ENTER twice
  - `bindkey 'tab' autosuggest-accept` — breaks autocompletion
- **OH-MY-ZSH Themes** — avit, spaceship, others
- **OH-MY-ZSH Plugins** — zsh-autosuggestions, zsh-autocomplete, others
- **Oh-My-Tmux**
- **zsh4h** (ZSH for Humans)
- **znap**
- **FZF**
- `[[ -r "/usr/local/etc/profile.d/bash_completion.sh" ]] && "/usr/local/etc/profile.d/bash_completion.sh"`
- `eval "$(rbenv init -)"`
- **grml-zsh-config**
- **zle-line-init**

## Operating systems

### SSH to local network device is denied on macOS

1. Go to **System Settings** > **Privacy & Security** > **Local Network**
2. Add Warp to the allowed apps list

### Unexpected loss of permission on macOS

1. [Apply pending Warp updates](https://docs.warp.dev/support-and-community/troubleshooting-and-support/updating-warp) so the new binary has correct permissions
2. Track this issue on [GitHub](https://github.com/warpdotdev/Warp/issues/3009)

### Auto-Update error on macOS

Resolved for current releases. To avoid: update Warp *before* upgrading to macOS Ventura. If experiencing the error:

1. Go to the macOS Applications folder
2. Right-click Warp > **Open**
3. In the '"Warp" is damaged' dialog, click **Open**

### Running x86 commands with Rosetta on macOS

1. Go to **Finder** > **Applications**, search for Warp
2. Right-click > **Get Info**
3. Check **Open with Rosetta**

#warp-terminal #troubleshooting #known-issues
