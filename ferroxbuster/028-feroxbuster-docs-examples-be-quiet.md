---
title: Silent/Quiet Output
url: https://epi052.github.io/feroxbuster-docs/examples/be-quiet
source: github_pages
fetched_at: 2026-02-06T10:54:58.000653723-03:00
rendered_js: true
word_count: 88
summary: This document explains how to use silence and quiet flags to suppress command-line output for piping and automated scanning workflows.
tags:
    - cli-flags
    - output-control
    - silent-mode
    - automation
    - logging
category: guide
---

## Silence all Output or Be Kinda Quiet

[Section titled “Silence all Output or Be Kinda Quiet”](#silence-all-output-or-be-kinda-quiet)

Version 2.0.0 introduces `--silent` which is almost equivalent to version 1.x.x’s `--quiet`.

Good for piping a list of urls to other commands:

- disables logging (no error messages to screen)
- don’t print banner
- only display urls during scan

```

https://localhost.com/contact
https://localhost.com/about
https://localhost.com/terms
```

Good for tmux windows that have notifications enabled as the only updates shown by the scan are new valid responses and new directories found that are suitable for recursion.

- hide progress bars
- don’t print banner

```

302        0l        0w        0c https://localhost.com/Login
200      126l      281w     4091c https://localhost.com/maintenance
200      126l      281w     4092c https://localhost.com/terms
... more individual entries, followed by the directories being scanned ...
Scanning: https://localhost.com
Scanning: https://localhost.com/homepage
Scanning: https://localhost.com/api
```