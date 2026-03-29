---
title: Text filters | Pyprland web
url: https://hyprland-community.github.io/pyprland/versions/2.5.x/filters
source: github_pages
fetched_at: 2026-01-31T16:00:55.239555545-03:00
rendered_js: false
word_count: 23
summary: This document explains how to use the sed-style string filtering functionality with specific syntax and supported flags.
tags:
    - filtering
    - string-replacement
    - sed-syntax
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