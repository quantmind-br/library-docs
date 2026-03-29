---
title: Main.rs
url: https://ratatui.rs/tutorials/json-editor/main/
source: crawler
fetched_at: 2026-02-01T21:12:35.680090812-03:00
rendered_js: false
word_count: 1140
summary: This document explains how to implement the main function and application loop in a Ratatui application, covering terminal setup, event handling, and state management.
tags:
    - ratatui
    - rust-tui
    - terminal-initialization
    - event-handling
    - main-loop
    - crossterm-backend
category: tutorial
---

The `main` file in many ratatui applications is simply a place to store the startup loop, and occasionally event handling. See more ways to handle events in [Event Handling](https://ratatui.rs/concepts/event-handling/)

In this application, we will be using our `main` function to run the startup steps, and start the main loop. We will also put our main loop logic and event handling in this file.

In our main function, we will set up the terminal, create an application state and run our application, and finally reset the terminal to the state we found it in.

### Application pre-run steps

[Section titled “Application pre-run steps”](#application-pre-run-steps)

Because a `ratatui` application takes the whole screen, and captures all of the keyboard input, we need some boilerplate at the beginning of our `main` function.

```

use ratatui::crossterm::event::EnableMouseCapture;
use ratatui::crossterm::execute;
use ratatui::crossterm::terminal::{enable_raw_mode, EnterAlternateScreen};
use std::io;
```

```

fnmain() -> Result<(), Box<dyn Error>> {
// setup terminal
enable_raw_mode()?;
letmutstderr= io::stderr(); // This is a special case. Normally using stdout is fine
execute!(stderr, EnterAlternateScreen, EnableMouseCapture)?;
// --snip--
```

You might notice that we are using `stderr` for our output. This is because we want to allow the user to pipe their completed json to other programs like `ratatui-tutorial > output.json`. To do this, we are using the fact that `stderr` is piped differently than `stdout`. We render output to `stderr`, and print our completed json to `stdout`.

For more information, please read the [crossterm documentation](https://docs.rs/crossterm/latest/crossterm/)

### State creation, and loop starting

[Section titled “State creation, and loop starting”](#state-creation-and-loop-starting)

Now that we have prepared the terminal for our application to run, it is time to actually run it.

First, we need to create an instance of our `App` to hold all of the program’s state, and then we will call our function which handles the event and draw loop.

```

// --snip--
letbackend= CrosstermBackend::new(stderr);
letmutterminal= Terminal::new(backend)?;
// create app and run it
letmutapp= App::new();
letres=run_app(&mutterminal, &mutapp);
// --snip--
```

### Application post-run steps

[Section titled “Application post-run steps”](#application-post-run-steps)

Since our `ratatui` application has changed the state of the user’s terminal with our [pre-run boilerplate](#application-pre-run-steps), we need to undo what we have done, and put the terminal back to the way we found it.

Most of these functions will simply be the inverse of what we have done above.

```

use ratatui::crossterm::event::DisableMouseCapture;
use ratatui::crossterm::terminal::{disable_raw_mode, LeaveAlternateScreen};
```

```

// --snip--
// restore terminal
disable_raw_mode()?;
execute!(
terminal.backend_mut(),
LeaveAlternateScreen,
DisableMouseCapture
)?;
terminal.show_cursor()?;
// --snip--
```

When an application exits without running this closing boilerplate, the terminal will act very strange, and the user will usually have to end the terminal session and start a new one. Thus it is important that we handle our error in such a way that we can call this last piece.

```

// --snip--
iflet Ok(do_print) =res {
ifdo_print {
app.print_json()?;
}
} elseiflet Err(err) =res {
println!("{err:?}");
}
Ok(())
}
```

The if statement at the end of boilerplate checks if the `run_app` function errored, or if it returned an `Ok` state. If it returned an `Ok` state, we need to check if we should print the json.

If we call our print function before we call `execute!(LeaveAlternateScreen)`, our prints will be rendered on an old screen and lost when we leave the alternate screen. (For more information on how this works, read the [Crossterm documentation](https://docs.rs/crossterm/latest/crossterm/terminal/struct.LeaveAlternateScreen.html))

So, altogether, our finished function should looks like this:

```

fnmain() -> Result<(), Box<dyn Error>> {
// setup terminal
enable_raw_mode()?;
letmutstderr= io::stderr(); // This is a special case. Normally using stdout is fine
execute!(stderr, EnterAlternateScreen, EnableMouseCapture)?;
letbackend= CrosstermBackend::new(stderr);
letmutterminal= Terminal::new(backend)?;
// create app and run it
letmutapp= App::new();
letres=run_app(&mutterminal, &mutapp);
// restore terminal
disable_raw_mode()?;
execute!(
terminal.backend_mut(),
LeaveAlternateScreen,
DisableMouseCapture
)?;
terminal.show_cursor()?;
iflet Ok(do_print) =res {
ifdo_print {
app.print_json()?;
}
} elseiflet Err(err) =res {
println!("{err:?}");
}
Ok(())
}
```

In this function, we will start to do the actual logic.

Let’s start with the method signature:

```

fnrun_app<B: Backend>(terminal:&mut Terminal<B>, app:&mut App) -> io::Result<bool> {
// --snip--
```

You’ll notice that we make this function generic across the `ratatui::backend::Backend`. In previous sections we hardcoded the `CrosstermBackend`. This trait approach allows us to make our code backend agnostic.

This method accepts an object of type `Terminal` which implements the `ratatui::backend::Backend` trait. This trait includes the three (four counting the `TestBackend`) officially supported backends included in `ratatui`. It allows for 3rd party backends to be implemented.

`run_app` also requires a mutable borrow to an application state object, as defined in this project.

Finally, the `run_app` returns an `io::Result<bool>` that indicates if there was an io error with the `Err` state, and an `Ok(true)` or `Ok(false)` that indicates if the program should print out the finished json.

Because `ratatui` requires us to implement our own event/ui loop, we will simply use the following code to update our main loop.

```

// --snip--
loop {
terminal.draw(|f|ui(f, app))?;
// --snip--
```

Let’s unpack that `draw` call really quick.

- `terminal` is the `Terminal<Backend>` that we take as an argument,
- `draw` is the `ratatui` command to draw a `Frame` to the terminal[1](#user-content-fn-note).
- `|f| ui(f, &app)` tells `draw` that we want to take `f: <Frame>` and pass it to our function `ui`, and `ui` will draw to that `Frame`.

Notice that we also pass an immutable borrow of our application state to the `ui` function. This will be important later.

Now that we have started our app , and have set up the UI rendering, we will implement the event handling.

Because we are using `crossterm`, we can simply poll for keyboard events with

```

iflet Event::Key(key) = event::read()? {
dbg!(key.code)
}
```

and then match the results.

Alternatively, we can set up a thread to run in the background to poll and send `Event`s, but let’s keep things simple here for the sake of illustration.

Note that the process for polling events will vary on the backend you are utilizing, and you will need to refer to the documentation of that backend for more information.

We will start with the keybinds and event handling for the `CurrentScreen::Main`.

```

// --snip--
iflet Event::Key(key) = event::read()? {
ifkey.kind == event::KeyEventKind::Release {
// Skip events that are not KeyEventKind::Press
continue;
}
matchapp.current_screen {
CurrentScreen::Main =>matchkey.code {
KeyCode::Char('e') => {
app.current_screen = CurrentScreen::Editing;
app.currently_editing = Some(CurrentlyEditing::Key);
}
KeyCode::Char('q') => {
app.current_screen = CurrentScreen::Exiting;
}
_=> {}
},
// --snip--
```

After matching to the `Main` enum variant, we match the event. When the user is in the main screen, there are only two keybinds, and the rest are ignored.

In this case, `KeyCode::Char('e')` changes the current screen to `CurrentScreen::Editing` and sets the `CurrentlyEditing` to a `Some` and notes that the user should be editing the `Key` value field, as opposed to the `Value` field.

`KeyCode::Char('q')` is straightforward, as it simply switches the application to the `Exiting` screen, and allows the ui and future event handling runs to do the rest.

The next handler we will prepare, will handle events while the application is on the `CurrentScreen::Exiting`. The job of this screen is to ask if the user wants to exit without outputting the json. It is simply a `y/n` question, so that is all we listen for. We also add an alternate exit key with `q`. If the user chooses to output the json, we return an `Ok(true)` that indicates that our `main` function should call `app.print_json()` to perform the serialization and printing for us after resetting the terminal to normal.

```

// --snip--
CurrentScreen::Exiting =>matchkey.code {
KeyCode::Char('y') => {
return Ok(true);
}
KeyCode::Char('n') | KeyCode::Char('q') => {
return Ok(false);
}
_=> {}
},
// --snip--
```

Our final handler will be a bit more involved, as we will be changing the state of internal variables.

We would like the `Enter` key to serve two purposes. When the user is editing the `Key`, we want the enter key to switch the focus to editing the `Value`. However, if the `Value` is what is being currently edited, `Enter` will save the key-value pair, and return to the `Main` screen.

```

// --snip--
CurrentScreen::Editing ifkey.kind == KeyEventKind::Press => {
matchkey.code {
KeyCode::Enter => {
iflet Some(editing) =&app.currently_editing {
matchediting {
CurrentlyEditing::Key => {
app.currently_editing = Some(CurrentlyEditing::Value);
}
CurrentlyEditing::Value => {
app.save_key_value();
app.current_screen = CurrentScreen::Main;
}
}
}
}
// --snip--
```

When `Backspace` is pressed, we need to first determine if the user is editing a `Key` or a `Value`, then `pop()` the endings of those strings accordingly.

```

// --snip--
KeyCode::Backspace => {
iflet Some(editing) =&app.currently_editing {
matchediting {
CurrentlyEditing::Key => {
app.key_input.pop();
}
CurrentlyEditing::Value => {
app.value_input.pop();
}
}
}
}
// --snip--
```

When `Escape` is pressed, we want to quit editing.

```

// --snip--
KeyCode::Esc => {
app.current_screen = CurrentScreen::Main;
app.currently_editing = None;
}
// --snip--
```

When `Tab` is pressed, we want the currently editing selection to switch.

```

// --snip--
KeyCode::Tab => {
app.toggle_editing();
}
// --snip--
```

And finally, if the user types a valid character, we want to capture that, and add it to the string that is the final key or value.

```

// --snip--
KeyCode::Char(value) => {
iflet Some(editing) =&app.currently_editing {
matchediting {
CurrentlyEditing::Key => {
app.key_input.push(value);
}
CurrentlyEditing::Value => {
app.value_input.push(value);
}
}
}
}
// --snip--
```

Altogether, the event loop should look like this:

```

// --snip--
iflet Event::Key(key) = event::read()? {
ifkey.kind == event::KeyEventKind::Release {
// Skip events that are not KeyEventKind::Press
continue;
}
matchapp.current_screen {
CurrentScreen::Main =>matchkey.code {
KeyCode::Char('e') => {
app.current_screen = CurrentScreen::Editing;
app.currently_editing = Some(CurrentlyEditing::Key);
}
KeyCode::Char('q') => {
app.current_screen = CurrentScreen::Exiting;
}
_=> {}
},
CurrentScreen::Exiting =>matchkey.code {
KeyCode::Char('y') => {
return Ok(true);
}
KeyCode::Char('n') | KeyCode::Char('q') => {
return Ok(false);
}
_=> {}
},
CurrentScreen::Editing ifkey.kind == KeyEventKind::Press => {
matchkey.code {
KeyCode::Enter => {
iflet Some(editing) =&app.currently_editing {
matchediting {
CurrentlyEditing::Key => {
app.currently_editing = Some(CurrentlyEditing::Value);
}
CurrentlyEditing::Value => {
app.save_key_value();
app.current_screen = CurrentScreen::Main;
}
}
}
}
KeyCode::Backspace => {
iflet Some(editing) =&app.currently_editing {
matchediting {
CurrentlyEditing::Key => {
app.key_input.pop();
}
CurrentlyEditing::Value => {
app.value_input.pop();
}
}
}
}
KeyCode::Esc => {
app.current_screen = CurrentScreen::Main;
app.currently_editing = None;
}
KeyCode::Tab => {
app.toggle_editing();
}
KeyCode::Char(value) => {
iflet Some(editing) =&app.currently_editing {
matchediting {
CurrentlyEditing::Key => {
app.key_input.push(value);
}
CurrentlyEditing::Value => {
app.value_input.push(value);
}
}
}
}
_=> {}
}
}
_=> {}
}
}
// --snip--
```

1. Technically this is the command to the `Terminal<Backend>`, but that only matters on the `TestBackend`. [↩](#user-content-fnref-note)