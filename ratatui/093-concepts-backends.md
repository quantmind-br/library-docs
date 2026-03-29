---
title: Backends
url: https://ratatui.rs/concepts/backends/
source: crawler
fetched_at: 2026-02-01T21:12:30.600747792-03:00
rendered_js: false
word_count: 272
summary: This document explains how Ratatui utilizes backends to interface with terminal emulators and details the supported libraries, features, and version compatibility requirements.
tags:
    - ratatui
    - terminal-backends
    - crossterm
    - termion
    - termwiz
    - raw-mode
    - alternate-screen
category: concept
---

Ratatui interfaces with the terminal emulator through a backend. These libraries enable Ratatui via the [`Terminal`](https://docs.rs/ratatui/latest/ratatui/struct.Terminal.html) type to draw styled text to the screen, manipulate the cursor, and interrogate properties of the terminal such as the console or window size. Your application will generally also use the backend directly to capture keyboard, mouse and window events, and enable raw mode and the alternate screen.

Ratatui supports the following backends:

- [Crossterm](https://crates.io/crates/crossterm) via [`CrosstermBackend`](https://docs.rs/ratatui/latest/ratatui/backend/struct.CrosstermBackend.html) and the `crossterm` feature (enabled by default). Also see [Crossterm version compatibility](#crossterm-version-compatibility) below for details on selecting specific versions.
- [Termion](https://crates.io/crates/termion) via [`TermionBackend`](https://docs.rs/ratatui/latest/ratatui/backend/struct.TermionBackend.html) and the `termion` feature.
- [Termwiz](https://crates.io/crates/termwiz) via [`TermwizBackend`](https://docs.rs/ratatui/latest/ratatui/backend/struct.TermwizBackend.html) and the `termwiz` feature.
- A [`TestBackend`](https://docs.rs/ratatui/latest/ratatui/backend/struct.TestBackend.html) which can be useful to unit test your application’s UI

For information on how to choose a backend see: [Comparison](https://ratatui.rs/concepts/backends/comparison/)

Each backend supports [Raw Mode](https://ratatui.rs/concepts/backends/raw-mode/) (which changes how the terminal handles input and output processing), an [Alternate Screen](https://ratatui.rs/concepts/backends/alternate-screen/) which allows it to render to a separate buffer than your shell commands use, and [Mouse Capture](https://ratatui.rs/concepts/backends/mouse-capture/), which allows your application to capture mouse events.

### Crossterm version compatibility

[Section titled “Crossterm version compatibility”](#crossterm-version-compatibility)

Avoid pulling in multiple semver-incompatible [Crossterm](https://crates.io/crates/crossterm) versions. Different major versions:

- keep separate event queues (which can lead to race conditions and lost events),
- track raw mode separately (so raw mode may not be restored correctly on exit),
- cannot exchange types even when names match (leading to compilation errors).

Also, specific versions may make it difficult to upgrade Ratatui/widgets unless everything is up to date.

As a mitigation, Ratatui 0.30+ supports multiple [Crossterm](https://crates.io/crates/crossterm) major versions via `crossterm_{version}` feature flags. You can select which version to use and avoid conflicts in your dependency graph.

For example:

```

ratatui = { version = "0.30", features = ["crossterm_0_28"] }
crossterm = "0.28"
# or
ratatui = { version = "0.30", features = ["crossterm_0_29"] }
crossterm = "0.29"
```