---
title: How to Center Widgets
url: https://ratatui.rs/recipes/layout/center-a-widget/
source: crawler
fetched_at: 2026-02-01T21:13:06.884480224-03:00
rendered_js: false
word_count: 271
summary: This document explains how to center widgets within a Terminal User Interface (TUI) layout using Rect helper methods for horizontal, vertical, and bidirectional alignment.
tags:
    - ratatui
    - rust
    - tui
    - layout-alignment
    - centering-widgets
    - rect-manipulation
    - popup-dialogs
category: guide
---

You want to center a widget within some area of your TUI’s layout.

To center a widget in any area, create a [`Rect`](https://docs.rs/ratatui/latest/ratatui/struct.Rect.html) that is centered within the area. You can calculate the x and y positions of the widget by subtracting the widget width and height from the enclosing area’s width and height, respectively, and dividing by 2.

More simply, you can use the `.centered_vertically()` and `.centered_horizontally()` methods on [`Rect`](https://docs.rs/ratatui/latest/ratatui/struct.Rect.html).

### Centering horizontally

[Section titled “Centering horizontally”](#centering-horizontally)

```

use ratatui::layout::{Constraint, Rect};
fncenter_horizontal(area: Rect, width: u16) -> Rect {
area.centered_horizontally(Constraint::Length(width))
}
```

### Centering vertically

[Section titled “Centering vertically”](#centering-vertically)

```

use ratatui::layout::{Constraint, Rect};
fncenter_vertical(area: Rect, height: u16) -> Rect {
area.centered_vertically(Constraint::Length(height))
}
```

### Centering both horizontally and vertically

[Section titled “Centering both horizontally and vertically”](#centering-both-horizontally-and-vertically)

You can use the `.centered` method to get a centered `Rect`.

````

13 collapsed lines
/// Centers a [`Rect`] within another [`Rect`] using the provided [`Constraint`]s.
///
/// # Examples
///
/// ```rust
/// use ratatui::layout::{Constraint, Rect};
///
/// let area = Rect::new(0, 0, 100, 100);
/// let horizontal = Constraint::Percentage(20);
/// let vertical = Constraint::Percentage(30);
///
/// let centered = center(area, horizontal, vertical);
/// ```
fncenter(area: Rect, horizontal: Constraint, vertical: Constraint) -> Rect {
area.centered(horizontal, vertical)
}
````

### Centering a widget

[Section titled “Centering a widget”](#centering-a-widget)

You can use these methods to draw any widget centered on the containing area.

```

fnrender(frame:&mut Frame) {
lettext= Text::raw("Hello world!");
letarea=frame.area().centered(
Constraint::Length(text.width() as u16),
Constraint::Length(1),
);
frame.render_widget(text, area);
}
```

A common use case for this feature is to create a popup style dialog block. For this, typically, you’ll want to use the \[`Clear`] widget to clear the popup area before rendering your content to it. The following is an example of how you might do that:

```

fnrender_popup(frame:&mut Frame) {
letarea=frame.area().centered(
Constraint::Percentage(20),
Constraint::Length(3), // top and bottom border + content
);
letpopup= Paragraph::new("Popup content").block(Block::bordered().title("Popup"));
frame.render_widget(Clear, area);
frame.render_widget(popup, area);
}
```

Center a widget by placing it inside a `Rect` that sits in the middle of the area. Compute that rect by hand or use the `.centered`, `.centered_horizontally()`, and `.centered_vertically()` helpers on [`Rect`](https://docs.rs/ratatui/latest/ratatui/struct.Rect.html), then render the widget (popups included) into it.

Full code for this recipe is available in the website repo at: [https://github.com/ratatui/ratatui-website/blob/main/code/recipes/how-to-misc/src/layout.rs](https://github.com/ratatui/ratatui-website/blob/main/code/recipes/how-to-misc/src/layout.rs)

There are several third party widget libraries for making popups easy to use:

- [tui-popup](https://crates.io/crates/tui-popup)
- [tui-confirm-dialog](https://crates.io/crates/tui-confirm-dialog)