---
title: UI - Editing Popup
url: https://ratatui.rs/tutorials/json-editor/ui-editing/
source: crawler
fetched_at: 2026-02-01T21:12:37.346492878-03:00
rendered_js: false
word_count: 260
summary: Explains how to create and render a centered popup window with dynamic layouts and styled input widgets using the Ratatui library.
tags:
    - ratatui
    - rust
    - tui
    - ui-layout
    - popup-rendering
    - widget-styling
category: tutorial
---

Now that the `Main` screen is rendered, we now need to check if the `Editing` popup needs to be rendered. Since the `ratatui` renderer simply writes over the cells within a `Rect` on a `render_widget`, we simply need to give `render_widget` an area on top of our `Main` screen to create the appearance of a popup.

## Popup area and title

[Section titled “Popup area and title”](#popup-area-and-title)

The first thing we will do, is draw the `Block` that will contain the popup. We will give this `Block` a title to display as well to explain to the user what it is.

```

iflet Some(editing) =&app.currently_editing {
letpopup_block= Block::default()
.title("Enter a new key-value pair")
.borders(Borders::NONE)
.style(Style::default().bg(Color::DarkGray));
letarea=centered_rect(60, 25, frame.area());
frame.render_widget(popup_block, area);
```

Now that we have where our popup is going to go, we can create the layout for the popup, and create and draw the widgets inside of it.

First, we will create split the `Rect` given to us by `centered_rect`, and create a layout from it. Note the use of `margin(1)`, which gives a 1 space margin around any layout block, meaning our new blocks and widgets don’t overwrite anything from the first popup block.

```

letpopup_chunks= Layout::default()
.direction(Direction::Horizontal)
.margin(1)
.constraints([Constraint::Percentage(50), Constraint::Percentage(50)])
.split(area);
```

Now that we have the layout for where we want to display the keys and values, we will actually create the blocks and paragraphs to show what the user has already entered.

```

letmutkey_block= Block::default().title("Key").borders(Borders::ALL);
letmutvalue_block= Block::default().title("Value").borders(Borders::ALL);
letactive_style= Style::default().bg(Color::LightYellow).fg(Color::Black);
matchediting {
CurrentlyEditing::Key =>key_block=key_block.style(active_style),
CurrentlyEditing::Value =>value_block=value_block.style(active_style),
};
letkey_text= Paragraph::new(app.key_input.clone()).block(key_block);
frame.render_widget(key_text, popup_chunks[0]);
letvalue_text= Paragraph::new(app.value_input.clone()).block(value_block);
frame.render_widget(value_text, popup_chunks[1]);
}
```

Note that we are declaring the blocks as variables, and then adding extra styling to the block the user is currently editing. Then we create the `Paragraph` widgets, and assign the blocks with those variables. Also note how we used the `popup_chunks` layout instead of the `popup_block` layout to render these widgets into.