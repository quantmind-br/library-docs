---
title: Understand a Large Codebase with Agents | Guides | Warp
url: https://docs.warp.dev/guides/agent-workflows/understanding-your-codebase
source: sitemap
fetched_at: 2026-04-29T15:06:29.998401457-03:00
rendered_js: false
word_count: 249
summary: This document introduces Warp's Codebase Context, a semantic search tool designed to help developers understand and navigate complex, multi-repository codebases for faster onboarding and feature development.
tags:
    - codebase-context
    - semantic-search
    - developer-productivity
    - onboarding-tool
    - code-indexing
category: concept
optimized: true
optimized_at: 2026-04-29T15:04:00Z
---
Kevin, who worked on Warp's Windows and Linux builds, wanted to jump into a feature he hadn't touched before: Block Sharing. This feature spans two codebases — Warp's client (Rust) and server (Go) — making onboarding tough. That's where Codebase Context comes in.

## What is Codebase Context?

Warp's Codebase Context uses semantic search to understand your code. It doesn't rely on exact function or variable names — instead, it searches based on meaning. Use it through a shared workflow in Warp Drive.

The workflow tells Warp to:

- Search across both client and server codebases
- Summarize how a feature works end-to-end
- Include clickable links to relevant files

## Real example: Block Sharing

Kevin types `block sharing` into Warp's shared workflow. Warp:

1. Searches the client codebase for the rendering logic
2. Searches the server codebase for GraphQL handlers
3. Generates a summary combining both perspectives

The output includes:

- Architecture overview
- Linked file paths
- Function and module summaries

No more manual onboarding or guessing file names.

## Incremental syncing

Whenever you change a file in an indexed repo:

- Warp detects the update automatically
- Re-embeds just that file
- Keeps your code context fresh

That means agents never reference stale code.

## Why it's game-changing

Codebase Context helps teams:

- Understand large or unfamiliar codebases
- Onboard faster
- Jump between client and server logic seamlessly
- Generate accurate, clickable documentation

> [!example]
> "This saved us hours of one-on-one walkthroughs." — Lucy