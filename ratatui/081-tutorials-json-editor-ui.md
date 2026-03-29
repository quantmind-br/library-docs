---
title: UI.rs
url: https://ratatui.rs/tutorials/json-editor/ui/
source: crawler
fetched_at: 2026-02-01T21:12:36.749433613-03:00
rendered_js: false
word_count: 396
summary: This document explains how to design and structure layouts within a Ratatui TUI application using frames, rectangles, and constraints. It covers partitioning screen space and implementing helper functions for responsive UI elements.
tags:
    - ratatui
    - rust-tui
    - layout-design
    - ui-components
    - terminal-interface
    - responsive-tui
category: tutorial
---

Finally we come to the last piece of the puzzle, and also the hardest part when you are just starting out creating `ratatui` TUIs --- the UI. We created a very simple UI with just one widget in the previous tutorial, but here we’ll explore some more sophisticated layouts.

Our first step is to grasp how we render widgets onto the terminal.

In essence: Widgets are constructed and then drawn onto the screen using a `Frame`, which is placed within a specified `Rect`.

Now, envision a scenario where we wish to divide our renderable `Rect` area into three distinct areas. For this, we can use the `Layout` functionality in `ratatui`.

```

letchunks= Layout::default()
.direction(Direction::Vertical)
.constraints([
Constraint::Length(3),
Constraint::Min(1),
Constraint::Length(3),
])
.split(frame.area());
```

This can be likened to partitioning a large rectangle into smaller sections.

In the example above, you can read the instructions aloud like this:

1. Take the area `f.area()` (which is a rectangle), and cut it into three vertical pieces (making horizontal cuts).
2. The first section will be 3 lines tall
3. The second section should never be smaller than one line tall, but can expand if needed.
4. The final section should also be 3 lines tall

For those visual learners, I have the following graphic:

Top segment always remains 3 lines Bottom segment is consistently 3 lines Constraint::Length 3 Middle segment maintains a minimum height of 1 line, but can expand if additional space is present. Constraint::Length &gt; 1 Constraint::Length 3

Now that we have that out of the way, let us create the TUI for our application.

## The function signature

[Section titled “The function signature”](#the-function-signature)

Our UI function needs two things to successfully create our UI elements. The `Frame` which contains the size of the terminal at render time (this is important, because it allows us to take resizable terminals into account), and the application state.

```

pubfnui(frame:&mut Frame, app:&App) {
```

Before we proceed, let’s implement a `centered_rect` helper function. This code is adapted from the [popup example](https://ratatui.rs/examples/apps/popup/).

```

/// helper function to create a centered rect using up certain percentage of the available rect `r`
fncentered_rect(percent_x: u16, percent_y: u16, r: Rect) -> Rect {
// Cut the given rectangle into three vertical pieces
letpopup_layout= Layout::default()
.direction(Direction::Vertical)
.constraints([
Constraint::Percentage((100-percent_y) /2),
Constraint::Percentage(percent_y),
Constraint::Percentage((100-percent_y) /2),
])
.split(r);
// Then cut the middle vertical piece into three width-wise pieces
Layout::default()
.direction(Direction::Horizontal)
.constraints([
Constraint::Percentage((100-percent_x) /2),
Constraint::Percentage(percent_x),
Constraint::Percentage((100-percent_x) /2),
])
.split(popup_layout[1])[1] // Return the middle chunk
}
```

This will be useful for the later subsections.