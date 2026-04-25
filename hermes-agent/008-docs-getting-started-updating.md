---
title: Updating & Uninstalling | Hermes Agent
url: https://hermes-agent.nousresearch.com/docs/getting-started/updating
source: crawler
fetched_at: 2026-04-24T17:00:17.595961534-03:00
rendered_js: false
word_count: 582
summary: This document serves as a comprehensive guide detailing the process of updating and uninstalling the Hermes Agent, covering automated update flows, manual procedures for various environments, and crucial post-update validation steps.
tags:
    - updating-process
    - agent-maintenance
    - hermes-agent
    - manual-update
    - rollback-guide
    - nix-users
    - uninstallation
category: guide
---

## Updating[​](#updating "Direct link to Updating")

Update to the latest version with a single command:

This pulls the latest code, updates dependencies, and prompts you to configure any new options that were added since your last update.

tip

`hermes update` automatically detects new configuration options and prompts you to add them. If you skipped that prompt, you can manually run `hermes config check` to see missing options, then `hermes config migrate` to interactively add them.

### What happens during an update[​](#what-happens-during-an-update "Direct link to What happens during an update")

When you run `hermes update`, the following steps occur:

1. **Git pull** — pulls the latest code from the `main` branch and updates submodules
2. **Dependency install** — runs `uv pip install -e ".[all]"` to pick up new or changed dependencies
3. **Config migration** — detects new config options added since your version and prompts you to set them
4. **Gateway auto-restart** — if the gateway service is running (systemd on Linux, launchd on macOS), it is **automatically restarted** after the update completes so the new code takes effect immediately

Expected output looks like:

```text
$ hermes update
Updating Hermes Agent...
📥 Pulling latest code...
Already up to date.  (or: Updating abc1234..def5678)
📦 Updating dependencies...
✅ Dependencies updated
🔍 Checking for new config options...
✅ Config is up to date  (or: Found 2 new options — running migration...)
🔄 Restarting gateway service...
✅ Gateway restarted
✅ Hermes Agent updated successfully!
```

### Recommended Post-Update Validation[​](#recommended-post-update-validation "Direct link to Recommended Post-Update Validation")

`hermes update` handles the main update path, but a quick validation confirms everything landed cleanly:

1. `git status --short` — if the tree is unexpectedly dirty, inspect before continuing
2. `hermes doctor` — checks config, dependencies, and service health
3. `hermes --version` — confirm the version bumped as expected
4. If you use the gateway: `hermes gateway status`
5. If `doctor` reports npm audit issues: run `npm audit fix` in the flagged directory

Dirty working tree after update

If `git status --short` shows unexpected changes after `hermes update`, stop and inspect them before continuing. This usually means local modifications were reapplied on top of the updated code, or a dependency step refreshed lockfiles.

### If your terminal disconnects mid-update[​](#if-your-terminal-disconnects-mid-update "Direct link to If your terminal disconnects mid-update")

`hermes update` protects itself against accidental terminal loss:

- The update ignores `SIGHUP`, so closing your SSH session or terminal window no longer kills it mid-install. `pip` and `git` child processes inherit this protection, so the Python environment cannot be left half-installed by a dropped connection.
- All output is mirrored to `~/.hermes/logs/update.log` while the update runs. If your terminal disappears, reconnect and inspect the log to see whether the update finished and whether the gateway restart succeeded:

```bash
tail-f ~/.hermes/logs/update.log
```

- `Ctrl-C` (SIGINT) and system shutdown (SIGTERM) are still honored — those are deliberate cancellations, not accidents.

You no longer need to wrap `hermes update` in `screen` or `tmux` to survive a terminal drop.

### Checking your current version[​](#checking-your-current-version "Direct link to Checking your current version")

Compare against the latest release at the [GitHub releases page](https://github.com/NousResearch/hermes-agent/releases).

### Updating from Messaging Platforms[​](#updating-from-messaging-platforms "Direct link to Updating from Messaging Platforms")

You can also update directly from Telegram, Discord, Slack, or WhatsApp by sending:

This pulls the latest code, updates dependencies, and restarts the gateway. The bot will briefly go offline during the restart (typically 5–15 seconds) and then resume.

### Manual Update[​](#manual-update "Direct link to Manual Update")

If you installed manually (not via the quick installer):

```bash
cd /path/to/hermes-agent
exportVIRTUAL_ENV="$(pwd)/venv"

# Pull latest code and submodules
git pull origin main
git submodule update --init--recursive

# Reinstall (picks up new dependencies)
uv pip install-e".[all]"
uv pip install-e"./tinker-atropos"

# Check for new config options
hermes config check
hermes config migrate   # Interactively add any missing options
```

### Rollback instructions[​](#rollback-instructions "Direct link to Rollback instructions")

If an update introduces a problem, you can roll back to a previous version:

```bash
cd /path/to/hermes-agent

# List recent versions
git log --oneline-10

# Roll back to a specific commit
git checkout <commit-hash>
git submodule update --init--recursive
uv pip install-e".[all]"

# Restart the gateway if running
hermes gateway restart
```

To roll back to a specific release tag:

```bash
git checkout v0.6.0
git submodule update --init--recursive
uv pip install-e".[all]"
```

warning

Rolling back may cause config incompatibilities if new options were added. Run `hermes config check` after rolling back and remove any unrecognized options from `config.yaml` if you encounter errors.

### Note for Nix users[​](#note-for-nix-users "Direct link to Note for Nix users")

If you installed via Nix flake, updates are managed through the Nix package manager:

```bash
# Update the flake input
nix flake update hermes-agent

# Or rebuild with the latest
nix profile upgrade hermes-agent
```

Nix installations are immutable — rollback is handled by Nix's generation system:

See [Nix Setup](https://hermes-agent.nousresearch.com/docs/getting-started/nix-setup) for more details.

* * *

## Uninstalling[​](#uninstalling "Direct link to Uninstalling")

The uninstaller gives you the option to keep your configuration files (`~/.hermes/`) for a future reinstall.

### Manual Uninstall[​](#manual-uninstall "Direct link to Manual Uninstall")

```bash
rm-f ~/.local/bin/hermes
rm-rf /path/to/hermes-agent
rm-rf ~/.hermes            # Optional — keep if you plan to reinstall
```

info

If you installed the gateway as a system service, stop and disable it first:

```bash
hermes gateway stop
# Linux: systemctl --user disable hermes-gateway
# macOS: launchctl remove ai.hermes.gateway
```