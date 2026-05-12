---
title: Secret Redaction | Support & Community | Warp
url: https://docs.warp.dev/support-and-community/privacy-security-and-licensing/secret-redaction
source: sitemap
fetched_at: 2026-04-29T15:05:52.538667021-03:00
rendered_js: false
word_count: 226
summary: This document explains how to configure and utilize the Secret Redaction feature to detect and protect sensitive information like API keys and passwords within the terminal.
tags:
    - security
    - privacy
    - secret-management
    - regex
    - data-protection
    - terminal-security
category: guide
optimized: true
optimized_at: 2026-04-29T00:00:00Z
---
Secret Redaction detects sensitive data (secrets, passwords, API keys, PII) using regex patterns and prevents it from being sent to Warp servers or LLM providers. Disabled by default.

## Enable it

Open **Settings** > **Privacy** > **Secret redaction**, or type "Secret Redaction" in the [Command Palette](https://docs.warp.dev/terminal/command-palette).

## How it works

Detected secrets are redacted instead of being sent to servers. Warp Drive also prevents saving secrets in plain text (workflows, MCP servers, prompts). Warp ships with a recommended regex list you can use directly. Add custom regex in **Settings** > **Privacy** > **Secret redaction** > **Custom secret redaction**.

## Visually hiding secrets

By default, secrets display with strikethrough: `echo password`. To show `echo ********` instead, enable **Settings** > **Privacy** > **Secret redaction** > **Hide secrets in blocklist**.

Click a secret to reveal it or copy from the tooltip. When copying terminal output containing secrets, it copies as asterisks unless revealed or copied from the tooltip. Secret redaction does **not** apply in [Session Sharing](https://docs.warp.dev/knowledge-and-collaboration/session-sharing/).

## Case sensitivity

Regexes are case-sensitive by default. Use `(?i)` to make them case-insensitive: `(?i)password` matches `PASSWORD`, `Password`, and `password`.

## Secret regex list

Recommended regular expressions for identifying secrets:

```regex
\b((25[0-5]|(2[0-4]|1\d|[1-9]|)\d)\.?\b){4}\b
\b((([0-9A-Fa-f]{1,4}:){1,6}:)|(([0-9A-Fa-f]{1,4}:){7}))([0-9A-Fa-f]{1,4})\b
\xapp-[0-9]+-[A-Za-z0-9_]+-[0-9]+-[a-f0-9]+\b
\b(\+\d{1,2}\s)?\(?\d{3}\)?[\s.-]\d{3}[\s.-]\d{4}\b
\b(AKIA|A3T|AGPA|AIDA|AROA|AIPA|ANPA|ANVA|ASIA)[A-Z0-9]{12,}\b
\b((([a-zA-z0-9]{2}[-:]){5}([a-zA-z0-9]{2}))|(([a-zA-z0-9]{2}:){5}([a-zA-z0-9]{2})))\b
\bAIza[0-9A-Za-z-_]{35}\b
\b[0-9]+-[0-9A-Za-z_]{32}\.apps\.googleusercontent\.com\b
\bsk-ant-api\d{0,2}-[a-zA-Z0-9\-]{80,120}\b
\b(ey[a-zA-z0-9_\-=]{10,}\.){2}[a-zA-z0-9_\-=]{10,}\b
\b([a-z0-9-]){1,30}(\.firebaseapp\.com)\b
\b(?:r|s)k_(test|live)_[0-9a-zA-Z]{24}\b
\bgithub_pat_[A-Za-z0-9_]{82}\b
```

**GitHub tokens (named):**

- GitHub Classic Personal Access Token
- GitHub Fine Grained Personal Access Token
- GitHub OAuth Access Token
- GitHub User to Server Token
- GitHub Server to Server Token
