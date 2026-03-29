---
title: Setup - OpenClaw
url: https://docs.openclaw.ai/start/setup
source: sitemap
fetched_at: 2026-01-30T20:23:32.634411487-03:00
rendered_js: false
word_count: 474
summary: This document provides instructions for setting up and customizing the OpenClaw platform, covering both stable and bleeding-edge workflows for macOS and Linux environments.
tags:
    - setup
    - configuration
    - gateway
    - macos
    - linux
    - development
    - workflow
    - authentication
category: guide
---

Last updated: 2026-01-01

## TL;DR

- **Tailoring lives outside the repo:** `~/.openclaw/workspace` (workspace) + `~/.openclaw/openclaw.json` (config).
- **Stable workflow:** install the macOS app; let it run the bundled Gateway.
- **Bleeding edge workflow:** run the Gateway yourself via `pnpm gateway:watch`, then let the macOS app attach in Local mode.

## Prereqs (from source)

- Node `>=22`
- `pnpm`
- Docker (optional; only for containerized setup/e2e — see [Docker](https://docs.openclaw.ai/install/docker))

## Tailoring strategy (so updates don’t hurt)

If you want “100% tailored to me” *and* easy updates, keep your customization in:

- **Config:** `~/.openclaw/openclaw.json` (JSON/JSON5-ish)
- **Workspace:** `~/.openclaw/workspace` (skills, prompts, memories; make it a private git repo)

Bootstrap once:

From inside this repo, use the local CLI entry:

If you don’t have a global install yet, run it via `pnpm openclaw setup`.

## Stable workflow (macOS app first)

1. Install + launch **OpenClaw.app** (menu bar).
2. Complete the onboarding/permissions checklist (TCC prompts).
3. Ensure Gateway is **Local** and running (the app manages it).
4. Link surfaces (example: WhatsApp):

<!--THE END-->

5. Sanity check:

If onboarding is not available in your build:

- Run `openclaw setup`, then `openclaw channels login`, then start the Gateway manually (`openclaw gateway`).

## Bleeding edge workflow (Gateway in a terminal)

Goal: work on the TypeScript Gateway, get hot reload, keep the macOS app UI attached.

### 0) (Optional) Run the macOS app from source too

If you also want the macOS app on the bleeding edge:

### 1) Start the dev Gateway

```
pnpm install
pnpm gateway:watch
```

`gateway:watch` runs the gateway in watch mode and reloads on TypeScript changes.

### 2) Point the macOS app at your running Gateway

In **OpenClaw.app**:

- Connection Mode: **Local** The app will attach to the running gateway on the configured port.

### 3) Verify

- In-app Gateway status should read **“Using existing gateway …”**
- Or via CLI:

### Common footguns

- **Wrong port:** Gateway WS defaults to `ws://127.0.0.1:18789`; keep app + CLI on the same port.
- **Where state lives:**
  
  - Credentials: `~/.openclaw/credentials/`
  - Sessions: `~/.openclaw/agents/<agentId>/sessions/`
  - Logs: `/tmp/openclaw/`

## Credential storage map

Use this when debugging auth or deciding what to back up:

- **WhatsApp**: `~/.openclaw/credentials/whatsapp/<accountId>/creds.json`
- **Telegram bot token**: config/env or `channels.telegram.tokenFile`
- **Discord bot token**: config/env (token file not yet supported)
- **Slack tokens**: config/env (`channels.slack.*`)
- **Pairing allowlists**: `~/.openclaw/credentials/<channel>-allowFrom.json`
- **Model auth profiles**: `~/.openclaw/agents/<agentId>/agent/auth-profiles.json`
- **Legacy OAuth import**: `~/.openclaw/credentials/oauth.json` More detail: [Security](https://docs.openclaw.ai/gateway/security#credential-storage-map).

## Updating (without wrecking your setup)

- Keep `~/.openclaw/workspace` and `~/.openclaw/` as “your stuff”; don’t put personal prompts/config into the `openclaw` repo.
- Updating source: `git pull` + `pnpm install` (when lockfile changed) + keep using `pnpm gateway:watch`.

## Linux (systemd user service)

Linux installs use a systemd **user** service. By default, systemd stops user services on logout/idle, which kills the Gateway. Onboarding attempts to enable lingering for you (may prompt for sudo). If it’s still off, run:

```
sudo loginctl enable-linger $USER
```

For always-on or multi-user servers, consider a **system** service instead of a user service (no lingering needed). See [Gateway runbook](https://docs.openclaw.ai/gateway) for the systemd notes.

- [Gateway runbook](https://docs.openclaw.ai/gateway) (flags, supervision, ports)
- [Gateway configuration](https://docs.openclaw.ai/gateway/configuration) (config schema + examples)
- [Discord](https://docs.openclaw.ai/channels/discord) and [Telegram](https://docs.openclaw.ai/channels/telegram) (reply tags + replyToMode settings)
- [OpenClaw assistant setup](https://docs.openclaw.ai/start/openclaw)
- [macOS app](https://docs.openclaw.ai/platforms/macos) (gateway lifecycle)