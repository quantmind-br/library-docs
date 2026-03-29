---
title: Table
url: https://ratatui.rs/examples/widgets/table/
source: crawler
fetched_at: 2026-02-01T21:12:57.933413953-03:00
rendered_js: false
word_count: 737
summary: This document provides a comprehensive example of implementing a stateful, interactive table widget in Ratatui, featuring row and column highlighting, custom styling, and scrollbar integration.
tags:
    - rust
    - ratatui
    - tui
    - table-widget
    - terminal-interface
    - stateful-widgets
    - event-handling
category: tutorial
---

```

gitclonehttps://github.com/ratatui/ratatui.git--branchlatest
cdratatui
cargorun--example=table--features=crossterm
```

```

//! # [Ratatui] Table example
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
use crossterm::event::KeyModifiers;
use itertools::Itertools;
use ratatui::{
crossterm::event::{self, Event, KeyCode, KeyEventKind},
layout::{Constraint, Layout, Margin, Rect},
style::{self, Color, Modifier, Style, Stylize},
text::Text,
widgets::{
Block, BorderType, Cell, HighlightSpacing, Paragraph, Row, Scrollbar, ScrollbarOrientation,
ScrollbarState, Table, TableState,
},
DefaultTerminal, Frame,
};
use style::palette::tailwind;
use unicode_width::UnicodeWidthStr;
constPALETTES: [tailwind::Palette; 4] = [
tailwind::BLUE,
tailwind::EMERALD,
tailwind::INDIGO,
tailwind::RED,
];
constINFO_TEXT: [&str; 2] = [
"(Esc) quit | (↑) move up | (↓) move down | (←) move left | (→) move right",
"(Shift + →) next color | (Shift + ←) previous color",
];
constITEM_HEIGHT: usize =4;
fnmain() -> Result<()> {
color_eyre::install()?;
letterminal= ratatui::init();
letapp_result= App::new().run(terminal);
ratatui::restore();
app_result
}
struct TableColors {
buffer_bg: Color,
header_bg: Color,
header_fg: Color,
row_fg: Color,
selected_row_style_fg: Color,
selected_column_style_fg: Color,
selected_cell_style_fg: Color,
normal_row_color: Color,
alt_row_color: Color,
footer_border_color: Color,
}
impl TableColors {
constfnnew(color:&tailwind::Palette) ->Self {
Self {
buffer_bg: tailwind::SLATE.c950,
header_bg:color.c900,
header_fg: tailwind::SLATE.c200,
row_fg: tailwind::SLATE.c200,
selected_row_style_fg:color.c400,
selected_column_style_fg:color.c400,
selected_cell_style_fg:color.c600,
normal_row_color: tailwind::SLATE.c950,
alt_row_color: tailwind::SLATE.c900,
footer_border_color:color.c400,
}
}
}
struct Data {
name: String,
address: String,
email: String,
}
impl Data {
constfnref_array(&self) -> [&String; 3] {
[&self.name, &self.address, &self.email]
}
fnname(&self) ->&str {
&self.name
}
fnaddress(&self) ->&str {
&self.address
}
fnemail(&self) ->&str {
&self.email
}
}
struct App {
state: TableState,
items: Vec<Data>,
longest_item_lens: (u16, u16, u16), // order is (name, address, email)
scroll_state: ScrollbarState,
colors: TableColors,
color_index: usize,
}
impl App {
fnnew() ->Self {
letdata_vec=generate_fake_names();
Self {
state: TableState::default().with_selected(0),
longest_item_lens:constraint_len_calculator(&data_vec),
scroll_state: ScrollbarState::new((data_vec.len() -1) *ITEM_HEIGHT),
colors: TableColors::new(&PALETTES[0]),
color_index:0,
items:data_vec,
}
}
pubfnnext_row(&mutself) {
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
self.scroll_state =self.scroll_state.position(i*ITEM_HEIGHT);
}
pubfnprevious_row(&mutself) {
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
self.scroll_state =self.scroll_state.position(i*ITEM_HEIGHT);
}
pubfnnext_column(&mutself) {
self.state.select_next_column();
}
pubfnprevious_column(&mutself) {
self.state.select_previous_column();
}
pubfnnext_color(&mutself) {
self.color_index = (self.color_index +1) %PALETTES.len();
}
pubfnprevious_color(&mutself) {
letcount=PALETTES.len();
self.color_index = (self.color_index +count-1) %count;
}
pubfnset_colors(&mutself) {
self.colors = TableColors::new(&PALETTES[self.color_index]);
}
fnrun(mutself, mutterminal: DefaultTerminal) -> Result<()> {
loop {
terminal.draw(|frame|self.draw(frame))?;
iflet Event::Key(key) = event::read()? {
ifkey.kind == KeyEventKind::Press {
letshift_pressed=key.modifiers.contains(KeyModifiers::SHIFT);
matchkey.code {
KeyCode::Char('q') | KeyCode::Esc =>return Ok(()),
KeyCode::Char('j') | KeyCode::Down =>self.next_row(),
KeyCode::Char('k') | KeyCode::Up =>self.previous_row(),
KeyCode::Char('l') | KeyCode::Right ifshift_pressed=>self.next_color(),
KeyCode::Char('h') | KeyCode::Left ifshift_pressed=> {
self.previous_color();
}
KeyCode::Char('l') | KeyCode::Right =>self.next_column(),
KeyCode::Char('h') | KeyCode::Left =>self.previous_column(),
_=> {}
}
}
}
}
}
fndraw(&mutself, frame:&mut Frame) {
letvertical=&Layout::vertical([Constraint::Min(5), Constraint::Length(4)]);
letrects=vertical.split(frame.area());
self.set_colors();
self.render_table(frame, rects[0]);
self.render_scrollbar(frame, rects[0]);
self.render_footer(frame, rects[1]);
}
fnrender_table(&mutself, frame:&mut Frame, area: Rect) {
letheader_style= Style::default()
.fg(self.colors.header_fg)
.bg(self.colors.header_bg);
letselected_row_style= Style::default()
.add_modifier(Modifier::REVERSED)
.fg(self.colors.selected_row_style_fg);
letselected_col_style= Style::default().fg(self.colors.selected_column_style_fg);
letselected_cell_style= Style::default()
.add_modifier(Modifier::REVERSED)
.fg(self.colors.selected_cell_style_fg);
letheader= ["Name", "Address", "Email"]
.into_iter()
.map(Cell::from)
.collect::<Row>()
.style(header_style)
.height(1);
letrows=self.items.iter().enumerate().map(|(i, data)| {
letcolor=matchi%2 {
0=>self.colors.normal_row_color,
_=>self.colors.alt_row_color,
};
letitem=data.ref_array();
item.into_iter()
.map(|content| Cell::from(Text::from(format!("\n{content}\n"))))
.collect::<Row>()
.style(Style::new().fg(self.colors.row_fg).bg(color))
.height(4)
});
letbar=" █ ";
lett= Table::new(
rows,
[
// + 1 is for padding.
Constraint::Length(self.longest_item_lens.0+1),
Constraint::Min(self.longest_item_lens.1+1),
Constraint::Min(self.longest_item_lens.2),
],
)
.header(header)
.row_highlight_style(selected_row_style)
.column_highlight_style(selected_col_style)
.cell_highlight_style(selected_cell_style)
.highlight_symbol(Text::from(vec![
"".into(),
bar.into(),
bar.into(),
"".into(),
]))
.bg(self.colors.buffer_bg)
.highlight_spacing(HighlightSpacing::Always);
frame.render_stateful_widget(t, area, &mutself.state);
}
fnrender_scrollbar(&mutself, frame:&mut Frame, area: Rect) {
frame.render_stateful_widget(
Scrollbar::default()
.orientation(ScrollbarOrientation::VerticalRight)
.begin_symbol(None)
.end_symbol(None),
area.inner(Margin {
vertical:1,
horizontal:1,
}),
&mutself.scroll_state,
);
}
fnrender_footer(&self, frame:&mut Frame, area: Rect) {
letinfo_footer= Paragraph::new(Text::from_iter(INFO_TEXT))
.style(
Style::new()
.fg(self.colors.row_fg)
.bg(self.colors.buffer_bg),
)
.centered()
.block(
Block::bordered()
.border_type(BorderType::Double)
.border_style(Style::new().fg(self.colors.footer_border_color)),
);
frame.render_widget(info_footer, area);
}
}
fngenerate_fake_names() -> Vec<Data> {
use fakeit::{address, contact, name};
(0..20)
.map(|_| {
letname= name::full();
letaddress=format!(
"{}\n{}, {} {}",
address::street(),
address::city(),
address::state(),
address::zip()
);
letemail= contact::email();
Data {
name,
address,
email,
}
})
.sorted_by(|a, b|a.name.cmp(&b.name))
.collect()
}
fnconstraint_len_calculator(items:&[Data]) -> (u16, u16, u16) {
letname_len=items
.iter()
.map(Data::name)
.map(UnicodeWidthStr::width)
.max()
.unwrap_or(0);
letaddress_len=items
.iter()
.map(Data::address)
.flat_map(str::lines)
.map(UnicodeWidthStr::width)
.max()
.unwrap_or(0);
letemail_len=items
.iter()
.map(Data::email)
.map(UnicodeWidthStr::width)
.max()
.unwrap_or(0);
#[allow(clippy::cast_possible_truncation)]
(name_lenas u16, address_lenas u16, email_lenas u16)
}
#[cfg(test)]
mod tests {
usecrate::Data;
#[test]
fnconstraint_len_calculator() {
lettest_data=vec![
Data {
name:"Emirhan Tala".to_string(),
address:"Cambridgelaan 6XX\n3584 XX Utrecht".to_string(),
email:"[email protected]".to_string(),
},
Data {
name:"thistextis26characterslong".to_string(),
address:"this line is 31 characters long\nbottom line is 33 characters long"
.to_string(),
email:"[email protected]".to_string(),
},
];
let (longest_name_len, longest_address_len, longest_email_len) =
crate::constraint_len_calculator(&test_data);
assert_eq!(26, longest_name_len);
assert_eq!(33, longest_address_len);
assert_eq!(40, longest_email_len);
}
}
```