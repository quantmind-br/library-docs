---
title: Credits | Support & Community | Warp
url: https://docs.warp.dev/support-and-community/plans-and-billing/credits
source: sitemap
fetched_at: 2026-04-29T15:05:47.241647616-03:00
rendered_js: false
word_count: 794
summary: This document explains how Warp credits function, detailing the factors that influence usage, how to track consumption, and the distinction between standard and cloud agent credits.
tags:
    - warp-credits
    - billing-and-usage
    - agent-platform
    - ai-compute
    - cost-management
    - cloud-agents
category: concept
optimized: true
optimized_at: 2026-04-29T00:00:00Z
---
Credits power all Warp Agent interactions, scaling with token usage rather than per-prompt.

## What are Warp credits?

Any interaction with Warp's Agent consumes credits. Credits are primarily based on AI usage — the number of credits a task consumes varies based on the size and complexity of your codebase, the size of the task, the model you're using, the amount of context the agent needs to gather, and more.

Credits also include a small hosting fee, charged only when running agents in the cloud, hosted on Warp's infrastructure. For details on cloud agent credits, see [[291-support-and-community-plans-and-billing-credits#cloud-agent-credits]].

Each interaction consumes **at least one credit**, though more complex interactions may use **multiple credits**. Because of factors such as codebase size, model choice, number of tool calls, and the nature of LLMs, credit usage is **non-deterministic** — two similar prompts can still use a different number of credits.

> [!tip]
> Build an intuitive understanding by experimenting with different prompts, models, and tracking how many credits they consume.

### Tracking your credit usage

In an Agent conversation, a **turn** represents a single exchange (a response from the LLM). To see how many credits a turn consumed, hover over the **credit count chip** at the bottom of the Agent's response.

You can view your total credit usage, along with other billing details, in **Settings** > **Billing and usage**.

## Credit limits and billing

- **Seat-level allocation**: On team plans, credit limits apply per seat — each team member has their own allowance. Individual users (not on a team) also have their own credit allocation.
- **Cloud Agent Credits**: Individual users can run cloud agents via CLI/API using their normal Warp credits, [[291-support-and-community-plans-and-billing-credits#cloud-agent-credits]], or a Build plan with available credits. Integrations (Slack, Linear) require team membership.
- **Hitting the credit limits**: Once you hit your monthly credit limit, your access depends on your plan. On the Free plan, AI access stops until your next billing cycle. On paid plans, you can continue using AI with usage-based billing via [[289-support-and-community-plans-and-billing-add-on-credits]].

## Other features that use credits

In addition to direct Agent conversations, the following features also consume credits:

- **Generate** — helps you look up commands and suggestions as you type. Multiple credits may be used before you select a final suggestion.

> [!note]
> Regular shell commands in Warp do not consume or count towards credits.

## How are Warp credits calculated?

A **credit** in Warp is a unit of work representing the total processing required to complete an interaction with an Agent. It scales with the number of tokens processed — **the more tokens used, the more credits consumed**.

Factors affecting credit usage:

1. **The LLM model used** — Smaller, faster models consume fewer credits than larger, reasoning-based models. Claude Opus 4.6 and 4.5 tend to consume the most, followed by Claude Sonnet 4.6, GPT-5.4, GPT-5.3 Codex, Gemini 3 Pro, and others. This generally correlates with model pricing.

   > [!tip]
   > If your task doesn't require deep reasoning, planning, or multi-step problem solving, choose a more lightweight model.

2. **Tool calls triggered by the Agent** — Warp's Agents make various tool calls including file searches (grep), file retrieval and reading, code diffs, web/documentation context, and other utilities. More tool calls = more credits.

3. **Task complexity and number of steps** — Simple tasks require only a quick response. Complex tasks involve planning, intermediate outputs, verification, applying changes, and self-correcting — each adding to the credits count.

   > [!tip]
   > Keep tasks well-scoped, work incrementally, and break large changes into smaller steps.

4. **Amount of context passed to the model** — Large prompts with attached blocks, long user messages, or file attachments (like images) increase token consumption and credit usage.

   > [!tip]
   > When sharing logs, code, or other large content, attach only the most relevant portions.

5. **Prompt caching (hits and misses)** — Model prompts often include repeated content. **Cache hits** reuse results from past requests, reducing tokens and latency. **Cache misses** require full reprocessing, increasing credits.

   > [!tip]
   > Work in a continuous session when possible to improve cache hit rates.

## Cloud Agent Credits

Cloud Agent Credits are consumed only by cloud agent runs — AI requests that run on Warp-hosted compute.

### Eligible for Cloud Agent Credits

- **First-party integrations** — Running agents through Slack or Linear integrations
- **Cloud agent runs** — Using `oz agent run-cloud` via the CLI
- **Oz API** — Running agents through Warp's Oz API
- **Cloud Mode** — Running an agent from Cloud Mode in the Warp app

### Not eligible for Cloud Agent Credits

- **Local agent runs** — Using `oz agent run` on your local machine
- **Self-hosted compute** — Using `oz agent run` on GitHub Actions, CI/CD pipelines, or other self-hosted infrastructure

#warp-credits #billing-and-usage #cloud-agents
