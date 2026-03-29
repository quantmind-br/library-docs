---
title: Constraints
url: https://ratatui.rs/examples/layout/constraints/
source: crawler
fetched_at: 2026-02-01T21:12:45.770636666-03:00
rendered_js: false
word_count: 1057
summary: This document provides a comprehensive code example demonstrating how to use different layout constraints in Ratatui to organize UI elements, covering Min, Max, Length, Percentage, Ratio, and Fill.
tags:
    - rust
    - ratatui
    - tui
    - layout-constraints
    - terminal-ui
    - user-interface
category: tutorial
---

```

gitclonehttps://github.com/ratatui/ratatui.git--branchlatest
cdratatui
cargorun--example=constraints--features=crossterm
```

```

//! # [Ratatui] Constraints example
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
use ratatui::{
buffer::Buffer,
crossterm::event::{self, Event, KeyCode, KeyEventKind},
layout::{
Constraint::{self, Fill, Length, Max, Min, Percentage, Ratio},
Layout, Rect,
},
style::{palette::tailwind, Color, Modifier, Style, Stylize},
symbols,
text::Line,
widgets::{
Block, Padding, Paragraph, Scrollbar, ScrollbarOrientation, ScrollbarState, StatefulWidget,
Tabs, Widget,
},
DefaultTerminal,
};
use strum::{Display, EnumIter, FromRepr, IntoEnumIterator};
constSPACER_HEIGHT: u16 =0;
constILLUSTRATION_HEIGHT: u16 =4;
constEXAMPLE_HEIGHT: u16 =ILLUSTRATION_HEIGHT+SPACER_HEIGHT;
// priority 2
constMIN_COLOR: Color = tailwind::BLUE.c900;
constMAX_COLOR: Color = tailwind::BLUE.c800;
// priority 3
constLENGTH_COLOR: Color = tailwind::SLATE.c700;
constPERCENTAGE_COLOR: Color = tailwind::SLATE.c800;
constRATIO_COLOR: Color = tailwind::SLATE.c900;
// priority 4
constFILL_COLOR: Color = tailwind::SLATE.c950;
fnmain() -> Result<()> {
color_eyre::install()?;
letterminal= ratatui::init();
letapp_result= App::default().run(terminal);
ratatui::restore();
app_result
}
#[derive(Default, Clone, Copy)]
struct App {
selected_tab: SelectedTab,
scroll_offset: u16,
max_scroll_offset: u16,
state: AppState,
}
/// Tabs for the different examples
///
/// The order of the variants is the order in which they are displayed.
#[derive(Default, Debug, Copy, Clone, Display, FromRepr, EnumIter, PartialEq, Eq)]
enum SelectedTab {
#[default]
Min,
Max,
Length,
Percentage,
Ratio,
Fill,
}
#[derive(Debug, Default, Clone, Copy, PartialEq, Eq)]
enum AppState {
#[default]
Running,
Quit,
}
impl App {
fnrun(mutself, mutterminal: DefaultTerminal) -> Result<()> {
self.update_max_scroll_offset();
whileself.is_running() {
terminal.draw(|frame|frame.render_widget(self, frame.area()))?;
self.handle_events()?;
}
Ok(())
}
fnupdate_max_scroll_offset(&mutself) {
self.max_scroll_offset = (self.selected_tab.get_example_count() -1) *EXAMPLE_HEIGHT;
}
fnis_running(self) -> bool {
self.state == AppState::Running
}
fnhandle_events(&mutself) -> Result<()> {
iflet Event::Key(key) = event::read()? {
ifkey.kind != KeyEventKind::Press {
return Ok(());
}
matchkey.code {
KeyCode::Char('q') | KeyCode::Esc =>self.quit(),
KeyCode::Char('l') | KeyCode::Right =>self.next(),
KeyCode::Char('h') | KeyCode::Left =>self.previous(),
KeyCode::Char('j') | KeyCode::Down =>self.down(),
KeyCode::Char('k') | KeyCode::Up =>self.up(),
KeyCode::Char('g') | KeyCode::Home =>self.top(),
KeyCode::Char('G') | KeyCode::End =>self.bottom(),
_=> (),
}
}
Ok(())
}
fnquit(&mutself) {
self.state = AppState::Quit;
}
fnnext(&mutself) {
self.selected_tab =self.selected_tab.next();
self.update_max_scroll_offset();
self.scroll_offset =0;
}
fnprevious(&mutself) {
self.selected_tab =self.selected_tab.previous();
self.update_max_scroll_offset();
self.scroll_offset =0;
}
fnup(&mutself) {
self.scroll_offset =self.scroll_offset.saturating_sub(1);
}
fndown(&mutself) {
self.scroll_offset =self
.scroll_offset
.saturating_add(1)
.min(self.max_scroll_offset);
}
fntop(&mutself) {
self.scroll_offset =0;
}
fnbottom(&mutself) {
self.scroll_offset =self.max_scroll_offset;
}
}
impl Widget for App {
fnrender(self, area: Rect, buf:&mut Buffer) {
let [tabs, axis, demo] = Layout::vertical([Length(3), Length(3), Fill(0)]).areas(area);
self.render_tabs(tabs, buf);
Self::render_axis(axis, buf);
self.render_demo(demo, buf);
}
}
impl App {
fnrender_tabs(self, area: Rect, buf:&mut Buffer) {
lettitles= SelectedTab::iter().map(SelectedTab::to_tab_title);
letblock= Block::new()
.title("Constraints ".bold())
.title(" Use h l or ◄ ► to change tab and j k or ▲ ▼  to scroll");
Tabs::new(titles)
.block(block)
.highlight_style(Modifier::REVERSED)
.select(self.selected_tab as usize)
.padding("", "")
.divider("")
.render(area, buf);
}
fnrender_axis(area: Rect, buf:&mut Buffer) {
letwidth=area.width as usize;
// a bar like `<----- 80 px ----->`
letwidth_label=format!("{width} px");
letwidth_bar=format!(
"<{width_label:-^width$}>",
width=width-width_label.len() /2
);
Paragraph::new(width_bar.dark_gray())
.centered()
.block(Block::new().padding(Padding {
left:0,
right:0,
top:1,
bottom:0,
}))
.render(area, buf);
}
/// Render the demo content
///
/// This function renders the demo content into a separate buffer and then splices the buffer
/// into the main buffer. This is done to make it possible to handle scrolling easily.
#[allow(clippy::cast_possible_truncation)]
fnrender_demo(self, area: Rect, buf:&mut Buffer) {
// render demo content into a separate buffer so all examples fit we add an extra
// area.height to make sure the last example is fully visible even when the scroll offset is
// at the max
letheight=self.selected_tab.get_example_count() *EXAMPLE_HEIGHT;
letdemo_area= Rect::new(0, 0, area.width, height+area.height);
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
self.selected_tab.render(content_area, &mutdemo_buf);
letvisible_content=demo_buf
.content
.into_iter()
.skip((demo_area.width *self.scroll_offset) as usize)
.take(area.area() as usize);
for (i, cell) invisible_content.enumerate() {
letx=ias u16 %area.width;
lety=ias u16 /area.width;
buf[(area.x +x, area.y +y)] =cell;
}
ifscrollbar_needed {
letmutstate= ScrollbarState::new(self.max_scroll_offset as usize)
.position(self.scroll_offset as usize);
Scrollbar::new(ScrollbarOrientation::VerticalRight).render(area, buf, &mutstate);
}
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
constfnget_example_count(self) -> u16 {
#[allow(clippy::match_same_arms)]
matchself {
Self::Length =>4,
Self::Percentage =>5,
Self::Ratio =>4,
Self::Fill =>2,
Self::Min =>5,
Self::Max =>5,
}
}
fnto_tab_title(value:Self) -> Line<'static> {
lettext=format!("  {value}  ");
letcolor=matchvalue {
Self::Length =>LENGTH_COLOR,
Self::Percentage =>PERCENTAGE_COLOR,
Self::Ratio =>RATIO_COLOR,
Self::Fill =>FILL_COLOR,
Self::Min =>MIN_COLOR,
Self::Max =>MAX_COLOR,
};
text.fg(tailwind::SLATE.c200).bg(color).into()
}
}
impl Widget for SelectedTab {
fnrender(self, area: Rect, buf:&mut Buffer) {
matchself {
Self::Length =>Self::render_length_example(area, buf),
Self::Percentage =>Self::render_percentage_example(area, buf),
Self::Ratio =>Self::render_ratio_example(area, buf),
Self::Fill =>Self::render_fill_example(area, buf),
Self::Min =>Self::render_min_example(area, buf),
Self::Max =>Self::render_max_example(area, buf),
}
}
}
impl SelectedTab {
fnrender_length_example(area: Rect, buf:&mut Buffer) {
let [example1, example2, example3, _] =
Layout::vertical([Length(EXAMPLE_HEIGHT); 4]).areas(area);
Example::new(&[Length(20), Length(20)]).render(example1, buf);
Example::new(&[Length(20), Min(20)]).render(example2, buf);
Example::new(&[Length(20), Max(20)]).render(example3, buf);
}
fnrender_percentage_example(area: Rect, buf:&mut Buffer) {
let [example1, example2, example3, example4, example5, _] =
Layout::vertical([Length(EXAMPLE_HEIGHT); 6]).areas(area);
Example::new(&[Percentage(75), Fill(0)]).render(example1, buf);
Example::new(&[Percentage(25), Fill(0)]).render(example2, buf);
Example::new(&[Percentage(50), Min(20)]).render(example3, buf);
Example::new(&[Percentage(0), Max(0)]).render(example4, buf);
Example::new(&[Percentage(0), Fill(0)]).render(example5, buf);
}
fnrender_ratio_example(area: Rect, buf:&mut Buffer) {
let [example1, example2, example3, example4, _] =
Layout::vertical([Length(EXAMPLE_HEIGHT); 5]).areas(area);
Example::new(&[Ratio(1, 2); 2]).render(example1, buf);
Example::new(&[Ratio(1, 4); 4]).render(example2, buf);
Example::new(&[Ratio(1, 2), Ratio(1, 3), Ratio(1, 4)]).render(example3, buf);
Example::new(&[Ratio(1, 2), Percentage(25), Length(10)]).render(example4, buf);
}
fnrender_fill_example(area: Rect, buf:&mut Buffer) {
let [example1, example2, _] = Layout::vertical([Length(EXAMPLE_HEIGHT); 3]).areas(area);
Example::new(&[Fill(1), Fill(2), Fill(3)]).render(example1, buf);
Example::new(&[Fill(1), Percentage(50), Fill(1)]).render(example2, buf);
}
fnrender_min_example(area: Rect, buf:&mut Buffer) {
let [example1, example2, example3, example4, example5, _] =
Layout::vertical([Length(EXAMPLE_HEIGHT); 6]).areas(area);
Example::new(&[Percentage(100), Min(0)]).render(example1, buf);
Example::new(&[Percentage(100), Min(20)]).render(example2, buf);
Example::new(&[Percentage(100), Min(40)]).render(example3, buf);
Example::new(&[Percentage(100), Min(60)]).render(example4, buf);
Example::new(&[Percentage(100), Min(80)]).render(example5, buf);
}
fnrender_max_example(area: Rect, buf:&mut Buffer) {
let [example1, example2, example3, example4, example5, _] =
Layout::vertical([Length(EXAMPLE_HEIGHT); 6]).areas(area);
Example::new(&[Percentage(0), Max(0)]).render(example1, buf);
Example::new(&[Percentage(0), Max(20)]).render(example2, buf);
Example::new(&[Percentage(0), Max(40)]).render(example3, buf);
Example::new(&[Percentage(0), Max(60)]).render(example4, buf);
Example::new(&[Percentage(0), Max(80)]).render(example5, buf);
}
}
struct Example {
constraints: Vec<Constraint>,
}
impl Example {
fnnew(constraints:&[Constraint]) ->Self {
Self {
constraints:constraints.into(),
}
}
}
impl Widget for Example {
fnrender(self, area: Rect, buf:&mut Buffer) {
let [area, _] =
Layout::vertical([Length(ILLUSTRATION_HEIGHT), Length(SPACER_HEIGHT)]).areas(area);
letblocks= Layout::horizontal(&self.constraints).split(area);
for (block, constraint) inblocks.iter().zip(&self.constraints) {
Self::illustration(*constraint, block.width).render(*block, buf);
}
}
}
impl Example {
fnillustration(constraint: Constraint, width: u16) ->impl Widget {
letcolor=matchconstraint {
Constraint::Length(_) =>LENGTH_COLOR,
Constraint::Percentage(_) =>PERCENTAGE_COLOR,
Constraint::Ratio(_, _) =>RATIO_COLOR,
Constraint::Fill(_) =>FILL_COLOR,
Constraint::Min(_) =>MIN_COLOR,
Constraint::Max(_) =>MAX_COLOR,
};
letfg= Color::White;
lettitle=format!("{constraint}");
letcontent=format!("{width} px");
lettext=format!("{title}\n{content}");
letblock= Block::bordered()
.border_set(symbols::border::QUADRANT_OUTSIDE)
.border_style(Style::reset().fg(color).reversed())
.style(Style::default().fg(fg).bg(color));
Paragraph::new(text).centered().block(block)
}
}
```