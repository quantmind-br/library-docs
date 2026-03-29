---
title: Scripts - OpenClaw
url: https://docs.openclaw.ai/scripts
source: sitemap
fetched_at: 2026-01-30T20:23:50.121028348-03:00
rendered_js: false
word_count: 116
summary: This document explains the purpose and usage of helper scripts in the `scripts/` directory for local workflows and operations tasks, along with conventions and guidelines for script development and maintenance.
tags:
    - scripts-directory
    - local-workflows
    - git-hooks
    - auth-monitoring
    - script-conventions
    - operations-tasks
category: reference
---

The `scripts/` directory contains helper scripts for local workflows and ops tasks. Use these when a task is clearly tied to a script; otherwise prefer the CLI.

## Conventions

- Scripts are **optional** unless referenced in docs or release checklists.
- Prefer CLI surfaces when they exist (example: auth monitoring uses `openclaw models status --check`).
- Assume scripts are host‑specific; read them before running on a new machine.

## Git hooks

- `scripts/setup-git-hooks.js`: best-effort setup for `core.hooksPath` when inside a git repo.
- `scripts/format-staged.js`: pre-commit formatter for staged `src/` and `test/` files.

## Auth monitoring scripts

Auth monitoring scripts are documented here: [/automation/auth-monitoring](https://docs.openclaw.ai/automation/auth-monitoring)

## When adding scripts

- Keep scripts focused and documented.
- Add a short entry in the relevant doc (or create one if missing).