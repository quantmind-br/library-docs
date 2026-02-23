---
title: YASB Reborn - Yet Another Status Bar
url: https://docs.yasb.dev/dev/widgets/komorebi-workspaces
source: crawler
fetched_at: 2026-02-23T05:20:43.089876-03:00
rendered_js: false
word_count: 472
---

Option Type Default Description `label_offline` string `'Komorebi Offline'` The label to display when Komorebi is offline. `label_workspace_btn` string `'{index}'` The format string for workspace buttons. `label_workspace_active_btn` string `'{index}'` The format string for the active workspace button. `label_workspace_populated_btn` string `'{index}'` The format string for the populated workspace button. `label_default_name` string `''` The default name for workspaces. `label_float_override` string `'Override Active'` The label to display when Komorebi's float override is active. `toggle_workspace_layer` dict `{'enabled': false, 'tiling_label': 'Tiling', 'floating_label': 'Floating'}` Controls toggling between tiling and floating layers. `app_icons` dict `{'enabled_populated': false, 'enabled_active': false, 'size': 16, 'max_icons': 0, 'hide_label': false, 'hide_duplicates': false, 'hide_floating': false}` Controls the display of opened app icons per workspace. `hide_if_offline` boolean `false` Whether to hide the widget if Komorebi is offline. `label_zero_index` boolean `false` Whether to use zero-based indexing for workspace labels. `hide_empty_workspaces` boolean `false` Whether to hide empty workspaces. `enable_scroll_switching` boolean `false` Enable scroll switching between workspaces. `reverse_scroll_direction` boolean `false` Reverse scroll direction. `animation` boolean `false` Button animation. `container_shadow` dict `None` Container shadow options. `btn_shadow` dict `None` Workspace button shadow options.

## Example Configuration

```
komorebi_workspaces:
type:"komorebi.workspaces.WorkspaceWidget"
options:
label_offline:"KomorebiOffline"
label_workspace_btn:"\udb81\udc3d"
label_workspace_active_btn:"\udb81\udc3e"
label_workspace_populated_btn:"\udb81\udc3e"
label_default_name:""
label_zero_index:false
hide_empty_workspaces:false
hide_if_offline:false
animation:true
toggle_workspace_layer:
enabled:false
tiling_label:"Tiling"
floating_label:"Floating"
app_icons:
enabled_populated:false
enabled_active:false
size:12
max_icons:0
hide_label:false
hide_duplicates:false
hide_floating:false
btn_shadow:
enabled:true
color:"black"
radius:3
offset:[1,1]
```

## Description of Options

- **label\_offline:** The label to display when Komorebi is offline.
- **label\_workspace\_btn:** The format string for workspace buttons, can be icon, {name} or {index}.
- **label\_workspace\_active\_btn:** The format string for the active workspace button, can be icon, {name} or {index}.
- **label\_workspace\_populated\_btn:** The format string for the populated workspace button, can be icon, {name} or {index}.
- **label\_default\_name:** The default name for workspaces.
- **label\_float\_override:** The label to display when Komorebi is Float Override Active.
- **toggle\_workspace\_layer:** Controls toggling between tiling and floating layers.
- **enabled:** Whether to enable the workspace layer toggle functionality.
- **tiling\_label:** The label to display for the tiling layer.
- **floating\_label:** The label to display for the floating layer.
- **app\_icons:** Controls the display of opened app icons per workspace.
- **enabled\_populated:** Whether to show app icons in populated workspaces.
- **enabled\_active:** Whether to show app icons in the active workspace.
- **size:** The size of the app icons.
- **max\_icons:** The maximum number of app icons to display (0 for no limit).
- **hide\_label:** Whether to hide the label of the workspace buttons that app icons are displayed.
- **hide\_duplicates:** Whether to hide duplicate app icons.
- **hide\_floating:** Whether to hide floating window app icons.
- **hide\_if\_offline:** Whether to hide the widget if Komorebi is offline.
- **label\_zero\_index:** Whether to use zero-based indexing for workspace labels.
- **hide\_empty\_workspaces:** Whether to hide empty workspaces.
- **enable\_scroll\_switching:** Enable scroll switching between workspaces.
- **reverse\_scroll\_direction:** Reverse scroll direction.
- **animation:** Buttons animation.
- **container\_shadow:** Container shadow options.
- **btn\_shadow:** Workspace button shadow options.
- **label\_shadow:** Label shadow options for labels.

## Style

```
.komorebi-workspaces{}/*Style for widget.*/
.komorebi-workspaces.widget-container{}/*Style for widget container.*/
.komorebi-workspaces.ws-btn{}/*Style for buttons.*/
.komorebi-workspaces.ws-btn.populated{}/*Style for buttons which contain window and are not empty.*/
.komorebi-workspaces.ws-btn.active{}/*Style for the active workspace button.*/
.komorebi-workspaces.ws-btn.button-1{}/*Style for first button.*/
.komorebi-workspaces.ws-btn.button-2{}/*Style for second  button.*/
.komorebi-workspaces.float-override{}/*Style for float override text and icon.*/
.komorebi-workspaces.workspace-layer{}/*Style for workspace layer text and icon.*/
.komorebi-workspaces.workspace-layer.tiling{}/*Style for workspace layer text and icon when in tiling mode.*/
.komorebi-workspaces.workspace-layer.floating{}/*Style for workspace layer text and icon when in floating mode.*/
```

If `app_icons` is enabled (either `enabled_populated` or `enabled_active`), you can't use `.ws-btn` to style label. Add the following styles:

```
.komorebi-workspaces.ws-btn.label{}/*Style for label text in buttons.*/
.komorebi-workspaces.ws-btn.populated.label{}/*Style for label text in populated buttons.*/
.komorebi-workspaces.ws-btn.active.label{}/*Style for label text in active buttons.*/
.komorebi-workspaces.ws-btn.icon{}/*Style for icon in buttons.*/
.komorebi-workspaces.ws-btn.icon-1{}/*Style for icon in first button.*/
.komorebi-workspaces.ws-btn.icon-2{}/*Style for icon in second button.*/
.komorebi-workspaces.ws-btn.active.icon{}/*Style for icon in active buttons.*/
```

> \[!NOTE]  
> You can use `button-x` to style each button separately. Where x is the index of the button. If `app_icons` is enabled, you can use `icon-x` to style each icon separately. Where x is the index of the icon.