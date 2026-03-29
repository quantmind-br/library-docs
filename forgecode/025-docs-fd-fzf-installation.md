---
title: ForgeCode
url: https://forgecode.dev/docs/fd-fzf-installation/
source: sitemap
fetched_at: 2026-03-29T16:30:39.345217-03:00
rendered_js: false
word_count: 577
summary: This document provides platform-specific installation and configuration instructions for the dependencies required to enable ZSH Support features in ForgeCode.
tags:
    - zsh
    - installation-guide
    - shell-configuration
    - environment-setup
    - cli-tools
    - dependency-management
category: guide
---

This guide provides platform-specific installation instructions for the dependencies required by [ZSH Support](https://forgecode.dev/docs/zsh-support/):

- **zsh-syntax-highlighting** (required) - Provides syntax highlighting for ForgeCode prompts
- **fd** (optional) - Fast file finder for `@filename<Tab>` file tagging
- **fzf** (optional) - Fuzzy finder for interactive file and agent selection

Requirements Overview

- **zsh-syntax-highlighting**: Required for syntax highlighting feature
- **fd + fzf**: Optional but recommended for fuzzy file finding and agent selection
- Without these tools, you'll need to type full file paths manually and won't get syntax highlighting

[zsh-syntax-highlighting](https://github.com/zsh-users/zsh-syntax-highlighting) provides syntax highlighting for ForgeCode prompts and is **required** for the advertised syntax highlighting feature.

### Package Manager Installation (Recommended)[​](#package-manager-installation-recommended "Direct link to Package Manager Installation (Recommended)")

#### macOS[​](#macos "Direct link to macOS")

#### Ubuntu/Debian[​](#ubuntudebian "Direct link to Ubuntu/Debian")

#### Arch Linux[​](#arch-linux "Direct link to Arch Linux")

#### Fedora[​](#fedora "Direct link to Fedora")

#### Other Linux Distributions[​](#other-linux-distributions "Direct link to Other Linux Distributions")

Check the [official installation guide](https://github.com/zsh-users/zsh-syntax-highlighting/blob/master/INSTALL.md) for distribution-specific instructions.

### Oh My Zsh Installation[​](#oh-my-zsh-installation "Direct link to Oh My Zsh Installation")

If you use Oh My Zsh:

### Manual Installation[​](#manual-installation "Direct link to Manual Installation")

For manual installation without a package manager:

### Verify zsh-syntax-highlighting Installation[​](#verify-zsh-syntax-highlighting-installation "Direct link to Verify zsh-syntax-highlighting Installation")

If this returns a version number, the plugin is loaded correctly.

`fd` is a fast and user-friendly alternative to the traditional `find` command, used by ZSH Support to quickly locate files in your project.

### macOS[​](#macos-1 "Direct link to macOS")

### Ubuntu/Debian[​](#ubuntudebian-1 "Direct link to Ubuntu/Debian")

Ubuntu/Debian Note

On Ubuntu/Debian systems, the binary is installed as `fdfind` instead of `fd` due to a naming conflict. The ZSH integration handles this automatically.

### Arch Linux[​](#arch-linux-1 "Direct link to Arch Linux")

### Other Linux Distributions[​](#other-linux-distributions-1 "Direct link to Other Linux Distributions")

**Using cargo (if Rust is installed):**

**Manual installation from GitHub releases:**

1. Visit [fd releases page](https://github.com/sharkdp/fd/releases)
2. Download the appropriate binary for your system
3. Extract and place in your PATH

### Verify fd Installation[​](#verify-fd-installation "Direct link to Verify fd Installation")

`fzf` is a command-line fuzzy finder that provides the interactive file selection interface in ZSH Support.

### macOS[​](#macos-2 "Direct link to macOS")

### Ubuntu/Debian[​](#ubuntudebian-2 "Direct link to Ubuntu/Debian")

### Arch Linux[​](#arch-linux-2 "Direct link to Arch Linux")

### Other Linux Distributions[​](#other-linux-distributions-2 "Direct link to Other Linux Distributions")

**Manual installation using git:**

**Using package managers:**

- **CentOS/RHEL/Fedora**: `sudo dnf install fzf` or `sudo yum install fzf`
- **openSUSE**: `sudo zypper install fzf`

### Verify fzf Installation[​](#verify-fzf-installation "Direct link to Verify fzf Installation")

Critical Loading Order

The order in which you load these components in your `.zshrc` file is crucial:

1. **All other plugins** (git, auto-completion, etc.)
2. **ForgeCode integration**: `source <($FORGE_BIN extension zsh)`
3. **zsh-syntax-highlighting**: Must be **LAST**

**Example ~/.zshrc structure:**

### Command Not Found After Installation[​](#command-not-found-after-installation "Direct link to Command Not Found After Installation")

If `fd` or `fzf` commands are not found after installation:

1. **Check if they're in your PATH:**
2. **Restart your terminal** or reload your shell configuration:
3. **For Ubuntu/Debian fd issues:** The binary might be installed as `fdfind`. Create a symlink:

### Permission Issues[​](#permission-issues "Direct link to Permission Issues")

If you encounter permission errors during installation:

- **Avoid using `sudo` with `cargo install`** - this can create permission issues
- **Use a package manager instead** when available
- **For manual installations**, ensure the binary is placed in a directory you own (like `~/.local/bin`)

### Syntax Highlighting Not Working[​](#syntax-highlighting-not-working "Direct link to Syntax Highlighting Not Working")

If ForgeCode prompts don't show syntax highlighting:

1. **Verify zsh-syntax-highlighting is installed**:
2. **Check loading order** in `.zshrc` - ensure zsh-syntax-highlighting is loaded last
3. **Verify the source path** is correct for your installation method

### ZSH Support Still Not Working[​](#zsh-support-still-not-working "Direct link to ZSH Support Still Not Working")

After installing all dependencies, if ZSH Support features don't work:

1. **Verify all tools are installed:**
2. **Reload ZSH configuration:**
3. **Test the integration:**
4. **Check the [ZSH Support troubleshooting section](https://forgecode.dev/docs/zsh-support/#troubleshooting)** for additional help.

### macOS[​](#macos-3 "Direct link to macOS")

- Homebrew installation is the most reliable method
- Both tools integrate seamlessly with the system PATH

### Linux[​](#linux "Direct link to Linux")

- Most modern distributions include both tools in their repositories
- Ubuntu/Debian users should be aware of the `fdfind` vs `fd` naming

### Windows (WSL)[​](#windows-wsl "Direct link to Windows (WSL)")

- Use the Linux installation methods within WSL
- Ensure your WSL distribution is up to date before installing

If the standard installation methods don't work for your system:

### Using Nix[​](#using-nix "Direct link to Using Nix")

### Using Snap (Ubuntu)[​](#using-snap-ubuntu "Direct link to Using Snap (Ubuntu)")

### Building from Source[​](#building-from-source "Direct link to Building from Source")

Both tools are written in Rust and can be built from source:

**fd:**

**fzf:**

**zsh-syntax-highlighting:**

- [zsh-syntax-highlighting Repository](https://github.com/zsh-users/zsh-syntax-highlighting)
- [zsh-syntax-highlighting Installation Guide](https://github.com/zsh-users/zsh-syntax-highlighting/blob/master/INSTALL.md)
- [fd Repository](https://github.com/sharkdp/fd)
- [fzf Repository](https://github.com/junegunn/fzf)
- [ZSH Support Documentation](https://forgecode.dev/docs/zsh-support/)