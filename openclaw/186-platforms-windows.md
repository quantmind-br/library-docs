---
title: Windows - OpenClaw
url: https://docs.openclaw.ai/platforms/windows
source: sitemap
fetched_at: 2026-01-30T20:25:42.81033278-03:00
rendered_js: false
word_count: 348
summary: This document provides instructions for installing and configuring OpenClaw on Windows using WSL2, including setup steps, gateway installation, and advanced networking configurations for accessing WSL services from other machines.
tags:
    - wsl2
    - windows
    - openclaw
    - gateway
    - installation
    - networking
    - ubuntu
    - cli
category: guide
---

## Windows (WSL2)

OpenClaw on Windows is recommended **via WSL2** (Ubuntu recommended). The CLI + Gateway run inside Linux, which keeps the runtime consistent and makes tooling far more compatible (Node/Bun/pnpm, Linux binaries, skills). Native Windows installs are untested and more problematic. Native Windows companion apps are planned.

## Install (WSL2)

- [Getting Started](https://docs.openclaw.ai/start/getting-started) (use inside WSL)
- [Install & updates](https://docs.openclaw.ai/install/updating)
- Official WSL2 guide (Microsoft): [https://learn.microsoft.com/windows/wsl/install](https://learn.microsoft.com/windows/wsl/install)

## Gateway

- [Gateway runbook](https://docs.openclaw.ai/gateway)
- [Configuration](https://docs.openclaw.ai/gateway/configuration)

## Gateway service install (CLI)

Inside WSL2:

```
openclaw onboard --install-daemon
```

Or:

Or:

Select **Gateway service** when prompted. Repair/migrate:

## Advanced: expose WSL services over LAN (portproxy)

WSL has its own virtual network. If another machine needs to reach a service running **inside WSL** (SSH, a local TTS server, or the Gateway), you must forward a Windows port to the current WSL IP. The WSL IP changes after restarts, so you may need to refresh the forwarding rule. Example (PowerShell **as Administrator**):

```
$Distro = "Ubuntu-24.04"
$ListenPort = 2222
$TargetPort = 22

$WslIp = (wsl -d $Distro -- hostname -I).Trim().Split(" ")[0]
if (-not $WslIp) { throw "WSL IP not found." }

netsh interface portproxy add v4tov4 listenaddress=0.0.0.0 listenport=$ListenPort `
  connectaddress=$WslIp connectport=$TargetPort
```

Allow the port through Windows Firewall (one-time):

```
New-NetFirewallRule -DisplayName "WSL SSH $ListenPort" -Direction Inbound `
  -Protocol TCP -LocalPort $ListenPort -Action Allow
```

Refresh the portproxy after WSL restarts:

```
netsh interface portproxy delete v4tov4 listenport=$ListenPort listenaddress=0.0.0.0 | Out-Null
netsh interface portproxy add v4tov4 listenport=$ListenPort listenaddress=0.0.0.0 `
  connectaddress=$WslIp connectport=$TargetPort | Out-Null
```

Notes:

- SSH from another machine targets the **Windows host IP** (example: `ssh user@windows-host -p 2222`).
- Remote nodes must point at a **reachable** Gateway URL (not `127.0.0.1`); use `openclaw status --all` to confirm.
- Use `listenaddress=0.0.0.0` for LAN access; `127.0.0.1` keeps it local only.
- If you want this automatic, register a Scheduled Task to run the refresh step at login.

## Step-by-step WSL2 install

### 1) Install WSL2 + Ubuntu

Open PowerShell (Admin):

```
wsl --install
# Or pick a distro explicitly:
wsl --list --online
wsl --install -d Ubuntu-24.04
```

Reboot if Windows asks.

### 2) Enable systemd (required for gateway install)

In your WSL terminal:

```
sudo tee /etc/wsl.conf >/dev/null <<'EOF'
[boot]
systemd=true
EOF
```

Then from PowerShell:

Re-open Ubuntu, then verify:

### 3) Install OpenClaw (inside WSL)

Follow the Linux Getting Started flow inside WSL:

```
git clone https://github.com/openclaw/openclaw.git
cd openclaw
pnpm install
pnpm ui:build # auto-installs UI deps on first run
pnpm build
openclaw onboard
```

Full guide: [Getting Started](https://docs.openclaw.ai/start/getting-started)

## Windows companion app

We do not have a Windows companion app yet. Contributions are welcome if you want contributions to make it happen.