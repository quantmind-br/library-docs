---
title: Tui with Terminal and EventHandler
url: https://ratatui.rs/recipes/apps/terminal-and-event-handler/
source: crawler
fetched_at: 2026-02-01T21:13:13.180378882-03:00
rendered_js: false
word_count: 94
summary: This document provides a reusable implementation of a TUI helper struct in Rust for managing terminal state, asynchronous event loops, and raw mode handling using Ratatui and Tokio.
tags:
    - rust
    - ratatui
    - tui-development
    - tokio
    - event-loop
    - terminal-interface
    - asynchronous-programming
category: guide
---

then you can copy-paste this `Tui` struct into your project.

```

cargoaddratatuitokiotokio_utilfutures# required
cargoaddcolor_eyreserdeserde_derive# optional
```

```

use std::{
ops::{Deref, DerefMut},
time::Duration,
};
use color_eyre::eyre::Result;
use futures::{FutureExt, StreamExt};
use ratatui::backend::CrosstermBackend as Backend;
use ratatui::crossterm::{
cursor,
event::{
DisableBracketedPaste, DisableMouseCapture, EnableBracketedPaste, EnableMouseCapture, Event as CrosstermEvent,
KeyEvent, KeyEventKind, MouseEvent,
},
terminal::{EnterAlternateScreen, LeaveAlternateScreen},
};
use serde::{Deserialize, Serialize};
use tokio::{
sync::mpsc::{self, UnboundedReceiver, UnboundedSender},
task::JoinHandle,
};
use tokio_util::sync::CancellationToken;
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
pubterminal: ratatui::Terminal<Backend<std::io::Stderr>>,
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
lettick_rate=4.0;
letframe_rate=60.0;
letterminal= ratatui::Terminal::new(Backend::new(std::io::stderr()))?;
let (event_tx, event_rx) = mpsc::unbounded_channel();
letcancellation_token= CancellationToken::new();
lettask= tokio::spawn(async {});
letmouse=false;
letpaste=false;
Ok(Self { terminal, task, cancellation_token, event_rx, event_tx, frame_rate, tick_rate, mouse, paste })
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
lettick_delay= std::time::Duration::from_secs_f64(1.0/self.tick_rate);
letrender_delay= std::time::Duration::from_secs_f64(1.0/self.frame_rate);
self.cancel();
self.cancellation_token = CancellationToken::new();
let_cancellation_token=self.cancellation_token.clone();
let_event_tx=self.event_tx.clone();
self.task = tokio::spawn(asyncmove {
letmutreader= crossterm::event::EventStream::new();
letmuttick_interval= tokio::time::interval(tick_delay);
letmutrender_interval= tokio::time::interval(render_delay);
_event_tx.send(Event::Init).unwrap();
loop {
lettick_delay=tick_interval.tick();
letrender_delay=render_interval.tick();
letcrossterm_event=reader.next().fuse();
tokio::select! {
_=_cancellation_token.cancelled() => {
break;
}
maybe_event=crossterm_event=> {
matchmaybe_event {
Some(Ok(evt)) => {
matchevt {
CrosstermEvent::Key(key) => {
ifkey.kind == KeyEventKind::Press {
_event_tx.send(Event::Key(key)).unwrap();
}
},
CrosstermEvent::Mouse(mouse) => {
_event_tx.send(Event::Mouse(mouse)).unwrap();
},
CrosstermEvent::Resize(x, y) => {
_event_tx.send(Event::Resize(x, y)).unwrap();
},
CrosstermEvent::FocusLost => {
_event_tx.send(Event::FocusLost).unwrap();
},
CrosstermEvent::FocusGained => {
_event_tx.send(Event::FocusGained).unwrap();
},
CrosstermEvent::Paste(s) => {
_event_tx.send(Event::Paste(s)).unwrap();
},
}
}
Some(Err(_)) => {
_event_tx.send(Event::Error).unwrap();
}
None => {},
}
},
_=tick_delay=> {
_event_tx.send(Event::Tick).unwrap();
},
_=render_delay=> {
_event_tx.send(Event::Render).unwrap();
},
}
}
});
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
log::error!("Failed to abort task in 100 milliseconds for unknown reason");
break;
}
}
Ok(())
}
pubfnenter(&mutself) -> Result<()> {
crossterm::terminal::enable_raw_mode()?;
crossterm::execute!(std::io::stderr(), EnterAlternateScreen, cursor::Hide)?;
ifself.mouse {
crossterm::execute!(std::io::stderr(), EnableMouseCapture)?;
}
ifself.paste {
crossterm::execute!(std::io::stderr(), EnableBracketedPaste)?;
}
self.start();
Ok(())
}
pubfnexit(&mutself) -> Result<()> {
self.stop()?;
if crossterm::terminal::is_raw_mode_enabled()? {
self.flush()?;
ifself.paste {
crossterm::execute!(std::io::stderr(), DisableBracketedPaste)?;
}
ifself.mouse {
crossterm::execute!(std::io::stderr(), DisableMouseCapture)?;
}
crossterm::execute!(std::io::stderr(), LeaveAlternateScreen, cursor::Show)?;
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
pubasyncfnnext(&mutself) -> Option<Event> {
self.event_rx.recv().await
}
}
impl Deref for Tui {
type Target = ratatui::Terminal<Backend<std::io::Stderr>>;
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

```

mod tui;
impl App {
asyncfnrun(&mutself) -> Result<()> {
letmuttui= tui::Tui::new()?
.tick_rate(4.0) // 4 ticks per second
.frame_rate(30.0); // 30 frames per second
tui.enter()?; // Starts event handler, enters raw mode, enters alternate screen
loop {
tui.draw(|f| { // Deref allows calling `tui.terminal.draw`
self.ui(f);
})?;
iflet Some(evt) =tui.next().await { // `tui.next().await` blocks till next event
letmutmaybe_action=self.handle_event(evt);
whilelet Some(action) =maybe_action {
maybe_action=self.update(action);
}
};
ifself.should_quit {
break;
}
}
tui.exit()?; // stops event handler, exits raw mode, exits alternate screen
Ok(())
}
}
```