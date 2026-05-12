---
title: Keyboard shortcuts | Warp
url: https://docs.warp.dev/getting-started/keyboard-shortcuts
source: sitemap
fetched_at: 2026-04-29T15:02:10.005236085-03:00
rendered_js: false
word_count: 767
summary: This document provides instructions on how to view, manage, and customize keyboard shortcuts within the Warp terminal, including a comprehensive list of available command actions.
tags:
    - warp-terminal
    - keyboard-shortcuts
    - keybindings
    - productivity
    - terminal-settings
category: guide
optimized: true
optimized_at: 2026-04-29T20:15:00Z
---
# Keyboard Shortcuts

Warp displays a shortcut screen on launch. Dismiss it with the **X** button. View shortcuts via the [[101-terminal-command-palette]] or Resource Center keyboard shortcut sidebar.

## Custom Keyboard Shortcuts

Navigate to **Settings** > **Keyboard shortcuts** to set custom shortcuts, clear conflicts, or search actions.

Remap using a keyset file — see the [keysets repository](https://github.com/warpdotdev/keysets/tree/main) for instructions.

> [!warning]
> Conflicting keybinds display with an orange border.

![keybinds that conflict with others are highlighted in orange](https://docs.warp.dev/~gitbook/image?url=https%3A%2F%2F4009768362-files.gitbook.io%2F~%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FPsjNxoJ0NFCXW6rRdHH3%252Fuploads%252Fgit-blob-b1deaff708f95fdb8ebffe491a823ccea24bac6c%252Fkeybinds-conflict.png%3Falt%3Dmedia&width=768&dpr=3&quality=100&sign=58413821&sv=2)

## All Available Shortcuts

### Warp Essentials

| Action | Shortcut |
|--------|----------|
| Launch Configuration Palette | `workspace:toggle_launch_config_palette` |
| Show Theme Chooser | `workspace:show_theme_chooser` |
| Show Command Search | `workspace:show_command_search` |
| Natural Language Command Search | `input:toggle_natural_language_command_search` |
| Trigger Subshell Bootstrap | `terminal:trigger_subshell_bootstrap` |
| Toggle Warp Drive | `terminal:toggle_warp_drive` |

### Blocks

| Action | Shortcut |
|--------|----------|
| Select Closest Bookmark Down | `terminal:select_bookmark_down` |
| Select Closest Bookmark Up | `terminal:select_bookmark_up` |
| Select All Blocks | `terminal:select_all_blocks` |
| Bookmark Selected Block | `terminal:bookmark_selected_block` |
| Select Next Block | `terminal:select_next_block` |
| Reinput Selected Commands | `terminal:reinput_commands` |
| Select Previous Block | `terminal:select_previous_block` |
| Open Block List Context Menu | `terminal:open_block_list_context_menu_via_keybinding` |
| Reinput as Root | `terminal:reinput_commands_with_sudo` |
| Open Share Modal | `terminal:open_share_modal` |
| Expand Selected Blocks Below | `terminal:expand_block_selection_below` |
| Expand Selected Blocks Above | `terminal:expand_block_selection_above` |

### Scrolling

| Action | Shortcut |
|--------|----------|
| Scroll to Top of Selected Block | `terminal:scroll_to_top_of_selected_block` |
| Scroll to Bottom of Selected Block | `terminal:scroll_to_bottom_of_selected_block` |
| Scroll Terminal Output Up One Line | `terminal:scroll_up_one_line` |
| Scroll Terminal Output Down One Line | `terminal:scroll_down_one_line` |

> [!info]
> "Scroll Terminal Output Up/Down One Line" has no default keybinding. Assign one in Settings > Keyboard shortcuts or trigger via [[101-terminal-command-palette]]. During long-running commands, `PAGE UP`, `PAGE DOWN`, `HOME`, and `END` forward to the running program.

### Input Editor

| Action | Shortcut |
|--------|----------|
| Fold Selected Ranges | `editor_view:fold_selected_ranges` |
| Delete All Left | `editor_view:delete_all_left` |
| Delete All Right | `editor_view:delete_all_right` |
| Move Cursor to Bottom | `editor_view:move_to_line_start` |
| Move Cursor to Top | `editor_view:move_to_line_end` |
| Move Cursor Right / Accept Autosuggestion | `editor_view:move_forward_one_character` |
| Add Selection for Next Occurrence | `editor_view:add_next_occurrence` |
| Remove Previous Character | `editor_view:remove_last_character` |
| Insert Newline | `editor_view:insert_newline` |
| Cut All Right | `editor_view:cut_all_right` |
| Select to Line Start | `editor_view:select_to_line_start` |
| Select One Character Left | `editor_view:add_cursor_below` |
| Select to Line End | `editor:select_to_line_end` |
| Select One Character Right | `editor_view:add_cursor_above` |
| Copy and Clear Selected Lines | `editor_view:clear_and_copy_lines` |
| Cut Word Left | `editor_view:cut_word_left` |
| Insert Last Word of Previous Command | `editor:insert_last_word_previous_command` |
| Move to Paragraph Start | `editor_view:move_to_paragraph_start` |
| Move Backward One Word | `editor_view:move_backward_one_word` |
| Cut Word Right | `editor_view:cut_word_right` |
| Move to Paragraph End | `editor_view:move_to_paragraph_end` |
| Move Forward One Word | `editor_view:move_forward_one_word` |
| Move Backward One Subword | `editor_view:move_backward_one_subword` |
| Move Forward One Subword | `editor_view:move_forward_one_subword` |
| Move to Buffer Start | `editor_view:move_to_buffer_start` |
| Move to Buffer End | `editor_view:move_to_buffer_end` |
| Select One Word Left | `editor_view:select_left_by_word` |
| Select One Word Right | `editor_view:select_right_by_word` |

### Terminal

| Action | Shortcut |
|--------|----------|
| Navigate Right Pane | `pane_group:navigate_right` |
| Set Concise Accessibility Announcements | `workspace:set_a11y_concise_verbosity_level` |
| Set Verbose Accessibility Announcements | `workspace:set_a11y_verbose_verbosity_level` |
| Show Settings Modal | `workspace:show_settings_modal` |
| Show Settings Account Page | `workspace:show_settings_account_page` |
| Find Next Occurrence | `find:find_next_occurrence` |
| Toggle Command Palette | `workspace:toggle_command_palette` |
| Toggle Mouse Reporting | `workspace:toggle_mouse_reporting` |
| Show Keybinding Settings | `workspace:show_keybinding_settings` |
| Toggle Resource Center | `workspace:toggle_resource_center` |
| Toggle Maximize Active Pane | `pane_group:toggle_maximize_pane` |
| Find Previous Occurrence | `find:find_prev_occurrence` |
| Toggle Navigation Palette | `workspace:toggle_navigation_palette` |

### Fundamentals

| Action | Shortcut |
|--------|----------|
| Decrease Font Size | `workspace:decrease_font_size` |
| Reset Font Size | `workspace:reset_font_size` |
| Increase Font Size | `workspace:increase_font_size` |
| Activate First Tab | `workspace:activate_first_tab` |
| Activate Second Tab | `workspace:activate_second_tab` |
| Activate Third Tab | `workspace:activate_third_tab` |
| Activate Fourth Tab | `workspace:activate_fourth_tab` |
| Activate Fifth Tab | `workspace:activate_fifth_tab` |
| Activate Sixth Tab | `workspace:activate_sixth_tab` |
| Activate Seventh Tab | `workspace:activate_seventh_tab` |
| Activate Eighth Tab | `workspace:activate_eighth_tab` |
| Activate Last Tab | `workspace:activate_last_tab` |
| Reopen Closed Tab | `workspace:reopen_closed_tab` |
| Activate Previous Tab | `workspace:activate_prev_tab` |
| Activate Next Tab | `workspace:activate_next_tab` |

#keyboard-shortcuts #warp-terminal #productivity