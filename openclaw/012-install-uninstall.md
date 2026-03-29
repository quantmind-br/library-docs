---
title: Uninstall - OpenClaw
url: https://docs.openclaw.ai/install/uninstall
source: sitemap
fetched_at: 2026-01-30T20:28:46.111024707-03:00
rendered_js: false
word_count: 322
summary: Provides instructions for completely uninstalling the OpenClaw CLI tool and its associated services across different operating systems, including both automated and manual removal methods.
tags:
    - uninstall
    - cli
    - gateway-service
    - macos
    - linux
    - windows
    - openclaw
    - removal
category: guide
---

Two paths:

- **Easy path** if `openclaw` is still installed.
- **Manual service removal** if the CLI is gone but the service is still running.

## Easy path (CLI still installed)

Recommended: use the built-in uninstaller:

Non-interactive (automation / npx):

```
openclaw uninstall --all --yes --non-interactive
npx -y openclaw uninstall --all --yes --non-interactive
```

Manual steps (same result):

1. Stop the gateway service:

<!--THE END-->

2. Uninstall the gateway service (launchd/systemd/schtasks):

```
openclaw gateway uninstall
```

3. Delete state + config:

```
rm -rf "${OPENCLAW_STATE_DIR:-$HOME/.openclaw}"
```

If you set `OPENCLAW_CONFIG_PATH` to a custom location outside the state dir, delete that file too.

4. Delete your workspace (optional, removes agent files):

```
rm -rf ~/.openclaw/workspace
```

5. Remove the CLI install (pick the one you used):

```
npm rm -g openclaw
pnpm remove -g openclaw
bun remove -g openclaw
```

6. If you installed the macOS app:

```
rm -rf /Applications/OpenClaw.app
```

Notes:

- If you used profiles (`--profile` / `OPENCLAW_PROFILE`), repeat step 3 for each state dir (defaults are `~/.openclaw-<profile>`).
- In remote mode, the state dir lives on the **gateway host**, so run steps 1-4 there too.

## Manual service removal (CLI not installed)

Use this if the gateway service keeps running but `openclaw` is missing.

### macOS (launchd)

Default label is `bot.molt.gateway` (or `bot.molt.<profile>`; legacy `com.openclaw.*` may still exist):

```
launchctl bootout gui/$UID/bot.molt.gateway
rm -f ~/Library/LaunchAgents/bot.molt.gateway.plist
```

If you used a profile, replace the label and plist name with `bot.molt.<profile>`. Remove any legacy `com.openclaw.*` plists if present.

### Linux (systemd user unit)

Default unit name is `openclaw-gateway.service` (or `openclaw-gateway-<profile>.service`):

```
systemctl --user disable --now openclaw-gateway.service
rm -f ~/.config/systemd/user/openclaw-gateway.service
systemctl --user daemon-reload
```

### Windows (Scheduled Task)

Default task name is `OpenClaw Gateway` (or `OpenClaw Gateway (<profile>)`). The task script lives under your state dir.

```
schtasks /Delete /F /TN "OpenClaw Gateway"
Remove-Item -Force "$env:USERPROFILE\.openclaw\gateway.cmd"
```

If you used a profile, delete the matching task name and `~\.openclaw-<profile>\gateway.cmd`.

## Normal install vs source checkout

### Normal install (install.sh / npm / pnpm / bun)

If you used `https://openclaw.bot/install.sh` or `install.ps1`, the CLI was installed with `npm install -g openclaw@latest`. Remove it with `npm rm -g openclaw` (or `pnpm remove -g` / `bun remove -g` if you installed that way).

### Source checkout (git clone)

If you run from a repo checkout (`git clone` + `openclaw ...` / `bun run openclaw ...`):

1. Uninstall the gateway service **before** deleting the repo (use the easy path above or manual service removal).
2. Delete the repo directory.
3. Remove state + workspace as shown above.