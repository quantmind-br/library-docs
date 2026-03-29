---
title: 'ForgeCode v0.106.0 Release: Plan Progress Tracking and Reliability Improvements'
url: https://forgecode.dev/blog/forge-v0106-release/
source: sitemap
fetched_at: 2026-03-29T14:48:12.371962876-03:00
rendered_js: false
word_count: 316
summary: This document explains the new features and improvements in ForgeCode version 0.106.0, including real-time plan progress tracking, VS Code extension functionality, and enhanced reliability features.
tags:
    - version-update
    - progress-tracking
    - vs-code-extension
    - reliability
    - error-handling
    - api-integration
category: reference
---

Version 0.106.0 introduces intelligent plan progress tracking and critical reliability improvements that make your development workflow smoother and more stable.

While ForgeCode has always supported plan creation through the Muse agent, v0.106.0 adds real-time progress tracking. ForgeCode now actively monitors and updates task status as it works through your plans.

![Progress Tracking in Forgecode](https://forgecode.dev/assets/images/task-list-d98d74c6693aabf0b188610e4183666a.png)

### How It Works[​](#how-it-works "Direct link to How It Works")

Plans use checkbox syntax that ForgeCode automatically manages:

- `[ ]` - Task not started
- `[~]` - Task in progress
- `[x]` - Task completed

When you reference a plan file, ForgeCode works through tasks sequentially and updates their status in real-time. You can watch tasks move from `[ ]` to `[~]` to `[x]` as work progresses.

The new VS Code extension enables quick file reference copying in ForgeCode's exact format, eliminating manual path and line number typing.

### Features[​](#features "Direct link to Features")

- **Copy File References**: Direct clipboard copying with line selections
- **Smart Format**: Automatic `@[<filepath>:<line start>:<line end>]` formatting
- **Quick Access**: `CTRL+U` keyboard shortcut
- **Requirements**: ForgeCode in PATH, VS Code 1.102.0+

### Usage[​](#usage "Direct link to Usage")

1. Select code or lines
2. Press `CTRL+U`
3. Paste formatted reference into ForgeCode

Install from the [VS Code Marketplace](https://marketplace.visualstudio.com/items?itemName=ForgeCode.forge-vscode).

![ForgeCode VS Code Extension Demo](https://forgecode.dev/assets/images/demo_vscode-91e033a7be71f6d1283957a4689f6479.gif)

### Fixed MCP Integration with OpenAI Models[​](#fixed-mcp-integration-with-openai-models "Direct link to Fixed MCP Integration with OpenAI Models")

Resolved critical MCP operation failures with OpenAI models caused by missing schema dependencies.

### Enhanced Retry Logic[​](#enhanced-retry-logic "Direct link to Enhanced Retry Logic")

Extended existing retry logic to handle empty response bodies. Previously, retry only worked for errors - now it also handles when AI providers return empty responses.

The system now retries for:

- Empty response bodies (new)
- Transport errors (existing)
- HTTP status codes: 429, 500, 502, 503, 504 (existing)

Configure retry behavior:

### Enhanced Error Messages[​](#enhanced-error-messages "Direct link to Enhanced Error Messages")

Replaced cryptic error messages with clear, actionable feedback that includes context and suggested next steps.

Version 0.106.0 establishes the foundation for advanced project management and development tooling. The VS Code extension will expand with additional IDE integrations and enhanced code context features.

* * *

*Forge is open-source and community-driven. Join us at [github.com/antinomyhq/forge](https://github.com/antinomyhq/forge) to contribute or report issues.*