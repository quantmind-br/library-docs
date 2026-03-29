---
title: Provider Actions | Walker
url: https://benz.gitbook.io/walker/customization/provider-actions
source: sitemap
fetched_at: 2026-02-01T13:48:47.353422496-03:00
rendered_js: false
word_count: 150
summary: This document explains how to configure multiple actions and keybindings for list items in Walker, including default behaviors, fallback configurations, and after-action triggers.
tags:
    - actions
    - keybinds
    - configuration
    - walker
    - providers
    - fallbacks
    - default-behavior
category: reference
---

Walker gives you the freedom to provide multiple actions/keybinds for a list item. These are configured in the `[providers.actions]` section of the config. This section will be merged with the default configuration.

```
[providers.actions]
runner = [
  { action = "run", default = true, bind = "Return" },
  { action = "runterminal", label = "run in terminal", bind = "shift Return" },
]
```

There is a bit of magic behavior going on:

- item has only 1 action and no bind set ⇒ automatic fallback
- default `bind` key ⇒ `Return`
- default `after` key ⇒ `Close`
- default `label` key ⇒ `action` key

### Possible `after` keys and their behavior

Activate item + select next

Reload with current query

Reload gets triggered by backend

Reload gets triggered by backend

switches to a given provider

Often times, you have multiple providers with the same actions, example: `menus:open` is a common action for custom menus. Instead of having to define this action for every provider, Walker allows you to set fallbacks, f.e.:

```
[providers.actions]
fallback = [
  { action = "menus:open", label = "open", after = "Nothing" },
  { action = "erase_history", label = "clear hist", bind = "ctrl h", after = "AsyncReload" },
]
```

You can define your own fallbacks in a similar fashion.

Last updated 3 months ago