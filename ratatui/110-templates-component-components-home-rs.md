---
title: Components/home.rs
url: https://ratatui.rs/templates/component/components-home-rs/
source: crawler
fetched_at: 2026-02-01T21:13:31.85291325-03:00
rendered_js: false
word_count: 0
summary: This document provides a Rust implementation of a terminal user interface component using the Ratatui library, covering state management, keyboard event handling, and asynchronous action processing.
tags:
    - rust
    - ratatui
    - terminal-ui
    - async-programming
    - event-handling
    - tokio
    - ui-component
category: reference
---

```

use std::{collections::HashMap, time::Duration};
use color_eyre::eyre::Result;
use log::error;
use ratatui::{
crossterm::event::{KeyCode, KeyEvent},
layout::{Alignment, Constraint, Layout, Margin, Position, Rect},
style::{Color, Modifier, Style, Stylize},
text::{Line, Span},
widgets::{Block, BorderType, Borders, Clear, Paragraph, Row, Table},
Frame,
};
use tokio::sync::mpsc::UnboundedSender;
use tracing::trace;
use tui_input::{backend::crossterm::EventHandler, Input};
usesuper::Component;
usecrate::{action::Action, config::key_event_to_string};
#[derive(Default, Copy, Clone, PartialEq, Eq)]
pubenum Mode {
#[default]
Normal,
Insert,
Processing,
}
#[derive(Default)]
pubstruct Home {
pubshow_help: bool,
pubcounter: usize,
pubapp_ticker: usize,
pubrender_ticker: usize,
pubmode: Mode,
pubinput: Input,
pubaction_tx: Option<UnboundedSender<Action>>,
pubkeymap: HashMap<KeyEvent, Action>,
pubtext: Vec<String>,
publast_events: Vec<KeyEvent>,
}
impl Home {
pubfnnew() ->Self {
Self::default()
}
pubfnkeymap(mutself, keymap: HashMap<KeyEvent, Action>) ->Self {
self.keymap =keymap;
self
}
pubfntick(&mutself) {
log::info!("Tick");
self.app_ticker =self.app_ticker.saturating_add(1);
self.last_events.drain(..);
}
pubfnrender_tick(&mutself) {
log::debug!("Render Tick");
self.render_ticker =self.render_ticker.saturating_add(1);
}
pubfnadd(&mutself, s: String) {
self.text.push(s)
}
pubfnschedule_increment(&mutself, i: usize) {
lettx=self.action_tx.clone().unwrap();
tokio::spawn(asyncmove {
tx.send(Action::EnterProcessing).unwrap();
tokio::time::sleep(Duration::from_secs(1)).await;
tx.send(Action::Increment(i)).unwrap();
tx.send(Action::ExitProcessing).unwrap();
});
}
pubfnschedule_decrement(&mutself, i: usize) {
lettx=self.action_tx.clone().unwrap();
tokio::spawn(asyncmove {
tx.send(Action::EnterProcessing).unwrap();
tokio::time::sleep(Duration::from_secs(1)).await;
tx.send(Action::Decrement(i)).unwrap();
tx.send(Action::ExitProcessing).unwrap();
});
}
pubfnincrement(&mutself, i: usize) {
self.counter =self.counter.saturating_add(i);
}
pubfndecrement(&mutself, i: usize) {
self.counter =self.counter.saturating_sub(i);
}
}
impl Component for Home {
fnregister_action_handler(&mutself, tx: UnboundedSender<Action>) -> Result<()> {
self.action_tx = Some(tx);
Ok(())
}
fnhandle_key_events(&mutself, key: KeyEvent) -> Result<Option<Action>> {
self.last_events.push(key);
letaction=matchself.mode {
Mode::Normal | Mode::Processing =>return Ok(None),
Mode::Insert =>matchkey.code {
KeyCode::Esc => Action::EnterNormal,
KeyCode::Enter => {
iflet Some(sender) =&self.action_tx {
iflet Err(e) =sender.send(Action::CompleteInput(self.input.value().to_string())) {
error!("Failed to send action: {:?}", e);
}
}
Action::EnterNormal
},
_=> {
self.input.handle_event(&ratatui::crossterm::event::Event::Key(key));
Action::Update
},
},
};
Ok(Some(action))
}
fnupdate(&mutself, action: Action) -> Result<Option<Action>> {
matchaction {
Action::Tick =>self.tick(),
Action::Render =>self.render_tick(),
Action::ToggleShowHelp =>self.show_help =!self.show_help,
Action::ScheduleIncrement =>self.schedule_increment(1),
Action::ScheduleDecrement =>self.schedule_decrement(1),
Action::Increment(i) =>self.increment(i),
Action::Decrement(i) =>self.decrement(i),
Action::CompleteInput(s) =>self.add(s),
Action::EnterNormal => {
self.mode = Mode::Normal;
},
Action::EnterInsert => {
self.mode = Mode::Insert;
},
Action::EnterProcessing => {
self.mode = Mode::Processing;
},
Action::ExitProcessing => {
// TODO: Make this go to previous mode instead
self.mode = Mode::Normal;
},
_=> (),
}
Ok(None)
}
fndraw(&mutself, f:&mut Frame<'_>, rect: Rect) -> Result<()> {
letrects= Layout::default().constraints([Constraint::Percentage(100), Constraint::Min(3)].as_ref()).split(rect);
letmuttext: Vec<Line> =self.text.clone().iter().map(|l| Line::from(l.clone())).collect();
text.insert(0, "".into());
text.insert(0, "Type into input and hit enter to display here".dim().into());
text.insert(0, "".into());
text.insert(0, format!("Render Ticker: {}", self.render_ticker).into());
text.insert(0, format!("App Ticker: {}", self.app_ticker).into());
text.insert(0, format!("Counter: {}", self.counter).into());
text.insert(0, "".into());
text.insert(
0,
Line::from(vec![
"Press ".into(),
Span::styled("j", Style::default().fg(Color::Red)),
" or ".into(),
Span::styled("k", Style::default().fg(Color::Red)),
" to ".into(),
Span::styled("increment", Style::default().fg(Color::Yellow)),
" or ".into(),
Span::styled("decrement", Style::default().fg(Color::Yellow)),
".".into(),
]),
);
text.insert(0, "".into());
f.render_widget(
Paragraph::new(text)
.block(
Block::default()
.title("ratatui async template")
.title_alignment(Alignment::Center)
.borders(Borders::ALL)
.border_style(matchself.mode {
Mode::Processing => Style::default().fg(Color::Yellow),
_=> Style::default(),
})
.border_type(BorderType::Rounded),
)
.style(Style::default().fg(Color::Cyan))
.alignment(Alignment::Center),
rects[0],
);
letwidth=rects[1].width.max(3) -3; // keep 2 for borders and 1 for cursor
letscroll=self.input.visual_scroll(widthas usize);
letinput= Paragraph::new(self.input.value())
.style(matchself.mode {
Mode::Insert => Style::default().fg(Color::Yellow),
_=> Style::default(),
})
.scroll((0, scrollas u16))
.block(Block::default().borders(Borders::ALL).title(Line::from(vec![
Span::raw("Enter Input Mode "),
Span::styled("(Press ", Style::default().fg(Color::DarkGray)),
Span::styled("/", Style::default().add_modifier(Modifier::BOLD).fg(Color::Gray)),
Span::styled(" to start, ", Style::default().fg(Color::DarkGray)),
Span::styled("ESC", Style::default().add_modifier(Modifier::BOLD).fg(Color::Gray)),
Span::styled(" to finish)", Style::default().fg(Color::DarkGray)),
])));
f.render_widget(input, rects[1]);
ifself.mode == Mode::Insert {
letposition= Position {
x: (rects[1].x +1+self.input.cursor() as u16).min(rects[1].x +rects[1].width -2),
y:rects[1].y +1,
};
f.set_cursor_position(position)
}
ifself.show_help {
letrect=rect.inner(Margin { horizontal:4, vertical:2 });
f.render_widget(Clear, rect);
letblock= Block::default()
.title(Line::from(vec![Span::styled("Key Bindings", Style::default().add_modifier(Modifier::BOLD))]))
.borders(Borders::ALL)
.border_style(Style::default().fg(Color::Yellow));
f.render_widget(block, rect);
letrows=vec![
Row::new(vec!["j", "Increment"]),
Row::new(vec!["k", "Decrement"]),
Row::new(vec!["/", "Enter Input"]),
Row::new(vec!["ESC", "Exit Input"]),
Row::new(vec!["Enter", "Submit Input"]),
Row::new(vec!["q", "Quit"]),
Row::new(vec!["?", "Open Help"]),
];
lettable= Table::new(rows, [Constraint::Percentage(10), Constraint::Percentage(90)])
.header(Row::new(vec!["Key", "Action"]).bottom_margin(1).style(Style::default().add_modifier(Modifier::BOLD)))
.column_spacing(1);
f.render_widget(table, rect.inner(Margin { vertical:4, horizontal:2 }));
};
f.render_widget(
Block::default()
.title(
Line::from(format!(
"{:?}",
&self.last_events.iter().map(key_event_to_string).collect::<Vec<_>>()
))
.alignment(Alignment::Right),
)
.title_style(Style::default().add_modifier(Modifier::BOLD)),
Rect { x:rect.x +1, y:rect.height.saturating_sub(1), width:rect.width.saturating_sub(2), height:1 },
);
Ok(())
}
}
```