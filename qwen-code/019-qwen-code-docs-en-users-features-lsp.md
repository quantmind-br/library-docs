---
title: Language Server Protocol (LSP) Support
url: https://qwenlm.github.io/qwen-code-docs/en/users/features/lsp
source: github_pages
fetched_at: 2026-04-09T09:04:01.93625143-03:00
rendered_js: true
word_count: 870
summary: This document details Qwen Code's implementation of Language Server Protocol (LSP) support, explaining how it provides advanced code intelligence features like finding references and diagnostics across various supported languages. It covers setup from prerequisites to detailed configuration options and available LSP operations.
tags:
    - lsp-support
    - code-intelligence
    - language-server
    - developer-tools
    - configuration-guide
    - api-operations
category: reference
---

Qwen Code provides native Language Server Protocol (LSP) support, enabling advanced code intelligence features like go-to-definition, find references, diagnostics, and code actions. This integration allows the AI agent to understand your code more deeply and provide more accurate assistance.

## Overview[](#overview)

LSP support in Qwen Code works by connecting to language servers that understand your code. When you work with TypeScript, Python, Go, or other supported languages, Qwen Code can automatically start the appropriate language server and use it to:

- Navigate to symbol definitions
- Find all references to a symbol
- Get hover information (documentation, type info)
- View diagnostic messages (errors, warnings)
- Access code actions (quick fixes, refactorings)
- Analyze call hierarchies

## Quick Start[](#quick-start)

LSP is an experimental feature in Qwen Code. To enable it, use the `--experimental-lsp` command line flag:

For most common languages, Qwen Code will automatically detect and start the appropriate language server if it’s installed on your system.

### Prerequisites[](#prerequisites)

You need to have the language server for your programming language installed:

LanguageLanguage ServerInstall CommandTypeScript/JavaScripttypescript-language-server`npm install -g typescript-language-server typescript`Pythonpylsp`pip install python-lsp-server`Gogopls`go install golang.org/x/tools/gopls@latest`Rustrust-analyzer[Installation guide](https://rust-analyzer.github.io/manual.html#installation) 

## Configuration[](#configuration)

### .lsp.json File[](#lspjson-file)

You can configure language servers using a `.lsp.json` file in your project root. This uses the language-keyed format described in the [Claude Code plugin LSP configuration reference](https://code.claude.com/docs/en/plugins-reference#lsp-servers) .

**Basic format:**

```
{
  "typescript": {
    "command": "typescript-language-server",
    "args": ["--stdio"],
    "extensionToLanguage": {
      ".ts": "typescript",
      ".tsx": "typescriptreact",
      ".js": "javascript",
      ".jsx": "javascriptreact"
    }
  }
}
```

### Configuration Options[](#configuration-options)

#### Required Fields[](#required-fields)

OptionTypeDescription`command`stringCommand to start the LSP server (must be in PATH)`extensionToLanguage`objectMaps file extensions to language identifiers

#### Optional Fields[](#optional-fields)

OptionTypeDefaultDescription`args`string\[]`[]`Command line arguments`transport`string`"stdio"`Transport type: `stdio` or `socket``env`object-Environment variables`initializationOptions`object-LSP initialization options`settings`object-Server settings via `workspace/didChangeConfiguration``workspaceFolder`string-Override workspace folder`startupTimeout`number`10000`Startup timeout in milliseconds`shutdownTimeout`number`5000`Shutdown timeout in milliseconds`restartOnCrash`boolean`false`Auto-restart on crash`maxRestarts`number`3`Maximum restart attempts`trustRequired`boolean`true`Require trusted workspace

### TCP/Socket Transport[](#tcpsocket-transport)

For servers that use TCP or Unix socket transport:

```
{
  "remote-lsp": {
    "transport": "tcp",
    "socket": {
      "host": "127.0.0.1",
      "port": 9999
    },
    "extensionToLanguage": {
      ".custom": "custom"
    }
  }
}
```

## Available LSP Operations[](#available-lsp-operations)

Qwen Code exposes LSP functionality through the unified `lsp` tool. Here are the available operations:

### Code Navigation[](#code-navigation)

#### Go to Definition[](#go-to-definition)

Find where a symbol is defined.

```
Operation: goToDefinition
Parameters:
  - filePath: Path to the file
  - line: Line number (1-based)
  - character: Column number (1-based)
```

#### Find References[](#find-references)

Find all references to a symbol.

```
Operation: findReferences
Parameters:
  - filePath: Path to the file
  - line: Line number (1-based)
  - character: Column number (1-based)
  - includeDeclaration: Include the declaration itself (optional)
```

#### Go to Implementation[](#go-to-implementation)

Find implementations of an interface or abstract method.

```
Operation: goToImplementation
Parameters:
  - filePath: Path to the file
  - line: Line number (1-based)
  - character: Column number (1-based)
```

### Symbol Information[](#symbol-information)

#### Hover[](#hover)

Get documentation and type information for a symbol.

```
Operation: hover
Parameters:
  - filePath: Path to the file
  - line: Line number (1-based)
  - character: Column number (1-based)
```

#### Document Symbols[](#document-symbols)

Get all symbols in a document.

```
Operation: documentSymbol
Parameters:
  - filePath: Path to the file
```

#### Workspace Symbol Search[](#workspace-symbol-search)

Search for symbols across the workspace.

```
Operation: workspaceSymbol
Parameters:
  - query: Search query string
  - limit: Maximum results (optional)
```

### Call Hierarchy[](#call-hierarchy)

#### Prepare Call Hierarchy[](#prepare-call-hierarchy)

Get the call hierarchy item at a position.

```
Operation: prepareCallHierarchy
Parameters:
  - filePath: Path to the file
  - line: Line number (1-based)
  - character: Column number (1-based)
```

#### Incoming Calls[](#incoming-calls)

Find all functions that call the given function.

```
Operation: incomingCalls
Parameters:
  - callHierarchyItem: Item from prepareCallHierarchy
```

#### Outgoing Calls[](#outgoing-calls)

Find all functions called by the given function.

```
Operation: outgoingCalls
Parameters:
  - callHierarchyItem: Item from prepareCallHierarchy
```

### Diagnostics[](#diagnostics)

#### File Diagnostics[](#file-diagnostics)

Get diagnostic messages (errors, warnings) for a file.

```
Operation: diagnostics
Parameters:
  - filePath: Path to the file
```

#### Workspace Diagnostics[](#workspace-diagnostics)

Get all diagnostic messages across the workspace.

```
Operation: workspaceDiagnostics
Parameters:
  - limit: Maximum results (optional)
```

### Code Actions[](#code-actions)

#### Get Code Actions[](#get-code-actions)

Get available code actions (quick fixes, refactorings) at a location.

```
Operation: codeActions
Parameters:
  - filePath: Path to the file
  - line: Start line number (1-based)
  - character: Start column number (1-based)
  - endLine: End line number (optional, defaults to line)
  - endCharacter: End column (optional, defaults to character)
  - diagnostics: Diagnostics to get actions for (optional)
  - codeActionKinds: Filter by action kind (optional)
```

Code action kinds:

- `quickfix` - Quick fixes for errors/warnings
- `refactor` - Refactoring operations
- `refactor.extract` - Extract to function/variable
- `refactor.inline` - Inline function/variable
- `source` - Source code actions
- `source.organizeImports` - Organize imports
- `source.fixAll` - Fix all auto-fixable issues

## Security[](#security)

LSP servers are only started in trusted workspaces by default. This is because language servers run with your user permissions and can execute code.

### Trust Controls[](#trust-controls)

- **Trusted Workspace**: LSP servers start automatically
- **Untrusted Workspace**: LSP servers won’t start unless `trustRequired: false` is set in the server configuration

To mark a workspace as trusted, use the `/trust` command or configure trusted folders in settings.

### Per-Server Trust Override[](#per-server-trust-override)

You can override trust requirements for specific servers in their configuration:

```
{
  "safe-server": {
    "command": "safe-language-server",
    "args": ["--stdio"],
    "trustRequired": false,
    "extensionToLanguage": {
      ".safe": "safe"
    }
  }
}
```

## Troubleshooting[](#troubleshooting)

### Server Not Starting[](#server-not-starting)

1. **Check if the server is installed**: Run the command manually to verify
2. **Check the PATH**: Ensure the server binary is in your system PATH
3. **Check workspace trust**: The workspace must be trusted for LSP
4. **Check logs**: Look for error messages in the console output
5. **Verify —experimental-lsp flag**: Make sure you’re using the flag when starting Qwen Code

### Slow Performance[](#slow-performance)

1. **Large projects**: Consider excluding `node_modules` and other large directories
2. **Server timeout**: Increase `startupTimeout` in server configuration for slow servers

### No Results[](#no-results)

1. **Server not ready**: The server may still be indexing
2. **File not saved**: Save your file for the server to pick up changes
3. **Wrong language**: Check if the correct server is running for your language

### Debugging[](#debugging)

Enable debug logging to see LSP communication:

```
DEBUG=lsp* qwen --experimental-lsp
```

Or check the LSP debugging guide at `packages/cli/LSP_DEBUGGING_GUIDE.md`.

## Claude Code Compatibility[](#claude-code-compatibility)

Qwen Code supports Claude Code-style `.lsp.json` configuration files in the language-keyed format defined in the [Claude Code plugins reference](https://code.claude.com/docs/en/plugins-reference#lsp-servers) . If you’re migrating from Claude Code, use the language-as-key layout in your configuration.

### Configuration Format[](#configuration-format)

The recommended format follows Claude Code’s specification:

```
{
  "go": {
    "command": "gopls",
    "args": ["serve"],
    "extensionToLanguage": {
      ".go": "go"
    }
  }
}
```

Claude Code LSP plugins can also supply `lspServers` in `plugin.json` (or a referenced `.lsp.json`). Qwen Code loads those configs when the extension is enabled, and they must use the same language-keyed format.

## Best Practices[](#best-practices)

1. **Install language servers globally**: This ensures they’re available in all projects
2. **Use project-specific settings**: Configure server options per project when needed via `.lsp.json`
3. **Keep servers updated**: Update your language servers regularly for best results
4. **Trust wisely**: Only trust workspaces from trusted sources

## FAQ[](#faq)

### Q: How do I enable LSP?[](#q-how-do-i-enable-lsp)

Use the `--experimental-lsp` flag when starting Qwen Code:

### Q: How do I know which language servers are running?[](#q-how-do-i-know-which-language-servers-are-running)

Use the `/lsp status` command to see all configured and running language servers.

### Q: Can I use multiple language servers for the same file type?[](#q-can-i-use-multiple-language-servers-for-the-same-file-type)

Yes, but only one will be used for each operation. The first server that returns results wins.

### Q: Does LSP work in sandbox mode?[](#q-does-lsp-work-in-sandbox-mode)

LSP servers run outside the sandbox to access your code. They’re subject to workspace trust controls.