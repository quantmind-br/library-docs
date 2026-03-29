---
title: Towards a New CLI
url: https://ampcode.com/news/towards-a-new-cli
source: crawler
fetched_at: 2026-02-06T02:08:44.38782837-03:00
rendered_js: false
word_count: 112
summary: This document announces the updated version of the Amp CLI, designed to integrate and support AI agents directly within the terminal environment. It highlights the growing trend of terminal-based agents and provides basic commands for installation and authentication.
tags:
    - amp-cli
    - terminal-agents
    - command-line-interface
    - ai-workflows
    - sourcegraph
    - developer-tools
category: other
---

Everything is changing and everything has changed, even in something that's decades old: the terminal.

Mere months ago, running agents in your terminal was considered a curiosity.

Now it's something we all do. Some of us casually; others many, many, *many* times a day — in multiple windows, multiple split panes, multiple checkouts of repositories.

Today we released a new version of our [Amp CLI](https://ampcode.com/manual#getting-started-command-line-interface).

It's our first step into a future of which we don't know much, but this: agents in the terminal are part of it — and we are building a CLI to unleash them.

You can use it right now:

```
$ npm install -g @sourcegraph/amp

$ amp login

$ amp
```

![Four instances of the Amp CLI in action](https://static.ampcode.com/news/towards-new-cli-quad.png)