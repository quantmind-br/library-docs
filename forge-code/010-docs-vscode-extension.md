---
title: "VS Code Extension for ForgeCode"
url: https://forgecode.dev/docs/vscode-extension/
source: sitemap
fetched_at: 2026-04-30T14:09:19.635442685-03:00
rendered_js: false
word_count: 376
summary: "Reference code snippets and manage ForgeCode sessions directly from VS Code with precise file references."
tags:
  - vscode-extension
  - developer-tools
  - code-referencing
  - workflow-automation
  - productivity
  - ide-integration
category: guide
optimized: true
---
# VS Code Extension for ForgeCode

> **TL;DR**
> Select code → `Ctrl+U` → Paste reference into ForgeCode. Start sessions directly from VS Code.

## Why Use the Extension?
- **Precision**: Reference exact lines/blocks, not "around line 50."
- **Speed**: No manual copying/pasting.
- **Context**: ForgeCode sees your code directly.

## Installation

### Prerequisites
- VS Code ≥1.102.0
- [ForgeCode CLI](https://forgecode.dev/docs/)

### Steps
1. Open VS Code.
2. `Ctrl+Shift+X` → Search "ForgeCode" → Install.
3. Test: Select code → `Ctrl+U` → Check clipboard.

> **Marketplace**: [VS Code Marketplace](https://marketplace.visualstudio.com/items?itemName=ForgeCode.forge-vscode)

## Core Workflow

1. **Select code** (or none for whole file).
2. **`Ctrl+U`** → Copies reference (e.g., `@[file.js:15:28]`).
3. **Paste** into ForgeCode.

### Reference Formats
| Selection | Format | Example |
|-----------|--------|---------|
| No selection | `@[file.js]` | Entire file |
| Single line | `@[file.js:42:42]` | Line 42 |
| Multi-line | `@[file.js:15:28]` | Lines 15–28 |

## Advanced Features

### Multi-File References
Copy/paste multiple references for cross-file context:
```plaintext
@[api.ts:10:25] @[ui.tsx:30:40]
```

### Start ForgeCode Session
- **Command Palette**: `Ctrl+Shift+P` → "Start New ForgeCode Session"
- **Right-click**: "Start New ForgeCode Session"
- **Toolbar**: Click ForgeCode icon (top-right)

> **Action**: Opens terminal, navigates to workspace, starts ForgeCode, auto-pastes reference.

## Settings

| Setting | Purpose | Default |
|---------|---------|---------|
| `forge.terminalMode` | Terminal behavior (`once`/`never`) | `once` |
| `forge.pasteDelay` | Auto-paste delay (ms) | `5000` |
| `forge.showInstallationPrompt` | Show CLI install prompt | `true` |

### `forge.terminalMode`
- **`once`**: Reuse terminal (default).
- **`never`**: Copy only (no terminal).

### `forge.pasteDelay`
- Increase if references aren’t pasted (e.g., `7000`).
- Decrease for faster machines (e.g., `3000`).

## Troubleshooting

| Issue | Solution |
|-------|----------|
| `Ctrl+U` does nothing | Rebind shortcut or use Command Palette/right-click. |
| Nothing copied | Check file type (text only), restart VS Code. |
| Terminal not opening | Verify `forge` in PATH, restart VS Code. |
| Weird paths | Normal for remote/VS Code workspaces; ForgeCode handles them. |

## Best Practices
- **Start small**: Reference one function first.
- **Be selective**: Focus references on relevant code.
- **Combine**: Add descriptions (e.g., `@[file.js:10:20] this logic fails for empty inputs`).

## Related Guides
- [File Tagging](https://forgecode.dev/docs/file-tagging/)
- [Quickstart](https://forgecode.dev/docs/)

## Support
- **Logs**: View → Output → "ForgeCode"
- **Bugs**: [GitHub Issues](https://github.com/antinomyhq/forge/issues)
- **Help**: [Discord](https://discord.gg/kRZBPpkgwq)