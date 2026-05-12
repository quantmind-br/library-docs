---
title: Supported shells | Warp
url: https://docs.warp.dev/getting-started/supported-shells
source: sitemap
fetched_at: 2026-04-29T15:02:09.873318651-03:00
rendered_js: false
word_count: 405
summary: This document explains how to configure and customize different shell environments within the Warp terminal, including bash, zsh, fish, and PowerShell.
tags:
    - warp-terminal
    - shell-configuration
    - zsh
    - bash
    - fish-shell
    - powershell
    - environment-variables
category: guide
optimized: true
optimized_at: 2026-04-29T18:00:00Z
---
Warp loads your login shell by default. Supported shells: bash, fish, zsh, PowerShell (pwsh). For other shells, Warp shows a banner and falls back to platform defaults.

| Platform | Default Shell |
|----------|---------------|
| macOS | zsh |
| Windows | PowerShell (pwsh) |
| Linux | bash |

## Changing the default shell

Set the startup shell for new sessions in **Settings** → **Features** → **Session** → **Startup shell for new sessions**. Changes apply to new sessions only.

## Customizing shell environments

### zsh

Configuration: `~/.zshrc` — runs on every new session. Use for environment variables, aliases, and [prompt customization](https://docs.warp.dev/terminal/appearance/prompt).

Edit: `nano ~/.zshrc` or `vi ~/.zshrc`
Reload: `source ~/.zshrc`

> [!info]
> Hidden files (starting with `.`) require "Show hidden files" enabled in your file explorer.

### Bash

Configuration: `~/.bashrc` (non-login) or `~/.bash_profile` (login). Use for environment variables, aliases, and [prompt customization](https://docs.warp.dev/terminal/appearance/prompt).

Edit: `nano ~/.bashrc` or `vi ~/.bashrc`
Reload: `source ~/.bashrc`

> [!info]
> Hidden files (starting with `.`) require "Show hidden files" enabled in your file explorer.

### Fish

Configuration: `~/.config/fish/config.fish`

> [!info]
> Fish does not use `export VAR=value`. Use `set -Ux VAR value` for persistent variables.

Edit: `nano ~/.config/fish/config.fish`
Reload: `source ~/.config/fish/config.fish`

### PowerShell

Configuration: `$PROFILE`. Create with `New-Item -Path $PROFILE -ItemType File -Force` if missing.

Edit: `code $PROFILE`
Reload: restart Warp or open new session

> [!warning]
> PowerShell's execution policy may block scripts. Enable with:
> ```powershell
> Set-ExecutionPolicy RemoteSigned -Scope CurrentUser
> ```

## macOS-specific guidance

### Setting up zsh

macOS ships with zsh at `/bin/zsh`. Confirm with `which zsh` or `zsh --version`.

### Installing Fish

Fish is not pre-installed on macOS. Install via Homebrew: `brew install fish`

#### Switching to Fish

**Option 1 (Warp only):** Set in **Settings** → **Features** → **Session**

**Option 2 (Account default):**
```bash
# Add to /etc/shells
echo /opt/homebrew/bin/fish | sudo tee -a /etc/shells  # Apple Silicon
echo /usr/local/bin/fish | sudo tee -a /etc/shells      # Intel

# Set default shell
chsh -s /opt/homebrew/bin/fish
```

> [!info]
> Homebrew installs to `/opt/homebrew` on Apple Silicon, `/usr/local` on Intel. Find fish with `which fish`.

### Installing PowerShell

PowerShell is not pre-installed on macOS. Install via Homebrew: `brew install powershell/tap/powershell`

#### Switching to pwsh

**Option 1 (Warp only):** Set in **Settings** → **Features** → **Session**

**Option 2 (Account default):**
```bash
# Add to /etc/shells
echo /opt/homebrew/bin/pwsh | sudo tee -a /etc/shells  # Apple Silicon
echo /usr/local/bin/pwsh | sudo tee -a /etc/shells      # Intel

# Set default shell
chsh -s /opt/homebrew/bin/pwsh
```

> [!info]
> Homebrew installs to `/opt/homebrew` on Apple Silicon, `/usr/local` on Intel. Find pwsh with `which pwsh`.

## Windows shells

Warp's default: PowerShell 7 (pwsh). Supported:

- PowerShell 7 (default)
- PowerShell 5
- Windows Subsystem for Linux (WSL2)
- Git Bash

> [!warning]
> Windows Command Prompt (cmd.exe) is not supported. See [GitHub issue](https://github.com/warpdotdev/Warp/issues/5882) for updates.