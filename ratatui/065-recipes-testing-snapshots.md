---
title: Testing with insta snapshots
url: https://ratatui.rs/recipes/testing/snapshots/
source: crawler
fetched_at: 2026-02-01T21:13:20.82124915-03:00
rendered_js: false
word_count: 278
summary: This document provides a step-by-step guide on implementing snapshot testing for Ratatui applications using the insta crate and cargo-insta tool.
tags:
    - ratatui
    - rust
    - snapshot-testing
    - insta
    - tui
    - testing
    - cargo-insta
category: tutorial
---

Snapshot tests allow you to skip the tedious process of writing exact tests by capturing reference values once. and then using them in all future tests runs. It’s easy to use [insta](https://insta.rs/) and [cargo-insta](https://crates.io/crates/cargo-insta) to write snapshot tests for Ratatui apps and widgets.

### 1. Add Dependencies

[Section titled “1. Add Dependencies”](#1-add-dependencies)

First, make sure to install cargo-insta and include the [`insta`](https://crates.io/crates/insta) crate in your `Cargo.toml`:

```

cargoinstallcargo-insta
cargoaddinsta--dev
```

### 2. Structuring Your Application

[Section titled “2. Structuring Your Application”](#2-structuring-your-application)

Let’s assume you have a simple application that implements the `App` struct, which is responsible for your TUI’s core logic and rendering. To test this with insta snapshots, you’ll use a [`TestBackend`](https://docs.rs/ratatui/latest/ratatui/backend/struct.TestBackend.html) from Ratatui to capture the output in a test environment.

Here’s the structure of your app and test:

```

#[derive(Default)]
pubstruct App { /* Your app struct */ }
impl Widget for App { /* Implement the Widget trait */ }
// Now in tests module:
#[cfg(test)]
mod tests {
usesuper::App;
use insta::assert_snapshot;
use ratatui::{backend::TestBackend, Terminal};
#[test]
fntest_render_app() {
letapp= App::default();
letmutterminal= Terminal::new(TestBackend::new(80, 20)).unwrap();
terminal
.draw(|frame|frame.render_widget(&app, frame.area()))
.unwrap();
assert_snapshot!(terminal.backend());
}
}
```

### 3. Running the Test

[Section titled “3. Running the Test”](#3-running-the-test)

When you run the test (`cargo test`), the output of the `Terminal::draw()` method will be compared against a snapshot. If this is the first time running the test or the output has changed, [`insta`](https://crates.io/crates/insta) will create a snapshot file under the `snapshots/` directory.

For example, after running the test, a new snapshot file might be created at:

```

snapshots/demo2__tests__render_app.snap
```

This file will store the visual representation of your terminal as a string:

```

---
source: examples/demo2/main.rs
expression: terminal.backend()
---
"Ratatui                               Recipe  Email  Traceroute  Weather        "
"▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▄▄███▄▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀"
"▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▄███████▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀"
"▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▄█████████▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀"
"▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀████████████▄▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀"
"▀▀                              ▀▀▀▀▀▀▀▀▀▀▀▀▀███████████▀▀▀▀▄▄██████▀▀▀▀▀▀▀▀▀▀▀▀"
"▀▀  ──────── Ratatui ─────────  ▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀███▀▄█▀▀████████▀▀▀▀▀▀▀▀▀▀▀▀▀"
"▀▀  - cooking up terminal user  ▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▄▄▄▄▀▄████████████▀▀▀▀▀▀▀▀▀▀▀▀▀▀"
"▀▀  interfaces -                ▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀████████████████▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀"
"▀▀                              ▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀███▀██████████▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀"
"▀▀  Ratatui is a Rust crate     ▀▀▀▀▀▀▀▀▀▀▀▀▀▄▀▀▄▀▀▀█████████▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀"
"▀▀  that provides widgets       ▀▀▀▀▀▀▀▀▀▀▀▄▀ ▄  ▀▄▀█████████▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀"
"▀▀  (e.g. Paragraph, Table)     ▀▀▀▀▀▀▀▀▀▄▀  ▀▀    ▀▄▀███████▄▄▄▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀"
"▀▀  and draws them to the       ▀▀▀▀▀▀▀▄▀      ▄▄    ▀▄▀█████████▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀"
"▀▀                              ▀▀▀▀▀▄▀         ▀▀     ▀▄▀██▀▀▀███▀▀▀▀▀▀▀▀▀▀▀▀▀▀"
"▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀█                    ▀▄▀▀▀▄██▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀"
"▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▄                    ▀▄▀█▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀"
"▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀"
"▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀"
"     H/←  Left  L/→  Right  K/↑  Up  J/↓  Down  D/Del  Destroy  Q/Esc  Quit     "
```

In the snapshot, each line represents a row of the terminal, capturing the rendered state of your TUI. The next time you run your tests, the output will be compared to this file to detect any unintentional changes.

### 4. Handling Snapshot Changes

[Section titled “4. Handling Snapshot Changes”](#4-handling-snapshot-changes)

When changes to the UI are intentional, you can update the snapshot by running:

This command allows you to review the differences and accept the new snapshot if desired.