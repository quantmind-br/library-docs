---
title: Hello World
url: https://ratatui.rs/examples/apps/hello_world/
source: crawler
fetched_at: 2026-02-01T21:12:42.041485436-03:00
rendered_js: false
word_count: 441
summary: This document provides a minimal example of a terminal user interface application using Ratatui, demonstrating basic setup, rendering, and event loop management.
tags:
    - rust
    - ratatui
    - terminal-ui
    - hello-world
    - event-loop
    - widget-rendering
category: tutorial
---

Demonstrates a basic hello world app. Source [hello-world.rs](https://github.com/ratatui/ratatui/blob/main/examples/apps/hello-world/src/main.rs).

```

gitclonehttps://github.com/ratatui/ratatui.git--branchlatest
cdratatui
cargorun--example=hello_world--features=crossterm
```

![hello_world](https://ratatui.rs/_astro/hello_world.DcmoHvlr_pCKA5.webp)

```

//! # [Ratatui] Hello World example
//!
//! The latest version of this example is available in the [examples] folder in the repository.
//!
//! Please note that the examples are designed to be run against the `main` branch of the Github
//! repository. This means that you may not be able to compile with the latest release version on
//! crates.io, or the one that you have installed locally.
//!
//! See the [examples readme] for more information on finding examples that match the version of the
//! library you are using.
//!
//! [Ratatui]: https://github.com/ratatui/ratatui
//! [examples]: https://github.com/ratatui/ratatui/blob/main/examples
//! [examples readme]: https://github.com/ratatui/ratatui/blob/main/examples/README.md
use std::time::Duration;
use color_eyre::{eyre::Context, Result};
use ratatui::{
crossterm::event::{self, Event, KeyCode},
widgets::Paragraph,
DefaultTerminal, Frame,
};
/// This is a bare minimum example. There are many approaches to running an application loop, so
/// this is not meant to be prescriptive. It is only meant to demonstrate the basic setup and
/// teardown of a terminal application.
///
/// This example does not handle events or update the application state. It just draws a greeting
/// and exits when the user presses 'q'.
fnmain() -> Result<()> {
color_eyre::install()?; // augment errors / panics with easy to read messages
letterminal= ratatui::init();
letapp_result=run(terminal).context("app loop failed");
ratatui::restore();
app_result
}
/// Run the application loop. This is where you would handle events and update the application
/// state. This example exits when the user presses 'q'. Other styles of application loops are
/// possible, for example, you could have multiple application states and switch between them based
/// on events, or you could have a single application state and update it based on events.
fnrun(mutterminal: DefaultTerminal) -> Result<()> {
loop {
terminal.draw(draw)?;
ifshould_quit()? {
break;
}
}
Ok(())
}
/// Render the application. This is where you would draw the application UI. This example draws a
/// greeting.
fndraw(frame:&mut Frame) {
letgreeting= Paragraph::new("Hello World! (press 'q' to quit)");
frame.render_widget(greeting, frame.area());
}
/// Check if the user has pressed 'q'. This is where you would handle events. This example just
/// checks if the user has pressed 'q' and returns true if they have. It does not handle any other
/// events. There is a 250ms timeout on the event poll to ensure that the terminal is rendered at
/// least once every 250ms. This allows you to do other work in the application loop, such as
/// updating the application state, without blocking the event loop for too long.
fnshould_quit() -> Result<bool> {
if event::poll(Duration::from_millis(250)).context("event poll failed")? {
iflet Event::Key(key) = event::read().context("event read failed")? {
return Ok(KeyCode::Char('q') ==key.code);
}
}
Ok(false)
}
```