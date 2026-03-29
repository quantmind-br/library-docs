---
title: ForgeCode
url: https://forgecode.dev/docs/piping-guide/
source: sitemap
fetched_at: 2026-03-29T16:30:44.863155-03:00
rendered_js: false
word_count: 164
summary: This document explains how to use standard input (stdin) piping to provide content to the ForgeCode command-line tool, along with best practices and usage limitations.
tags:
    - cli-tool
    - stdin-piping
    - command-line-interface
    - input-methods
    - workflow-automation
category: guide
---

ForgeCode supports reading input from stdin (standard input) via piping, allowing you to pass content from other commands or files directly to ForgeCode.

Pipe content from any command or file directly to ForgeCode:

When you pipe content to ForgeCode:

1. **Detects Piped Input**: Automatically recognizes stdin from a pipe
2. **Reads and Processes**: Reads all content until EOF, trims whitespace, and uses it as your prompt

### --prompt Flag Takes Precedence[​](#--prompt-flag-takes-precedence "Direct link to --prompt Flag Takes Precedence")

Cannot Combine Piping with --prompt

The `--prompt` flag will **completely ignore** piped content:

Choose one input method or the other.

### Works with Other Flags[​](#works-with-other-flags "Direct link to Works with Other Flags")

Piping works with all other ForgeCode flags:

### Code Review Workflow[​](#code-review-workflow "Direct link to Code Review Workflow")

### Log Analysis[​](#log-analysis "Direct link to Log Analysis")

### File Content Review[​](#file-content-review "Direct link to File Content Review")

### Command Output Analysis[​](#command-output-analysis "Direct link to Command Output Analysis")

### Conditional Piping[​](#conditional-piping "Direct link to Conditional Piping")

### Multi-Source Input[​](#multi-source-input "Direct link to Multi-Source Input")

### Using Here-Documents[​](#using-here-documents "Direct link to Using Here-Documents")

1. **Don't Mix Input Methods**: The `--prompt` flag ignores piped content. Use one or the other.
2. **Use Command Substitution**: `echo "Context: $(command)" | forge` ensures you always have content.
3. **Mind Large Files**: Piped content is read entirely into memory.
4. **Capture Errors**: Use `2>&1` to capture both stdout and stderr.