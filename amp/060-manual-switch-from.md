---
title: Switch to Amp
url: https://ampcode.com/manual/switch-from#claude-code
source: crawler
fetched_at: 2026-02-06T02:07:51.651628826-03:00
rendered_js: false
word_count: 583
summary: This document provides a comprehensive migration guide for users switching from Claude Code to the Amp coding agent, highlighting benefits, equivalent features, and configuration steps.
tags:
    - migration-guide
    - claude-code
    - coding-agents
    - cli-tools
    - developer-productivity
    - ai-tools
category: guide
---

## **Welcome to Amp.** Here's how to switch from other coding agents.

*We want this page to be fair and helpful. Email [amp-devs@ampcode.com](mailto:amp-devs@ampcode.com) or post on X to [@AmpCode](https://x.com/AmpCode) with feedback.*

## From Claude Code[#](#claude-code)[#](#claude-code)

### Benefits of Amp[#](#benefits-of-amp)[#](#benefits-of-amp)

People who switch from Claude Code to Amp usually cite some of the following reasons:

- **[More polished CLI and editor extensions](https://ampcode.com/manual#get-started):** The Amp CLI doesn’t flicker, because we built it on a custom high-performance TUI framework. We’ve also heard from many people that Amp’s VS Code extension is superior to Claude Code’s native VS Code extension.
- [**GPT-5.2 in the oracle**](https://ampcode.com/manual#oracle): You can invoke GPT-5.2 in Amp by asking it to “use the oracle”, which brings GPT-5.2’s superior reasoning capabilities to bear on complex problems.
- [**Use of non-Claude models when needed**](https://ampcode.com/models): Amp uses other models when they’re best, such as Gemini 3 for code review and image generation, and GPT-5.2 for the oracle (mentioned above).
- [**Thread sharing**](https://ampcode.com/manual#thread-sharing): Amp’s thread sharing feature allows you to easily share threads with your team, which helps with code review, debugging, and teaching others how to use coding agents.
- [**Free daily grant**](https://ampcode.com/free): Amp gives you $10/day of free usage when you’re eligible for and have enabled the daily grant. Depending on your usage patterns, Amp may cost you less than Claude Max’s $200/month plan even if you supplement your free daily grant with paid usage on top.

### What's Missing in Amp[#](#whats-missing-in-amp)[#](#whats-missing-in-amp)

- [Custom subagents](https://docs.claude.com/en/docs/claude-code/sub-agents) and [plugins](https://docs.claude.com/en/docs/claude-code/plugins): Armin Ronacher’s [Agentic Coding Things That Didn’t Work](https://lucumr.pocoo.org/2025/7/30/things-that-didnt-work/) captures our general sentiment here. Our first priority is something more basic: making it easy and commonplace to write custom tools for your codebase. We’ll consider more complex solutions (like plugins and custom subagents, but not all of them) once we see this more basic problem solved, by us or anyone else.
- [Hooks](https://docs.claude.com/en/docs/claude-code/hooks-guide): We haven’t implemented these yet (except an internal implementation we’re dogfooding). We think they could be valuable in some cases.
- [Claude Code on the web](https://docs.claude.com/en/docs/claude-code/claude-code-on-the-web): We are currently dogfooding a web-based async Amp agent, but it’s not available externally yet.
- [Monthly subscription plans](https://www.claude.com/pricing/max): Amp doesn’t have a monthly subscription plan, but we do have automatic monthly top-ups if you want to set a budget. When using Amp’s `smart` mode, you can set up minimum threshold automatic top-ups and you will *never* hit rate limits, unlike in Claude Code. You can also use Amp’s [free daily grant](https://ampcode.com/free) completely free of charge.

### Use the Oracle for Planning[#](#use-the-oracle-for-planning)[#](#use-the-oracle-for-planning)

**Claude Code plan mode** → **Amp [oracle](https://ampcode.com/manual#oracle) and [handoff](https://ampcode.com/manual#handoff)**

When you need deep reasoning or planning in Amp, ask it to “use the oracle”. The oracle uses GPT-5.2 to help with complex analysis and planning tasks. Then, after the oracle has generated a plan, continue in that thread or use `/handoff` to draft a new thread with the relevant context.

### Equivalent Features[#](#equivalent-features)[#](#equivalent-features)

- Claude Code’s [skills](https://docs.claude.com/en/docs/claude-code/skills) in `.claude/skills/` → Amp’s [agent skills](https://ampcode.com/news/agent-skills) in `.agents/skills/` (also supports `.claude/skills/` for compatibility)
- `claude -p <prompt>` → `amp -x <prompt>` (for executing a single prompt non-interactively)
- Claude Code’s [settings](https://docs.claude.com/en/docs/claude-code/settings) in `~/.claude/settings.json` → Amp’s [settings](https://ampcode.com/manual#configuration) in `~/.config/amp/settings.json`
- Claude Code’s [permissions](https://docs.claude.com/en/docs/claude-code/iam#access-control-and-permissions) → Amp’s [permissions](https://ampcode.com/manual#permissions)
- Claude Code’s [MCP support](https://docs.claude.com/en/docs/claude-code/mcp) → Amp’s [MCP support](https://ampcode.com/manual#mcp)
- Claude’s [Agent SDK](https://docs.claude.com/en/api/agent-sdk/overview) → [Amp SDK](https://ampcode.com/manual/sdk)

### Rename Your Agent Files (Optional)[#](#configuration-files)[#](#configuration-files)

Claude Code uses files named [`CLAUDE.md`](https://docs.claude.com/en/docs/claude-code/memory). Amp uses [`AGENTS.md`](https://ampcode.com/manual/#AGENTS.md) (following the [AGENTS.md](https://agents.md) convention).

No migration is needed. If no `AGENTS.md` file exists in a directory, Amp will read `CLAUDE.md`. However, we recommend using the `AGENTS.md` filename because it is more conventional: `mv CLAUDE.md AGENTS.md && ln -s AGENTS.md CLAUDE.md` for each `CLAUDE.md` file in your repository.