---
title: Barchart
url: https://ratatui.rs/examples/widgets/barchart/
source: crawler
fetched_at: 2026-02-01T21:12:49.288758849-03:00
rendered_js: false
word_count: 350
summary: This document demonstrates how to implement and customize vertical and horizontal bar charts using the Ratatui BarChart widget.
tags:
    - ratatui
    - rust
    - barchart
    - terminal-ui
    - widgets
    - data-visualization
category: tutorial
---

Demonstrates the [`BarChart`](https://docs.rs/ratatui/latest/ratatui/widgets/struct.BarChart.html) widget.

```

gitclonehttps://github.com/ratatui/ratatui.git--branchlatest
cdratatui
cargorun--example=barchart--features=crossterm
```

![Barchart](https://ratatui.rs/_astro/barchart.V3Sio283_ZhxYa8.webp)

```

//! # [Ratatui] `BarChart` example
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
use rand::{rng, Rng};
use ratatui::{
crossterm::event::{self, Event, KeyCode, KeyEventKind},
layout::{Constraint, Direction, Layout},
style::{Color, Style, Stylize},
text::Line,
widgets::{Bar, BarChart, BarGroup, Block},
DefaultTerminal, Frame,
};
fnmain() -> Result<()> {
color_eyre::install()?;
letterminal= ratatui::init();
letapp_result= App::new().run(terminal);
ratatui::restore();
app_result
}
struct App {
should_exit: bool,
temperatures: Vec<u8>,
}
impl App {
fnnew() ->Self {
letmutrng=rng();
lettemperatures= (0..24).map(|_|rng.random_range(50..90)).collect();
Self {
should_exit:false,
temperatures,
}
}
fnrun(mutself, mutterminal: DefaultTerminal) -> Result<()> {
while!self.should_exit {
terminal.draw(|frame|self.draw(frame))?;
self.handle_events()?;
}
Ok(())
}
fnhandle_events(&mutself) -> Result<()> {
iflet Event::Key(key) = event::read()? {
ifkey.kind == KeyEventKind::Press &&key.code == KeyCode::Char('q') {
self.should_exit =true;
}
}
Ok(())
}
fndraw(&self, frame:&mut Frame) {
let [title, vertical, horizontal] = Layout::vertical([
Constraint::Length(1),
Constraint::Fill(1),
Constraint::Fill(1),
])
.spacing(1)
.areas(frame.area());
frame.render_widget("Barchart".bold().into_centered_line(), title);
frame.render_widget(vertical_barchart(&self.temperatures), vertical);
frame.render_widget(horizontal_barchart(&self.temperatures), horizontal);
}
}
/// Create a vertical bar chart from the temperatures data.
fnvertical_barchart(temperatures:&[u8]) -> BarChart {
letbars: Vec<Bar> =temperatures
.iter()
.enumerate()
.map(|(hour, value)|vertical_bar(hour, value))
.collect();
lettitle= Line::from("Weather (Vertical)").centered();
BarChart::default()
.data(BarGroup::default().bars(&bars))
.block(Block::new().title(title))
.bar_width(5)
}
fnvertical_bar(hour: usize, temperature:&u8) -> Bar {
Bar::default()
.value(u64::from(*temperature))
.label(Line::from(format!("{hour:>02}:00")))
.text_value(format!("{temperature:>3}°"))
.style(temperature_style(*temperature))
.value_style(temperature_style(*temperature).reversed())
}
/// Create a horizontal bar chart from the temperatures data.
fnhorizontal_barchart(temperatures:&[u8]) -> BarChart {
letbars: Vec<Bar> =temperatures
.iter()
.enumerate()
.map(|(hour, value)|horizontal_bar(hour, value))
.collect();
lettitle= Line::from("Weather (Horizontal)").centered();
BarChart::default()
.block(Block::new().title(title))
.data(BarGroup::default().bars(&bars))
.bar_width(1)
.bar_gap(0)
.direction(Direction::Horizontal)
}
fnhorizontal_bar(hour: usize, temperature:&u8) -> Bar {
letstyle=temperature_style(*temperature);
Bar::default()
.value(u64::from(*temperature))
.label(Line::from(format!("{hour:>02}:00")))
.text_value(format!("{temperature:>3}°"))
.style(style)
.value_style(style.reversed())
}
/// create a yellow to red value based on the value (50-90)
fntemperature_style(value: u8) -> Style {
letgreen= (255.0* (1.0- f64::from(value-50) /40.0)) as u8;
letcolor= Color::Rgb(255, green, 0);
Style::new().fg(color)
}
```