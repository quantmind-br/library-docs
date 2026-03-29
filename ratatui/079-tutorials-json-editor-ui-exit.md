---
title: UI - Exit Popup
url: https://ratatui.rs/tutorials/json-editor/ui-exit/
source: crawler
fetched_at: 2026-02-01T21:12:39.017609384-03:00
rendered_js: false
word_count: 170
summary: This document explains how to implement an exit confirmation screen in a terminal application, specifically demonstrating the use of the Clear widget to render a centered popup for user feedback.
tags:
    - rust
    - ratatui
    - tui-development
    - terminal-interface
    - clear-widget
    - ui-layout
category: tutorial
---

We have a way for the user to view their already entered key-value pairs, and we have a way for the user to enter new ones. The last screen we need to create, is the exit/confirmation screen.

In this screen, we are asking the user if they want to output the key-value pairs they have entered in the `stdout` pipe, or close without outputting anything.

```

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
```

The only thing in this part that we haven’t done before, is use the [`Clear`](https://docs.rs/ratatui/latest/ratatui/widgets/struct.Clear.html) widget. This is a special widget that does what the name suggests --- it clears everything in the space it is rendered.