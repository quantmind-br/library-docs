---
title: Migrate from tui-rs
url: https://ratatui.rs/recipes/apps/migrate-from-tui-rs/
source: crawler
fetched_at: 2026-02-01T21:13:16.59876126-03:00
rendered_js: false
word_count: 191
summary: This document outlines multiple strategies for migrating projects from the tui-rs library to Ratatui, including full replacement and aliasing methods.
tags:
    - rust
    - ratatui
    - tui-rs
    - migration-guide
    - terminal-ui
    - dependency-management
category: guide
---

[Ratatui](https://github.com/tui-rs-revival/ratatui) is a fork of [tui-rs](https://github.com/fdehau/tui-rs/), created to continue maintenance of the project.

Several options are available to migrate apps and libs:

- Fully replace `tui-rs` with `ratatui` (preferred approach)
- Use `ratatui` as a drop in replacement aliased as `tui`
- Support both `tui` and `ratatui`

## Fully replace Tui with Ratatui

[Section titled “Fully replace Tui with Ratatui”](#fully-replace-tui-with-ratatui)

Most new code should use the following. To take this approach to migration requires find and replace `tui::`-&gt;`ratatui::` on the entire codebase.

```

ratatui = { version = "0.28.0" }
crossterm = { version = "0.28.0" }
```

## Drop in replacement

[Section titled “Drop in replacement”](#drop-in-replacement)

The simplest approach to migrating to `ratatui` is to use it as drop in replacement for tui and update the terminal libraries used (`crossterm` / `termion`). E.g.:

```

tui = { package = "ratatui", version = "0.28.0", features = ["crossterm"] }
crossterm = { version = "0.28.0" }
```

## Support both tui and ratatui

[Section titled “Support both tui and ratatui”](#support-both-tui-and-ratatui)

For more complex scenarios where a library (or in some cases an app) needs to support both ratatui and maintain existing support for tui, it may be feasible to use feature flags to select which library to use. See [tui-logger](https://github.com/gin66/tui-logger) for an example of this approach.

## Backwards compatibility and breaking changes

[Section titled “Backwards compatibility and breaking changes”](#backwards-compatibility-and-breaking-changes)

- [BREAKING-CHANGES.md](https://github.com/ratatui/ratatui/blob/main/BREAKING-CHANGES.md)
- PRs tagged with the [breaking changes](https://github.com/ratatui/ratatui/pulls?q=is%3Apr%20label%3A%22breaking%20change%22%20is%3Aclosed) label