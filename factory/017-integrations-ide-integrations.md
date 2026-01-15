---
title: IDE Integrations - Factory Documentation
url: https://docs.factory.ai/integrations/ide-integrations
source: sitemap
fetched_at: 2026-01-13T19:04:28.269068227-03:00
rendered_js: false
word_count: 808
summary: Explains how to install, configure, and troubleshoot Droid IDE extensions for Visual Studio Code and JetBrains, including features like diff viewing, diagnostic sharing, and context awareness.
tags:
    - ide-integration
    - vs-code
    - jetbrains
    - installation
    - troubleshooting
    - developer-tools
    - plugins
category: configuration
---

Droid works great with any Integrated Development Environment (IDE) that has a terminal. Just run `droid`, and you’re ready to go. In addition, Droid provides dedicated plugins for both Visual Studio Code (including popular forks like Cursor, Windsurf, and VSCodium) and JetBrains IDEs. For JetBrains IDEs such as IntelliJ IDEA, PyCharm, Android Studio, WebStorm, PhpStorm, and GoLand, you can either install the official Factory Droid plugin for enhanced integration or simply run `droid` in the integrated terminal.

## Features

- **Quick launch**: Use keyboard shortcuts to open Droid directly from your editor, or click the Droid button in the UI
- **Diff viewing**: Code changes can be displayed directly in the IDE diff viewer instead of the terminal
- **Selection context**: The current selection/tab in the IDE is automatically shared with Droid
- **File reference shortcuts**: Use keyboard shortcuts to insert file references
- **Diagnostic sharing**: Diagnostic errors (lint, syntax, etc.) from the IDE are automatically shared with Droid as you work

## Installation

### VS Code

To install Droid on VS Code and popular forks like Cursor, Windsurf, and VSCodium:

1. Open VS Code
2. Open the integrated terminal
3. Run `droid` - the extension will auto-install

### JetBrains IDEs (IntelliJ IDEA, PyCharm, WebStorm, etc.)

Factory provides two ways to work with JetBrains IDEs:

1. **Dedicated Plugin**: [Install the official Factory Droid plugin](https://plugins.jetbrains.com/plugin/28649-factory-droid) from the JetBrains Marketplace for enhanced IDE integration
2. **Terminal Integration**: Run `droid` in the integrated terminal (no plugin required)

**Supported JetBrains IDEs:**

- IntelliJ IDEA (Ultimate and Community)
- PyCharm (Professional and Community)
- WebStorm
- PhpStorm
- Android Studio
- GoLand
- CLion
- RubyMine
- DataGrip
- Rider

#### Option 1: Install the Factory Droid Plugin (Recommended)

1. Open your JetBrains IDE
2. Go to **Settings/Preferences** → **Plugins**
3. Click the **Marketplace** tab
4. Search for “Factory Droid”
5. Click **Install** on the Factory Droid plugin
6. Restart your IDE when prompted
7. The Factory Droid toolbar will appear - click it to launch

![Factory Droid plugin in IntelliJ IDEA](https://mintcdn.com/factory/c8NJRDPUbEO7dzm3/images/intellij.png?fit=max&auto=format&n=c8NJRDPUbEO7dzm3&q=85&s=8f0205daf9b4276cf2061e8fd17e2926)

#### Option 2: Terminal Integration

1. Open your JetBrains IDE
2. Open the integrated terminal (`Alt+F12` on Windows/Linux, `Option+F12` on macOS)
3. Navigate to your project root directory
4. Run `droid` - all Factory features will be automatically available

**Plugin Features (Option 1):**

- **Toolbar Integration**: Launch Factory Droid directly from the IDE toolbar
- **MCP-powered Context**: Secure context sharing with awareness of files you’re editing
- **Real-time Diagnostics**: View compiler errors and warnings shared with Droid
- **Diff Visualization**: Review proposed changes before applying them
- **Seamless CLI Integration**: Run tasks locally or in cloud sandboxes
- **Enhanced Security**: Enterprise-grade guardrails for team collaboration

**Terminal Integration Features (Option 2):**

- **Project Context**: Droid automatically understands your project structure and build configuration
- **File Navigation**: Quick file references and code exploration work seamlessly
- **Multi-language Support**: Full support for all languages supported by your JetBrains IDE

## Usage

### From your IDE

Run `droid` from your IDE’s integrated terminal, and all features will be active.

### The `/ide` Command

Use the `/ide` command within droid to manage your IDE integrations:

This command will:

- Show the current extension version if installed
- Prompt to install the extension if not yet installed
- Works with VS Code, Cursor, and Windsurf

## Troubleshooting

### VS Code extension not installing

- Ensure you’re running Droid from VS Code’s integrated terminal
- Ensure that the CLI corresponding to your IDE is installed:
  
  - For VS Code: `code` command should be available
  - For Cursor: `cursor` command should be available
  - For Windsurf: `windsurf` command should be available
  - For VSCodium: `codium` command should be available
  - If not installed, use `Cmd+Shift+P` (Mac) or `Ctrl+Shift+P` (Windows/Linux) and search for “Shell Command: Install ‘code’ command in PATH” (or the equivalent for your IDE)
- Check that VS Code has permission to install extensions

### JetBrains/IntelliJ terminal issues

- Ensure you’re running Droid from the project root directory
- Use the integrated terminal inside the IDE rather than an external shell
- Completely restart the IDE if terminal state issues persist
- **For IntelliJ IDEA**: Make sure the terminal is using your system shell (not the embedded terminal)
- **Project SDK**: Ensure your project SDK is properly configured if using language-specific features
- **Terminal Settings**: Go to Settings → Tools → Terminal and verify shell path is correct

### ESC key configuration

If the ESC key doesn’t interrupt Droid operations in JetBrains terminals:

1. Go to Settings → Tools → Terminal
2. Either:
   
   - Uncheck “Move focus to the editor with Escape”, or
   - Click “Configure terminal keybindings” and delete the “Switch focus to Editor” shortcut
3. Apply the changes

This allows the ESC key to properly interrupt Droid operations.

### Common issues

SymptomFix**”Editor integration disabled” message**Verify the VS Code extension is installed or update `editorIntegration` to match your editorCLI cannot find Node/BunEnsure the `droid` binary is on the PATH VS Code/JetBrains uses (restart after install)Missing file contextSave files; unsaved buffers older than 500 KB are skipped for performanceStale diagnosticsRun **↻ Refresh Diagnostics** command (VS Code Command Palette)VS Code terminal closes immediatelyCheck your shell’s startup scripts: they must not auto-exitNetwork blocked in corporate proxyConfigure proxy variables in settings or set `HTTP_PROXY`/`HTTPS_PROXY` env vars

For additional help, email [support@factory.ai](mailto:support@factory.ai) with logs from `~/.factory/logs/`

## Next steps