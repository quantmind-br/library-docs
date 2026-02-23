---
title: YASB Reborn - Yet Another Status Bar
url: https://docs.yasb.dev/dev/widgets/komorebi-stack
source: crawler
fetched_at: 2026-02-23T05:20:43.736277-03:00
rendered_js: false
word_count: 541
---

*This widget displays information about each window in the currently active Komorebi stack.*

Option Type Default Description `label_offline` string `'Komorebi Offline'` The label to display when Komorebi is offline. `label_window` string `'{title}'` The format string for window buttons. `label_window_active` string `'{title}'` The format string for the active window button. `label_no_window` string `''` The label to display when no window is in focus. `label_zero_index` boolean `false` Whether to use zero-based indexing for window labels. `show_icons` string `never` Whether to display app icons. `icon_size` integer `16` The size of the icon displayed. `max_length` integer `None` The maximum length of the label text. `max_length_active` integer `None` The maximum length of the label text for the active window. `max_length_overall` integer `None` If specified, `max_length` will be calculated as `max_length_overall` divided by the number of inactive windows. `max_length_ellipsis` string `'...'` The ellipsis to use when the label text exceeds the maximum length. `hide_if_offline` boolean `false` Whether to hide the widget if Komorebi is offline. `show_only_stack` boolean `false` Whether to hide the widget if no stacked windows in focus. `rewrite` list `[]` Rewrite options for window titles and process names. `enable_scroll_switching` boolean `false` Enable scroll switching between windows. `reverse_scroll_direction` boolean `false` Reverse scroll direction. `animation` boolean `false` Buttons animation. `container_shadow` dict `None` Container shadow options. `label_shadow` dict `None` Label shadow options. `btn_shadow` dict `None` Window button shadow options.

## Example Configuration

```
komorebi_stack:
type:"komorebi.stack.StackWidget"
options:
label_offline:"Offline"
label_window:"{process}"
label_window_active:"{title}"
label_no_window:"NoWindow"
label_zero_index:false
show_icons:"always"
icon_size:14
max_length:10
max_length_active:20
max_length_ellipsis:".."
hide_if_offline:false
show_only_stack:false
rewrite:

-pattern:"^(.+?)\\.exe$"
replacement:"\\1"
case:"lower"
animation:true
enable_scroll_switching :true
container_shadow:
enabled:true
color:"#000000"
offset:[0,1]
radius:2
btn_shadow:
enabled:true
color:"#000000"
offset:[0,1]
radius:2
label_shadow:
enabled:true
color:"#000000"
offset:[0,1]
radius:2
```

## Description of Options

- **label\_offline:** The label to display when Komorebi is offline.
- **label\_window:** The format string for window buttons, can be {title}, {index}, {process}, or {hwnd}.
- **label\_window\_active:** The format string for the active window button, can be {title}, {index}, {process}, or {hwnd}.
- **label\_no\_window:** The label to display when no window is in focus.
- **label\_zero\_index:** Whether to use zero-based indexing for window labels.
- **show\_icons:** Whether to display app icons. Options are `always`, `never`, or `focused`.
- **max\_length:** The maximum number of characters to display for the label. If the title exceeds this length, it will be truncated.
- **max\_length\_active:** The maximum number of characters to display for the active window label. If the title exceeds this length, it will be truncated.
- **max\_length\_ellipsis:** The string to append to truncated window titles.
- **hide\_if\_offline:** Whether to hide the widget if Komorebi is offline.
- **show\_only\_stack:** Whether to hide the widget if no stacked windows in focus.
- **rewrite:** A list of search-and-replace rules to be applied to window titles and process names. See [Rewrite Options](#rewrite-options) below.
- **enable\_scroll\_switching:** Enable scroll switching between workspaces.
- **reverse\_scroll\_direction:** Reverse scroll direction.
- **animation:** Buttons animation.
- **container\_shadow:** Container shadow options.
- **label\_shadow:** Label shadow options for labels, including icons and labels within each window button.
- **btn\_shadow:** Window button shadow options.

> Note: Left click on window title switches to the window, and Middle click closes the window.

## Rewrite Options

The `rewrite` option allows you to supply a list of search-and-replace rules to be applied, in order, to window titles and process names. Each rule is a dict with the following schema:

Field Type Required Default Description `pattern` string yes None A Python regular expression to match against the window title or process name. [More Info](https://docs.python.org/3/library/re.html) `replacement` string yes None The replacement text; can use backrefs like `\1`, `\2`, etc. `case` string no None If specified, the replacement will be converted to the specified case. Allowed values: `lower`, `upper`, `title`, `capitalize`

### Example

```
komorebi_stack:
type:"komorebi.stack.StackWidget"
options:
label_window:"{title}"
# …
rewrite:
# Strip trailing ".exe" (case-insensitive) and lowercase:

-pattern:"^(.+?)\\.exe$"
replacement:"\\1"
case:lower

# Replace "Microsoft Edge" with "Edge" and uppercase:

-pattern:"MicrosoftEdge"
replacement:"Edge"
case:upper

# Replace "Visual Studio Code" with "VSCode":

-pattern:"VisualStudioCode"
replacement:"VSCode"
```

## Style

```
.komorebi-stack{}/*Style for widget.*/
.komorebi-stack.widget-container{}/*Style for widget container.*/
.komorebi-stack.window{}/*Style for buttons.*/
.komorebi-stack.window.label{}/*Style for the window label.*/
.komorebi-stack.window.icon{}/*Style for the window icon.*/
.komorebi-stack.window.active{}/*Style for the active window button.*/
.komorebi-stack.window.active.label{}/*Style for the active window label.*/
.komorebi-stack.window.active.icon{}/*Style for the active window icon.*/
.komorebi-stack.window.button-1{}/*Style for first button.*/
.komorebi-stack.window.button-2{}/*Style for second  button.*/
.komorebi-stack.offline-status{}/*Style for offline status label.*/
.komorebi-stack.no-window{}/*Style for no window label.*/
```

## Example Style

```
.komorebi-stack{
margin:4px0;
}
.komorebi-stack.widget-container{
background-color:#282936;
border-radius:4px;
}
.komorebi-stack.window{
background-color:transparent;
border:none;
margin:0px8px;
padding:04px;
}
.komorebi-stack.window.active{
background-color:#45475a;
border-radius:4px;
height:auto;
margin:0;
}
```