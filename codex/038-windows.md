---
title: Windows
url: https://developers.openai.com/codex/windows.md
source: llms
fetched_at: 2026-04-30T10:16:11.641125973-03:00
rendered_js: false
word_count: 1193
summary: This document outlines the requirements, installation methods, and configuration options for running the Codex application on Windows, including native sandbox settings and WSL2 integration.
tags:
    - windows-installation
    - wsl2
    - sandbox-configuration
    - codex-setup
    - developer-environment
    - system-administration
category: guide
optimized: true
optimized_at: 2026-04-30T13:30:00Z
---
# Windows

Use Codex on Windows via the native [[011-app|Codex app]], [[015-cli|CLI]], or [[025-ide|IDE extension]]. Supports parallel agent threads, worktrees, automations, Git, in-app browser, artifact previews, plugins, and skills.

Three practical ways to run:
- Native Windows with `elevated` sandbox (preferred)
- Native Windows with `unelevated` sandbox (fallback)
- Inside [WSL2](https://learn.microsoft.com/en-us/windows/wsl/install) (Linux sandbox implementation)

## Windows sandbox

Blocks filesystem writes outside the working folder and prevents network access without explicit approval.

Configure in `config.toml`:
```toml
[windows]
sandbox = "elevated"  # or "unelevated"
```

| Mode | Description |
|------|-------------|
| **elevated** | Dedicated lower-privilege sandbox users, filesystem permission boundaries, firewall rules, local policy changes. Preferred. |
| **unelevated** | Restricted Windows token derived from current user, ACL-based filesystem boundaries, environment-level offline controls. Weaker but useful when admin-approved setup is blocked. |

If both are available, use `elevated`. If default doesn't work, use `unelevated` as fallback while troubleshooting.

Both modes use a private desktop for stronger UI isolation. Set `windows.sandbox_private_desktop = false` only if you need older `Winsta0\Default` behavior for compatibility.

### Sandbox permissions

> [!warning]
> Full access mode means Codex is not limited to your project directory and might perform unintentional destructive actions leading to data loss. For safer automation, keep sandbox boundaries and use [[061-rules|rules]] for targeted exceptions, or set approval policy to never so Codex attempts to solve problems without asking for escalated permissions. See [[041-agent-approvals-security|approval and security setup]].

### Windows version matrix

| Version | Support | Notes |
|---------|---------|-------|
| Windows 11 | Recommended | Best baseline for enterprise deployment |
| Recent, fully updated Windows 10 | Best effort | Requires modern console support (ConPTY). Version 1809+ required in practice. |
| Older Windows 10 builds | Not recommended | Likely missing ConPTY and more likely to fail in enterprise setups |

Additional assumptions:
- `winget` should be available. If missing, update Windows or install Windows Package Manager first.
- Recommended native sandbox depends on administrator-approved setup.
- Some enterprise-managed devices block required setup steps even on acceptable OS versions.

### Grant sandbox read access

When a command fails because the sandbox can't read a directory:
```text
/sandbox-add-read-dir C:\absolute\directory\path
```

Path must be an existing absolute directory. After success, later sandboxed commands can read that directory during the current session.

Use native Windows sandbox by default for best performance and speed. Choose WSL2 when you need a Linux-native environment, your workflow already lives in WSL2, or neither native sandbox mode meets your needs.

## Windows Subsystem for Linux (WSL2)

Codex runs inside the Linux environment instead of using the native Windows sandbox. Useful for Linux-native tooling, existing WSL2 workflows, or when native sandbox modes don't work.

WSL1 was supported through Codex `0.114`. Starting in `0.115`, the Linux sandbox moved to `bubblewrap`, so WSL1 is no longer supported.

### Launch VS Code from inside WSL

See [official VS Code WSL tutorial](https://code.visualstudio.com/docs/remote/wsl-tutorial).

Prerequisites:
- Windows with WSL installed (`wsl --install` in PowerShell as administrator; Ubuntu is common)
- VS Code with [WSL extension](https://marketplace.visualstudio.com/items?itemName=ms-vscode-remote.remote-wsl)

Open from WSL terminal:
```bash
cd ~/code/your-project
code .
```

Confirms connection:
- Green status bar shows `WSL: <distro>`
- Integrated terminals display Linux paths (`/home/...`)
- `echo $WSL_DISTRO_NAME` prints your distribution name

If no "WSL: ..." in status bar: press `Ctrl+Shift+P`, pick `WSL: Reopen Folder in WSL`, keep repository under `/home/...` (not `C:\`) for best performance.

If Windows app/project picker doesn't show WSL repository: type `\\wsl$` into file picker or Explorer, navigate to your distro's home directory.

### Use Codex CLI with WSL

From elevated PowerShell or Windows Terminal:
```powershell
# Install default Linux distribution
wsl --install

# Start a shell inside WSL
wsl
```

From WSL shell:
```bash
# Install Node.js via nvm
curl -o- https://raw.githubusercontent.com/nvm-sh/nvm/master/install.sh | bash
nvm install 22

# Install and run Codex
npm i -g @openai/codex
codex
```

### Working on code inside WSL

- Working in `/mnt/c/...` can be slower than Windows-native paths. Keep repositories under Linux home (`~/code/my-app`) for faster I/O and fewer symlink/permission issues.
- If you need Windows access to files, they're under `\\wsl$\Ubuntu\home\<user>` in Explorer.

## Troubleshooting and FAQ

### Native sandbox setup failed

Common causes for `elevated` sandbox setup failure:
- Windows UAC or administrator prompt declined
- Machine does not allow local user/group creation
- Machine does not allow firewall rule changes
- Machine blocks logon rights needed by sandbox users
- Enterprise policy blocks part of setup flow

What to try:
1. Try `elevated` setup again and approve administrator prompt if allowed.
2. If company laptop blocks this, ask IT whether machine allows administrator-approved setup for local user/group creation, firewall configuration, and sandbox-user logon rights.
3. If default setup still fails, use `unelevated` sandbox to continue working while issue is investigated.

### Codex switched to unelevated sandbox

Means Codex couldn't finish `elevated` sandbox setup.
- Codex still runs sandboxed with ACL-based filesystem boundaries.
- No separate sandbox-user boundary from `elevated`; weaker network isolation.
- Useful fallback, but not preferred long-term enterprise configuration.

Best long-term fix on managed enterprise laptop: get `elevated` sandbox working with IT help.

### Windows error 1385

Sandboxed commands fail with error `1385` = Windows denying the logon type the sandbox user needs.

Usually means Codex created sandbox users successfully, but Windows policy prevents them from launching sandboxed commands.

What to do:
1. Ask IT whether device policy grants required logon rights to Codex-created sandbox users.
2. Compare group policy or OU differences if issue affects only some machines/teams.
3. Use `unelevated` sandbox to keep working while policy issue is investigated.
4. Send `CODEX_HOME/.sandbox/sandbox.log` along with Windows version and failure description.

### Some folders writable by Everyone

Codex may warn that some folders are writable by `Everyone`.

1. Review folders listed in the warning.
2. Remove `Everyone` write access if appropriate.
3. Restart Codex or re-run sandbox setup after correcting permissions.

Ask IT team for help if unsure how to change permissions.

### Sandboxed commands cannot reach the network

Some tasks intentionally run without outbound network access depending on permissions mode.
1. Check whether task was supposed to run with network disabled.
2. If network access expected, restart Codex and try again.
3. If issue persists, collect sandbox log for review.

### Sandboxing worked before and then stopped

Can happen after:
- moving a repo or workspace
- changing machine permissions
- changing Windows policies
- other system configuration changes

What to try:
1. Restart Codex.
2. Try `elevated` sandbox setup again.
3. If that doesn't fix it, use `unelevated` sandbox as temporary fallback.
4. Collect sandbox log for review.

### Send diagnostics to OpenAI

Include:
- `CODEX_HOME/.sandbox/sandbox.log`
- Short description of what you were trying to do
- Whether `elevated` failed or `unelevated` was used
- Any error message shown in the app
- Whether you saw `1385` or another Windows/PowerShell error
- Whether you're on Windows 11 or Windows 10

Do not send:
- Contents of `CODEX_HOME/.sandbox-secrets/`

### IDE extension installed but unresponsive

System may be missing C++ development tools required by some native dependencies:
- Visual Studio Build Tools (C++ workload)
- Microsoft Visual C++ Redistributable (x64)
- With `winget`: `winget install --id Microsoft.VisualStudio.2022.BuildTools -e`

Fully restart VS Code after installation.

### Large repositories feel slow in WSL

- Make sure you're not working under `/mnt/c`. Move repository to WSL (`~/code/...`).
- Increase memory and CPU for WSL if needed; update WSL:
  ```powershell
  wsl --update
  wsl --shutdown
  ```

### VS Code in WSL cannot find codex

Verify binary exists and is on PATH inside WSL:
```bash
which codex || echo "codex not found"
```

If not found, install by following the [CLI with WSL instructions](#use-codex-cli-with-wsl) above.

#windows #sandbox #wsl #installation #troubleshooting