---
title: Rush Mode
url: https://ampcode.com/news/rush-mode
source: crawler
fetched_at: 2026-02-06T02:07:52.71310175-03:00
rendered_js: false
word_count: 247
summary: This document introduces Amp's 'rush' mode, a faster and more cost-effective agent setting optimized for simple coding tasks and small bug fixes.
tags:
    - amp-editor
    - rush-mode
    - cost-efficiency
    - performance-benchmarks
    - coding-tools
category: guide
---

Amp has a new mode: `rush`, named so because a rushed job is faster and cheaper in the moment, and sometimes that's more important than quality.

Token-by-token, it's 67% cheaper and 50% faster than `smart`.

Prompt-to-result (what you actually care about)? It depends. It's less capable, which means that on complex tasks it often spends more tokens and time fixing its mistakes along the way.

You can `rush` small, well-defined tasks: simple bugs, small UI changes, minor features. For best results, mention the files that need to be changed.

Don't `rush` complex tasks: new end-to-end features, bugs with no clear diagnosis, an architecture refactor. It'll be slower and not much cheaper, if it even arrives at a solution at all. Use `smart` instead.

For example:

- A small `rush`-able task that took 37 seconds and cost $0.12 (44% faster and 77% cheaper than `smart`): ["warn if there are more than 20 MCP tools..."](https://ampcode.com/threads/T-62d6f9c3-4859-4dbe-a0ec-0460e2a3707a)
- A complex, non-`rush`-worthy refactor where `rush` took 2x longer than `smart` and was just 19% cheaper: ["refactor all hardcoded colors from the CLI and web UI..."](https://ampcode.com/threads/T-aae44811-8790-4ea5-9841-ad85014db950)

The `rush` agent mode is a unique combination of system prompt, tools, and model (Haiku 4.5 for now). You can use all of Amp's [subagents](https://ampcode.com/models) in `rush` mode, including [the oracle](https://ampcode.com/manual#oracle) and [the librarian](https://ampcode.com/manual#librarian). You'll also notice it doesn't show its TODOs, which makes it faster.

To use it: run command `mode: use rush` in the Amp CLI, or select `rush` mode in the Amp editor extension's prompt field.