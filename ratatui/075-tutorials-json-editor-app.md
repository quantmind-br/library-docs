---
title: App.rs
url: https://ratatui.rs/tutorials/json-editor/app/
source: crawler
fetched_at: 2026-02-01T21:12:35.998451174-03:00
rendered_js: false
word_count: 609
summary: This document explains how to structure application state and manage different navigation modes in a Ratatui application using Rust structs and enums.
tags:
    - ratatui
    - rust
    - state-management
    - tui-development
    - application-architecture
category: tutorial
---

As we saw in the previous section, a common model for smaller `ratatui` applications is to have one application state struct called `App` or some variant of that name. We will be using this paradigm in this application as well.

This struct will contain all of our “persistent” data and will be passed to any function that needs to know the current state of the application.

## Application modes

[Section titled “Application modes”](#application-modes)

It is useful to think about the several “modes” that your application can be in. Thinking in “modes” will make it easier to segregate everything from what window is getting drawn, to what keybinds to listen for.

We will be using the application’s state to track two things:

1. what screen the user is seeing,
2. which box should be highlighted, the “key” or “value” (this only applies when the user is editing a key-value pair).

### Current Screen Enum

[Section titled “Current Screen Enum”](#current-screen-enum)

In this tutorial application, we will have three “screens”:

- `Main`: the main summary screen showing all past key-value pairs entered
- `Editing`: the screen shown when the user wishes to create a new key-value pair
- `Exiting`: displays a prompt asking if the user wants to output the key-value pairs they have entered.

We represent these possible modes with a simple enum:

```

pubenum CurrentScreen {
Main,
Editing,
Exiting,
}
```

### Currently Editing Enum

[Section titled “Currently Editing Enum”](#currently-editing-enum)

As you may already know, `ratatui` does not automatically redraw the screen[1](#user-content-fn-note). `ratatui` also does not remember anything about what it drew last frame.

This means that the programmer is responsible for handling all state and updating widgets to reflect changes. In this case, we will allow the user to input two strings in the `Editing` mode - a key and a value. The programmer is responsible for knowing which the user is trying to edit.

For this purpose, we will create another enum for our application state called `CurrentlyEditing` to keep track of which field the user is currently entering:

```

pubenum CurrentlyEditing {
Key,
Value,
}
```

## The full application state

[Section titled “The full application state”](#the-full-application-state)

Now that we have enums to help us track where the user is, we will create the struct that actually stores this data which can be passed around where it is needed.

```

pubstruct App {
pubkey_input: String,              // the currently being edited json key.
pubvalue_input: String,            // the currently being edited json value.
pubpairs: HashMap<String, String>, // The representation of our key and value pairs with serde Serialize support
pubcurrent_screen: CurrentScreen, // the current screen the user is looking at, and will later determine what is rendered.
pubcurrently_editing: Option<CurrentlyEditing>, // the optional state containing which of the key or value pair the user is editing. It is an option, because when the user is not directly editing a key-value pair, this will be set to `None`.
}
```

While we could simply keep our application state as simply a holder of values, we can also create a few helper functions which will make our life easier elsewhere. Of course, these functions should only affect the application state itself, and nothing outside of it.

We will be adding this function simply to make creating the state easier. While this could be avoided by specifying it all in the instantiation of the variable, doing it here allows for easy to change universal defaults for the state.

```

impl App {
pubfnnew() -> App {
App {
key_input: String::new(),
value_input: String::new(),
pairs: HashMap::new(),
current_screen: CurrentScreen::Main,
currently_editing: None,
}
}
// --snip--
```

This function will be called when the user saves a key-value pair in the editor. It adds the two stored variables to the key-value pairs `HashMap`, and resets the status of all of the editing variables.

```

// --snip--
pubfnsave_key_value(&mutself) {
self.pairs
.insert(self.key_input.clone(), self.value_input.clone());
self.key_input = String::new();
self.value_input = String::new();
self.currently_editing = None;
}
// --snip--
```

Sometimes it is easier to put simple logic into a convenience function so we don’t have to worry about it in the main code block. `toggle_editing` is one of those cases. All we are doing, is checking if something is currently being edited, and if it is, swapping between editing the Key and Value fields.

```

// --snip--
pubfntoggle_editing(&mutself) {
iflet Some(edit_mode) =&self.currently_editing {
matchedit_mode {
CurrentlyEditing::Key =>self.currently_editing = Some(CurrentlyEditing::Value),
CurrentlyEditing::Value =>self.currently_editing = Some(CurrentlyEditing::Key),
};
} else {
self.currently_editing = Some(CurrentlyEditing::Key);
}
}
// --snip--
```

Finally, is another convenience function to print out the serialized json from all of our key-value pairs.

```

// --snip--
pubfnprint_json(&self) -> serde_json::Result<()> {
letoutput= serde_json::to_string(&self.pairs)?;
println!("{output}");
Ok(())
}
// --snip--
```

1. In ratatui, every frame draws the UI anew. See the [Rendering section](https://ratatui.rs/concepts/rendering/) for more information. [↩](#user-content-fnref-note)