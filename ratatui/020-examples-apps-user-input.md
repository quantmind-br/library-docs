---
title: User Input
url: https://ratatui.rs/examples/apps/user_input/
source: crawler
fetched_at: 2026-02-01T21:12:44.496669675-03:00
rendered_js: false
word_count: 775
summary: This document demonstrates how to implement and handle user text input, cursor movement, and state-based input modes in a Ratatui terminal application.
tags:
    - ratatui
    - rust
    - user-input
    - terminal-ui
    - event-handling
    - cursor-management
category: tutorial
---

```

gitclonehttps://github.com/ratatui/ratatui.git--branchlatest
cdratatui
cargorun--example=user_input--features=crossterm
```

```

//! # [Ratatui] User Input example
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
// A simple example demonstrating how to handle user input. This is a bit out of the scope of
// the library as it does not provide any input handling out of the box. However, it may helps
// some to get started.
//
// This is a very simple example:
//   * An input box always focused. Every character you type is registered here.
//   * An entered character is inserted at the cursor position.
//   * Pressing Backspace erases the left character before the cursor position
//   * Pressing Enter pushes the current input in the history of previous messages. **Note: ** as
//   this is a relatively simple example unicode characters are unsupported and their use will
// result in undefined behaviour.
//
// See also https://github.com/rhysd/tui-textarea and https://github.com/sayanarijit/tui-input/
use color_eyre::Result;
use ratatui::{
crossterm::event::{self, Event, KeyCode, KeyEventKind},
layout::{Constraint, Layout, Position},
style::{Color, Modifier, Style, Stylize},
text::{Line, Span, Text},
widgets::{Block, List, ListItem, Paragraph},
DefaultTerminal, Frame,
};
fnmain() -> Result<()> {
color_eyre::install()?;
letterminal= ratatui::init();
letapp_result= App::new().run(terminal);
ratatui::restore();
app_result
}
/// App holds the state of the application
struct App {
/// Current value of the input box
input: String,
/// Position of cursor in the editor area.
character_index: usize,
/// Current input mode
input_mode: InputMode,
/// History of recorded messages
messages: Vec<String>,
}
enum InputMode {
Normal,
Editing,
}
impl App {
constfnnew() ->Self {
Self {
input: String::new(),
input_mode: InputMode::Normal,
messages: Vec::new(),
character_index:0,
}
}
fnmove_cursor_left(&mutself) {
letcursor_moved_left=self.character_index.saturating_sub(1);
self.character_index =self.clamp_cursor(cursor_moved_left);
}
fnmove_cursor_right(&mutself) {
letcursor_moved_right=self.character_index.saturating_add(1);
self.character_index =self.clamp_cursor(cursor_moved_right);
}
fnenter_char(&mutself, new_char: char) {
letindex=self.byte_index();
self.input.insert(index, new_char);
self.move_cursor_right();
}
/// Returns the byte index based on the character position.
///
/// Since each character in a string can be contain multiple bytes, it's necessary to calculate
/// the byte index based on the index of the character.
fnbyte_index(&self) -> usize {
self.input
.char_indices()
.map(|(i, _)|i)
.nth(self.character_index)
.unwrap_or(self.input.len())
}
fndelete_char(&mutself) {
letis_not_cursor_leftmost=self.character_index !=0;
ifis_not_cursor_leftmost {
// Method "remove" is not used on the saved text for deleting the selected char.
// Reason: Using remove on String works on bytes instead of the chars.
// Using remove would require special care because of char boundaries.
letcurrent_index=self.character_index;
letfrom_left_to_current_index=current_index-1;
// Getting all characters before the selected character.
letbefore_char_to_delete=self.input.chars().take(from_left_to_current_index);
// Getting all characters after selected character.
letafter_char_to_delete=self.input.chars().skip(current_index);
// Put all characters together except the selected one.
// By leaving the selected one out, it is forgotten and therefore deleted.
self.input =before_char_to_delete.chain(after_char_to_delete).collect();
self.move_cursor_left();
}
}
fnclamp_cursor(&self, new_cursor_pos: usize) -> usize {
new_cursor_pos.clamp(0, self.input.chars().count())
}
fnreset_cursor(&mutself) {
self.character_index =0;
}
fnsubmit_message(&mutself) {
self.messages.push(self.input.clone());
self.input.clear();
self.reset_cursor();
}
fnrun(mutself, mutterminal: DefaultTerminal) -> Result<()> {
loop {
terminal.draw(|frame|self.draw(frame))?;
iflet Event::Key(key) = event::read()? {
matchself.input_mode {
InputMode::Normal =>matchkey.code {
KeyCode::Char('e') => {
self.input_mode = InputMode::Editing;
}
KeyCode::Char('q') => {
return Ok(());
}
_=> {}
},
InputMode::Editing ifkey.kind == KeyEventKind::Press =>matchkey.code {
KeyCode::Enter =>self.submit_message(),
KeyCode::Char(to_insert) =>self.enter_char(to_insert),
KeyCode::Backspace =>self.delete_char(),
KeyCode::Left =>self.move_cursor_left(),
KeyCode::Right =>self.move_cursor_right(),
KeyCode::Esc =>self.input_mode = InputMode::Normal,
_=> {}
},
InputMode::Editing => {}
}
}
}
}
fndraw(&self, frame:&mut Frame) {
letvertical= Layout::vertical([
Constraint::Length(1),
Constraint::Length(3),
Constraint::Min(1),
]);
let [help_area, input_area, messages_area] =vertical.areas(frame.area());
let (msg, style) =matchself.input_mode {
InputMode::Normal => (
vec![
"Press ".into(),
"q".bold(),
" to exit, ".into(),
"e".bold(),
" to start editing.".bold(),
],
Style::default().add_modifier(Modifier::RAPID_BLINK),
),
InputMode::Editing => (
vec![
"Press ".into(),
"Esc".bold(),
" to stop editing, ".into(),
"Enter".bold(),
" to record the message".into(),
],
Style::default(),
),
};
lettext= Text::from(Line::from(msg)).patch_style(style);
lethelp_message= Paragraph::new(text);
frame.render_widget(help_message, help_area);
letinput= Paragraph::new(self.input.as_str())
.style(matchself.input_mode {
InputMode::Normal => Style::default(),
InputMode::Editing => Style::default().fg(Color::Yellow),
})
.block(Block::bordered().title("Input"));
frame.render_widget(input, input_area);
matchself.input_mode {
// Hide the cursor. `Frame` does this by default, so we don't need to do anything here
InputMode::Normal => {}
// Make the cursor visible and ask ratatui to put it at the specified coordinates after
// rendering
#[allow(clippy::cast_possible_truncation)]
InputMode::Editing =>frame.set_cursor_position(Position::new(
// Draw the cursor at the current position in the input field.
// This position is can be controlled via the left and right arrow key
input_area.x +self.character_index as u16 +1,
// Move one line down, from the border to the input line
input_area.y +1,
)),
}
letmessages: Vec<ListItem> =self
.messages
.iter()
.enumerate()
.map(|(i, m)| {
letcontent= Line::from(Span::raw(format!("{i}: {m}")));
ListItem::new(content)
})
.collect();
letmessages= List::new(messages).block(Block::bordered().title("Messages"));
frame.render_widget(messages, messages_area);
}
}
```