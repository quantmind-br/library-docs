---
title: Modifiers
url: https://ratatui.rs/examples/style/modifiers/
source: crawler
fetched_at: 2026-02-01T21:12:48.435749083-03:00
rendered_js: false
word_count: 318
summary: This document provides a practical example of how to use text modifiers and color combinations in the Ratatui library to style terminal user interfaces.
tags:
    - ratatui
    - rust
    - terminal-styling
    - text-modifiers
    - ui-development
category: tutorial
---

Demonstrates the style [`Modifiers`](https://docs.rs/ratatui/latest/ratatui/style/struct.Modifier.html)

```

gitclonehttps://github.com/ratatui/ratatui.git--branchlatest
cdratatui
cargorun--example=modifiers--features=crossterm
```

![modifiers](https://ratatui.rs/_astro/modifiers.R_TsFsSS_1ics8i.webp)

```

//! # [Ratatui] Modifiers example
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
// This example is useful for testing how your terminal emulator handles different modifiers.
// It will render a grid of combinations of foreground and background colors with all
// modifiers applied to them.
use std::{error::Error, iter::once, result};
use itertools::Itertools;
use ratatui::{
crossterm::event::{self, Event, KeyCode, KeyEventKind},
layout::{Constraint, Layout},
style::{Color, Modifier, Style, Stylize},
text::Line,
widgets::Paragraph,
DefaultTerminal, Frame,
};
type Result<T> = result::Result<T, Box<dyn Error>>;
fnmain() -> Result<()> {
color_eyre::install()?;
letterminal= ratatui::init();
letapp_result=run(terminal);
ratatui::restore();
app_result
}
fnrun(mutterminal: DefaultTerminal) -> Result<()> {
loop {
terminal.draw(draw)?;
iflet Event::Key(key) = event::read()? {
ifkey.kind == KeyEventKind::Press &&key.code == KeyCode::Char('q') {
return Ok(());
}
}
}
}
fndraw(frame:&mut Frame) {
letvertical= Layout::vertical([Constraint::Length(1), Constraint::Min(0)]);
let [text_area, main_area] =vertical.areas(frame.area());
frame.render_widget(
Paragraph::new("Note: not all terminals support all modifiers")
.style(Style::default().fg(Color::Red).add_modifier(Modifier::BOLD)),
text_area,
);
letlayout= Layout::vertical([Constraint::Length(1); 50])
.split(main_area)
.iter()
.flat_map(|area| {
Layout::horizontal([Constraint::Percentage(20); 5])
.split(*area)
.to_vec()
})
.collect_vec();
letcolors= [
Color::Black,
Color::DarkGray,
Color::Gray,
Color::White,
Color::Red,
];
letall_modifiers=once(Modifier::empty())
.chain(Modifier::all().iter())
.collect_vec();
letmutindex=0;
forbgin&colors {
forfgin&colors {
formodifierin&all_modifiers {
letmodifier_name=format!("{modifier:11?}");
letpadding= ("").repeat(12-modifier_name.len());
letparagraph= Paragraph::new(Line::from(vec![
modifier_name.fg(*fg).bg(*bg).add_modifier(*modifier),
padding.fg(*fg).bg(*bg).add_modifier(*modifier),
// This is a hack to work around a bug in VHS which is used for rendering the
// examples to gifs. The bug is that the background color of a paragraph seems
// to bleed into the next character.
".".black().on_black(),
]));
frame.render_widget(paragraph, layout[index]);
index+=1;
}
}
}
}
```