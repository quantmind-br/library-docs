---
title: Remote connections
url: https://developers.openai.com/codex/remote-connections.md
source: llms
fetched_at: 2026-04-30T10:16:00.518199065-03:00
rendered_js: false
word_count: 261
summary: This document outlines how to enable and configure SSH-based remote connections in the Codex application to access projects hosted on external machines.
tags:
    - ssh
    - remote-access
    - codex-app
    - configuration
    - feature-flag
    - security
category: configuration
optimized: true
optimized_at: 2026-04-30T13:30:00Z
---
# Remote connections

> [!warning]
> **Alpha feature.** Set `remote_connections = true` in the `[features]` table in `~/.codex/config.toml` to enable. Availability, setup flows, and supported environments may change.

Work with projects on another SSH-accessible machine. Use when the codebase, credentials, services, or build environment you need are on that host.

Keep the remote host configured with the same security expectations as normal SSH access: trusted keys, least-privilege accounts, no unauthenticated public listeners.

## Codex app setup

1. **Add the host to your SSH config** so Codex can auto-discover it:
   ```text
   Host devbox
     HostName devbox.example.com
     User you
     IdentityFile ~/.ssh/id_ed25519
   ```
   Codex reads concrete host aliases from `~/.ssh/config`, resolves them with OpenSSH, and ignores pattern-only hosts.
2. **Confirm SSH access** from the machine running Codex:
   ```bash
   ssh devbox
   ```
3. **Install and authenticate Codex on the remote host.** The app starts the remote Codex app server through SSH using the remote user's login shell. Ensure `codex` is on the remote `PATH` in that shell.
4. **In the Codex app**, open **Settings > Connections**, add or enable the SSH host, then choose a remote project folder.

If remote connections don't appear, enable the feature flag:
```toml
[features]
remote_connections = true
```

Remote project threads run commands, read files, and write changes on the remote host.

## Authentication and network exposure

Use SSH port forwarding with local-host WebSocket listeners. Don't expose an unauthenticated app-server listener on a shared or public network.

For remote machines outside your current network, use a VPN or mesh networking tool such as Tailscale instead of exposing the app server directly to the internet.

## See also

- [[051-app-settings|Codex app settings]]
- [[066-cli-reference|Command line options]]
- [[012-auth|Authentication]]

#ssh #remote #codex #alpha