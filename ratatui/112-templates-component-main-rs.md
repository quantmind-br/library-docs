---
title: Main.rs
url: https://ratatui.rs/templates/component/main-rs/
source: crawler
fetched_at: 2026-02-01T21:13:27.012500204-03:00
rendered_js: false
word_count: 114
summary: This document explains the structure and role of the main entry point and core modules in a Rust-based Terminal User Interface (TUI) application.
tags:
    - rust
    - tui
    - ratatui
    - cli-parsing
    - logging
    - error-handling
category: guide
---

In this section, let’s just cover the contents of `main.rs`, `build.rs` and `utils.rs`.

The `main.rs` file is the entry point of the application. Here’s the complete `main.rs` file:

```

use clap::Parser;
use cli::Cli;
use color_eyre::Result;
usecrate::app::App;
mod action;
mod app;
mod cli;
mod components;
mod config;
mod errors;
mod logging;
mod tui;
#[tokio::main]
asyncfnmain() -> Result<()> {
crate::errors::init()?;
crate::logging::init()?;
letargs= Cli::parse();
letmutapp= App::new(args.tick_rate, args.frame_rate)?;
app.run().await?;
Ok(())
}
```

In essence, the `main` function creates an instance of `App` and calls `App.run()`, which runs the “`handle event` -&gt; `update state` -&gt; `draw`” loop. We will talk more about this in a later section.

This `main.rs` file incorporates some key features that are not necessarily related to `ratatui`, but in my opinion, essential for any Terminal User Interface (TUI) program:

- Command Line Argument Parsing (`clap`)
- XDG Base Directory Specification
- Logging
- Panic Handler

These are described in more detail in the \[`config.rs`], \[`cli.rs`], \[`errors.rs`] and \[`logging.rs`] files.