---
title: Queue Messages in the CLI
url: https://ampcode.com/news/queue-messages-in-the-cli
source: crawler
fetched_at: 2026-02-06T02:08:39.342505641-03:00
rendered_js: false
word_count: 37
summary: This document explains how to use CLI commands to queue and dequeue messages for an agent to process sequentially.
tags:
    - cli-commands
    - message-queueing
    - agent-interaction
    - command-line-interface
category: guide
---

You can now also [queue messages](https://ampcode.com/manual#queueing-messages) in the CLI. Once queued, messages will be sent to the agent once it's done with its current turn.

Use `/queue <message>` to enqueue a message and `/dequeue` to dequeue them.