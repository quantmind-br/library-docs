---
title: Docs.rs
url: https://ratatui.rs/examples/apps/docsrs/
source: crawler
fetched_at: 2026-02-01T21:12:40.709140578-03:00
rendered_js: false
word_count: 340
summary: This document provides example Rust code for the Ratatui library, demonstrating how to implement terminal user interfaces with layouts, text styling, and event handling.
tags:
    - rust
    - ratatui
    - tui
    - terminal-ui
    - layout
    - styling
    - event-handling
category: tutorial
---

Several examples used for importing into the main docs.rs page.

```

gitclonehttps://github.com/ratatui/ratatui.git--branchlatest
cdratatui
cargorun--example=docsrs--features=crossterm
```

```

//! # [Ratatui] Docs.rs example
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
use color_eyre::Result;
use ratatui::{
crossterm::event::{self, Event, KeyCode},
layout::{Constraint, Layout},
style::{Color, Modifier, Style, Stylize},
text::{Line, Span, Text},
widgets::{Block, Borders, Paragraph},
DefaultTerminal, Frame,
};
/// Example code for lib.rs
///
/// When cargo-rdme supports doc comments that import from code, this will be imported
/// rather than copied to the lib.rs file.
fnmain() -> Result<()> {
color_eyre::install()?;
letfirst_arg= std::env::args().nth(1).unwrap_or_default();
letterminal= ratatui::init();
letapp_result=run(terminal, &first_arg);
ratatui::restore();
app_result
}
fnrun(mutterminal: DefaultTerminal, first_arg:&str) -> Result<()> {
letmutshould_quit=false;
while!should_quit {
terminal.draw(matchfirst_arg {
"layout"=>layout,
"styling"=>styling,
_=>hello_world,
})?;
should_quit=handle_events()?;
}
Ok(())
}
fnhandle_events() -> std::io::Result<bool> {
iflet Event::Key(key) = event::read()? {
ifkey.kind == event::KeyEventKind::Press &&key.code == KeyCode::Char('q') {
return Ok(true);
}
}
Ok(false)
}
fnhello_world(frame:&mut Frame) {
frame.render_widget(
Paragraph::new("Hello World!").block(Block::bordered().title("Greeting")),
frame.area(),
);
}
fnlayout(frame:&mut Frame) {
letvertical= Layout::vertical([
Constraint::Length(1),
Constraint::Min(0),
Constraint::Length(1),
]);
lethorizontal= Layout::horizontal([Constraint::Ratio(1, 2); 2]);
let [title_bar, main_area, status_bar] =vertical.areas(frame.area());
let [left, right] =horizontal.areas(main_area);
frame.render_widget(
Block::new().borders(Borders::TOP).title("Title Bar"),
title_bar,
);
frame.render_widget(
Block::new().borders(Borders::TOP).title("Status Bar"),
status_bar,
);
frame.render_widget(Block::bordered().title("Left"), left);
frame.render_widget(Block::bordered().title("Right"), right);
}
fnstyling(frame:&mut Frame) {
letareas= Layout::vertical([
Constraint::Length(1),
Constraint::Length(1),
Constraint::Length(1),
Constraint::Length(1),
Constraint::Min(0),
])
.split(frame.area());
letspan1= Span::raw("Hello ");
letspan2= Span::styled(
"World",
Style::new()
.fg(Color::Green)
.bg(Color::White)
.add_modifier(Modifier::BOLD),
);
letspan3="!".red().on_light_yellow().italic();
letline= Line::from(vec![span1, span2, span3]);
lettext: Text = Text::from(vec![line]);
frame.render_widget(Paragraph::new(text), areas[0]);
// or using the short-hand syntax and implicit conversions
frame.render_widget(
Paragraph::new("Hello World!".red().on_white().bold()),
areas[1],
);
// to style the whole widget instead of just the text
frame.render_widget(
Paragraph::new("Hello World!").style(Style::new().red().on_white()),
areas[2],
);
// or using the short-hand syntax
frame.render_widget(Paragraph::new("Hello World!").blue().on_yellow(), areas[3]);
}
```