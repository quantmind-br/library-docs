---
title: Hermes Agent Documentation | Hermes Agent
url: https://hermes-agent.nousresearch.com/docs/
source: crawler
fetched_at: 2026-04-24T16:59:57.553768895-03:00
rendered_js: false
word_count: 492
summary: This document introduces the Hermes Agent, an autonomous AI agent characterized by a built-in learning loop that allows it to create, improve, and persist skills across sessions. It outlines its versatility, detailing how it can run on various infrastructures and interface with numerous platforms.
tags:
    - ai-agent
    - autonomous-system
    - self-improving
    - learning-loop
    - nous-research
    - tool-calling
category: guide
---

The self-improving AI agent built by [Nous Research](https://nousresearch.com). The only agent with a built-in learning loop — it creates skills from experience, improves them during use, nudges itself to persist knowledge, and builds a deepening model of who you are across sessions.

## What is Hermes Agent?[​](#what-is-hermes-agent "Direct link to What is Hermes Agent?")

It's not a coding copilot tethered to an IDE or a chatbot wrapper around a single API. It's an **autonomous agent** that gets more capable the longer it runs. It lives wherever you put it — a $5 VPS, a GPU cluster, or serverless infrastructure (Daytona, Modal) that costs nearly nothing when idle. Talk to it from Telegram while it works on a cloud VM you never SSH into yourself. It's not tied to your laptop.

## Quick Links[​](#quick-links "Direct link to Quick Links")

🚀 [**Installation**](https://hermes-agent.nousresearch.com/docs/getting-started/installation)Install in 60 seconds on Linux, macOS, or WSL2📖 [**Quickstart Tutorial**](https://hermes-agent.nousresearch.com/docs/getting-started/quickstart)Your first conversation and key features to try🗺️ [**Learning Path**](https://hermes-agent.nousresearch.com/docs/getting-started/learning-path)Find the right docs for your experience level⚙️ [**Configuration**](https://hermes-agent.nousresearch.com/docs/user-guide/configuration)Config file, providers, models, and options💬 [**Messaging Gateway**](https://hermes-agent.nousresearch.com/docs/user-guide/messaging)Set up Telegram, Discord, Slack, or WhatsApp🔧 [**Tools & Toolsets**](https://hermes-agent.nousresearch.com/docs/user-guide/features/tools)47 built-in tools and how to configure them🧠 [**Memory System**](https://hermes-agent.nousresearch.com/docs/user-guide/features/memory)Persistent memory that grows across sessions📚 [**Skills System**](https://hermes-agent.nousresearch.com/docs/user-guide/features/skills)Procedural memory the agent creates and reuses🔌 [**MCP Integration**](https://hermes-agent.nousresearch.com/docs/user-guide/features/mcp)Connect to MCP servers, filter their tools, and extend Hermes safely🧭 [**Use MCP with Hermes**](https://hermes-agent.nousresearch.com/docs/guides/use-mcp-with-hermes)Practical MCP setup patterns, examples, and tutorials🎙️ [**Voice Mode**](https://hermes-agent.nousresearch.com/docs/user-guide/features/voice-mode)Real-time voice interaction in CLI, Telegram, Discord, and Discord VC🗣️ [**Use Voice Mode with Hermes**](https://hermes-agent.nousresearch.com/docs/guides/use-voice-mode-with-hermes)Hands-on setup and usage patterns for Hermes voice workflows🎭 [**Personality & SOUL.md**](https://hermes-agent.nousresearch.com/docs/user-guide/features/personality)Define Hermes' default voice with a global SOUL.md📄 [**Context Files**](https://hermes-agent.nousresearch.com/docs/user-guide/features/context-files)Project context files that shape every conversation🔒 [**Security**](https://hermes-agent.nousresearch.com/docs/user-guide/security)Command approval, authorization, container isolation💡 [**Tips & Best Practices**](https://hermes-agent.nousresearch.com/docs/guides/tips)Quick wins to get the most out of Hermes🏗️ [**Architecture**](https://hermes-agent.nousresearch.com/docs/developer-guide/architecture)How it works under the hood❓ [**FAQ & Troubleshooting**](https://hermes-agent.nousresearch.com/docs/reference/faq)Common questions and solutions

## Key Features[​](#key-features "Direct link to Key Features")

- **A closed learning loop** — Agent-curated memory with periodic nudges, autonomous skill creation, skill self-improvement during use, FTS5 cross-session recall with LLM summarization, and [Honcho](https://github.com/plastic-labs/honcho) dialectic user modeling
- **Runs anywhere, not just your laptop** — 6 terminal backends: local, Docker, SSH, Daytona, Singularity, Modal. Daytona and Modal offer serverless persistence — your environment hibernates when idle, costing nearly nothing
- **Lives where you do** — CLI, Telegram, Discord, Slack, WhatsApp, Signal, Matrix, Mattermost, Email, SMS, DingTalk, Feishu, WeCom, BlueBubbles, Home Assistant — 15+ platforms from one gateway
- **Built by model trainers** — Created by [Nous Research](https://nousresearch.com), the lab behind Hermes, Nomos, and Psyche. Works with [Nous Portal](https://portal.nousresearch.com), [OpenRouter](https://openrouter.ai), OpenAI, or any endpoint
- **Scheduled automations** — Built-in cron with delivery to any platform
- **Delegates & parallelizes** — Spawn isolated subagents for parallel workstreams. Programmatic Tool Calling via `execute_code` collapses multi-step pipelines into single inference calls
- **Open standard skills** — Compatible with [agentskills.io](https://agentskills.io). Skills are portable, shareable, and community-contributed via the Skills Hub
- **Full web control** — Search, extract, browse, vision, image generation, TTS
- **MCP support** — Connect to any MCP server for extended tool capabilities
- **Research-ready** — Batch processing, trajectory export, RL training with Atropos. Built by [Nous Research](https://nousresearch.com) — the lab behind Hermes, Nomos, and Psyche models