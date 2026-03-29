---
title: Layout
url: https://ratatui.rs/examples/layout/layout/
source: crawler
fetched_at: 2026-02-01T21:12:46.028802576-03:00
rendered_js: false
word_count: 496
summary: This document demonstrates how to use the Ratatui layout system to partition terminal screen space using various geometric constraints. It provides a functional implementation for organizing UI components through nested vertical and horizontal layouts.
tags:
    - ratatui
    - rust-library
    - terminal-ui
    - layout-system
    - ui-constraints
    - tui-development
category: tutorial
---

```

gitclonehttps://github.com/ratatui/ratatui.git--branchlatest
cdratatui
cargorun--example=layout--features=crossterm
```

```

//! # [Ratatui] Layout example
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
use itertools::Itertools;
use ratatui::{
crossterm::event::{self, Event, KeyCode, KeyEventKind},
layout::{
Constraint::{self, Length, Max, Min, Percentage, Ratio},
Layout, Rect,
},
style::{Color, Style, Stylize},
text::Line,
widgets::{Block, Paragraph},
DefaultTerminal, Frame,
};
fnmain() -> color_eyre::Result<()> {
color_eyre::install()?;
letterminal= ratatui::init();
letapp_result=run(terminal);
ratatui::restore();
app_result
}
fnrun(mutterminal: DefaultTerminal) -> color_eyre::Result<()> {
loop {
terminal.draw(draw)?;
iflet Event::Key(key) = event::read()? {
ifkey.kind == KeyEventKind::Press &&key.code == KeyCode::Char('q') {
break Ok(());
}
}
}
}
#[allow(clippy::too_many_lines)]
fndraw(frame:&mut Frame) {
letvertical= Layout::vertical([
Length(4),  // text
Length(50), // examples
Min(0),     // fills remaining space
]);
let [text_area, examples_area, _] =vertical.areas(frame.area());
// title
frame.render_widget(
Paragraph::new(vec![
Line::from("Horizontal Layout Example. Press q to quit".dark_gray()).centered(),
Line::from("Each line has 2 constraints, plus Min(0) to fill the remaining space."),
Line::from("E.g. the second line of the Len/Min box is [Length(2), Min(2), Min(0)]"),
Line::from("Note: constraint labels that don't fit are truncated"),
]),
text_area,
);
letexample_rows= Layout::vertical([
Length(9),
Length(9),
Length(9),
Length(9),
Length(9),
Min(0), // fills remaining space
])
.split(examples_area);
letexample_areas=example_rows.iter().flat_map(|area| {
Layout::horizontal([
Length(14),
Length(14),
Length(14),
Length(14),
Length(14),
Min(0), // fills remaining space
])
.split(*area)
.iter()
.copied()
.take(5) // ignore Min(0)
.collect_vec()
});
// the examples are a cartesian product of the following constraints
// e.g. Len/Len, Len/Min, Len/Max, Len/Perc, Len/Ratio, Min/Len, Min/Min, ...
letexamples= [
(
"Len",
[
Length(0),
Length(2),
Length(3),
Length(6),
Length(10),
Length(15),
],
),
("Min", [Min(0), Min(2), Min(3), Min(6), Min(10), Min(15)]),
("Max", [Max(0), Max(2), Max(3), Max(6), Max(10), Max(15)]),
(
"Perc",
[
Percentage(0),
Percentage(25),
Percentage(50),
Percentage(75),
Percentage(100),
Percentage(150),
],
),
(
"Ratio",
[
Ratio(0, 4),
Ratio(1, 4),
Ratio(2, 4),
Ratio(3, 4),
Ratio(4, 4),
Ratio(6, 4),
],
),
];
for ((a, b), area) inexamples
.iter()
.cartesian_product(examples.iter())
.zip(example_areas)
{
let (name_a, examples_a) =a;
let (name_b, examples_b) =b;
letconstraints=examples_a.iter().copied().zip(examples_b.iter().copied());
render_example_combination(frame, area, &format!("{name_a}/{name_b}"), constraints);
}
}
/// Renders a single example box
fnrender_example_combination(
frame:&mut Frame,
area: Rect,
title:&str,
constraints:impl ExactSizeIterator<Item = (Constraint, Constraint)>,
) {
letblock= Block::bordered()
.title(title.gray())
.style(Style::reset())
.border_style(Style::default().fg(Color::DarkGray));
letinner=block.inner(area);
frame.render_widget(block, area);
letlayout= Layout::vertical(vec![Length(1); constraints.len() +1]).split(inner);
for ((a, b), &area) inconstraints.into_iter().zip(layout.iter()) {
render_single_example(frame, area, vec![a, b, Min(0)]);
}
// This is to make it easy to visually see the alignment of the examples
// with the constraints.
frame.render_widget(Paragraph::new("123456789012"), layout[6]);
}
/// Renders a single example line
fnrender_single_example(frame:&mut Frame, area: Rect, constraints: Vec<Constraint>) {
letred= Paragraph::new(constraint_label(constraints[0])).on_red();
letblue= Paragraph::new(constraint_label(constraints[1])).on_blue();
letgreen= Paragraph::new("·".repeat(12)).on_green();
lethorizontal= Layout::horizontal(constraints);
let [r, b, g] =horizontal.areas(area);
frame.render_widget(red, r);
frame.render_widget(blue, b);
frame.render_widget(green, g);
}
fnconstraint_label(constraint: Constraint) -> String {
matchconstraint {
Constraint::Ratio(a, b) =>format!("{a}:{b}"),
Constraint::Length(n)
| Constraint::Min(n)
| Constraint::Max(n)
| Constraint::Percentage(n)
| Constraint::Fill(n) =>format!("{n}"),
}
}
```