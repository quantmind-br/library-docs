---
title: Dmenu | Walker
url: https://benz.gitbook.io/walker/dmenu
source: sitemap
fetched_at: 2026-02-01T13:48:40.438505009-03:00
rendered_js: false
word_count: 83
summary: This document explains how to use Walker as a dmenu replacement with various command-line flags for customization and behavior control.
tags:
    - dmenu
    - command-line
    - terminal
    - cli-tool
    - interface
category: guide
---

Walker can be used as a basic dmenu. The following flags can be used:

flag

description

`-d, --dmenu`

use Walker as dmenu

`-I, --inputonly`

hides the list

`-i, --index`

prints the index instead of the selected text

`-p, --placeholder`

set the input placeholder

`-c, --current`

marks the current value (with a css class `current`)

`-k, --keepopen`

keeps Walker open after selection

`-e, --exit`

exit after this dmenu call. only when using service

## [hashtag](#example) Example

```
echo`first\nsecond\nthird`|walker-d
```

[PreviousProviderschevron-left](https://benz.gitbook.io/walker/providers)[NextFAQchevron-right](https://benz.gitbook.io/walker/faq)

Last updated 3 months ago