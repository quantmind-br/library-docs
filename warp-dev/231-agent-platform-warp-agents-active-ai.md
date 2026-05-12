---
title: Active AI recommendations | Agents | Warp
url: https://docs.warp.dev/agent-platform/warp-agents/active-ai
source: sitemap
fetched_at: 2026-04-29T15:04:10.695341086-03:00
rendered_js: false
word_count: 381
summary: This document explains how to configure and use Active AI features in Warp, including Prompt Suggestions, Next Command, and Suggested Code Diffs.
tags:
    - warp-terminal
    - ai-features
    - prompt-suggestions
    - command-automation
    - code-diffs
    - privacy-settings
category: configuration
optimized: true
optimized_at: 2026-04-29T00:00:00Z
---
Active AI features can be disabled in **Settings** → **Agents** → **Warp Agent** with the Active AI toggle.

## Prompt Suggestions

Prompt Suggestions are contextual AI-powered suggestions that activate Agent Mode, similar to how Warp suggests commands to run.

To disable: **Settings** → **Agents** → **Warp Agent** → **Active AI** → **Prompt Suggestions**

### Accepting a prompt suggestion

Press `CMD-ENTER` (macOS), `CTRL-SHIFT-ENTER` (Linux/Windows), or click the chip to auto-populate the suggestion into Agent Mode (with the most recent block attached).

> [!info]
> Prompt Suggestions use an LLM to generate prompts based on your terminal session. These AI requests do not contribute towards your AI limits. Accepted prompts run in Agent Mode contribute as normal.
> If [Secret Redaction](https://docs.warp.dev/support-and-community/privacy-security-and-licensing/secret-redaction) is enabled, selected regexes are applied to content sent to Active AI features.

## Next Command

Next Command uses AI to suggest the next command based on your terminal session and command history.

To disable: **Settings** → **Agents** → **Warp Agent** → **Active AI** → **Next Command**

> [!info]
> Next Command uses command history (enriched with git branch, exit code, and directory metadata) and recent block input/output to generate command suggestions.
> [Secret Redaction](https://docs.warp.dev/support-and-community/privacy-security-and-licensing/secret-redaction) is automatically applied.

### Accepting Next Command suggestions

Press `→` or `CTRL-F` to accept a suggestion into your input buffer, then `ENTER` to execute. Change the accept keybinding via the inline keybinding picker.

### Billing

Next Commands are unlimited across all Warp plans, including Free. See [warp.dev/pricing](https://warp.dev/pricing) for AI limits and pricing.

## Suggested Code Diffs

Suggested Code Diffs surface potential fixes for command-line errors (compiler errors, simple merge conflicts).

When an error occurs and Warp evaluates it as suitable for an LLM fix, a "Generating fix" banner appears. Stop this with `CTRL + C` or the stop button.

### Using a suggested code diff

Accept via buttons in the diff view, or:
- `CMD + ENTER` (macOS) / `CTRL + ENTER` (Windows/Linux)

View details with:
- `CMD + E` (macOS) / `CTRL + E` (Windows/Linux) — expands to inspect, refine, or edit
- `↓` — scroll through the entire diff

> [!info]
> Suggested Code Diffs do not count toward AI request limits. Monthly limits scale by plan tier. See [warp.dev/pricing](https://warp.dev/pricing).

## Active AI privacy

See the [Privacy Page](https://docs.warp.dev/support-and-community/privacy-security-and-licensing/privacy) for data handling details.

#active-ai #prompt-suggestions #code-diffs
