---
description: Auto-generated documentation index
generated: 2026-04-26T13:37:55Z
source: https://wiki.hypr.land/sitemap.xml
total_docs: 90
categories: 8
optimized: true
optimized_at: 2026-04-26T13:37:55Z
format: obsidian
---

# wiki.hypr.land Documentation Index

> Organized for AI agent consumption. Files numbered following a logical learning sequence.

## Summary

| Property | Value |
|----------|-------|
| Source | https://wiki.hypr.land/sitemap.xml |
| Generated | 2026-04-26T13:37:55Z |
| Total Documents | 90 |
| Categories | Quick Start & Installation, Tutorials & Guides, Concepts & Fundamentals, Configuration, API Reference, Troubleshooting, Changelog & Releases, Meta & Resources |

---

## Document Index

### 1. Quick Start & Installation (001–005)
*Installation, setup, and first steps*

| # | File | Title | Summary | Tags |
|---|---|---|---|---|
| 001 | `001-getting-started-installation.md` | Installation | This document provides comprehensive instructions on how to install and build the Hyprland window manager across variou… | hyprland, linux-installation, wayland-compositor, window-manager, build-instructions, distro-compatibility |
| 002 | `002-getting-started-master-tutorial.md` | Master tutorial | This document serves as an introductory guide for new users to set up, launch, and configure the Hyprland tiling window… | hyprland, wayland, linux-desktop, window-manager, installation-guide, system-configuration |
| 003 | `003-getting-started-preconfigured-setups.md` | Preconfigured setups | This document provides a curated list of pre-configured dotfile collections and setups for users looking to quickly cus… | hyprland, dotfiles, linux-customization, window-manager, desktop-environment |
| 004 | `004-getting-started.md` | Getting Started | This document serves as an entry point for new users, directing them to essential installation steps and the primary in… | hyprland, getting-started, installation, desktop-environment, linux-configuration |
| 005 | `005-plugins-development-getting-started.md` | Getting started | This document provides a foundational guide for developing plugins for the Hyprland compositor using C++, including set… | hyprland, c-plus-plus, plugin-development, compositor, linux-desktop, software-extensibility |

### 2. Tutorials & Guides (006–034)
*Step-by-step tutorials and how-to guides*

#### Hypr

| # | File | Title | Summary | Tags |
|---|---|---|---|---|
| 006 | `006-hypr-ecosystem-hyprcursor.md` | hyprcursor | This document provides instructions on how to install, configure, and manage hyprcursor themes within the Hyprland ecos… | hyprland, cursor-theme, configuration, linux-desktop, xcursor-fallback, ui-customization |
| 007 | `007-hypr-ecosystem-hyprlock.md` | hyprlock | This document provides a comprehensive configuration guide for hyprlock, a GPU-accelerated screen locker for the Hyprla… | hyprland, hyprlock, wayland, screen-lock, configuration, linux-security |
| 008 | `008-hypr-ecosystem-hyprshutdown.md` | hyprshutdown | This document provides an overview and configuration guide for hyprshutdown, a utility designed to gracefully terminate… | hyprland, desktop-environment, shutdown-utility, linux-utilities, session-management, nvidia-troubleshooting |
| 009 | `009-hypr-ecosystem-hyprsunset.md` | hyprsunset | This document provides an overview and configuration guide for hyprsunset, a utility for Hyprland that enables blue light… | hyprland, blue-light-filter, gamma-adjustment, system-utility, configuration, linux-desktop |
| 010 | `010-hypr-ecosystem-hyprtoolkit-development.md` | Development | This document provides an introduction to the Hyprtoolkit C++ GUI framework, covering its retained-mode architecture, l… | c-plus-plus, gui-framework, hyprland, retained-mode, layout-management, event-loop |
| 011 | `011-hypr-ecosystem-xdg-desktop-portal-hyprland.md` | xdg-desktop-portal-hyprland | This document provides instructions on installing, configuring, and troubleshooting xdg-desktop-portal-hyprland (XDPH)… | hyprland, xdg-desktop-portal, screensharing, linux-desktop, wayland, configuration |

#### Configuring

| # | File | Title | Summary | Tags |
|---|---|---|---|---|
| 012 | `012-configuring-binds.md` | Binds | This document provides a comprehensive guide to configuring keyboard and mouse bindings in Hyprland, including syntax,… | hyprland, configuration, keybinds, window-manager, linux, input-mapping |
| 013 | `013-configuring-example-configurations.md` | Example configurations | This document provides a curated list of external repositories containing Hyprland dotfiles to serve as configuration e… | hyprland, configuration, dotfiles, customization, window-manager, linux-desktop |
| 014 | `014-configuring-expanding-functionality.md` | Expanding functionality | This document describes the IPC sockets available in Hyprland, explaining how to use socket1 for commands and socket2 f… | hyprland, ipc, socket-communication, bash-scripting, linux-desktop, automation |
| 015 | `015-configuring-performance.md` | Performance | This document provides performance optimization techniques and troubleshooting steps for resolving lag, power consumpti… | hyprland, performance-tuning, wayland, linux-optimization, battery-life, fractional-scaling |
| 016 | `016-configuring-uncommon-tips-tricks.md` | Uncommon tips & tricks | This document provides a collection of common configuration patterns, scripts, and customization techniques for the Hyp… | hyprland, configuration, keyboard-layout, keybinds, scripts, xkb |

#### Nix

| # | File | Title | Summary | Tags |
|---|---|---|---|---|
| 017 | `017-nix-hyprland-on-home-manager.md` | Hyprland on Home Manager | This document provides instructions for installing and configuring the Hyprland window manager using NixOS and Home Man… | hyprland, nix, nixos, home-manager, wayland, declarative-configuration |
| 018 | `018-nix-hyprland-on-nixos.md` | Hyprland on NixOS | This document provides instructions on configuring the Hyprland window manager on NixOS using official modules and disc… | nixos, hyprland, configuration, wayland, home-manager, linux-desktop |
| 019 | `019-nix-hyprland-on-other-distros.md` | Hyprland on Other Distros | This document provides instructions for installing and managing the Hyprland window manager on Linux distributions that… | hyprland, nix, linux, window-manager, nixgl, package-management |
| 020 | `020-nix-options-overrides.md` | Options & Overrides | This document explains how to customize and override Hyprland package configurations and build options using Nix, NixOS… | nixos, home-manager, hyprland, nix-packaging, package-overrides, xwayland |
| 021 | `021-nix-plugins.md` | Plugins | This document explains the standard procedures for managing, installing, and building Hyprland plugins within the Nix e… | nix, hyprland, plugin-management, nixpkgs, flakes, linux-desktop |

#### Useful

| # | File | Title | Summary | Tags |
|---|---|---|---|---|
| 022 | `022-useful-utilities-app-clients.md` | App clients | This document lists recommended Wayland-compatible replacements for common communication applications that struggle wit… | wayland, linux-desktop, software-alternatives, discord-clients, matrix-clients |
| 023 | `023-useful-utilities-clipboard-managers.md` | Clipboard Managers | This document provides instructions for integrating and configuring various clipboard management tools within the Hyprl… | hyprland, clipboard-manager, wayland, linux-desktop, system-configuration, productivity-tools |
| 024 | `024-useful-utilities-color-pickers.md` | Color pickers | This document recommends using the hyprpicker utility for color picking within the Hyprland window manager ecosystem. | hyprland, color-picker, desktop-utilities, linux-desktop, hyprpicker, screen-tools |
| 025 | `025-useful-utilities-screen-sharing.md` | Screen sharing | This document provides instructions for setting up screensharing in Hyprland using PipeWire and addresses compatibility… | hyprland, screensharing, pipewire, wayland, xwayland, desktop-portal |
| 026 | `026-useful-utilities-systemd-start.md` | Systemd startup | This document provides instructions on using the Universal Wayland Session Manager (UWSM) to wrap Wayland compositors l… | wayland, session-management, systemd, hyprland, linux-desktop, xdg-autostart |

#### Plugins

| # | File | Title | Summary | Tags |
|---|---|---|---|---|
| 027 | `027-plugins-development-advanced.md` | Advanced | This document outlines advanced techniques for developing Hyprland plugins, specifically covering member access manipul… | hyprland, plugin-api, cpp, function-hooking, configuration-management, linux-compositor |
| 028 | `028-plugins-development-plugin-guidelines.md` | Plugin guidelines | This document provides guidelines for developing compatible plugins for Hyprland, focusing on manifest configuration, b… | hyprland, plugin-development, manifest-configuration, hyprpm, api-best-practices |
| 029 | `029-plugins-development.md` | Development | This document outlines the development workflow and technical guidelines for creating custom plugins for the Hyprland w… | hyprland, plugin-development, software-extensions, window-manager, developer-guide |
| 030 | `030-plugins-using-plugins.md` | Using plugins | This document provides instructions on how to install, manage, and load plugins for the Hyprland window manager using t… | hyprland, plugins, hyprpm, window-manager, installation-guide |

#### Other

| # | File | Title | Summary | Tags |
|---|---|---|---|---|
| 031 | `031-configuring.md` | Configuring | This document serves as a comprehensive guide for customizing and configuring the Hyprland window manager environment,… | hyprland, desktop-customization, configuration-guide, window-manager, linux-desktop |
| 032 | `032-crashes-and-bugs.md` | Crashes and Bugs | This document provides comprehensive procedures for debugging, diagnosing crashes, and gathering technical logs for the… | hyprland, debugging, linux, crash-report, system-logs, wayland |
| 033 | `033-hyprland-wiki.md` | Hyprland Wiki | This document serves as the introductory landing page for the Hyprland compositor wiki, providing guidance on versionin… | hyprland, wayland, compositor, linux-desktop, documentation-portal, window-manager |
| 034 | `034-nvidia.md` | Nvidia | This document provides a guide for configuring Nvidia graphics drivers and hardware acceleration to ensure compatibilit… | nvidia, hyprland, wayland, linux, graphics-drivers, kernel-modules |

### 3. Concepts & Fundamentals (035–038)
*Core concepts and fundamental principles*

| # | File | Title | Summary | Tags |
|---|---|---|---|---|
| 035 | `035-hypr-ecosystem-hyprpwcenter.md` | hyprpwcenter | This document provides an overview of hyprpwcenter, a graphical user interface tool designed for managing and configuri… | pipewire, gui-control-center, audio-management, hyprland-ecosystem, linux-audio |
| 036 | `036-hypr-ecosystem-hyprsysteminfo.md` | hyprsysteminfo | This document describes hyprsysteminfo, a graphical utility designed to display and easily copy system information and… | hyprland, system-information, gui-application, utility-tool |
| 037 | `037-plugins.md` | Plugins | This document provides an overview of the plugin system for the Hyprland window manager, including resources for both u… | hyprland, plugin-system, window-manager, software-extension, customization |
| 038 | `038-useful-utilities-hypr-ecosystem.md` | Hypr Ecosystem | This document provides an overview of the hypr ecosystem, a suite of applications specifically designed for seamless in… | hyprland, desktop-environment, ecosystem, software-utilities, linux-desktop |

### 4. Configuration (039–060)
*Configuration, settings, and customization*

| # | File | Title | Summary | Tags |
|---|---|---|---|---|
| 039 | `039-configuring-animations.md` | Animations | This document explains how to configure animation settings, including bezier curves and the hierarchical animation tree… | hyprland, configuration, animations, bezier-curves, window-manager, ui-customization |
| 040 | `040-configuring-environment-variables.md` | Environment variables | This document provides instructions and best practices for configuring environment variables within the Hyprland window… | hyprland, environment-variables, wayland, linux-configuration, display-server, nvidia-setup |
| 041 | `041-configuring-gestures.md` | Gestures | This document outlines the configuration syntax and supported parameters for trackpad gestures in Hyprland, including a… | hyprland, configuration, gestures, trackpad-support, input-mapping, window-management |
| 042 | `042-configuring-keywords.md` | Keywords | This document outlines advanced configuration keywords for the Hyprland compositor, covering execution commands, multi-… | hyprland, configuration, shell-execution, input-devices, environment-variables, config-files |
| 043 | `043-configuring-monitors.md` | Monitors | This document describes the syntax and configuration options for defining monitor settings, including resolution, posit… | hyprland, monitor-configuration, display-settings, linux-desktop, compositor-config |
| 044 | `044-configuring-multi-gpu.md` | Multi-GPU | This document explains how to configure Hyprland to utilize specific GPUs in multi-GPU systems by identifying device pa… | hyprland, multi-gpu, drm, linux-configuration, udev-rules, gpu-passthrough |
| 045 | `045-configuring-permissions.md` | Permissions | This document explains how to configure and manage the permission system in Hyprland to control sensitive compositor ac… | hyprland, permissions, security, compositor, configuration, access-control |
| 046 | `046-configuring-start.md` | Start | This document provides instructions on locating, managing, and structuring the Hyprland configuration file, including h… | hyprland, configuration-file, linux-desktop, system-settings, hyprlang, window-manager |
| 047 | `047-configuring-tearing.md` | Tearing | This document provides instructions on how to enable screen tearing in Hyprland to reduce input latency in games, inclu… | hyprland, screen-tearing, window-rules, gpu-configuration, latency-reduction |
| 048 | `048-configuring-window-rules.md` | Window Rules | This document explains how to configure window rules in Hyprland to control window behavior, appearance, and placement… | hyprland, window-management, configuration, window-rules, linux-desktop, regex |
| 049 | `049-configuring-workspace-rules.md` | Workspace Rules | This document explains how to configure workspace-specific behaviors in Hyprland by applying custom rules and utilizing… | hyprland, workspace-rules, window-management, configuration, compositor-settings, desktop-customization |
| 050 | `050-configuring-xwayland.md` | XWayland | This document provides configuration details for managing XWayland behavior in Hyprland, specifically addressing HiDPI… | xwayland, hidpi, scaling, unix-sockets, configuration, wayland |
| 051 | `051-hypr-ecosystem-aquamarine.md` | aquamarine | This document provides an overview of the Aquamarine library, a lightweight rendering backend for Linux, including inst… | linux, rendering-backend, wayland, drm, kms, environment-variables |
| 052 | `052-hypr-ecosystem-hypridle.md` | hypridle | This document provides configuration instructions and parameter definitions for hypridle, the idle management daemon fo… | hyprland, idle-daemon, linux-desktop, configuration, system-management, wayland |
| 053 | `053-hypr-ecosystem-hyprland-qt-support.md` | hyprland-qt-support | This document describes the configuration options available for the hyprland-qt-support package, which provides a QML s… | hyprland, qt6, ui-configuration, qml-style, desktop-customization |
| 054 | `054-hypr-ecosystem-hyprlauncher.md` | hyprlauncher | This document provides an overview of the Hyprlauncher daemon, including instructions for usage, daemon management, and… | hyprland, launcher, daemon, linux-desktop, system-configuration, application-launcher |
| 055 | `055-hypr-ecosystem-hyprpaper.md` | hyprpaper | This document provides installation, configuration, and usage instructions for hyprpaper, an IPC-controlled wallpaper u… | hyprland, wallpaper-manager, linux-desktop, ipc-configuration, system-customization |
| 056 | `056-hypr-ecosystem-hyprpolkitagent.md` | hyprpolkitagent | This document provides instructions on installing and configuring the hyprpolkitagent authentication daemon for use wit… | hyprland, polkit, authentication-daemon, systemd, linux-configuration, desktop-environment |
| 057 | `057-hypr-ecosystem-hyprqt6engine.md` | hyprqt6engine | This document describes how to install and configure hyprqt6engine, a theme engine for Qt6 applications designed for co… | qt6-theming, hyprland, desktop-customization, linux-gui, kde-compatibility |
| 058 | `058-nix-cachix.md` | Cachix | This document explains how to configure a Cachix binary cache for the Hyprland Nix flake to avoid long build times by u… | nix, hyprland, cachix, binary-cache, nixos, configuration |
| 059 | `059-nix.md` | Nix | This document provides instructions for installing and configuring the Hyprland window manager on NixOS using official… | nixos, hyprland, home-manager, linux-configuration, window-manager, nix-modules |
| 060 | `060-useful-utilities-must-have.md` | Must have | This document outlines the essential software dependencies and system components required to ensure optimal performance… | hyprland, desktop-environment, system-configuration, linux-desktop, software-dependencies |

### 5. API Reference (061–082)
*API and SDK reference*

| # | File | Title | Summary | Tags |
|---|---|---|---|---|
| 061 | `061-configuring-dispatchers.md` | Dispatchers | This document provides a comprehensive reference for available dispatchers and parameter types used to control window m… | hyprland, dispatchers, window-management, wayland-compositor, configuration-reference |
| 062 | `062-configuring-dwindle-layout.md` | Dwindle Layout | This document provides configuration options, layout behavior, and dispatchers for the Dwindle tiling window management… | window-management, dwindle-layout, tiling-window-manager, config-reference, layout-dispatchers |
| 063 | `063-configuring-master-layout.md` | Master Layout | This document provides a technical reference for the master tiling layout, detailing its configuration options, workspa… | window-manager, tiling-layout, hyprland, desktop-customization, configuration-reference, layout-management |
| 064 | `064-configuring-monocle-layout.md` | Monocle Layout | This document explains the functionality and configuration quirks of the Monocle window layout in Hyprland. | hyprland, window-manager, layout-configuration, monocle-layout, desktop-environment |
| 065 | `065-configuring-scrolling-layout.md` | Scrolling Layout | This document provides the configuration options, layout messages, and rules for the scrolling layout, which arranges w… | hyprland, scrolling-layout, window-management, configuration-settings, layout-messages |
| 066 | `066-configuring-using-hyprctl.md` | Using hyprctl | This document provides a comprehensive reference for the hyprctl command-line utility, which is used to control and que… | hyprland, cli, compositor, linux, ipc, system-configuration |
| 067 | `067-configuring-variables.md` | Variables | This document provides a comprehensive reference for configuring Hyprland options, including definitions for variable t… | hyprland, configuration, wayland, compositor, desktop-environment, reference-guide |
| 068 | `068-connect.md` | Connect | This document provides a directory of official communication channels, social media profiles, and web resources for the… | hyprland, community-resources, official-links, support-channels, documentation |
| 069 | `069-hypr-ecosystem-hyprgraphics.md` | hyprgraphics | This document provides an overview of the hyprgraphics library, which supplies shared utility functions for graphics pr… | graphics-library, resource-management, image-loading, color-calculation, hypr-ecosystem |
| 070 | `070-hypr-ecosystem-hyprland-guiutils.md` | hyprland-guiutils | This document provides an overview and links to the Hyprland GUI utilities, serving as the official successor to hyprla… | hyprland, gui-utilities, linux-desktop, software-ecosystem, hyprgraphics |
| 071 | `071-hypr-ecosystem-hyprlang.md` | hyprlang | This document outlines the syntax, structure, and features of the hyprlang configuration language, including variable h… | hyprlang, configuration-syntax, parsing-library, scripting-language, config-format |
| 072 | `072-hypr-ecosystem-hyprpicker.md` | hyprpicker | This document provides a reference for the command-line flags and configuration options available for the hyprpicker co… | hyprland, color-picker, cli-utility, desktop-environment, screen-capture |
| 073 | `073-hypr-ecosystem-hyprtoolkit.md` | hyprtoolkit | This document provides an overview and configuration reference for hyprtoolkit, a GUI development toolkit designed for… | wayland, gui-toolkit, hyprland, configuration-reference, linux-desktop |
| 074 | `074-hypr-ecosystem-hyprutils.md` | hyprutils | This document describes hyprutils, a library that provides shared data structures and implementations for the hypr ecos… | hyprland, shared-libraries, ecosystem-tools, development-utilities |
| 075 | `075-hypr-ecosystem-hyprwayland-scanner.md` | hyprwayland-scanner | hyprwayland-scanner is a utility designed to generate safe C++ source files and headers from Wayland protocol specifica… | wayland, c-plus-plus, code-generation, protocol-scanner, hyprland-ecosystem |
| 076 | `076-hypr-ecosystem.md` | Hypr Ecosystem | This document clarifies that the provided documentation is maintained specifically for the latest development versions… | documentation-policy, version-control, git-branch, software-development |
| 077 | `077-ipc.md` | IPC | This document describes the IPC mechanisms for Hyprland, explaining how to interact with the compositor using UNIX sock… | hyprland, ipc, unix-sockets, linux-compositor, event-driven, system-automation |
| 078 | `078-useful-utilities-app-launchers.md` | App launchers | This document provides a categorized list and brief descriptions of various application launchers and menu systems comp… | wayland, application-launcher, desktop-environment, linux-desktop, system-utility |
| 079 | `079-useful-utilities-file-managers.md` | File Managers | This document provides a curated list of graphical and terminal-based file managers available for Linux desktop environ… | file-manager, gui-tools, tui-applications, linux-utilities, desktop-environment |
| 080 | `080-useful-utilities-other.md` | Other | This document provides a curated list of third-party tools, utilities, and applications that enhance the functionality… | hyprland, wayland, utilities, system-tools, desktop-environment, software-list |
| 081 | `081-useful-utilities-wallpapers.md` | Wallpapers | This document provides an overview of various wallpaper utilities and daemons compatible with the Wayland display proto… | wayland, wallpaper-utility, desktop-customization, linux-desktop, wallpaper-daemon |
| 082 | `082-useful-utilities.md` | Useful Utilities | This document serves as an index page for the Hyprland wiki, providing navigation to various useful utilities and exter… | hyprland, wiki-index, utilities, software-resources, desktop-environment |

### 6. Troubleshooting (083–083)
*Troubleshooting, FAQs, and error handling*

| # | File | Title | Summary | Tags |
|---|---|---|---|---|
| 083 | `083-faq.md` | FAQ | This document provides troubleshooting steps and configuration guidance for common issues encountered when using the Hy… | hyprland, troubleshooting, wayland, linux, desktop-environment, installation |

### 7. Meta & Resources (086–093)
*Pricing, legal, community, and other resources*

| # | File | Title | Summary | Tags |
|---|---|---|---|---|
| 086 | `086-contributing-and-debugging-issue-guidelines.md` | Issue Guidelines | This document outlines the required procedure for reporting bugs or requesting features by directing users to open disc… | contribution-guidelines, issue-tracking, feature-requests, bug-reporting, community-standards, project-management |
| 087 | `087-contributing-and-debugging-pr-guidelines.md` | PR Guidelines | This document outlines the coding standards, submission requirements, and technical guidelines for contributors to the… | contribution-guidelines, code-style, pull-request, c-plus-plus, development-workflow, coding-standards |
| 088 | `088-contributing-and-debugging-tests.md` | Tests | This document outlines the procedures for running unit and integration tests within Hyprland projects to ensure code qu… | hyprland, unit-testing, gtest, hyprtester, code-quality, software-testing |
| 089 | `089-contributing-and-debugging-translations.md` | Translations | This document provides instructions for contributing translations to the Hyprland ecosystem, detailing how to register… | hyprland, localization, translation, contributing, open-source, c-plus-plus |
| 090 | `090-contributing-and-debugging.md` | Contributing and Debugging | This document provides instructions for setting up a development environment, building Hyprland in debug mode, and perf… | hyprland, debugging, development-setup, c-plus-plus, cmake, nix |
| 091 | `091-nix-contributing-and-debugging.md` | Contributing and Debugging | This document outlines the procedures for building, debugging, and troubleshooting Hyprland and related programs within… | hyprland, nix, debugging, software-build, stacktrace, development-environment |
| 093 | `093-useful-utilities-status-bars.md` | Status bars | This document provides an overview and configuration guide for various status bar and widget system tools compatible wi… | hyprland, wayland, waybar, desktop-customization, widgets, linux-desktop |

---

*Auto-generated. Files numbered sequentially following a content-driven learning progression.*