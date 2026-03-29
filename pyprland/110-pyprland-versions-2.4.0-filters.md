---
title: Text filters | Pyprland web
url: https://hyprland-community.github.io/pyprland/versions/2.4.0/filters
source: github_pages
fetched_at: 2026-01-31T16:04:59.978917498-03:00
rendered_js: false
word_count: 23
summary: This document explains how to use the sed-style string filtering functionality available in the application, specifically detailing the close match of sed's 's' command with support for global replacement flags.
tags:
    - filtering
    - string-replacement
    - sed-command
    - text-processing
    - regex
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