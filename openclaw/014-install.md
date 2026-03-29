---
title: Index - OpenClaw
url: https://docs.openclaw.ai/install
source: sitemap
fetched_at: 2026-01-30T20:28:27.951761644-03:00
rendered_js: false
word_count: 361
summary: This document provides comprehensive instructions for installing the openclaw tool through multiple methods including installer scripts, npm, git, and containerization, along with system requirements, post-installation steps, and troubleshooting guidance.
tags:
    - installation
    - cli
    - setup
    - nodejs
    - npm
    - docker
    - troubleshooting
    - onboarding
category: guide
---

## Install

Use the installer unless you have a reason not to. It sets up the CLI and runs onboarding.

## Quick install (recommended)

```
curl -fsSL https://openclaw.bot/install.sh | bash
```

Windows (PowerShell):

```
iwr -useb https://openclaw.ai/install.ps1 | iex
```

Next step (if you skipped onboarding):

```
openclaw onboard --install-daemon
```

## System requirements

- **Node &gt;=22**
- macOS, Linux, or Windows via WSL2
- `pnpm` only if you build from source

## Choose your install path

### 1) Installer script (recommended)

Installs `openclaw` globally via npm and runs onboarding.

```
curl -fsSL https://openclaw.bot/install.sh | bash
```

Installer flags:

```
curl -fsSL https://openclaw.bot/install.sh | bash -s -- --help
```

Details: [Installer internals](https://docs.openclaw.ai/install/installer). Non-interactive (skip onboarding):

```
curl -fsSL https://openclaw.bot/install.sh | bash -s -- --no-onboard
```

### 2) Global install (manual)

If you already have Node:

```
npm install -g openclaw@latest
```

If you have libvips installed globally (common on macOS via Homebrew) and `sharp` fails to install, force prebuilt binaries:

```
SHARP_IGNORE_GLOBAL_LIBVIPS=1 npm install -g openclaw@latest
```

If you see `sharp: Please add node-gyp to your dependencies`, either install build tooling (macOS: Xcode CLT + `npm install -g node-gyp`) or use the `SHARP_IGNORE_GLOBAL_LIBVIPS=1` workaround above to skip the native build. Or:

```
pnpm add -g openclaw@latest
```

Then:

```
openclaw onboard --install-daemon
```

### 3) From source (contributors/dev)

```
git clone https://github.com/openclaw/openclaw.git
cd openclaw
pnpm install
pnpm ui:build # auto-installs UI deps on first run
pnpm build
openclaw onboard --install-daemon
```

Tip: if you don’t have a global install yet, run repo commands via `pnpm openclaw ...`.

### 4) Other install options

- Docker: [Docker](https://docs.openclaw.ai/install/docker)
- Nix: [Nix](https://docs.openclaw.ai/install/nix)
- Ansible: [Ansible](https://docs.openclaw.ai/install/ansible)
- Bun (CLI only): [Bun](https://docs.openclaw.ai/install/bun)

## After install

- Run onboarding: `openclaw onboard --install-daemon`
- Quick check: `openclaw doctor`
- Check gateway health: `openclaw status` + `openclaw health`
- Open the dashboard: `openclaw dashboard`

## Install method: npm vs git (installer)

The installer supports two methods:

- `npm` (default): `npm install -g openclaw@latest`
- `git`: clone/build from GitHub and run from a source checkout

### CLI flags

```
# Explicit npm
curl -fsSL https://openclaw.bot/install.sh | bash -s -- --install-method npm

# Install from GitHub (source checkout)
curl -fsSL https://openclaw.bot/install.sh | bash -s -- --install-method git
```

Common flags:

- `--install-method npm|git`
- `--git-dir <path>` (default: `~/openclaw`)
- `--no-git-update` (skip `git pull` when using an existing checkout)
- `--no-prompt` (disable prompts; required in CI/automation)
- `--dry-run` (print what would happen; make no changes)
- `--no-onboard` (skip onboarding)

### Environment variables

Equivalent env vars (useful for automation):

- `OPENCLAW_INSTALL_METHOD=git|npm`
- `OPENCLAW_GIT_DIR=...`
- `OPENCLAW_GIT_UPDATE=0|1`
- `OPENCLAW_NO_PROMPT=1`
- `OPENCLAW_DRY_RUN=1`
- `OPENCLAW_NO_ONBOARD=1`
- `SHARP_IGNORE_GLOBAL_LIBVIPS=0|1` (default: `1`; avoids `sharp` building against system libvips)

## Troubleshooting: `openclaw` not found (PATH)

Quick diagnosis:

```
node -v
npm -v
npm prefix -g
echo "$PATH"
```

If `$(npm prefix -g)/bin` (macOS/Linux) or `$(npm prefix -g)` (Windows) is **not** present inside `echo "$PATH"`, your shell can’t find global npm binaries (including `openclaw`). Fix: add it to your shell startup file (zsh: `~/.zshrc`, bash: `~/.bashrc`):

```
# macOS / Linux
export PATH="$(npm prefix -g)/bin:$PATH"
```

On Windows, add the output of `npm prefix -g` to your PATH. Then open a new terminal (or `rehash` in zsh / `hash -r` in bash).

## Update / uninstall

- Updates: [Updating](https://docs.openclaw.ai/install/updating)
- Migrate to a new machine: [Migrating](https://docs.openclaw.ai/install/migrating)
- Uninstall: [Uninstall](https://docs.openclaw.ai/install/uninstall)