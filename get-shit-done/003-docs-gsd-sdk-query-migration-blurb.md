---
title: Gsd sdk query migration blurb
url: https://github.com/gsd-build/get-shit-done/blob/main/docs/gsd-sdk-query-migration-blurb.md
source: git
fetched_at: 2026-04-16T16:20:07.999943637-03:00
rendered_js: false
word_count: 238
summary: This document outlines the transition from the monolithic gsd-tools subprocess to the new gsd-sdk query system, highlighting improvements in type safety, error handling, and operational stability.
tags:
    - sdk-migration
    - gsd-sdk
    - query-system
    - api-refactoring
    - workflow-optimization
    - cli-replacement
category: concept
---

# GSD SDK query migration (summary blurb)

Copy-paste friendly for Discord and GitHub comments.

---

**@gsd-build/sdk** replaces the untyped, monolithic `gsd-tools.cjs` subprocess with a typed, tested, registry-based query system and **`gsd-sdk query`**, giving GSD structured results, classified errors (`GSDQueryError`), and golden-verified parity with the old CLI. That gives the framework one stable contract instead of a fragile, very large CLI that every workflow had to spawn and parse by hand.

**What users can expect**

- Same GSD commands and workflows they already use.
- Snappier runs (less Node startup on chained tool calls).
- Fewer mysterious mid-workflow failures and safer upgrades, because behavior is covered by tests and a single stable contract.
- Stronger predictability: outputs and failure modes are consistent and explicit.

**Cost and tokens**

The SDK does not automatically reduce LLM tokens per model call. Savings show up indirectly: fewer ambiguous tool results and fewer retry or recovery loops, which often lowers real-world session cost and wall time.

**Agents then vs now**

Agents always followed workflow instructions. What improved is the surface those steps run on. Before, workflows effectively said to shell out to `gsd-tools.cjs` and interpret stdout or JSON with brittle assumptions. Now they point at **`gsd-sdk query`** and typed handlers that return the shapes prompts expect, with clearer error reasons when something must stop or be fixed, so instruction following holds end to end with less thrash from bad parses or silent output drift.
