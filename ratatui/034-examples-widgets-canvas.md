---
title: Canvas
url: https://ratatui.rs/examples/widgets/canvas/
source: crawler
fetched_at: 2026-02-01T21:12:51.841014837-03:00
rendered_js: false
word_count: 593
summary: This document demonstrates how to use the Ratatui Canvas widget to draw shapes, maps, and interactive graphics within a terminal UI. It covers coordinate-based rendering, marker styles, and handling mouse input for dynamic drawing.
tags:
    - ratatui
    - rust-tui
    - canvas-widget
    - terminal-graphics
    - event-handling
    - user-interface
category: tutorial
---

```

gitclonehttps://github.com/ratatui/ratatui.git--branchlatest
cdratatui
cargorun--example=canvas--features=crossterm
```

```

//! # [Ratatui] Canvas example
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
use std::{
io::stdout,
time::{Duration, Instant},
};
use color_eyre::Result;
use crossterm::{
event::{DisableMouseCapture, EnableMouseCapture, KeyEventKind},
ExecutableCommand,
};
use itertools::Itertools;
use ratatui::{
crossterm::event::{self, Event, KeyCode, MouseEventKind},
layout::{Constraint, Layout, Position, Rect},
style::{Color, Stylize},
symbols::Marker,
widgets::{
canvas::{Canvas, Circle, Map, MapResolution, Points, Rectangle},
Block, Widget,
},
DefaultTerminal, Frame,
};
fnmain() -> Result<()> {
color_eyre::install()?;
stdout().execute(EnableMouseCapture)?;
letterminal= ratatui::init();
letapp_result= App::new().run(terminal);
ratatui::restore();
stdout().execute(DisableMouseCapture)?;
app_result
}
struct App {
exit: bool,
x: f64,
y: f64,
ball: Circle,
playground: Rect,
vx: f64,
vy: f64,
tick_count: u64,
marker: Marker,
points: Vec<Position>,
is_drawing: bool,
}
impl App {
constfnnew() ->Self {
Self {
exit:false,
x:0.0,
y:0.0,
ball: Circle {
x:20.0,
y:40.0,
radius:10.0,
color: Color::Yellow,
},
playground: Rect::new(10, 10, 200, 100),
vx:1.0,
vy:1.0,
tick_count:0,
marker: Marker::Dot,
points:vec![],
is_drawing:false,
}
}
pubfnrun(mutself, mutterminal: DefaultTerminal) -> Result<()> {
lettick_rate= Duration::from_millis(16);
letmutlast_tick= Instant::now();
while!self.exit {
terminal.draw(|frame|self.draw(frame))?;
lettimeout=tick_rate.saturating_sub(last_tick.elapsed());
if event::poll(timeout)? {
match event::read()? {
Event::Key(key) =>self.handle_key_press(key),
Event::Mouse(event) =>self.handle_mouse_event(event),
_=> (),
}
}
iflast_tick.elapsed() >=tick_rate {
self.on_tick();
last_tick= Instant::now();
}
}
Ok(())
}
fnhandle_key_press(&mutself, key: event::KeyEvent) {
ifkey.kind != KeyEventKind::Press {
return;
}
matchkey.code {
KeyCode::Char('q') =>self.exit =true,
KeyCode::Down | KeyCode::Char('j') =>self.y +=1.0,
KeyCode::Up | KeyCode::Char('k') =>self.y -=1.0,
KeyCode::Right | KeyCode::Char('l') =>self.x +=1.0,
KeyCode::Left | KeyCode::Char('h') =>self.x -=1.0,
_=> {}
}
}
fnhandle_mouse_event(&mutself, event: event::MouseEvent) {
matchevent.kind {
MouseEventKind::Down(_) =>self.is_drawing =true,
MouseEventKind::Up(_) =>self.is_drawing =false,
MouseEventKind::Drag(_) => {
self.points.push(Position::new(event.column, event.row));
}
_=> {}
}
}
fnon_tick(&mutself) {
self.tick_count +=1;
// only change marker every 180 ticks (3s) to avoid stroboscopic effect
if (self.tick_count %180) ==0 {
self.marker =matchself.marker {
Marker::Dot => Marker::Braille,
Marker::Braille => Marker::Block,
Marker::Block => Marker::HalfBlock,
Marker::HalfBlock => Marker::Bar,
Marker::Bar => Marker::Dot,
};
}
// bounce the ball by flipping the velocity vector
letball=&self.ball;
letplayground=self.playground;
ifball.x -ball.radius < f64::from(playground.left())
||ball.x +ball.radius > f64::from(playground.right())
{
self.vx =-self.vx;
}
ifball.y -ball.radius < f64::from(playground.top())
||ball.y +ball.radius > f64::from(playground.bottom())
{
self.vy =-self.vy;
}
self.ball.x +=self.vx;
self.ball.y +=self.vy;
}
fndraw(&self, frame:&mut Frame) {
lethorizontal=
Layout::horizontal([Constraint::Percentage(50), Constraint::Percentage(50)]);
letvertical= Layout::vertical([Constraint::Percentage(50), Constraint::Percentage(50)]);
let [left, right] =horizontal.areas(frame.area());
let [draw, map] =vertical.areas(left);
let [pong, boxes] =vertical.areas(right);
frame.render_widget(self.map_canvas(), map);
frame.render_widget(self.draw_canvas(draw), draw);
frame.render_widget(self.pong_canvas(), pong);
frame.render_widget(self.boxes_canvas(boxes), boxes);
}
fnmap_canvas(&self) ->impl Widget + '_ {
Canvas::default()
.block(Block::bordered().title("World"))
.marker(self.marker)
.paint(|ctx| {
ctx.draw(&Map {
color: Color::Green,
resolution: MapResolution::High,
});
ctx.print(self.x, -self.y, "You are here".yellow());
})
.x_bounds([-180.0, 180.0])
.y_bounds([-90.0, 90.0])
}
fndraw_canvas(&self, area: Rect) ->impl Widget + '_ {
Canvas::default()
.block(Block::bordered().title("Draw here"))
.marker(self.marker)
.x_bounds([0.0, f64::from(area.width)])
.y_bounds([0.0, f64::from(area.height)])
.paint(move|ctx| {
letpoints=self
.points
.iter()
.map(|p| {
(
f64::from(p.x) - f64::from(area.left()),
f64::from(area.bottom()) - f64::from(p.y),
)
})
.collect_vec();
ctx.draw(&Points {
coords:&points,
color: Color::White,
});
})
}
fnpong_canvas(&self) ->impl Widget + '_ {
Canvas::default()
.block(Block::bordered().title("Pong"))
.marker(self.marker)
.paint(|ctx| {
ctx.draw(&self.ball);
})
.x_bounds([10.0, 210.0])
.y_bounds([10.0, 110.0])
}
fnboxes_canvas(&self, area: Rect) ->impl Widget {
letleft=0.0;
letright= f64::from(area.width);
letbottom=0.0;
lettop= f64::from(area.height).mul_add(2.0, -4.0);
Canvas::default()
.block(Block::bordered().title("Rects"))
.marker(self.marker)
.x_bounds([left, right])
.y_bounds([bottom, top])
.paint(|ctx| {
foriin0..=11 {
ctx.draw(&Rectangle {
x: f64::from(i*i+3*i) /2.0+2.0,
y:2.0,
width: f64::from(i),
height: f64::from(i),
color: Color::Red,
});
ctx.draw(&Rectangle {
x: f64::from(i*i+3*i) /2.0+2.0,
y:21.0,
width: f64::from(i),
height: f64::from(i),
color: Color::Blue,
});
}
foriin0..100 {
ifi%10!=0 {
ctx.print(f64::from(i) +1.0, 0.0, format!("{i}", i=i%10));
}
ifi%2==0&&i%10!=0 {
ctx.print(0.0, f64::from(i), format!("{i}", i=i%10));
}
}
})
}
}
```