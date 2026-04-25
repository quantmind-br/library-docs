---
title: 'Qwen Code Weekly: Agent Skills GA, One-Click Install, Session Export'
url: https://qwenlm.github.io/qwen-code-docs/en/blog/weekly-update-2026-02-09
source: github_pages
fetched_at: 2026-04-09T09:05:36.257734375-03:00
rendered_js: true
word_count: 546
summary: This weekly blog post details updates for Qwen Code, announcing major stable feature releases like Agent Skills going General Availability and adding session history export capabilities across multiple formats. It also covers installation improvements, SDK optimizations, and numerous bug fixes.
tags:
    - weekly-update
    - feature-release
    - agent-skills
    - session-export
    - sdk-optimization
    - installation-guide
    - code-development
category: blog
---

[Blog](https://qwenlm.github.io/qwen-code-docs/en/blog/ "Blog")

Qwen Code Weekly: Agent Skills GA, One-Click Install, Session Export

This week we released v0.9.0, v0.9.1 stable versions and v0.10.0 preview.

- Agent Skills officially removed experimental flag, upgraded to stable feature
- Added one-click install script to further lower the barrier to entry
- Support exporting session history to Markdown, JSONL, HTML formats
- Free quota adjusted from 2000/day to 1000/day

## ✨ New Features[](#-new-features)

### Agent Skills Goes GA[](#agent-skills-goes-ga)

Agent Skills removed `--experimental-skills` flag, meaning Skills has been fully tested over 4 release cycles since its official release in 0.6.0, upgraded from experimental to stable status, and can be safely used in production environments.

See PR [#1738](https://github.com/QwenLM/qwen-code/pull/1738) 

![](https://gw.alicdn.com/imgextra/i1/O1CN01xkzvoE1fomm8znzBG_!!6000000004054-2-tps-1694-952.png)

### Session History Export Support[](#session-history-export-support)

Added `/export` command, supporting export of session history to Markdown, JSONL, and HTML formats. Users can easily save and share conversation records, generate documents or reports. See PR [#1515](https://github.com/QwenLM/qwen-code/pull/1515) 

**How to use?**

- `/export <format> <session ID>`
- When `<session ID>` is empty, exports the current conversation.

![](https://gw.alicdn.com/imgextra/i2/O1CN01vq4v6W1oJwe6lyVg2_!!6000000005205-1-tps-1280-720.gif)

### New One-Click Install Script[](#new-one-click-install-script)

Added one-click install script to further lower the barrier to entry, supporting one-line command installation.

See PR [#1653](https://github.com/QwenLM/qwen-code/pull/1653) 

**Linux / macOS**

```
curl -fsSL https://qwen-code-assets.oss-cn-hangzhou.aliyuncs.com/installation/install-qwen.sh | bash
```

**Windows (Run as Administrator CMD)**

```
curl -fsSL -o %TEMP%\install-qwen.bat https://qwen-code-assets.oss-cn-hangzhou.aliyuncs.com/installation/install-qwen.bat && %TEMP%\install-qwen.bat
```

It is recommended to restart your terminal after installation to ensure environment variables take effect.

### Large File Paste Optimization[](#large-file-paste-optimization)

Optimized for large file paste scenarios, added placeholder prompts, and fixed enter submission issue on macOS. Improved user experience, especially when dealing with large amounts of code or text.

See PR [#1713](https://github.com/QwenLM/qwen-code/pull/1713) 

![](https://gw.alicdn.com/imgextra/i3/O1CN01rFSm7o1hoRiIy0xrP_!!6000000004324-1-tps-1280-720.gif)

### SDK Feature Optimization[](#sdk-feature-optimization)

- **Session Resume Feature**: TypeScript SDK now supports `resume` option, equivalent to CLI’s `--resume` flag, users can now save session state. See PR [#1714](https://github.com/QwenLM/qwen-code/pull/1714)
- **Electron IPC Integration Support**: Added FORK\_MODE support for ProcessTransport, enabling deep integration with Electron IPC, making it convenient for developers to build desktop applications. See PR [#1719](https://github.com/QwenLM/qwen-code/pull/1719)

### Search Tools Support in Plan Mode[](#search-tools-support-in-plan-mode)

Automatically enable WebFetch and WebSearch tools in plan mode, simplifying user operations.

See PR [#1686](https://github.com/QwenLM/qwen-code/pull/1686) 

![](https://gw.alicdn.com/imgextra/i3/O1CN016eKNFf1CtFmYQHGsd_!!6000000000138-2-tps-1694-952.png)

## 🔧 Important Fixes[](#-important-fixes)

- **Symbolic Link Support**: Skills added symbolic link support for easier organization and management of Skills [#1690](https://github.com/QwenLM/qwen-code/pull/1690)
- **SubAgents Tool Limitations**: Prevent unauthorized tool usage, enhancing security [#1691](https://github.com/QwenLM/qwen-code/pull/1691)
- **File Editing Trailing Whitespace Handling**: Fixed issue of preserving trailing whitespace when editing files, ensuring format integrity [#1688](https://github.com/QwenLM/qwen-code/pull/1688)
- **Docker Build Fix**: Fixed Docker build errors and supported manual version builds [#1722](https://github.com/QwenLM/qwen-code/pull/1722)
- **CLI Parameter Parsing**: Fixed CLI entry point parameter parsing issues [#1758](https://github.com/QwenLM/qwen-code/pull/1758)
- **ACP Model Selection**: Fixed ACP model selection to support all configured authentication types [#1555](https://github.com/QwenLM/qwen-code/pull/1555)
- **UTF-8 BOM Preservation** [#1680](https://github.com/QwenLM/qwen-code/pull/1680)  - Preserve UTF-8 BOM when editing files, ensuring encoding compatibility
- **Debug Mode Refactoring** [#1610](https://github.com/QwenLM/qwen-code/pull/1610)  - Refactored debug mode output, routing console calls to log file-first debugLogger
- **Build Efficiency Improvement** [#1681](https://github.com/QwenLM/qwen-code/pull/1681)  - Improved build process and added development mode

### Windows Compatibility Improvements[](#windows-compatibility-improvements)

- Enabled Shift+Tab shortcut in Windows PowerShell [#1607](https://github.com/QwenLM/qwen-code/pull/1607)
- Prevent Tab key from cycling approval modes when autocomplete is activated on Windows [#1736](https://github.com/QwenLM/qwen-code/pull/1736)

### MCP Feature Optimization[](#mcp-feature-optimization)

- Fixed MCP multi-part tool result processing logic, ensuring correctness of complex tool calls [#1755](https://github.com/QwenLM/qwen-code/pull/1755)
- Improved MCP server management process and authentication mechanism, enhancing stability and security [#1752](https://github.com/QwenLM/qwen-code/pull/1752)
- Properly clean up MCP server child processes on exit, preventing resource leaks [#1285](https://github.com/QwenLM/qwen-code/pull/1285)

**Upgrade**: Run `npm i @qwen-code/qwen-code@latest -g` to upgrade to the latest version.

For questions or suggestions, welcome to [GitHub Issues](https://github.com/QwenLM/qwen-code/issues) !

Last updated on March 31, 2026

[Qwen Code Weekly: LSP Support, Batch Runner, New Languages](https://qwenlm.github.io/qwen-code-docs/en/blog/weekly-update-2026-02-03/ "Qwen Code Weekly: LSP Support, Batch Runner, New Languages")[Qwen Code Weekly: Insight Analytics, Clipboard Images, Terminal Capture](https://qwenlm.github.io/qwen-code-docs/en/blog/weekly-update-2026-03-03/ "Qwen Code Weekly: Insight Analytics, Clipboard Images, Terminal Capture")