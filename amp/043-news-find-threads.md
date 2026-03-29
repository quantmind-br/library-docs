---
title: Find Threads
url: https://ampcode.com/news/find-threads
source: crawler
fetched_at: 2026-02-06T02:08:21.008506051-03:00
rendered_js: false
word_count: 258
summary: This document introduces the find_thread tool for Amp, which enables users to search historical conversation threads using keywords or by identifying threads that modified specific files.
tags:
    - amp-platform
    - thread-search
    - find-thread-tool
    - context-retrieval
    - file-search
category: guide
---

Amp can now search your threads.

A few weeks ago we shipped [the ability to read other threads](https://ampcode.com/news/read-threads). That was the first step: reference a thread by ID or URL, let Amp pull out the relevant context.

But what if you don't have the thread ID at hand? What if the only thing you know about a thread is that it changed or created a specific file? Or some keywords?

That's what the new `find_thread` tool is for. It lets Amp search your threads in two ways:

**Keyword search**: find threads that mention specific terms. "Find threads where we discussed the database migration." The agent in Amp will then use the same search functionality as on [the thread feed](https://ampcode.com/threads) and return matches.

**File search**: find threads that touched a specific file. Think of it like `git blame`, but for Amp. "Which thread last modified this file?" Amp looks at file changes across threads and tells you which conversations touched it.

Here's how we've been using it to find threads:

- "Which Amp thread created core/src/tools/tool-service.ts?"
- "Search my threads to find the one in which we added the explosion animation. I want to continue working on that."
- "Show me all threads that modified src/terminal/pty.rs"
- "Find and read the thread that created scripts/deploy.sh."
- "Find the thread in which we added @server/src/backfill-service.ts, read it, and extract the SQL snippet we used to test the migration."

The `find_thread` tool is the sibling to `read_thread`. First you find, then you read. Together they turn your Amp threads into reusable context.

![Find thread in action](https://static.ampcode.com/news/find-thread.png)