---
title: Agents Panel
url: https://ampcode.com/news/agents-panel
source: crawler
fetched_at: 2026-02-06T02:08:13.349279085-03:00
rendered_js: false
word_count: 165
summary: This document introduces the Agents Panel in the Amp editor extension and explains how to navigate, manage, and archive agent threads using keyboard shortcuts.
tags:
    - amp-editor
    - agent-threads
    - keyboard-shortcuts
    - thread-management
    - vscode-extension
category: guide
---

![Agents Panel](https://static.ampcode.com/news/vscode-threads-view/threads-main.png)

The Amp editor extension now has a new panel to view and manage all active agent threads.

You can use the keyboard to navigate between threads:

- `j`/`k` or arrow keys to move between threads
- `Space` to expand a thread panel to show the last message or tool result
- `Enter` to open a thread
- `e` to archive or unarchive a thread
- `Esc` to toggle focus between the thread list and the input, which starts new threads

We recommend archiving old threads so the displayed threads represent your working set. You can use `Archive Old Threads` from the Amp command palette (`Cmd-K` from the Amp panel) to archive threads older than 72 hours.

As coding agents improve and require less direct human oversight, more time will be spent by humans in managing and orchestrating work across multiple agent threads. We'll have more to share soon.

To get started, click the button on the left end of the navbar or use `Cmd-Opt-I` (macOS) or `Ctrl-Alt-I` (Windows/Linux).