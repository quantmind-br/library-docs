---
title: 'GitHub MCP: Summarizing PRs & Creating Issues | Guides | Warp'
url: https://docs.warp.dev/guides/external-tools-and-integrations/github-mcp-summarizing-open-prs-and-creating-gh-issues
source: sitemap
fetched_at: 2026-04-29T15:06:48.939268217-03:00
rendered_js: false
word_count: 216
summary: This document provides instructions on setting up the GitHub MCP server within the Warp terminal to automate repository tasks such as summarizing pull requests and creating issues from code comments.
tags:
    - github-integration
    - warp-terminal
    - mcp-server
    - automation
    - workflow-optimization
    - developer-productivity
category: guide
optimized: true
optimized_at: 2026-04-29T15:06:48.939268217-03:00
---
The GitHub MCP Server lets Warp agents read, write, and automate tasks in GitHub repositories directly — no manual tab-switching required.

## Setup

### Step 1. Get a GitHub Personal Access Token

1. Go to **GitHub → Settings → Developer Settings → Personal Access Tokens**
2. Create a new token and enable:
   - `repo`
   - `read:user`

### Step 2. Add the Server in Warp

1. Open the **MCP Panel** via Command Palette (`Cmd + P`)
2. Click **Add Server**
3. Paste in your JSON config and the access token
4. Save — available endpoints appear immediately

## Workflow 1 — Summarize All Open PRs

Use Warp's agent to summarize pull requests. The MCP server:

- Lists PRs
- Fetches comments and reviews
- Compiles summaries with clickable links

Perfect for daily PR triage or stand-ups.

## Workflow 2 — Create GitHub Issues from TODOs

Use a saved prompt to automate issue creation:

1. Warp scans your codebase for TODO comments
2. Calls `create_issue` for each one via MCP
3. Generates a linked list of new issues

This turns scattered notes into trackable tickets instantly.

## Why It's Useful

- Save 20–30 minutes per session
- Keep repos synchronized automatically
- Enable PR summaries, issue tracking, and automation — all inside Warp

#github-integration #warp-terminal #mcp-server #automation #workflow-optimization
