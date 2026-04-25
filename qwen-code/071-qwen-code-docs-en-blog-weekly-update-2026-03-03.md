---
title: 'Qwen Code Weekly: Insight Analytics, Clipboard Images, Terminal Capture'
url: https://qwenlm.github.io/qwen-code-docs/en/blog/weekly-update-2026-03-03
source: github_pages
fetched_at: 2026-04-09T09:05:37.978975928-03:00
rendered_js: true
word_count: 412
summary: This blog post details the latest updates and new features in Qwen Code, including built-in insight analytics, cross-platform clipboard image support, automated terminal screenshot generation, and various bug fixes across different versions.
tags:
    - qwen-code
    - feature-update
    - analytics
    - clipboard-images
    - terminal-capture
    - software-release
category: blog
---

[Blog](https://qwenlm.github.io/qwen-code-docs/en/blog/ "Blog")

Qwen Code Weekly: Insight Analytics, Clipboard Images, Terminal Capture

This week we released v0.10.0, v0.11.0 major feature versions and 5 bugfix versions.

- Released two major feature versions: v0.10.0 and v0.11.0, plus 5 bugfix versions
- OAuth authentication with model upgraded to qwen3.5-plus, 1000 free calls per day
- Added Insight analytics
- Clipboard image support
- Terminal Capture automated validation and screenshot generation

## ✨ New Features[](#-new-features)

### Insight Analytics[](#insight-analytics)

Official built-in command that deeply analyzes local Session records to provide personalized programming insights and usage analysis reports.

![](https://gw.alicdn.com/imgextra/i1/O1CN01fU1ONc1cQ6aODsN3J_!!6000000003594-2-tps-1698-954.png)

Usage: Type `/insight` to start parallel LLM analysis

Generates a detailed HTML report divided into 7 sections:

- **What You Work On** - Your work focus
- **How You Use Qwen Code** - How you use Qwen Code
- **Impressive Things** - Notable achievements
- **Where Things Go Wrong** - Problem areas
- **Features to Try** - Features worth trying
- **New Usage Patterns** - New usage patterns
- **On the Horizon** - Future outlook

Finally, you can export an image for social media sharing.

![](https://gw.alicdn.com/imgextra/i4/O1CN01xJKhpq1WNSbVJyveF_!!6000000002776-2-tps-2400-1332.png)

👇 Feature Demo

### Clipboard Image Support[](#clipboard-image-support)

Cross-platform support: macOS / Windows / Linux. See PR [#1612](https://github.com/QwenLM/qwen-code/pull/1612) 

Features:

- **Image Capture**: Capture images from system clipboard
- **Temporary Storage**: Save to clipboard temp directory
- **LRU Cleanup**: Auto-delete oldest 50 images when exceeding 100
- **Attachment UI**: `↑` to enter attachment mode, `←/→` to navigate, `Delete` to remove

![](https://gw.alicdn.com/imgextra/i2/O1CN01OsEDov1z4nJto1CfQ_!!6000000006661-2-tps-1694-956.png)

### Terminal-Capture[](#terminal-capture)

Purpose: Automated terminal screenshot tool for CLI visual verification, automatically validates features and produces demo screenshots.

Architecture: node-pty (pseudo-terminal) → xterm.js (rendering) → Playwright (screenshot), see PR [#1840](https://github.com/QwenLM/qwen-code/pull/1840) 

👇 Feature Demo

### MCP Tool Progress Updates[](#mcp-tool-progress-updates)

Feature: MCP tools support real-time progress notifications

- **TUI Mode**: Display `⏳ [50/100] Processing...`
- **SDK Mode**: New `tool_progress` stream event type

See PR [#1756](https://github.com/QwenLM/qwen-code/pull/1756) 

## 🔧 Important Fixes[](#-important-fixes)

PRVersionIssueImpact[#1330](https://github.com/QwenLM/qwen-code/pull/1330) v0.10.0Setting naming confusionRenamed disable* → enable\*, auto-migration[#1768](https://github.com/QwenLM/qwen-code/pull/1768) v0.11.0Windows path case sensitivitySession matching failed, normalized to lowercase[#1811](https://github.com/QwenLM/qwen-code/pull/1811) v0.10.2AbortSignal memory leakMaxListenersExceededWarning[#1821](https://github.com/QwenLM/qwen-code/pull/1821) v0.10.2JSON Schema incompatibilitySupport draft-2020-12[#1791](https://github.com/QwenLM/qwen-code/pull/1791) v0.10.2TPM rate limitingDetect and wait 1 minute to retry[#1825](https://github.com/QwenLM/qwen-code/pull/1825) v0.10.2Subagent abort accumulationFixed listener leak[#1796](https://github.com/QwenLM/qwen-code/pull/1796) v0.11.0ESC cancel blockingFixed input blocking issue[#1877](https://github.com/QwenLM/qwen-code/pull/1877) v0.11.0Arch OS installationAdded sudo detection for permission checks[#1929](https://github.com/QwenLM/qwen-code/pull/1929) v0.11.0LSP compatibilityChanged workspaceFolders to boolean[#1857](https://github.com/QwenLM/qwen-code/pull/1857) v0.10.6BOM detectionImproved length checking and codePointAt

### Windows Platform Fixes[](#windows-platform-fixes)

PRIssue[#1604](https://github.com/QwenLM/qwen-code/pull/1604) Sandbox detection using PowerShell Get-Command[#1736](https://github.com/QwenLM/qwen-code/pull/1736) Tab key doesn’t cycle approval modes when autocomplete is active[#1768](https://github.com/QwenLM/qwen-code/pull/1768) Path case sensitivity causing session mismatch

**Upgrade**: Run `npm i @qwen-code/qwen-code@latest -g` to upgrade to the latest version.

For questions or suggestions, welcome to [GitHub Issues](https://github.com/QwenLM/qwen-code/issues) !

Last updated on March 31, 2026

[Qwen Code Weekly: Agent Skills GA, One-Click Install, Session Export](https://qwenlm.github.io/qwen-code-docs/en/blog/weekly-update-2026-02-09/ "Qwen Code Weekly: Agent Skills GA, One-Click Install, Session Export")[Qwen Code Weekly: HTML Export Enhancement, Terminal GIF Recording, GitHub Workflow Commands](https://qwenlm.github.io/qwen-code-docs/en/blog/weekly-update-2026-03-06/ "Qwen Code Weekly: HTML Export Enhancement, Terminal GIF Recording, GitHub Workflow Commands")