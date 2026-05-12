---
title: Installation and setup | Warp
url: https://docs.warp.dev/getting-started/installation-and-setup
source: sitemap
fetched_at: 2026-04-29T15:01:59.683457075-03:00
rendered_js: false
word_count: 288
summary: This document provides instructions for installing, building from source, and performing the initial configuration of the Warp terminal application.
tags:
    - terminal-emulator
    - software-installation
    - development-environment
    - shell-configuration
    - warp-terminal
category: guide
optimized: true
optimized_at: 2026-04-29T20:15:00Z
---
# Installation and Setup

Warp is available on macOS, Windows, and Linux (all architectures: x86_64 and ARM64).

## Install Warp

**Minimum requirements:** macOS 10.14+ (Intel or Apple silicon) with Metal support. Windows requires x86_64 or ARM64. Linux requires x86_64 or ARM64.

### Download

- Download Warp and drag into Applications folder.
- Install via Homebrew: `brew install warp-cli`

### Warp Preview

[Warp Preview](https://docs.warp.dev/support-and-community/community/warp-preview-and-alpha-program) provides early access to experimental features on all platforms.

## Build from Source

Warp's client is open source under [AGPL v3](https://github.com/warpdotdev/warp/blob/master/LICENSE).

```bash
git clone https://github.com/warpdotdev/warp.git
cd warp
cargo run
```

`cargo run` launches a `warp-oss` binary. See the repo's `README.md` and `CONTRIBUTING.md` for prerequisites (Xcode on macOS, pinned Rust toolchain, `protoc`).

> [!note]
> Self-built binaries use a separate config directory and don't auto-update. Use official builds for daily use.

## Initial Setup

### Log In (Optional)

Create an account via **Sign up** button (top right) or **Settings** > **Account** > **Sign up**. Skip if preferred. For login issues, see [Login Troubleshooting](https://docs.warp.dev/support-and-community/troubleshooting-and-support/troubleshooting-login-issues).

> [!note]
> Google/GitHub sign-in grants Warp email address access only. See [Privacy](https://docs.warp.dev/support-and-community/privacy-security-and-licensing/privacy) for details.

### Offline Use

Warp requires internet on first launch only. After that, it runs offline, though AI and real-time collaboration features require connectivity.

### Import Settings

For migration from other terminals/editors, see [[024-getting-started-migrate-to-warp]] for per-source guides including settings-import steps.

### Default Shell

Warp loads your login shell by default (bash, fish, zsh, or PowerShell). If your shell isn't supported (e.g., Nushell), Warp defaults to zsh.

| Shell | Default On |
|-------|------------|
| zsh | macOS (Catalina+, since 2019) |
| bash | Most Linux distributions |
| bash | Windows (via WSL) |
| PowerShell | Windows |

Change the default shell: **Settings** > **Features** > **Session** > **Startup shell for new sessions**.

#warp-terminal #software-installation #shell-configuration