# Dank Linux Documentation Index

> Organized index for AI agent consumption. Documents follow logical learning sequence.

## Metadata Summary

| Property | Value |
|----------|-------|
| **Source** | https://danklinux.com/sitemap.xml |
| **Generated** | 2026-01-24 |
| **Total Documents** | 57 |
| **Strategy** | sitemap |

---

## Document Index

### 1. Home & Introduction (001-002)
*Main landing pages and welcome documentation*

| # | File | Title | Summary | Keywords |
|---|------|-------|---------|----------|
| 001 | `001-homepage.md` | Modern Desktop Suite | DankMaterialShell introduction - customizable desktop shell for Wayland with Material Design 3 theming | linux-desktop, wayland, material-design, shell-environment |
| 002 | `002-docs.md` | Welcome | Dank Linux introduction and DankMaterialShell quick-start guide | dank-linux, dankmaterialshell, desktop-environment, wayland-shell |

### 2. Getting Started (003-005)
*Installation guides and repository setup*

| # | File | Title | Summary | Keywords |
|---|------|-------|---------|----------|
| 003 | `003-docs-getting-started.md` | Getting Started | Introductory guide for Dank Linux installation and configuration | dank-linux, linux-installation, system-setup |
| 004 | `004-docs-dankinstall.md` | DankInstall | Automated installer script for DankMaterialShell across Linux distributions | dank-material-shell, linux-installation, dotfiles-automation |
| 005 | `005-docs-danklinux.md` | DankLinux Repository | Pre-built packages for Fedora, CentOS, Debian, Ubuntu, OpenSUSE | linux-repository, package-management, installation-guide |

### 3. DankMaterialShell - Core (006-011)
*Overview, installation, and compositor setup*

| # | File | Title | Summary | Keywords |
|---|------|-------|---------|----------|
| 006 | `006-docs-dankmaterialshell-overview.md` | Overview & Architecture | DankMaterialShell architecture - Wayland shell built with Go and Quickshell | wayland-shell, quickshell, system-architecture, go-backend |
| 007 | `007-docs-dankmaterialshell-installation.md` | Installation | Install DankMaterialShell on Arch, Fedora, Debian, Ubuntu | dankmaterialshell, linux-installation, quickshell, package-management |
| 008 | `008-docs-dankmaterialshell-nixos.md` | NixOS Installation | Install DankMaterialShell on NixOS using native nixpkgs | nixos, dank-material-shell, nixpkgs, system-configuration |
| 009 | `009-docs-dankmaterialshell-nixos-flake.md` | NixOS Installation (Flake) | Install DankMaterialShell on NixOS using flakes and home-manager | nixos, home-manager, niri, flakes |
| 010 | `010-docs-dankmaterialshell-managing.md` | Managing Your Installation | Update, configure, and troubleshoot DankMaterialShell with systemd | dankmaterialshell, systemd, service-management, troubleshooting |
| 011 | `011-docs-dankmaterialshell-compositors.md` | Compositor Setup | Configure DMS with niri and Hyprland - keybindings, layer rules, startup | dankmaterialshell, wayland, niri, hyprland, compositor-configuration |

### 4. DankMaterialShell - Configuration (012-015)
*Advanced settings, layers, IPC, and integrations*

| # | File | Title | Summary | Keywords |
|---|------|-------|---------|----------|
| 012 | `012-docs-dankmaterialshell-advanced-configuration.md` | Advanced Configuration | Environment variables for DankMaterialShell configuration | dank-material-shell, environment-variables, wayland, display-layers |
| 013 | `013-docs-dankmaterialshell-layers.md` | Layer Namespaces | Configure blur effects and layer shell rules for Hyprland and Niri | wayland, layer-shell, hyprland, niri, blur-effects |
| 014 | `014-docs-dankmaterialshell-keybinds-ipc.md` | Keybinds & IPC | IPC interface reference for controlling system settings, media, and UI | dms, ipc-reference, shell-automation, command-line-interface |
| 015 | `015-docs-dankmaterialshell-calendar-integration.md` | Calendar Integration | Sync CalDAV calendars with vdirsyncer and khal | calendar-sync, caldav, vdirsyncer, khal, dashboard-integration |

### 5. DankMaterialShell - Theming (016-018)
*Custom themes, application theming, and icons*

| # | File | Title | Summary | Keywords |
|---|------|-------|---------|----------|
| 016 | `016-docs-dankmaterialshell-custom-themes.md` | Custom Themes | Create custom color themes using JSON and matugen | dankmaterialshell, theming, color-schemes, matugen, json-configuration |
| 017 | `017-docs-dankmaterialshell-application-themes.md` | Application Theming | Theme GTK, Qt, and terminal apps with Matugen | dank-material-shell, matugen, gtk, qt, terminal-theming |
| 018 | `018-docs-dankmaterialshell-icon-theming.md` | Icon Theming | Configure icon themes for Qt6 and GTK applications | qt6, icon-theming, dankmaterialshell, desktop-environments |

### 6. DankMaterialShell - CLI Tools (019-026)
*Command-line utilities for screenshots, clipboard, brightness, and more*

| # | File | Title | Summary | Keywords |
|---|------|-------|---------|----------|
| 019 | `019-docs-dankmaterialshell-cli-process-management.md` | Process Management | Manage DMS backend and Quickshell UI with run, restart, kill commands | dms-cli, process-management, systemd-integration |
| 020 | `020-docs-dankmaterialshell-cli-screenshot.md` | Screenshot | Capture screenshots on Wayland with multiple modes and formats | screenshot-tool, wayland, cli-utility, image-capture |
| 021 | `021-docs-dankmaterialshell-cli-clipboard.md` | Clipboard Manager | Wayland clipboard with history, search, and persistence | wayland, clipboard-manager, dms-cl, clipboard-history |
| 022 | `022-docs-dankmaterialshell-cli-brightness.md` | Brightness Control | Control backlight, LED, and DDC/I2C monitor brightness | dms-brightness, brightness-control, ddc-ci, monitor-settings |
| 023 | `023-docs-dankmaterialshell-cli-color-picker.md` | Color Picker | Pick colors from Wayland screen with multiple output formats | wayland, color-picker, cli-utility, color-formats |
| 024 | `024-docs-dankmaterialshell-cli-dank16.md` | Dank16 | Generate Base16 color palettes from a single hex color | color-palette, base16-spec, terminal-themes, color-generation |
| 025 | `025-docs-dankmaterialshell-cli-doctor.md` | System Diagnostics (doctor) | Diagnose DMS installation, dependencies, and configuration | dms-doctor, diagnostics, troubleshooting, dependency-verification |
| 026 | `026-docs-dankmaterialshell-cli-keybinds-cheatsheets.md` | Keybinds & Cheatsheets | Manage keybinds and cheatsheets for Hyprland, Sway, and more | keybind-management, keyboard-shortcuts, hyprland, sway |

### 7. DankMaterialShell - Plugins (027-028)
*Plugin system overview and development guide*

| # | File | Title | Summary | Keywords |
|---|------|-------|---------|----------|
| 027 | `027-docs-dankmaterialshell-plugins-overview.md` | Plugins Overview | Plugin types, installation methods, and configuration | dankmaterialshell, plugin-system, desktop-extension, qml |
| 028 | `028-docs-dankmaterialshell-plugin-development.md` | Plugin Development | Build plugins - environment setup, manifest, QML patterns | dank-material-shell, plugin-development, qml, widget-creation |

### 8. DankGreeter (029-033)
*greetd-compatible login manager*

| # | File | Title | Summary | Keywords |
|---|------|-------|---------|----------|
| 029 | `029-docs-dankgreeter.md` | DankGreeter | greetd-compatible login interface matching DMS aesthetic | greetd, greeter, dankmaterialshell, linux-login |
| 030 | `030-docs-dankgreeter-installation.md` | Installation | Install dms-greeter for greetd on various Linux distributions | linux-installation, greetd, dms-greeter, display-manager |
| 031 | `031-docs-dankgreeter-nixos.md` | NixOS Installation | Install DankGreeter on NixOS using native nixpkgs | nixos, dankgreeter, display-manager, nixpkgs-unstable |
| 032 | `032-docs-dankgreeter-nixos-flake.md` | NixOS Installation (Flake) | Install DankGreeter on NixOS using Flakes | nixos, nix-flakes, dankgreeter, login-manager |
| 033 | `033-docs-dankgreeter-configuration.md` | Configuration | Configure greeter themes, wallpapers, and sync with user settings | dms-greeter, theme-syncing, configuration-management |

### 9. DankSearch (034-039)
*Native file system search utility*

| # | File | Title | Summary | Keywords |
|---|------|-------|---------|----------|
| 034 | `034-docs-danksearch.md` | DankSearch | Native file search with CLI and REST API interfaces | file-search, cli, rest-api, indexing, danksearch |
| 035 | `035-docs-danksearch-installation.md` | Installation | Install dsearch on Arch, Fedora, NixOS, and from source | dsearch, installation-guide, linux, arch-linux, fedora |
| 036 | `036-docs-danksearch-nixos.md` | NixOS Installation | Install DankSearch on NixOS using nixpkgs module | nixos, danksearch, nixpkgs, systemd, configuration |
| 037 | `037-docs-danksearch-nixos-flake.md` | NixOS Installation (Flake) | Install DankSearch on NixOS with home-manager and flakes | nixos, home-manager, nix-flakes, danksearch, systemd |
| 038 | `038-docs-danksearch-configuration.md` | Configuration | Configure dsearch with TOML - index paths, performance, exclusions | danksearch, toml-configuration, file-indexing, indexing-rules |
| 039 | `039-docs-danksearch-usage.md` | Usage | Use dsearch CLI and HTTP API for file search with filters | dsearch, filesystem-search, cli-reference, api-usage, exif-metadata |

### 10. DGOP (040-043)
*System and process monitoring tool*

| # | File | Title | Summary | Keywords |
|---|------|-------|---------|----------|
| 040 | `040-docs-dgop.md` | DGOP | System monitoring with TUI, CLI, and REST API | system-monitoring, terminal-ui, process-management, rest-api |
| 041 | `041-docs-dgop-installation.md` | Installation | Install dgop on various Linux distributions | installation, dgop, system-monitoring, linux, go-lang |
| 042 | `042-docs-dgop-configuration.md` | Configuration | Configure UI themes, charts, and status indicators | ui-configuration, theme-settings, color-mapping, json-format |
| 043 | `043-docs-dgop-usage.md` | Usage | dgop CLI and API for system metrics and process management | dgop, system-monitoring, cli-reference, api-usage, openapi |

### 11. Contributing (044-046)
*Contribution guidelines and plugin registry*

| # | File | Title | Summary | Keywords |
|---|------|-------|---------|----------|
| 044 | `044-docs-contributing.md` | Contributing | General contribution guidelines and community conduct | contribution-guidelines, open-source, mit-license, bug-reporting |
| 045 | `045-docs-contributing-registry.md` | Contributing to Registry | Submit plugins and themes to DankMaterialShell registry | dankmaterialshell, plugin-contribution, theme-submission, json-schema |
| 046 | `046-plugins.md` | Plugins & Themes | Plugin directory for discovering DMS extensions | dankmaterialshell, plugin-management, extensibility, widgets |

### 12. Blog (047-055)
*Release announcements and project news*

| # | File | Title | Summary | Keywords |
|---|------|-------|---------|----------|
| 047 | `047-blog.md` | Dank Linux Blog | News, releases, and updates from the project | wayland, desktop-shell, quickshell, release-announcement |
| 048 | `048-blog-v1-release.md` | DMS 1.0 "The Dark Knight" | First major release of DankMaterialShell | dankmaterialshell, wayland-compositor, release-notes, quickshell |
| 049 | `049-blog-v1-2-release.md` | DMS 1.2 "Spicy Miso" | Desktop widgets, clipboard history, expanded configuration | dankmaterialshell, release-notes, wayland, plugin-system |
| 050 | `050-blog-desktop-widgets-1-2.md` | Desktop Widgets in DMS 1.2 | Tutorial on building custom widgets using the plugin system | dank-material-shell, desktop-widgets, plugin-development, qml |
| 051 | `051-blog-tags.md` | Tags | Blog tag listing | dank-linux, mit-license, open-source |
| 052 | `052-blog-tags-release.md` | Release Tags | Posts tagged with Release | dankmaterialshell, wayland, release-announcement |
| 053 | `053-blog-tags-announcement.md` | Announcement Tags | Posts tagged with Announcement | dank-material-shell, wayland, software-release |
| 054 | `054-blog-archive.md` | Archive | Blog post archive | copyright, mit-license, dank-linux |
| 055 | `055-blog-authors.md` | Authors | Blog authors listing | dank-linux, mit-license, copyright |

### 13. Support & Other (056-057)
*Help resources and utilities*

| # | File | Title | Summary | Keywords |
|---|------|-------|---------|----------|
| 056 | `056-docs-support.md` | Support | Community discussions on Discord and project support | dank-linux, dank-material-shell, community, discord |
| 057 | `057-search.md` | Search | Site search functionality | dank-linux, mit-license, open-source |

---

## Quick Reference

### By Topic
| Topic | File Range |
|-------|------------|
| **Installation** | 003-005, 007-009, 030-032, 035-037, 041 |
| **Configuration** | 012-015, 033, 038, 042 |
| **Theming** | 016-018 |
| **CLI Tools** | 019-026, 039, 043 |
| **Plugins** | 027-028, 045-046 |
| **NixOS** | 008-009, 031-032, 036-037 |

### By Component
| Component | Files |
|-----------|-------|
| **DankMaterialShell** | 006-028 |
| **DankGreeter** | 029-033 |
| **DankSearch** | 034-039 |
| **DGOP** | 040-043 |

---

## Learning Path

### Level 1: Foundation (Start Here)
- Read files **001-002** for introduction and overview
- Complete files **003-005** for getting started and installation options

### Level 2: Core Installation
- Install DankMaterialShell with files **006-011**
- Set up your compositor (niri/Hyprland) with file **011**

### Level 3: Configuration & Customization
- Configure advanced settings with files **012-015**
- Customize themes with files **016-018**

### Level 4: CLI Tools & Productivity
- Learn CLI utilities from files **019-026**
- Master keybinds and IPC with files **014, 026**

### Level 5: Extensions & Plugins
- Explore plugin system in files **027-028**
- Learn to contribute with files **044-046**

### Level 6: Additional Components
- Set up DankGreeter (login manager) with files **029-033**
- Install DankSearch (file search) with files **034-039**
- Install DGOP (system monitor) with files **040-043**

---

*This index is auto-generated and optimized for AI agent search. Files are numbered sequentially following a logical learning progression.*
