---
title: Migrating to 1.0
url: https://opencode.ai/docs/1-0
source: sitemap
fetched_at: 2026-01-24T22:48:27.405608199-03:00
rendered_js: false
word_count: 192
summary: This document announces the release of OpenCode 1.0, detailing a complete TUI rewrite using Zig and SolidJS, along with significant UX updates and breaking keybinding changes.
tags:
    - opencode
    - release-notes
    - tui
    - breaking-changes
    - software-update
    - keybindings
category: reference
---

OpenCode 1.0 is a complete rewrite of the TUI.

We moved from the go+bubbletea based TUI which had performance and capability issues to an in-house framework (OpenTUI) written in zig+solidjs.

The new TUI works like the old one since it connects to the same opencode server.

* * *

## [Upgrading](#upgrading)

You should not be autoupgraded to 1.0 if you are currently using a previous version. However some older versions of OpenCode always grab latest.

To upgrade manually, run

To downgrade back to 0.x, run

```

$opencodeupgrade0.15.31
```

* * *

## [UX changes](#ux-changes)

The session history is more compressed, only showing full details of the edit and bash tool.

We added a command bar which almost everything flows through. Press ctrl+p to bring it up in any context and see everything you can do.

Added a session sidebar (can be toggled) with useful information.

We removed some functionality that we weren’t sure anyone actually used. If something important is missing please open an issue and we’ll add it back quickly.

* * *

## [Breaking changes](#breaking-changes)

### [Keybinds renamed](#keybinds-renamed)

- messages\_revert -&gt; messages\_undo
- switch\_agent -&gt; agent\_cycle
- switch\_agent\_reverse -&gt; agent\_cycle\_reverse
- switch\_mode -&gt; agent\_cycle
- switch\_mode\_reverse -&gt; agent\_cycle\_reverse

### [Keybinds removed](#keybinds-removed)

- messages\_layout\_toggle
- messages\_next
- messages\_previous
- file\_diff\_toggle
- file\_search
- file\_close
- file\_list
- app\_help
- project\_init
- tool\_details
- thinking\_blocks