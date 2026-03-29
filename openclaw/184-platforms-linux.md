---
title: Linux - OpenClaw
url: https://docs.openclaw.ai/platforms/linux
source: sitemap
fetched_at: 2026-01-30T20:27:28.629089286-03:00
rendered_js: false
word_count: 142
summary: This document provides instructions for installing and running the OpenClaw Gateway on Linux systems, including setup on VPS environments and systemd service configuration.
tags:
    - linux
    - gateway
    - installation
    - nodejs
    - systemd
    - vps
    - deployment
category: guide
---

## Linux App

The Gateway is fully supported on Linux. **Node is the recommended runtime**. Bun is not recommended for the Gateway (WhatsApp/Telegram bugs). Native Linux companion apps are planned. Contributions are welcome if you want to help build one.

## Beginner quick path (VPS)

1. Install Node 22+
2. `npm i -g openclaw@latest`
3. `openclaw onboard --install-daemon`
4. From your laptop: `ssh -N -L 18789:127.0.0.1:18789 <user>@<host>`
5. Open `http://127.0.0.1:18789/` and paste your token

Step-by-step VPS guide: [exe.dev](https://docs.openclaw.ai/platforms/exe-dev)

## Install

- [Getting Started](https://docs.openclaw.ai/start/getting-started)
- [Install & updates](https://docs.openclaw.ai/install/updating)
- Optional flows: [Bun (experimental)](https://docs.openclaw.ai/install/bun), [Nix](https://docs.openclaw.ai/install/nix), [Docker](https://docs.openclaw.ai/install/docker)

## Gateway

- [Gateway runbook](https://docs.openclaw.ai/gateway)
- [Configuration](https://docs.openclaw.ai/gateway/configuration)

## Gateway service install (CLI)

Use one of these:

```
openclaw onboard --install-daemon
```

Or:

Or:

Select **Gateway service** when prompted. Repair/migrate:

## System control (systemd user unit)

OpenClaw installs a systemd **user** service by default. Use a **system** service for shared or always-on servers. The full unit example and guidance live in the [Gateway runbook](https://docs.openclaw.ai/gateway). Minimal setup: Create `~/.config/systemd/user/openclaw-gateway[-<profile>].service`:

```
[Unit]
Description=OpenClaw Gateway (profile: <profile>, v<version>)
After=network-online.target
Wants=network-online.target

[Service]
ExecStart=/usr/local/bin/openclaw gateway --port 18789
Restart=always
RestartSec=5

[Install]
WantedBy=default.target
```

Enable it:

```
systemctl --user enable --now openclaw-gateway[-<profile>].service
```