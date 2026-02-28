---
title: YASB Reborn - Yet Another Status Bar
url: https://docs.yasb.dev/latest/widgets/glazewm-workspaces
source: crawler
fetched_at: 2026-02-23T05:28:34.988927-03:00
rendered_js: false
word_count: 684
---

Option Type Default Description `offline_label` string `'GlazeWM Offline'` The label to display when GlazeWM is offline. `populated_label` string `'{name}'` Optional label for populated workspaces. `empty_label` string `'{name}'` Optional label for empty workspaces. `active_populated_label` string `'{name}'` Optional label for the currently active workspace (has opened windows). `active_empty_label` string `'{name}'` Optional label for the currently active workspace (has no windows opened). `focused_populated_label` string `'{name}'` Optional label for the currently focused workspace (has opened windows). Falls back to `active_populated_label` if not set. `focused_empty_label` string `'{name}'` Optional label for the currently focused workspace (has no windows opened). Falls back to `active_empty_label` if not set. `hide_empty_workspaces` boolean `true` Whether to hide empty workspaces. `hide_if_offline` boolean `false` Whether to hide workspaces widget if GlazeWM is offline. `glazewm_server_uri` string `'ws://localhost:6123'` Optional GlazeWM server uri. `enable_scroll_switching` boolean `true` Enable scroll switching between workspaces. `reverse_scroll_direction` boolean `false` Reverse scroll direction. `container_shadow` dict `None` Container shadow options. `btn_shadow` dict `None` Workspace button shadow options. `app_icons` dict `{'enabled_populated': False, 'enabled_active': False, 'enabled_focused': None, 'size': 16, 'max_icons': 0, 'hide_label': False, 'hide_duplicates': False, 'hide_floating': False}` Controls the display of opened app icons per workspace. `enabled_focused` falls back to `enabled_active` if not explicitly set to a non-None bool value. `animation` boolean `false` Buttons animation.

## Example Configuration

```
glazewm_workspaces:
type:"glazewm.workspaces.GlazewmWorkspacesWidget"
options:
offline_label:"GlazeWMOffline"
hide_empty_workspaces:true
hide_if_offline:false
enable_scroll_switching:true
btn_shadow:
enabled:true
color:"black"
radius:3
offset:[1,1]
app_icons:
enabled_populated:false
enabled_active:false
size:16
max_icons:0
hide_label:false
hide_duplicates:false
hide_floating:false
animation:false

# By default workspace names are fetched from GlazeWM and "display_name" option takes priority over "name".
# However, you can customize populated and empty labels here using {name} and {display_name} placeholders if needed.
# {name} will be replaced with workspace name (index) from GlazeWM.
# {display_name} will be replaced with workspace display_name from GlazeWM.

# populated_label: "{name} {display_name} \uebb4"
# empty_label: "{name} {display_name} \uebb5"
```

## Description of Options

- **offline\_label:** The label to display when GlazeWM is offline.
- **populated\_label:** Optional label for populated workspaces. If not set, name or display\_name from GlazeWM will be used.
- **empty\_label:** Optional label for empty workspaces. If not set, name or display\_name from GlazeWM will be used.
- **active\_populated\_label:** Optional label for the currently active workspace (has windows opened). If not set, name or display\_name from GlazeWM will be used.
- **active\_empty\_label:** Optional label for the currently active workspace (has no windows opened). If not set, name or display\_name from GlazeWM will be used.
- **focused\_populated\_label:** Optional label for the currently focused workspace (has windows opened). If not set, **active\_populated\_label** will be used, falling back to name or display\_name from GlazeWM.
- **focused\_empty\_label:** Optional label for the currently focused workspace (has no windows opened). If not set, **active\_empty\_label** will be used, falling back to name or display\_name from GlazeWM.
- **hide\_empty\_workspaces:** Whether to hide empty workspaces.
- **hide\_if\_offline:** Whether to hide workspaces widget if GlazeWM is offline.
- **glazewm\_server\_uri:** Optional GlazeWM server uri if it ever changes on GlazeWM side.
- **enable\_scroll\_switching:** Enable scroll switching between workspaces.
- **reverse\_scroll\_direction:** Reverse scroll direction for switching workspaces.
- **container\_shadow:** Container shadow options.
- **btn\_shadow:** Workspace button shadow options.
- **app\_icons:** Controls the display of opened app icons per workspace.
- **enabled\_populated:** Whether to show app icons in populated workspaces.
- **enabled\_active:** Whether to show app icons in the active workspace.
- **enabled\_focused:** Whether to show app icons in the focused workspace. If not set, **enabled\_active** will be used.
- **size:** The size of the app icons.
- **max\_icons:** The maximum number of app icons to display (0 for no limit).
- **hide\_label:** Whether to hide the label of the workspace buttons that app icons are displayed.
- **hide\_duplicates:** Whether to hide duplicate app icons.
- **hide\_floating:** Whether to hide floating window app icons.
- **label\_shadow:** Label shadow options for labels.
- **animation:** Buttons animation (used only when app\_icons is enabled)

## Note on Shadows

`container_shadow` is applied to the container if it's not transparent. If it is transparent, container shadows will be applied to the `btn` instead. This can cause double shadows if you have `btn_shadow` already. Apply the shadows only to the container that is actually visible.

## Note on Workspace Names

In GlazeWM config use "1", "2", "3" for workspace "name" and NOT some custom string. This will ensure proper sorting of workspaces.

If you need a custom name for each workspace - use "display\_name".

**Example:**

```
workspaces:

-name:"1"
display_name:"Work"# Optional

-name:"2"
display_name:"Browser"# Optional

-name:"3"
display_name:"Music"# Optional
# and so on...
```

## Style

```
.glazewm-workspaces{}/*Style for widget.*/
.glazewm-workspaces.ws-btn{}/*Style for workspace buttons.*/
.glazewm-workspaces.ws-btn.active_populated{}/*Style for active populated workspace button.*/
.glazewm-workspaces.ws-btn.active_empty{}/*Style for active empty workspace button.*/
.glazewm-workspaces.ws-btn.focused_populated{}/*Style for focused populated workspace button.*/
.glazewm-workspaces.ws-btn.focused_empty{}/*Style for focused empty workspace button.*/
.glazewm-workspaces.ws-btn.populated{}/*Style for populated workspace button.*/
.glazewm-workspaces.ws-btn.empty{}/*Style for empty workspace button.*/
.glazewm-workspaces.offline-status{}/*Style for offline status label.*/
```

Note: `focused_populated` and `focused_empty` MUST COME AFTER `active_populated` and `active_empty`, respectively, otherwise the `active_*` classes will override any CSS conflicting properties set by their `focused_*` counterparts. Any property that you do not want the `focused_*` classes to inherit from their `active_*` counterparts will need to be set to an explicit value or **unset** if you both do not want to inherit a specific property and you do not want to set it to something.

If `app_icons` is enabled (either `enabled_populated`, `enabled_active`, or `enabled_focused`), the following styles are available:

```
.glazewm-workspaces.ws-btn.label{}/*Style for workspace label in buttons.*/
.glazewm-workspaces.ws-btn.icon{}/*Style for icon in buttons.*/
.glazewm-workspaces.ws-btn.icon-1{}/*Style for icon in first button in a workspace.*/
.glazewm-workspaces.ws-btn.icon-2{}/*Style for icon in second button in a workspace.*/
...
```

## Example CSS

```
.glazewm-workspaces{
margin:0;
}

.glazewm-workspaces.ws-btn{
font-size:14px;
background-color:transparent;
border:none;
padding:0px4px0px4px;
margin:02px02px;
color:#CDD6F4;
}

.glazewm-workspaces.ws-btn.active_populated{
color:#C2DAF7;
background-color:#727272;
}
.glazewm-workspaces.ws-btn.active_empty{
color:#7D8B9D;
background-color:#727272;
}

.glazewm-workspaces.ws-btn.populated{
color:#C2DAF7;
}

.glazewm-workspaces.ws-btn.empty{
color:#7D8B9D;
}

.glazewm-workspaces.ws-btn:hover,
.glazewm-workspaces.ws-btn.populated:hover,
.glazewm-workspaces.ws-btn.empty:hover{
background-color:#727272;
}
```