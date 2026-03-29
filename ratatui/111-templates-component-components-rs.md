---
title: Components.rs
url: https://ratatui.rs/templates/component/components-rs/
source: crawler
fetched_at: 2026-02-01T21:13:30.270349296-03:00
rendered_js: false
word_count: 980
summary: This document defines a Rust trait for building terminal user interface components, specifying the required methods for event handling, state management, and rendering.
tags:
    - rust
    - ratatui
    - tui
    - component-trait
    - event-handling
    - state-management
    - terminal-interface
category: api
---

In `components/mod.rs`, we implement a `trait` called `Component`:

```

pubtrait Component {
/// Register an action handler that can send actions for processing if necessary.
///
/// # Arguments
///
/// * `tx` - An unbounded sender that can send actions.
///
/// # Returns
///
/// * `Result<()>` - An Ok result or an error.
fnregister_action_handler(&mutself, tx: UnboundedSender<Action>) -> Result<()> {
let_=tx; // to appease clippy
Ok(())
}
/// Register a configuration handler that provides configuration settings if necessary.
///
/// # Arguments
///
/// * `config` - Configuration settings.
///
/// # Returns
///
/// * `Result<()>` - An Ok result or an error.
fnregister_config_handler(&mutself, config: Config) -> Result<()> {
let_=config; // to appease clippy
Ok(())
}
/// Initialize the component with a specified area if necessary.
///
/// # Arguments
///
/// * `area` - Rectangular area to initialize the component within.
///
/// # Returns
///
/// * `Result<()>` - An Ok result or an error.
fninit(&mutself, area: Size) -> Result<()> {
let_=area; // to appease clippy
Ok(())
}
/// Handle incoming events and produce actions if necessary.
///
/// # Arguments
///
/// * `event` - An optional event to be processed.
///
/// # Returns
///
/// * `Result<Option<Action>>` - An action to be processed or none.
fnhandle_events(&mutself, event: Option<Event>) -> Result<Option<Action>> {
letaction=matchevent {
Some(Event::Key(key_event)) =>self.handle_key_event(key_event)?,
Some(Event::Mouse(mouse_event)) =>self.handle_mouse_event(mouse_event)?,
_=> None,
};
Ok(action)
}
/// Handle key events and produce actions if necessary.
///
/// # Arguments
///
/// * `key` - A key event to be processed.
///
/// # Returns
///
/// * `Result<Option<Action>>` - An action to be processed or none.
fnhandle_key_event(&mutself, key: KeyEvent) -> Result<Option<Action>> {
let_=key; // to appease clippy
Ok(None)
}
/// Handle mouse events and produce actions if necessary.
///
/// # Arguments
///
/// * `mouse` - A mouse event to be processed.
///
/// # Returns
///
/// * `Result<Option<Action>>` - An action to be processed or none.
fnhandle_mouse_event(&mutself, mouse: MouseEvent) -> Result<Option<Action>> {
let_=mouse; // to appease clippy
Ok(None)
}
/// Update the state of the component based on a received action. (REQUIRED)
///
/// # Arguments
///
/// * `action` - An action that may modify the state of the component.
///
/// # Returns
///
/// * `Result<Option<Action>>` - An action to be processed or none.
fnupdate(&mutself, action: Action) -> Result<Option<Action>> {
let_=action; // to appease clippy
Ok(None)
}
/// Render the component on the screen. (REQUIRED)
///
/// # Arguments
///
/// * `f` - A frame used for rendering.
/// * `area` - The area in which the component should be drawn.
///
/// # Returns
///
/// * `Result<()>` - An Ok result or an error.
fndraw(&mutself, frame:&mut Frame, area: Rect) -> Result<()>;
}
```

I personally like keeping the functions for `handle_events` (i.e. event -&gt; action mapping), `dispatch` (i.e. action -&gt; state update mapping) and `render` (i.e. state -&gt; drawing mapping) all in one file for each component of my application.

Full code for the `components.rs` file is:

```

use color_eyre::Result;
use crossterm::event::{KeyEvent, MouseEvent};
use ratatui::{
Frame,
layout::{Rect, Size},
};
use tokio::sync::mpsc::UnboundedSender;
usecrate::{action::Action, config::Config, tui::Event};
pubmod fps;
pubmod home;
/// `Component` is a trait that represents a visual and interactive element of the user interface.
///
/// Implementors of this trait can be registered with the main application loop and will be able to
/// receive events, update state, and be rendered on the screen.
pubtrait Component {
/// Register an action handler that can send actions for processing if necessary.
///
/// # Arguments
///
/// * `tx` - An unbounded sender that can send actions.
///
/// # Returns
///
/// * `Result<()>` - An Ok result or an error.
fnregister_action_handler(&mutself, tx: UnboundedSender<Action>) -> Result<()> {
let_=tx; // to appease clippy
Ok(())
}
/// Register a configuration handler that provides configuration settings if necessary.
///
/// # Arguments
///
/// * `config` - Configuration settings.
///
/// # Returns
///
/// * `Result<()>` - An Ok result or an error.
fnregister_config_handler(&mutself, config: Config) -> Result<()> {
let_=config; // to appease clippy
Ok(())
}
/// Initialize the component with a specified area if necessary.
///
/// # Arguments
///
/// * `area` - Rectangular area to initialize the component within.
///
/// # Returns
///
/// * `Result<()>` - An Ok result or an error.
fninit(&mutself, area: Size) -> Result<()> {
let_=area; // to appease clippy
Ok(())
}
/// Handle incoming events and produce actions if necessary.
///
/// # Arguments
///
/// * `event` - An optional event to be processed.
///
/// # Returns
///
/// * `Result<Option<Action>>` - An action to be processed or none.
fnhandle_events(&mutself, event: Option<Event>) -> Result<Option<Action>> {
letaction=matchevent {
Some(Event::Key(key_event)) =>self.handle_key_event(key_event)?,
Some(Event::Mouse(mouse_event)) =>self.handle_mouse_event(mouse_event)?,
_=> None,
};
Ok(action)
}
/// Handle key events and produce actions if necessary.
///
/// # Arguments
///
/// * `key` - A key event to be processed.
///
/// # Returns
///
/// * `Result<Option<Action>>` - An action to be processed or none.
fnhandle_key_event(&mutself, key: KeyEvent) -> Result<Option<Action>> {
let_=key; // to appease clippy
Ok(None)
}
/// Handle mouse events and produce actions if necessary.
///
/// # Arguments
///
/// * `mouse` - A mouse event to be processed.
///
/// # Returns
///
/// * `Result<Option<Action>>` - An action to be processed or none.
fnhandle_mouse_event(&mutself, mouse: MouseEvent) -> Result<Option<Action>> {
let_=mouse; // to appease clippy
Ok(None)
}
/// Update the state of the component based on a received action. (REQUIRED)
///
/// # Arguments
///
/// * `action` - An action that may modify the state of the component.
///
/// # Returns
///
/// * `Result<Option<Action>>` - An action to be processed or none.
fnupdate(&mutself, action: Action) -> Result<Option<Action>> {
let_=action; // to appease clippy
Ok(None)
}
/// Render the component on the screen. (REQUIRED)
///
/// # Arguments
///
/// * `f` - A frame used for rendering.
/// * `area` - The area in which the component should be drawn.
///
/// # Returns
///
/// * `Result<()>` - An Ok result or an error.
fndraw(&mutself, frame:&mut Frame, area: Rect) -> Result<()>;
}
```