---
title: Continue-As-New | Mistral Docs
url: https://docs.mistral.ai/studio-api/workflows/building-workflows/continue_as_new
source: sitemap
fetched_at: 2026-04-26T04:13:39.686023502-03:00
rendered_js: false
word_count: 113
summary: This document explains how to use the Continue-As-New pattern to manage long-running workflows by resetting event history while preserving application state.
tags:
    - workflow-orchestration
    - event-history
    - long-running-processes
    - state-management
    - workflow-optimization
category: concept
optimized: true
optimized_at: 2026-04-26T00:00:00Z
---

Continue-As-New resets the workflow's event history while carrying forward its state, enabling indefinitely long-running workflows without hitting history size limits.

## When to Use

- Long-running workflows that iterate indefinitely
- When workflow history approaches size limits (~50K events or 50MB)
- Workflows that need to run for weeks or months

## Behavior

When `continue_as_new()` is called, the current run completes and a new run starts fresh from the beginning with the provided state. All accumulated event history is discarded.

> [!important] Your workflow's `run` method must accept a state parameter to restore its state when continuing as new.

## Checking History Size

Use `should_continue_as_new()` to check whether it's time to reset. This returns `True` when the event history is approaching the system limit.