---
title: Action Reference - Keybindings
url: https://ghostty.org/docs/config/keybind/reference
source: crawler
fetched_at: 2026-03-10T06:35:11.10071-03:00
rendered_js: true
word_count: 2517
summary: This document serves as a reference listing and describing all available keybinding actions within the Ghostty terminal emulator.
tags:
    - ghostty
    - keybinding
    - reference
    - actions
    - terminal-control
category: reference
---

This is a reference of all Ghostty keybinding actions.

Ignore this key combination.

Ghostty will not process this combination nor forward it to the child process within the terminal, but it may still be processed by the OS or other applications.

Unbind a previously bound key binding.

This cannot unbind bindings that were not bound by Ghostty or the user (e.g. bindings set by the OS or some other application).

Send a CSI sequence.

The value should be the CSI sequence without the CSI header (`ESC [` or `\x1b[`).

For example, `csi:0m` can be sent to reset all styles of the current text.

Send an `ESC` sequence.

Send the specified text.

Uses Zig string literal syntax. This is currently not validated. If the text is invalid (i.e. contains an invalid escape sequence), the error will currently only show up in logs.

Send data to the pty depending on whether cursor key mode is enabled (`application`) or disabled (`normal`).

Reset the terminal.

This can fix a lot of issues when a running program puts the terminal into a broken state, equivalent to running the `reset` command.

If you do this while in a TUI program such as vim, this may break the program. If you do this while in a shell, you may have to press enter after to get a new prompt.

Copy the selected text to the clipboard.

Paste the contents of the default clipboard.

Paste the contents of the selection clipboard.

If there is a URL under the cursor, copy it to the default clipboard.

Copy the terminal title to the clipboard. If the terminal title is not set or is empty this has no effect.

Increase the font size by the specified amount in points (pt).

For example, `increase_font_size:1.5` will increase the font size by 1.5 points.

Decrease the font size by the specified amount in points (pt).

For example, `decrease_font_size:1.5` will decrease the font size by 1.5 points.

Reset the font size to the original configured size.

Set the font size to the specified size in points (pt).

For example, `set_font_size:14.5` will set the font size to 14.5 points.

Start a search for the given text. If the text is empty, then the search is canceled. A canceled search will not disable any GUI elements showing search. For that, the explicit end\_search binding should be used.

If a previous search is active, it is replaced.

Start a search for the current text selection. If there is no selection, this does nothing. If a search is already active, this changes the search terms.

Navigate the search results. If there is no active search, this is not performed.

Start a search if it isn't started already. This doesn't set any search terms, but opens the UI for searching.

End the current search if any and hide any GUI elements.

Clear the screen and all scrollback.

Select all text on the screen.

Scroll to the top of the screen.

Scroll to the bottom of the screen.

Scroll to the selected text.

Scroll to the given absolute row in the screen with 0 being the first row.

Scroll the screen up by one page.

Scroll the screen down by one page.

Scroll the screen by the specified fraction of a page.

Positive values scroll downwards, and negative values scroll upwards.

For example, `scroll_page_fractional:0.5` would scroll the screen downwards by half a page, while `scroll_page_fractional:-1.5` would scroll it upwards by one and a half pages.

Scroll the screen by the specified amount of lines.

Positive values scroll downwards, and negative values scroll upwards.

For example, `scroll_page_lines:3` would scroll the screen downwards by 3 lines, while `scroll_page_lines:-10` would scroll it upwards by 10 lines.

Adjust the current selection in the given direction or position, relative to the cursor.

WARNING: This does not create a new selection, and does nothing when there currently isn't one.

Valid arguments are:

- `left`, `right`
  
  Adjust the selection one cell to the left or right respectively.
- `up`, `down`
  
  Adjust the selection one line upwards or downwards respectively.
- `page_up`, `page_down`
  
  Adjust the selection one page upwards or downwards respectively.
- `home`, `end`
  
  Adjust the selection to the top-left or the bottom-right corner of the screen respectively.
- `beginning_of_line`, `end_of_line`
  
  Adjust the selection to the beginning or the end of the line respectively.

Jump the viewport forward or back by the given number of prompts.

Requires shell integration.

Positive values scroll downwards, and negative values scroll upwards.

Write the entire scrollback into a temporary file with the specified action. The action determines what to do with the filepath.

Valid actions are:

- `copy`
  
  Copy the file path into the clipboard.
- `paste`
  
  Paste the file path into the terminal.
- `open`
  
  Open the file in the default OS editor for text files.
  
  The default OS editor is determined by using `open` on macOS and `xdg-open` on Linux.

Write the contents of the screen into a temporary file with the specified action.

See `write_scrollback_file` for possible actions.

Write the currently selected text into a temporary file with the specified action.

See `write_scrollback_file` for possible actions.

Does nothing when no text is selected.

Open a new window.

If the application isn't currently focused, this will bring it to the front.

Open a new tab.

Go to the previous tab.

Go to the next tab.

Go to the last tab.

Go to the tab with the specific index, starting from 1.

If the tab number is higher than the number of tabs, this will go to the last tab.

Moves a tab by a relative offset.

Positive values move the tab forwards, and negative values move it backwards. If the new position is out of bounds, it is wrapped around cyclically within the tab list.

For example, `move_tab:1` moves the tab one position forwards, and if it was already the last tab in the list, it wraps around and becomes the first tab in the list. Likewise, `move_tab:-1` moves the tab one position backwards, and if it was the first tab, then it will become the last tab.

Toggle the tab overview.

This is only supported on Linux and when the system's libadwaita version is 1.4 or newer. The current libadwaita version can be found by running `ghostty +version`.

Change the title of the current focused surface via a pop-up prompt.

Change the title of the current tab via a pop-up prompt. The title set via this prompt overrides any title set by the terminal and persists across focus changes within the tab.

Create a new split in the specified direction.

Valid arguments:

- `right`, `down`, `left`, `up`
  
  Creates a new split in the corresponding direction.
- `auto`
  
  Creates a new split along the larger direction. For example, if the parent split is currently wider than it is tall, then a left-right split would be created, and vice versa.

Focus on a split either in the specified direction (`right`, `down`, `left` and `up`), or in the adjacent split in the order of creation (`previous` and `next`).

Focus on either the previous window or the next one ('previous', 'next')

Zoom in or out of the current split.

When a split is zoomed into, it will take up the entire space in the current tab, hiding other splits. The tab or tab bar would also reflect this by displaying an icon indicating the zoomed state.

Toggle read-only mode for the current surface.

When a surface is in read-only mode:

- No input is sent to the PTY (mouse events, key encoding)
- Input can still be used at the terminal level to make selections, copy/paste (keybinds), scroll, etc.
- Warn before quit is always enabled in this state even if an active process is not running

Resize the current split in the specified direction and amount in pixels. The two arguments should be joined with a comma (`,`), like in `resize_split:up,10`.

Equalize the size of all splits in the current window.

Reset the window to the default size. The "default size" is the size that a new window would be created with. This has no effect if the window is fullscreen.

Only implemented on macOS.

Control the visibility of the terminal inspector.

Valid arguments: `toggle`, `show`, `hide`.

Show the GTK inspector.

Has no effect on macOS.

Show the on-screen keyboard if one is present.

Only implemented on Linux (GTK). On GNOME, the "Screen Keyboard" accessibility feature must be turned on, which can be found under Settings &gt; Accessibility &gt; Typing. Other platforms are as of now untested.

Open the configuration file in the default OS editor.

If your default OS editor isn't configured then this will fail. Currently, any failures to open the configuration will show up only in the logs.

Reload the configuration.

The exact meaning depends on the app runtime in use, but this usually involves re-reading the configuration file and applying any changes Note that not all changes can be applied at runtime.

Close the current "surface", whether that is a window, tab, split, etc.

This might trigger a close confirmation popup, depending on the value of the `confirm-close-surface` configuration setting.

Close the current tab and all splits therein, close all other tabs, or close every tab to the right of the current one depending on the mode.

If the mode is not specified, defaults to closing the current tab.

This might trigger a close confirmation popup, depending on the value of the `confirm-close-surface` configuration setting.

Close the current window and all tabs and splits therein.

This might trigger a close confirmation popup, depending on the value of the `confirm-close-surface` configuration setting.

Close all windows.

WARNING: This action has been deprecated and has no effect on either Linux or macOS. Users are instead encouraged to use `all:close_window` instead.

Maximize or unmaximize the current window.

This has no effect on macOS as it does not have the concept of maximized windows.

Fullscreen or unfullscreen the current window.

Toggle window decorations (titlebar, buttons, etc.) for the current window.

Only implemented on Linux.

Toggle whether the terminal window should always float on top of other windows even when unfocused.

Terminal windows always start as normal (not float-on-top) windows.

Only implemented on macOS.

Toggle secure input mode.

This is used to prevent apps from monitoring your keyboard input when entering passwords or other sensitive information.

This applies to the entire application, not just the focused terminal. You must manually untoggle it or quit Ghostty entirely to disable it.

Only implemented on macOS, as this uses a built-in system API.

Toggle mouse reporting on or off.

When mouse reporting is disabled, mouse events will not be reported to terminal applications even if they request it. This allows you to always use the mouse for selection and other terminal UI interactions without applications capturing mouse input.

This can also be controlled via the `mouse-reporting` configuration option.

Toggle the command palette.

The command palette is a popup that lets you see what actions you can perform, their associated keybindings (if any), a search bar to filter the actions, and the ability to then execute the action.

This requires libadwaita 1.5 or newer on Linux. The current libadwaita version can be found by running `ghostty +version`.

Toggle the quick terminal.

The quick terminal, also known as the "Quake-style" or drop-down terminal, is a terminal window that appears on demand from a keybinding, often sliding in from a screen edge such as the top. This is useful for quick access to a terminal without having to open a new window or tab.

The terminal state is preserved between appearances, so showing the quick terminal after it was already hidden would display the same window instead of creating a new one.

As quick terminals are often useful when other windows are currently focused, they are best used with *global* keybinds. For example, one can define the following key bind to toggle the quick terminal from anywhere within the system by pressing ``Cmd+` ``:

```ini
keybind = global:cmd+backquote=toggle_quick_terminal
```

The quick terminal has some limitations:

- Only one quick terminal instance can exist at a time.
- Unlike normal terminal windows, the quick terminal will not be restored when the application is restarted on systems that support window restoration like macOS.
- On Linux, the quick terminal is only supported on Wayland and not X11, and only on Wayland compositors that support the `wlr-layer-shell-v1` protocol. In practice, this means that only GNOME users would not be able to use this feature.
- On Linux, slide-in animations are only supported on KDE, and when the "Sliding Popups" KWin plugin is enabled.
  
  If you do not have this plugin enabled, open System Settings &gt; Apps & Windows &gt; Window Management &gt; Desktop Effects, and enable the plugin in the plugin list. Ghostty would then need to be restarted fully for this to take effect.
- Quick terminal tabs are only supported on Linux and not on macOS. This is because tabs on macOS require a title bar.
- On macOS, a fullscreened quick terminal will always be in non-native fullscreen mode. This is a requirement due to how the quick terminal is rendered.

See the various configurations for the quick terminal in the configuration file to customize its behavior.

Show or hide all windows. If all windows become shown, we also ensure Ghostty becomes focused. When hiding all windows, focus is yielded to the next application as determined by the OS.

Note: When the focused surface is fullscreen, this method does nothing.

Only implemented on macOS.

Toggle the window background opacity between transparent and opaque.

This does nothing when `background-opacity` is set to 1 or above.

When `background-opacity` is less than 1, this action will either make the window transparent or not depending on its current transparency state.

Only implemented on macOS.

Check for updates.

Only implemented on macOS.

Undo the last undoable action for the focused surface or terminal, if possible. This can undo actions such as closing tabs or windows.

Not every action in Ghostty can be undone or redone. The list of actions support undo/redo is currently limited to:

- New window, close window
- New tab, close tab
- New split, close split

All actions are only undoable/redoable for a limited time. For example, restoring a closed split can only be done for some number of seconds since the split was closed. The exact amount is configured with the `undo-timeout` configuration settings.

The undo/redo actions being limited ensures that there is bounded memory usage over time, closed surfaces don't continue running in the background indefinitely, and the keybinds become available for terminal applications to use.

Only implemented on macOS.

Redo the last undoable action for the focused surface or terminal, if possible. See "undo" for more details on what can and cannot be undone or redone.

End the currently active key sequence, if any, and flush the keys up to this point to the terminal, excluding the key that triggered this action.

For example: `ctrl+w>escape=end_key_sequence` would encode `ctrl+w` to the terminal and exit the key sequence.

Normally, an invalid sequence will reset the key sequence and flush all data including the invalid key. This action allows you to flush only the prior keys, which is useful when you want to bind something like a control key (`ctrl+w`) but not send additional inputs.