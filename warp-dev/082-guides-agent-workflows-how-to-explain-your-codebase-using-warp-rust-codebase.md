---
title: Explain Your Codebase with Agents | Guides | Warp
url: https://docs.warp.dev/guides/agent-workflows/how-to-explain-your-codebase-using-warp-rust-codebase
source: sitemap
fetched_at: 2026-04-29T15:06:24.538759277-03:00
rendered_js: false
word_count: 124
summary: This document explains how to utilize the Warp AI agent to perform semantic and symbol-level searches for navigating and understanding complex codebases.
tags:
    - ai-coding-assistant
    - code-navigation
    - semantic-search
    - symbolic-search
    - developer-tools
    - code-analysis
category: tutorial
optimized: true
optimized_at: 2026-04-29T00:00:00Z
---
Use Warp's AI agent to explore unfamiliar codebases via semantic and symbol-level search.

## Overview

- How Warp explains unknown code sections
- How it combines semantic and keyword searches
- How to use these insights to modify UI components

## Example Prompt

```
Please explain how the agent popup code is structured,
where it lives in the codebase,
and how it is rendered and called.
I want to understand the full data flow and structure
so I can add a new agent button to it.
```

## How Warp's Agent Searches

1. Uses **semantic (vectorized) search** to locate relevant files
2. Switches to **symbolic search** (`grep` + direct code reads) for probable matches (e.g., `agent_management_popup.rs`)
3. Intelligently reads large files in chunks to extract relevant definitions and render logic

## Generated Explanation

Warp returns a full breakdown:

- File paths where the component is defined
- How it's rendered within the workspace
- Which actions and UI components trigger it
- Step-by-step data flow through the component
