# Ghostty Documentation Index

> Organized index for AI agent consumption. Documents follow logical learning sequence.

## Metadata Summary

| Property | Value |
|----------|-------|
| **Source** | https://ghostty.org/docs |
| **Generated** | 2026-03-10T06:40:00Z |
| **Total Documents** | 101 |
| **Strategy** | crawler |

---

## Document Index

### 1. Introduction & Overview (001-005)
*Core documentation introducing Ghostty terminal emulator*

| # | File | Title | Summary | Keywords |
|---|------|-------|---------|----------|
| 001 | `001-index.md` | Ghostty | Ghostty is a cross-platform terminal emulator emphasizing speed, rich features, and performance through native UI and GPU acceleration. | terminal-emulator, cross-platform, gpu-acceleration, software-tool |
| 002 | `002-docs.md` | Ghostty Docs | This document introduces Ghostty, a terminal emulator characterized by its speed, extensive features, and cross-platform compatibility achieved through native UI and GPU acceleration. | terminal-emulator, cross-platform, gpu-acceleration, fast-software |
| 003 | `003-download.md` | Download Ghostty | This document outlines the installation methods for Ghostty version 1.3.0 on both macOS and Linux operating systems. | installation, macos, linux, binary, package-manager, build-from-source |
| 004 | `004-docs-about.md` | About Ghostty | Ghostty is a terminal emulator designed to be fast, feature-rich, and native, uniquely achieving competitiveness across all three areas by utilizing a shared core library called libghostty for cross-platform emulation. | terminal-emulator, performance, native-ui, libghostty, zig, macos, linux, feature-rich |
| 005 | `005-docs-sponsor.md` | Financial Support | This document explains how the Ghostty project is supported financially through donations via its fiscal sponsor, Hack Club, detailing how funds are allocated and the benefits of its non-profit structure. | non-profit, fiscal-sponsorship, donations, hack-club, contributor-compensation, governance |

### 2. Installation (006-011)
*Guides for installing Ghostty across different platforms*

| # | File | Title | Summary | Keywords |
|---|------|-------|---------|----------|
| 006 | `006-docs-install-binary.md` | Binaries and Packages - Install | This document outlines the various methods available for installing the Ghostty terminal emulator using prebuilt binaries and packages across different operating systems. | installation, prebuilt-binaries, macos, linux, nix, homebrew, package-management |
| 007 | `007-docs-install-pre.md` | Prerelease Builds - Install | This document explains how users can install and use prerelease (tip) builds of the Ghostty terminal emulator across various operating systems to test new features and report bugs. | prerelease, installation, ghostty, macos, linux, nix, aur, homebrew |
| 008 | `008-docs-install-build.md` | Build from Source - Install | This document provides instructions for compiling the Ghostty terminal emulator from its source code, detailing prerequisites like installing the correct Zig compiler version. | ghostty, source-code, build-from-source, zig, linux-dependencies, nix |
| 009 | `009-docs-install-package.md` | Packaging Ghostty - Install | This document directs users interested in building and distributing the Ghostty software to the official packaging guide located within the source tree. | packaging, building, distribution, downstream-maintainers, ghostty |
| 010 | `010-docs-linux.md` | Linux | This document provides Linux-specific instructions and prerequisites for installing and running the Ghostty terminal emulator, focusing on installation methods and minimum required GTK and Adwaita versions. | linux, installation, gtk, adwaita, dependencies, wayland, x11 |
| 011 | `011-docs-linux-systemd.md` | Systemd and D-Bus - Linux | This document explains how Ghostty leverages systemd and D-Bus integration to enable on-demand launching, instantaneous window creation, and centralized logging. | ghostty, systemd, dbus, activation, user-service, instant-launching |

### 3. Release Notes (012-022)
*Version history and changelog - sorted newest to oldest*

| # | File | Title | Summary | Keywords |
|---|------|-------|---------|----------|
| 012 | `012-docs-install-release-notes.md` | Release Notes - Install | This document provides an index listing all published versions of the Ghostty software along with links to their corresponding release notes. | ghostty, version-history, release-notes, software-updates |
| 013 | `013-docs-install-release-notes-1-3-0.md` | 1.3.0 - Release Notes | This document details the new features, improvements, and bug fixes included in the Ghostty 1.3.0 release, highlighting major additions like scrollback search and native scrollbars. | release-notes, scrollback-search, native-scrollbars, osc-133, keybinds, command-notifications |
| 014 | `014-docs-install-release-notes-1-2-3.md` | 1.2.3 - Release Notes | This document details the release notes for Ghostty version 1.2.3, highlighting critical fixes for deadlocks, titlebar styling issues on macOS, and improvements to font rendering. | release-notes, bug-fixes, deadlock-fix, macos-titlebar, font-rendering, patch-release |
| 015 | `015-docs-install-release-notes-1-2-2.md` | 1.2.2 - Release Notes | This document details the release notes for Ghostty version 1.2.2, primarily addressing a critical memory leak regression from the previous version. | release-notes, hotfix, memory-leak, macos, font-rendering, bug-fix |
| 016 | `016-docs-install-release-notes-1-2-1.md` | 1.2.1 - Release Notes | This document details the release notes for Ghostty version 1.2.1, focusing on fixes for issues introduced in the previous version. | release-notes, bug-fixes, font-rendering, shell-integration, configuration, macos-fixes, gtk-fixes |
| 017 | `017-docs-install-release-notes-1-2-0.md` | 1.2.0 - Release Notes | This document details the major features and improvements introduced in Ghostty version 1.2.0, including a new command palette and configuration options. | release-notes, command-palette, quick-terminal, icon-update, renderer-rework, ssh-integration |
| 018 | `018-docs-install-release-notes-1-1-3.md` | 1.1.3 - Release Notes | This document details the release notes for Ghostty version 1.1.3, which focuses primarily on fixing critical compatibility issues with Gnome 48 and GTK 4.18. | release-notes, compatibility, gtk-4.18, gnome-48, bug-fixes, macos |
| 019 | `019-docs-install-release-notes-1-1-2.md` | 1.1.2 - Release Notes | This document details the release notes for Ghostty version 1.1.2, which serves as a hotfix for a critical macOS regression affecting control-modified keys. | release-notes, hotfix, macos, kitty-protocol, regression-fix |
| 020 | `020-docs-install-release-notes-1-1-1.md` | 1.1.1 - Release Notes | This document details the fixes, improvements, and new features introduced in Ghostty version 1.1.1, primarily focusing on correcting regressions from the 1.1.0 release. | release-notes, bug-fixes, ssd-support, ime-input, macos-fixes, gtk-updates |
| 021 | `021-docs-install-release-notes-1-1-0.md` | 1.1.0 - Release Notes | This document details the features, bug fixes, and improvements included in the Ghostty 1.1.0 release, highlighting changes to window decoration support on Linux. | release-notes, window-decoration, ssd, ime-support, keybindings, alpha-blending, macos, linux |
| 022 | `022-docs-install-release-notes-1-0-1.md` | 1.0.1 - Release Notes | These release notes detail version 1.0.1 of Ghostty, highlighting security fixes, configuration improvements like default file creation and better settings opening logic. | release-notes, security-fix, configuration, bitmap-fonts, macos, gtk, bug-fix |

### 4. Features (023-026)
*Ghostty's feature documentation*

| # | File | Title | Summary | Keywords |
|---|------|-------|---------|----------|
| 023 | `023-docs-features.md` | Features | This document details the extensive features supported by the Ghostty terminal emulator, categorized for both end-users and application developers. | terminal-emulator, feature-set, platform-native, gpu-acceleration, kitty-protocol, xterm-compatibility |
| 024 | `024-docs-features-theme.md` | Color Theme - Features | This document explains how to customize the color theme in Ghostty using built-in themes, specifying light and dark modes, and authoring custom theme files. | theming, color-customization, configuration, built-in-themes, custom-themes |
| 025 | `025-docs-features-shell-integration.md` | Shell Integration - Features | This document explains how Ghostty automatically injects shell integration features for supported shells like bash, zsh, fish, and elvish. | shell-integration, ghostty, terminal-features, bash, zsh, fish, configuration |
| 026 | `026-docs-features-applescript.md` | AppleScript (macOS) - Features | This document provides a comprehensive guide to automating the Ghostty terminal emulator on macOS using AppleScript, detailing the object model and available commands. | ghostty, macos, applescript, automation, scripting-dictionary, terminal-control |

### 5. Configuration (027-031)
*How to configure Ghostty*

| # | File | Title | Summary | Keywords |
|---|------|-------|---------|----------|
| 027 | `027-docs-config.md` | Configuration | This document explains how to configure the Ghostty terminal emulator using its text-based configuration file, detailing file locations, supported syntax, and methods for splitting configuration. | configuration, ghostty, text-based-config, file-locations, syntax, key-value |
| 028 | `028-docs-config-keybind.md` | Keybindings - Configuration | This document explains how to define custom keyboard shortcuts in Ghostty using the `keybind` configuration option, detailing the syntax for triggers, modifiers, prefixes, and available actions. | keybindings, configuration, customization, trigger-syntax, modifiers, actions, ghostty-config |
| 029 | `029-docs-config-keybind-sequence.md` | Trigger Sequences - Keybindings | This document explains how to configure keybindings in Ghostty that require a specific sequence of keypress events to activate an action, using the '>' separator. | keybindings, trigger-sequence, configuration, leader-key, ghostty-config |
| 030 | `030-docs-config-keybind-reference.md` | Action Reference - Keybindings | This document serves as a reference listing and describing all available keybinding actions within the Ghostty terminal emulator. | ghostty, keybinding, reference, actions, terminal-control |
| 031 | `031-docs-config-reference.md` | Option Reference - Configuration | This document serves as a reference detailing various configuration options for the Ghostty terminal emulator, focusing primarily on settings related to font selection, styling, and GUI language. | configuration-options, font-settings, language, font-features, gui-settings |

### 6. Help & Troubleshooting (032-038)
*Common issues, solutions, and support resources*

| # | File | Title | Summary | Keywords |
|---|------|-------|---------|----------|
| 032 | `032-docs-help.md` | Help | This document explains how users can seek help, find solutions to common issues encountered with Ghostty, and details the correct procedure for reporting bugs or requesting new features. | troubleshooting, support, bug-reporting, community-help, common-problems |
| 033 | `033-docs-help-terminfo.md` | Terminfo - Help | This document explains how Ghostty uses the terminfo format, specifically setting the TERM variable to 'xterm-ghostty', and provides solutions for compatibility issues. | terminfo, ghostty, term-variable, sudo-issues, ssh-compatibility, shell-integration |
| 034 | `034-docs-help-gtk-single-instance.md` | GTK Single Instance - Help | This document explains how Ghostty utilizes GTK single instance mode by default when not launched from a command-line interface. | gtk, single-instance, ghostty, startup-performance, configuration, cli-detection |
| 035 | `035-docs-help-gtk-opengl-context.md` | GTK OpenGL Context - Help | This document explains troubleshooting steps for the Ghostty error where it fails to start due to being unable to acquire an OpenGL context from GTK. | ghostty, opengl, gtk, context-error, troubleshooting, driver-issues |
| 036 | `036-docs-help-macos-tiling-wms.md` | macOS Tiling Window Managers - Help | This document explains why Ghostty tabs may appear as separate windows when using macOS tiling window managers like Yabai or Aerospace. | ghostty, macos, tiling-window-managers, yabai, aerospace, native-tabs, window-management |
| 037 | `037-docs-help-macos-login-shells.md` | macOS Login Shells - Help | This document explains why macOS defaults terminal shells to be login shells, contrasting this behavior with other Unix systems. | macos, terminal-emulators, login-shells, zsh, dotfiles, shell-configuration |
| 038 | `038-docs-help-synchronized-output.md` | Synchronized Output - Help | This document explains that screen tearing or flickering in the Ghostty terminal emulator is typically due to the application not synchronizing its output correctly. | ghostty, screen-tearing, synchronized-output, performance, cli-applications, rendering |

### 7. VT - Terminal API Overview (039-041)
*Introduction to Ghostty's terminal API for developers*

| # | File | Title | Summary | Keywords |
|---|------|-------|---------|----------|
| 039 | `039-docs-vt.md` | Terminal API (VT) | This document provides an overview of how Ghostty supports control sequences (VT sequences or escape codes) used by terminal programs to interact with the terminal. | ghostty, api, control-sequences, vt-sequences, escape-codes, terminal-interaction |
| 040 | `040-docs-vt-reference.md` | Reference - Terminal API (VT) | This document serves as a reference listing the various VT sequences supported by the Ghostty terminal emulator, organized by sequence type. | vt-sequences, ghostty, terminal-emulation, control-sequences, operating-system-commands |
| 041 | `041-docs-vt-external.md` | External Protocols - Terminal API (VT) | This document lists the external terminal emulator protocols that Ghostty supports, such as Hyperlinks and Kitty Color Protocol. | external-protocols, terminal-emulators, osc-8, osc-21, ghostty-support |

### 8. VT Concepts (042-045)
*Fundamental concepts for understanding terminal emulation*

| # | File | Title | Summary | Keywords |
|---|------|-------|---------|----------|
| 042 | `042-docs-vt-concepts-sequences.md` | Control Sequences - Concepts | This document explains terminal control sequences, which programs use to send commands like cursor movement and color changes to the terminal. | terminal-control, escape-sequences, control-characters, csi-sequences, osc-sequences, data-encoding |
| 043 | `043-docs-vt-concepts-colors.md` | Colors - Concepts | This document explains the color capabilities of Ghostty, detailing its 256-color palette, special colors, dynamic colors, and the various color specification formats. | color-specification, terminal-emulation, ghostty, special-colors, dynamic-colors, rgb-formats |
| 044 | `044-docs-vt-concepts-cursor.md` | Cursor - Concepts | This document explains the concept of the terminal cursor, defining its location, its role in character printing and control sequences, and introducing the related concept of the pending wrap state. | terminal-cursor, cursor-position, pending-wrap-state, terminal-api, control-sequences |
| 045 | `045-docs-vt-concepts-screen.md` | Screen - Concepts | This document provides reference material and conceptual explanations for the Ghostty terminal emulator, specifically detailing aspects of its Virtual Terminal (VT) implementation. | ghostty, terminal, vt, reference, documentation, concepts |

### 9. VT Control Characters (046-050)
*Basic control characters in terminal emulation*

| # | File | Title | Summary | Keywords |
|---|------|-------|---------|----------|
| 046 | `046-docs-vt-control-bel.md` | Bell (BEL) - Control | This document explains the purpose of the Bell (BEL) control character (ASCII 0x07), which is used to alert the user. | bell-character, control-character, user-attention, osc-sequence, terminal-behavior |
| 047 | `047-docs-vt-control-bs.md` | Backspace (BS) - Control | This document explains the function of the Backspace (BS) control character, which moves the cursor backward by one position in a terminal interface. | control-character, cursor-movement, backspace, terminal, vt |
| 048 | `048-docs-vt-control-cr.md` | Carriage Return (CR) - Control | This document explains the behavior of the Carriage Return (CR, 0x0D) control sequence on the cursor position. | carriage-return, cursor-movement, control-sequence, terminal, pending-wrap, left-margin |
| 049 | `049-docs-vt-control-lf.md` | Linefeed (LF) - Control | This document describes the action to move the terminal cursor down by one line, including necessary scrolling. | cursor-control, terminal, line-feed, movement |
| 050 | `050-docs-vt-control-tab.md` | Tab (TAB) - Control | This document describes the control sequence used to move the terminal cursor to the next tab stop position. | cursor-movement, tab-stop, control-sequence, vt |

### 10. VT ESC Sequences (051-058)
*Escape sequences for terminal control*

| # | File | Title | Summary | Keywords |
|---|------|-------|---------|----------|
| 051 | `051-docs-vt-esc-deckpam.md` | Keypad Application Mode (DECKPAM) - ESC | This document outlines the escape sequence used to set the numeric keypad to application mode in a terminal environment. | terminal, keypad, escape-sequence, control-codes, application-mode |
| 052 | `052-docs-vt-esc-deckpnm.md` | Keypad Numeric Mode (DECKPNM) - ESC | This document specifies the control sequences used to set the numeric keypad to numeric mode within a terminal environment. | terminal, control-sequence, numeric-keypad, escape-sequence, vt |
| 053 | `053-docs-vt-esc-decaln.md` | Screen Alignment Test (DECALN) - ESC | This document details the behavior and usage of the DEC ALN (Declare Alignment) control sequence, which resets screen margins and fills the screen with 'E'. | dec-aln, escape-sequence, terminal-control, cursor-manipulation, screen-filling |
| 054 | `054-docs-vt-esc-decrc.md` | Restore Cursor (DECRC) - ESC | This document describes the ANSI escape sequence used to restore the cursor state that was previously saved using the Save Cursor (DECSC) command. | vt100, ansi, escape-sequence, cursor-control, decrc |
| 055 | `055-docs-vt-esc-decsc.md` | Save Cursor (DECSC) - ESC | This document explains the functionality of the Save Cursor (DECSC) control sequence, detailing which attributes are saved. | save-cursor, decsc, cursor-state, terminal-control, sgr-attributes |
| 056 | `056-docs-vt-esc-ind.md` | Index (IND) - ESC | This document details the behavior of the DEC Index (IND) control sequence, which moves the cursor down one cell, potentially causing scrolling. | dec-index, terminal-control, cursor-movement, scrolling, escape-sequence |
| 057 | `057-docs-vt-esc-ri.md` | Reverse Index (RI) - ESC | This document details the behavior of the Reverse Index (RI) escape sequence, which moves the cursor up one cell and potentially triggers scrolling. | reverse-index, escape-sequence, cursor-movement, scrolling, terminal-control |
| 058 | `058-docs-vt-esc-ris.md` | Reset to Initial State (RIS) - ESC | This document describes the Full Reset (RIS) sequence for terminal emulation, which reverts the terminal to its initial, default operational state. | full-reset, ris, terminal-control, initial-state, ansi-escape-sequence |

### 11. VT CSI - Cursor Movement (059-069)
*CSI sequences for cursor positioning*

| # | File | Title | Summary | Keywords |
|---|------|-------|---------|----------|
| 059 | `059-docs-vt-csi-cup.md` | Cursor Position (CUP) - CSI | This document details the Control Sequence Introducer (CSI) command used to move the terminal cursor to a specific row and column. | terminal-control, cursor-movement, csi-sequence, cup, ansi-escape-codes, origin-mode |
| 060 | `060-docs-vt-csi-cuu.md` | Cursor Up (CUU) - CSI | This document details the sequence and behavior for moving the terminal cursor a specified number of cells up. | terminal-control, cursor-movement, ansi-escape-sequence, cuu, terminal-manipulation |
| 061 | `061-docs-vt-csi-cud.md` | Cursor Down (CUD) - CSI | This document details the ANSI escape sequence used to move the terminal cursor down a specified number of cells. | cursor-movement, ansi-escape-sequence, terminal-control, csi-sequence, cursor-down |
| 062 | `062-docs-vt-csi-cuf.md` | Cursor Forward (CUF) - CSI | This document details the Control Sequence Introducer (CSI) command used to move the cursor a specified number of cells to the right. | csi, cursor-movement, terminal-control, escape-sequences, cuf, right-move |
| 063 | `063-docs-vt-csi-cub.md` | Cursor Backward (CUB) - CSI | This document details the Control Sequence Introducer (CSI) sequence CUB (Cursor Backward) which moves the terminal cursor left. | csi, cursor-backward, cub, terminal-control, escape-sequence, wrapping-modes |
| 064 | `064-docs-vt-csi-cnl.md` | Cursor Next Line (CNL) - CSI | This document explains the ANSI escape sequence required to move the cursor down a specified number of cells and then return it to the beginning of the line. | cursor-movement, ansi-escape-sequence, terminal-control, csi, cursor-down-line |
| 065 | `065-docs-vt-csi-cpl.md` | Cursor Preceding Line (CPL) - CSI | This document details the control sequence for moving the terminal cursor up 'n' lines to the start of the respective lines. | cursor-movement, terminal-control, cpl, ansi-escape-sequence, control-sequence |
| 066 | `066-docs-vt-csi-cht.md` | Cursor Horizontal Tabulation (CHT) - CSI | This document describes the CSI sequence used to move the cursor right to the next tab stop. | cursor-movement, terminal-control, csi-sequence, tab-stop |
| 067 | `067-docs-vt-csi-cbt.md` | Cursor Backward Tabulation (CBT) - CSI | This document details the Control Sequence (CSI) command for moving the cursor backward to the preceding tab stop. | terminal-control, escape-sequences, cursor-movement, cbt, tab-stops |
| 068 | `068-docs-vt-csi-hpa.md` | Horizontal Position Absolute (HPA) - CSI | This document explains the control sequence used to move the cursor to a specific column. | cursor-movement, escape-sequence, terminal-control, cup, hpa |
| 069 | `069-docs-vt-csi-vpa.md` | Vertical Position Absolute (VPA) - CSI | This document describes the VT escape sequence VPA used to move the cursor to a specific row in a terminal interface. | vt, escape-sequence, cursor-control, vpa, cup |

### 12. VT CSI - Position Relative (070-072)
*CSI sequences for relative cursor positioning*

| # | File | Title | Summary | Keywords |
|---|------|-------|---------|----------|
| 070 | `070-docs-vt-csi-hpr.md` | Horizontal Position Relative (HPR) - CSI | This document explains the function and control sequence for the Horizontal Position Reply (HPR) terminal command. | terminal-control, cursor-movement, hpr, ansi-escape-codes, cup-invocation |
| 071 | `071-docs-vt-csi-vpr.md` | Vertical Position Relative (VPR) - CSI | This document describes the VT sequence VPR, which moves the cursor vertically by a specified relative amount. | vt-sequence, cursor-movement, vpr, terminal-control, escape-codes |
| 072 | `072-docs-vt-csi-rep.md` | Repeat (REP) - CSI | This document explains the Repeat Previous Character (REP) control sequence, detailing its structure and parameter constraints. | terminal-control, csi-sequence, character-repetition, ansi-escape-codes, rep |

### 13. VT CSI - Erase & Delete (073-081)
*CSI sequences for erasing and deleting content*

| # | File | Title | Summary | Keywords |
|---|------|-------|---------|----------|
| 073 | `073-docs-vt-csi-ed.md` | Erase in Display (ED) - CSI | This document describes the Control Sequence Introducer (CSI) command used to erase display contents. | erase-display, csi-sequence, terminal-control, cursor-position, scrollback |
| 074 | `074-docs-vt-csi-el.md` | Erase in Line (EL) - CSI | This document details the behavior of the ANSI Escape Sequence CSI n K (EL), which is used to erase content on the current line. | ansi-escape-sequences, terminal-control, erase-line, csi, el |
| 075 | `075-docs-vt-csi-ech.md` | Erase Character (ECH) - CSI | This document explains the behavior of the Erase in Character (ECH) Control Sequence, specifically how it blanks cells to the right of the cursor. | ech, erase-in-character, terminal-sequence, sgr-state, protected-attributes, decsca |
| 076 | `076-docs-vt-csi-ich.md` | Insert Character (ICH) - CSI | This document details the use of the Insert Character (ICH) Control Sequence, which inserts a specified number of blank characters at the current cursor position. | csi, ich, terminal-control, cursor-manipulation, escape-sequences, sgr |
| 077 | `077-docs-vt-csi-dch.md` | Delete Character (DCH) - CSI | This document details the ANSI escape sequence used to delete $n$ characters at the current cursor position. | ansi-escape-sequence, delete-character, terminal-control, cursor-movement, scroll-region |
| 078 | `078-docs-vt-csi-il.md` | Insert Line (IL) - CSI | This document describes the ANSI escape sequence 'Insert Line' (IL), which inserts specified blank lines at the current cursor position. | ansi-escape-sequences, insert-line, csi, cursor-manipulation, scroll-region |
| 079 | `079-docs-vt-csi-dl.md` | Delete Line (DL) - CSI | This document describes the Delete Line (DL) control sequence, which removes a specified number of lines at the cursor position. | delete-line, csi-sequence, terminal-control, cursor-manipulation, scroll-region |
| 080 | `080-docs-vt-csi-su.md` | Scroll Up (SU) - CSI | This document explains the usage of the terminal control sequence (CSI) 'SU' (Scroll Up), which removes a specified number of lines from the top of the scroll region. | terminal, control-sequence, csi, scroll-up, su, line-manipulation |
| 081 | `081-docs-vt-csi-sd.md` | Scroll Down (SD) - CSI | This document details the terminal control sequence 'SD' (Scroll Down), which inserts 'n' lines at the top of the current scroll region. | terminal-sequence, csi, scroll-down, line-insertion, vt100 |

### 14. VT CSI - Margins & Scrolling (082-085)
*CSI sequences for scroll regions and margins*

| # | File | Title | Summary | Keywords |
|---|------|-------|---------|----------|
| 082 | `082-docs-vt-csi-decstbm.md` | Set Top and Bottom Margins (DECSTBM) - CSI | This document explains the ANSI/VT escape sequence DECSTBM used to set the top and bottom margins, defining the terminal's scroll region. | ansi-escape-sequence, terminal-control, decstbm, scroll-region, cursor-movement |
| 083 | `083-docs-vt-csi-decslrm.md` | Set Left and Right Margins (DECSLRM) - CSI | This document explains the control sequence used to set the left and right margins (scroll region) in a terminal environment. | terminal-control, scroll-region, decslrm, ansi-escape-sequences, cursor-positioning |
| 084 | `084-docs-vt-csi-tbc.md` | Tab Clear (TBC) - CSI | This document explains how to use the ANSI escape sequence CSI ? n g to clear one or all terminal tab stops. | ansi-escape-sequence, tab-stops, terminal-control, csi-command |
| 085 | `085-docs-vt-csi-dsr.md` | Device Status Report (DSR) - CSI | This document explains how to use Control Sequence Introducers (CSI) sequences, specifically Device Status Reports (DSR), to request status information. | terminal-control, csi-sequences, device-status-report, operating-status, cursor-position |

### 15. VT CSI - Cursor Style & Misc (086-087)
*CSI sequences for cursor styling and miscellaneous control*

| # | File | Title | Summary | Keywords |
|---|------|-------|---------|----------|
| 086 | `086-docs-vt-csi-decscusr.md` | Set Cursor Style (DECSCUSR) - CSI | This document details the ANSI escape sequence used to set the cursor style in a terminal, specifying the meaning of the optional parameter 'n'. | ansi-escape-sequences, cursor-style, terminal-control, decscusr |
| 087 | `087-docs-vt-csi-xtshiftescape.md` | Shift-Escape Behavior (XTSHIFTESCAPE) - CSI | This document explains how to use the XTSHIFTESCAPE sequence to configure whether the terminal allows mouse reports to capture the shift modifier. | terminal-control, mouse-reporting, shift-modifier, xterm-configuration, xtshiftescape |

### 16. VT OSC - Window (088-091)
*OSC sequences for window control*

| # | File | Title | Summary | Keywords |
|---|------|-------|---------|----------|
| 088 | `088-docs-vt-osc-0.md` | Change Window Icon and Title (OSC 0) - OSC | This document details the byte sequences for control characters and explains that the specific sequence 0x1B 0x5C maps to an alias for the Change Window Title OSC. | control-characters, byte-sequence, osc-command, alias, terminal-emulator |
| 089 | `089-docs-vt-osc-1.md` | Change Window Icon (OSC 1) - OSC | This document outlines the sequence of control characters (OSC 1) used to attempt to change the name of the window icon. | terminal, osc-1, window-icon, control-sequence, platform-dependence |
| 090 | `090-docs-vt-osc-2.md` | Change Window Title (OSC 2) - OSC | This document outlines the specific sequence of control codes (OSC 2) required to change the window title in a terminal environment. | terminal-control, osc-sequence, window-title, ansi-escape-codes, utf-8 |
| 091 | `091-docs-vt-osc-7.md` | Change Working Directory (OSC 7) - OSC | This document describes the control sequence used by terminal emulators to signal a change in the current working directory to an integrated shell. | terminal-control, current-working-directory, osc-sequence, shell-integration, uri-navigation |

### 17. VT OSC - Colors (092-097)
*OSC sequences for color manipulation*

| # | File | Title | Summary | Keywords |
|---|------|-------|---------|----------|
| 092 | `092-docs-vt-osc-4.md` | Query or Change Palette Colors (OSC 4) - OSC | This document explains the use of the operating system command (OSC) sequence 4 for querying and modifying colors within the terminal's palette. | terminal-control, osc-sequence-4, color-palette, color-query, ansi-escape-codes |
| 093 | `093-docs-vt-osc-5.md` | Query or Change Special Colors (OSC 5) - OSC | This document explains the usage of an escape sequence for querying or changing the five special terminal colors. | terminal-control, escape-sequence, special-colors, osc, color-manipulation |
| 094 | `094-docs-vt-osc-1x.md` | Query or Change Dynamic Colors (OSC 10–19) - OSC | This document describes how to query or change dynamic terminal colors based on a specific sequence structure involving an index 'n' (10-19). | dynamic-colors, terminal-control, osc, ansi-escape-sequence, color-specification |
| 095 | `095-docs-vt-osc-104.md` | Reset Palette Colors (OSC 104) - OSC | This document explains the sequence of escape codes used to reset colors within a terminal palette. | terminal, escape-codes, color-palette, osc-104, ansi |
| 096 | `096-docs-vt-osc-105.md` | Reset Special Colors (OSC 105) - OSC | This document details the structure and function of OSC sequence 105, which is used to reset special terminal colors. | osc-105, terminal-control, color-reset, escape-sequences, ansi |
| 097 | `097-docs-vt-osc-11x.md` | Reset Dynamic Colors (OSC 110–119) - OSC | This document explains the use of the OSC sequence 11x to reset specific dynamic colors based on the numerical index provided. | osc-sequence, dynamic-colors, color-reset, terminal-control |

### 18. VT OSC - Clipboard & Notifications (098-101)
*OSC sequences for clipboard and desktop notifications*

| # | File | Title | Summary | Keywords |
|---|------|-------|---------|----------|
| 098 | `098-docs-vt-osc-52.md` | Query or Change Clipboard Data (OSC 52) - OSC | This document explains the format and behavior of OSC 52 sequences used to query or change data associated with various system clipboards. | osc-52, clipboard, terminal-control, xterm-sequence, data-query, data-setting |
| 099 | `099-docs-vt-osc-9.md` | Show Desktop Notification (OSC 9) - OSC | This document details the use of OSC 9 sequences for displaying desktop notifications, including a special consideration for avoiding conflicts with ConEmu extensions. | desktop-notification, osc-9, terminal-escape-sequence, conemu-conflict, ghostty |
| 100 | `100-docs-vt-osc-22.md` | Change Pointer Shape (OSC 22) - OSC | This document details the use of Operating System Command (OSC) sequence 22 to change the terminal pointer shape. | terminal-control, osc-sequence, pointer-shape, cursor-control, terminal-emulation |
| 101 | `101-docs-vt-osc-conemu.md` | ConEmu Extensions (OSC 9;n) - OSC | This document details how the Ghostty terminal emulator handles and resolves conflicts with custom protocols, specifically those pioneered by ConEmu using OSC 9. | conemu, osc-9, custom-protocols, ghostty, terminal-emulator, progress-state |

---

## Quick Reference

### By Topic

| Topic | File Range |
|-------|------------|
| **Getting Started** | 001-005 |
| **Installation** | 006-011 |
| **Release History** | 012-022 |
| **Features** | 023-026 |
| **Configuration** | 027-031 |
| **Troubleshooting** | 032-038 |
| **VT API Overview** | 039-041 |
| **VT Concepts** | 042-045 |
| **VT Control** | 046-050 |
| **VT ESC** | 051-058 |
| **VT CSI** | 059-087 |
| **VT OSC** | 088-101 |

### By Concept

| Concept | Files |
|---------|-------|
| **Cursor Movement** | 044, 047-050, 059-072, 086 |
| **Colors** | 043, 092-097 |
| **Scrolling & Margins** | 080-083 |
| **Erasing & Deleting** | 073-081 |
| **Window Control** | 088-091 |
| **Clipboard** | 098 |
| **Notifications** | 099, 101 |

---

## Learning Path

### Level 1: Foundation (Start Here)
- Read files **001-005** for introduction and overview
- Complete files **006-011** for installation guides

### Level 2: Core Understanding
- Learn configuration from files **027-031**
- Explore features in files **023-026**
- Review release notes in files **012-022**

### Level 3: Practical Application
- Configure themes with file **024**
- Set up keybindings with files **028-030**
- Integrate shell with file **025**

### Level 4: Advanced Usage
- Master terminal API with files **039-041**
- Learn VT concepts from files **042-045**
- Implement control sequences from files **046-087**

### Level 5: Reference & Support
- Consult VT reference docs **040, 042-101**
- Review troubleshooting guides **032-038**
- Check VT CSI/OSC sequences as needed

---

*This index is auto-generated and optimized for AI agent search. Files are numbered sequentially following a logical learning progression adapted to the Ghostty documentation structure.*