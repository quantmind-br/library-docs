---
title: Grid Layout
url: https://ratatui.rs/recipes/layout/grid/
source: crawler
fetched_at: 2026-02-01T21:13:07.26850178-03:00
rendered_js: false
word_count: 101
summary: This document explains how to implement a grid-based widget layout in a TUI application by combining horizontal and vertical constraints. It demonstrates using Layout methods and iterator patterns to split a rectangular area into a grid of cells.
tags:
    - tui-layout
    - grid-layout
    - ratatui
    - rust-programming
    - widget-rendering
category: guide
---

You want to create a grid layout for your TUI application, where widgets are arranged in a grid-like structure.

To create a grid layout, you can use the `Layout` struct to define the horizontal and vertical constraints of the rows and columns. Combine these constraints with iterator methods to create a grid layout.

Given the following grid struct:

```

struct Grid {
cols: usize,
rows: usize,
}
```

With the following render method:

```

impl Widget for Grid {
fnrender(self, area: Rect, buf:&mut Buffer) {
letcol_constraints= (0..self.cols).map(|_| Constraint::Length(9));
letrow_constraints= (0..self.rows).map(|_| Constraint::Length(3));
lethorizontal= Layout::horizontal(col_constraints).spacing(1);
letvertical= Layout::vertical(row_constraints).spacing(1);
letrows=vertical.split(area);
letcells=rows.iter().flat_map(|&row|horizontal.split(row).to_vec());
for (i, cell) incells.enumerate() {
Paragraph::new(format!("Area {:02}", i+1))
.block(Block::bordered())
.render(cell, buf);
}
}
}
```

The output will look like this:

```

┌───────┐ ┌───────┐ ┌───────┐ ┌───────┐
│Area 01│ │Area 02│ │Area 03│ │Area 04│
└───────┘ └───────┘ └───────┘ └───────┘
┌───────┐ ┌───────┐ ┌───────┐ ┌───────┐
│Area 05│ │Area 06│ │Area 07│ │Area 08│
└───────┘ └───────┘ └───────┘ └───────┘
┌───────┐ ┌───────┐ ┌───────┐ ┌───────┐
│Area 09│ │Area 10│ │Area 11│ │Area 12│
└───────┘ └───────┘ └───────┘ └───────┘
┌───────┐ ┌───────┐ ┌───────┐ ┌───────┐
│Area 13│ │Area 14│ │Area 15│ │Area 16│
└───────┘ └───────┘ └───────┘ └───────┘
```

In Ratatui 0.30, we introduce a few [new methods on Rect](https://github.com/ratatui/ratatui/pull/1909), which removes the need to bind rows to satisfy the borrow checker, and simplifies this to a single line of code:

```

letcells=area.layout_vec(&vertical).iter().flat_map(|row|row.layout_vec(&horizontal));
```