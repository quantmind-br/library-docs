---
title: Popups (overwrite regions)
url: https://ratatui.rs/recipes/render/overwrite-regions/
source: crawler
fetched_at: 2026-02-01T21:13:15.964360435-03:00
rendered_js: false
word_count: 179
summary: This document explains how to use the Clear widget in Ratatui to prevent background styles and symbols from bleeding through into foreground widgets. It demonstrates how to properly implement popups by clearing the rendering area before drawing new content.
tags:
    - ratatui
    - rust-tui
    - clear-widget
    - rendering-buffer
    - popup-window
    - terminal-graphics
category: tutorial
---

Ratatui renders text in the order that the application writes to the buffer. This means that earlier instructions will be overwritten by later ones. However, it’s important to note that widgets do not always clear every cell in the area that they are rendering to. This may cause symbols and styles that were previously rendered to the buffer to “bleed” through into the cells that are rendered on top of those cells.

The following code exhibits this problem:

```

use lipsum::lipsum;
use ratatui::{
backend::CrosstermBackend,
crossterm::{
event::{self, Event},
terminal::{disable_raw_mode, enable_raw_mode, EnterAlternateScreen, LeaveAlternateScreen},
ExecutableCommand,
},
layout::Rect,
style::{Style, Stylize},
widgets::{Block, Borders, Paragraph, Wrap},
Frame, Terminal,
};
// -- snip --
fnui(frame:&mut Frame) {
letarea=frame.area();
letbackground_text= Paragraph::new(lipsum(1000))
.wrap(Wrap { trim:true })
.light_blue()
.italic()
.on_black();
frame.render_widget(background_text, area);
// take up a third of the screen vertically and half horizontally
letpopup_area= Rect {
x:area.width /4,
y:area.height /3,
width:area.width /2,
height:area.height /3,
};
letbad_popup= Paragraph::new("Hello world!")
.wrap(Wrap { trim:true })
.style(Style::new().yellow())
.block(
Block::new()
.title("Without Clear")
.title_style(Style::new().white().bold())
.borders(Borders::ALL)
.border_style(Style::new().red()),
);
frame.render_widget(bad_popup, popup_area);
}
```

![problem](https://github.com/ratatui/ratatui-website/assets/381361/a32bd6e2-9704-4054-b41d-a34715fc217f)

Notice that the background color (black in this case), the italics, and the lorem ipsum background text show through the popup.

This problem is easy to prevent by rendering a [`Clear`](https://docs.rs/ratatui/latest/ratatui/widgets/struct.Clear.html) widget prior to rendering the main popup. Here is an example of how to use this technique to create a `Popup` widget:

```

use derive_setters::Setters;
use lipsum::lipsum;
use ratatui::{
backend::CrosstermBackend,
buffer::Buffer,
crossterm::{
event::{self, Event},
terminal::{disable_raw_mode, enable_raw_mode, EnterAlternateScreen, LeaveAlternateScreen},
ExecutableCommand,
},
layout::Rect,
style::{Style, Stylize},
text::{Line, Text},
widgets::{Block, Borders, Clear, Paragraph, Widget, Wrap},
Frame, Terminal,
};
#[derive(Debug, Default, Setters)]
struct Popup<'a> {
#[setters(into)]
title: Line<'a>,
#[setters(into)]
content: Text<'a>,
border_style: Style,
title_style: Style,
style: Style,
}
impl Widget for Popup<'_> {
fnrender(self, area: Rect, buf:&mut Buffer) {
// ensure that all cells under the popup are cleared to avoid leaking content
Clear.render(area, buf);
letblock= Block::new()
.title(self.title)
.title_style(self.title_style)
.borders(Borders::ALL)
.border_style(self.border_style);
Paragraph::new(self.content)
.wrap(Wrap { trim:true })
.style(self.style)
.block(block)
.render(area, buf);
}
}
```

We can use the new `Popup` widget with the following code:

```

letpopup= Popup::default()
.content("Hello world!")
.style(Style::new().yellow())
.title("With Clear")
.title_style(Style::new().white().bold())
.border_style(Style::new().red());
frame.render_widget(popup, popup_area);
```

Which results in the following:

![demo](https://github.com/ratatui/ratatui-website/assets/381361/39e92dad-8127-4588-8361-45d2f95abf32)

Notice that the background is set to the default background and there are no italics or symbols from the background text.

Full source for this article is available at [https://github.com/ratatui/ratatui-website/tree/main/code/recipes/how-to-overwrite-regions](https://github.com/ratatui/ratatui-website/tree/main/code/recipes/how-to-overwrite-regions)