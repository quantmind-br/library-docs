---
title: Tui.rs
url: https://ratatui.rs/templates/component/tui-rs/
source: crawler
fetched_at: 2026-02-01T21:13:30.244122782-03:00
rendered_js: false
word_count: 744
summary: This document explains the architecture and implementation of a Tui struct for managing terminal lifecycle and asynchronous event handling in Rust applications.
tags:
    - rust
    - ratatui
    - crossterm
    - tokio
    - terminal-ui
    - event-loop
    - async-programming
category: tutorial
---

This page will explain how the `tui.rs` file works in the `components` template.

In this section of the tutorial, we are going to discuss the basic components of the `Tui` struct.

You’ll find most people setup and teardown of a terminal application using `crossterm` like so:

```

fnsetup_terminal() -> Result<Terminal<CrosstermBackend<Stdout>>> {
letmutstdout= io::stdout();
crossterm::terminal::enable_raw_mode()?;
crossterm::execute!(stdout, EnterAlternateScreen, EnableMouseCapture, HideCursor)?;
Terminal::new(CrosstermBackend::new(stdout))
}
fnteardown_terminal(terminal:&mut Terminal<CrosstermBackend<Stdout>>) -> Result<()> {
letmutstdout= io::stdout();
crossterm::terminal::disable_raw_mode()?;
crossterm::execute!(stdout, LeaveAlternateScreen, DisableMouseCapture, ShowCursor)?;
Ok(())
}
fnmain() -> Result<()> {
letmutterminal=setup_terminal()?;
run_app(&mutterminal)?;
teardown_terminal(&mutterminal)?;
Ok(())
}
```

You can use `termion` or `termwiz` instead here, and you’ll have to change the implementation of `setup_terminal` and `teardown_terminal`.

See the [backends](https://ratatui.rs/concepts/backends/) page for more information.

Our implementation of the `Tui` struct has the following parts:

- Setup and teardown of the terminal
- The `Tui` struct itself
- Async event handling using `tokio`

## Terminal Setup and Teardown

[Section titled “Terminal Setup and Teardown”](#terminal-setup-and-teardown)

The `Tui` struct has a `terminal` field that is of type `ratatui::Terminal<Backend<Stdout>>`. This template uses `crossterm` as the backend. In the constructor for the `Tui` struct, we create and store a new `ratatui::Terminal`. The setup and teardown of the terminal is managed by the following methods:

```

impl Tui {
pubfnstart(&mutself) {
self.cancel(); // Cancel any existing task
self.cancellation_token = CancellationToken::new();
letevent_loop=Self::event_loop(
self.event_tx.clone(),
self.cancellation_token.clone(),
self.tick_rate,
self.frame_rate,
);
self.task = tokio::spawn(async {
event_loop.await;
});
}
pubfnenter(&mutself) -> Result<()> {
crossterm::terminal::enable_raw_mode()?;
crossterm::execute!(stdout(), EnterAlternateScreen, cursor::Hide)?;
ifself.mouse {
crossterm::execute!(stdout(), EnableMouseCapture)?;
}
ifself.paste {
crossterm::execute!(stdout(), EnableBracketedPaste)?;
}
self.start();
Ok(())
}
pubfnexit(&mutself) -> Result<()> {
self.stop()?;
if crossterm::terminal::is_raw_mode_enabled()? {
self.flush()?;
ifself.paste {
crossterm::execute!(stdout(), DisableBracketedPaste)?;
}
ifself.mouse {
crossterm::execute!(stdout(), DisableMouseCapture)?;
}
crossterm::execute!(stdout(), LeaveAlternateScreen, cursor::Show)?;
crossterm::terminal::disable_raw_mode()?;
}
Ok(())
}
pubfnstop(&self) -> Result<()> {
self.cancel();
letmutcounter=0;
while!self.task.is_finished() {
std::thread::sleep(Duration::from_millis(1));
counter+=1;
ifcounter>50 {
self.task.abort();
}
ifcounter>100 {
error!("Failed to abort task in 100 milliseconds for unknown reason");
break;
}
}
Ok(())
}
}
```

When we call the `run()` method on the `App` struct (the function that we called in our `main.rs` file), the first function that runs is the `Tui::enter()` function. This function prepares the terminal by enabling the terminal `raw_mode`, entering an `AlternateScreen`, and if the App has mouse controls, it enables mouse capture. Then, it calls the `Tui::start()` method to initialize the event loop.

```

self.task = tokio::spawn(async {
event_loop.await;
});
```

While we are in the “raw mode”, i.e. after we call `t.enter()`, any key presses in that terminal window are sent to `stdin`. We have to read these key presses from `stdin` if we want to act on them.

There are a number of different ways to do that. `crossterm` has a `event` module that implements features to read these key presses for us.

Let’s assume we were building a simple “counter” application, that incremented a counter when we pressed `j` and decremented a counter when we pressed `k`.

```

fnmain() -> Result {
letmutapp= App::new();
letmutt= Tui::new()?;
t.enter()?;
loop {
if crossterm::event::poll(Duration::from_millis(250))? {
iflet Event::Key(key) = crossterm::event::read()? {
matchkey.code {
KeyCode::Char('j') =>app.increment(),
KeyCode::Char('k') =>app.decrement(),
KeyCode::Char('q') =>break,
_=> (),
}
}
};
t.terminal.draw(|f| {
ui(app, f)
})?;
}
t.exit()?;
Ok(())
}
```

This works perfectly fine, and many small to medium size programs can get away with doing just that.

However, this approach conflates the key input handling with app state updates, and does so in the “draw” loop. The practical issue with this approach is we block the draw loop for 250 ms waiting for a key press. This can have odd side effects, for example pressing an holding a key will result in faster draws to the terminal.

In terms of architecture, the code could get complicated to reason about. For example, we may even want key presses to mean *different* things depending on the state of the app (when you are focused on an input field, you may want to enter the letter `"j"` into the text input field, but when focused on a list of items, you may want to scroll down the list.)

First, instead of polling, we are going to introduce channels to get the key presses asynchronously and send them over a channel. We will then receive on the channel in the main loop.

This block of code creates a new `tokio::task` to asynchronously run the event loop. This makes sure that our main thread isn’t block due to things like polling for `key_events`.

The `event_loop` function is defined as follows:

```

asyncfnevent_loop(
event_tx: UnboundedSender<Event>,
cancellation_token: CancellationToken,
tick_rate: f64,
frame_rate: f64,
) {
letmutevent_stream= EventStream::new();
letmuttick_interval=interval(Duration::from_secs_f64(1.0/tick_rate));
letmutrender_interval=interval(Duration::from_secs_f64(1.0/frame_rate));
// if this fails, then it's likely a bug in the calling code
event_tx
.send(Event::Init)
.expect("failed to send init event");
loop {
letevent= tokio::select! {
_=cancellation_token.cancelled() => {
break;
}
_=tick_interval.tick() => Event::Tick,
_=render_interval.tick() => Event::Render,
crossterm_event=event_stream.next().fuse() =>matchcrossterm_event {
Some(Ok(event)) =>matchevent {
CrosstermEvent::Key(key) ifkey.kind == KeyEventKind::Press => Event::Key(key),
CrosstermEvent::Mouse(mouse) => Event::Mouse(mouse),
CrosstermEvent::Resize(x, y) => Event::Resize(x, y),
CrosstermEvent::FocusLost => Event::FocusLost,
CrosstermEvent::FocusGained => Event::FocusGained,
CrosstermEvent::Paste(s) => Event::Paste(s),
_=>continue, // ignore other events
}
Some(Err(_)) => Event::Error,
None =>break, // the event stream has stopped and will not produce any more events
},
};
ifevent_tx.send(event).is_err() {
// the receiver has been dropped, so there's no point in continuing the loop
break;
}
}
cancellation_token.cancel();
}
```

The event loop function takes an `event_tx`. It uses this to send events (like KeyPresses) to other parts of our app. This is done using unbounded Multiple Producer Single Consumer (`mpsc`) channels. The function creates initializes the tick rate (time delay between `ticks`), frame rate, and an `event_stream`. A `tick` is a fundamental unit of time for our app. Think of it as a `CLOCK` for our app, similar to ones found in microcontrollers. Every tick, the execution of our app moves forward. The default tick rate is 4 ticks per second (also known as TPS). After this, the loop gets events and passes them to our app. The possible events are:

```

pubenum Event {
Init,
Quit,
Error,
Closed,
Tick,
Render,
FocusGained,
FocusLost,
Paste(String),
Key(KeyEvent),
Mouse(MouseEvent),
Resize(u16, u16),
}
```

## Cleanup and Teardown

[Section titled “Cleanup and Teardown”](#cleanup-and-teardown)

When it’s time to stop the app, the `Tui` struct has a `cancellation_token` field. This is a `CancellationToken` that can be used to stop the `tokio` task on request. When the `exit` method is called, it calls the `stop` method, which stops all pending `tokio` tasks. After this, we clean up the terminal and make sure that we don’t leave the user’s terminal in an unusable state. In case our app terminates unexpectedly, we don’t want to ruin our user’s terminal. So we implement the `Drop` trait on the `Tui` struct. When it is dropped, it calls the exit function, restoring the terminal.

```

impl Drop for Tui {
fndrop(&mutself) {
self.exit().unwrap();
}
}
```

```

use std::{
io::{Stdout, stdout},
ops::{Deref, DerefMut},
time::Duration,
};
use color_eyre::Result;
use crossterm::{
cursor,
event::{
DisableBracketedPaste, DisableMouseCapture, EnableBracketedPaste, EnableMouseCapture,
Event as CrosstermEvent, EventStream, KeyEvent, KeyEventKind, MouseEvent,
},
terminal::{EnterAlternateScreen, LeaveAlternateScreen},
};
use futures::{FutureExt, StreamExt};
use ratatui::backend::CrosstermBackend as Backend;
use serde::{Deserialize, Serialize};
use tokio::{
sync::mpsc::{self, UnboundedReceiver, UnboundedSender},
task::JoinHandle,
time::interval,
};
use tokio_util::sync::CancellationToken;
use tracing::error;
#[derive(Clone, Debug, Serialize, Deserialize)]
pubenum Event {
Init,
Quit,
Error,
Closed,
Tick,
Render,
FocusGained,
FocusLost,
Paste(String),
Key(KeyEvent),
Mouse(MouseEvent),
Resize(u16, u16),
}
pubstruct Tui {
pubterminal: ratatui::Terminal<Backend<Stdout>>,
pubtask: JoinHandle<()>,
pubcancellation_token: CancellationToken,
pubevent_rx: UnboundedReceiver<Event>,
pubevent_tx: UnboundedSender<Event>,
pubframe_rate: f64,
pubtick_rate: f64,
pubmouse: bool,
pubpaste: bool,
}
impl Tui {
pubfnnew() -> Result<Self> {
let (event_tx, event_rx) = mpsc::unbounded_channel();
Ok(Self {
terminal: ratatui::Terminal::new(Backend::new(stdout()))?,
task: tokio::spawn(async {}),
cancellation_token: CancellationToken::new(),
event_rx,
event_tx,
frame_rate:60.0,
tick_rate:4.0,
mouse:false,
paste:false,
})
}
pubfntick_rate(mutself, tick_rate: f64) ->Self {
self.tick_rate =tick_rate;
self
}
pubfnframe_rate(mutself, frame_rate: f64) ->Self {
self.frame_rate =frame_rate;
self
}
pubfnmouse(mutself, mouse: bool) ->Self {
self.mouse =mouse;
self
}
pubfnpaste(mutself, paste: bool) ->Self {
self.paste =paste;
self
}
pubfnstart(&mutself) {
self.cancel(); // Cancel any existing task
self.cancellation_token = CancellationToken::new();
letevent_loop=Self::event_loop(
self.event_tx.clone(),
self.cancellation_token.clone(),
self.tick_rate,
self.frame_rate,
);
self.task = tokio::spawn(async {
event_loop.await;
});
}
asyncfnevent_loop(
event_tx: UnboundedSender<Event>,
cancellation_token: CancellationToken,
tick_rate: f64,
frame_rate: f64,
) {
letmutevent_stream= EventStream::new();
letmuttick_interval=interval(Duration::from_secs_f64(1.0/tick_rate));
letmutrender_interval=interval(Duration::from_secs_f64(1.0/frame_rate));
// if this fails, then it's likely a bug in the calling code
event_tx
.send(Event::Init)
.expect("failed to send init event");
loop {
letevent= tokio::select! {
_=cancellation_token.cancelled() => {
break;
}
_=tick_interval.tick() => Event::Tick,
_=render_interval.tick() => Event::Render,
crossterm_event=event_stream.next().fuse() =>matchcrossterm_event {
Some(Ok(event)) =>matchevent {
CrosstermEvent::Key(key) ifkey.kind == KeyEventKind::Press => Event::Key(key),
CrosstermEvent::Mouse(mouse) => Event::Mouse(mouse),
CrosstermEvent::Resize(x, y) => Event::Resize(x, y),
CrosstermEvent::FocusLost => Event::FocusLost,
CrosstermEvent::FocusGained => Event::FocusGained,
CrosstermEvent::Paste(s) => Event::Paste(s),
_=>continue, // ignore other events
}
Some(Err(_)) => Event::Error,
None =>break, // the event stream has stopped and will not produce any more events
},
};
ifevent_tx.send(event).is_err() {
// the receiver has been dropped, so there's no point in continuing the loop
break;
}
}
cancellation_token.cancel();
}
pubfnstop(&self) -> Result<()> {
self.cancel();
letmutcounter=0;
while!self.task.is_finished() {
std::thread::sleep(Duration::from_millis(1));
counter+=1;
ifcounter>50 {
self.task.abort();
}
ifcounter>100 {
error!("Failed to abort task in 100 milliseconds for unknown reason");
break;
}
}
Ok(())
}
pubfnenter(&mutself) -> Result<()> {
crossterm::terminal::enable_raw_mode()?;
crossterm::execute!(stdout(), EnterAlternateScreen, cursor::Hide)?;
ifself.mouse {
crossterm::execute!(stdout(), EnableMouseCapture)?;
}
ifself.paste {
crossterm::execute!(stdout(), EnableBracketedPaste)?;
}
self.start();
Ok(())
}
pubfnexit(&mutself) -> Result<()> {
self.stop()?;
if crossterm::terminal::is_raw_mode_enabled()? {
self.flush()?;
ifself.paste {
crossterm::execute!(stdout(), DisableBracketedPaste)?;
}
ifself.mouse {
crossterm::execute!(stdout(), DisableMouseCapture)?;
}
crossterm::execute!(stdout(), LeaveAlternateScreen, cursor::Show)?;
crossterm::terminal::disable_raw_mode()?;
}
Ok(())
}
pubfncancel(&self) {
self.cancellation_token.cancel();
}
pubfnsuspend(&mutself) -> Result<()> {
self.exit()?;
#[cfg(not(windows))]
signal_hook::low_level::raise(signal_hook::consts::signal::SIGTSTP)?;
Ok(())
}
pubfnresume(&mutself) -> Result<()> {
self.enter()?;
Ok(())
}
pubasyncfnnext_event(&mutself) -> Option<Event> {
self.event_rx.recv().await
}
}
impl Deref for Tui {
type Target = ratatui::Terminal<Backend<Stdout>>;
fnderef(&self) ->&Self::Target {
&self.terminal
}
}
impl DerefMut for Tui {
fnderef_mut(&mutself) ->&mutSelf::Target {
&mutself.terminal
}
}
impl Drop for Tui {
fndrop(&mutself) {
self.exit().unwrap();
}
}
```