---
title: Text filters | Pyprland web
url: https://hyprland-community.github.io/pyprland/versions/2.4.6/filters
source: github_pages
fetched_at: 2026-01-31T15:59:53.518628102-03:00
rendered_js: false
word_count: 23
summary: This document explains how to use the sed-style string replacement filter functionality with basic regex patterns and flags.
tags:
    - filter
    - regex
    - string-replacement
    - sed-command
    - text-processing
category: reference
---

At the moment there is only one filter, close match of [sed's "s" command](https://www.gnu.org/software/sed/manual/html_node/The-_0022s_0022-Command.html).

The only supported flag is "g"

## Example [​](#example)

toml

```
filter = 's/foo/bar/'
filter = 's/.*started (.*)/\1 has started/'
filter = 's#</?div>##g'
```