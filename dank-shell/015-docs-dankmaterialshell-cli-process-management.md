---
title: Process Management | Dank Linux
url: https://danklinux.com/docs/dankmaterialshell/cli-process-management
source: sitemap
fetched_at: 2026-04-26T08:38:49.572366455-03:00
rendered_js: false
word_count: 836
summary: This document explains the dms command-line interface used for managing DankMaterialShell backend processes, Quickshell UI instances, and their associated inter-process communication.
tags:
    - process-management
    - shell-configuration
    - wayland
    - ipc
    - systemd
    - cli-tools
category: guide
optimized: true
optimized_at: 2026-04-26T00:00:00Z
---

Version: 1.4

`dms` provides process management for running, restarting, and killing DankMaterialShell instances. The DMS backend server spawns and manages the Quickshell UI process as a child, configuring IPC communication between them.

## Overview

DankMaterialShell consists of:

- Launching the DMS backend server
- Spawning Quickshell as a child process with DMS configuration
- Configuring IPC communication between backend and frontend
- Restarting both processes to apply configuration changes
- Managing daemon and session modes

## Commands

### `dms run`

Launch DankMaterialShell by starting the backend server and Quickshell UI process, then establishing IPC communication via Unix socket.

| Flag | Description |
|------|-------------|
| `-d, --daemon` | Run in daemon mode (detached from terminal) |
| `--session` | Session managed mode (for use with systemd or other session managers) |
| `-h, --help` | Show help |

**Examples:**

```bash
# Run DMS normally (attached to terminal)
dms run
# Run DMS in daemon mode (detached)
dms run --daemon
# Run DMS as a session-managed process
dms run --session
```

**When to use each mode:**

- **Normal mode**: For testing, debugging, or manual shell management
- **Daemon mode**: For background operation without terminal attachment
- **Session mode**: When managing DMS via systemd user units or similar session managers

### `dms restart`

Kill the DMS backend server (along with its Quickshell child process) and relaunch them. Use after making configuration changes to reload the shell.

**What it does:**

1. Terminates the DMS backend server (which also kills its Quickshell child process)
2. Cleans up any orphaned Quickshell processes if needed
3. Relaunches the backend, which spawns a fresh Quickshell instance
4. Re-establishes IPC communication

**Use cases:**

- After modifying DMS configuration files
- After updating themes or plugins
- When the shell becomes unresponsive
- After applying compositor changes that affect DMS

### `dms kill`

Kill the DMS backend server (which automatically terminates its Quickshell child process) without restarting.

**Examples:**

```bash
# Kill all DMS instances
dms kill
```

**Use cases:**

- Stopping DMS before logging out
- Cleaning up stuck processes
- Switching to a different desktop environment
- Troubleshooting process issues

## Running DMS at Login

> [!tip]
> If you used [[034-docs-1.2-dankinstall|DankInstall]], DMS is already configured as a systemd service and starts automatically.

### Systemd User Service (Recommended)

Systemd provides automatic startup, session integration, and logging via journalctl. This is the default for dankinstall setups.

```bash
# Enable and start
systemctl --user enable --now dms
# Check status
systemctl --user status dms
# View logs
journalctl --user -u dms -f
```

> [!warning]
> If using systemd, don't add `dms run` to your compositor config -- you'll end up with two instances.

### Manual Launch

Add to your compositor's autostart configuration:

**Hyprland** (`~/.config/hypr/hyprland.conf`):

```conf
exec-once = dms run
```

**Sway** (`~/.config/sway/config`):

```conf
exec dms run
```

**Niri** (`~/.config/niri/config.kdl`):

```kdl
spawn-at-startup "dms" "run"
```

### Custom Systemd Unit (Advanced)

For a custom unit (e.g., for a source build without `make install`), create `~/.config/systemd/user/dms.service`:

```ini
[Unit]
Description=Dank Material Shell (DMS)
PartOf=graphical-session.target
After=graphical-session.target
Requisite=graphical-session.target
[Service]
Type=simple
ExecStart=/usr/bin/dms run --session
Restart=always
RestartSec=2
TimeoutStopSec=10
[Install]
WantedBy=graphical-session.target
```

Then reload and enable:

```bash
systemctl --user daemon-reload
systemctl --user enable --now dms
```

## Process Architecture

DMS operates as a multi-process system:

1. **DMS Backend Server** (Go): Handles IPC requests, plugin management, system monitoring, and CLI operations
2. **Quickshell UI Process**: Qt/QML runtime that renders the shell interface (spawned as a child of the backend)
3. **IPC Layer**: Unix socket communication between backend and frontend
4. **Plugins**: Optional processes that extend functionality

**Process hierarchy:**

```text
compositor (hyprland/sway/niri/etc)
└── dms backend server
    ├── IPC server (Unix socket)
    ├── Plugin manager
    └── quickshell (child process)
        └── Connects to parent via IPC
```

## Troubleshooting

### DMS Won't Start

- Check if Quickshell is installed
- Check for conflicting processes
- Try running without daemon mode to see errors

### Multiple Instances Running

```bash
dms kill
sleep 1
dms run --daemon
```

### Configuration Not Reloading

Use `dms restart` instead of manually killing processes.

### Systemd Service Fails

```bash
journalctl --user -u dms.service -n 50
# Verify the service file has correct paths
systemctl --user cat dms.service
```

## Integration with Compositor

DMS is designed to work with Wayland compositors:

- **Hyprland**: Use `exec-once` for autostart
- **Sway**: Use `exec` for autostart
- **Niri**: Use `spawn-at-startup` for autostart
- **MangoWC**: Use compositor-specific autostart mechanism

When the compositor exits, the DMS backend automatically terminates along with its Quickshell child process. If processes don't clean up properly, run `dms kill` before logging out.

## Command Reference

**Process Management Commands:**

| Command | Description |
|---------|-------------|
| `run [flags]` | Launch Quickshell with DMS configuration |
| `restart` | Kill and relaunch DMS |
| `kill` | Kill all running DMS instances |

**Global Flags:**

| Flag | Description |
|------|-------------|
| `-c, --config <path>` | Specify custom DMS config directory |
| `-h, --help` | Show help |

**Run Command Flags:**

| Flag | Description |
|------|-------------|
| `-d, --daemon` | Run in daemon mode |
| `--session` | Session managed mode |

## Other CLI Commands

`dms` also provides:

- **IPC**: `dms ipc` - Send commands to running DMS instances (see [[075-docs-1.2-dankmaterialshell-keybinds-ipc|Keybinds & IPC]])
- **Keybinds**: `dms keybinds` - Manage keybind cheatsheets (see [[014-docs-dankmaterialshell-cli-keybinds-cheatsheets|Keybinds & Cheatsheets]])
- **Brightness**: `dms brightness` - Control device brightness (see [[079-docs-dankmaterialshell-cli-brightness|Brightness Control]])
- **Dank16**: `dms dank16` - Generate color palettes (see [[013-docs-dankmaterialshell-cli-dank16|Dank16]])
- **Plugins**: `dms plugins` - Manage DMS plugins (see [[004-docs-dankmaterialshell-plugins-overview|Plugins Overview]])
- **Update**: `dms update` - Update DankMaterialShell
- **Version**: `dms version` - Show version information

Run `dms --help` for a complete list of available commands.
