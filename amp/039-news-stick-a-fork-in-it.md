---
title: Stick a Fork in It, It's Done
url: https://ampcode.com/news/stick-a-fork-in-it
source: crawler
fetched_at: 2026-02-06T02:08:09.747698318-03:00
rendered_js: false
word_count: 277
summary: This document announces the deprecation of the fork command in Amp and provides instructions on using handoff and thread mentions as more efficient alternatives for context sharing.
tags:
    - thread-management
    - context-sharing
    - amp-workflow
    - handoff
    - thread-mentions
    - thread-navigation
category: guide
---

We're ripping out the Fork command.

We added [thread forking](https://ampcode.com/news/thread-forking) back in July 2025 (now ancient, primordial history) as a way to conveniently share context for branching experiments or side quests in Amp.

Today we have better ways of sharing context between threads: [handoff](https://ampcode.com/manual#handoff) and [thread mentions](https://ampcode.com/manual#referencing-threads), which treat threads as first-class stores of context.

Perhaps there is a great potential UX out there for `fork`, but we want Amp to be simple as well as powerful. We'd rather spend our time perfecting `handoff` and `thread mentions` than support `fork`.

## Handoff

[Handoff](https://ampcode.com/news/handoff) is great for extracting useful context from your thread for the next goal at hand. This means you can start a new thread with only the necessary context.

- Use `thread: handoff` from the command palette.
- Prompt your task and a new thread will be started with the necessary context already in the prompt.

## Thread Mentions

Thread mentions let you pull information from other threads into your current thread. You can reference multiple threads, merging context from many sources.

- Use `thread:new` and then use the `enter` shortcut to start a new thread with a reference to the main thread.
- Or, use `@@` to search for the thread you want to pull context from.
- Once you run your prompt, Amp will [read the threads](https://ampcode.com/news/read-threads) and extract context pertinent to your task.

## Managing Threads

Using new threads as branches leads to many threads, often running in parallel. To manage them:

- use `thread: switch to previous` or `thread: switch to parent` to return to the main thread.
- use the [`thread: map`](https://ampcode.com/news/thread-map) to get a birds eye view and easily navigate back to the main thread (CLI only for now).