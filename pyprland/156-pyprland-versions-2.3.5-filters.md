---
title: Text filters | Pyprland web
url: https://hyprland-community.github.io/pyprland/versions/2.3.5/filters
source: github_pages
fetched_at: 2026-01-31T15:59:04.521961512-03:00
rendered_js: false
word_count: 23
summary: This document explains the usage and syntax of a text filtering feature that mimics sed's 's' command for pattern replacement.
tags:
    - text-processing
    - sed
    - pattern-replacement
    - filtering
    - regular-expressions
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