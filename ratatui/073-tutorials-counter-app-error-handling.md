---
title: Counter App Error Handling
url: https://ratatui.rs/tutorials/counter-app/error-handling/
source: crawler
fetched_at: 2026-02-01T21:12:34.967490928-03:00
rendered_js: false
word_count: 1303
summary: This tutorial explains how to implement robust error and panic handling in Ratatui applications to ensure the terminal state is correctly restored during a crash or unhandled error.
tags:
    - rust
    - ratatui
    - error-handling
    - panic-handling
    - terminal-ui
    - color-eyre
category: tutorial
---

In the previous section, you created a [basic counter app](https://ratatui.rs/tutorials/counter-app/basic-app/) that responds to the user pressing the **Left** and **Right** arrow keys to control the value of a counter. This tutorial will start with that code and add error and panic handling.

A quick reminder of where we left off in the basic app:

```

# -- snip --
[dependencies]
ratatui = "0.30.0"
crossterm = "0.29.0"
```

```

use std::io;
use crossterm::event::{self, Event, KeyCode, KeyEvent, KeyEventKind};
use ratatui::{
buffer::Buffer,
layout::Rect,
style::Stylize,
symbols::border,
text::{Line, Text},
widgets::{Block, Paragraph, Widget},
DefaultTerminal, Frame,
};
fnmain() -> io::Result<()> {
ratatui::run(|terminal| App::default().run(terminal))
}
#[derive(Debug, Default)]
pubstruct App {
counter: u8,
exit: bool,
}
impl App {
/// runs the application's main loop until the user quits
pubfnrun(&mutself, terminal:&mut DefaultTerminal) -> io::Result<()> {
while!self.exit {
terminal.draw(|frame|self.draw(frame))?;
self.handle_events()?;
}
Ok(())
}
fndraw(&self, frame:&mut Frame) {
frame.render_widget(self, frame.area());
}
/// updates the application's state based on user input
fnhandle_events(&mutself) -> io::Result<()> {
match event::read()? {
// it's important to check that the event is a key press event as
// crossterm also emits key release and repeat events on Windows.
Event::Key(key_event) ifkey_event.kind == KeyEventKind::Press => {
self.handle_key_event(key_event)
}
_=> {}
};
Ok(())
}
fnhandle_key_event(&mutself, key_event: KeyEvent) {
matchkey_event.code {
KeyCode::Char('q') =>self.exit(),
KeyCode::Left =>self.decrement_counter(),
KeyCode::Right =>self.increment_counter(),
_=> {}
}
}
fnexit(&mutself) {
self.exit =true;
}
fnincrement_counter(&mutself) {
self.counter +=1;
}
fndecrement_counter(&mutself) {
self.counter -=1;
}
}
impl Widget for&App {
fnrender(self, area: Rect, buf:&mut Buffer) {
lettitle= Line::from(" Counter App Tutorial ".bold());
letinstructions= Line::from(vec![
" Decrement ".into(),
"<Left>".blue().bold(),
" Increment ".into(),
"<Right>".blue().bold(),
" Quit ".into(),
"<Q> ".blue().bold(),
]);
letblock= Block::bordered()
.title(title.centered())
.title_bottom(instructions.centered())
.border_set(border::THICK);
letcounter_text= Text::from(vec![Line::from(vec![
"Value: ".into(),
self.counter.to_string().yellow(),
])]);
Paragraph::new(counter_text)
.centered()
.block(block)
.render(area, buf);
}
}
#[cfg(test)]
mod tests {
usesuper::*;
use ratatui::style::Style;
#[test]
fnrender() {
letapp= App::default();
letmutbuf= Buffer::empty(Rect::new(0, 0, 50, 4));
app.render(buf.area, &mutbuf);
letmutexpected= Buffer::with_lines(vec![
"┏━━━━━━━━━━━━━ Counter App Tutorial ━━━━━━━━━━━━━┓",
"┃                    Value: 0                    ┃",
"┃                                                ┃",
"┗━ Decrement <Left> Increment <Right> Quit <Q> ━━┛",
]);
lettitle_style= Style::new().bold();
letcounter_style= Style::new().yellow();
letkey_style= Style::new().blue().bold();
expected.set_style(Rect::new(14, 0, 22, 1), title_style);
expected.set_style(Rect::new(28, 1, 1, 1), counter_style);
expected.set_style(Rect::new(13, 3, 6, 1), key_style);
expected.set_style(Rect::new(30, 3, 7, 1), key_style);
expected.set_style(Rect::new(43, 3, 4, 1), key_style);
assert_eq!(buf, expected);
}
#[test]
fnhandle_key_event() {
letmutapp= App::default();
app.handle_key_event(KeyCode::Right.into());
assert_eq!(app.counter, 1);
app.handle_key_event(KeyCode::Left.into());
assert_eq!(app.counter, 0);
letmutapp= App::default();
app.handle_key_event(KeyCode::Char('q').into());
assert!(app.exit);
}
}
```

The app you built in the previous section has an intentional error in that causes the app to panic when the user presses the **Left** arrow key when the Counter is already at 0. When this happens, the main function does not have a chance to restore the terminal state before it exits.

```

fnmain() -> io::Result<()> {
ratatui::run(|terminal| App::default().run(terminal))
}
```

The application’s default panic handler runs and displays the details messed up. This is because raw mode stops the terminal from interpreting newlines in the usual way. The shell prompt is also rendered at the wrong place.

![Basic App Error](https://ratatui.rs/_astro/basic-app-error.ZBvysa33_ZYXsud.webp)

To recover from this, on a macOS or Linux console, run the `reset` command. On a Windows console you may need to restart the console.

There are two ways that a rust application can fail. The rust book chapter on [error handling](https://doc.rust-lang.org/book/ch09-00-error-handling.html) explains this in better detail.

> Rust groups errors into two major categories: *recoverable* and *unrecoverable* errors. For a recoverable error, such as a *file not found error*, we most likely just want to report the problem to the user and retry the operation. Unrecoverable errors are always symptoms of bugs, like trying to access a location beyond the end of an array, and so we want to immediately stop the program. — [https://doc.rust-lang.org/book/ch09-00-error-handling.html](https://doc.rust-lang.org/book/ch09-00-error-handling.html)

One approach that makes it easy to show unhandled errors is to use the [color-eyre](https://crates.io/crates/color-eyre) crate to augment the error reporting hooks. In a ratatui application that’s running on the [alternate screen](https://ratatui.rs/concepts/backends/alternate-screen/) in [raw mode](https://ratatui.rs/concepts/backends/raw-mode/), it’s important to restore the terminal before displaying these errors to the user.

* * *

Add the `color-eyre` crate

Update the `main` function’s return value to [`color_eyre::Result<()>`](https://docs.rs/eyre/latest/eyre/type.Result.html) and call the the [`color_eyre::install`](https://docs.rs/color-eyre/latest/color_eyre/fn.install.html) function. We can also add an error message that helps your app user understand what to do if restoring the terminal does fail.

```

use color_eyre::{
eyre::{bail, WrapErr},
Result,
};
fnmain() -> Result<()> {
color_eyre::install()?;
letmutterminal= tui::init()?;
letapp_result= App::default().run(&mutterminal);
iflet Err(err) = tui::restore() {
eprintln!(
"failed to restore terminal. Run `reset` or restart your terminal to recover: {err}"
);
}
app_result
}
```

Next, update the `tui::init()` function to replace the panic hook with one that first restores the terminal before printing the panic information. This will ensure that both panics and unhandled errors (i.e. any `Result::Err`s that bubble up to the top level of the main function) are both displayed on the terminal correctly when the application exits.

```

/// Initialize the terminal
pubfninit() -> io::Result<Tui> {
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

Color eyre works by adding extra information to Results. You can add context to the errors by calling `wrap_err` (defined on the `color_eyre::eyre::WrapErr` trait).

Update the `App::run` function to add some information about the update function failing and change the return value.

```

impl App {
/// runs the application's main loop until the user quits
pubfnrun(&mutself, terminal:&mut tui::Tui) -> Result<()> {
while!self.exit {
terminal.draw(|frame|self.render_frame(frame))?;
self.handle_events().wrap_err("handle events failed")?;
}
Ok(())
}
}
```

## Creating a recoverable error

[Section titled “Creating a recoverable error”](#creating-a-recoverable-error)

The tutorial needs a synthetic error to show how we can handle recoverable errors. Change `handle_key_event` to return a `color_eyre::Result` and make sure the calls to increment and decrement calls have the `?` operator to propagate the error to the caller.

```

impl App {
fnhandle_key_event(&mutself, key_event: KeyEvent) -> Result<()> {
matchkey_event.code {
KeyCode::Char('q') =>self.exit(),
KeyCode::Left =>self.decrement_counter()?,
KeyCode::Right =>self.increment_counter()?,
_=> {}
}
Ok(())
}
}
```

Let’s add an error that occurs when the counter is above 2. Also change both methods’ return types. Add the new error to the `increment_counter` method. You can use the `bail!` macro for this:

```

impl App {
fndecrement_counter(&mutself) -> Result<()> {
self.counter -=1;
Ok(())
}
fnincrement_counter(&mutself) -> Result<()> {
self.counter +=1;
ifself.counter >2 {
bail!("counter overflow");
}
Ok(())
}
}
```

In the `handle_events` method, add some extra information about which key caused the failure and update the return value.

```

impl App {
/// updates the application's state based on user input
fnhandle_events(&mutself) -> Result<()> {
match event::read()? {
// it's important to check that the event is a key press event as
// crossterm also emits key release and repeat events on Windows.
Event::Key(key_event) ifkey_event.kind == KeyEventKind::Press =>self
.handle_key_event(key_event)
.wrap_err_with(||format!("handling key event failed:\n{key_event:#?}")),
_=> Ok(()),
}
}
}
```

Update the tests for this method to unwrap the calls to handle\_key\_events. This will cause the test to fail if an error is returned.

```

mod tests {
#[test]
fnhandle_key_event() {
letmutapp= App::default();
app.handle_key_event(KeyCode::Right.into()).unwrap();
assert_eq!(app.counter, 1);
app.handle_key_event(KeyCode::Left.into()).unwrap();
assert_eq!(app.counter, 0);
letmutapp= App::default();
app.handle_key_event(KeyCode::Char('q').into()).unwrap();
assert!(app.exit);
}
}
```

Add tests for the panic and overflow conditions

```

mod tests {
#[test]
#[should_panic(expected ="attempt to subtract with overflow")]
fnhandle_key_event_panic() {
letmutapp= App::default();
let_=app.handle_key_event(KeyCode::Left.into());
}
#[test]
fnhandle_key_event_overflow() {
letmutapp= App::default();
assert!(app.handle_key_event(KeyCode::Right.into()).is_ok());
assert!(app.handle_key_event(KeyCode::Right.into()).is_ok());
assert_eq!(
app.handle_key_event(KeyCode::Right.into())
.unwrap_err()
.to_string(),
"counter overflow"
);
}
}
```

Run the tests:

```

running 4 tests
thread 'tests::handle_key_event_panic' panicked at code/counter-app-error-handling/src/main.rs:94:9:
attempt to subtract with overflow
test tests::handle_key_event ... okstack backtrace:
test tests::handle_key_event_overflow ... ok
test tests::render ... ok
20 collapsed lines
0: rust_begin_unwind
at /rustc/07dca489ac2d933c78d3c5158e3f43beefeb02ce/library/std/src/panicking.rs:645:5
1: core::panicking::panic_fmt
at /rustc/07dca489ac2d933c78d3c5158e3f43beefeb02ce/library/core/src/panicking.rs:72:14
2: core::panicking::panic
at /rustc/07dca489ac2d933c78d3c5158e3f43beefeb02ce/library/core/src/panicking.rs:144:5
3: counter_app_error_handling::App::decrement_counter
at ./src/main.rs:94:9
4: counter_app_error_handling::App::handle_key_event
at ./src/main.rs:79:30
5: counter_app_error_handling::tests::handle_key_event_panic
at ./src/main.rs:200:17
6: counter_app_error_handling::tests::handle_key_event_panic::{{closure}}
at ./src/main.rs:198:32
7: core::ops::function::FnOnce::call_once
at /rustc/07dca489ac2d933c78d3c5158e3f43beefeb02ce/library/core/src/ops/function.rs:250:5
8: core::ops::function::FnOnce::call_once
at /rustc/07dca489ac2d933c78d3c5158e3f43beefeb02ce/library/core/src/ops/function.rs:250:5
note: Some details are omitted, run with `RUST_BACKTRACE=full` for a verbose backtrace.
test tests::handle_key_event_panic - should panic ... ok
test result: ok. 4 passed; 0 failed; 0 ignored; 0 measured; 0 filtered out; finished in 0.01s
```

Putting this altogether, you should now have the following files.

```

use color_eyre::{
eyre::{bail, WrapErr},
Result,
};
use ratatui::{
buffer::Buffer,
crossterm::event::{self, Event, KeyCode, KeyEvent, KeyEventKind},
layout::Rect,
style::Stylize,
symbols::border,
text::{Line, Text},
widgets::{Block, Borders, Paragraph, Widget},
Frame,
};
mod tui;
fnmain() -> Result<()> {
color_eyre::install()?;
letmutterminal= tui::init()?;
letapp_result= App::default().run(&mutterminal);
iflet Err(err) = tui::restore() {
eprintln!(
"failed to restore terminal. Run `reset` or restart your terminal to recover: {err}"
);
}
app_result
}
#[derive(Debug, Default)]
pubstruct App {
counter: u8,
exit: bool,
}
impl App {
/// runs the application's main loop until the user quits
pubfnrun(&mutself, terminal:&mut tui::Tui) -> Result<()> {
while!self.exit {
terminal.draw(|frame|self.render_frame(frame))?;
self.handle_events().wrap_err("handle events failed")?;
}
Ok(())
}
fnrender_frame(&self, frame:&mut Frame) {
frame.render_widget(self, frame.area());
}
/// updates the application's state based on user input
fnhandle_events(&mutself) -> Result<()> {
match event::read()? {
// it's important to check that the event is a key press event as
// crossterm also emits key release and repeat events on Windows.
Event::Key(key_event) ifkey_event.kind == KeyEventKind::Press =>self
.handle_key_event(key_event)
.wrap_err_with(||format!("handling key event failed:\n{key_event:#?}")),
_=> Ok(()),
}
}
fnhandle_key_event(&mutself, key_event: KeyEvent) -> Result<()> {
matchkey_event.code {
KeyCode::Char('q') =>self.exit(),
KeyCode::Left =>self.decrement_counter()?,
KeyCode::Right =>self.increment_counter()?,
_=> {}
}
Ok(())
}
fnexit(&mutself) {
self.exit =true;
}
fndecrement_counter(&mutself) -> Result<()> {
self.counter -=1;
Ok(())
}
fnincrement_counter(&mutself) -> Result<()> {
self.counter +=1;
ifself.counter >2 {
bail!("counter overflow");
}
Ok(())
}
}
impl Widget for&App {
fnrender(self, area: Rect, buf:&mut Buffer) {
lettitle= Line::from(" Counter App Tutorial ".bold());
letinstructions= Line::from(vec![
" Decrement ".into(),
"<Left>".blue().bold(),
" Increment ".into(),
"<Right>".blue().bold(),
" Quit ".into(),
"<Q> ".blue().bold(),
]);
letblock= Block::default()
.title(title.centered())
.title_bottom(instructions.centered())
.borders(Borders::ALL)
.border_set(border::THICK);
letcounter_text= Text::from(vec![Line::from(vec![
"Value: ".into(),
self.counter.to_string().yellow(),
])]);
Paragraph::new(counter_text)
.centered()
.block(block)
.render(area, buf);
}
}
#[cfg(test)]
mod tests {
use ratatui::style::Style;
usesuper::*;
#[test]
fnrender() {
letapp= App::default();
letmutbuf= Buffer::empty(Rect::new(0, 0, 50, 4));
app.render(buf.area, &mutbuf);
letmutexpected= Buffer::with_lines(vec![
"┏━━━━━━━━━━━━━ Counter App Tutorial ━━━━━━━━━━━━━┓",
"┃                    Value: 0                    ┃",
"┃                                                ┃",
"┗━ Decrement <Left> Increment <Right> Quit <Q> ━━┛",
]);
lettitle_style= Style::new().bold();
letcounter_style= Style::new().yellow();
letkey_style= Style::new().blue().bold();
expected.set_style(Rect::new(14, 0, 22, 1), title_style);
expected.set_style(Rect::new(28, 1, 1, 1), counter_style);
expected.set_style(Rect::new(13, 3, 6, 1), key_style);
expected.set_style(Rect::new(30, 3, 7, 1), key_style);
expected.set_style(Rect::new(43, 3, 4, 1), key_style);
assert_eq!(buf, expected);
}
#[test]
fnhandle_key_event() {
letmutapp= App::default();
app.handle_key_event(KeyCode::Right.into()).unwrap();
assert_eq!(app.counter, 1);
app.handle_key_event(KeyCode::Left.into()).unwrap();
assert_eq!(app.counter, 0);
letmutapp= App::default();
app.handle_key_event(KeyCode::Char('q').into()).unwrap();
assert!(app.exit);
}
#[test]
#[should_panic(expected ="attempt to subtract with overflow")]
fnhandle_key_event_panic() {
letmutapp= App::default();
let_=app.handle_key_event(KeyCode::Left.into());
}
#[test]
fnhandle_key_event_overflow() {
letmutapp= App::default();
assert!(app.handle_key_event(KeyCode::Right.into()).is_ok());
assert!(app.handle_key_event(KeyCode::Right.into()).is_ok());
assert_eq!(
app.handle_key_event(KeyCode::Right.into())
.unwrap_err()
.to_string(),
"counter overflow"
);
}
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
/// A type alias for the terminal type used in this application
pubtype Tui = Terminal<CrosstermBackend<Stdout>>;
/// Initialize the terminal
pubfninit() -> io::Result<Tui> {
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

Experiment to see what happens when the application panics. The application has an intentional bug where it uses `u8` for the counter field, but doesn’t guard against decrementing this below 0. Run the app and press the **Left** arrow key.

![panic demo](https://ratatui.rs/_astro/panic.D9ocQdTm_2tGlPf.webp)

To get more information about where the error occurred, add `RUST_BACKTRACE=full` before the command.

![panic-full demo](https://ratatui.rs/_astro/panic-full.Cz0u1XOJ_Z2mUhmS.webp)

Experiment to see what happens when the application returns an unhandled error as a result. The app will cause this to happen when the counter increases past 2. Run the app and press the Right arrow 3 times.

![error demo](https://ratatui.rs/_astro/error.BpmoZUoW_20kgdG.webp)

To get more information about where the error occurred, add `RUST_BACKTRACE=full` before the command.

![error-full demo](https://ratatui.rs/_astro/error-full.Cog0iEHQ_3Hiwi.webp)