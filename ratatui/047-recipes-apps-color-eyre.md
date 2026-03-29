---
title: Use `color_eyre` with Ratatui
url: https://ratatui.rs/recipes/apps/color-eyre/
source: crawler
fetched_at: 2026-02-01T21:13:15.274087207-03:00
rendered_js: false
word_count: 365
summary: This document explains how to integrate the color-eyre crate into a Ratatui application to provide formatted error reports while ensuring the terminal state is correctly restored during panics or errors.
tags:
    - rust
    - ratatui
    - color-eyre
    - error-handling
    - terminal-management
    - panic-hooks
category: guide
---

The [`color_eyre`](https://crates.io/crates/color-eyre) crate provides error report handlers for panics and errors. It displays the reports formatted and in color. To use these handlers, a Ratatui app needs to restore the terminal before displaying the errors.

First add the crate to your `Cargo.toml`

Call the [`color_eyre::install`](https://docs.rs/color-eyre/latest/color_eyre/fn.install.html) method from your main function and update the return value to [`color_eyre::Result<()>`](https://docs.rs/eyre/latest/eyre/type.Result.html).

```

fnmain() -> color_eyre::Result<()> {
color_eyre::install()?;
9 collapsed lines
letterminal= tui::init()?;
letresult=run(terminal).wrap_err("run failed");
iflet Err(err) = tui::restore() {
eprintln!(
"failed to restore terminal. Run `reset` or restart your terminal to recover: {err}"
);
}
result
}
```

In your terminal initialization function, add some new code that replaces rusts default panic handler with one that restores the terminal before displaying the panic details. This will be used by both panics and unhandled errors that fall through to the end of the program.

```

/// Initialize the terminal
pubfninit() -> io::Result<ratatui::Terminal<CrosstermBackend<Stdout>>> {
execute!(stdout(), EnterAlternateScreen)?;
enable_raw_mode()?;
set_panic_hook();
Terminal::new(CrosstermBackend::new(stdout()))
}
fnset_panic_hook() {
lethook= std::panic::take_hook();
std::panic::set_hook(Box::new(move|panic_info| {
let_=restore(); // ignore any errors as we are already failing
hook(panic_info);
}));
}
```

In your application, wrap errors with extra context as needed:

Add the following import:

```

use color_eyre::eyre::WrapErr;
```

Call wrap\_err from methods that can fail with an error.

```

fnmain() -> color_eyre::Result<()> {
color_eyre::install()?;
letterminal= tui::init()?;
letresult=run(terminal).wrap_err("run failed");
iflet Err(err) = tui::restore() {
eprintln!(
"failed to restore terminal. Run `reset` or restart your terminal to recover: {err}"
);
}
result
}
```

Full code

```

use std::panic;
use color_eyre::eyre::WrapErr;
use color_eyre::eyre::bail;
use ratatui::{
backend::Backend,
crossterm::event::{self, Event, KeyCode, KeyEvent},
widgets::Paragraph,
Terminal,
};
mod tui;
fnmain() -> color_eyre::Result<()> {
color_eyre::install()?;
letterminal= tui::init()?;
letresult=run(terminal).wrap_err("run failed");
iflet Err(err) = tui::restore() {
eprintln!(
"failed to restore terminal. Run `reset` or restart your terminal to recover: {err}"
);
}
result
}
fnrun(mutterminal: Terminal<impl Backend>) -> color_eyre::Result<()> {
loop {
terminal.draw(|frame| {
letmessage="Press <Q> to quit, <P> to panic, or <E> to error";
frame.render_widget(Paragraph::new(message), frame.area());
})?;
match event::read()? {
Event::Key(KeyEvent {
code: KeyCode::Char('q'),
..
}) =>break,
Event::Key(KeyEvent {
code: KeyCode::Char('p'),
..
}) =>panic!("User triggered panic"),
Event::Key(KeyEvent {
code: KeyCode::Char('e'),
..
}) =>bail!("user triggered error"),
_=> {}
}
}
Ok(())
}
```

```

use std::io::{self, stdout, Stdout};
use ratatui::{
backend::CrosstermBackend,
crossterm::{
execute,
terminal::{disable_raw_mode, enable_raw_mode, EnterAlternateScreen, LeaveAlternateScreen},
},
Terminal,
};
/// Initialize the terminal
pubfninit() -> io::Result<ratatui::Terminal<CrosstermBackend<Stdout>>> {
execute!(stdout(), EnterAlternateScreen)?;
enable_raw_mode()?;
set_panic_hook();
Terminal::new(CrosstermBackend::new(stdout()))
}
fnset_panic_hook() {
lethook= std::panic::take_hook();
std::panic::set_hook(Box::new(move|panic_info| {
let_=restore(); // ignore any errors as we are already failing
hook(panic_info);
}));
}
/// Restore the terminal to its original state
pubfnrestore() -> io::Result<()> {
execute!(stdout(), LeaveAlternateScreen)?;
disable_raw_mode()?;
Ok(())
}
```

![Panic](https://ratatui.rs/_astro/panic.CkBmxTd9_HdDl1.webp)

With `RUST_BACKTRACE=full`:

![Panic Full](https://ratatui.rs/_astro/panic-full.Bib68E5F_LlF7A.webp)

![Error](https://ratatui.rs/_astro/error.DQ6-o1HU_1Mf6fe.webp)

With `RUST_BACKTRACE=full`:

![Error Full](https://ratatui.rs/_astro/error-full.Jmp9wWxd_Z2uNwzs.webp)

![Quit](https://ratatui.rs/_astro/quit.DVKsjeV4_ZOEuSK.webp)

See the `color_eyre` [docs](https://docs.rs/color_eyre/latest/color_eyre) and [examples](https://github.com/eyre-rs/eyre/blob/master/color-eyre/examples/) for more advanced setups. E.g.:

- [Capturing span traces](https://github.com/eyre-rs/eyre/blob/master/color-eyre/examples/usage.rs)
- [Configuring an automatic issue url](https://github.com/eyre-rs/eyre/blob/master/color-eyre/examples/github_issue.rs)