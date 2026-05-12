---
title: Cloud environments
url: https://developers.openai.com/codex/cloud/environments.md
source: llms
fetched_at: 2026-04-30T10:15:20.061803419-03:00
rendered_js: false
word_count: 433
summary: This document explains how to configure cloud environments in Codex, detailing the container lifecycle, setup scripts, environment variables, secrets management, and caching behavior.
tags:
    - cloud-environments
    - codex-configuration
    - container-setup
    - environment-variables
    - cache-management
    - task-execution
category: configuration
optimized: true
optimized_at: 2026-04-30T13:30:00Z
---
# Cloud environments

Control what Codex installs and runs during cloud tasks. Configure in [Codex settings](https://chatgpt.com/codex/settings/environments).

## How cloud tasks run

1. **Create container** — checks out repo at selected branch or commit SHA
2. **Run setup script** — plus optional maintenance script when resuming cached container
3. **Apply internet access settings** — setup scripts run with internet access. Agent internet access off by default; enable limited or unrestricted if needed. See [[053-cloud-internet-access|agent internet access]]
4. **Agent loop** — edits code, runs checks, validates work. Uses `AGENTS.md` for project-specific lint and test commands
5. **Finish** — shows answer and diff of changed files. Open a PR or ask follow-ups

## Default universal image

`universal` container image pre-installed with common languages, packages, and tools. Select **Set package versions** in environment settings to pin Python, Node.js, and other runtime versions.

For details: [openai/codex-universal](https://github.com/openai/codex-universal) (reference Dockerfile, locally pullable/testable image).

Install additional packages via [setup scripts](#manual-setup).

## Environment variables and secrets

| Type | Duration | Availability |
|------|----------|--------------|
| **Environment variables** | Full task (setup + agent phase) | Setup scripts and agent |
| **Secrets** | Setup scripts only | Removed before agent phase starts. Stored with extra encryption. |

## Automatic setup

For common package managers (`npm`, `yarn`, `pnpm`, `pip`, `pipenv`, `poetry`), Codex can automatically install dependencies and tools.

## Manual setup

Provide a custom setup script for more complex development setups:
```bash
# Install type checker
pip install pyright

# Install dependencies
poetry install --with test
pnpm install
```

Setup scripts run in a separate Bash session from the agent — commands like `export` don't persist into the agent phase. To persist environment variables, add them to `~/.bashrc` or configure in environment settings.

## Container caching

Caches container state for up to 12 hours to speed up new tasks and follow-ups.

**When cached:**
- Codex clones repository and checks out default branch
- Runs setup script and caches resulting container state

**When resumed:**
- Checks out branch specified for the task
- Runs maintenance script (optional) — useful when setup script ran on older commit and dependencies need updating

Cache automatically invalidates if you change setup script, maintenance script, environment variables, or secrets. If cached state becomes incompatible, select **Reset cache** on the environment page.

For Business and Enterprise users, caches are shared across all users with access to the environment. Invalidating affects all users in your workspace.

## Internet access and network proxy

Internet available during setup script phase. During agent phase, off by default — configure limited or unrestricted access. See [[053-cloud-internet-access|agent internet access]].

Environments run behind an HTTP/HTTPS network proxy for security and abuse prevention. All outbound internet traffic passes through this proxy.

#cloud #environments #containers #caching #codex