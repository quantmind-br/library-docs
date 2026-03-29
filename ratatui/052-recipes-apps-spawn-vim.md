---
title: Spawn External Editor (Vim)
url: https://ratatui.rs/recipes/apps/spawn-vim/
source: crawler
fetched_at: 2026-02-01T21:13:19.249601892-03:00
rendered_js: false
word_count: 326
summary: This document explains how to temporarily suspend a Ratatui TUI application to execute an external command, such as a text editor, and restore the TUI state upon completion.
tags:
    - ratatui
    - rust
    - terminal-ui
    - external-process
    - vim
    - crossterm
category: tutorial
---

In this recipe, we will explore how to spawn an external editor (Vim) from within the TUI app. This example demonstrates how to temporarily exit the TUI, run an external command, and then return back to our TUI app.

Full code:

```

use ratatui::{
backend::CrosstermBackend,
crossterm::{
event::{self, Event, KeyCode, KeyEventKind},
terminal::{disable_raw_mode, enable_raw_mode, EnterAlternateScreen, LeaveAlternateScreen},
ExecutableCommand,
},
widgets::Paragraph,
DefaultTerminal, Frame,
};
use std::io::{stdout, Result};
use std::process::Command;
type Terminal = ratatui::Terminal<CrosstermBackend<std::io::Stdout>>;
enum Action {
EditFile,
Quit,
None,
}
fnmain() -> Result<()> {
letterminal= ratatui::init();
letapp_result=run(terminal);
ratatui::restore();
app_result
}
fnrun(mutterminal: DefaultTerminal) -> Result<()> {
loop {
terminal.draw(draw)?;
matchhandle_events()? {
Action::EditFile =>run_editor(&mutterminal)?,
Action::Quit =>break,
Action::None => {}
}
}
Ok(())
}
fnhandle_events() -> Result<Action> {
if!event::poll(std::time::Duration::from_millis(16))? {
return Ok(Action::None);
}
match event::read()? {
Event::Key(key) ifkey.kind == KeyEventKind::Press =>matchkey.code {
KeyCode::Char('q') => Ok(Action::Quit),
KeyCode::Char('e') => Ok(Action::EditFile),
_=> Ok(Action::None),
},
_=> Ok(Action::None),
}
}
fnrun_editor(terminal:&mut Terminal) -> Result<()> {
stdout().execute(LeaveAlternateScreen)?;
disable_raw_mode()?;
Command::new("vim").arg("/tmp/a.txt").status()?;
stdout().execute(EnterAlternateScreen)?;
enable_raw_mode()?;
terminal.clear()?;
Ok(())
}
fndraw(frame:&mut Frame) {
frame.render_widget(
Paragraph::new("Hello ratatui! (press 'q' to quit, 'e' to edit a file)"),
frame.area(),
);
}
```

First, let’s look at the main function and the event handling logic:

```

enum Action {
EditFile,
Quit,
None,
}
fnmain() -> Result<()> {
letterminal= ratatui::init();
letapp_result=run(terminal);
ratatui::restore();
app_result
}
fnrun(mutterminal: DefaultTerminal) -> Result<()> {
loop {
terminal.draw(draw)?;
matchhandle_events()? {
Action::EditFile =>run_editor(&mutterminal)?,
Action::Quit =>break,
Action::None => {}
}
}
Ok(())
}
fnhandle_events() -> Result<Action> {
if!event::poll(std::time::Duration::from_millis(16))? {
return Ok(Action::None);
}
match event::read()? {
Event::Key(key) ifkey.kind == KeyEventKind::Press =>matchkey.code {
KeyCode::Char('q') => Ok(Action::Quit),
KeyCode::Char('e') => Ok(Action::EditFile),
_=> Ok(Action::None),
},
_=> Ok(Action::None),
}
}
```

After initializing the terminal in `main` function, we enter a loop in `run` function where we draw the UI and handle events. The `handle_events` function listens for key events and returns an `Action` based on the key pressed. Here, we are calling `run_editor` function on `Action::EditFile` which we will define in next section.

Now, let’s define the function `run_editor` function attached to `Action::EditFile` action.

```

fnrun_editor(terminal:&mut Terminal) -> Result<()> {
stdout().execute(LeaveAlternateScreen)?;
disable_raw_mode()?;
Command::new("vim").arg("/tmp/a.txt").status()?;
stdout().execute(EnterAlternateScreen)?;
enable_raw_mode()?;
terminal.clear()?;
Ok(())
}
```

To spawn Vim from our TUI app, we first need to relinquish control of input and output, allowing Vim to have full control over the terminal.

The `run_editor` function handles the logic for spawning vim. First, we leave the alternate screen and disable raw mode to restore terminal to it’s original state. This part is similar to what [`ratatui::restore`](https://docs.rs/ratatui/latest/ratatui/fn.restore.html) function does in the `main` function. Next, we spawn a child process with `Command::new("vim").arg("/tmp/a.txt").status()` which launches `vim` to edit the given file. At this point, we have given up control of our TUI app to vim. Our TUI app will now wait for the exit status of the child process. Once the user exits Vim, our TUI app regains control over the terminal by re-entering alternate screen and enabling raw mode. Lastly, we clear the terminal to ensure the TUI is displayed correctly.

Running this program will display “Hello ratatui! (press ‘q’ to quit, ‘e’ to edit a file)” in the terminal. Pressing ‘e’ will spawn a child process to spawn Vim for editing a temporary file and then return to the ratatui application after Vim is closed.

Feel free to adapt this example to use other editors like `nvim`, `nano`, etc., by changing the command in the `Action::EditFile` arm.