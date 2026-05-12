---
title: Legacy SSH wrapper | Warp
url: https://docs.warp.dev/terminal/warpify/ssh-legacy
source: sitemap
fetched_at: 2026-04-29T15:03:00.177611952-03:00
rendered_js: false
word_count: 341
summary: This document explains how the Warp terminal integrates its features with SSH sessions and provides troubleshooting steps for common connection and configuration issues.
tags:
    - ssh-integration
    - terminal-features
    - troubleshooting
    - warp-terminal
    - remote-access
    - shell-configuration
category: guide
optimized: true
optimized_at: 2026-04-29T00:00:00Z
---
> [!info]
> For tmux SSH troubleshooting, see [[121-terminal-warpify-ssh|SSH]].

When you SSH into a remote box, you get all Warp features without any configuration. The input editor, auto-completions, and history search work the same on any machine.

> [!warning]
> [SSH Wrapper limitations](https://github.com/warpdotdev/Warp/issues/578) (as of May 2024):
> - Only supports `bash` or `zsh` in remote sessions. Use `command ssh` directly for other shells.
> - For zsh, `xxd` is required to bootstrap Warp.
> - `RemoteCommand` causes the SSH wrapper to fail.
> - The SSH wrapper is only initialized on your local machine — nested SSH sessions are not supported.

For zsh on the remote host, Warp creates a temp folder as `ZDOTDIR` during bootstrapping and removes it when the shell is set up.

## Implementation

Warp creates a wrapper around `/usr/bin/ssh` that sets up the shell for Warp's feature set. Authentication proceeds normally via `/usr/bin/ssh`, then Warp bootstraps the remote shell to work with Blocks and the Input Editor.

- Warp takes over the prompt, enabling a modern input editor.
- Warp configures `histcontrol` to ignore commands with leading spaces, keeping bootstrapping code out of history.

Opt out by invoking `command ssh` directly. View the SSH wrapper with `which warp_ssh_helper` (zsh) or `type warp_ssh_helper` (bash).

> [!info]
> Warp [Completions](https://docs.warp.dev/terminal/command-completions/completions) for ssh show entries from `~/.ssh/config` and `~/.ssh/known_hosts`.

## Troubleshooting

### `channel 2: open failed: connect failed: open failed`

Your server config (usually `/etc/ssh/sshd_config`) may be blocking Warp's ControlMaster connection. Completions and history from the remote host won't work until resolved.

**Fix:** Ensure `MaxSessions` is commented out or set to at least `2`. Edit requires sudo, then restart `sshd`.

### SSH Wrapper fails

There are [known issues with SSH Wrapper](https://github.com/warpdotdev/Warp/issues?q=is%3Aissue+is%3Aopen+sort%3Acreated-desc+label%3ABugs+label%3ASSH). **Workaround:**

1. Add `command ssh` to **Settings → Warpify → Subshells → Added commands**
2. Run `command ssh <user@server>` to connect

This attempts to enable Warp features as a [[122-terminal-warpify-subshells|subshell]].

> [!info]
> If the subshell workaround helps, disable the SSH Wrapper in **Settings → Features → Session**, then start a new session (or invoke `command ssh` directly).
