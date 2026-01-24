---
title: DMS 1.0 "The Dark Knight" Released
url: https://danklinux.com/blog/v1-release
source: sitemap
fetched_at: 2026-01-24T13:32:48.624195577-03:00
rendered_js: false
word_count: 1555
summary: This document announces the official 1.0 release of DankMaterialShell (DMS), a Go-based desktop shell for Wayland compositors. It details major architectural updates and new features such as multi-bar support, built-in system utilities, and a community plugin system.
tags:
    - wayland
    - desktop-shell
    - release-announcement
    - linux-desktop
    - quickshell
    - software-development
category: other
---

We're excited to announce DankMaterialShell (DMS) 1.0! ~ DMS is a Desktop Shell for Wayland Compositors built with [Quickshell](https://quickshell.org/) & GO.

What started as a small hobby project has grown into a full desktop shell and application suite with thousands of users and dozens of contributors - with first class support for [niri](https://github.com/YaLTeR/niri), [Hyprland](https://hypr.land), [Sway](https://swaywm.org), [MangoWC](https://mangowc.vercel.app/), and [LabWC](https://labwc.github.io/). As well as general support for all compositors implementing select wayland protocols.

This release marks more than just a version number, it's a commitment to stability and predictability. Going forward, DMS will follow a milestone/roadmap-based release cycle, with bug-fix releases as needed in-between major versions.

DMS has come a long way since its inception, and we're excited to pivot towards a more structured development process - which represents a step towards making DMS a mainstream Linux desktop project.

2,300+Commits

2.4k+GitHub Stars

75+Contributors

26Community Plugins

## What's New[​](#whats-new "Direct link to What's New")

### OMEGA Bar[​](#omega-bar "Direct link to OMEGA Bar")

Add up to **4** bar configurations, each with their own set of widgets, layout, and style. Configure which monitor each bar appears on and independently control each bar with new [IPCs](https://danklinux.com/docs/dankmaterialshell/keybinds-ipc#bar).

![Omega Bars](https://danklinux.com/img/blog/v1/omegabar_light.png)![Omega Bars](https://danklinux.com/img/blog/v1/omegabar_dark.png)

Multiple bar configurations with independent widgets and styles

### Comprehensive Keyboard Shortcuts (niri)[​](#comprehensive-keyboard-shortcuts-niri "Direct link to Comprehensive Keyboard Shortcuts (niri)")

Configure global keyboard shortcuts - available to niri users. Requires quickshell version from DankLinux repositories or quickshell-git from AUR.

![Keyboard Shortcuts](https://danklinux.com/img/blog/v1/keybinds_light.png)![Keyboard Shortcuts](https://danklinux.com/img/blog/v1/keybinds_dark.png)

Keyboard shortcuts configuration with conflict detection

### Printer Management (CUPS)[​](#printer-management-cups "Direct link to Printer Management (CUPS)")

Manage printers directly from DMS Settings with CUPS integration. Add, remove, and configure printers with ease. A new control center widget allows viewing printers and managing print jobs.

![Printer Management](https://danklinux.com/img/blog/v1/printers_light.png)![Printer Management](https://danklinux.com/img/blog/v1/printers_dark.png)

CUPS printer management with status monitoring and job control

### Comprehensive Network Management[​](#comprehensive-network-management "Direct link to Comprehensive Network Management")

Comprehensive network view with support for NetworkManager, IWD, and systemd-networkd. Import VPN profiles, manage connections, and connect to Wi-Fi networks.

![Network Management](https://danklinux.com/img/blog/v1/network_light.png)![Network Management](https://danklinux.com/img/blog/v1/network_dark.png)

Network settings with WiFi and VPN management

### Polkit Agent[​](#polkit-agent "Direct link to Polkit Agent")

DMS now includes its own Polkit agent for handling privilege escalation requests. No more need for external polkit agents like `polkit-gnome`, `mate-polkit`, or `kde-polkit`.

![Polkit Agent](https://danklinux.com/img/blog/v1/polkit_light.png)![Polkit Agent](https://danklinux.com/img/blog/v1/polkit_dark.png)

Native polkit authentication dialog for privilege escalation

### File-Type Associations[​](#file-type-associations "Direct link to File-Type Associations")

Set default applications for different file types and protocols directly from DMS Settings. Easily manage which apps open specific file formats and choose your preferred applications for handling various file types and links. See the [desktop integration documentation](https://danklinux.com/docs/dankmaterialshell/overview#desktop-integration).

![App Picker](https://danklinux.com/img/blog/v1/apppicker_light.png)![App Picker](https://danklinux.com/img/blog/v1/apppicker_dark.png)

Open with dialog for selecting default applications

Special thanks to [@devnullvoid](https://github.com/devnullvoid) for the contribution.

### Dank Color Picker[​](#dank-color-picker "Direct link to Dank Color Picker")

The color picker is not new, but the eye dropper/color picker tool is now built-in to DMS - no more need for third-party tools! It is now integrated into DMS and available as a standalone tool for Wayland compositors. See the [CLI color picker documentation](https://danklinux.com/docs/dankmaterialshell/cli-color-picker).

![Color Picker](https://danklinux.com/img/blog/v1/colorpick_light.png)![Color Picker](https://danklinux.com/img/blog/v1/colorpick_dark.png)

Pick colors from anywhere on your screen with multiple output formats

### Dank Screenshot[​](#dank-screenshot "Direct link to Dank Screenshot")

DMS now ships with its own screenshot tool - no need for grim, slurp, or grimblast anymore. Capture a region, a single screen, all screens, or currently focused window (Hyprland/MangoWC/DWL only). Save to clipboard, file, stdout, or mix and match. Get notified when it's done. Supports PNG, JPEG, and PPM formats. See the [CLI screenshot documentation](https://danklinux.com/docs/dankmaterialshell/cli-screenshot).

Compatible with many Wayland compositors including Hyprland, Sway, MangoWC, and niri.

![Screenshot Tool](https://danklinux.com/img/blog/v1/screenshot_light.png)![Screenshot Tool](https://danklinux.com/img/blog/v1/screenshot_dark.png)

Region selection with live dimensions across multiple monitors

### DMS Plugin System[​](#dms-plugin-system "Direct link to DMS Plugin System")

DMS features a powerful plugin system that allows developers and enthusiasts to extend the shell with custom functionality. The plugin ecosystem now includes 26 community-created plugins, with 6 new additions since the v0.6.2 release. From system utilities to creative tools, the plugin system makes it possible to add custom widgets, integrate with external services, or build entirely new features on top of DMS.

Explore the [full plugins directory](https://danklinux.com/plugins) to discover community contributions including wallpaper engines, system monitors, media controls, container management, and more. New plugins are being added regularly as the community continues to build amazing extensions.

![DMS Plugin System](https://danklinux.com/img/blog/v1/dms_plugins.png)

26 community plugins extending DMS functionality

Special thanks to [rochacbruno](https://github.com/rochacbruno) for developing and iterating on the plugin system, as well as maintaining the [plugin registry](https://github.com/AvengeMedia/dms-plugin-registry).

## Packages for Ubuntu, Debian, OpenSUSE, Fedora, CentOS, and Arch Linux[​](#packages-for-ubuntu-debian-opensuse-fedora-centos-and-arch-linux "Direct link to Packages for Ubuntu, Debian, OpenSUSE, Fedora, CentOS, and Arch Linux")

DMS is now available through the [DankLinux Repository](https://danklinux.com/docs/danklinux) with official packages for Ubuntu, Debian, OpenSUSE, and Fedora/CentOS via PPA, OBS, and COPR. Arch Linux users can grab it from the Arch User Repository (AUR).

This includes not only DMS itself but also core dependencies that may be used with or without DMS including:

- **niri** - Ubuntu, Debian, and OpenSUSE (includes **xwayland-satellite**)
- **quickshell** - Ubuntu, Debian, OpenSUSE, and Fedora
- **dgop** - All supported distributions
- **dsearch** - All supported distributions
- **dms-greeter** - AUR, Fedora, and Ubuntu (more via DankInstaller)
- **matugen** - Ubuntu, Debian, OpenSUSE, and Fedora
- **cliphist** - All supported distributions
- **ghostty** - Fedora, Debian and Ubuntu

*Development packages/nightly builds are also available via the same repositories*

### Available on nixpkgs[​](#available-on-nixpkgs "Direct link to Available on nixpkgs")

[![Packaged for Nixpkgs](https://danklinux.com/img/distros/nixpkgs-light.svg)![Packaged for Nixpkgs](https://danklinux.com/img/distros/nixpkgs-dark.svg)](https://search.nixos.org/options?channel=unstable&query=dms-)

DMS is now available on nixpkgs unstable. This simplifies installation significantly for NixOS users and those using Nix package manager and represents a major step towards broader adoption. Check the available options on [search.nixos.org](https://search.nixos.org/options?channel=unstable&query=dms-).

Special thanks to [@LuckShiba](https://github.com/LuckShiba) for creating the nixpkgs package and [@marcusramberg](https://github.com/marcusramberg) for approving!

## More than just a Shell[​](#more-than-just-a-shell "Direct link to More than just a Shell")

DMS has become more than just a desktop shell. It is a comprehensive suite of tools that provide core desktop features in a cohesive, integrated way - or as completely standalone utilities to enrich non-DMS desktops.

- **DankMaterialShell (qml)** - The quickshell-based part of the shell
- **DankMaterialShell (go)** - A comprehensive backend service and suite of tools
  
  - **Dank16** - A contrast-aware color palette generator for Base16-style themes
  - **Matugen** - A custom matugen runner that enriches matugen templates with Dank16 and custom colors
  - **Brightness** - A complete management CLI and socket service for backlight, LED, and ddc/ci brightness control.
  - **Networking** - Native dbus integration with NetworkManager, IWD, and systemd-networkd for comprehensive network management - including VPNs, WiFi, and Ethernet.
  - **Keybinds** - A complete keybinds system with pluggable providers for reading and writing keybinds for cheatsheets and management interfaces.
  - **Color Picker** - A CLI color picker with multiple output formats and an eye dropper tool for Wayland.
  - **Screenshot** - A complete screenshot tool with region selection, window capture, and multiple output formats.
  - **Plugins** - A plugin system for extending the shell and launcher with custom functionality.
- **dgop** - A stateless system monitoring tool with a unique cursor-based approach. CLI and fully documented (With OpenAPI 3.1) REST API.
- **dsearch** - A blazingly fast, indexed filesystem search server with incremental indexes. Fully configurable - choose depth, folders, exclusions, metadata, content, and more. CLI, Unix Socket, and Rest API.

**TL;DR** *DMS* replaces many tools commonly used for Wayland desktops. No `brightnessctl`, `ddcutil`, `grimblast`, `nmcli`, `iwctl`, `grim`, `slurp`, `wofi`, `fuzzel`, `swayidle`, `hyprlock`, `mate/gnome/kde polkit`, `mako/dunst`, `hyprpicker`, `sddm`, or (a bunch of other stuff) needed anymore. Fully optional, and completely standalone from DMS itself.

## Bug Fixes and Improvements[​](#bug-fixes-and-improvements "Direct link to Bug Fixes and Improvements")

|- View Details (300+ commits) -|

Since the last v0.6.2 release, DMS has received extensive bug fixes and stability improvements across all components:

**Screenshot & Color Picker**

- Handle 24-bit frames from compositor and RGB888 bit flipping
- Color space and scaling fixes
- Handle transformed and multi-monitor displays
- Save button display fixes with eye dropper
- Fallback to niri picker when on niri

**Bar & Dock**

- Center section positioning and border thickness fixes
- Privacy indicator background color alignment
- Transparency handling improvements (&gt;95% opacity, window-rules)
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

- NixOS fprintd unlock, TUI startup crash, and systemd service PATH
- DMS CLI versioning in all builds
- IPC argument handling
- OpenSUSE package directory and hash versioning
- Hyprland configuration syntax
- NixOS nativeBuildInputs

**Plugin System**

- Plugin reactivity and tooltip updates
- Plugin popout binding and reload IPCs

And many more targeted fixes across the entire codebase to ensure stability and reliability across all supported compositors (Hyprland, Sway, niri, MangoWC, LabWC, and DWL).

## Resources[​](#resources "Direct link to Resources")

[Get Started with DMS →](https://danklinux.com/docs/getting-started)

![niri](https://danklinux.com/img/niri.svg)Special thanks to [YaLTeR](https://github.com/YaLTeR) for collaborating with the DMS team, for [niri](https://github.com/YaLTeR/niri) - the compositor that inspired DMS, and for hosting DMS on the [niri Discord](https://discord.gg/ppWTpKmPgT).

## Thank You

To everyone who has supported DMS through feedback, contributions, sponsorships, donations, and packaging.

Here's to many more releases ahead!