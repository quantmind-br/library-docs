---
title: Sparkline
url: https://ratatui.rs/examples/widgets/sparkline/
source: crawler
fetched_at: 2026-02-01T21:12:56.279480433-03:00
rendered_js: false
word_count: 330
summary: This document demonstrates how to implement and style the Sparkline widget in Ratatui to visualize data trends within a terminal user interface.
tags:
    - ratatui
    - sparkline
    - widget
    - rust
    - data-visualization
    - tui
    - terminal-graphics
category: tutorial
---

Demonstrates the [`Sparkline`](https://docs.rs/ratatui/latest/ratatui/widgets/struct.Sparkline.html) widget.

```

gitclonehttps://github.com/ratatui/ratatui.git--branchlatest
cdratatui
cargorun--example=sparkline--features=crossterm
```

![sparkline](https://ratatui.rs/_astro/sparkline.CAk-51Nq_Z1440a1.webp)

```

//! # [Ratatui] Sparkline example
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
use std::time::{Duration, Instant};
use color_eyre::Result;
use rand::{
distr::{Distribution, Uniform},
rngs::ThreadRng,
};
use ratatui::{
crossterm::event::{self, Event, KeyCode},
layout::{Constraint, Layout},
style::{Color, Style},
widgets::{Block, Borders, Sparkline},
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
signal: RandomSignal,
data1: Vec<u64>,
data2: Vec<u64>,
data3: Vec<u64>,
}
#[derive(Clone)]
struct RandomSignal {
distribution: Uniform<u64>,
rng: ThreadRng,
}
impl RandomSignal {
fnnew(lower: u64, upper: u64) ->Self {
Self {
distribution: Uniform::new(lower, upper).unwrap(),
rng: rand::rng(),
}
}
}
impl Iterator for RandomSignal {
type Item = u64;
fnnext(&mutself) -> Option<u64> {
Some(self.distribution.sample(&mutself.rng))
}
}
impl App {
fnnew() ->Self {
letmutsignal= RandomSignal::new(0, 100);
letdata1=signal.by_ref().take(200).collect::<Vec<u64>>();
letdata2=signal.by_ref().take(200).collect::<Vec<u64>>();
letdata3=signal.by_ref().take(200).collect::<Vec<u64>>();
Self {
signal,
data1,
data2,
data3,
}
}
fnon_tick(&mutself) {
letvalue=self.signal.next().unwrap();
self.data1.pop();
self.data1.insert(0, value);
letvalue=self.signal.next().unwrap();
self.data2.pop();
self.data2.insert(0, value);
letvalue=self.signal.next().unwrap();
self.data3.pop();
self.data3.insert(0, value);
}
fnrun(mutself, mutterminal: DefaultTerminal) -> Result<()> {
lettick_rate= Duration::from_millis(250);
letmutlast_tick= Instant::now();
loop {
terminal.draw(|frame|self.draw(frame))?;
lettimeout=tick_rate.saturating_sub(last_tick.elapsed());
if event::poll(timeout)? {
iflet Event::Key(key) = event::read()? {
ifkey.code == KeyCode::Char('q') {
return Ok(());
}
}
}
iflast_tick.elapsed() >=tick_rate {
self.on_tick();
last_tick= Instant::now();
}
}
}
fndraw(&self, frame:&mut Frame) {
letchunks= Layout::vertical([
Constraint::Length(3),
Constraint::Length(3),
Constraint::Min(0),
])
.split(frame.area());
letsparkline= Sparkline::default()
.block(
Block::new()
.borders(Borders::LEFT| Borders::RIGHT)
.title("Data1"),
)
.data(&self.data1)
.style(Style::default().fg(Color::Yellow));
frame.render_widget(sparkline, chunks[0]);
letsparkline= Sparkline::default()
.block(
Block::new()
.borders(Borders::LEFT| Borders::RIGHT)
.title("Data2"),
)
.data(&self.data2)
.style(Style::default().bg(Color::Green));
frame.render_widget(sparkline, chunks[1]);
// Multiline
letsparkline= Sparkline::default()
.block(
Block::new()
.borders(Borders::LEFT| Borders::RIGHT)
.title("Data3"),
)
.data(&self.data3)
.style(Style::default().fg(Color::Red));
frame.render_widget(sparkline, chunks[2]);
}
}
```