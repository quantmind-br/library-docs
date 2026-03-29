---
title: Flex
url: https://ratatui.rs/examples/layout/flex/
source: crawler
fetched_at: 2026-02-01T21:12:46.149591996-03:00
rendered_js: false
word_count: 1496
summary: This document demonstrates the Flex layout system in the Ratatui library, illustrating how different constraints and alignment strategies affect the distribution of space in a terminal UI.
tags:
    - rust
    - ratatui
    - tui
    - layout-constraints
    - flex-layout
    - terminal-ui
category: tutorial
---

```

gitclonehttps://github.com/ratatui/ratatui.git--branchlatest
cdratatui
cargorun--example=flex--features=crossterm
```

```

//! # [Ratatui] Flex example
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
use std::num::NonZeroUsize;
use color_eyre::Result;
use ratatui::{
buffer::Buffer,
crossterm::event::{self, Event, KeyCode, KeyEventKind},
layout::{
Alignment,
Constraint::{self, Fill, Length, Max, Min, Percentage, Ratio},
Flex, Layout, Rect,
},
style::{palette::tailwind, Color, Modifier, Style, Stylize},
symbols::{self, line},
text::{Line, Text},
widgets::{
Block, Paragraph, Scrollbar, ScrollbarOrientation, ScrollbarState, StatefulWidget, Tabs,
Widget,
},
DefaultTerminal,
};
use strum::{Display, EnumIter, FromRepr, IntoEnumIterator};
fnmain() -> Result<()> {
color_eyre::install()?;
letterminal= ratatui::init();
letapp_result= App::default().run(terminal);
ratatui::restore();
app_result
}
constEXAMPLE_DATA:&[(&str, &[Constraint])] =&[
(
"Min(u16) takes any excess space always",
&[Length(10), Min(10), Max(10), Percentage(10), Ratio(1,10)],
),
(
"Fill(u16) takes any excess space always",
&[Length(20), Percentage(20), Ratio(1, 5), Fill(1)],
),
(
"Here's all constraints in one line",
&[Length(10), Min(10), Max(10), Percentage(10), Ratio(1,10), Fill(1)],
),
(
"",
&[Max(50), Min(50)],
),
(
"",
&[Max(20), Length(10)],
),
(
"",
&[Max(20), Length(10)],
),
(
"Min grows always but also allows Fill to grow",
&[Percentage(50), Fill(1), Fill(2), Min(50)],
),
(
"In `Legacy`, the last constraint of lowest priority takes excess space",
&[Length(20), Length(20), Percentage(20)],
),
("", &[Length(20), Percentage(20), Length(20)]),
("A lowest priority constraint will be broken before a high priority constraint", &[Ratio(1,4), Percentage(20)]),
("`Length` is higher priority than `Percentage`", &[Percentage(20), Length(10)]),
("`Min/Max` is higher priority than `Length`", &[Length(10), Max(20)]),
("", &[Length(100), Min(20)]),
("`Length` is higher priority than `Min/Max`", &[Max(20), Length(10)]),
("", &[Min(20), Length(90)]),
("Fill is the lowest priority and will fill any excess space", &[Fill(1), Ratio(1, 4)]),
("Fill can be used to scale proportionally with other Fill blocks", &[Fill(1), Percentage(20), Fill(2)]),
("", &[Ratio(1, 3), Percentage(20), Ratio(2, 3)]),
("Legacy will stretch the last lowest priority constraint\nStretch will only stretch equal weighted constraints", &[Length(20), Length(15)]),
("", &[Percentage(20), Length(15)]),
("`Fill(u16)` fills up excess space, but is lower priority to spacers.\ni.e. Fill will only have widths in Flex::Stretch and Flex::Legacy", &[Fill(1), Fill(1)]),
("", &[Length(20), Length(20)]),
(
"When not using `Flex::Stretch` or `Flex::Legacy`,\n`Min(u16)` and `Max(u16)` collapse to their lowest values",
&[Min(20), Max(20)],
),
(
"",
&[Max(20)],
),
("", &[Min(20), Max(20), Length(20), Length(20)]),
("", &[Fill(0), Fill(0)]),
(
"`Fill(1)` can be to scale with respect to other `Fill(2)`",
&[Fill(1), Fill(2)],
),
(
"",
&[Fill(1), Min(10), Max(10), Fill(2)],
),
(
"`Fill(0)` collapses if there are other non-zero `Fill(_)`\nconstraints. e.g. `[Fill(0), Fill(0), Fill(1)]`:",
&[
Fill(0),
Fill(0),
Fill(1),
],
),
];
#[derive(Default, Clone, Copy)]
struct App {
selected_tab: SelectedTab,
scroll_offset: u16,
spacing: u16,
state: AppState,
}
#[derive(Debug, Default, Clone, Copy, PartialEq, Eq)]
enum AppState {
#[default]
Running,
Quit,
}
#[derive(Debug, Clone, PartialEq, Eq)]
struct Example {
constraints: Vec<Constraint>,
description: String,
flex: Flex,
spacing: u16,
}
/// Tabs for the different layouts
///
/// Note: the order of the variants will determine the order of the tabs this uses several derive
/// macros from the `strum` crate to make it easier to iterate over the variants.
/// (`FromRepr`,`Display`,`EnumIter`).
#[derive(Default, Debug, Copy, Clone, PartialEq, Eq, FromRepr, Display, EnumIter)]
enum SelectedTab {
#[default]
Legacy,
Start,
Center,
End,
SpaceAround,
SpaceBetween,
}
impl App {
fnrun(mutself, mutterminal: DefaultTerminal) -> Result<()> {
// increase the layout cache to account for the number of layout events. This ensures that
// layout is not generally reprocessed on every frame (which would lead to possible janky
// results when there are more than one possible solution to the requested layout). This
// assumes the user changes spacing about a 100 times or so.
letcache_size=EXAMPLE_DATA.len() * SelectedTab::iter().len() *100;
Layout::init_cache(NonZeroUsize::new(cache_size).unwrap());
whileself.is_running() {
terminal.draw(|frame|frame.render_widget(self, frame.area()))?;
self.handle_events()?;
}
Ok(())
}
fnis_running(self) -> bool {
self.state == AppState::Running
}
fnhandle_events(&mutself) -> Result<()> {
match event::read()? {
Event::Key(key) ifkey.kind == KeyEventKind::Press =>matchkey.code {
KeyCode::Char('q') | KeyCode::Esc =>self.quit(),
KeyCode::Char('l') | KeyCode::Right =>self.next(),
KeyCode::Char('h') | KeyCode::Left =>self.previous(),
KeyCode::Char('j') | KeyCode::Down =>self.down(),
KeyCode::Char('k') | KeyCode::Up =>self.up(),
KeyCode::Char('g') | KeyCode::Home =>self.top(),
KeyCode::Char('G') | KeyCode::End =>self.bottom(),
KeyCode::Char('+') =>self.increment_spacing(),
KeyCode::Char('-') =>self.decrement_spacing(),
_=> (),
},
_=> {}
}
Ok(())
}
fnnext(&mutself) {
self.selected_tab =self.selected_tab.next();
}
fnprevious(&mutself) {
self.selected_tab =self.selected_tab.previous();
}
fnup(&mutself) {
self.scroll_offset =self.scroll_offset.saturating_sub(1);
}
fndown(&mutself) {
self.scroll_offset =self
.scroll_offset
.saturating_add(1)
.min(max_scroll_offset());
}
fntop(&mutself) {
self.scroll_offset =0;
}
fnbottom(&mutself) {
self.scroll_offset =max_scroll_offset();
}
fnincrement_spacing(&mutself) {
self.spacing =self.spacing.saturating_add(1);
}
fndecrement_spacing(&mutself) {
self.spacing =self.spacing.saturating_sub(1);
}
fnquit(&mutself) {
self.state = AppState::Quit;
}
}
// when scrolling, make sure we don't scroll past the last example
fnmax_scroll_offset() -> u16 {
example_height()
-EXAMPLE_DATA
.last()
.map_or(0, |(desc, _)|get_description_height(desc) +4)
}
/// The height of all examples combined
///
/// Each may or may not have a title so we need to account for that.
fnexample_height() -> u16 {
EXAMPLE_DATA
.iter()
.map(|(desc, _)|get_description_height(desc) +4)
.sum()
}
impl Widget for App {
fnrender(self, area: Rect, buf:&mut Buffer) {
letlayout= Layout::vertical([Length(3), Length(1), Fill(0)]);
let [tabs, axis, demo] =layout.areas(area);
self.tabs().render(tabs, buf);
letscroll_needed=self.render_demo(demo, buf);
letaxis_width=ifscroll_needed {
axis.width.saturating_sub(1)
} else {
axis.width
};
Self::axis(axis_width, self.spacing).render(axis, buf);
}
}
impl App {
fntabs(self) ->impl Widget {
lettab_titles= SelectedTab::iter().map(SelectedTab::to_tab_title);
letblock= Block::new()
.title("Flex Layouts ".bold())
.title(" Use ◄ ► to change tab, ▲ ▼  to scroll, - + to change spacing ");
Tabs::new(tab_titles)
.block(block)
.highlight_style(Modifier::REVERSED)
.select(self.selected_tab as usize)
.divider("")
.padding("", "")
}
/// a bar like `<----- 80 px (gap: 2 px)? ----->`
fnaxis(width: u16, spacing: u16) ->impl Widget {
letwidth=widthas usize;
// only show gap when spacing is not zero
letlabel=ifspacing!=0 {
format!("{width} px (gap: {spacing} px)")
} else {
format!("{width} px")
};
letbar_width=width.saturating_sub(2); // we want to `<` and `>` at the ends
letwidth_bar=format!("<{label:-^bar_width$}>");
Paragraph::new(width_bar.dark_gray()).centered()
}
/// Render the demo content
///
/// This function renders the demo content into a separate buffer and then splices the buffer
/// into the main buffer. This is done to make it possible to handle scrolling easily.
///
/// Returns bool indicating whether scroll was needed
#[allow(clippy::cast_possible_truncation)]
fnrender_demo(self, area: Rect, buf:&mut Buffer) -> bool {
// render demo content into a separate buffer so all examples fit we add an extra
// area.height to make sure the last example is fully visible even when the scroll offset is
// at the max
letheight=example_height();
letdemo_area= Rect::new(0, 0, area.width, height);
letmutdemo_buf= Buffer::empty(demo_area);
letscrollbar_needed=self.scroll_offset !=0||height>area.height;
letcontent_area=ifscrollbar_needed {
Rect {
width:demo_area.width -1,
..demo_area
}
} else {
demo_area
};
letmutspacing=self.spacing;
self.selected_tab
.render(content_area, &mutdemo_buf, &mutspacing);
letvisible_content=demo_buf
.content
.into_iter()
.skip((area.width *self.scroll_offset) as usize)
.take(area.area() as usize);
for (i, cell) invisible_content.enumerate() {
letx=ias u16 %area.width;
lety=ias u16 /area.width;
buf[(area.x +x, area.y +y)] =cell;
}
ifscrollbar_needed {
letarea=area.intersection(buf.area);
letmutstate= ScrollbarState::new(max_scroll_offset() as usize)
.position(self.scroll_offset as usize);
Scrollbar::new(ScrollbarOrientation::VerticalRight).render(area, buf, &mutstate);
}
scrollbar_needed
}
}
impl SelectedTab {
/// Get the previous tab, if there is no previous tab return the current tab.
fnprevious(self) ->Self {
letcurrent_index: usize =selfas usize;
letprevious_index=current_index.saturating_sub(1);
Self::from_repr(previous_index).unwrap_or(self)
}
/// Get the next tab, if there is no next tab return the current tab.
fnnext(self) ->Self {
letcurrent_index=selfas usize;
letnext_index=current_index.saturating_add(1);
Self::from_repr(next_index).unwrap_or(self)
}
/// Convert a `SelectedTab` into a `Line` to display it by the `Tabs` widget.
fnto_tab_title(value:Self) -> Line<'static> {
use tailwind::{INDIGO, ORANGE, SKY};
lettext=value.to_string();
letcolor=matchvalue {
Self::Legacy =>ORANGE.c400,
Self::Start =>SKY.c400,
Self::Center =>SKY.c300,
Self::End =>SKY.c200,
Self::SpaceAround =>INDIGO.c400,
Self::SpaceBetween =>INDIGO.c300,
};
format!(" {text} ").fg(color).bg(Color::Black).into()
}
}
impl StatefulWidget for SelectedTab {
type State = u16;
fnrender(self, area: Rect, buf:&mut Buffer, spacing:&mutSelf::State) {
letspacing=*spacing;
matchself {
Self::Legacy =>Self::render_examples(area, buf, Flex::Legacy, spacing),
Self::Start =>Self::render_examples(area, buf, Flex::Start, spacing),
Self::Center =>Self::render_examples(area, buf, Flex::Center, spacing),
Self::End =>Self::render_examples(area, buf, Flex::End, spacing),
Self::SpaceAround =>Self::render_examples(area, buf, Flex::SpaceAround, spacing),
Self::SpaceBetween =>Self::render_examples(area, buf, Flex::SpaceBetween, spacing),
}
}
}
impl SelectedTab {
fnrender_examples(area: Rect, buf:&mut Buffer, flex: Flex, spacing: u16) {
letheights=EXAMPLE_DATA
.iter()
.map(|(desc, _)|get_description_height(desc) +4);
letareas= Layout::vertical(heights).flex(Flex::Start).split(area);
for (area, (description, constraints)) inareas.iter().zip(EXAMPLE_DATA.iter()) {
Example::new(constraints, description, flex, spacing).render(*area, buf);
}
}
}
impl Example {
fnnew(constraints:&[Constraint], description:&str, flex: Flex, spacing: u16) ->Self {
Self {
constraints:constraints.into(),
description:description.into(),
flex,
spacing,
}
}
}
impl Widget for Example {
fnrender(self, area: Rect, buf:&mut Buffer) {
lettitle_height=get_description_height(&self.description);
letlayout= Layout::vertical([Length(title_height), Fill(0)]);
let [title, illustrations] =layout.areas(area);
let (blocks, spacers) = Layout::horizontal(&self.constraints)
.flex(self.flex)
.spacing(self.spacing)
.split_with_spacers(illustrations);
if!self.description.is_empty() {
Paragraph::new(
self.description
.split('\n')
.map(|s|format!("// {s}").italic().fg(tailwind::SLATE.c400))
.map(Line::from)
.collect::<Vec<Line>>(),
)
.render(title, buf);
}
for (block, constraint) inblocks.iter().zip(&self.constraints) {
Self::illustration(*constraint, block.width).render(*block, buf);
}
forspacerinspacers.iter() {
Self::render_spacer(*spacer, buf);
}
}
}
impl Example {
fnrender_spacer(spacer: Rect, buf:&mut Buffer) {
ifspacer.width >1 {
letcorners_only= symbols::border::Set {
top_left: line::NORMAL.top_left,
top_right: line::NORMAL.top_right,
bottom_left: line::NORMAL.bottom_left,
bottom_right: line::NORMAL.bottom_right,
vertical_left:"",
vertical_right:"",
horizontal_top:"",
horizontal_bottom:"",
};
Block::bordered()
.border_set(corners_only)
.border_style(Style::reset().dark_gray())
.render(spacer, buf);
} else {
Paragraph::new(Text::from(vec![
Line::from(""),
Line::from("│"),
Line::from("│"),
Line::from(""),
]))
.style(Style::reset().dark_gray())
.render(spacer, buf);
}
letwidth=spacer.width;
letlabel=ifwidth>4 {
format!("{width} px")
} elseifwidth>2 {
format!("{width}")
} else {
String::new()
};
lettext= Text::from(vec![
Line::raw(""),
Line::raw(""),
Line::styled(label, Style::reset().dark_gray()),
]);
Paragraph::new(text)
.style(Style::reset().dark_gray())
.alignment(Alignment::Center)
.render(spacer, buf);
}
fnillustration(constraint: Constraint, width: u16) ->impl Widget {
letmain_color=color_for_constraint(constraint);
letfg_color= Color::White;
lettitle=format!("{constraint}");
letcontent=format!("{width} px");
lettext=format!("{title}\n{content}");
letblock= Block::bordered()
.border_set(symbols::border::QUADRANT_OUTSIDE)
.border_style(Style::reset().fg(main_color).reversed())
.style(Style::default().fg(fg_color).bg(main_color));
Paragraph::new(text).centered().block(block)
}
}
constfncolor_for_constraint(constraint: Constraint) -> Color {
use tailwind::{BLUE, SLATE};
matchconstraint {
Constraint::Min(_) =>BLUE.c900,
Constraint::Max(_) =>BLUE.c800,
Constraint::Length(_) =>SLATE.c700,
Constraint::Percentage(_) =>SLATE.c800,
Constraint::Ratio(_, _) =>SLATE.c900,
Constraint::Fill(_) =>SLATE.c950,
}
}
#[allow(clippy::cast_possible_truncation)]
fnget_description_height(s:&str) -> u16 {
ifs.is_empty() {
0
} else {
s.split('\n').count() as u16
}
}
```