---
title: Popup
url: https://ratatui.rs/examples/apps/popup/
source: crawler
fetched_at: 2026-02-01T21:12:44.017631058-03:00
rendered_js: false
word_count: 307
summary: This document demonstrates how to use the Clear widget in Ratatui to create popup overlays by clearing a specific area of the terminal before rendering a new widget on top.
tags:
    - ratatui
    - rust
    - tui
    - popup-window
    - clear-widget
    - layout-management
    - ui-overlay
category: tutorial
---

Demonstrates how to render a widget over the top of previously rendered widgets using the [`Clear`](https://docs.rs/ratatui/latest/ratatui/widgets/struct.Clear.html) widget. Source [popup.rs](https://github.com/ratatui/ratatui/blob/main/examples/apps/popup/src/main.rs).

```

gitclonehttps://github.com/ratatui/ratatui.git--branchlatest
cdratatui
cargorun--example=popup--features=crossterm
```

![popup](https://ratatui.rs/_astro/popup.DReEVcA__16AaHV.webp)

```

//! # [Ratatui] Popup example
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
// See also https://github.com/joshka/tui-popup and
// https://github.com/sephiroth74/tui-confirm-dialog
use color_eyre::Result;
use ratatui::{
crossterm::event::{self, Event, KeyCode, KeyEventKind},
layout::{Constraint, Flex, Layout, Rect},
style::Stylize,
widgets::{Block, Clear, Paragraph, Wrap},
DefaultTerminal, Frame,
};
fnmain() -> Result<()> {
color_eyre::install()?;
letterminal= ratatui::init();
letapp_result= App::default().run(terminal);
ratatui::restore();
app_result
}
#[derive(Default)]
struct App {
show_popup: bool,
}
impl App {
fnrun(mutself, mutterminal: DefaultTerminal) -> Result<()> {
loop {
terminal.draw(|frame|self.draw(frame))?;
iflet Event::Key(key) = event::read()? {
ifkey.kind == KeyEventKind::Press {
matchkey.code {
KeyCode::Char('q') =>return Ok(()),
KeyCode::Char('p') =>self.show_popup =!self.show_popup,
_=> {}
}
}
}
}
}
fndraw(&self, frame:&mut Frame) {
letarea=frame.area();
letvertical= Layout::vertical([Constraint::Percentage(20), Constraint::Percentage(80)]);
let [instructions, content] =vertical.areas(area);
lettext=ifself.show_popup {
"Press p to close the popup"
} else {
"Press p to show the popup"
};
letparagraph= Paragraph::new(text.slow_blink())
.centered()
.wrap(Wrap { trim:true });
frame.render_widget(paragraph, instructions);
letblock= Block::bordered().title("Content").on_blue();
frame.render_widget(block, content);
ifself.show_popup {
letblock= Block::bordered().title("Popup");
letarea=popup_area(area, 60, 20);
frame.render_widget(Clear, area); //this clears out the background
frame.render_widget(block, area);
}
}
}
/// helper function to create a centered rect using up certain percentage of the available rect `r`
fnpopup_area(area: Rect, percent_x: u16, percent_y: u16) -> Rect {
letvertical= Layout::vertical([Constraint::Percentage(percent_y)]).flex(Flex::Center);
lethorizontal= Layout::horizontal([Constraint::Percentage(percent_x)]).flex(Flex::Center);
let [area] =vertical.areas(area);
let [area] =horizontal.areas(area);
area
}
```