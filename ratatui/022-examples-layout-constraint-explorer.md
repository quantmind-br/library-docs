---
title: Constraint Explorer
url: https://ratatui.rs/examples/layout/constraint-explorer/
source: crawler
fetched_at: 2026-02-01T21:12:44.811530147-03:00
rendered_js: false
word_count: 1367
summary: An interactive utility and code example for visualizing and exploring how different layout constraints interact within the Ratatui terminal UI library.
tags:
    - ratatui
    - rust
    - layout-constraints
    - terminal-ui
    - tui-development
    - visualization
category: tutorial
---

The constraint explorer is a utility that can be used to work out the interaction between your constraints.

```

gitclonehttps://github.com/ratatui/ratatui.git--branchlatest
cdratatui
cargorun--example=constraint-explorer--features=crossterm
```

````

//! # [Ratatui] Constraint explorer example
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
use itertools::Itertools;
use ratatui::{
buffer::Buffer,
crossterm::event::{self, Event, KeyCode, KeyEventKind},
layout::{
Constraint::{self, Fill, Length, Max, Min, Percentage, Ratio},
Flex, Layout, Rect,
},
style::{
palette::tailwind::{BLUE, SKY, SLATE, STONE},
Color, Style, Stylize,
},
symbols::{self, line},
text::{Line, Span, Text},
widgets::{Block, Paragraph, Widget, Wrap},
DefaultTerminal,
};
use strum::{Display, EnumIter, FromRepr};
fnmain() -> Result<()> {
color_eyre::install()?;
letterminal= ratatui::init();
letapp_result= App::default().run(terminal);
ratatui::restore();
app_result
}
#[derive(Default)]
struct App {
mode: AppMode,
spacing: u16,
constraints: Vec<Constraint>,
selected_index: usize,
value: u16,
}
#[derive(Debug, Default, PartialEq, Eq)]
enum AppMode {
#[default]
Running,
Quit,
}
/// A variant of [`Constraint`] that can be rendered as a tab.
#[derive(Debug, Default, Clone, Copy, PartialEq, Eq, EnumIter, FromRepr, Display)]
enum ConstraintName {
#[default]
Length,
Percentage,
Ratio,
Min,
Max,
Fill,
}
/// A widget that renders a [`Constraint`] as a block. E.g.:
/// ```plain
/// ┌──────────────┐
/// │  Length(16)  │
/// │     16px     │
/// └──────────────┘
/// ```
struct ConstraintBlock {
constraint: Constraint,
legend: bool,
selected: bool,
}
/// A widget that renders a spacer with a label indicating the width of the spacer. E.g.:
///
/// ```plain
/// ┌      ┐
///   8 px
/// └      ┘
/// ```
struct SpacerBlock;
// App behaviour
impl App {
fnrun(mutself, mutterminal: DefaultTerminal) -> Result<()> {
self.insert_test_defaults();
whileself.is_running() {
terminal.draw(|frame|frame.render_widget(&self, frame.area()))?;
self.handle_events()?;
}
Ok(())
}
// TODO remove these - these are just for testing
fninsert_test_defaults(&mutself) {
self.constraints =vec![
Constraint::Length(20),
Constraint::Length(20),
Constraint::Length(20),
];
self.value =20;
}
fnis_running(&self) -> bool {
self.mode == AppMode::Running
}
fnhandle_events(&mutself) -> Result<()> {
match event::read()? {
Event::Key(key) ifkey.kind == KeyEventKind::Press =>matchkey.code {
KeyCode::Char('q') | KeyCode::Esc =>self.exit(),
KeyCode::Char('1') =>self.swap_constraint(ConstraintName::Min),
KeyCode::Char('2') =>self.swap_constraint(ConstraintName::Max),
KeyCode::Char('3') =>self.swap_constraint(ConstraintName::Length),
KeyCode::Char('4') =>self.swap_constraint(ConstraintName::Percentage),
KeyCode::Char('5') =>self.swap_constraint(ConstraintName::Ratio),
KeyCode::Char('6') =>self.swap_constraint(ConstraintName::Fill),
KeyCode::Char('+') =>self.increment_spacing(),
KeyCode::Char('-') =>self.decrement_spacing(),
KeyCode::Char('x') =>self.delete_block(),
KeyCode::Char('a') =>self.insert_block(),
KeyCode::Char('k') | KeyCode::Up =>self.increment_value(),
KeyCode::Char('j') | KeyCode::Down =>self.decrement_value(),
KeyCode::Char('h') | KeyCode::Left =>self.prev_block(),
KeyCode::Char('l') | KeyCode::Right =>self.next_block(),
_=> {}
},
_=> {}
}
Ok(())
}
fnincrement_value(&mutself) {
let Some(constraint) =self.constraints.get_mut(self.selected_index) else {
return;
};
matchconstraint {
Constraint::Length(v)
| Constraint::Min(v)
| Constraint::Max(v)
| Constraint::Fill(v)
| Constraint::Percentage(v) =>*v=v.saturating_add(1),
Constraint::Ratio(_n, d) =>*d=d.saturating_add(1),
};
}
fndecrement_value(&mutself) {
let Some(constraint) =self.constraints.get_mut(self.selected_index) else {
return;
};
matchconstraint {
Constraint::Length(v)
| Constraint::Min(v)
| Constraint::Max(v)
| Constraint::Fill(v)
| Constraint::Percentage(v) =>*v=v.saturating_sub(1),
Constraint::Ratio(_n, d) =>*d=d.saturating_sub(1),
};
}
/// select the next block with wrap around
fnnext_block(&mutself) {
ifself.constraints.is_empty() {
return;
}
letlen=self.constraints.len();
self.selected_index = (self.selected_index +1) %len;
}
/// select the previous block with wrap around
fnprev_block(&mutself) {
ifself.constraints.is_empty() {
return;
}
letlen=self.constraints.len();
self.selected_index = (self.selected_index +self.constraints.len() -1) %len;
}
/// delete the selected block
fndelete_block(&mutself) {
ifself.constraints.is_empty() {
return;
}
self.constraints.remove(self.selected_index);
self.selected_index =self.selected_index.saturating_sub(1);
}
/// insert a block after the selected block
fninsert_block(&mutself) {
letindex=self
.selected_index
.saturating_add(1)
.min(self.constraints.len());
letconstraint= Constraint::Length(self.value);
self.constraints.insert(index, constraint);
self.selected_index =index;
}
fnincrement_spacing(&mutself) {
self.spacing =self.spacing.saturating_add(1);
}
fndecrement_spacing(&mutself) {
self.spacing =self.spacing.saturating_sub(1);
}
fnexit(&mutself) {
self.mode = AppMode::Quit;
}
fnswap_constraint(&mutself, name: ConstraintName) {
ifself.constraints.is_empty() {
return;
}
letconstraint=matchname {
ConstraintName::Length =>Length(self.value),
ConstraintName::Percentage =>Percentage(self.value),
ConstraintName::Min =>Min(self.value),
ConstraintName::Max =>Max(self.value),
ConstraintName::Fill =>Fill(self.value),
ConstraintName::Ratio =>Ratio(1, u32::from(self.value) /4), // for balance
};
self.constraints[self.selected_index] =constraint;
}
}
impl From<Constraint> for ConstraintName {
fnfrom(constraint: Constraint) ->Self {
matchconstraint {
Length(_) =>Self::Length,
Percentage(_) =>Self::Percentage,
Ratio(_, _) =>Self::Ratio,
Min(_) =>Self::Min,
Max(_) =>Self::Max,
Fill(_) =>Self::Fill,
}
}
}
impl Widget for&App {
fnrender(self, area: Rect, buf:&mut Buffer) {
let [header_area, instructions_area, swap_legend_area, _, blocks_area] =
Layout::vertical([
Length(2), // header
Length(2), // instructions
Length(1), // swap key legend
Length(1), // gap
Fill(1),   // blocks
])
.areas(area);
App::header().render(header_area, buf);
App::instructions().render(instructions_area, buf);
App::swap_legend().render(swap_legend_area, buf);
self.render_layout_blocks(blocks_area, buf);
}
}
// App rendering
impl App {
constHEADER_COLOR: Color =SLATE.c200;
constTEXT_COLOR: Color =SLATE.c400;
constAXIS_COLOR: Color =SLATE.c500;
fnheader() ->impl Widget {
lettext="Constraint Explorer";
text.bold().fg(Self::HEADER_COLOR).into_centered_line()
}
fninstructions() ->impl Widget {
lettext="◄ ►: select, ▲ ▼: edit, 1-6: swap, a: add, x: delete, q: quit, + -: spacing";
Paragraph::new(text)
.fg(Self::TEXT_COLOR)
.centered()
.wrap(Wrap { trim:false })
}
fnswap_legend() ->impl Widget {
#[allow(unstable_name_collisions)]
Paragraph::new(
Line::from(
[
ConstraintName::Min,
ConstraintName::Max,
ConstraintName::Length,
ConstraintName::Percentage,
ConstraintName::Ratio,
ConstraintName::Fill,
]
.iter()
.enumerate()
.map(|(i, name)| {
format!("  {i}: {name}  ", i=i+1)
.fg(SLATE.c200)
.bg(name.color())
})
.intersperse(Span::from(""))
.collect_vec(),
)
.centered(),
)
.wrap(Wrap { trim:false })
}
/// A bar like `<----- 80 px (gap: 2 px) ----->`
///
/// Only shows the gap when spacing is not zero
fnaxis(&self, width: u16) ->impl Widget {
letlabel=ifself.spacing !=0 {
format!("{} px (gap: {} px)", width, self.spacing)
} else {
format!("{width} px")
};
letbar_width=width.saturating_sub(2) as usize; // we want to `<` and `>` at the ends
letwidth_bar=format!("<{label:-^bar_width$}>");
Paragraph::new(width_bar).fg(Self::AXIS_COLOR).centered()
}
fnrender_layout_blocks(&self, area: Rect, buf:&mut Buffer) {
let [user_constraints, area] = Layout::vertical([Length(3), Fill(1)])
.spacing(1)
.areas(area);
self.render_user_constraints_legend(user_constraints, buf);
let [start, center, end, space_around, space_between] =
Layout::vertical([Length(7); 5]).areas(area);
self.render_layout_block(Flex::Start, start, buf);
self.render_layout_block(Flex::Center, center, buf);
self.render_layout_block(Flex::End, end, buf);
self.render_layout_block(Flex::SpaceAround, space_around, buf);
self.render_layout_block(Flex::SpaceBetween, space_between, buf);
}
fnrender_user_constraints_legend(&self, area: Rect, buf:&mut Buffer) {
letconstraints=self.constraints.iter().map(|_| Constraint::Fill(1));
letblocks= Layout::horizontal(constraints).split(area);
for (i, (area, constraint)) inblocks.iter().zip(self.constraints.iter()).enumerate() {
letselected=self.selected_index ==i;
ConstraintBlock::new(*constraint, selected, true).render(*area, buf);
}
}
fnrender_layout_block(&self, flex: Flex, area: Rect, buf:&mut Buffer) {
let [label_area, axis_area, blocks_area] =
Layout::vertical([Length(1), Max(1), Length(4)]).areas(area);
iflabel_area.height >0 {
format!("Flex::{flex:?}").bold().render(label_area, buf);
}
self.axis(area.width).render(axis_area, buf);
let (blocks, spacers) = Layout::horizontal(&self.constraints)
.flex(flex)
.spacing(self.spacing)
.split_with_spacers(blocks_area);
for (i, (area, constraint)) inblocks.iter().zip(self.constraints.iter()).enumerate() {
letselected=self.selected_index ==i;
ConstraintBlock::new(*constraint, selected, false).render(*area, buf);
}
forareainspacers.iter() {
SpacerBlock.render(*area, buf);
}
}
}
impl Widget for ConstraintBlock {
fnrender(self, area: Rect, buf:&mut Buffer) {
matcharea.height {
1=>self.render_1px(area, buf),
2=>self.render_2px(area, buf),
_=>self.render_4px(area, buf),
}
}
}
impl ConstraintBlock {
constTEXT_COLOR: Color =SLATE.c200;
constfnnew(constraint: Constraint, selected: bool, legend: bool) ->Self {
Self {
constraint,
legend,
selected,
}
}
fnlabel(&self, width: u16) -> String {
letlong_width=format!("{width} px");
letshort_width=format!("{width}");
// border takes up 2 columns
letavailable_space=width.saturating_sub(2) as usize;
letwidth_label=iflong_width.len() < available_space {
long_width
} elseifshort_width.len() < available_space {
short_width
} else {
String::new()
};
format!("{}\n{}", self.constraint, width_label)
}
fnrender_1px(&self, area: Rect, buf:&mut Buffer) {
letlighter_color= ConstraintName::from(self.constraint).lighter_color();
letmain_color= ConstraintName::from(self.constraint).color();
letselected_color=ifself.selected {
lighter_color
} else {
main_color
};
Block::new()
.fg(Self::TEXT_COLOR)
.bg(selected_color)
.render(area, buf);
}
fnrender_2px(&self, area: Rect, buf:&mut Buffer) {
letlighter_color= ConstraintName::from(self.constraint).lighter_color();
letmain_color= ConstraintName::from(self.constraint).color();
letselected_color=ifself.selected {
lighter_color
} else {
main_color
};
Block::bordered()
.border_set(symbols::border::QUADRANT_OUTSIDE)
.border_style(Style::reset().fg(selected_color).reversed())
.render(area, buf);
}
fnrender_4px(&self, area: Rect, buf:&mut Buffer) {
letlighter_color= ConstraintName::from(self.constraint).lighter_color();
letmain_color= ConstraintName::from(self.constraint).color();
letselected_color=ifself.selected {
lighter_color
} else {
main_color
};
letcolor=ifself.legend {
selected_color
} else {
main_color
};
letlabel=self.label(area.width);
letblock= Block::bordered()
.border_set(symbols::border::QUADRANT_OUTSIDE)
.border_style(Style::reset().fg(color).reversed())
.fg(Self::TEXT_COLOR)
.bg(color);
Paragraph::new(label)
.centered()
.fg(Self::TEXT_COLOR)
.bg(color)
.block(block)
.render(area, buf);
if!self.legend {
letborder_color=ifself.selected {
lighter_color
} else {
main_color
};
iflet Some(last_row) =area.rows().next_back() {
buf.set_style(last_row, border_color);
}
}
}
}
impl Widget for SpacerBlock {
fnrender(self, area: Rect, buf:&mut Buffer) {
matcharea.height {
1=> (),
2=>Self::render_2px(area, buf),
3=>Self::render_3px(area, buf),
_=>Self::render_4px(area, buf),
}
}
}
impl SpacerBlock {
constTEXT_COLOR: Color =SLATE.c500;
constBORDER_COLOR: Color =SLATE.c600;
/// A block with a corner borders
fnblock() ->impl Widget {
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
.border_style(Self::BORDER_COLOR)
}
/// A vertical line used if there is not enough space to render the block
fnline() ->impl Widget {
Paragraph::new(Text::from(vec![
Line::from(""),
Line::from("│"),
Line::from("│"),
Line::from(""),
]))
.style(Self::BORDER_COLOR)
}
/// A label that says "Spacer" if there is enough space
fnspacer_label(width: u16) ->impl Widget {
letlabel=ifwidth>=6 { "Spacer" } else { "" };
label.fg(Self::TEXT_COLOR).into_centered_line()
}
/// A label that says "8 px" if there is enough space
fnlabel(width: u16) ->impl Widget {
letlong_label=format!("{width} px");
letshort_label=format!("{width}");
letlabel=iflong_label.len() < widthas usize {
long_label
} elseifshort_label.len() < widthas usize {
short_label
} else {
String::new()
};
Line::styled(label, Self::TEXT_COLOR).centered()
}
fnrender_2px(area: Rect, buf:&mut Buffer) {
ifarea.width >1 {
Self::block().render(area, buf);
} else {
Self::line().render(area, buf);
}
}
fnrender_3px(area: Rect, buf:&mut Buffer) {
ifarea.width >1 {
Self::block().render(area, buf);
} else {
Self::line().render(area, buf);
}
letrow=area.rows().nth(1).unwrap_or_default();
Self::spacer_label(area.width).render(row, buf);
}
fnrender_4px(area: Rect, buf:&mut Buffer) {
ifarea.width >1 {
Self::block().render(area, buf);
} else {
Self::line().render(area, buf);
}
letrow=area.rows().nth(1).unwrap_or_default();
Self::spacer_label(area.width).render(row, buf);
letrow=area.rows().nth(2).unwrap_or_default();
Self::label(area.width).render(row, buf);
}
}
impl ConstraintName {
constfncolor(self) -> Color {
matchself {
Self::Length =>SLATE.c700,
Self::Percentage =>SLATE.c800,
Self::Ratio =>SLATE.c900,
Self::Fill =>SLATE.c950,
Self::Min =>BLUE.c800,
Self::Max =>BLUE.c900,
}
}
constfnlighter_color(self) -> Color {
matchself {
Self::Length =>STONE.c500,
Self::Percentage =>STONE.c600,
Self::Ratio =>STONE.c700,
Self::Fill =>STONE.c800,
Self::Min =>SKY.c600,
Self::Max =>SKY.c700,
}
}
}
````