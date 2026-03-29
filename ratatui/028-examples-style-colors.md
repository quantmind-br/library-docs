---
title: Colors
url: https://ratatui.rs/examples/style/colors/
source: crawler
fetched_at: 2026-02-01T21:12:46.959971679-03:00
rendered_js: false
word_count: 856
summary: This document demonstrates how to use and display the full range of colors supported by the Ratatui library, including named, indexed, and grayscale variants.
tags:
    - ratatui
    - rust-tui
    - terminal-colors
    - ui-styling
    - crossterm
    - color-palette
category: tutorial
---

```

gitclonehttps://github.com/ratatui/ratatui.git--branchlatest
cdratatui
cargorun--example=colors--features=crossterm
```

```

//! # [Ratatui] Colors example
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
// This example shows all the colors supported by ratatui. It will render a grid of foreground
// and background colors with their names and indexes.
use color_eyre::Result;
use itertools::Itertools;
use ratatui::{
crossterm::event::{self, Event, KeyCode, KeyEventKind},
layout::{Alignment, Constraint, Layout, Rect},
style::{Color, Style, Stylize},
text::Line,
widgets::{Block, Borders, Paragraph},
DefaultTerminal, Frame,
};
fnmain() -> Result<()> {
color_eyre::install()?;
letterminal= ratatui::init();
letapp_result=run(terminal);
ratatui::restore();
app_result
}
fnrun(mutterminal: DefaultTerminal) -> Result<()> {
loop {
terminal.draw(draw)?;
iflet Event::Key(key) = event::read()? {
ifkey.kind == KeyEventKind::Press &&key.code == KeyCode::Char('q') {
return Ok(());
}
}
}
}
fndraw(frame:&mut Frame) {
letlayout= Layout::vertical([
Constraint::Length(30),
Constraint::Length(17),
Constraint::Length(2),
])
.split(frame.area());
render_named_colors(frame, layout[0]);
render_indexed_colors(frame, layout[1]);
render_indexed_grayscale(frame, layout[2]);
}
constNAMED_COLORS: [Color; 16] = [
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
fnrender_named_colors(frame:&mut Frame, area: Rect) {
letlayout= Layout::vertical([Constraint::Length(3); 10]).split(area);
render_fg_named_colors(frame, Color::Reset, layout[0]);
render_fg_named_colors(frame, Color::Black, layout[1]);
render_fg_named_colors(frame, Color::DarkGray, layout[2]);
render_fg_named_colors(frame, Color::Gray, layout[3]);
render_fg_named_colors(frame, Color::White, layout[4]);
render_bg_named_colors(frame, Color::Reset, layout[5]);
render_bg_named_colors(frame, Color::Black, layout[6]);
render_bg_named_colors(frame, Color::DarkGray, layout[7]);
render_bg_named_colors(frame, Color::Gray, layout[8]);
render_bg_named_colors(frame, Color::White, layout[9]);
}
fnrender_fg_named_colors(frame:&mut Frame, bg: Color, area: Rect) {
letblock=title_block(format!("Foreground colors on {bg} background"));
letinner=block.inner(area);
frame.render_widget(block, area);
letvertical= Layout::vertical([Constraint::Length(1); 2]).split(inner);
letareas=vertical.iter().flat_map(|area| {
Layout::horizontal([Constraint::Ratio(1, 8); 8])
.split(*area)
.to_vec()
});
for (fg, area) inNAMED_COLORS.into_iter().zip(areas) {
letcolor_name=fg.to_string();
letparagraph= Paragraph::new(color_name).fg(fg).bg(bg);
frame.render_widget(paragraph, area);
}
}
fnrender_bg_named_colors(frame:&mut Frame, fg: Color, area: Rect) {
letblock=title_block(format!("Background colors with {fg} foreground"));
letinner=block.inner(area);
frame.render_widget(block, area);
letvertical= Layout::vertical([Constraint::Length(1); 2]).split(inner);
letareas=vertical.iter().flat_map(|area| {
Layout::horizontal([Constraint::Ratio(1, 8); 8])
.split(*area)
.to_vec()
});
for (bg, area) inNAMED_COLORS.into_iter().zip(areas) {
letcolor_name=bg.to_string();
letparagraph= Paragraph::new(color_name).fg(fg).bg(bg);
frame.render_widget(paragraph, area);
}
}
fnrender_indexed_colors(frame:&mut Frame, area: Rect) {
letblock=title_block("Indexed colors".into());
letinner=block.inner(area);
frame.render_widget(block, area);
letlayout= Layout::vertical([
Constraint::Length(1), // 0 - 15
Constraint::Length(1), // blank
Constraint::Min(6),    // 16 - 123
Constraint::Length(1), // blank
Constraint::Min(6),    // 124 - 231
Constraint::Length(1), // blank
])
.split(inner);
//    0   1   2   3   4   5    6   7   8   9  10  11   12  13  14  15
letcolor_layout= Layout::horizontal([Constraint::Length(5); 16]).split(layout[0]);
foriin0..16 {
letcolor= Color::Indexed(i);
letcolor_index=format!("{i:0>2}");
letbg=ifi<1 { Color::DarkGray } else { Color::Black };
letparagraph= Paragraph::new(Line::from(vec![
color_index.fg(color).bg(bg),
"██".bg(color).fg(color),
]));
frame.render_widget(paragraph, color_layout[ias usize]);
}
//   16  17  18  19  20  21   52  53  54  55  56  57   88  89  90  91  92  93
//   22  23  24  25  26  27   58  59  60  61  62  63   94  95  96  97  98  99
//   28  29  30  31  32  33   64  65  66  67  68  69  100 101 102 103 104 105
//   34  35  36  37  38  39   70  71  72  73  74  75  106 107 108 109 110 111
//   40  41  42  43  44  45   76  77  78  79  80  81  112 113 114 115 116 117
//   46  47  48  49  50  51   82  83  84  85  86  87  118 119 120 121 122 123
//
//  124 125 126 127 128 129  160 161 162 163 164 165  196 197 198 199 200 201
//  130 131 132 133 134 135  166 167 168 169 170 171  202 203 204 205 206 207
//  136 137 138 139 140 141  172 173 174 175 176 177  208 209 210 211 212 213
//  142 143 144 145 146 147  178 179 180 181 182 183  214 215 216 217 218 219
//  148 149 150 151 152 153  184 185 186 187 188 189  220 221 222 223 224 225
//  154 155 156 157 158 159  190 191 192 193 194 195  226 227 228 229 230 231
// the above looks complex but it's so the colors are grouped into blocks that display nicely
letindex_layout= [layout[2], layout[4]]
.iter()
// two rows of 3 columns
.flat_map(|area| {
Layout::horizontal([Constraint::Length(27); 3])
.split(*area)
.to_vec()
})
// each with 6 rows
.flat_map(|area| {
Layout::vertical([Constraint::Length(1); 6])
.split(area)
.to_vec()
})
// each with 6 columns
.flat_map(|area| {
Layout::horizontal([Constraint::Min(4); 6])
.split(area)
.to_vec()
})
.collect_vec();
foriin16..=231 {
letcolor= Color::Indexed(i);
letcolor_index=format!("{i:0>3}");
letparagraph= Paragraph::new(Line::from(vec![
color_index.fg(color).bg(Color::Reset),
".".bg(color).fg(color),
// There's a bug in VHS that seems to bleed backgrounds into the next
// character. This is a workaround to make the bug less obvious.
"███".reversed(),
]));
frame.render_widget(paragraph, index_layout[ias usize -16]);
}
}
fntitle_block(title: String) -> Block<'static> {
Block::new()
.borders(Borders::TOP)
.title_alignment(Alignment::Center)
.border_style(Style::new().dark_gray())
.title_style(Style::new().reset())
.title(title)
}
fnrender_indexed_grayscale(frame:&mut Frame, area: Rect) {
letlayout= Layout::vertical([
Constraint::Length(1), // 232 - 243
Constraint::Length(1), // 244 - 255
])
.split(area)
.iter()
.flat_map(|area| {
Layout::horizontal([Constraint::Length(6); 12])
.split(*area)
.to_vec()
})
.collect_vec();
foriin232..=255 {
letcolor= Color::Indexed(i);
letcolor_index=format!("{i:0>3}");
// make the dark colors easier to read
letbg=ifi<244 { Color::Gray } else { Color::Black };
letparagraph= Paragraph::new(Line::from(vec![
color_index.fg(color).bg(bg),
"██".bg(color).fg(color),
// There's a bug in VHS that seems to bleed backgrounds into the next
// character. This is a workaround to make the bug less obvious.
"███████".reversed(),
]));
frame.render_widget(paragraph, layout[ias usize -232]);
}
}
```