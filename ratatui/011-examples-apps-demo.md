---
title: Demo
url: https://ratatui.rs/examples/apps/demo/
source: crawler
fetched_at: 2026-02-01T21:12:39.942276801-03:00
rendered_js: false
word_count: 1958
summary: This document provides the source code and setup instructions for the original Ratatui demo application across multiple terminal backends. It demonstrates how to structure a Rust terminal UI application using stateful widgets, data signals, and event handling.
tags:
    - ratatui
    - rust-tui
    - terminal-ui
    - crossterm
    - state-management
    - demo-example
category: tutorial
---

This is the original demo example from the main README. It is available for each of the backends.

```

gitclonehttps://github.com/ratatui/ratatui.git--branchlatest
cdratatui
cargorun--example=demo--features=crossterm
cargorun--example=demo--no-default-features--features=termion
cargorun--example=demo--no-default-features--features=termwiz
```

```

//! # [Ratatui] Original Demo example
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
use std::{error::Error, time::Duration};
use argh::FromArgs;
mod app;
#[cfg(feature ="crossterm")]
mod crossterm;
#[cfg(all(not(windows), feature ="termion"))]
mod termion;
#[cfg(feature ="termwiz")]
mod termwiz;
mod ui;
/// Demo
#[derive(Debug, FromArgs)]
struct Cli {
/// time in ms between two ticks.
#[argh(option, default ="250")]
tick_rate: u64,
/// whether unicode symbols are used to improve the overall look of the app
#[argh(option, default ="true")]
enhanced_graphics: bool,
}
fnmain() -> Result<(), Box<dyn Error>> {
letcli: Cli = argh::from_env();
lettick_rate= Duration::from_millis(cli.tick_rate);
#[cfg(feature ="crossterm")]
crate::crossterm::run(tick_rate, cli.enhanced_graphics)?;
#[cfg(all(not(windows), feature ="termion", not(feature ="crossterm")))]
crate::termion::run(tick_rate, cli.enhanced_graphics)?;
#[cfg(all(
feature ="termwiz",
not(feature ="crossterm"),
not(feature ="termion")
))]
crate::termwiz::run(tick_rate, cli.enhanced_graphics)?;
Ok(())
}
```

```

use rand::{
distr::{Distribution, Uniform},
rngs::ThreadRng,
};
use ratatui::widgets::ListState;
constTASKS: [&str; 24] = [
"Item1", "Item2", "Item3", "Item4", "Item5", "Item6", "Item7", "Item8", "Item9", "Item10",
"Item11", "Item12", "Item13", "Item14", "Item15", "Item16", "Item17", "Item18", "Item19",
"Item20", "Item21", "Item22", "Item23", "Item24",
];
constLOGS: [(&str, &str); 26] = [
("Event1", "INFO"),
("Event2", "INFO"),
("Event3", "CRITICAL"),
("Event4", "ERROR"),
("Event5", "INFO"),
("Event6", "INFO"),
("Event7", "WARNING"),
("Event8", "INFO"),
("Event9", "INFO"),
("Event10", "INFO"),
("Event11", "CRITICAL"),
("Event12", "INFO"),
("Event13", "INFO"),
("Event14", "INFO"),
("Event15", "INFO"),
("Event16", "INFO"),
("Event17", "ERROR"),
("Event18", "ERROR"),
("Event19", "INFO"),
("Event20", "INFO"),
("Event21", "WARNING"),
("Event22", "INFO"),
("Event23", "INFO"),
("Event24", "WARNING"),
("Event25", "INFO"),
("Event26", "INFO"),
];
constEVENTS: [(&str, u64); 24] = [
("B1", 9),
("B2", 12),
("B3", 5),
("B4", 8),
("B5", 2),
("B6", 4),
("B7", 5),
("B8", 9),
("B9", 14),
("B10", 15),
("B11", 1),
("B12", 0),
("B13", 4),
("B14", 6),
("B15", 4),
("B16", 6),
("B17", 4),
("B18", 7),
("B19", 13),
("B20", 8),
("B21", 11),
("B22", 9),
("B23", 3),
("B24", 5),
];
#[derive(Clone)]
pubstruct RandomSignal {
distribution: Uniform<u64>,
rng: ThreadRng,
}
impl RandomSignal {
pubfnnew(lower: u64, upper: u64) ->Self {
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
#[derive(Clone)]
pubstruct SinSignal {
x: f64,
interval: f64,
period: f64,
scale: f64,
}
impl SinSignal {
pubconstfnnew(interval: f64, period: f64, scale: f64) ->Self {
Self {
x:0.0,
interval,
period,
scale,
}
}
}
impl Iterator for SinSignal {
type Item = (f64, f64);
fnnext(&mutself) -> Option<Self::Item> {
letpoint= (self.x, (self.x *1.0/self.period).sin() *self.scale);
self.x +=self.interval;
Some(point)
}
}
pubstruct TabsState<'a> {
pubtitles: Vec<&'a str>,
pubindex: usize,
}
impl<'a> TabsState<'a> {
pubconstfnnew(titles: Vec<&'a str>) ->Self {
Self { titles, index:0 }
}
pubfnnext(&mutself) {
self.index = (self.index +1) %self.titles.len();
}
pubfnprevious(&mutself) {
ifself.index >0 {
self.index -=1;
} else {
self.index =self.titles.len() -1;
}
}
}
pubstruct StatefulList<T> {
pubstate: ListState,
pubitems: Vec<T>,
}
impl<T> StatefulList<T> {
pubfnwith_items(items: Vec<T>) ->Self {
Self {
state: ListState::default(),
items,
}
}
pubfnnext(&mutself) {
leti=matchself.state.selected() {
Some(i) => {
ifi>=self.items.len() -1 {
0
} else {
i+1
}
}
None =>0,
};
self.state.select(Some(i));
}
pubfnprevious(&mutself) {
leti=matchself.state.selected() {
Some(i) => {
ifi==0 {
self.items.len() -1
} else {
i-1
}
}
None =>0,
};
self.state.select(Some(i));
}
}
pubstruct Signal<S: Iterator> {
source: S,
pubpoints: Vec<S::Item>,
tick_rate: usize,
}
impl<S> Signal<S>
where
S: Iterator,
{
fnon_tick(&mutself) {
self.points.drain(0..self.tick_rate);
self.points
.extend(self.source.by_ref().take(self.tick_rate));
}
}
pubstruct Signals {
pubsin1: Signal<SinSignal>,
pubsin2: Signal<SinSignal>,
pubwindow: [f64; 2],
}
impl Signals {
fnon_tick(&mutself) {
self.sin1.on_tick();
self.sin2.on_tick();
self.window[0] +=1.0;
self.window[1] +=1.0;
}
}
pubstruct Server<'a> {
pubname:&'a str,
publocation:&'a str,
pubcoords: (f64, f64),
pubstatus:&'a str,
}
pubstruct App<'a> {
pubtitle:&'a str,
pubshould_quit: bool,
pubtabs: TabsState<'a>,
pubshow_chart: bool,
pubprogress: f64,
pubsparkline: Signal<RandomSignal>,
pubtasks: StatefulList<&'a str>,
publogs: StatefulList<(&'a str, &'a str)>,
pubsignals: Signals,
pubbarchart: Vec<(&'a str, u64)>,
pubservers: Vec<Server<'a>>,
pubenhanced_graphics: bool,
}
impl<'a> App<'a> {
pubfnnew(title:&'a str, enhanced_graphics: bool) ->Self {
letmutrand_signal= RandomSignal::new(0, 100);
letsparkline_points=rand_signal.by_ref().take(300).collect();
letmutsin_signal= SinSignal::new(0.2, 3.0, 18.0);
letsin1_points=sin_signal.by_ref().take(100).collect();
letmutsin_signal2= SinSignal::new(0.1, 2.0, 10.0);
letsin2_points=sin_signal2.by_ref().take(200).collect();
App {
title,
should_quit:false,
tabs: TabsState::new(vec!["Tab0", "Tab1", "Tab2"]),
show_chart:true,
progress:0.0,
sparkline: Signal {
source:rand_signal,
points:sparkline_points,
tick_rate:1,
},
tasks: StatefulList::with_items(TASKS.to_vec()),
logs: StatefulList::with_items(LOGS.to_vec()),
signals: Signals {
sin1: Signal {
source:sin_signal,
points:sin1_points,
tick_rate:5,
},
sin2: Signal {
source:sin_signal2,
points:sin2_points,
tick_rate:10,
},
window: [0.0, 20.0],
},
barchart:EVENTS.to_vec(),
servers:vec![
Server {
name:"NorthAmerica-1",
location:"New York City",
coords: (40.71, -74.00),
status:"Up",
},
Server {
name:"Europe-1",
location:"Paris",
coords: (48.85, 2.35),
status:"Failure",
},
Server {
name:"SouthAmerica-1",
location:"São Paulo",
coords: (-23.54, -46.62),
status:"Up",
},
Server {
name:"Asia-1",
location:"Singapore",
coords: (1.35, 103.86),
status:"Up",
},
],
enhanced_graphics,
}
}
pubfnon_up(&mutself) {
self.tasks.previous();
}
pubfnon_down(&mutself) {
self.tasks.next();
}
pubfnon_right(&mutself) {
self.tabs.next();
}
pubfnon_left(&mutself) {
self.tabs.previous();
}
pubfnon_key(&mutself, c: char) {
matchc {
'q'=> {
self.should_quit =true;
}
't'=> {
self.show_chart =!self.show_chart;
}
_=> {}
}
}
pubfnon_tick(&mutself) {
// Update progress
self.progress +=0.001;
ifself.progress >1.0 {
self.progress =0.0;
}
self.sparkline.on_tick();
self.signals.on_tick();
letlog=self.logs.items.pop().unwrap();
self.logs.items.insert(0, log);
letevent=self.barchart.pop().unwrap();
self.barchart.insert(0, event);
}
}
```

```

use ratatui::{
layout::{Constraint, Layout, Rect},
style::{Color, Modifier, Style},
symbols,
text::{self, Span},
widgets::{
canvas::{self, Canvas, Circle, Map, MapResolution, Rectangle},
Axis, BarChart, Block, Cell, Chart, Dataset, Gauge, LineGauge, List, ListItem, Paragraph,
Row, Sparkline, Table, Tabs, Wrap,
},
Frame,
};
usecrate::app::App;
pubfndraw(frame:&mut Frame, app:&mut App) {
letchunks= Layout::vertical([Constraint::Length(3), Constraint::Min(0)]).split(frame.area());
lettabs=app
.tabs
.titles
.iter()
.map(|t| text::Line::from(Span::styled(*t, Style::default().fg(Color::Green))))
.collect::<Tabs>()
.block(Block::bordered().title(app.title))
.highlight_style(Style::default().fg(Color::Yellow))
.select(app.tabs.index);
frame.render_widget(tabs, chunks[0]);
matchapp.tabs.index {
0=>draw_first_tab(frame, app, chunks[1]),
1=>draw_second_tab(frame, app, chunks[1]),
2=>draw_third_tab(frame, app, chunks[1]),
_=> {}
};
}
fndraw_first_tab(frame:&mut Frame, app:&mut App, area: Rect) {
letchunks= Layout::vertical([
Constraint::Length(9),
Constraint::Min(8),
Constraint::Length(7),
])
.split(area);
draw_gauges(frame, app, chunks[0]);
draw_charts(frame, app, chunks[1]);
draw_text(frame, chunks[2]);
}
fndraw_gauges(frame:&mut Frame, app:&mut App, area: Rect) {
letchunks= Layout::vertical([
Constraint::Length(2),
Constraint::Length(3),
Constraint::Length(2),
])
.margin(1)
.split(area);
letblock= Block::bordered().title("Graphs");
frame.render_widget(block, area);
letlabel=format!("{:.2}%", app.progress *100.0);
letgauge= Gauge::default()
.block(Block::new().title("Gauge:"))
.gauge_style(
Style::default()
.fg(Color::Magenta)
.bg(Color::Black)
.add_modifier(Modifier::ITALIC| Modifier::BOLD),
)
.use_unicode(app.enhanced_graphics)
.label(label)
.ratio(app.progress);
frame.render_widget(gauge, chunks[0]);
letsparkline= Sparkline::default()
.block(Block::new().title("Sparkline:"))
.style(Style::default().fg(Color::Green))
.data(&app.sparkline.points)
.bar_set(ifapp.enhanced_graphics {
symbols::bar::NINE_LEVELS
} else {
symbols::bar::THREE_LEVELS
});
frame.render_widget(sparkline, chunks[1]);
letline_gauge= LineGauge::default()
.block(Block::new().title("LineGauge:"))
.filled_style(Style::default().fg(Color::Magenta))
.line_set(ifapp.enhanced_graphics {
symbols::line::THICK
} else {
symbols::line::NORMAL
})
.ratio(app.progress);
frame.render_widget(line_gauge, chunks[2]);
}
#[allow(clippy::too_many_lines)]
fndraw_charts(frame:&mut Frame, app:&mut App, area: Rect) {
letconstraints=ifapp.show_chart {
vec![Constraint::Percentage(50), Constraint::Percentage(50)]
} else {
vec![Constraint::Percentage(100)]
};
letchunks= Layout::horizontal(constraints).split(area);
{
letchunks= Layout::vertical([Constraint::Percentage(50), Constraint::Percentage(50)])
.split(chunks[0]);
{
letchunks=
Layout::horizontal([Constraint::Percentage(50), Constraint::Percentage(50)])
.split(chunks[0]);
// Draw tasks
lettasks: Vec<ListItem> =app
.tasks
.items
.iter()
.map(|i| ListItem::new(vec![text::Line::from(Span::raw(*i))]))
.collect();
lettasks= List::new(tasks)
.block(Block::bordered().title("List"))
.highlight_style(Style::default().add_modifier(Modifier::BOLD))
.highlight_symbol("> ");
frame.render_stateful_widget(tasks, chunks[0], &mutapp.tasks.state);
// Draw logs
letinfo_style= Style::default().fg(Color::Blue);
letwarning_style= Style::default().fg(Color::Yellow);
leterror_style= Style::default().fg(Color::Magenta);
letcritical_style= Style::default().fg(Color::Red);
letlogs: Vec<ListItem> =app
.logs
.items
.iter()
.map(|&(evt, level)| {
lets=matchlevel {
"ERROR"=>error_style,
"CRITICAL"=>critical_style,
"WARNING"=>warning_style,
_=>info_style,
};
letcontent=vec![text::Line::from(vec![
Span::styled(format!("{level:<9}"), s),
Span::raw(evt),
])];
ListItem::new(content)
})
.collect();
letlogs= List::new(logs).block(Block::bordered().title("List"));
frame.render_stateful_widget(logs, chunks[1], &mutapp.logs.state);
}
letbarchart= BarChart::default()
.block(Block::bordered().title("Bar chart"))
.data(&app.barchart)
.bar_width(3)
.bar_gap(2)
.bar_set(ifapp.enhanced_graphics {
symbols::bar::NINE_LEVELS
} else {
symbols::bar::THREE_LEVELS
})
.value_style(
Style::default()
.fg(Color::Black)
.bg(Color::Green)
.add_modifier(Modifier::ITALIC),
)
.label_style(Style::default().fg(Color::Yellow))
.bar_style(Style::default().fg(Color::Green));
frame.render_widget(barchart, chunks[1]);
}
ifapp.show_chart {
letx_labels=vec![
Span::styled(
format!("{}", app.signals.window[0]),
Style::default().add_modifier(Modifier::BOLD),
),
Span::raw(format!(
"{}",
(app.signals.window[0] +app.signals.window[1]) /2.0
)),
Span::styled(
format!("{}", app.signals.window[1]),
Style::default().add_modifier(Modifier::BOLD),
),
];
letdatasets=vec![
Dataset::default()
.name("data2")
.marker(symbols::Marker::Dot)
.style(Style::default().fg(Color::Cyan))
.data(&app.signals.sin1.points),
Dataset::default()
.name("data3")
.marker(ifapp.enhanced_graphics {
symbols::Marker::Braille
} else {
symbols::Marker::Dot
})
.style(Style::default().fg(Color::Yellow))
.data(&app.signals.sin2.points),
];
letchart= Chart::new(datasets)
.block(
Block::bordered().title(Span::styled(
"Chart",
Style::default()
.fg(Color::Cyan)
.add_modifier(Modifier::BOLD),
)),
)
.x_axis(
Axis::default()
.title("X Axis")
.style(Style::default().fg(Color::Gray))
.bounds(app.signals.window)
.labels(x_labels),
)
.y_axis(
Axis::default()
.title("Y Axis")
.style(Style::default().fg(Color::Gray))
.bounds([-20.0, 20.0])
.labels([
Span::styled("-20", Style::default().add_modifier(Modifier::BOLD)),
Span::raw("0"),
Span::styled("20", Style::default().add_modifier(Modifier::BOLD)),
]),
);
frame.render_widget(chart, chunks[1]);
}
}
fndraw_text(frame:&mut Frame, area: Rect) {
lettext=vec![
text::Line::from("This is a paragraph with several lines. You can change style your text the way you want"),
text::Line::from(""),
text::Line::from(vec![
Span::from("For example: "),
Span::styled("under", Style::default().fg(Color::Red)),
Span::raw(""),
Span::styled("the", Style::default().fg(Color::Green)),
Span::raw(""),
Span::styled("rainbow", Style::default().fg(Color::Blue)),
Span::raw("."),
]),
text::Line::from(vec![
Span::raw("Oh and if you didn't "),
Span::styled("notice", Style::default().add_modifier(Modifier::ITALIC)),
Span::raw(" you can "),
Span::styled("automatically", Style::default().add_modifier(Modifier::BOLD)),
Span::raw(""),
Span::styled("wrap", Style::default().add_modifier(Modifier::REVERSED)),
Span::raw(" your "),
Span::styled("text", Style::default().add_modifier(Modifier::UNDERLINED)),
Span::raw(".")
]),
text::Line::from(
"One more thing is that it should display unicode characters: 10€"
),
];
letblock= Block::bordered().title(Span::styled(
"Footer",
Style::default()
.fg(Color::Magenta)
.add_modifier(Modifier::BOLD),
));
letparagraph= Paragraph::new(text).block(block).wrap(Wrap { trim:true });
frame.render_widget(paragraph, area);
}
fndraw_second_tab(frame:&mut Frame, app:&mut App, area: Rect) {
letchunks=
Layout::horizontal([Constraint::Percentage(30), Constraint::Percentage(70)]).split(area);
letup_style= Style::default().fg(Color::Green);
letfailure_style= Style::default()
.fg(Color::Red)
.add_modifier(Modifier::RAPID_BLINK| Modifier::CROSSED_OUT);
letrows=app.servers.iter().map(|s| {
letstyle=ifs.status =="Up" {
up_style
} else {
failure_style
};
Row::new(vec![s.name, s.location, s.status]).style(style)
});
lettable= Table::new(
rows,
[
Constraint::Length(15),
Constraint::Length(15),
Constraint::Length(10),
],
)
.header(
Row::new(vec!["Server", "Location", "Status"])
.style(Style::default().fg(Color::Yellow))
.bottom_margin(1),
)
.block(Block::bordered().title("Servers"));
frame.render_widget(table, chunks[0]);
letmap= Canvas::default()
.block(Block::bordered().title("World"))
.paint(|ctx| {
ctx.draw(&Map {
color: Color::White,
resolution: MapResolution::High,
});
ctx.layer();
ctx.draw(&Rectangle {
x:0.0,
y:30.0,
width:10.0,
height:10.0,
color: Color::Yellow,
});
ctx.draw(&Circle {
x:app.servers[2].coords.1,
y:app.servers[2].coords.0,
radius:10.0,
color: Color::Green,
});
for (i, s1) inapp.servers.iter().enumerate() {
fors2in&app.servers[i+1..] {
ctx.draw(&canvas::Line {
x1:s1.coords.1,
y1:s1.coords.0,
y2:s2.coords.0,
x2:s2.coords.1,
color: Color::Yellow,
});
}
}
forserverin&app.servers {
letcolor=ifserver.status =="Up" {
Color::Green
} else {
Color::Red
};
ctx.print(
server.coords.1,
server.coords.0,
Span::styled("X", Style::default().fg(color)),
);
}
})
.marker(ifapp.enhanced_graphics {
symbols::Marker::Braille
} else {
symbols::Marker::Dot
})
.x_bounds([-180.0, 180.0])
.y_bounds([-90.0, 90.0]);
frame.render_widget(map, chunks[1]);
}
fndraw_third_tab(frame:&mut Frame, _app:&mut App, area: Rect) {
letchunks= Layout::horizontal([Constraint::Ratio(1, 2), Constraint::Ratio(1, 2)]).split(area);
letcolors= [
Color::Reset,
Color::Black,
Color::Red,
Color::Green,
Color::Yellow,
Color::Blue,
Color::Magenta,
Color::Cyan,
Color::Gray,
Color::DarkGray,
Color::LightRed,
Color::LightGreen,
Color::LightYellow,
Color::LightBlue,
Color::LightMagenta,
Color::LightCyan,
Color::White,
];
letitems: Vec<Row> =colors
.iter()
.map(|c| {
letcells=vec![
Cell::from(Span::raw(format!("{c:?}: "))),
Cell::from(Span::styled("Foreground", Style::default().fg(*c))),
Cell::from(Span::styled("Background", Style::default().bg(*c))),
];
Row::new(cells)
})
.collect();
lettable= Table::new(
items,
[
Constraint::Ratio(1, 3),
Constraint::Ratio(1, 3),
Constraint::Ratio(1, 3),
],
)
.block(Block::bordered().title("Colors"));
frame.render_widget(table, chunks[0]);
}
```

```

use std::{
error::Error,
io,
time::{Duration, Instant},
};
use ratatui::{
backend::{Backend, CrosstermBackend},
crossterm::{
event::{self, DisableMouseCapture, EnableMouseCapture, Event, KeyCode, KeyEventKind},
execute,
terminal::{disable_raw_mode, enable_raw_mode, EnterAlternateScreen, LeaveAlternateScreen},
},
Terminal,
};
usecrate::{app::App, ui};
pubfnrun(tick_rate: Duration, enhanced_graphics: bool) -> Result<(), Box<dyn Error>> {
// setup terminal
enable_raw_mode()?;
letmutstdout= io::stdout();
execute!(stdout, EnterAlternateScreen, EnableMouseCapture)?;
letbackend= CrosstermBackend::new(stdout);
letmutterminal= Terminal::new(backend)?;
// create app and run it
letapp= App::new("Crossterm Demo", enhanced_graphics);
letapp_result=run_app(&mutterminal, app, tick_rate);
// restore terminal
disable_raw_mode()?;
execute!(
terminal.backend_mut(),
LeaveAlternateScreen,
DisableMouseCapture
)?;
terminal.show_cursor()?;
iflet Err(err) =app_result {
println!("{err:?}");
}
Ok(())
}
fnrun_app<B: Backend>(
terminal:&mut Terminal<B>,
mutapp: App,
tick_rate: Duration,
) -> io::Result<()> {
letmutlast_tick= Instant::now();
loop {
terminal.draw(|frame| ui::draw(frame, &mutapp))?;
lettimeout=tick_rate.saturating_sub(last_tick.elapsed());
if event::poll(timeout)? {
iflet Event::Key(key) = event::read()? {
ifkey.kind == KeyEventKind::Press {
matchkey.code {
KeyCode::Left | KeyCode::Char('h') =>app.on_left(),
KeyCode::Up | KeyCode::Char('k') =>app.on_up(),
KeyCode::Right | KeyCode::Char('l') =>app.on_right(),
KeyCode::Down | KeyCode::Char('j') =>app.on_down(),
KeyCode::Char(c) =>app.on_key(c),
_=> {}
}
}
}
}
iflast_tick.elapsed() >=tick_rate {
app.on_tick();
last_tick= Instant::now();
}
ifapp.should_quit {
return Ok(());
}
}
}
```

```

#![allow(dead_code)]
use std::{error::Error, io, sync::mpsc, thread, time::Duration};
use ratatui::{
backend::{Backend, TermionBackend},
termion::{
event::Key,
input::{MouseTerminal, TermRead},
raw::IntoRawMode,
screen::IntoAlternateScreen,
},
Terminal,
};
usecrate::{app::App, ui};
pubfnrun(tick_rate: Duration, enhanced_graphics: bool) -> Result<(), Box<dyn Error>> {
// setup terminal
letstdout= io::stdout()
.into_raw_mode()
.unwrap()
.into_alternate_screen()
.unwrap();
letstdout= MouseTerminal::from(stdout);
letbackend= TermionBackend::new(stdout);
letmutterminal= Terminal::new(backend)?;
// create app and run it
letapp= App::new("Termion demo", enhanced_graphics);
run_app(&mutterminal, app, tick_rate)?;
Ok(())
}
fnrun_app<B: Backend>(
terminal:&mut Terminal<B>,
mutapp: App,
tick_rate: Duration,
) -> Result<(), Box<dyn Error>> {
letevents=events(tick_rate);
loop {
terminal.draw(|frame| ui::draw(frame, &mutapp))?;
matchevents.recv()? {
Event::Input(key) =>matchkey {
Key::Up | Key::Char('k') =>app.on_up(),
Key::Down | Key::Char('j') =>app.on_down(),
Key::Left | Key::Char('h') =>app.on_left(),
Key::Right | Key::Char('l') =>app.on_right(),
Key::Char(c) =>app.on_key(c),
_=> {}
},
Event::Tick =>app.on_tick(),
}
ifapp.should_quit {
return Ok(());
}
}
}
enum Event {
Input(Key),
Tick,
}
fnevents(tick_rate: Duration) -> mpsc::Receiver<Event> {
let (tx, rx) = mpsc::channel();
letkeys_tx=tx.clone();
thread::spawn(move|| {
letstdin= io::stdin();
forkeyinstdin.keys().flatten() {
iflet Err(err) =keys_tx.send(Event::Input(key)) {
eprintln!("{err}");
return;
}
}
});
thread::spawn(move||loop {
iflet Err(err) =tx.send(Event::Tick) {
eprintln!("{err}");
break;
}
thread::sleep(tick_rate);
});
rx
}
```

```

#![allow(dead_code)]
use std::{
error::Error,
time::{Duration, Instant},
};
use ratatui::{
backend::TermwizBackend,
termwiz::{
input::{InputEvent, KeyCode},
terminal::Terminal as TermwizTerminal,
},
Terminal,
};
usecrate::{app::App, ui};
pubfnrun(tick_rate: Duration, enhanced_graphics: bool) -> Result<(), Box<dyn Error>> {
letbackend= TermwizBackend::new()?;
letmutterminal= Terminal::new(backend)?;
terminal.hide_cursor()?;
// create app and run it
letapp= App::new("Termwiz Demo", enhanced_graphics);
letapp_result=run_app(&mutterminal, app, tick_rate);
terminal.show_cursor()?;
terminal.flush()?;
iflet Err(err) =app_result {
println!("{err:?}");
}
Ok(())
}
fnrun_app(
terminal:&mut Terminal<TermwizBackend>,
mutapp: App,
tick_rate: Duration,
) -> Result<(), Box<dyn Error>> {
letmutlast_tick= Instant::now();
loop {
terminal.draw(|frame| ui::draw(frame, &mutapp))?;
lettimeout=tick_rate.saturating_sub(last_tick.elapsed());
iflet Some(input) =terminal
.backend_mut()
.buffered_terminal_mut()
.terminal()
.poll_input(Some(timeout))?
{
matchinput {
InputEvent::Key(key_code) =>matchkey_code.key {
KeyCode::UpArrow | KeyCode::Char('k') =>app.on_up(),
KeyCode::DownArrow | KeyCode::Char('j') =>app.on_down(),
KeyCode::LeftArrow | KeyCode::Char('h') =>app.on_left(),
KeyCode::RightArrow | KeyCode::Char('l') =>app.on_right(),
KeyCode::Char(c) =>app.on_key(c),
_=> {}
},
InputEvent::Resized { cols, rows } => {
terminal
.backend_mut()
.buffered_terminal_mut()
.resize(cols, rows);
}
_=> {}
}
}
iflast_tick.elapsed() >=tick_rate {
app.on_tick();
last_tick= Instant::now();
}
ifapp.should_quit {
return Ok(());
}
}
}
```