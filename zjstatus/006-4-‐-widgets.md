---
title: !!binary NCDvv72AkCBXaWRnZXRz
url: https://github.com/dj95/zjstatus/wiki/4-‐-Widgets
source: wiki
fetched_at: 2026-04-30T12:58:28.809413518-03:00
rendered_js: false
word_count: 1073
summary: This document provides a configuration reference for the various widgets available in zjstatus, a status bar plugin for the Zellij terminal multiplexer.
tags:
    - zellij
    - zjstatus
    - terminal-emulator
    - configuration
    - widgets
    - plugin-settings
category: reference
---

zjstatus contains the following widgets with their respective config.

## command

**Handle** `{command_NAME}`

⚠️  zellij 0.39.0 or newer is needed!

This widget is able to run arbitrary commands and prints the result. Keep in mind, that it
runs **just** the command **not** in a shell. If you'd like to use a shell, please make
sure you specify it and properly use it for running your command. Since the command widget
should be able to run multiple commands, it behaves a bit different than the other widgets.
Therefore the command need to have a name in form of e.g. `{command_pwd}` or `{command_git_branch}`. The following
options can be provided per named command.

> [!IMPORTANT]
> NAME must be a lowercase name of your choice.

```javascript
// the command that should be executed
command_NAME_command  "bash -c \"pwd | base64\""

// themeing and format of the command
command_NAME_format   "#[fg=blue, bg=black] {exit_code} {stdout} {stderr}"

// interval in seconds, between two command runs
//
// Set to "0" for running the command once. Only non-negative integers are allowed.
command_NAME_interval "1"

// render mode of the command. ["static", "dynamic", "raw"]
//
// "static"  :: format the command with the given format from the config and don't
//              consider any other formatting directives
// "dynamic" :: format the command based on the command output. When the command
//              output contains formatting strings for zjstatus, zjstatus will
//              try to render them. This might lead to unexpected behavior, in case
//              the formatting is not correct.
// "raw"     :: do not apply any formatting. This can be used to properly render
//              ansi escape sequences from the command output.
command_NAME_rendermode "static"

// set an absolute path as cwd where the command should be executed
command_NAME_cwd       "/Users/daniel"

// specify environment variables that are set when running the command
command_NAME_env {
    FOO "1"
    BAR "foo"
}
```

## datetime

**Handle** `{datetime}`

Print the date and/or time by the given format string. Due to the WASM sandbox
the timezone cannot be determined from the system. You can configure it
with the `datetime_timezone` parameter. Choose the according string from the
chrono documentation: [https://docs.rs/chrono-tz/latest/chrono_tz/enum.Tz.html](https://docs.rs/chrono-tz/latest/chrono_tz/enum.Tz.html).
For the `datetime_format` syntax, you can also check the specifiers table 
available in the chrono documentation:
[https://docs.rs/chrono/latest/chrono/format/strftime/index.html](https://docs.rs/chrono/latest/chrono/format/strftime/index.html).

```javascript
// theme formatting for colors. Datetime output is printed in {format}.
datetime        "#[fg=#6C7086,bold] {format} "

// format of the date
datetime_format "%A, %d %b %Y %H:%M"

// timezone to print
datetime_timezone "Europe/Berlin"
```

## mode

**Handle** `{mode}`

Indicate the current active mode in zellij. Each mode can be configured individually. If a mode is not configured, it will
fall back to the format of `mode_normal`, if `mode_default_to_mode` is not specified or invalid. Otherwise it will use the
format referenced in `mode_default_to_mode`, if the format for a mode is unspecified. The name of the mode can be used
in the `{name}` variable.

```javascript
mode_normal        "#[bg=#89B4FA] {name} "
mode_locked        "#[bg=#89B4FA] {name} "
mode_resize        "#[bg=#89B4FA] {name} "
mode_pane          "#[bg=#89B4FA] {name} "
mode_tab           "#[bg=#89B4FA] {name} "
mode_scroll        "#[bg=#89B4FA] {name} "
mode_enter_search  "#[bg=#89B4FA] {name} "
mode_search        "#[bg=#89B4FA] {name} "
mode_rename_tab    "#[bg=#89B4FA] {name} "
mode_rename_pane   "#[bg=#89B4FA] {name} "
mode_session       "#[bg=#89B4FA] {name} "
mode_move          "#[bg=#89B4FA] {name} "
mode_prompt        "#[bg=#89B4FA] {name} "
mode_tmux          "#[bg=#ffc387] {name} "

mode_default_to_mode "tmux"
```

## notifications

**Handle** `{notifications}`

⚠️  zellij 0.40.0 or newer is needed!

Prints the last received notification message from the `zjstatus::notify::` command. The message must not contain newlines! It is automatically hidden after the configured interval. Within the format, `{message}` will be replace by the last received message.

```javascript
notification_format_unread           "#[fg=#89B4FA,bg=#181825,blink]  #[fg=#89B4FA,bg=#181825] {message} "
notification_format_no_notifications "#[fg=#89B4FA,bg=#181825,dim]   "
notification_show_interval           "10"
```

## pipe

**Handle** `{pipe}`

Display a text received by a pipe input. For sending a message, use the pipe message protocol. Like the command widget this
widget must contain a name. E.g. `pipe_test_format` has the name `test`. For sending data to this widget, run
`zellij pipe "zjstatus::pipe::pipe_test::your message"`. `{output}` will be replaced with the last received output from 
the pipe. Please bear in mind to **not** send newlines through the pipe.

```javascript
pipe_NAME_format "#[fg=#89B4FA,bg=#181825] {output}"

// render mode of the pipe. ["static", "dynamic", "raw"]
//
// "static"  :: format the pipe content with the given format from the config and don't
//              consider any other formatting directives
// "dynamic" :: format the based on the pipe content. When the pipe
//              content contains formatting strings for zjstatus, zjstatus will
//              try to render them. This might lead to unexpected behavior, in case
//              the formatting is not correct.
// "raw"     :: do not apply any formatting. This can be used to properly render
//              ansi escape sequences from the command output.
pipe_NAME_rendermode "static"
```

## session

**Handle** `{session}`

Print the current session name. This module cannot be configured. For formatting, please put the Formatting
sequence right before the handle in `format_left`, `format_center` or `format_right`.

## swap layout

**Handle** `{swap_layout}`  
**Click behavior** Switch to the next swap layout

Print the active swap layout. The widget can be hidden if it's empty, when the correct configuration is set. The name of the layout can be used with `{name}` in the config.

```javascript
swap_layout_format          "#[fg=#6C7086] {name} "
swap_layout_hide_if_empty   "true"
```

## tabs

**Handle** `{tabs}`  
**Click behavior** Navigate to the tab that got clicked

Print a list of current tabs. The name of the tab can be used with `{name}` in the config. The active tab will
default to the normal formatting, if not configured.
With `{index}` the tab position can also be used. With `{floating_total_count}` you can print the total amount
of floating panes.
In addition to separate formats for sync and fullscreen tabs, you can use `{sync_indicator}`,
`{fullscreen_indicator}` and `{floating_indicator}` in each format. It will be replaced with the respective
configuration from `tab_sync_indicator` and so on. Please be aware, that the indicators are only replaced
when they are configured.

```javascript
// formatting for inactive tabs
tab_normal              "#[fg=#6C7086] {index} :: {name} "
tab_normal_fullscreen   "#[fg=#6C7086] {index} :: {name} [] "
tab_normal_sync         "#[fg=#6C7086] {index} :: {name} <> "

// formatting for the current active tab
tab_active              "#[fg=#9399B2,bold,italic] {name} {floating_indicator}"
tab_active_fullscreen   "#[fg=#9399B2,bold,italic] {name} {fullscreen_indicator}"
tab_active_sync         "#[fg=#9399B2,bold,italic] {name} {sync_indicator}"

// separator between the tabs
tab_separator           "#[fg=#6C7086,bg=#181825] | "

// format when renaming a tab
tab_rename              "#[fg=#eba0ac,bg=#181825] {index} {name} {floating_indicator} "

// indicators
tab_sync_indicator       "<> "
tab_fullscreen_indicator "[] "
tab_floating_indicator   "⬚ "

// limit tab display count
tab_display_count         "3"  // limit to showing 3 tabs
tab_truncate_start_format "#[fg=red,bg=#181825] < +{count} ..."
tab_truncate_end_format   "#[fg=red,bg=#181825] ... +{count} >"

// index configuration
tab_zero_based_index      "false" // start with 0 instead of 1 for the index
```
