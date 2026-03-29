---
title: Gauge
url: https://ratatui.rs/examples/widgets/gauge/
source: crawler
fetched_at: 2026-02-01T21:12:52.851731219-03:00
rendered_js: false
word_count: 544
summary: This document demonstrates how to implement and customize different types of Gauge widgets in a Ratatui terminal application, including percentage-based, ratio-based, and unicode versions.
tags:
    - ratatui
    - rust
    - tui
    - gauge-widget
    - terminal-ui
    - user-interface
category: tutorial
---

```

gitclonehttps://github.com/ratatui/ratatui.git--branchlatest
cdratatui
cargorun--example=gauge--features=crossterm
```

```

//! # [Ratatui] Gauge example
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
use color_eyre::Result;
use ratatui::{
buffer::Buffer,
crossterm::event::{self, Event, KeyCode, KeyEventKind},
layout::{Alignment, Constraint, Layout, Rect},
style::{palette::tailwind, Color, Style, Stylize},
text::{Line, Span},
widgets::{Block, Borders, Gauge, Padding, Paragraph, Widget},
DefaultTerminal,
};
constGAUGE1_COLOR: Color = tailwind::RED.c800;
constGAUGE2_COLOR: Color = tailwind::GREEN.c800;
constGAUGE3_COLOR: Color = tailwind::BLUE.c800;
constGAUGE4_COLOR: Color = tailwind::ORANGE.c800;
constCUSTOM_LABEL_COLOR: Color = tailwind::SLATE.c200;
#[derive(Debug, Default, Clone, Copy)]
struct App {
state: AppState,
progress_columns: u16,
progress1: u16,
progress2: f64,
progress3: f64,
progress4: f64,
}
#[derive(Debug, Default, Clone, Copy, PartialEq, Eq)]
enum AppState {
#[default]
Running,
Started,
Quitting,
}
fnmain() -> Result<()> {
color_eyre::install()?;
letterminal= ratatui::init();
letapp_result= App::default().run(terminal);
ratatui::restore();
app_result
}
impl App {
fnrun(mutself, mutterminal: DefaultTerminal) -> Result<()> {
whileself.state != AppState::Quitting {
terminal.draw(|frame|frame.render_widget(&self, frame.area()))?;
self.handle_events()?;
self.update(terminal.size()?.width);
}
Ok(())
}
fnupdate(&mutself, terminal_width: u16) {
ifself.state != AppState::Started {
return;
}
// progress1 and progress2 help show the difference between ratio and percentage measuring
// the same thing, but converting to either a u16 or f64. Effectively, we're showing the
// difference between how a continuous gauge acts for floor and rounded values.
self.progress_columns = (self.progress_columns +1).clamp(0, terminal_width);
self.progress1 =self.progress_columns *100/terminal_width;
self.progress2 = f64::from(self.progress_columns) *100.0/ f64::from(terminal_width);
// progress3 and progress4 similarly show the difference between unicode and non-unicode
// gauges measuring the same thing.
self.progress3 = (self.progress3 +0.1).clamp(40.0, 100.0);
self.progress4 = (self.progress4 +0.1).clamp(40.0, 100.0);
}
fnhandle_events(&mutself) -> Result<()> {
lettimeout= Duration::from_secs_f32(1.0/20.0);
if event::poll(timeout)? {
iflet Event::Key(key) = event::read()? {
ifkey.kind == KeyEventKind::Press {
matchkey.code {
KeyCode::Char(' ') | KeyCode::Enter =>self.start(),
KeyCode::Char('q') | KeyCode::Esc =>self.quit(),
_=> {}
}
}
}
}
Ok(())
}
fnstart(&mutself) {
self.state = AppState::Started;
}
fnquit(&mutself) {
self.state = AppState::Quitting;
}
}
impl Widget for&App {
#[allow(clippy::similar_names)]
fnrender(self, area: Rect, buf:&mut Buffer) {
use Constraint::{Length, Min, Ratio};
letlayout= Layout::vertical([Length(2), Min(0), Length(1)]);
let [header_area, gauge_area, footer_area] =layout.areas(area);
letlayout= Layout::vertical([Ratio(1, 4); 4]);
let [gauge1_area, gauge2_area, gauge3_area, gauge4_area] =layout.areas(gauge_area);
render_header(header_area, buf);
render_footer(footer_area, buf);
self.render_gauge1(gauge1_area, buf);
self.render_gauge2(gauge2_area, buf);
self.render_gauge3(gauge3_area, buf);
self.render_gauge4(gauge4_area, buf);
}
}
fnrender_header(area: Rect, buf:&mut Buffer) {
Paragraph::new("Ratatui Gauge Example")
.bold()
.alignment(Alignment::Center)
.fg(CUSTOM_LABEL_COLOR)
.render(area, buf);
}
fnrender_footer(area: Rect, buf:&mut Buffer) {
Paragraph::new("Press ENTER to start")
.alignment(Alignment::Center)
.fg(CUSTOM_LABEL_COLOR)
.bold()
.render(area, buf);
}
impl App {
fnrender_gauge1(&self, area: Rect, buf:&mut Buffer) {
lettitle=title_block("Gauge with percentage");
Gauge::default()
.block(title)
.gauge_style(GAUGE1_COLOR)
.percent(self.progress1)
.render(area, buf);
}
fnrender_gauge2(&self, area: Rect, buf:&mut Buffer) {
lettitle=title_block("Gauge with ratio and custom label");
letlabel= Span::styled(
format!("{:.1}/100", self.progress2),
Style::new().italic().bold().fg(CUSTOM_LABEL_COLOR),
);
Gauge::default()
.block(title)
.gauge_style(GAUGE2_COLOR)
.ratio(self.progress2 /100.0)
.label(label)
.render(area, buf);
}
fnrender_gauge3(&self, area: Rect, buf:&mut Buffer) {
lettitle=title_block("Gauge with ratio (no unicode)");
letlabel=format!("{:.1}%", self.progress3);
Gauge::default()
.block(title)
.gauge_style(GAUGE3_COLOR)
.ratio(self.progress3 /100.0)
.label(label)
.render(area, buf);
}
fnrender_gauge4(&self, area: Rect, buf:&mut Buffer) {
lettitle=title_block("Gauge with ratio (unicode)");
letlabel=format!("{:.1}%", self.progress3);
Gauge::default()
.block(title)
.gauge_style(GAUGE4_COLOR)
.ratio(self.progress4 /100.0)
.label(label)
.use_unicode(true)
.render(area, buf);
}
}
fntitle_block(title:&str) -> Block {
lettitle= Line::from(title).centered();
Block::new()
.borders(Borders::NONE)
.padding(Padding::vertical(1))
.title(title)
.fg(CUSTOM_LABEL_COLOR)
}
```