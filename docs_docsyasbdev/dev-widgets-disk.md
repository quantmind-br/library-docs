---
title: YASB Reborn - Yet Another Status Bar
url: https://docs.yasb.dev/dev/widgets/disk
source: crawler
fetched_at: 2026-02-23T05:20:32.748112-03:00
rendered_js: false
word_count: 756
---

Option Type Default Description `label` string `'{volume_label} {space[used][percent]}'` The format string for the disk widget. `label_alt` string `'{volume_label} {space[used][gb]} / {space[total][gb]}'` The alternative format string for the disk widget. `class_name` string `""` Additional CSS class name for the widget. `volume_label` string `'C'` Partition which you want to show in the bar `decimal_display` integer `1` The number of decimal places to show, default 1 (min 0 max 3) `update_interval` integer `60` The interval in seconds to update the disk widget. Must be between 0 and 3600. `group_label` dict `{'volume_labels': ["C"], 'show_label_name': true, 'blur': true, 'round_corners': true, 'round_corners_type': 'normal','border_color': 'System', 'alignment': 'right', 'direction': 'down', 'offset_top': 6, 'offset_left': 0}` Group labels for multiple disks. This will show the labels of multiple disks in a popup window. `callbacks` dict `{'on_left': 'do_nothing', 'on_middle': 'do_nothing', 'on_right': "exec explorer C:\\"}` Callbacks for mouse events. `disk_thresholds` dict `{'low': 25, 'medium': 50, 'high': 90}` Thresholds for Disk usage levels. `animation` dict `{'enabled': true, 'type': 'fadeInOut', 'duration': 200}` Animation settings for the widget. `container_shadow` dict `None` Container shadow options. `label_shadow` dict `None` Label shadow options. `progress_bar` dict `{'enabled': false, 'position': 'left', 'size': 14, 'thickness': 2, 'color': '#57948a', 'animation': false}` Progress bar settings.

## Example Configuration

```
disk:
type:"yasb.disk.DiskWidget"
options:
label:"{volume_label}{space[used][percent]}"
label_alt:"{volume_label}{space[used][gb]}/{space[total][gb]}"
volume_label:"C"
update_interval:60
group_label:
volume_labels:["C","D","E","F"]
show_label_name:true
blur:True
round_corners:True
round_corners_type:"small"
border_color:"System"
alignment:"right"
direction:"down"
callbacks:
on_left:"toggle_group"
on_middle:"toggle_label"
on_right:"execexplorerC:\\"# Open disk C in file explorer
label_shadow:
enabled:true
color:"black"
radius:3
offset:[1,1]
disk_thresholds:
low:25
medium:50
high:90
```

## Description of Options

- **label:** The format string for the disk widget. Displays free space in percent.
- **label\_alt:** The alternative format string for the disk widget.
- **class\_name:** Additional CSS class name for the widget. This allows for custom styling.
- **volume\_label:** Partition/volume which you want to show in the bar.
- **decimal\_display:** The number of decimal places to show, default 1 (min 0 max 3).
- **update\_interval:** The interval in seconds to update the disk widget. Must be between 0 and 3600.
- **disk\_thresholds:** A dictionary specifying the thresholds for disk usage levels. The keys are `low`, `medium`, and `high`, and the values are the percentage thresholds. Based on the current disk usage, a CSS class is applied to the label: `status-low`, `status-medium`, `status-high`, or `status-critical`.
- **group\_label:** Group labels for multiple disks. This will show the labels of multiple disks in a popup window.
- **volume\_labels:** List of volume labels to show in the group label.
- **show\_label\_name:** Show the label name in the group label.
- **blur:** Enable blur effect for the group label.
- **round\_corners:** Enable round corners for group label.
- **round\_corners\_type:** Border type for group label can be `normal` and `small`. Default is `normal`.
- **border\_color:** Border color for group label can be `None`, `System` or `Hex Color` `"#ff0000"`.
- **alignment:** Alignment of the group label. Possible values are `left`, `center`, and `right`.
- **direction:** Direction of the group label. Possible values are `up` and `down`.
- **offset\_top:** Offset from the top of the screen.
- **offset\_left:** Offset from the left of the screen.
- **callbacks:** A dictionary specifying the callbacks for mouse events. The keys are `on_left`, `on_middle`, and `on_right`, and the values are the names of the callback functions.
- **Available callbacks:** `toggle_label`, `toggle_group`, `do_nothing`, or `exec <command>`.
- **animation:** A dictionary specifying the animation settings for the widget. It contains three keys: `enabled`, `type`, and `duration`. The `type` can be `fadeInOut` and the `duration` is the animation duration in milliseconds.
- **container\_shadow:** Container shadow options.
- **label\_shadow:** Label shadow options.
- **progress\_bar**: A dictionary containing settings for the progress bar. It includes:
- **enabled**: Whether the progress bar is enabled.
- **position**: The position of the progress bar, either "left" or "right".
- **size**: The size of the progress bar.
- **thickness**: The thickness of the progress bar.
- **color**: The color of the progress bar. Color can be single color or gradient. For example, `color: "#57948a"` or `color: ["#57948a", "#ff0000"]"` for a gradient.
- **background\_color**: The background color of the progress bar.
- **animation**: Whether to enable smooth change of the progress bar value.

## Label Format Variables

The following variables can be used in `label` and `label_alt`:

Variable Description Example Output `{volume_label}` The drive letter `C` `{space[total][mb]}` Total space in MB `953674.32MB` `{space[total][gb]}` Total space in GB `931.51GB` `{space[total][tb]}` Total space in TB `0.91TB` `{space[free][mb]}` Free space in MB `476837.16MB` `{space[free][gb]}` Free space in GB `465.66GB` `{space[free][tb]}` Free space in TB `0.45TB` `{space[free][percent]}` Free space percentage `50.0%` `{space[used][mb]}` Used space in MB `476837.16MB` `{space[used][gb]}` Used space in GB `465.85GB` `{space[used][tb]}` Used space in TB `0.45TB` `{space[used][percent]}` Used space percentage `50.0%`

## Disk Threshold Classes

Based on `disk_thresholds` configuration, the widget applies CSS classes to style the label based on disk usage:

Disk Usage CSS Class Applied 0% - `low` `status-low` `low` - `medium` `status-medium` `medium` - `high` `status-high` Above `high` `status-critical`

```
.disk-widget{}
.disk-widget.your_class{}/* If you are using class_name option */
.disk-widget.widget-container{}
.disk-widget.widget-container.label{}
.disk-widget.widget-container.label.alt{}
.disk-widget.widget-container.icon{}
/* Threshold status classes */
.disk-widget.widget-container.label.status-low{}
.disk-widget.widget-container.label.status-medium{}
.disk-widget.widget-container.label.status-high{}
.disk-widget.widget-container.label.status-critical{}
/* Group label style */
.disk-group{}
.disk-group-row{}
.disk-group-label{}
.disk-group-label-size{}
.disk-group-label-bar{}
.disk-group-label-bar::chunk{}

/* Disk progress bar styles if enabled */
.disk-widget.progress-circle{}
```

## Example Style for Threshold Classes

```
.disk-widget.widget-container.label.status-low{
color:#a6e3a1;/* Green */
}
.disk-widget.widget-container.label.status-medium{
color:#f9e2af;/* Yellow */
}
.disk-widget.widget-container.label.status-high{
color:#fab387;/* Orange */
}
.disk-widget.widget-container.label.status-critical{
color:#f38ba8;/* Red */
}
```

## Example Style for Group Label

```
.disk-group{
background-color:rgba(17,17,27,0.75);
}
.disk-group-row{
min-width:220px;
max-width:220px;
max-height:40px;
margin:0;
padding:0;
border-radius:6px;
border:1pxsolidrgba(128,128,128,0);
}
.disk-group-row:hover{
background-color:rgba(255,255,255,0.05);
border:1pxsolidrgba(255,255,255,0.1)
}
.disk-group-label-bar{
max-height:8px;
border:0pxsolidrgba(128,128,128,0);
background-color:rgba(137,180,250,0.1);
border-radius:4px
}
.disk-group-label-bar::chunk{
background-color:rgba(137,180,250,0.3);
border-radius:4px
}
.disk-group-label{
font-size:10px
}
.disk-group-label-size{
font-size:10px;
color:#585b70
}
```

## Example Settings for Group Label and show menu

```
disk:
type:"yasb.disk.DiskWidget"
options:
label:"<span>\uf473</span>"
label_alt:"<span>\uf473</span>"
group_label:
volume_labels:["C","D","E","F"]
show_label_name:true
blur:True
round_corners:True
round_corners_type:"normal"
border_color:"System"
alignment:"right"
direction:"down"
distance:6
callbacks:
on_left:"toggle_group"
```

## Style for Group Label and show menu

```
.disk-widget{
padding:06px06px;
}
.disk-group{
background-color:rgba(17,17,27,0.4);
}
.disk-group-row{
min-width:220px;
max-width:220px;
max-height:40px;
margin:0;
padding:0;
border-radius:6px;
border:1pxsolidrgba(128,128,128,0);
}
.disk-group-row:hover{
background-color:rgba(255,255,255,0.05);
border:1pxsolidrgba(255,255,255,0.1);
}
.disk-group-label-bar{
max-height:8px;
border:0pxsolidrgba(128,128,128,0);
background-color:rgba(137,180,250,0.1);
border-radius:4px;
}
.disk-group-label-bar::chunk{
background-color:rgba(61,135,255,0.3);
border-radius:4px;
}
.disk-group-label{
font-size:10px;
}
.disk-group-label-size{
font-size:10px;
color:#666879;
}
```

## Preview of example above

![GitHub YASB Widget](https://docs.yasb.dev/dev/widgets/assets/758425162-b61ef748-4280-0884-dc5f59c2ba8d.png)