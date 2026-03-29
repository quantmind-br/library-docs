---
title: Closing Thoughts
url: https://ratatui.rs/tutorials/json-editor/closing-thoughts/
source: crawler
fetched_at: 2026-02-01T21:12:37.8011623-03:00
rendered_js: false
word_count: 702
summary: This tutorial explains the fundamental architecture and flow of a Ratatui application by demonstrating how to build an interactive JSON editor with state management and event handling.
tags:
    - ratatui
    - rust-tui
    - terminal-ui
    - crossterm
    - event-handling
    - state-management
    - ui-layout
category: tutorial
---

This tutorial should get you started with a basic understanding of the flow of a `ratatui` program. However, this is only *one* way to create a `ratatui` application. Because `ratatui` is relatively low level compared to other UI frameworks, almost any application model can be implemented. You can explore more of these in [Concepts: Application Patterns](https://ratatui.rs/concepts/application-patterns/the-elm-architecture/) and get some inspiration for what model will work best for your application.

You can find the finished project used for the tutorial on [GitHub](https://github.com/ratatui/ratatui-website/tree/main/code/tutorials/json-editor). The code is also shown at the bottom of this page.

You can test this application by yourself by running:

and double checking the output.

```

use std::{error::Error, io};
use ratatui::{
backend::{Backend, CrosstermBackend},
crossterm::{
event::{self, DisableMouseCapture, EnableMouseCapture, Event, KeyCode, KeyEventKind},
execute,
terminal::{disable_raw_mode, enable_raw_mode, EnterAlternateScreen, LeaveAlternateScreen},
},
Terminal,
};
mod app;
mod ui;
usecrate::{
app::{App, CurrentScreen, CurrentlyEditing},
ui::ui,
};
fnmain() -> Result<(), Box<dyn Error>> {
// setup terminal
enable_raw_mode()?;
letmutstderr= io::stderr(); // This is a special case. Normally using stdout is fine
execute!(stderr, EnterAlternateScreen, EnableMouseCapture)?;
letbackend= CrosstermBackend::new(stderr);
letmutterminal= Terminal::new(backend)?;
// create app and run it
letmutapp= App::new();
letres=run_app(&mutterminal, &mutapp);
// restore terminal
disable_raw_mode()?;
execute!(
terminal.backend_mut(),
LeaveAlternateScreen,
DisableMouseCapture
)?;
terminal.show_cursor()?;
iflet Ok(do_print) =res {
ifdo_print {
app.print_json()?;
}
} elseiflet Err(err) =res {
println!("{err:?}");
}
Ok(())
}
fnrun_app<B: Backend>(terminal:&mut Terminal<B>, app:&mut App) -> io::Result<bool> {
loop {
terminal.draw(|f|ui(f, app))?;
iflet Event::Key(key) = event::read()? {
ifkey.kind == event::KeyEventKind::Release {
// Skip events that are not KeyEventKind::Press
continue;
}
matchapp.current_screen {
CurrentScreen::Main =>matchkey.code {
KeyCode::Char('e') => {
app.current_screen = CurrentScreen::Editing;
app.currently_editing = Some(CurrentlyEditing::Key);
}
KeyCode::Char('q') => {
app.current_screen = CurrentScreen::Exiting;
}
_=> {}
},
CurrentScreen::Exiting =>matchkey.code {
KeyCode::Char('y') => {
return Ok(true);
}
KeyCode::Char('n') | KeyCode::Char('q') => {
return Ok(false);
}
_=> {}
},
CurrentScreen::Editing ifkey.kind == KeyEventKind::Press => {
matchkey.code {
KeyCode::Enter => {
iflet Some(editing) =&app.currently_editing {
matchediting {
CurrentlyEditing::Key => {
app.currently_editing = Some(CurrentlyEditing::Value);
}
CurrentlyEditing::Value => {
app.save_key_value();
app.current_screen = CurrentScreen::Main;
}
}
}
}
KeyCode::Backspace => {
iflet Some(editing) =&app.currently_editing {
matchediting {
CurrentlyEditing::Key => {
app.key_input.pop();
}
CurrentlyEditing::Value => {
app.value_input.pop();
}
}
}
}
KeyCode::Esc => {
app.current_screen = CurrentScreen::Main;
app.currently_editing = None;
}
KeyCode::Tab => {
app.toggle_editing();
}
KeyCode::Char(value) => {
iflet Some(editing) =&app.currently_editing {
matchediting {
CurrentlyEditing::Key => {
app.key_input.push(value);
}
CurrentlyEditing::Value => {
app.value_input.push(value);
}
}
}
}
_=> {}
}
}
_=> {}
}
}
}
}
```

```

use std::collections::HashMap;
pubenum CurrentScreen {
Main,
Editing,
Exiting,
}
pubenum CurrentlyEditing {
Key,
Value,
}
pubstruct App {
pubkey_input: String,              // the currently being edited json key.
pubvalue_input: String,            // the currently being edited json value.
pubpairs: HashMap<String, String>, // The representation of our key and value pairs with serde Serialize support
pubcurrent_screen: CurrentScreen, // the current screen the user is looking at, and will later determine what is rendered.
pubcurrently_editing: Option<CurrentlyEditing>, // the optional state containing which of the key or value pair the user is editing. It is an option, because when the user is not directly editing a key-value pair, this will be set to `None`.
}
impl App {
pubfnnew() -> App {
App {
key_input: String::new(),
value_input: String::new(),
pairs: HashMap::new(),
current_screen: CurrentScreen::Main,
currently_editing: None,
}
}
pubfnsave_key_value(&mutself) {
self.pairs
.insert(self.key_input.clone(), self.value_input.clone());
self.key_input = String::new();
self.value_input = String::new();
self.currently_editing = None;
}
pubfntoggle_editing(&mutself) {
iflet Some(edit_mode) =&self.currently_editing {
matchedit_mode {
CurrentlyEditing::Key =>self.currently_editing = Some(CurrentlyEditing::Value),
CurrentlyEditing::Value =>self.currently_editing = Some(CurrentlyEditing::Key),
};
} else {
self.currently_editing = Some(CurrentlyEditing::Key);
}
}
pubfnprint_json(&self) -> serde_json::Result<()> {
letoutput= serde_json::to_string(&self.pairs)?;
println!("{output}");
Ok(())
}
}
```

```

use ratatui::{
layout::{Constraint, Direction, Layout, Rect},
style::{Color, Style},
text::{Line, Span, Text},
widgets::{Block, Borders, Clear, List, ListItem, Paragraph, Wrap},
Frame,
};
usecrate::app::{App, CurrentScreen, CurrentlyEditing};
pubfnui(frame:&mut Frame, app:&App) {
// Create the layout sections.
letchunks= Layout::default()
.direction(Direction::Vertical)
.constraints([
Constraint::Length(3),
Constraint::Min(1),
Constraint::Length(3),
])
.split(frame.area());
lettitle_block= Block::default()
.borders(Borders::ALL)
.style(Style::default());
lettitle= Paragraph::new(Text::styled(
"Create New Json",
Style::default().fg(Color::Green),
))
.block(title_block);
frame.render_widget(title, chunks[0]);
letmutlist_items= Vec::<ListItem>::new();
forkeyinapp.pairs.keys() {
list_items.push(ListItem::new(Line::from(Span::styled(
format!("{: <25} : {}", key, app.pairs.get(key).unwrap()),
Style::default().fg(Color::Yellow),
))));
}
letlist= List::new(list_items);
frame.render_widget(list, chunks[1]);
letcurrent_navigation_text=vec![
// The first half of the text
matchapp.current_screen {
CurrentScreen::Main => Span::styled("Normal Mode", Style::default().fg(Color::Green)),
CurrentScreen::Editing => {
Span::styled("Editing Mode", Style::default().fg(Color::Yellow))
}
CurrentScreen::Exiting => Span::styled("Exiting", Style::default().fg(Color::LightRed)),
}
.to_owned(),
// A white divider bar to separate the two sections
Span::styled(" | ", Style::default().fg(Color::White)),
// The final section of the text, with hints on what the user is editing
{
iflet Some(editing) =&app.currently_editing {
matchediting {
CurrentlyEditing::Key => {
Span::styled("Editing Json Key", Style::default().fg(Color::Green))
}
CurrentlyEditing::Value => {
Span::styled("Editing Json Value", Style::default().fg(Color::LightGreen))
}
}
} else {
Span::styled("Not Editing Anything", Style::default().fg(Color::DarkGray))
}
},
];
letmode_footer= Paragraph::new(Line::from(current_navigation_text))
.block(Block::default().borders(Borders::ALL));
letcurrent_keys_hint= {
matchapp.current_screen {
CurrentScreen::Main => Span::styled(
"(q) to quit / (e) to make new pair",
Style::default().fg(Color::Red),
),
CurrentScreen::Editing => Span::styled(
"(ESC) to cancel/(Tab) to switch boxes/enter to complete",
Style::default().fg(Color::Red),
),
CurrentScreen::Exiting => Span::styled(
"(q) to quit / (e) to make new pair",
Style::default().fg(Color::Red),
),
}
};
letkey_notes_footer=
Paragraph::new(Line::from(current_keys_hint)).block(Block::default().borders(Borders::ALL));
letfooter_chunks= Layout::default()
.direction(Direction::Horizontal)
.constraints([Constraint::Percentage(50), Constraint::Percentage(50)])
.split(chunks[2]);
frame.render_widget(mode_footer, footer_chunks[0]);
frame.render_widget(key_notes_footer, footer_chunks[1]);
iflet Some(editing) =&app.currently_editing {
letpopup_block= Block::default()
.title("Enter a new key-value pair")
.borders(Borders::NONE)
.style(Style::default().bg(Color::DarkGray));
letarea=centered_rect(60, 25, frame.area());
frame.render_widget(popup_block, area);
letpopup_chunks= Layout::default()
.direction(Direction::Horizontal)
.margin(1)
.constraints([Constraint::Percentage(50), Constraint::Percentage(50)])
.split(area);
letmutkey_block= Block::default().title("Key").borders(Borders::ALL);
letmutvalue_block= Block::default().title("Value").borders(Borders::ALL);
letactive_style= Style::default().bg(Color::LightYellow).fg(Color::Black);
matchediting {
CurrentlyEditing::Key =>key_block=key_block.style(active_style),
CurrentlyEditing::Value =>value_block=value_block.style(active_style),
};
letkey_text= Paragraph::new(app.key_input.clone()).block(key_block);
frame.render_widget(key_text, popup_chunks[0]);
letvalue_text= Paragraph::new(app.value_input.clone()).block(value_block);
frame.render_widget(value_text, popup_chunks[1]);
}
iflet CurrentScreen::Exiting =app.current_screen {
frame.render_widget(Clear, frame.area()); //this clears the entire screen and anything already drawn
letpopup_block= Block::default()
.title("Y/N")
.borders(Borders::NONE)
.style(Style::default().bg(Color::DarkGray));
letexit_text= Text::styled(
"Would you like to output the buffer as json? (y/n)",
Style::default().fg(Color::Red),
);
// the `trim: false` will stop the text from being cut off when over the edge of the block
letexit_paragraph= Paragraph::new(exit_text)
.block(popup_block)
.wrap(Wrap { trim:false });
letarea=centered_rect(60, 25, frame.area());
frame.render_widget(exit_paragraph, area);
}
}
/// helper function to create a centered rect using up certain percentage of the available rect `r`
fncentered_rect(percent_x: u16, percent_y: u16, r: Rect) -> Rect {
// Cut the given rectangle into three vertical pieces
letpopup_layout= Layout::default()
.direction(Direction::Vertical)
.constraints([
Constraint::Percentage((100-percent_y) /2),
Constraint::Percentage(percent_y),
Constraint::Percentage((100-percent_y) /2),
])
.split(r);
// Then cut the middle vertical piece into three width-wise pieces
Layout::default()
.direction(Direction::Horizontal)
.constraints([
Constraint::Percentage((100-percent_x) /2),
Constraint::Percentage(percent_x),
Constraint::Percentage((100-percent_x) /2),
])
.split(popup_layout[1])[1] // Return the middle chunk
}
```