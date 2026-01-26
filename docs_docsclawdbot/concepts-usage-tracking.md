---
title: "null"
url: https://docs.clawd.bot/concepts/usage-tracking.md
source: llms
fetched_at: 2026-01-26T09:51:45.166356-03:00
rendered_js: false
word_count: 200
summary: This document explains how Clawdbot tracks and displays real-time AI provider usage and quotas across chat interfaces, the CLI, and the macOS menu bar. It details the supported providers and the specific credential types required to pull data from their usage endpoints.
tags:
    - usage-tracking
    - clawdbot
    - api-quota
    - provider-integration
    - cost-monitoring
    - llm-usage
category: reference
---

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.clawd.bot/llms.txt
> Use this file to discover all available pages before exploring further.

# null

# Usage tracking

## What it is

* Pulls provider usage/quota directly from their usage endpoints.
* No estimated costs; only the provider-reported windows.

## Where it shows up

* `/status` in chats: emoji‑rich status card with session tokens + estimated cost (API key only). Provider usage shows for the **current model provider** when available.
* `/usage off|tokens|full` in chats: per-response usage footer (OAuth shows tokens only).
* `/usage cost` in chats: local cost summary aggregated from Clawdbot session logs.
* CLI: `clawdbot status --usage` prints a full per-provider breakdown.
* CLI: `clawdbot channels list` prints the same usage snapshot alongside provider config (use `--no-usage` to skip).
* macOS menu bar: “Usage” section under Context (only if available).

## Providers + credentials

* **Anthropic (Claude)**: OAuth tokens in auth profiles.
* **GitHub Copilot**: OAuth tokens in auth profiles.
* **Gemini CLI**: OAuth tokens in auth profiles.
* **Antigravity**: OAuth tokens in auth profiles.
* **OpenAI Codex**: OAuth tokens in auth profiles (accountId used when present).
* **MiniMax**: API key (coding plan key; `MINIMAX_CODE_PLAN_KEY` or `MINIMAX_API_KEY`); uses the 5‑hour coding plan window.
* **z.ai**: API key via env/config/auth store.

Usage is hidden if no matching OAuth/API credentials exist.