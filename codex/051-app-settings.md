---
title: Codex app settings
url: https://developers.openai.com/codex/app/settings.md
source: llms
fetched_at: 2026-04-30T10:15:06.383194358-03:00
rendered_js: false
word_count: 363
summary: This document provides an overview of the Codex application settings panel, explaining how to configure general behavior, interface appearance, agent integration, security preferences, and various productivity features.
tags:
    - app-configuration
    - user-settings
    - system-preferences
    - codex-app
    - agent-setup
    - customization
category: configuration
optimized: true
optimized_at: 2026-04-30T13:30:00Z
---
# Codex app settings

Open [**Settings**](codex://settings) from the app menu or press `Cmd+,`.

## General

- Choose where files open
- Control how much command output appears in threads
- Require `Cmd+Enter` for multiline prompts
- Prevent sleep while a thread runs

## Notifications

- Choose when turn completion notifications appear
- Whether the app should prompt for notification permissions

## Agent configuration

Codex agents in the app inherit the same configuration as IDE and CLI. Use in-app controls for common settings, or edit `config.toml` for advanced options. See [[041-agent-approvals-security|Codex security]] and [[055-config-basic|config basics]].

## Appearance

- Choose base theme
- Adjust accent, background, and foreground colors
- Change UI and code fonts
- Share custom themes with friends

## Git

- Standardize branch naming
- Choose whether Codex uses force pushes
- Set prompts for commit messages and PR descriptions

## Integrations & MCP

Connect external tools via MCP (Model Context Protocol). Enable recommended servers or add your own. If a server requires OAuth, the app starts the auth flow. Settings apply to CLI and IDE extension because MCP configuration lives in `config.toml`. See [[058-mcp|Model Context Protocol docs]].

## Browser use

Install or enable the bundled Browser plugin and manage allowlisted and blocklisted websites. Codex asks before using a website unless allowlisted. Removing a site from the blocklist lets Codex ask again. See [[003-app-browser|In-app browser]].

## Computer Use

On macOS, review desktop-app access and related preferences after setup. To revoke system-level access, update Screen Recording or Accessibility permissions in macOS Privacy & Security settings. Not available in the European Economic Area, United Kingdom, or Switzerland at launch.

## Personalization

Choose **Friendly**, **Pragmatic**, or **None** as default personality. Use **None** to disable personality instructions. Update at any time.

Add your own custom instructions — edits update your [[020-guides-agents-md|personal instructions in `AGENTS.md`]].

## Context-aware suggestions

Surface follow-ups and tasks you may want to resume when starting or returning to Codex.

## Memories

Enable Memories, where available, to let Codex carry useful context from past threads into future work. See [[059-memories|Memories]] for setup, storage, and per-thread controls.

## Archived threads

Lists archived chats with dates and project context. Use **Unarchive** to restore.

#settings #codex-app #configuration