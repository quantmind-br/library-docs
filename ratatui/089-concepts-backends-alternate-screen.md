---
title: Alternate Screen
url: https://ratatui.rs/concepts/backends/alternate-screen/
source: crawler
fetched_at: 2026-02-01T21:13:03.7703786-03:00
rendered_js: false
word_count: 212
summary: This document explains the concept of the alternate screen buffer in terminal emulators, which allows TUI applications to run without disrupting the primary terminal scrollback. It provides a technical overview and a code example using Rust and Ratatui to demonstrate buffer switching.
tags:
    - terminal-ui
    - alternate-screen
    - rust
    - ratatui
    - crossterm
    - tui-development
    - buffer-management
category: concept
---

The alternate screen is a separate buffer that some terminals provide, distinct from the main screen. When activated, the terminal will display the alternate screen, hiding the current content of the main screen. Applications can write to this screen as if it were the regular terminal display, but when the application exits, the terminal will switch back to the main screen, and the contents of the alternate screen will be cleared. This is useful for applications like text editors or terminal games that want to use the full terminal window without disrupting the command line or other terminal content.

This creates a seamless transition between the application and the regular terminal session, as the content displayed before launching the application will reappear after the application exits.

Take this “hello world” program below. If we run it with and without the `std::io::stderr().execute(EnterAlternateScreen)?` (and the corresponding `LeaveAlternateScreen`), you can see how the program behaves differently.

```

17 collapsed lines
use std::{
io::{stderr, Result},
thread::sleep,
time::Duration,
};
use ratatui::crossterm::{
terminal::{EnterAlternateScreen, LeaveAlternateScreen},
ExecutableCommand,
};
use ratatui::{prelude::*, widgets::*};
fnmain() -> Result<()> {
letshould_enter_alternate_screen= std::env::args().nth(1).unwrap().parse::<bool>().unwrap();
ifshould_enter_alternate_screen {
stderr().execute(EnterAlternateScreen)?; // remove this line
}
letmutterminal= Terminal::new(CrosstermBackend::new(stderr()))?;
terminal.draw(|f| {
f.render_widget(Paragraph::new("Hello World!"), Rect::new(10, 20, 20, 1));
})?;
sleep(Duration::from_secs(2));
5 collapsed lines
ifshould_enter_alternate_screen {
stderr().execute(LeaveAlternateScreen)?; // remove this line
}
Ok(())
}
```

![](https://user-images.githubusercontent.com/1813121/272299743-f666980f-93b8-40d4-a979-1fce26d0f84a.gif)

Try running this code on your own and experiment with `EnterAlternateScreen` and `LeaveAlternateScreen`.

Note that not all terminal emulators support the alternate screen, and even those that do may handle it differently. As a result, the behavior may vary depending on the backend being used. Always consult the specific backend’s documentation to understand how it implements the alternate screen.