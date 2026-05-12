---
title: DMS 1.0 "The Dark Knight" Released | Dank Linux
url: https://danklinux.com/blog/v1-release
source: sitemap
fetched_at: 2026-04-26T08:35:04.060164744-03:00
rendered_js: false
word_count: 1609
summary: This document announces the 1.0 release of DankMaterialShell (DMS), a Wayland desktop shell, highlighting its new features such as customizable bars, integrated tools, and expanded package support across major Linux distributions.
tags:
    - wayland
    - desktop-shell
    - linux
    - quickshell
    - software-release
    - dms
category: other
optimized: true
optimized_at: 2026-04-26T00:00:00Z
---

# DMS 1.0 "The Dark Knight"

DankMaterialShell (DMS) is a Desktop Shell for Wayland Compositors built with [Quickshell](https://quickshell.org/) & Go. What started as a hobby project has grown into a full desktop shell with thousands of users and dozens of contributors, supporting [niri](https://github.com/niri-wm/niri), [Hyprland](https://hypr.land), [Sway](https://swaywm.org/), [MangoWC](https://mangowc.vercel.app/), and [LabWC](https://labwc.github.io/).

This release marks a commitment to stability and predictability. DMS follows a milestone/roadmap-based release cycle with bug-fix releases as needed between major versions.

## Statistics

- **2,300+** Commits
- **2.4k+** GitHub Stars
- **75+** Contributors
- **26** Community Plugins

## What's New

### OMEGA Bar

Add up to **4** bar configurations, each with their own widgets, layout, and style. Configure per-monitor and control each bar independently via [IPCs](https://danklinux.com/docs/dankmaterialshell/keybinds-ipc#bar).

![Omega Bars](https://danklinux.com/img/blog/v1/omegabar_light.png)![Omega Bars](https://danklinux.com/img/blog/v1/omegabar_dark.png)

### Comprehensive Keyboard Shortcuts (niri)

Configure global keyboard shortcuts on niri. Requires quickshell version from DankLinux repositories or quickshell-git from AUR.

![Keyboard Shortcuts](https://danklinux.com/img/blog/v1/keybinds_light.png)![Keyboard Shortcuts](https://danklinux.com/img/blog/v1/keybinds_dark.png)

### Printer Management (CUPS)

Manage printers directly from DMS Settings with CUPS integration. Add, remove, and configure printers. Control center widget shows printers and manages print jobs.

![Printer Management](https://danklinux.com/img/blog/v1/printers_light.png)![Printer Management](https://danklinux.com/img/blog/v1/printers_dark.png)

### Comprehensive Network Management

Network view with support for NetworkManager, IWD, and systemd-networkd. Import VPN profiles, manage connections, and connect to Wi-Fi networks.

![Network Management](https://danklinux.com/img/blog/v1/network_light.png)![Network Management](https://danklinux.com/img/blog/v1/network_dark.png)

### Polkit Agent

DMS includes its own Polkit agent for privilege escalation. No external polkit agents needed (`polkit-gnome`, `mate-polkit`, `kde-polkit`).

![Polkit Agent](https://danklinux.com/img/blog/v1/polkit_light.png)![Polkit Agent](https://danklinux.com/img/blog/v1/polkit_dark.png)

### File-Type Associations

Set default applications for file types and protocols from DMS Settings. See the [[044-docs-dankmaterialshell-overview#desktop-integration|desktop integration documentation]].

![App Picker](https://danklinux.com/img/blog/v1/apppicker_light.png)![App Picker](https://danklinux.com/img/blog/v1/apppicker_dark.png)

Special thanks to [@devnullvoid](https://github.com/devnullvoid) for this contribution.

### Dank Color Picker

Integrated color picker with eye dropper tool — no third-party tools needed. Available as standalone tool for Wayland compositors. See the [[067-docs-1.5-dankmaterialshell-cli-color-picker|CLI color picker documentation]].

![Color Picker](https://danklinux.com/img/blog/v1/colorpick_light.png)![Color Picker](https://danklinux.com/img/blog/v1/colorpick_dark.png)

### Dank Screenshot

Built-in screenshot tool — no `grim`, `slurp`, or `grimblast` needed. Capture region, single screen, all screens, or focused window (Hyprland/MangoWC/DWL only). Save to clipboard, file, stdout. Supports PNG, JPEG, and PPM formats. See the [[068-docs-1.5-dankmaterialshell-cli-screenshot|CLI screenshot documentation]].

![Screenshot Tool](https://danklinux.com/img/blog/v1/screenshot_light.png)![Screenshot Tool](https://danklinux.com/img/blog/v1/screenshot_dark.png)

### DMS Plugin System

26 community-created plugins extend DMS functionality. Explore the [full plugins directory](https://danklinux.com/plugins) for wallpaper engines, system monitors, media controls, container management, and more.

![DMS Plugin System](https://danklinux.com/img/blog/v1/dms_plugins.png)

Special thanks to [rochacbruno](https://github.com/rochacbruno) for developing the plugin system and maintaining the [plugin registry](https://github.com/AvengeMedia/dms-plugin-registry).

## Packages for Ubuntu, Debian, OpenSUSE, Fedora, CentOS, and Arch Linux

DMS is available through the [[041-docs-danklinux|DankLinux Repository]] with official packages:

| Package | Distributions |
|---------|---------------|
| niri | Ubuntu, Debian, OpenSUSE (includes xwayland-satellite) |
| quickshell | Ubuntu, Debian, OpenSUSE, Fedora |
| dgop | All supported distributions |
| dsearch | All supported distributions |
| dms-greeter | AUR, Fedora, Ubuntu |
| matugen | Ubuntu, Debian, OpenSUSE, Fedora |
| cliphist | All supported distributions |
| ghostty | Fedora, Debian, Ubuntu |

Development/nightly builds available via the same repositories.

### Available on nixpkgs

DMS is now on nixpkgs unstable. Check options on [search.nixos.org](https://search.nixos.org/options?channel=unstable&query=dms-).

Special thanks to [@LuckShiba](https://github.com/LuckShiba) for the nixpkgs package and [@marcusramberg](https://github.com/marcusramberg) for approving it.

## More than just a Shell

DMS is a comprehensive suite providing core desktop features cohesively or as standalone utilities:

- **DankMaterialShell (qml)** — The quickshell-based shell
- **DankMaterialShell (go)** — Backend service and tools
  - **Dank16** — Contrast-aware Base16 color palette generator
  - **Matugen** — Custom matugen runner with Dank16 integration
  - **Brightness** — CLI and socket service for backlight/LED/DDC/CI control
  - **Networking** — DBus integration with NetworkManager, IWD, systemd-networkd
  - **Keybinds** — Pluggable keybinds system for cheatsheets and management
  - **Color Picker** — CLI color picker with eye dropper for Wayland
  - **Screenshot** — Region selection, window capture, multiple output formats
  - **Plugins** — Plugin system for extending shell and launcher
- **dgop** — Stateless system monitoring with REST API
- **dsearch** — Fast indexed filesystem search server

> [!tip]
> DMS replaces: `brightnessctl`, `ddcutil`, `grimblast`, `nmcli`, `iwctl`, `grim`, `slurp`, `wofi`, `fuzzel`, `swayidle`, `hyprlock`, `mate/gnome/kde polkit`, `mako/dunst`, `hyprpicker`, `sddm`, and more.

## Bug Fixes and Improvements (300+ commits)

**Screenshot & Color Picker**
- Handle 24-bit frames from compositor and RGB888 bit flipping
- Color space and scaling fixes
- Handle transformed and multi-monitor displays
- Save button display fixes with eye dropper
- Fallback to niri picker when on niri

**Bar & Dock**
- Center section positioning and border thickness fixes
- Privacy indicator background color alignment
- Transparency handling improvements (>95% opacity, window-rules)
- Opacity binding and early-return fixes
- Maximize detection, scroll handling, and widget background options
- IPC reliability when screens change
- Auto-hide flickering and popout interaction fixes

**Display & Monitors**
- Workspace overview truncation and scaling (Hyprland)
- Physical vs. logical resolution display
- Icon vertical alignment in monitor widgets

**Audio & Media**
- Audio slider binding in control center
- Output device switching IPC and OSD
- Media control column positioning (bar awareness)
- Media OSD suppression on new players
- Player button control popup display

**Network & VPN**
- VPN icon consistency and lock screen status
- VPN password prompting fixes
- Binding loop fixes

**Keyboard & Input**
- Alt+Shift and KDL parsing for keybinds
- Keybind tab issues (niri)
- Capslock detection for devices without LED
- Window close on Esc prevention
- Context menu keyboard navigation

**Brightness & Gamma**
- Non-automation toggling fixes
- Night mode on startup
- DDC device erasure and OSD behavior
- Per-display pinned device IPCs
- Udev monitor integration for brightness events

**Settings & System**
- Weather setting (greeter)
- Mango config override (greeter)
- Launcher tab sizing
- Settings window scrollable areas
- Custom themes and font family handling

**Notifications & UI**
- Keyboard navigation in notification popout
- Button widget binding loops
- ProcessList context menu visibility
- Excessive repaints in modals
- DnD tooltip display

**Lock Screen & Power**
- VPN icon consistency
- Single-display lock screen option
- Hold-style confirmation for power actions
- Profile OSD and DBus activation

**Wallpaper & Themes**
- Per-monitor wallpaper display
- Wallpaper cycling
- Privacy widget background colors

**Build & Distribution**
- NixOS fprintd unlock, TUI startup crash, systemd service PATH
- DMS CLI versioning in all builds
- IPC argument handling
- OpenSUSE package directory and hash versioning
- Hyprland configuration syntax
- NixOS nativeBuildInputs

**Plugin System**
- Plugin reactivity and tooltip updates
- Plugin popout binding and reload IPCs

## Resources

[Get Started with DMS](https://danklinux.com/docs/getting-started)

Special thanks to [YaLTeR](https://github.com/YaLTeR) for collaborating with the DMS team, for [niri](https://github.com/niri-wm/niri), and for hosting DMS on the [niri Discord](https://discord.gg/ppWTpKmPgT).

#dms #wayland #desktop-shell #linux #quickshell #software-release
