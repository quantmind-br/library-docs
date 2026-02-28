---
title: YASB Reborn - Yet Another Status Bar
url: https://docs.yasb.dev/latest/widgets/bluetooth
source: crawler
fetched_at: 2026-02-23T05:28:32.432634-03:00
rendered_js: false
word_count: 395
---

Option Type Default Description `label` string `'{icon}'` The format string for the bluetooth widget. Displays icons. `label_alt` string `'{device_name}'` The alternative format string for the bluetooth widget. Displays list of connected devices. `class_name` string `""` Additional CSS class name for the widget. `label_no_device` string `'No devices connected'` The string to display `{device_name}` when no devices are connected. `label_device_separator` string `', '` The string to separate multiple device names. `max_length` integer `None` The maximum length of the label text. `max_length_ellipsis` string `"..."` The ellipsis to use when the label text exceeds the maximum length. `tooltip` boolean `true` Whether to show the tooltip on hover. `icons` dict `{'bluetooth_on': '\udb80\udcaf', 'bluetooth_off': '\udb80\udcb2', 'bluetooth_connected': '\udb80\udcb1'}` Icons for bluetooth widget `device_aliases` list `[]` List of device aliases. `callbacks` dict `{'on_left': 'toggle_mute', 'on_middle': 'toggle_label', 'on_right': 'do_nothing'}` Callbacks for mouse events on the bluetooth widget. `animation` dict `{'enabled': true, 'type': 'fadeInOut', 'duration': 200}` Animation settings for the widget. `container_shadow` dict `None` Container shadow options. `label_shadow` dict `None` Label shadow options.

## Example Configuration

```
bluetooth:
type:"yasb.bluetooth.BluetoothWidget"
options:
label:"<span>{icon}</span>{device_count}"
label_alt:"{device_name}"
label_no_device:"Nodevicesconnected"
label_device_separator:","
max_length:10
max_length_ellipsis:"..."
icons:
bluetooth_on:"\udb80\udcaf"
bluetooth_off:"\udb80\udcb2"
bluetooth_connected:"\udb80\udcb1"
device_aliases:

-name:"T5.0"
alias:"\uf025"
callbacks:
on_left:"toggle_label"
on_right:"execcmd.exe/cstartms-settings:bluetooth"
label_shadow:
enabled:true
color:"black"
radius:3
offset:[1,1]
```

## Description of Options

- **label:** The format string for the bluetooth widget. Displays the bluetooth icon.
- **label\_alt:** The alternative format string for the bluetooth widget. Displays list of connected devices.
- **class\_name:** Additional CSS class name for the widget. This allows for custom styling.
- **label\_no\_device:** The string to display `{device_name}` when no devices are connected.
- **label\_device\_separator:** The string to separate multiple device names.
- **max\_length:** The maximum number of characters of the label text. If the text exceeds this length, it will be truncated.
- **max\_length\_ellipsis:** The string to append to truncated label text.
- **tooltip:** Whether to show the tooltip on hover.
- **icons:** A dictionary specifying the icons for the bluetooth widget. The keys are `bluetooth_on`, `bluetooth_off`, and `bluetooth_connected`, and the values are the unicode characters for the icons.
- **device\_aliases:** A list of dictionaries specifying device aliases. Each dictionary should contain a `name` and an `alias`. The `name` is the real name of the device, and the `alias` is the text to display for that device.
- **callbacks:** A dictionary specifying the callbacks for mouse events. The keys are `on_left`, `on_middle`, and `on_right`, and the values are the names of the callback functions.
- **animation:** A dictionary specifying the animation settings for the widget. It contains three keys: `enabled`, `type`, and `duration`. The `type` can be `fadeInOut` and the `duration` is the animation duration in milliseconds.
- **container\_shadow:** Container shadow options.
- **label\_shadow:** Label shadow options.

## Example Style

```
.bluetooth-widget{}
.bluetooth-widget.your_class{}/* If you are using class_name option */
.bluetooth-widget.widget-container{}
.bluetooth-widget.label{}
.bluetooth-widget.label.alt{}
.bluetooth-widget.icon{}
```