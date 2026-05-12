---
title: Thread Map
url: https://ampcode.com/news/thread-map
source: crawler
fetched_at: 2026-02-06T02:08:15.02937524-03:00
rendered_js: false
word_count: 356
summary: This document introduces the Thread Map feature in the Amp CLI, which visualizes connections between related conversation threads and identifies common organizational patterns like hub-and-spokes and chains.
tags:
    - amp-cli
    - thread-management
    - workflow-visualization
    - context-optimization
    - thread-mapping
    - productivity-tools
category: concept
---

Two days ago, Lewis wrote about [working with short threads](https://ampcode.com/200k-tokens-is-plenty) — a lot of them, connected via [handoff](https://ampcode.com/manual#handoff) and [thread mentions](https://ampcode.com/manual#referencing-threads) and forks. In his post, he showed a diagram, a *map* of one feature spread across 13 threads.

That map? It exists now, we built it:

![Old whisperer of the orb reading a thread map](https://ampcode.com/%28marketing%29/news/thread-map2.jpg)

Run `threads: map` in the [Amp CLI command palette](https://ampcode.com/news/command-palette) to try it out.

You'll see a top-down view of all threads connected to your current thread via mentions, handoffs, or forks. If you hit `Enter`, you'll open the selected thread and can continue your work there.

(Yes, it's only available in the Amp CLI right now, but coming to other clients soon.)

If you only use handoff and forks occasionally, you might not need this yet. But if you do work with many short, connected threads — like [Lewis](https://ampcode.com/200k-tokens-is-plenty) or [Igor](https://x.com/bedesqui/status/1998374596144406754) — this map might make it even easier, because you can see the *shape* of your work.

Here are some patterns we've noticed so far:

## 1. Hub-and-Spokes

![Bicycle spokes pattern](https://static.ampcode.com/news/thread-map-bicycle-spokes.png)

One thread will form a core from which many other threads can be created. This might be an initial implementation thread, or a context-gathering research thread. The spokes might be refactoring threads, or subfeatures. They don't need the context of the other spokes—by linking only to the hub thread, the context window of each spoke remains lean and relevant.

## 2. Chain

![Chains pattern](https://static.ampcode.com/news/thread-map-chains.png)

Many short threads chained together. This is a common pattern when one change depends on another. This pattern often emerges when using the `handoff` feature to extract only the relevant context from a previous thread, allowing you to keep threads short but still continue serially dependent work. This is common in research or exploratory tasks, where the desired state is unknown.

It's not uncommon for the end of a chain to lead to the central node of a hub-and-spokes pattern; a desired state is found and work can be more easily parallelised.

## What's Next?

Our bet is that there are many more patterns out there, waiting to be recognised. Let us know what you find.

![Thread map patterns](https://static.ampcode.com/news/thread-map-patterns-slow.gif)