---
title: Crashes and Bugs
url: https://wiki.hypr.land/Crashes-and-Bugs/
source: sitemap
fetched_at: 2026-04-26T09:48:36.599062682-03:00
rendered_js: false
word_count: 719
summary: This document provides comprehensive procedures for debugging, diagnosing crashes, and gathering technical logs for the Hyprland window manager.
tags:
    - hyprland
    - debugging
    - linux
    - crash-report
    - system-logs
    - wayland
    - git-bisect
category: guide
optimized: true
optimized_at: 2026-04-26T00:00:00Z
---

## Getting the log

Enable logs in `hyprland.conf`:

```ini
debug:disable_logs = false
debug:gl_debugging = true
```

> [!warning]
> Disable these when done — they cause a performance hit.

Log locations:

```sh
# From TTY (if crashed session was last launched)
cat $XDG_RUNTIME_DIR/hypr/$(ls -t $XDG_RUNTIME_DIR/hypr/ | head -n 1)/hyprland.log

# From within Hyprland (last session's log)
cat $XDG_RUNTIME_DIR/hypr/$(ls -t $XDG_RUNTIME_DIR/hypr/ | head -n 2 | tail -n 1)/hyprland.log
```

## Obtaining the Crash Report

Crash report directory: `$XDG_CACHE_HOME/hyprland` (or `$HOME/.cache/hyprland` if unset).

Look for `hyprlandCrashReport[XXXX].txt` where `[XXXX]` is the crashed process PID. Attach this file to your issue.

## Crashes at Launch

Diagnose by log contents:

| Error | Action |
|---|---|
| `backend failed to start` | Launch in TTY, refer to RED logs |
| `Monitor X has NO PREFERRED MODE, and an INVALID one was requested` | Monitor issue |
| Other | Use `coredumpctl`, find latest PID, run `coredumpctl info PID` |
| Driver failure (e.g. `radeon`) | Report issue |
| Hyprland failure | Report issue |

## Crashes not at Launch

Report on GitHub or Discord.

## Debug Stacktrace

> [!info]
> Systemd-only.

1. Build Hyprland in debug: `make debug`
2. Start Hyprland and trigger the crash
3. In tty/terminal: `coredumpctl debug Hyprland`
   - Say `y` if gdb asks for symbols
   - Say `c` if it asks about paging
4. At `(gdb)` prompt: `set logging file output.log` then `set logging enabled`
5. Run `bt -full`, then `exit`, and attach `output.log`

## Trace Log

Launch Hyprland with:

```sh
HYPRLAND_TRACE=1 AQ_TRACE=1 Hyprland
```

> [!warning]
> These produce very verbose logging and massive log files. Reproduce the issue as fast as possible.

## Bugs

> [!tip]
> READ the [FAQ](https://wiki.hypr.land/FAQ) first.

If not listed there, ask on Discord or open a [GitHub discussion](https://github.com/hyprwm/Hyprland/discussions).

## Git Bisecting

"Bisecting" finds the first git commit that introduced a bug/regression using binary search.

```sh
git clone --recursive https://github.com/hyprwm/Hyprland
cd Hyprland

# Start bisect: replace [good] and [bad] with actual commit hashes
git bisect good [good commit]
git bisect bad [bad commit]

# For each step: reset, build, test
git reset --hard --recurse-submodules
make all
./build/Hyprland  # run from TTY
```

- If bug is absent → `git bisect good`
- If bug is present → `git bisect bad`
- If build error → `git bisect skip`

Continue until git identifies the first bad commit.

## Building with ASan

> [!info]
> Deepest level of memory issue debugging. Do this in tty with no Hyprland instances running.

```sh
git clone --recursive https://github.com/hyprwm/Hyprland
make asan
Hyprland  # reproduce crash
```

Search for `asan.log.XXXXX` files in `cwd`, `~`, or `./build`. Zip and attach to issue.

## Debugging DRM Issues

DRM (Direct Rendering Manager) issues cause freezes and glitches.

> [!warning]
> DRM logs are EXTREMELY verbose. Reproduce the bug ASAP to avoid a 1GB log file.

```sh
echo 0x19F | sudo tee /sys/module/drm/parameters/debug  # enables verbose drm logging
sudo dmesg -C                                           # clears kernel debug logs
dmesg -w > ~/dmesg.log &                                 # writes kernel logs to ~/dmesg.log
Hyprland
# ... repro the issue, then quit Hyprland
fg  # CTRL+C to stop writing logs
echo 0 | sudo tee /sys/module/drm/parameters/debug       # disables drm logging
```

Attach `dmesg.log` to your issue.