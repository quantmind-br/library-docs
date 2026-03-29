---
title: ForgeCode
url: https://forgecode.dev/docs/vscode-extension/
source: sitemap
fetched_at: 2026-03-29T14:52:29.885243142-03:00
rendered_js: false
word_count: 1182
summary: Documentation for a VS Code extension that integrates with ForgeCode CLI to enable quick code referencing and direct session launching from the editor.
tags:
    - vscode-extension
    - forgecode
    - code-reference
    - keyboard-shortcuts
    - terminal-integration
    - file-paths
    - code-snippets
category: guide
---

Tired of manually typing file paths and copying code snippets when asking ForgeCode for help? This VS Code extension lets you reference any code with a single keystroke and start ForgeCode sessions directly from your editor.

**The problem:** Describing code problems is slow and unclear

- "That function around line 50 something..."
- Copy-pasting code snippets manually
- Typing out long file paths

**The solution:** Show ForgeCode exactly what you mean

- Select any code → Press `Ctrl+U` → Get a perfect reference
- Works with single lines, code blocks, or entire files

Prerequisite: ForgeCode CLI

This extension works with [ForgeCode CLI](https://forgecode.dev/docs/). Install that first if you haven't already.

![ForgeCode VS Code Extension Demo](https://forgecode.dev/assets/images/demo_vscode-91e033a7be71f6d1283957a4689f6479.gif)

**What you just saw:** Select code → Press `Ctrl+U` → Reference copied and ready to use with ForgeCode.

### What You Need[​](#what-you-need "Direct link to What You Need")

- **VS Code**: Version 1.102.0 or higher
- **ForgeCode CLI**: [Install](https://forgecode.dev/docs/) it first if you haven't already

### Install the Extension[​](#install-the-extension "Direct link to Install the Extension")

**Option 1: VS Code Marketplace (Recommended)**

1. Open VS Code
2. Press `Ctrl+Shift+X` to open Extensions panel
3. Search for **"ForgeCode"**
4. Click **Install** on the official ForgeCode extension

**Option 2: Command Line**

**Test that it works:** Open any code file, select some text, press `Ctrl+U`. If a file reference gets copied to your clipboard, you're ready to go!

**Official extension:** [VS Code Marketplace](https://marketplace.visualstudio.com/items?itemName=ForgeCode.forge-vscode)

### The Core Workflow[​](#the-core-workflow "Direct link to The Core Workflow")

1. **Select code** (or don't select anything for whole file)
2. **Press `Ctrl+U`**
3. **Paste into ForgeCode** conversation

That's it. No typing, no manual copying.

**What gets copied:**

Format: `@[<filepath>:<line start>:<line end>]`

**How selection works:**

- **No selection**: `@[path/to/file.js]` → References entire file
- **Single line**: `@[path/to/file.js:42:42]` → References line 42 only
- **Multiple lines**: `@[path/to/file.js:15:28]` → References lines 15-28

### Power Move: Multi-File References[​](#power-move-multi-file-references "Direct link to Power Move: Multi-File References")

Here's the real power move. You can reference multiple files in a single ForgeCode prompt by copying and pasting references one at a time:

**Example:**

Now ForgeCode can see exactly what code you're talking about, with full context and precise line numbers. No more "that function around line 50 something" conversations.

**Alternative ways to copy:**

- **Command Palette**: `Ctrl+Shift+P` → type "Copy File Reference"
- **Right-click Menu**: Select code → right-click → "Copy File Reference"

### Start New ForgeCode Session[​](#start-new-forgecode-session "Direct link to Start New ForgeCode Session")

Start a ForgeCode terminal directly in VS Code without switching windows.

**How to use:**

- **Command Palette**: `Ctrl+Shift+P` → type "Start New ForgeCode Session"
- **Right-click Menu**: Right-click in any file → "Start New ForgeCode Session"
- **Editor Toolbar**: Click the ForgeCode icon in the top-right of the editor

The extension will:

1. Create a new integrated terminal in VS Code
2. Navigate to your workspace directory
3. Start ForgeCode automatically
4. Auto-paste any file reference from the current editor (if open)

### Debugging Issues[​](#debugging-issues "Direct link to Debugging Issues")

**Scenario:** Authentication fails in production but works locally.

ForgeCode sees the exact code and can suggest environment-specific issues to check.

### Code Reviews[​](#code-reviews "Direct link to Code Reviews")

**Scenario:** You spot a component that could be improved.

Instead of generic advice, ForgeCode sees your specific component and suggests targeted improvements.

### Type Mismatches[​](#type-mismatches "Direct link to Type Mismatches")

**Scenario:** API data doesn't match your TypeScript types.

ForgeCode compares both files simultaneously and suggests proper fixes.

### Feature Implementation[​](#feature-implementation "Direct link to Feature Implementation")

**Scenario:** Adding dark mode across multiple components.

ForgeCode understands your theme system and suggests consistent changes across files.

The extension provides several settings to customize its behavior. Access settings via **File → Preferences → Settings → Extensions → ForgeCode**.

### Available Settings[​](#available-settings "Direct link to Available Settings")

#### `forge.terminalMode`[​](#forgeterminalmode "Direct link to forgeterminalmode")

Controls terminal interaction when copying file references with `Ctrl+U`.

- **Type**: String (dropdown)
- **Options**:
  
  - `once` (default): Open terminal once and reuse it for subsequent operations
  - `never`: Never open terminal, only copy file reference to clipboard
- **Default**: `once`

**When to use `once`:** Most users should use this. The extension intelligently manages ForgeCode terminals, creating one when needed and reusing it for subsequent file references.

**When to use `never`:** Use this if you always work with ForgeCode in an external terminal and only want the extension to copy file references to clipboard without any terminal interaction.

#### `forge.pasteDelay`[​](#forgepastedelay "Direct link to forgepastedelay")

Delay in milliseconds before auto-pasting file reference into a newly created ForgeCode terminal.

- **Type**: Number
- **Default**: `5000` (5 seconds)
- **Range**: 0-10000 milliseconds

**Why this exists:** When the extension creates a new ForgeCode terminal, it needs time to start up before accepting input. This delay ensures the file reference is pasted after ForgeCode is ready.

**When to adjust:**

- If file references aren't being pasted: Increase the value (try 7000-10000ms)
- If you have a fast machine and want quicker pasting: Decrease the value (try 3000-4000ms)
- Note: This only affects newly created terminals, not existing ones

#### `forge.showInstallationPrompt`[​](#forgeshowinstallationprompt "Direct link to forgeshowinstallationprompt")

Show a prompt to install ForgeCode CLI if it's not detected in your PATH.

- **Type**: Boolean
- **Default**: `true`

**When to disable:** If you use ForgeCode via `npx` or have it installed in a non-standard location, you might want to disable this prompt.

### Extension Not Working[​](#extension-not-working "Direct link to Extension Not Working")

**Quick fixes to try:**

1. Verify ForgeCode CLI is installed - run `forge --version` in terminal
2. Check your VS Code version (Help → About) - need 1.102.0+
3. Verify the extension is enabled in Extensions view (`Ctrl+Shift+X`)
4. Restart VS Code completely

### Keyboard Shortcut Not Working[​](#keyboard-shortcut-not-working "Direct link to Keyboard Shortcut Not Working")

**`Ctrl+U` does nothing:**

This usually means another extension grabbed that shortcut. Here's how to fix it:

1. **File → Preferences → Keyboard Shortcuts**
2. Search for **"ForgeCode"** or **"Copy File Reference"**
3. Click the pencil icon next to "Copy File Reference"
4. Pick a new combo like `Ctrl+Shift+U` or `Alt+U`

**Common culprits:** Vim extensions, browser preview extensions, other developer tools.

### Nothing Gets Copied to Clipboard[​](#nothing-gets-copied-to-clipboard "Direct link to Nothing Gets Copied to Clipboard")

Try these workarounds:

- Use Command Palette: `Ctrl+Shift+P` → "Copy File Reference"
- Use right-click menu → "Copy File Reference"
- Check if you're in a text file (extension won't work on images/binaries)
- Some systems have clipboard permission issues - restart VS Code usually fixes this

### Terminal Not Opening or ForgeCode Not Starting[​](#terminal-not-opening-or-forgecode-not-starting "Direct link to Terminal Not Opening or ForgeCode Not Starting")

**If "Start New ForgeCode Session" doesn't work:**

1. Check that ForgeCode is in your PATH - run `which forge` (macOS/Linux) or `where forge` (Windows) in terminal
2. Verify ForgeCode is installed by running `forge --version`
3. Restart VS Code after installing ForgeCode

**If file references aren't being pasted automatically:**

- Increase the `forge.pasteDelay` setting (try 7000-10000ms for slower machines)
- The default is 5000ms (5 seconds) - if that's not enough, ForgeCode may need more time to start
- Check that your terminal shell is compatible (bash, zsh, PowerShell work well)
- Try using `Ctrl+U` to copy the reference, then manually paste it into the ForgeCode terminal

### Weird File Paths[​](#weird-file-paths "Direct link to Weird File Paths")

Sometimes you'll see paths like `/workspaces/project/src/file.js` instead of normal ones.

**This is actually fine.** VS Code uses different path formats for remote development, containers, and workspace setups. ForgeCode handles these correctly, so don't worry about how they look.

**Start small:** Reference one function, ask ForgeCode about it, see how it responds. Then level up to multi-file references.

**Be selective:** Don't dump entire files unless you actually need context from the whole thing. ForgeCode works better with focused references.

**Combine with descriptions:** `@[component.tsx:45:67] this validation logic isn't working with empty strings` gives ForgeCode both code and context.

You're ready to start using the extension! The goal isn't to reference every line of code - it's to give ForgeCode just enough context to actually help with your specific situation.

- [File Tagging](https://forgecode.dev/docs/file-tagging/)
- [Quickstart: Get started with ForgeCode in minutes](https://forgecode.dev/docs/)

* * *

**If you're still stuck:**

- **Extension logs:** View → Output → Select "ForgeCode" from dropdown
- **Report bugs:** [GitHub Issues](https://github.com/antinomyhq/forge/issues)
- **Community help:** Join our [Discord](https://discord.gg/kRZBPpkgwq) for quick answers