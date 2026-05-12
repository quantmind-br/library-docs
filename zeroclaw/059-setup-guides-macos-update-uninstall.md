---
title: macOS Update and Uninstall Guide
date: 2026-05-05T00:00:00Z
url: https://github.com/openagen/zeroclaw/blob/master/docs/setup-guides/macos-update-uninstall.md
source: git
fetched_at: 2026-05-02T14:52:14.654357376-03:00
rendered_js: false
word_count: 157
summary: This document outlines the standard procedures for updating and uninstalling the ZeroClaw software on macOS, covering various installation methods and cleanup steps.
tags:
    - macos
    - software-update
    - uninstall-guide
    - zeroclaw
    - cli-tools
    - system-maintenance
category: guide
optimized: true
optimized_at: 2026-05-05T00:00:00Z
---
# macOS Update and Uninstall Guide

Last verified: **February 22, 2026**

## Check current install method

```bash
which zeroclaw
zeroclaw --version
```

Typical locations:
- Homebrew: `/opt/homebrew/bin/zeroclaw` (Apple Silicon) or `/usr/local/bin/zeroclaw` (Intel)
- Cargo/bootstrap/manual: `~/.cargo/bin/zeroclaw`

If both exist, shell `PATH` order decides which one runs.

## Update on macOS

### Homebrew install

```bash
brew update
brew upgrade zeroclaw
zeroclaw --version
```

### Clone + bootstrap install

From local repository checkout:

```bash
git pull --ff-only
./install.sh --prefer-prebuilt
zeroclaw --version
```

Source-only update:

```bash
git pull --ff-only
cargo install --path . --force --locked
zeroclaw --version
```

### Manual prebuilt binary install

Re-run download/install flow with latest release asset, then verify:

```bash
zeroclaw --version
```

## Uninstall on macOS

### Stop and remove background service first

Prevents daemon from continuing after binary removal.

```bash
zeroclaw service stop || true
zeroclaw service uninstall || true
```

Service artifacts removed by `service uninstall`:
- `~/Library/LaunchAgents/com.zeroclaw.daemon.plist`

### Remove the binary by install method

**Homebrew:**

```bash
brew uninstall zeroclaw
```

**Cargo/bootstrap/manual** (`~/.cargo/bin/zeroclaw`):

```bash
cargo uninstall zeroclaw || true
rm -f ~/.cargo/bin/zeroclaw
```

### Optional: remove local runtime data

Run only for full cleanup of config, auth profiles, logs, and workspace state.

```bash
rm -rf ~/.zeroclaw
```

## Verify uninstall completed

```bash
command -v zeroclaw || echo "zeroclaw binary not found"
pgrep -fl zeroclaw || echo "No running zeroclaw process"
```

If `pgrep` still finds a process, stop manually and re-check:

```bash
pkill -f zeroclaw
```

## Related docs

- [[001-setup-guides-one-click-bootstrap|One-Click Bootstrap]]
- [[120-reference-cli-commands-reference|Commands Reference]]
- [[069-ops-operations-runbook|Troubleshooting]]

#macos #software-update #uninstall-guide #zeroclaw #cli-tools #system-maintenance
