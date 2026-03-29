---
title: Comparison of Backends
url: https://ratatui.rs/concepts/backends/comparison/
source: crawler
fetched_at: 2026-02-01T21:13:04.517024582-03:00
rendered_js: false
word_count: 142
summary: This document explains the various terminal backends supported by the Ratatui library and provides a framework for selecting the most suitable one for a project.
tags:
    - ratatui
    - terminal-backend
    - rust-programming
    - crossterm
    - termion
    - termwiz
category: guide
---

Ratatui interfaces with the terminal emulator through its “backends”. These are powerful libraries that grant `ratatui` the ability to capture keypresses, maneuver the cursor, style the text with colors and other features. As of now, `ratatui` supports three backends:

- [Crossterm](https://crates.io/crates/crossterm)
- [Termion](https://crates.io/crates/termion)
- [Termwiz](https://crates.io/crates/termwiz)

Selecting a backend does influence your project’s structure, but the core functionalities remain consistent across all options. Here’s a flowchart that can help you make your decision.

Yes

No

Yes

No

Yes

No

Yes

No

Is the TUI only for Wezterm users?

Is Windows compatibility important?

Are you familiar with Crossterm?

Are you familiar with Termion?

Crossterm

Termwiz

Termion

Though we try to make sure that all backends are fully-supported, the most commonly-used backend is Crossterm. If you have no particular reason to use Termion or Termwiz, you will find it easiest to learn Crossterm simply due to its popularity.