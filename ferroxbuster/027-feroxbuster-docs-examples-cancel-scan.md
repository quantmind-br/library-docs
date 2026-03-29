---
title: Scan Management Menu
url: https://epi052.github.io/feroxbuster-docs/examples/cancel-scan
source: github_pages
fetched_at: 2026-02-06T10:54:59.662596057-03:00
rendered_js: true
word_count: 471
summary: This document explains how to use the interactive Scan Management Menu in feroxbuster to cancel scans, add new URLs, apply response filters, and adjust scan limits during runtime.
tags:
    - feroxbuster
    - scan-management
    - interactive-menu
    - directory-scanning
    - response-filtering
    - cli-tool
category: guide
---

Version 1.12.0 expanded the pause/resume functionality introduced in [v1.4.0](https://epi052.github.io/feroxbuster-docs/examples/pause-scan/) by adding an interactive menu from which currently running recursive scans can be cancelled, without affecting the overall scan. Scans can still be paused indefinitely by pressing `ENTER`.

Version 2.4.1 expanded functionality even further with the ability to add a brand-new scan. Now that cancelling is no longer the only action available to users, the name has been updated to the **Scan Management Menu**™.

Version 2.6.2 brought yet another capability: users can now add new filters to their current scan. Adding a new filter works the same as though you had specified `--filter-*` on the command-line.

Version 2.12.0 continued to improve on the **Scan Management Menu**™ menu by adding the ability to adjust the maximum number of concurrent directory scans that can progress at any given time. Additionally, a status line showing the current limit and how much of that limit is actively in use (i.e. number of active directory scans). Setting a new scan limit works the same as though you had specified `-L|--scan-limit` on the command line.

Below is an example of the Scan Cancel Management Menu™.

![cancel-menu](https://epi052.github.io/feroxbuster-docs/images/examples/cancel-menu.png)

Using the menu is pretty simple: from a running scan, press `ENTER` to view the menu

- Choose a scan to cancel by entering `cancel` or `c` followed by its scan index (`1`)
  
  - more than one scan can be selected by using a comma-separated list of indexes and/or ranges (`1-4,8,9-13` … etc)
- Confirm selections, after which all non-cancelled scans will resume
  
  - To skip confirmation, simply add a `-f` somewhere in your input (`3-5 -f`)

### Add a New Url for Scanning

[Section titled “Add a New Url for Scanning”](#add-a-new-url-for-scanning)

- Enter `add` or `a` followed by the new url you’d liked you add to the current scan queue

### Add a New Response Filter

[Section titled “Add a New Response Filter”](#add-a-new-response-filter)

- Enter `new-filter` or `n`, then the type of filter you’d like to add, and the value to pass to the filter itself.

Valid filter types:

- `status`
- `lines`
- `size`
- `words`
- `regex`
- `similarity`

Examples:

- `n status 301` - equivalent to command-line option `--filter-status 301`
- `new-filter lines 1` - equivalent to command-line option `--filter-lines 1`
- `new-filter words 7` - equivalent to command-line option `--filter-words 7`
- `n regex token:[0-9a-zA-Z]+` - equivalent to command-line option `--filter-regex 'token:[0-9a-zA-Z]+'`
- `n similarity https://target.url/page/with/csrf-token` - equivalent to command-line option `--filter-similar-to https://target.url/page/with/csrf-token`
- `new-filter size 1337` - equivalent to command-line option `--filter-size 1337`

### Set a Scan Limit (-L)

[Section titled “Set a Scan Limit (-L)”](#set-a-scan-limit--l)

- Enter `set-limit` or `s` followed by the new limit of concurrent directories you’d like to scan.

Here is a short demonstration of the menu’s `cancel` and `add` capabilities. They’re shown on an older version of the menu, but the functionality has not changed for these two commands.

![cancel-scan](https://epi052.github.io/feroxbuster-docs/images/examples/cancel-scan.gif)

Another short demo, this time showcasing the menu’s `new-filter` and `rm-filter` commands.

![cancel-scan2](https://epi052.github.io/feroxbuster-docs/images/examples/cancel-scan2.gif)