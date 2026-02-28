---
title: YASB Reborn - Yet Another Status Bar
url: https://docs.yasb.dev/latest/widgets/systray
source: crawler
fetched_at: 2026-02-23T05:28:42.476885-03:00
rendered_js: false
word_count: 537
---

Option Type Default Description `class_name` string `'systray'` The class name for the base widget. `label_collapsed` string `'▼'` Label used for the collapse button when unpinned container is hidden. `label_expanded` string `'▶'` Label used for the collapse button when unpinned container is shown. `label_position` string `'left'` The position of the button that collapses unpinned container. Can be "left" or "right". `icon_size` integer `16` The size of the icons in the systray. Can be any integer between 8 and 64. `pin_click_modifier` string `'alt'` The modifier key used to pin/unpin icons. Can be "ctrl", "alt" or "shift". `show_unpinned` boolean `true` Whether to show unpinned container on startup. `show_unpinned_button` boolean `true` Whether to show the collapse unpinned icons button. `show_battery` boolean `false` Whether to show battery icon (from the original systray). `show_volume` boolean `false` Whether to show volume icon (from the original systray). `show_network` boolean `false` Whether to show network icon (from the original systray). `tooltip` boolean `true` Whether to show tooltips when hovering over systray icons. `container_shadow` dict `None` Container shadow options. `unpinned_shadow` dict `None` Unpinned container shadow options. `pinned_shadow` dict `None` Pinned container shadow options. `unpinned_vis_btn_shadow` dict `None` Unpinned visibility button shadow options. `btn_shadow` dict `None` Systray button (icons) shadow options.

## Example Configuration

```
systray:
type:"yasb.systray.SystrayWidget"
options:
class_name:"systray"
label_collapsed:"▼"
label_expanded:"▶"
label_position:"left"# Can be "left" or "right"
icon_size:16# Can be any integer between 8 and 64
pin_click_modifier:"alt"# Can be "ctrl", "alt" or "shift"
show_unpinned:true
show_unpinned_button:true
show_battery:false
show_volume:false
show_network:false
btn_shadow:
enabled:true
color:"black"
radius:3
offset:[1,1]
```

## Note on Shadows

`container_shadow` is applied to the container if it's not transparent. If it is transparent, container shadows will be applied to the child container and buttons instead. This can cause double shadows if you already have shadows applied to the child container and buttons. Apply the shadows only to the container that is actually visible.

There are some limitations with the systray widget:

- Systray widget will not show icons for apps if they ignore "TaskbarCreated" message. Meaning that if the original developers decided to ignore this message - their systray icons will not be shown. It's rare, but there are such cases (NVIDIA App for example). This is NOT a YASB bug.
- In rare cases systray icon might ignore click events if the original application was already running before YASB was started. Example: Epic Games Launcher. No solution for this so far.

## Description of Options

- **class\_name:** The class name for the base widget. Can be changed if multiple systray widgets need to have different styling.
- **label\_collapsed:** Label used for the collapse button when unpinned container is hidden.
- **label\_expanded:** Label used for the collapse button when unpinned container is shown.
- **label\_position:** The position of the button that collapses unpinned container.
- **icon\_size:** The size of the icons in the systray. Can be any integer between 8 and 64.
- **pin\_click\_modifier:** The modifier key used to pin/unpin icons. Can be "ctrl", "alt" or "shift".
- **show\_unpinned:** Whether to show unpinned container on startup.
- **show\_unpinned\_button:** Whether to show the 'collapse unpinned icons' button.
- **show\_battery:** Whether to show battery icon (from the original systray).
- **show\_volume:** Whether to show volume icon (from the original systray).
- **show\_network:** Whether to show network icon (from the original systray).
- **tooltip:** Whether to show tooltips when hovering over systray icons.
- **container\_shadow:** Container shadow options.
- **unpinned\_shadow:** Unpinned container shadow options.
- **pinned\_shadow:** Pinned container shadow options.
- **unpinned\_vis\_btn\_shadow:** Unpinned visibility button shadow options.
- **btn\_shadow:** Systray button (icons) shadow options.

## Debug Options

Show unpinned button has a right click menu that allows you to refresh the systray icons.

## Style

```
.systray{}/* The base widget style */
.systray.widget-container{}/* Style for the widget container */
.systray.unpinned-container{}/* Style for container with unpinned systray icons */
.systray.pinned-container{}/* Style for container with pinned systray icons */
.systray.pinned-container[forceshow=true]{}/* Style for pinned container when it is forced to show during dragging operation */
.systray.button{}/* Style for the individual systray buttons/icons */
.systray.button[dragging=true]{}/* Style for systray buttons/icons when dragging operation is in progress */
.systray.unpinned-visibility-btn{}/* Style for the 'collapse unpinned icons' button */
```

## Example CSS

```
.systray{
background:transparent;
border:none;
margin:0;
}

.systray.unpinned-container{
background:darkblue;
border-radius:8px;
}

.systray.pinned-container{
background:transparent;
}

.systray.pinned-container[forceshow=true]{
background:red;
}

.systray.button{
border-radius:4px;
padding:2px2px;
}

.systray.button:hover{
background:#727272;
}

.systray.button[dragging=true]{
background:orange;
border-color:#FF8800;
}

.systray.unpinned-visibility-btn{
border-radius:4px;
height:20px;
width:16px;
}

.systray.unpinned-visibility-btn:checked{
background:darkblue;
}

.systray.unpinned-visibility-btn:hover{
border:1pxsolid#AAAAAA;
border-radius:4px;
border-color:#AAAAAA;
}
```