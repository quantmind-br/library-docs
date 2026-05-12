---
title: Warp Drive Context | Reference | Warp
url: https://docs.warp.dev/reference/cli/warp-drive
source: sitemap
fetched_at: 2026-04-29T15:05:02.402373427-03:00
rendered_js: false
word_count: 96
summary: This document explains how to reuse saved prompts and incorporate Warp Drive objects as context when executing agent commands via the CLI.
tags:
    - warp-drive
    - cli-commands
    - prompt-management
    - workflow-automation
    - context-injection
category: guide
optimized: true
optimized_at: 2026-04-29T00:00:00Z
---
## Reusing saved prompts

Save prompts in [Warp Drive](https://docs.warp.dev/knowledge-and-collaboration/warp-drive) to reuse across sessions, share with teammates, and integrate into automated workflows. See [Prompts](https://docs.warp.dev/knowledge-and-collaboration/warp-drive/prompts).

Find the prompt ID — it's the last segment of its Warp Drive sharing link:

```
https://warp.dev/drive/prompt/Fix-compiler-error-sgNpbUgDkmp2IImUVDc8kR
# ID: sgNpbUgDkmp2IImUVDc8kR
```

Pass the ID using the `--saved-prompt` flag:

```
$ oz agent run --saved-prompt sgNpbUgDkmp2IImUVDc8kR
```

## Referencing Warp Drive objects as context

Use `<workflow:id>`, `<notebook:id>`, or `<rule:id>` in prompts to attach [Warp Drive objects](https://docs.warp.dev/knowledge-and-collaboration/warp-drive) and [rules](https://docs.warp.dev/knowledge-and-collaboration/rules) as context for the agent.

> [!tip]
> Use the [@ context menu](https://docs.warp.dev/agent-platform/warp-agents/agent-context/using-to-add-context) in Warp to construct a prompt with the right references, then copy it into your CLI command.

```
$ oz agent run --prompt "Follow the instructions in <notebook:gq1CMAUWLtaL1CpEoTDQ3y>"
```
