---
title: Sandbox
url: https://developers.openai.com/codex/concepts/sandboxing.md
source: llms
fetched_at: 2026-04-30T10:15:24.002508509-03:00
rendered_js: false
word_count: 642
summary: This document explains the purpose and configuration of the Codex sandbox, a security feature that provides a constrained environment for agentic tasks to execute commands safely.
tags:
    - security-boundary
    - sandbox-configuration
    - agentic-automation
    - permissions-management
    - codex-environment
    - system-security
category: concept
optimized: true
optimized_at: 2026-04-30T13:30:00Z
---
# Sandbox

The boundary that lets Codex act autonomously without unrestricted machine access. Commands in the **Codex app**, **IDE extension**, or **CLI** run inside a constrained environment by default.

Defines what Codex can do on its own: which files it can modify, whether commands can use the network. When a task stays inside boundaries, Codex keeps moving without confirmation. When it needs to go beyond, Codex falls back to the approval flow.

Sandboxing and approvals are different controls:
- **Sandbox** = technical boundaries
- **Approval policy** = when Codex must stop and ask before crossing them

## What the sandbox does

Applies to spawned commands, not just built-in file operations. Tools like `git`, package managers, and test runners inherit the same sandbox boundaries.

Platform-native enforcement on each OS. Implementation differs between macOS, Linux, WSL2, and native Windows, but the concept is the same: bounded workspace for routine autonomous tasks.

## Why it matters

Reduces approval fatigue. Codex can read files, make edits, and run routine project commands within the boundary you already approved.

Provides a clearer trust model: you aren't just trusting the agent's intentions; you're trusting that it operates inside enforced limits.

## Getting started

Codex applies sandboxing automatically in default permissions mode.

### Prerequisites

- **macOS**: works out of the box using Seatbelt framework.
- **Windows**: native [[038-windows|Windows sandbox]] in PowerShell; Linux sandbox implementation in WSL2.
- **Linux / WSL2**: install `bubblewrap` first:

  ```bash
  # Ubuntu/Debian
  sudo apt install bubblewrap

  # Fedora
  sudo dnf install bubblewrap
  ```

Codex uses first `bwrap` executable on `PATH`. If unavailable, falls back to a bundled helper requiring unprivileged user namespace creation. Installing the distribution package keeps setup reliable.

Startup warning appears when `bwrap` is missing or helper can't create user namespace. On distributions restricting this AppArmor setting, prefer loading the `bwrap` AppArmor profile.

**Ubuntu AppArmor note:**
- **Ubuntu 25.04**: installing `bubblewrap` from Ubuntu's repo should work without extra setup. `bwrap-userns-restrict` profile ships in `apparmor` package at `/etc/apparmor.d/bwrap-userns-restrict`.
- **Ubuntu 24.04**: may still warn after installation. Copy and load extra profile:
  ```bash
  sudo apt update
  sudo apt install apparmor-profiles apparmor-utils
  sudo install -m 0644 \
    /usr/share/apparmor/extra-profiles/bwrap-userns-restrict \
    /etc/apparmor.d/bwrap-userns-restrict
  sudo apparmor_parser -r /etc/apparmor.d/bwrap-userns-restrict
  ```
  `apparmor_parser -r` loads profile without reboot. Or reload all profiles:
  ```bash
  sudo systemctl reload apparmor.service
  ```
  If profile unavailable or doesn't resolve:
  ```bash
  sudo sysctl -w kernel.apparmor_restrict_unprivileged_userns=0
  ```

## How you control it

In the Codex app and IDE, choose a mode from the permissions selector under the composer or chat input: default permissions, full access, or custom configuration.

In the CLI, use [[014-cli-slash-commands|/permissions]] to switch modes during a session.

## Configure defaults

Store defaults in `config.toml`:

| Setting | Key | Description |
|---------|-----|-------------|
| Sandbox mode | `sandbox_mode` | `read-only`, `workspace-write`, `danger-full-access` |
| Approval policy | `approval_policy` | `untrusted`, `on-request`, `never` |
| Writable roots | `sandbox_workspace_write.writable_roots` | Extend modification areas without removing sandbox |

Common modes:
- `read-only` — inspect files, no edits or commands without approval
- `workspace-write` — read, edit within workspace, run routine local commands (default low-friction mode)
- `danger-full-access` — no sandbox restrictions. Removes filesystem and network boundaries.

Approval policies:
- `untrusted` — asks before running commands not in trusted set
- `on-request` — works inside sandbox by default, asks when going beyond
- `never` — doesn't stop for approval prompts

**Full access** = `sandbox_mode = "danger-full-access"` + `approval_policy = "never"`.
**`--full-auto`** = lower-risk preset: `workspace-write` + `on-request`.

Writable roots let Codex work across multiple directories without removing the sandbox entirely.

For reusable permission sets, define `[permissions.<name>.filesystem]` or `[permissions.<name>.network]`. Managed network profiles use map tables (`domains`, `unix_sockets`). Filesystem profiles can deny reads for exact paths or glob patterns by setting entries to `"none"` — keep local secrets unreadable without turning off workspace writes.

For specific exceptions, use [[061-rules|rules]] to allow, prompt, or forbid command prefixes outside the sandbox — often better than broadly expanding access.

Automatic review (when available) doesn't change the sandbox boundary. It reviews approval requests (sandbox escalations, network access) while actions already allowed inside run without extra review.

Platform details: [[038-windows|Windows]] for native setup/behavior/troubleshooting; [[041-agent-approvals-security|Agent approvals & security]] for admin requirements and org-level constraints.

#sandbox #security #permissions #configuration #codex