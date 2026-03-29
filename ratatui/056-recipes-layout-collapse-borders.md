---
title: Collapse borders in a layout
url: https://ratatui.rs/recipes/layout/collapse-borders/
source: crawler
fetched_at: 2026-02-01T21:13:09.512844417-03:00
rendered_js: false
word_count: 139
summary: This document explains how to create seamless terminal user interfaces by collapsing adjacent widget borders using Ratatui's border merging features. It provides a step-by-step guide on using overlapping layouts and merge strategies to handle complex border joining logic.
tags:
    - ratatui
    - rust-tui
    - layout-management
    - border-merging
    - terminal-ui
    - widget-styling
category: tutorial
---

A common layout for applications is to split up the screen into panes, with borders around each pane. Often this leads to making UIs that look disconnected. E.g., the following layout:

![problem](https://user-images.githubusercontent.com/381361/279935613-01b5083d-dcca-4ee3-981c-38fe700bbfe4.png)

Created by the following code:

```

fndraw(frame:&mut Frame) {
// create a layout that splits the screen into 2 equal columns and the right column
// into 2 equal rows
let [left, right] = Layout::horizontal([Constraint::Fill(1); 2]).areas(frame.area());
let [top_right, bottom_right] = Layout::vertical([Constraint::Fill(1); 2]).areas(right);
frame.render_widget(Block::bordered().title("Left Block"), left);
frame.render_widget(Block::bordered().title("Top Right Block"), top_right);
frame.render_widget(Block::bordered().title("Bottom Right Block"), bottom_right);
}
```

We can do better though, by collapsing borders. E.g.:

![solution](https://user-images.githubusercontent.com/381361/279935618-3b411b45-1a02-4f4c-af9f-7b68f766023e.png)

Starting with Ratatui 0.30, collapsing borders has become much easier thanks to the new `merge_borders` method and `Spacing::Overlap`. The recipe is simple:

1. Import `Spacing` and `MergeStrategy`.
   
   ```
   
   use ratatui::{
   layout::{Constraint, Layout, Spacing},
   symbols::merge::MergeStrategy,
   widgets::Block,
   DefaultTerminal, Frame,
   };
   ```
2. Use `Spacing::Overlap(1)` in your layout to make borders overlap.
   
   ```
   
   // Use Spacing::Overlap(1) to make the borders overlap
   let [left, right] = Layout::horizontal([Constraint::Fill(1); 2])
   .spacing(Spacing::Overlap(1))
   .areas(frame.area());
   let [top_right, bottom_right] = Layout::vertical([Constraint::Fill(1); 2])
   .spacing(Spacing::Overlap(1))
   .areas(right);
   ```
3. Add `.merge_borders(MergeStrategy::Exact)` to your blocks to automatically merge borders (see [`MergeStrategy` documentation](https://docs.rs/ratatui/latest/ratatui/symbols/merge/enum.MergeStrategy.html#variants) for details about the different strategies).
   
   ```
   
   // Use merge_borders(MergeStrategy::Exact) to automatically handle border merging
   letleft_block= Block::bordered()
   .title("Left Block")
   .merge_borders(MergeStrategy::Exact);
   lettop_right_block= Block::bordered()
   .title("Top Right Block")
   .merge_borders(MergeStrategy::Exact);
   letbottom_right_block= Block::bordered()
   .title("Bottom Right Block")
   .merge_borders(MergeStrategy::Exact);
   ```

Setting `merge_borders` to `MergeStrategy::Exact` or `MergeStrategy::Fuzzy` automatically handles all the complex border joining logic. The `Spacing::Overlap(1)` ensures that adjacent borders occupy the same space, allowing them to be merged.

The full code for this example is available at [https://github.com/ratatui/ratatui-website/blob/main/code/recipes/how-to-collapse-borders](https://github.com/ratatui/ratatui-website/blob/main/code/recipes/how-to-collapse-borders)

```

use std::time::Duration;
use color_eyre::Result;
use ratatui::crossterm::event::{self, Event};
use ratatui::{
layout::{Constraint, Layout, Spacing},
symbols::merge::MergeStrategy,
widgets::Block,
DefaultTerminal, Frame,
};
/// This example shows how to use the new Ratatui v0.30 border merging feature to collapse borders
/// between widgets.
/// See https://ratatui.rs/how-to/layout/collapse-borders for more info
fnmain() -> Result<()> {
color_eyre::install()?;
letterminal= ratatui::init();
letresult=run(terminal);
ratatui::restore();
result
}
fnrun(mutterminal: DefaultTerminal) -> Result<()> {
loop {
terminal.draw(draw)?;
ifkey_pressed()? {
return Ok(());
}
}
}
fnkey_pressed() -> Result<bool> {
Ok(event::poll(Duration::from_millis(16))?&&matches!(event::read()?, Event::Key(_)))
}
fndraw(frame:&mut Frame) {
// create a layout that splits the screen into 2 equal columns and the right column
// into 2 equal rows
// Use Spacing::Overlap(1) to make the borders overlap
let [left, right] = Layout::horizontal([Constraint::Fill(1); 2])
.spacing(Spacing::Overlap(1))
.areas(frame.area());
let [top_right, bottom_right] = Layout::vertical([Constraint::Fill(1); 2])
.spacing(Spacing::Overlap(1))
.areas(right);
// Use merge_borders(MergeStrategy::Exact) to automatically handle border merging
letleft_block= Block::bordered()
.title("Left Block")
.merge_borders(MergeStrategy::Exact);
lettop_right_block= Block::bordered()
.title("Top Right Block")
.merge_borders(MergeStrategy::Exact);
letbottom_right_block= Block::bordered()
.title("Bottom Right Block")
.merge_borders(MergeStrategy::Exact);
frame.render_widget(left_block, left);
frame.render_widget(top_right_block, top_right);
frame.render_widget(bottom_right_block, bottom_right);
}
```