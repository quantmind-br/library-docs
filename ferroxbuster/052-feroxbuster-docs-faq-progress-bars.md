---
title: Progress bars print one line at a time
url: https://epi052.github.io/feroxbuster-docs/faq/progress-bars
source: github_pages
fetched_at: 2026-02-06T10:56:26.88449019-03:00
rendered_js: true
word_count: 81
summary: This document explains how to resolve display issues with feroxbuster progress bars when using a terminal that is too narrow.
tags:
    - feroxbuster
    - terminal-width
    - progress-bar
    - troubleshooting
    - cli-output
category: guide
---

## Progress bars print one line at a time

[Section titled “Progress bars print one line at a time”](#progress-bars-print-one-line-at-a-time)

`feroxbuster` needs a terminal width of at least the size of what’s being printed in order to do progress bar printing correctly. If your width is too small, you may see output like what’s shown below.

![small-term](https://epi052.github.io/feroxbuster-docs/images/small-term.png)

If you can, simply make the terminal wider and rerun. If you’re unable to make your terminal wider consider using `-q` to suppress the progress bars.