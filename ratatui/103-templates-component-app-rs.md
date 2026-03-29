---
title: App.rs
url: https://ratatui.rs/templates/component/app-rs/
source: crawler
fetched_at: 2026-02-01T21:13:34.463008636-03:00
rendered_js: false
word_count: 918
summary: This document explains architectural strategies for Terminal User Interfaces, contrasting simple blocking loops with action-based dispatch models for handling asynchronous tasks.
tags:
    - tui
    - event-loop
    - state-management
    - ratatui
    - rust-programming
    - software-architecture
category: concept
---

Finally, putting all the pieces together, we are almost ready to get the `Run` struct. Before we do, we should discuss the process of a TUI.

Most TUIs are single process, single threaded applications.

Get Key Event Update State Draw

When an application is structured like this, the TUI is blocking at each step:

1. Waiting for a Event.
   
   - If no key or mouse event in 250ms, send `Tick`.
2. Update the state of the app based on `event` or `action`.
3. `draw` the state of the app to the terminal using `ratatui`.

This works perfectly fine for small applications, and this is what I recommend starting out with. For *most* TUIs, you’ll never need to graduate from this process methodology.

Usually, `draw` and `get_events` are fast enough that it doesn’t matter. But if you do need to do a computationally demanding or I/O intensive task while updating state (e.g. reading a database, computing math or making a web request), your app may “hang” while it is doing so.

Let’s say a user presses `j` to scroll down a list. And every time the user presses `j` you want to check the web for additional items to add to the list.

What should happen when a user presses and holds `j`? It is up to you to decide how you would like your TUI application to behave in that instance.

You may decide that the desired behavior for your app is to hang while downloading new elements for the list, and all key presses while the app hangs are received and handled “instantly” after the download completes.

Or you may decide to `flush` all keyboard events so they are not buffered, and you may want to implement something like the following:

```

letmutapp= App::new();
loop {
// ...
letbefore_draw= Instant::now();
t.terminal.draw(|f|self.render(f))?;
// If drawing to the terminal is slow, flush all keyboard events so they're not buffered.
ifbefore_draw.elapsed() > Duration::from_millis(20) {
whilelet Ok(_) =events.try_next() {}
}
// ...
}
```

Alternatively, you may decide you want the app to update in the background, and a user should be able to scroll through the existing list while the app is downloading new elements.

In my experience, the trade-off is here is usually complexity for the developer versus ergonomics for the user.

Let’s say we weren’t worried about complexity, and were interested in performing a computationally demanding or I/O intensive task in the background.

To do this, we employ a model that dispatches and receives `Action`s to perform certain actions. This allows us to have actions that result in other actions easily. For example, if we have to make a network request, and then render the UI again, we can have an `update()` that looks like:

```

fnupdate(&mutself, action: Action) -> Option<Action> {
matchaction {
Action::Tick => {
self.last_tick_key_events.drain(..);
}
Action::Quit =>self.should_quit =true,
Action::Suspend =>self.should_suspend =true,
Action::Resume =>self.should_suspend =false,
Action::ClearScreen =>tui.terminal.clear()?,
Action::Resize(w, h) =>self.handle_resize(tui, w, h)?,
Action::Render =>self.render(tui)?,
Action::NetworkRequest => {
self.perform_expensive_request();
Some(Action::Render) // Triggers a render
}
_=> None,
}
}
```

A similar method is defined for each component, which allows them to send their `Action` to other parts of the app.

To do this, we set up an `action_tx` and an `action_rx` in the `App` struct.

```

pubstruct App {
should_quit: bool,
should_suspend: bool,
action_tx: mpsc::UnboundedSender<Action>,
action_rx: mpsc::UnboundedReceiver<Action>,
}
```

To handle multiple components produicing actions, like `Render`s and `Tick`s based on their own logic, each component has a `register_action_handler()` method, which allows them to send their `Action` to a central action handler.

Then, we have to handle actions sent by the components. For each component, if there is an action returned by its `update` method, we propagate it to the receiver. This ensures that all actions and handled. Thus our `handle_actions` function looks like:

```

fnhandle_actions(&mutself, tui:&mut Tui) -> Result<()> {
whilelet Ok(action) =self.action_rx.try_recv() {
ifaction!= Action::Tick &&action!= Action::Render {
debug!("{action:?}");
}
matchaction {
Action::Tick => {
self.last_tick_key_events.drain(..);
}
Action::Quit =>self.should_quit =true,
Action::Suspend =>self.should_suspend =true,
Action::Resume =>self.should_suspend =false,
Action::ClearScreen =>tui.terminal.clear()?,
Action::Resize(w, h) =>self.handle_resize(tui, w, h)?,
Action::Render =>self.render(tui)?,
_=> {}
}
forcomponentinself.components.iter_mut() {
iflet Some(action) =component.update(action.clone())? {
self.action_tx.send(action)?
};
}
}
Ok(())
}
```

Similar to actions, there are certain events that can happen while the app is running. For example, a keypress, a mouse click, and more. To handle this, the `app` struct has the `handle_event` and `handle_key_event` methods that are responsible for handling these events. These methods are also defined for all components. When an event occurs, we perform the necessary function and sometimes send an `Action` related to the event. The code for these two functions is:

```

asyncfnhandle_events(&mutself, tui:&mut Tui) -> Result<()> {
let Some(event) =tui.next_event().awaitelse {
return Ok(());
};
letaction_tx=self.action_tx.clone();
matchevent {
Event::Quit =>action_tx.send(Action::Quit)?,
Event::Tick =>action_tx.send(Action::Tick)?,
Event::Render =>action_tx.send(Action::Render)?,
Event::Resize(x, y) =>action_tx.send(Action::Resize(x, y))?,
Event::Key(key) =>self.handle_key_event(key)?,
_=> {}
}
forcomponentinself.components.iter_mut() {
iflet Some(action) =component.handle_events(Some(event.clone()))? {
action_tx.send(action)?;
}
}
Ok(())
}
fnhandle_key_event(&mutself, key: KeyEvent) -> Result<()> {
letaction_tx=self.action_tx.clone();
let Some(keymap) =self.config.keybindings.get(&self.mode) else {
return Ok(());
}; // See `config.rs`
matchkeymap.get(&vec![key]) {
Some(action) => {
info!("Got action: {action:?}");
action_tx.send(action.clone())?;
}
_=> {
// If the key was not handled as a single key action,
// then consider it for multi-key combinations.
self.last_tick_key_events.push(key);
// Check for multi-key combinations
iflet Some(action) =keymap.get(&self.last_tick_key_events) {
info!("Got action: {action:?}");
action_tx.send(action.clone())?;
}
}
}
Ok(())
}
```

Now our final architecture would look like this:

Render Thread Event Thread Main Thread Get Key Event Map Event to Action Send Action on action tx Recv Action Recv on render rx Dispatch Action Render Component Update Component

You can change around when “thread” or “task” does what in your application if you’d like.

It is up to you to decide is this pattern is worth it. In this template, we are going to keep things a little simpler. We are going to use just one thread or task to handle all the `Event`s.

Event Thread Main Thread Get Event Send Event on event tx Recv Event and Map to Action Update Component

All business logic will be located in a `App` struct.

```

#[derive(Default)]
struct App {
counter: i64,
}
impl App {
fnhandle_events(&mutself, event: Option<Event>) -> Action {
matchevent {
Some(Event::Quit) => Action::Quit,
Some(Event::AppTick) => Action::Tick,
Some(Event::Render) => Action::Render,
Some(Event::Key(key_event)) => {
iflet Some(key) =event {
matchkey.code {
KeyCode::Char('j') => Action::Increment,
KeyCode::Char('k') => Action::Decrement
_=> {}
}
}
},
Some(_) => Action::Noop,
None => Action::Noop,
}
}
fnupdate(&mutself, action: Action) {
matchaction {
Action::Tick =>self.tick(),
Action::Increment =>self.increment(),
Action::Decrement =>self.decrement(),
}
fnincrement(&mutself) {
self.counter +=1;
}
fndecrement(&mutself) {
self.counter -=1;
}
fnrender(&mutself, f:&mut Frame<'_>) {
f.render_widget(
Paragraph::new(format!(
"Press j or k to increment or decrement.\n\nCounter: {}",
self.counter
))
)
}
}
```

With that, our `App` becomes a little more simpler:

```

pubstruct App {
pubtick_rate: (u64, u64),
pubcomponent: Home,
pubshould_quit: bool,
}
impl Component {
pubfnnew(tick_rate: (u64, u64)) -> Result<Self> {
letcomponent= Home::new();
Ok(Self { tick_rate, component, should_quit:false, should_suspend:false })
}
pubasyncfnrun(&mutself) -> Result<()> {
let (action_tx, mutaction_rx) = mpsc::unbounded_channel();
letmuttui= Tui::new();
tui.enter()
loop {
iflet Some(e) =tui.next().await {
iflet Some(action) =self.component.handle_events(Some(e.clone())) {
action_tx.send(action)?;
}
}
whilelet Ok(action) =action_rx.try_recv().await {
matchaction {
Action::Render =>tui.draw(|f|self.component.render(f, f.area()))?,
Action::Quit =>self.should_quit =true,
_=>self.component.update(action),
}
}
ifself.should_quit {
tui.stop()?;
break;
}
}
tui.exit()
Ok(())
}
}
```

Now that we have a framework for driving our app forward, we can define a `run` method to start the app. It registers the event handlers for all components, and starts an event loop that handles events and actions.

```

pubasyncfnrun(&mutself) -> Result<()> {
letmuttui= Tui::new()?
// .mouse(true) // uncomment this line to enable mouse support
.tick_rate(self.tick_rate)
.frame_rate(self.frame_rate);
tui.enter()?;
forcomponentinself.components.iter_mut() {
component.register_action_handler(self.action_tx.clone())?;
}
forcomponentinself.components.iter_mut() {
component.register_config_handler(self.config.clone())?;
}
forcomponentinself.components.iter_mut() {
component.init(tui.size()?)?;
}
letaction_tx=self.action_tx.clone();
loop {
self.handle_events(&muttui).await?;
self.handle_actions(&muttui)?;
ifself.should_suspend {
tui.suspend()?;
action_tx.send(Action::Resume)?;
action_tx.send(Action::ClearScreen)?;
// tui.mouse(true);
tui.enter()?;
} elseifself.should_quit {
tui.stop()?;
break;
}
}
tui.exit()?;
Ok(())
}
```

To handle different modes of the app, we have a `mode` field in the `App` struct. Furthermore, for configurable multi-key combinations, we track the event in the last tick.

Full code for the `app.rs` file is:

```

use color_eyre::Result;
use crossterm::event::KeyEvent;
use ratatui::prelude::Rect;
use serde::{Deserialize, Serialize};
use tokio::sync::mpsc;
use tracing::{debug, info};
usecrate::{
action::Action,
components::{Component, fps::FpsCounter, home::Home},
config::Config,
tui::{Event, Tui},
};
pubstruct App {
config: Config,
tick_rate: f64,
frame_rate: f64,
components: Vec<Box<dyn Component>>,
should_quit: bool,
should_suspend: bool,
mode: Mode,
last_tick_key_events: Vec<KeyEvent>,
action_tx: mpsc::UnboundedSender<Action>,
action_rx: mpsc::UnboundedReceiver<Action>,
}
#[derive(Default, Debug, Copy, Clone, PartialEq, Eq, Hash, Serialize, Deserialize)]
pubenum Mode {
#[default]
Home,
}
impl App {
pubfnnew(tick_rate: f64, frame_rate: f64) -> Result<Self> {
let (action_tx, action_rx) = mpsc::unbounded_channel();
Ok(Self {
tick_rate,
frame_rate,
components:vec![Box::new(Home::new()), Box::new(FpsCounter::default())],
should_quit:false,
should_suspend:false,
config: Config::new()?,
mode: Mode::Home,
last_tick_key_events: Vec::new(),
action_tx,
action_rx,
})
}
pubasyncfnrun(&mutself) -> Result<()> {
letmuttui= Tui::new()?
// .mouse(true) // uncomment this line to enable mouse support
.tick_rate(self.tick_rate)
.frame_rate(self.frame_rate);
tui.enter()?;
forcomponentinself.components.iter_mut() {
component.register_action_handler(self.action_tx.clone())?;
}
forcomponentinself.components.iter_mut() {
component.register_config_handler(self.config.clone())?;
}
forcomponentinself.components.iter_mut() {
component.init(tui.size()?)?;
}
letaction_tx=self.action_tx.clone();
loop {
self.handle_events(&muttui).await?;
self.handle_actions(&muttui)?;
ifself.should_suspend {
tui.suspend()?;
action_tx.send(Action::Resume)?;
action_tx.send(Action::ClearScreen)?;
// tui.mouse(true);
tui.enter()?;
} elseifself.should_quit {
tui.stop()?;
break;
}
}
tui.exit()?;
Ok(())
}
asyncfnhandle_events(&mutself, tui:&mut Tui) -> Result<()> {
let Some(event) =tui.next_event().awaitelse {
return Ok(());
};
letaction_tx=self.action_tx.clone();
matchevent {
Event::Quit =>action_tx.send(Action::Quit)?,
Event::Tick =>action_tx.send(Action::Tick)?,
Event::Render =>action_tx.send(Action::Render)?,
Event::Resize(x, y) =>action_tx.send(Action::Resize(x, y))?,
Event::Key(key) =>self.handle_key_event(key)?,
_=> {}
}
forcomponentinself.components.iter_mut() {
iflet Some(action) =component.handle_events(Some(event.clone()))? {
action_tx.send(action)?;
}
}
Ok(())
}
fnhandle_key_event(&mutself, key: KeyEvent) -> Result<()> {
letaction_tx=self.action_tx.clone();
let Some(keymap) =self.config.keybindings.get(&self.mode) else {
return Ok(());
};
matchkeymap.get(&vec![key]) {
Some(action) => {
info!("Got action: {action:?}");
action_tx.send(action.clone())?;
}
_=> {
// If the key was not handled as a single key action,
// then consider it for multi-key combinations.
self.last_tick_key_events.push(key);
// Check for multi-key combinations
iflet Some(action) =keymap.get(&self.last_tick_key_events) {
info!("Got action: {action:?}");
action_tx.send(action.clone())?;
}
}
}
Ok(())
}
fnhandle_actions(&mutself, tui:&mut Tui) -> Result<()> {
whilelet Ok(action) =self.action_rx.try_recv() {
ifaction!= Action::Tick &&action!= Action::Render {
debug!("{action:?}");
}
matchaction {
Action::Tick => {
self.last_tick_key_events.drain(..);
}
Action::Quit =>self.should_quit =true,
Action::Suspend =>self.should_suspend =true,
Action::Resume =>self.should_suspend =false,
Action::ClearScreen =>tui.terminal.clear()?,
Action::Resize(w, h) =>self.handle_resize(tui, w, h)?,
Action::Render =>self.render(tui)?,
_=> {}
}
forcomponentinself.components.iter_mut() {
iflet Some(action) =component.update(action.clone())? {
self.action_tx.send(action)?
};
}
}
Ok(())
}
fnhandle_resize(&mutself, tui:&mut Tui, w: u16, h: u16) -> Result<()> {
tui.resize(Rect::new(0, 0, w, h))?;
self.render(tui)?;
Ok(())
}
fnrender(&mutself, tui:&mut Tui) -> Result<()> {
tui.draw(|frame| {
forcomponentinself.components.iter_mut() {
iflet Err(err) =component.draw(frame, frame.area()) {
let_=self
.action_tx
.send(Action::Error(format!("Failed to draw: {:?}", err)));
}
}
})?;
Ok(())
}
}
```