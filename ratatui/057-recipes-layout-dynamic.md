---
title: Create Dynamic layouts
url: https://ratatui.rs/recipes/layout/dynamic/
source: crawler
fetched_at: 2026-02-01T21:13:11.203288819-03:00
rendered_js: false
word_count: 51
summary: This document explains how to programmatically generate and update terminal user interface layouts based on application state and user input.
tags:
    - rust
    - tui
    - layout-management
    - dynamic-ui
    - ratatui
    - state-handling
category: guide
---

With real world applications, the content can often be dynamic. For example, a chat application may need to resize the chat input area based on the number of incoming messages. To achieve this, you can generate layouts dynamically:

```

fnget_layout_based_on_messages(msg_count: usize, f:&Frame) -> Rc<[Rect]> {
letmsg_percentage=ifmsg_count>50 { 80 } else { 50 };
Layout::default()
.direction(Direction::Vertical)
.constraints([
Constraint::Percentage(msg_percentage),
Constraint::Percentage(100-msg_percentage),
])
.split(f.area())
}
```

You can even update the layout based on some user input or command:

```

matchaction {
Action::IncreaseSize => {
current_percentage+=5;
ifcurrent_percentage>95 {
current_percentage=95;
}
},
Action::DecreaseSize => {
current_percentage-=5;
ifcurrent_percentage<5 {
current_percentage=5;
}
},
_=> {}
}
letchunks= Layout::default()
.direction(Direction::Horizontal)
.constraints([
Constraint::Percentage(current_percentage),
Constraint::Percentage(100-current_percentage),
])
.split(f.area());
```