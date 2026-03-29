---
title: ForgeCode
url: https://forgecode.dev/docs/shell-commands/
source: sitemap
fetched_at: 2026-03-29T14:52:20.12961672-03:00
rendered_js: false
word_count: 385
summary: This document explains how to execute native shell commands in ForgeCode using the ! prefix, including execution behavior, shell compatibility, and limitations around state persistence.
tags:
    - shell-commands
    - command-execution
    - forgecode-cli
    - shell-compatibility
    - state-management
    - directory-navigation
category: reference
---

ForgeCode allows you to execute native shell commands directly from the CLI by prefixing them with `!` without switching context. These commands are executed immediately without being processed by the AI, providing a fast way to run system operations without leaving the ForgeCode environment.

Direct Execution

Commands that start with `!` bypass the AI and are executed directly in your shell. This ensures immediate execution and allows you to seamlessly integrate shell operations into your ForgeCode workflow.

To execute a shell command, prefix it with `!`:

These commands will be executed in your current working directory, and their output will be displayed in the console.

### Shell Compatibility[​](#shell-compatibility "Direct link to Shell Compatibility")

ZSH and PowerShell don't work out of the box with ForgeCode's shell command execution. ForgeCode uses a restricted bash environment for security and consistency across platforms. If you're using ZSH or PowerShell as your default shell, some shell-specific features, aliases, and functions will not be available when executing commands through ForgeCode.

**Workaround**: Use standard POSIX-compliant commands or explicitly call your preferred shell:

### Stateless Execution[​](#stateless-execution "Direct link to Stateless Execution")

All commands are executed fresh without carrying forward information between runs. Each shell command starts with a clean environment, meaning:

- Environment variables set in one command won't persist to the next.
- Background processes started in one command won't be accessible in subsequent commands.
- Shell history and session state are not maintained.

**Example of what won't work**:

**Workaround**: Combine related commands in a single execution:

### Directory Changes Don't Persist[​](#directory-changes-dont-persist "Direct link to Directory Changes Don't Persist")

Changing the directory will only be applicable until the command executes and will not affect ForgeCode's working directory. The `cd` command or any directory navigation within a shell command is temporary and isolated to that specific command execution.

**Example**:

**Workaround**: To change ForgeCode's working directory for a session, restart ForgeCode in your target directory:

1. **Exit and navigate:**
2. **Or restart with path directly:**

**Alternative approach:**

- Chain commands with directory changes:

Purpose of Shell Commands

The `!` shortcut is for quick command execution without context switching, not as a replacement for your preferred shell environment. For complex shell workflows, interactive sessions, or shell-specific features, continue using your native ZSH, PowerShell, or bash terminal alongside ForgeCode.

The available shell commands depend on your operating system:

- **macOS/Linux**: Full bash command support.
- **Windows**: Command Prompt commands.

Make sure to use commands appropriate for your platform when sharing ForgeCode sessions or documentation.