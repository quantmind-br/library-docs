---
title: 'Module 3: Custom Workflows - Zencoder Docs'
url: https://docs.zencoder.ai/learn/10x-engineer/module-03
source: crawler
fetched_at: 2026-01-23T09:28:31.863328283-03:00
rendered_js: false
word_count: 214
summary: This module explains how to customize AI agents by configuring global instructions, managing Zencoder rules, creating custom agent roles, and integrating MCP tools.
tags:
    - agent-configuration
    - zencoder-rules
    - custom-agents
    - mcp-tools
    - workflow-integration
category: tutorial
---

## Intro

Module 3 personalizes the agent stack: capturing reusable instructions and rules, shaping bespoke agents (or borrowing from the library), and wiring MCP tools so every workflow matches your team’s policies and integrations.

## Video lesson

Preview lesson. The full video is available on Udemy.

## Key takeaways

- Use global Instructions for always-on guidance, and store reusable Zencoder Rules in `.zencoder/rules/*.md` so the whole project inherits consistent behaviours.
- Tweak each rule’s `always_apply` flag or mention it ad hoc; leverage `globs` to target file types (e.g., Markdown style guides) and keep shared rules in version control.
- Remember that repo-info output (`repo.md`) is itself an auto-applied rule, giving downstream agents immediate architectural context.
- Build custom agents by setting name, alias, instructions, and tool access; and save them in the custom tab.
- Browse the agent library for prebuilt roles (architecture reviews, etc.), clone them with one click, and adapt tooling or prompts as needed.
- Share vetted custom agents with your org by switching scope from personal to org; manage shared catalog entries through the web dashboard.
- Expand agent capabilities by installing MCP tools: some are one-click (Playwright E2E, Context7 docs) while others require OAuth or API tokens (InstantDB, GitHub).
- After installation, confirm new tools appear for the right agents and prune unused ones to avoid overwhelming default agent menus.