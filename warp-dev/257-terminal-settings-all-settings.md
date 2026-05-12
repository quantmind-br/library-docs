---
title: All settings reference | Warp
url: https://docs.warp.dev/terminal/settings/all-settings
source: sitemap
fetched_at: 2026-04-29T15:02:56.718758499-03:00
rendered_js: false
word_count: 3676
summary: Complete reference of Warp terminal configuration settings in TOML format, organized by section.
tags:
    - warp-terminal
    - toml-configuration
    - settings-reference
    - terminal-customization
    - appearance-settings
category: reference
optimized: true
optimized_at: 2026-04-29T00:00:00Z
---
This page lists every configurable setting in [`settings.toml`](https://docs.warp.dev/terminal/settings) organized by TOML section. Only include settings you want to change — Warp uses built-in defaults for everything else.

## General

Top-level settings controlling Warp startup, session management, and window preferences.

**Section**: `[general]`

| Setting | Type | Default | Description |
|---------|------|---------|-------------|
| `default_session_mode` | string | `"terminal"` | Default mode for new sessions. Options: `"terminal"`, `"agent"`, `"cloud_agent"`, `"tab_config"`, `"docker_sandbox"` |
| `default_tab_config_path` | string | `""` | Path to tab config when `default_session_mode` is `"tab_config"` |
| `link_tooltip` | boolean | `true` | Show tooltip on link hover |
| `login_item` | boolean | `true` | Launch Warp on login |
| `mouse_scroll_multiplier` | number | `3.0` | Scroll speed multiplier |
| `new_tab_placement` | string | `"after_current_tab"` | Where new tabs are placed. Options: `"after_current_tab"`, `"after_all_tabs"` |
| `quit_on_last_window_closed` | boolean | `false` | Quit Warp when last window closes |
| `restore_session` | boolean | `true` | Restore previous session on startup |
| `should_confirm_close_session` | boolean | `true` | Show confirmation on session close |
| `show_changelog_after_update` | boolean | `true` | Show changelog after update |
| `show_warning_before_quitting` | boolean | `true` | Show warning before quitting |
| `snackbar_enabled` | boolean | `true` | Show snackbar notifications |
| `user_native_preference` | string | `"not_selected"` | Prefer native or web app. Options: `"not_selected"`, `"web"`, `"desktop"` |

### Undo close

**Section**: `[general.undo_close]`

| Setting | Type | Default | Description |
|---------|------|---------|-------------|
| `enabled` | boolean | `true` | Enable undo close feature |
| `grace_period` | integer | `60` | Seconds after closing a tab to undo |

## Appearance

Visual settings for themes, fonts, cursor, tabs, window, and layout.

**Section**: `[appearance]`

| Setting | Type | Default | Description |
|---------|------|---------|-------------|
| `spacing` | string | `"normal"` | Spacing between blocks. Options: `"normal"`, `"compact"` |

### Themes

**Section**: `[appearance.themes]`

| Setting | Type | Default | Description |
|---------|------|---------|-------------|
| `theme` | string | `"dark"` | Color theme. Options: `"adeberry"`, `"phenomenon"`, `"dark"`, `"dracula"`, `"fancy_dracula"`, `"cyber_wave"`, `"solar_flare"`, `"solarized_dark"`, `"willow_dream"`, `"light"`, `"dark_city"`, `"gruvbox_dark"`, `"red_rock"`, `"jelly_fish"`, `"leafy"`, `"koi"`, `"solarized_light"`, `"snowy"`, `"gruvbox_light"`, `"pink_city"`, `"marble"`, or custom theme object |
| `system_theme` | boolean | `false` | Match system light/dark theme |
| `selected_system_themes` | object | `{ dark = "dark", light = "light" }` | Themes for system light/dark modes |

### Text

**Section**: `[appearance.text]`

| Setting | Type | Default | Description |
|---------|------|---------|-------------|
| `font_name` | string | `"Hack"` | Monospace font for terminal |
| `font_size` | number | `13.0` | Font size |
| `font_weight` | string | `"normal"` | Font weight. Options: `"thin"` through `"black"` |
| `line_height_ratio` | number | `1.2` | Line height ratio |
| `ligature_rendering_enabled` | boolean | `false` | Render font ligatures |
| `ai_font_name` | string | `"Hack"` | Font for AI-generated content |
| `match_ai_font` | boolean | `false` | AI font matches terminal font |
| `notebook_font_size` | number | `14.0` | Font size in notebooks |
| `match_notebook_to_monospace_font_size` | boolean | `true` | Notebook font size matches terminal |
| `use_thin_strokes` | string | `"on_high_dpi_displays"` | Thin font strokes on macOS. Options: `"never"`, `"on_low_dpi_displays"`, `"on_high_dpi_displays"`, `"always"` |
| `enforce_minimum_contrast` | string | `"only_named_colors"` | Minimum contrast enforcement. Options: `"never"`, `"only_named_colors"`, `"always"` |

### Cursor

**Section**: `[appearance.cursor]`

| Setting | Type | Default | Description |
|---------|------|---------|-------------|
| `cursor_display_type` | string | `"bar"` | Cursor style. Options: `"bar"`, `"block"`, `"underline"` |
| `cursor_blink` | string | `"enabled"` | Cursor blink. Options: `"enabled"`, `"disabled"` |

### Blocks

**Section**: `[appearance.blocks]`

| Setting | Type | Default | Description |
|---------|------|---------|-------------|
| `show_block_dividers` | boolean | `true` | Show dividers between blocks |
| `show_jump_to_bottom_of_block_button` | boolean | `true` | Show jump-to-bottom button in long output |
| `should_show_bootstrap_block` | boolean | `false` | Show bootstrap block |
| `should_show_in_band_command_blocks` | boolean | `false` | Show in-band command blocks |
| `should_show_ssh_block` | boolean | `false` | Show SSH connection block |

### Tabs

**Section**: `[appearance.tabs]`

| Setting | Type | Default | Description |
|---------|------|---------|-------------|
| `workspace_decoration_visibility` | string | `"hide_fullscreen"` | When tab bar is visible. Options: `"always_show"`, `"hide_fullscreen"`, `"on_hover"` |
| `tab_close_button_position` | string | `"right"` | Close button position. Options: `"right"`, `"left"` |
| `show_indicators_button` | boolean | `true` | Show activity indicators on tabs |
| `preserve_active_tab_color` | boolean | `false` | Preserve active tab color on switch |
| `header_toolbar_chip_selection` | string/object | `"default"` | Header toolbar chip config |

### Vertical tabs

**Section**: `[appearance.vertical_tabs]`

| Setting | Type | Default | Description |
|---------|------|---------|-------------|
| `enabled` | boolean | `false` | Display tabs vertically |
| `view_mode` | string | `"compact"` | Display mode. Options: `"compact"`, `"expanded"` |
| `primary_info` | string | `"command"` | Primary info on tabs. Options: `"command"`, `"working_directory"`, `"branch"` |
| `compact_subtitle` | string | `"branch"` | Subtitle for compact view. Options: `"branch"`, `"working_directory"`, `"command"` |
| `display_granularity` | string | `"panes"` | Row granularity. Options: `"panes"`, `"tabs"` |
| `tab_item_mode` | string | `"focused_session"` | Tab item mode. Options: `"focused_session"`, `"summary"` |
| `show_details_on_hover` | boolean | `true` | Show details sidecar on hover |
| `show_diff_stats` | boolean | `true` | Show diff stats |
| `show_pr_link` | boolean | `true` | Show PR links |
| `use_latest_prompt_as_title` | boolean | `false` | Use latest prompt as tab name |

### Panes

**Section**: `[appearance.panes]`

| Setting | Type | Default | Description |
|---------|------|---------|-------------|
| `focus_pane_on_hover` | boolean | `false` | Focus pane on hover |
| `should_dim_inactive_panes` | boolean | `false` | Dim inactive panes |

### Input position

**Section**: `[appearance.input]`

| Setting | Type | Default | Description |
|---------|------|---------|-------------|
| `input_mode` | string | `"pinned_to_bottom"` | Terminal input position. Options: `"pinned_to_bottom"`, `"pinned_to_top"`, `"waterfall"` |

### Full-screen apps

**Section**: `[appearance.full_screen_apps]`

| Setting | Type | Default | Description |
|---------|------|---------|-------------|
| `alt_screen_padding` | string/object | `{ custom = { uniform_padding = 0.0 } }` | Padding around full-screen apps |

### Icon

**Section**: `[appearance.icon]`

| Setting | Type | Default | Description |
|---------|------|---------|-------------|
| `app_icon` | string | `"default"` | Dock icon. Options: `"default"`, `"aurora"`, `"classic1"`, `"classic2"`, `"classic3"`, `"comets"`, `"cow"`, `"glass_sky"`, `"glitch"`, `"glow"`, `"holographic"`, `"mono"`, `"neon"`, `"original"`, `"starburst"`, `"sticker"`, `"warp_one"` |

### Window

**Section**: `[appearance.window]`

| Setting | Type | Default | Description |
|---------|------|---------|-------------|
| `override_opacity` | integer | `100` | Window background opacity (1-100) |
| `override_blur` | integer | `1` | Blur radius for window |
| `override_blur_texture` | boolean | `false` | Apply blur texture |
| `zoom_level` | integer | `100` | Zoom level as percentage |
| `open_windows_at_custom_size` | boolean | `false` | Open new windows at custom size |
| `new_windows_num_columns` | integer | `80` | Columns for new custom-size windows |
| `new_windows_num_rows` | integer | `40` | Rows for new custom-size windows |
| `left_panel_visibility_across_tabs` | boolean | `true` | Share left panel visibility across tabs |

## Terminal

Settings controlling terminal behavior, input, and event handling.

**Section**: `[terminal]`

| Setting | Type | Default | Description |
|---------|------|---------|-------------|
| `copy_on_select` | boolean | `true` | Auto-copy text on selection |
| `focus_reporting_enabled` | boolean | `true` | Forward focus/blur to full-screen apps |
| `mouse_reporting_enabled` | boolean | `true` | Forward mouse events to full-screen apps |
| `scroll_reporting_enabled` | boolean | `true` | Forward scroll events to full-screen apps |
| `maximum_grid_size` | integer | `50000` | Max terminal grid rows |
| `use_audible_bell` | boolean | `false` | Play bell sound on terminal bell |
| `show_terminal_zero_state_block` | boolean | `true` | Show AI zero-state block in new sessions |

### Input

**Section**: `[terminal.input]`

| Setting | Type | Default | Description |
|---------|------|---------|-------------|
| `syntax_highlighting` | boolean | `true` | Syntax highlighting in input |
| `honor_ps1` | boolean | `false` | Use shell's PS1 instead of Warp prompt |
| `input_box_type_setting` | string | `"classic"` | Input style. Options: `"universal"` (AI-first), `"classic"` (terminal-first) |
| `alias_expansion_enabled` | boolean | `false` | Enable shell alias expansion |
| `command_corrections` | boolean | `true` | Suggest corrections for mistyped commands |
| `error_underlining_enabled` | boolean | `true` | Underline command errors |
| `completions_open_while_typing` | boolean | `false` | Auto-open completions menu |
| `classic_completions_mode` | boolean | `false` | Enable classic completions mode |
| `show_hint_text` | boolean | `true` | Show hint text in input |
| `show_terminal_input_message_bar` | boolean | `true` | Show terminal input message bar |
| `enable_slash_commands_in_terminal` | boolean | `true` | Enable slash commands |
| `at_context_menu_in_terminal_mode` | boolean | `true` | Enable @ context menu in terminal mode |
| `outline_codebase_symbols_for_at_context_menu` | boolean | `true` | Show codebase symbols in @ menu |
| `middle_click_paste_enabled` | boolean | `true` | Middle-click pastes from clipboard |
| `extra_meta_keys` | object | `{ left_alt = false, right_alt = false }` | Additional meta keys |

#### Autosuggestions

**Section**: `[terminal.input.autosuggestions]`

| Setting | Type | Default | Description |
|---------|------|---------|-------------|
| `enabled` | boolean | `true` | Show command autosuggestions |
| `keybinding_hint` | boolean | `true` | Display keybinding hints |
| `show_ignore_button` | boolean | `false` | Show ignore button |

### Smart select

**Section**: `[terminal.smart_select]`

| Setting | Type | Default | Description |
|---------|------|---------|-------------|
| `enabled` | boolean | `true` | Double-click smart selection for URLs, emails, file paths |
| `word_char_allowlist` | string | `"-.~/\\"` | Characters considered part of a word when smart select disabled |

## Session

Settings controlling shell selection and working directory for new sessions.

**Section**: `[session]`

| Setting | Type | Default | Description |
|---------|------|---------|-------------|
| `startup_shell_override` | string/null | `null` | Shell for Warp startup. Options: `"system_default"`, `{ executable = "/path/to/shell" }`, `{ custom = "command" }` |
| `new_session_shell_override` | string/object/null | `null` | Shell for new sessions |

### Working directory config

**Section**: `[session.working_directory_config]`

| Setting | Type | Default | Description |
|---------|------|---------|-------------|
| `advanced_mode` | boolean | `false` | Separate settings per session source |

When `advanced_mode` is `false`, `[session.working_directory_config.global]` applies to all sources. When `true`, configure each source independently.

**Section**: `[session.working_directory_config.global]` (also `.split_pane`, `.new_tab`, `.new_window`)

| Setting | Type | Default | Description |
|---------|------|---------|-------------|
| `mode` | string | `"previous_dir"` | Working directory source. Options: `"home_dir"`, `"previous_dir"`, `"custom_dir"` |
| `custom_dir` | string | `""` | Custom directory path (when mode is `"custom_dir"`) |

## Agents

Settings for Warp agents including model behavior, permissions, knowledge, MCP servers, and voice.

**Section**: `[agents]`

| Setting | Type | Default | Description |
|---------|------|---------|-------------|
| `cloud_conversation_storage_enabled` | boolean | `true` | Store conversations in cloud |

### Knowledge

**Section**: `[agents.knowledge]`

| Setting | Type | Default | Description |
|---------|------|---------|-------------|
| `rules_enabled` | boolean | `true` | Agent uses saved rules |
| `warp_drive_context_enabled` | boolean | `true` | Include Warp Drive context in AI requests |

### MCP servers

**Section**: `[agents.mcp_servers]`

| Setting | Type | Default | Description |
|---------|------|---------|-------------|
| `file_based_mcp_enabled` | boolean | `false` | Auto-detect third-party file-based MCP servers |

### Profiles (permissions)

**Section**: `[agents.profiles]`

| Setting | Type | Default | Description |
|---------|------|---------|-------------|
| `agent_mode_coding_permissions` | string | `"always_ask_before_reading"` | File read permission level. Options: `"always_ask_before_reading"`, `"always_allow_reading"`, `"allow_reading_specific_files"` |
| `agent_mode_coding_file_read_allowlist` | array | `[]` | File paths agent can read without permission |
| `agent_mode_execute_readonly_commands` | boolean | `false` | Auto-execute read-only commands without asking |
| `agent_mode_command_execution_allowlist` | array | `["cat(\\s.*)?", "echo(\\s.*)?", "find .*", "grep(\\s.*)?", "ls(\\s.*)?", "which .*"]` | Commands agent can execute without permission (regex) |
| `agent_mode_command_execution_denylist` | array | `["bash(\\s.*)?", "fish(\\s.*)?", "pwsh(\\s.*)?", "sh(\\s.*)?", "zsh(\\s.*)?", "curl(\\s.*)?", "eval(\\s.*)?", "exec(\\s.*)?", "source(\\s.*)?", "wget(\\s.*)?", "dig(\\s.*)?", "nslookup(\\s.*)?", "host(\\s.*)?", "ssh(\\s.*)?", "scp(\\s.*)?", "rsync(\\s.*)?", "telnet(\\s.*)?", "rm(\\s.*)?"]` | Commands agent must always ask before executing (regex) |

### Warp Agent (AI features)

**Section**: `[agents.warp_agent]`

| Setting | Type | Default | Description |
|---------|------|---------|-------------|
| `is_any_ai_enabled` | boolean | `true` | Enable all AI features |

#### Active AI

**Section**: `[agents.warp_agent.active_ai]`

| Setting | Type | Default | Description |
|---------|------|---------|-------------|
| `enabled` | boolean | `true` | Enable proactive AI features |
| `code_suggestions_enabled` | boolean | `true` | Enable AI code suggestions |
| `intelligent_autosuggestions_enabled` | boolean | `true` | Enable AI-powered intelligent autosuggestions |
| `agent_mode_query_suggestions_enabled` | boolean | `true` | Show prompt suggestions in Agent Mode |
| `shared_block_title_generation_enabled` | boolean | `true` | Auto-generate titles when sharing blocks |

#### Input

**Section**: `[agents.warp_agent.input]`

| Setting | Type | Default | Description |
|---------|------|---------|-------------|
| `ai_auto_detection_enabled` | boolean | `true` | Auto-detect natural language input |
| `ai_command_denylist` | string | `""` | Commands excluded from AI detection |
| `nld_in_terminal_enabled` | boolean | `false` | Enable natural language detection in terminal |
| `show_model_selectors_in_prompt` | boolean | `true` | Show AI model selectors |
| `show_agent_tips` | boolean | `true` | Show agent tips |
| `include_agent_commands_in_history` | boolean | `false` | Include agent-executed commands in history |
| `agent_toolbar_chip_selection_setting` | string/object | `"default"` | Layout of context chips in Agent Mode toolbar |

#### Other

**Section**: `[agents.warp_agent.other]`

| Setting | Type | Default | Description |
|---------|------|---------|-------------|
| `thinking_display_mode` | string | `"show_and_collapse"` | How thinking traces display. Options: `"show_and_collapse"`, `"always_show"`, `"never_show"` |
| `open_conversation_layout_preference` | string | `"new_tab"` | Open agent conversations in new tab or split. Options: `"new_tab"`, `"split_pane"` |
| `show_conversation_history` | boolean | `true` | Show conversation history in tools panel |
| `show_agent_notifications` | boolean | `true` | Show agent notifications |
| `should_show_oz_updates_in_zero_state` | boolean | `true` | Show "What's new" in agent view |
| `should_render_use_agent_toolbar_for_user_commands` | boolean | `true` | Show "Use Agent" footer for terminal commands |
| `cloud_agent_computer_use_enabled` | boolean | `false` | Enable computer use for cloud agent |

### Code review autogeneration

Controls AI autogeneration in code review dialogs.

**Section**: `[agents.oz.active_ai]`

| Setting | Type | Default | Description |
|---------|------|---------|-------------|
| `git_operations_autogen_enabled` | boolean | `true` | Auto-generate commit messages and PR title/body |

### Third-party (CLI agents)

**Section**: `[agents.third_party]`

| Setting | Type | Default | Description |
|---------|------|---------|-------------|
| `should_render_cli_agent_toolbar` | boolean | `true` | Show CLI agent footer |
| `auto_toggle_composer` | boolean | `true` | Auto close/reopen Rich Input based on blocked state |
| `auto_open_composer_on_cli_agent_start` | boolean | `false` | Auto-open Rich Input when CLI agent starts |
| `auto_dismiss_composer_after_submit` | boolean | `false` | Auto-close Rich Input after submit |
| `cli_agent_toolbar_chip_selection_setting` | string/object | `"default"` | Layout of context chips in CLI Agent toolbar |
| `cli_agent_toolbar_enabled_commands` | object | `{}` | Map custom toolbar commands to CLI agents |

### Voice

**Section**: `[agents.voice]`

| Setting | Type | Default | Description |
|---------|------|---------|-------------|
| `voice_input_enabled` | boolean | `true` | Enable voice input for AI |
| `voice_input_toggle_key` | string | `"none"` | Key to toggle voice input. Options: `"none"`, `"fn"`, `"alt_left"`, `"alt_right"`, `"control_left"`, `"control_right"`, `"super_left"`, `"super_right"`, `"shift_left"`, `"shift_right"` |

## Code

Settings for Warp's code editor, file handling, and codebase indexing.

**Section**: `[code.editor]`

| Setting | Type | Default | Description |
|---------|------|---------|-------------|
| `open_file_editor` | string/object | `"system_default"` | Editor for opening files. Options: `"system_default"`, `"warp"`, `"env_editor"`, or external editor object. Supported: VS Code, VS Code Insiders, PyCharm, IntelliJ IDEA, CLion, RustRover, Sublime Text 4, Zed, Cursor, Windsurf |
| `open_code_panels_file_editor` | string/object | `"warp"` | Editor for opening files from code panels |
| `open_file_layout` | string | `"split_pane"` | Layout when opening files. Options: `"split_pane"`, `"new_tab"` |
| `prefer_markdown_viewer` | boolean | `true` | Use Markdown viewer for MD files |
| `prefer_tabbed_editor_view` | boolean | `true` | Prefer tabbed editor view |
| `show_code_review_button` | boolean | `true` | Show code review button on tabs |
| `auto_open_code_review_pane_on_first_agent_change` | boolean | `false` | Auto-open code review pane on first agent change |
| `show_code_review_diff_stats` | boolean | `true` | Show lines added/removed on code review |
| `show_project_explorer` | boolean | `true` | Show project explorer in tools panel |
| `show_global_search` | boolean | `true` | Show global search in tools panel |
| `use_warp_as_default_editor` | boolean | `false` | Use Warp as default code editor |

### Indexing

**Section**: `[code.indexing]`

| Setting | Type | Default | Description |
|---------|------|---------|-------------|
| `agent_mode_codebase_context` | boolean | `true` | Provide Codebase Context to agent |
| `agent_mode_codebase_context_auto_indexing` | boolean | `false` | Enable automatic codebase indexing |

## Keys

Keyboard behavior settings.

**Section**: `[keys]`

| Setting | Type | Default | Description |
|---------|------|---------|-------------|
| `ctrl_tab_behavior_setting` | string | `"activate_prev_next_tab"` | `Ctrl+Tab` behavior. Options: `"activate_prev_next_tab"`, `"cycle_most_recent_session"` |

## Notifications

Desktop notification behavior settings.

**Section**: `[notifications]`

| Setting | Type | Default | Description |
|---------|------|---------|-------------|
| `toast_duration_secs` | integer | `8` | Notification toast duration (seconds) |

### Preferences

**Section**: `[notifications.preferences]`

| Setting | Type | Default | Description |
|---------|------|---------|-------------|
| `mode` | string | `"unset"` | Notification mode. Options: `"unset"`, `"dismissed"`, `"enabled"`, `"disabled"` |
| `is_long_running_enabled` | boolean | `true` | Notify when long-running command completes |
| `long_running_threshold` | integer | `30` | Threshold (seconds) for long-running notifications |
| `is_agent_task_completed_enabled` | boolean | `true` | Notify when agent task completes |
| `is_needs_attention_enabled` | boolean | `true` | Notify when session needs attention |
| `is_password_prompt_enabled` | boolean | `true` | Notify when password prompt detected |
| `play_notification_sound` | boolean | `true` | Play sound with notifications |

## Privacy

Telemetry, crash reporting, and secret redaction settings.

**Section**: `[privacy]`

| Setting | Type | Default | Description |
|---------|------|---------|-------------|
| `telemetry_enabled` | boolean | `true` | Collect anonymous usage telemetry |
| `crash_reporting_enabled` | boolean | `true` | Send crash reports |
| `custom_secret_regex_list` | array | `[]` | Custom regex patterns for secret detection/redaction |

Each item in `custom_secret_regex_list`:

```toml
[[privacy.custom_secret_regex_list]]
name = "example"
pattern = "your-pattern-here"
```

### Secret redaction

**Section**: `[privacy.secret_redaction]`

| Setting | Type | Default | Description |
|---------|------|---------|-------------|
| `enabled` | boolean | `false` | Detect and obscure secrets in output |
| `hide_secrets_in_block_list` | boolean | `false` | Hide detected secrets with asterisks in block list |
| `secret_display_mode_setting` | string | `"strikethrough"` | How secrets display. Options: `"asterisks"`, `"strikethrough"`, `"always_show"` |

## System

Low-level system and rendering settings.

**Section**: `[system]`

| Setting | Type | Default | Description |
|---------|------|---------|-------------|
| `prefer_low_power_gpu` | boolean | `false` | Prefer integrated (low-power) GPU |
| `preferred_graphics_backend` | string/null | `null` | Preferred graphics backend (Windows). Options: `"dx12"`, `"vulkan"`, `"gl"`, `"metal"`, `null` |
| `linux_selection_clipboard` | boolean | `true` | Use Linux primary selection clipboard |

## Text editing

Text editing behavior in the input editor.

**Section**: `[text_editing]`

| Setting | Type | Default | Description |
|---------|------|---------|-------------|
| `vim_mode_enabled` | boolean | `false` | Enable Vim keybindings |
| `vim_status_bar` | boolean | `true` | Show Vim status bar |
| `vim_unnamed_system_clipboard` | boolean | `false` | Vim unnamed register uses system clipboard |
| `autocomplete_symbols` | boolean | `true` | Auto-complete matching brackets and quotes |

## Warp Drive

Shared workflows, notebooks, and prompts settings.

**Section**: `[warp_drive]`

| Setting | Type | Default | Description |
|---------|------|---------|-------------|
| `enabled` | boolean | `true` | Enable Warp Drive |
| `sorting_choice` | string | `"by_object_type"` | Sort order. Options: `"by_timestamp"`, `"alphabetical_descending"`, `"alphabetical_ascending"`, `"by_object_type"` |

## Warpify

Warp features in SSH sessions and subshells.

### SSH

**Section**: `[warpify.ssh]`

| Setting | Type | Default | Description |
|---------|------|---------|-------------|
| `enable_ssh_warpification` | boolean | `true` | Enable Warp features in SSH sessions |
| `enable_legacy_ssh_wrapper` | boolean | `true` | Enable legacy SSH wrapper |
| `use_ssh_tmux_wrapper` | boolean | `false` | Use tmux-based wrapper |
| `ssh_extension_install_mode` | string | `"always_ask"` | SSH extension install behavior. Options: `"always_ask"`, `"always_install"`, `"never_install"` |
| `ssh_hosts_denylist` | array | `[]` | SSH hosts excluded from warpification |

### Subshells

**Section**: `[warpify.subshells]`

| Setting | Type | Default | Description |
|---------|------|---------|-------------|
| `added_subshell_commands` | array | `[]` | Additional regex patterns for subshell commands |
| `subshell_commands_denylist` | array | `[]` | Commands excluded from subshell warpification |

## Workflows

Workflow behavior settings.

**Section**: `[workflows]`

| Setting | Type | Default | Description |
|---------|------|---------|-------------|
| `show_global_workflows_in_universal_search` | boolean | `false` | Show global workflows in search results |

## Accessibility

Screen reader support settings.

**Section**: `[accessibility]`

| Setting | Type | Default | Description |
|---------|------|---------|-------------|
| `accessibility_verbosity` | string | `"verbose"` | Screen reader verbosity. Options: `"verbose"` (includes help), `"concise"` (value only) |

## Account

Account-related settings.

**Section**: `[account]`

| Setting | Type | Default | Description |
|---------|------|---------|-------------|
| `is_settings_sync_enabled` | boolean | `false` | Sync settings across devices via cloud |

## Cloud platform

Third-party API key and cloud model configuration.

### Third-party API keys

**Section**: `[cloud_platform.third_party_api_keys]`

| Setting | Type | Default | Description |
|---------|------|---------|-------------|
| `aws_bedrock_credentials_enabled` | boolean | `false` | Use local AWS credentials for Bedrock |
| `aws_bedrock_profile` | string | `"default"` | AWS profile for Bedrock |
| `aws_bedrock_auto_login` | boolean | `false` | Auto-run AWS login when credentials expire |
| `aws_bedrock_auth_refresh_command` | string | `"aws login"` | Command to refresh AWS credentials |
| `can_use_warp_credits_with_byok` | boolean | `false` | Use Warp credits with your own API key |

## Global hotkey

Global activation hotkey and dedicated hotkey window (Quake Mode) settings.

### Toggle all windows

**Section**: `[global_hotkey.toggle_all_windows]`

| Setting | Type | Default | Description |
|---------|------|---------|-------------|
| `enabled` | boolean | `false` | Enable hotkey to toggle all windows (mutually exclusive with `dedicated_window.enabled`) |
| `keybinding` | string/null | `null` | Hotkey keybinding (e.g., `"cmd-shift-a"`, `"alt-enter"`) |

### Dedicated window (Quake Mode)

**Section**: `[global_hotkey.dedicated_window]`

| Setting | Type | Default | Description |
|---------|------|---------|-------------|
| `enabled` | boolean | `false` | Enable dedicated hotkey window (mutually exclusive with `toggle_all_windows.enabled`) |

**Section**: `[global_hotkey.dedicated_window.settings]`

| Setting | Type | Default | Description |
|---------|------|---------|-------------|
| `active_pin_position` | string | — | Screen edge for pinning. Options: `"top"`, `"bottom"`, `"left"`, `"right"` |
| `hide_window_when_unfocused` | boolean | — | Hide window when unfocused |
| `keybinding` | string/null | — | Keyboard shortcut to toggle window |
| `pin_screen` | string/object/null | — | Display to pin. Options: `"primary"`, `{ external = 1 }`, `null` |

Window size percentages are configured per pin position:

```toml
[global_hotkey.dedicated_window.settings]
top = { size = 50 }
bottom = { size = 50 }
left = { size = 50 }
right = { size = 50 }
```
