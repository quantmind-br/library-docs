---
description: Auto-generated documentation index
generated: 2026-02-04T15:46:26Z
source: https://github.com/tmux/tmux/wiki/
total_docs: 11
categories: 8
---

# tmux Documentation Index

> Organized index for AI agent consumption. Documents follow logical learning sequence for mastering tmux terminal multiplexer.

## Metadata Summary

| Property | Value |
|----------|-------|
| **Source** | https://github.com/tmux/tmux/wiki/ |
| **Generated** | 2026-02-04T15:46:26Z |
| **Total Documents** | 11 |
| **Categories** | 8 |

---

## Document Index

### 1. Introduction & Overview (001)
*Entry point for understanding tmux and its capabilities*

| # | File | Title | Summary | Keywords |
|---|------|-------|---------|----------|
| 001 | `001-index.md` | Home | Introduces tmux, a terminal multiplexer, and provides a centralized index of links for installation, documentation, support, and contribution. | tmux, terminal-multiplexer, cli-tools, documentation-index, open-source |

### 2. Quick Start & Installation (002-003)
*Get up and running with tmux quickly*

| # | File | Title | Summary | Keywords |
|---|------|-------|---------|----------|
| 002 | `002-getting-started.md` | Getting Started | Provides an introductory overview of tmux, detailing its server-client architecture and the organizational hierarchy of sessions, windows, and panes. | tmux, terminal-multiplexer, session-management, cli-tools, unix-utilities |
| 003 | `003-installing.md` | Installing | Provides comprehensive instructions for installing tmux on various platforms using package managers, prebuilt binaries, or by compiling from source. | tmux, installation-guide, linux-administration, compilation, package-management, macos |

### 3. Configuration & Customization (004-006)
*Customize tmux behavior and appearance*

| # | File | Title | Summary | Keywords |
|---|------|-------|---------|----------|
| 004 | `004-modifier-keys.md` | Modifier Keys | Explains how tmux interprets modifier keys and escape sequences from terminal emulators and provides guidance on configuring extended key support. | tmux, terminal-emulators, modifier-keys, keyboard-shortcuts, troubleshooting, extended-keys |
| 005 | `005-formats.md` | Formats | Explains how to use tmux formats and directives to customize command output, status lines, and configuration logic with variable expansion, string modifiers, and substitutions. | tmux, terminal-multiplexer, text-formatting, string-manipulation, cli-tools, configuration-syntax |
| 006 | `006-recipes.md` | Recipes | Provides a collection of configuration snippets and key binding recipes to customize tmux behavior for pane management, mouse interaction, and session navigation. | tmux-config, key-bindings, terminal-multiplexer, pane-management, workflow-optimization, shell-scripting |

### 4. Features & Integration (007)
*Integrate tmux with system features*

| # | File | Title | Summary | Keywords |
|---|------|-------|---------|----------|
| 007 | `007-clipboard.md` | Clipboard | Explains how to synchronize the tmux internal clipboard with the system clipboard using OSC 52 escape sequences or external piping utilities. | tmux, clipboard-synchronization, osc-52, terminal-configuration, set-clipboard, unix-shell |

### 5. Advanced Topics (008)
*Master advanced tmux features*

| # | File | Title | Summary | Keywords |
|---|------|-------|---------|----------|
| 008 | `008-advanced-use.md` | Advanced Use | Explains advanced tmux features including server socket management, pane monitoring for activity or silence, and handling working directories and window dimensions. | tmux-configuration, terminal-multiplexer, socket-management, pane-monitoring, window-management, session-scripting |

### 6. Technical Reference (009)
*Protocol and interface documentation*

| # | File | Title | Summary | Keywords |
|---|------|-------|---------|----------|
| 009 | `009-control-mode.md` | Control Mode | Explains tmux control mode, a text-only protocol that enables external applications to interface with and manage tmux sessions through standard commands and asynchronous notifications. | tmux, control-mode, terminal-protocol, iterm2-integration, session-management, cli-interface |

### 7. Support & Troubleshooting (010)
*Find help and solve problems*

| # | File | Title | Summary | Keywords |
|---|------|-------|---------|----------|
| 010 | `010-faq.md` | FAQ | Provides a collection of frequently asked questions and troubleshooting steps for tmux, covering terminal settings, color support, and basic configuration. | tmux, terminal-multiplexer, troubleshooting, configuration, environment-variables, faq |

### 8. Meta & Resources (011)
*Contribute and explore development*

| # | File | Title | Summary | Keywords |
|---|------|-------|---------|----------|
| 011 | `011-contributing.md` | Contributing | Outlines the tmux development process, including source code management, release cycles, and a roadmap of planned features and documentation improvements. | tmux, open-source-development, software-releases, contributor-guidelines, feature-roadmap, openbsd |

---

## Quick Reference

### By Topic

| Topic | File Range |
|-------|------------|
| **Getting Started** | 001-003 |
| **Configuration** | 004-006 |
| **Clipboard Integration** | 007 |
| **Advanced Features** | 008-009 |
| **Troubleshooting** | 010 |
| **Development** | 011 |

### By Concept

| Concept | Files |
|---------|-------|
| **Session Management** | 001, 002, 008, 009 |
| **Configuration** | 004, 005, 006, 010 |
| **Keyboard & Input** | 004 |
| **System Integration** | 007 |
| **Automation & Scripting** | 005, 006, 008, 009 |

### By Common Tasks

| Task | Files |
|------|-------|
| **Install tmux** | 003 |
| **First-time setup** | 002, 003 |
| **Customize keybindings** | 004, 006 |
| **Configure status line** | 005, 006 |
| **Enable clipboard** | 007 |
| **Automate workflows** | 005, 006, 008 |
| **Build integrations** | 009 |
| **Troubleshoot issues** | 010 |
| **Contribute to tmux** | 011 |

---

## Learning Path

### Level 1: Foundation (Start Here)
- Read file **001** for introduction and overview of tmux
- Complete files **002-003** for quick start and installation

**Goal**: Understand what tmux is, install it, and learn basic concepts (sessions, windows, panes)

### Level 2: Core Understanding
- Learn keyboard configuration from file **004**
- Understand format syntax from file **005**
- Apply practical recipes from file **006**

**Goal**: Configure tmux behavior, customize status lines, and optimize workflow

### Level 3: Practical Application
- Explore clipboard integration in file **007**
- Master advanced features in file **008**
- Learn control mode protocol in file **009**

**Goal**: Integrate tmux with system tools, automate tasks, and build external integrations

### Level 4: Reference & Support
- Consult FAQ in file **010** for troubleshooting
- Review contributing guidelines in file **011** for development

**Goal**: Solve common issues and understand how to contribute to tmux development

---

## Key Topics Coverage

### Architecture & Concepts
- **Server-client model** (files 002, 008)
- **Sessions, windows, panes hierarchy** (file 002)
- **Socket management** (file 008)

### Configuration
- **Key bindings** (files 004, 006)
- **Format strings** (file 005)
- **Status line customization** (files 005, 006)
- **Mouse support** (file 006)

### Integration
- **Clipboard synchronization** (file 007)
- **Control mode protocol** (file 009)
- **Terminal emulator compatibility** (file 004)

### Automation
- **Scripting** (files 006, 008)
- **Pane monitoring** (file 008)
- **Working directory management** (file 008)

### Platform Support
- **Linux** (file 003)
- **macOS** (file 003)
- **OpenBSD** (files 003, 011)
- **Package managers** (file 003)

---

*This index is auto-generated and optimized for AI agent search. Files are numbered sequentially following a logical learning progression from basic concepts to advanced topics.*
