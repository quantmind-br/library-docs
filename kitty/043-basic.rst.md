---
title: Tabs and Windows
title: Tabs and Windows
word_count: 635
summary: Keyboard shortcuts and organizational hierarchy for managing windows, tabs, and OS windows in kitty terminal emulator.
optimized: true
optimized_at: 2026-05-04T20:45:41Z
---
# Tabs and Windows

kitty organizes programs hierarchically: **OS Window** (top level) > **Tab** > **kitty Window** (arranged via [[039-layouts.rst.md|Arranging windows]]). All shortcuts are [[025-mapping.rst.md|configurable]].

## Scrolling

| Action | Shortcut |
|--------|----------|
| Line up | `scroll_line_up` (also Opt+Cmd+Up, Cmd+Up on macOS) |
| Line down | `scroll_line_down` (also Opt+Cmd+Down, Cmd+Down on macOS) |
| Page up | `scroll_page_up` (also Cmd+Up on macOS) |
| Page down | `scroll_page_down` (also Cmd+Down on macOS) |
| Top | `scroll_home` (also Cmd+Home on macOS) |
| Bottom | `scroll_end` (also Cmd+End on macOS) |
| Previous shell prompt | `scroll_to_previous_prompt` (see [[041-shell-integration.rst.md|Shell integration]]) |
| Next shell prompt | `scroll_to_next_prompt` (see [[041-shell-integration.rst.md|Shell integration]]) |
| Browse scrollback in less | `show_scrollback` |
| Browse last command output | `show_last_command_output` (see [[041-shell-integration.rst.md|Shell integration]]) |
| Search scrollback in less | `search_scrollback` (also Cmd+F on macOS) |

> [!note]
> Scroll actions only work on the main screen. When the alternate screen is active (e.g., fullscreen editors), key events pass to the running program.

## Tabs

| Action | Shortcut |
|--------|----------|
| New tab | `new_tab` (also Cmd+t on macOS) |
| Close tab | `close_tab` (also Cmd+w on macOS) |
| Next tab | `next_tab` (also Shift+Ctrl+Tab, Shift+Cmd+] on macOS) |
| Previous tab | `previous_tab` (also Shift+Ctrl+Tab, Shift+Cmd+[ on macOS) |
| Next layout | `next_layout` |
| Move tab forward | `move_tab_forward` |
| Move tab backward | `move_tab_backward` |
| Set tab title | `set_tab_title` (also Shift+Cmd+i on macOS) |

## Windows

| Action | Shortcut |
|--------|----------|
| New window | `new_window` (also Cmd+Return on macOS) |
| New OS window | `new_os_window` (also Cmd+n on macOS) |
| Close window | `close_window` (also Shift+Cmd+d on macOS) |
| Resize window | `start_resizing_window` (also Cmd+r on macOS) |
| Next window | `next_window` |
| Previous window | `previous_window` |
| Move window forward | `move_window_forward` |
| Move window backward | `move_window_backward` |
| Move window to top | `move_window_to_top` |
| Visually focus window | `focus_visible_window` |
| Visually swap window | `swap_with_window` |
| Focus window 1-10 | `first_window` ... `tenth_window` (also Cmd+1...9 on macOS) |

### Vim-style window navigation

```
map ctrl+left  neighboring_window left
map shift+left  move_window right
map ctrl+down   neighboring_window down
map shift+down  move_window up
```

### Previous window

```
map ctrl+p nth_window -1
```

Negative numbers access previously active windows; positive numbers (starting from zero) access by index.

### OS window switching

`nth_os_window N` switches to the Nth OS window (positive numbers starting from one).

### Detaching windows/tabs

**Window detachment:**
```
map ctrl+f2 detach_window                  # to new OS window
map ctrl+f3 detach_window new-tab           # to new tab
map ctrl+f3 detach_window tab-prev          # to previously active tab
map ctrl+f3 detach_window new-tab-left     # to new tab on the left
map ctrl+f4 detach_window ask              # ask which tab
```

**Tab detachment:**
```
map ctrl+f2 detach_tab                     # to new OS window
map ctrl+f4 detach_tab ask                # ask which OS window
```

> [!tip]
> Tabs can be rearranged, detached, and moved via drag and drop.

### Close other windows in tab

```
map f9 close_other_windows_in_tab
```

## Other keyboard shortcuts

See [[042-actions.rst.md|Mappable actions]] for the complete list.

| Action | Shortcut |
|--------|----------|
| Show this help | `show_kitty_doc` |
| Copy to clipboard | `copy_to_clipboard` (also Cmd+c on macOS) |
| Paste from clipboard | `paste_from_clipboard` (also Cmd+v on macOS) |
| Paste from selection | `paste_from_selection` |
| Pass selection to program | `pass_selection_to_program` |
| Increase font size | `increase_font_size` (also Cmd++ on macOS) |
| Decrease font size | `decrease_font_size` (also Cmd+- on macOS) |
| Restore font size | `reset_font_size` (also Cmd+0 on macOS) |
| Toggle fullscreen | `toggle_fullscreen` (also Ctrl+Cmd+f on macOS) |
| Toggle maximized | `toggle_maximized` |
| Input Unicode character | `input_unicode_character` (also Ctrl+Cmd+Space on macOS) |
| Open URL in browser | `open_url` |
| Reset terminal | `reset_terminal` (also Opt+Cmd+r on macOS) |
| Edit kitty.conf | `edit_config_file` (also Cmd+, on macOS) |
| Reload kitty.conf | `reload_config_file` (also Ctrl+Cmd+, on macOS) |
| Debug kitty.conf | `debug_config` (also Opt+Cmd+, on macOS) |
| Open kitty shell | `kitty_shell` |
| Increase background opacity | `increase_background_opacity` |
| Decrease background opacity | `decrease_background_opacity` |
| Full background opacity | `full_background_opacity` |
| Reset background opacity | `reset_background_opacity` |

#kitty #terminal-emulator #window-management #tab-management
