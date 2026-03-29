---
title: Setup Panic Hooks
url: https://ratatui.rs/recipes/apps/panic-hooks/
source: crawler
fetched_at: 2026-02-01T21:13:14.184299912-03:00
rendered_js: false
word_count: 386
summary: This document explains how to implement panic hooks in Ratatui applications to ensure the terminal returns to its original state when an unexpected crash occurs.
tags:
    - ratatui
    - rust
    - panic-handling
    - terminal-ui
    - crossterm
    - termion
    - error-handling
category: guide
---

When building TUIs with `ratatui`, it’s vital to ensure that if your application encounters a panic, it gracefully returns to the original terminal state. This prevents the terminal from getting stuck in a modified state, which can be quite disruptive for users.

The rust standard library allows applications to setup a panic hook that runs whenever a panic occurs. Ratatui applications should use this to disable raw mode and return the main screen.

Given the following application that panics after a 1 second delay as a basis, we can implement the hooks for each backend.

```

pubfnmain() -> io::Result<()> {
init_panic_hook();
letmuttui=init_tui()?;
tui.draw(|frame|frame.render_widget(Span::from("Hello, world!"), frame.area()))?;
sleep(Duration::from_secs(1));
panic!("This is a panic!");
}
```

Restoring the terminal state in an app that uses the `CrosstermBackend` is pretty simple. The `init_panic_hook` method saves a copy of the current hook, and then sets up a new hook that restores the terminal to the original state before calling the original hook. It’s important to avoid panicking while restoring the terminal state, otherwise the original panic reason might be lost. In your own app, this might be supplemented with logging to a file or similar.

```

26 collapsed lines
use std::{
io::{self, stdout},
panic::{set_hook, take_hook},
thread::sleep,
time::Duration,
};
use ratatui::{
backend::{Backend, CrosstermBackend},
crossterm::{
execute,
terminal::{disable_raw_mode, enable_raw_mode, EnterAlternateScreen, LeaveAlternateScreen},
},
text::Span,
Terminal,
};
pubfnmain() -> io::Result<()> {
init_panic_hook();
letmuttui=init_tui()?;
tui.draw(|frame|frame.render_widget(Span::from("Hello, world!"), frame.area()))?;
sleep(Duration::from_secs(1));
panic!("This is a panic!");
}
pubfninit_panic_hook() {
letoriginal_hook=take_hook();
set_hook(Box::new(move|panic_info| {
// intentionally ignore errors here since we're already in a panic
let_=restore_tui();
original_hook(panic_info);
}));
}
pubfninit_tui() -> io::Result<Terminal<impl Backend>> {
enable_raw_mode()?;
execute!(stdout(), EnterAlternateScreen)?;
Terminal::new(CrosstermBackend::new(stdout()))
}
pubfnrestore_tui() -> io::Result<()> {
disable_raw_mode()?;
execute!(stdout(), LeaveAlternateScreen)?;
Ok(())
}
```

Termion requires a bit more effort, as the code for enabling and disabling raw mode is only available on the `RawTerminal` type. The type stores a copy of the terminal state when constructed and then restores that when dropped. It has a `suspend_raw_mode` function that temporarily restores the terminal state.

To make it possible for the `init_tui` method to see the terminal in a cooked state (the opposite of raw), the `init_panic_hook` method needs to create a `RawTerminal` which will be used in the panic hook, and immediately suspend raw mode.

Termion provides a similar wrapper type for the alternate screen, but this type doesn’t implement a method to leave the alternate screen except when dropped. Apps should use `ToAlternateScreen` / `ToMainScreen` instead of the `IntoAlternateScreen` wrapper. Also make sure to call `stdout().flush`, to make this change take effect.

```

23 collapsed lines
use std::{
io::{self, stdout, Write},
panic::{set_hook, take_hook},
thread::sleep,
time::Duration,
};
use ratatui::{
backend::{Backend, TermionBackend},
termion::{
raw::IntoRawMode,
screen::{ToAlternateScreen, ToMainScreen},
},
text::Span,
Terminal,
};
pubfnmain() -> io::Result<()> {
init_panic_hook()?;
letmuttui=init_tui()?;
tui.draw(|frame|frame.render_widget(Span::from("Hello, world!"), frame.area()))?;
sleep(Duration::from_secs(1));
panic!("This is a panic!");
}
pubfninit_panic_hook() -> io::Result<()> {
letraw_output=stdout().into_raw_mode()?;
raw_output.suspend_raw_mode()?;
letoriginal_hook=take_hook();
set_hook(Box::new(move|panic_info| {
// intentionally ignore errors here since we're already in a panic
let_=raw_output.suspend_raw_mode();
let_=restore_tui();
original_hook(panic_info);
}));
Ok(())
}
pubfninit_tui() -> io::Result<Terminal<impl Backend>> {
letmutstdout=stdout().into_raw_mode()?;
write!(stdout, "{}", ToAlternateScreen)?;
stdout.flush()?;
Terminal::new(TermionBackend::new(stdout))
}
pubfnrestore_tui() -> io::Result<()> {
write!(stdout(), "{}", ToMainScreen)?;
stdout().flush()?;
Ok(())
}
```

For more discussion on this, see:

- [https://github.com/ratatui/ratatui/issues/1005](https://github.com/ratatui/ratatui/issues/1005)
- [https://gitlab.redox-os.org/redox-os/termion/-/issues/176](https://gitlab.redox-os.org/redox-os/termion/-/issues/176)

Termwiz is a little more difficult as the methods to disable raw mode and exit the alternate screen require mutable access to the terminal instance.

As a general rule, you want to take the original panic hook and execute it after cleaning up the terminal. In the next sections we will discuss some third party packages that can help give better output for handling errors and panics.