---
title: hyprshutdown
url: https://wiki.hypr.land/Hypr-Ecosystem/hyprshutdown/
source: sitemap
fetched_at: 2026-04-26T09:49:14.598550523-03:00
rendered_js: false
word_count: 197
summary: Graceful shutdown utility for Hyprland — opens a GUI, requests apps to exit, then quits the compositor.
tags:
    - hyprland
    - desktop-environment
    - shutdown-utility
    - linux-utilities
    - session-management
    - nvidia-troubleshooting
category: guide
optimized: true
optimized_at: 2026-04-26T00:00:00Z
---

[hyprshutdown](https://github.com/hyprwm/hyprshutdown) gracefully requests apps to exit before quitting Hyprland. Use this instead of `dispatch exit` which kills apps directly.

## Command-Line Options

| Option | Description |
|---|---|
| `--vt N` | Switch to VT N after exit (fixes NVIDIA+SDDM black screen) |
| `--dry-run` | Show UI without closing apps or exiting |
| `--no-exit` | Close apps but do not exit Hyprland |
| `--top-label`, `-t` | Custom text for shutdown dialog |
| `--post-cmd`, `-p` | Command to run after Hyprland exits |
| `--no-fork` | Run in foreground (no daemonization) |
| `--verbose` | Enable debug logging |
| `--help`, `-h` | Show help |

## System Shutdown / Reboot

```sh
hyprshutdown -t 'Shutting down...' --post-cmd 'shutdown -P 0'
hyprshutdown -t 'Restarting...' --post-cmd 'reboot'
```

## NVIDIA + SDDM Black Screen

> [!warning] NVIDIA + SDDM users may see a black screen on logout. The `--vt` flag forces a switch back to SDDM's virtual terminal (typically VT2).

**Setup — passwordless sudo for `chvt`:**

```bash
echo "$USER ALL=(ALL) NOPASSWD: /usr/bin/chvt" | sudo tee /etc/sudoers.d/chvt
sudo chmod 440 /etc/sudoers.d/chvt
```

`chvt` only switches virtual terminals — no privilege escalation risk.

> [!info] Last updated: April 20, 2026

[[006-hypr-ecosystem-hyprcursor|hyprcursor]] [[035-hypr-ecosystem-hyprpwcenter|hyprpwcenter]]

#hyprshutdown #session-management #hyprland
