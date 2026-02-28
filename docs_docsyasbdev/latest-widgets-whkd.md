---
title: YASB Reborn - Yet Another Status Bar
url: https://docs.yasb.dev/latest/widgets/whkd
source: crawler
fetched_at: 2026-02-23T05:28:48.256498-03:00
rendered_js: false
word_count: 259
---

Whkd is a simple hotkey daemon for Windows that reacts to input events by executing commands. More information can be found [here](https://github.com/LGUG2Z/whkd).

Option Type Default Description `label` string `"\uf11c"` The string for the label button. `special_keys` list `None` A list of special keys to be used as hotkeys. `animation` dict `{'enabled': true, 'type': 'fadeInOut', 'duration': 200}` Animation settings for the widget. `container_shadow` dict `None` Container shadow options. `label_shadow` dict `None` Label shadow options.

## Example Configuration

```
whkd:
type:"yasb.whkd.WhkdWidget"
options:
label:"<span>\uf11c</span>"
special_keys:

-key:"win"
key_replace:"\ue70f"

-key:"ctrl"
key_replace:"Ctrl"

-key:"alt"
key_replace:"Alt"

-key:"shift"
key_replace:"Shift"

-key:"left"
key_replace:"\u2190"

-key:"right"
key_replace:"\u2192"

-key:"up"
key_replace:"\u2191"

-key:"down"
key_replace:"\u2193"
label_shadow:
enabled:true
color:"black"
radius:3
offset:[1,1]
```

## Description of Options

- **label:** The string for the label button.
- **special\_keys:** A list of special keys to be used as hotkeys. The list contains dictionaries with two keys: `key` and `key_replace`. The `key` is the special key to be used as a hotkey and the `key_replace` is the string to replace the special key with.
- **key:** The special key to be used as a hotkey.
- **key\_replace:** The string to replace the special key with.
- **animation:** A dictionary specifying the animation settings for the widget. It contains three keys: `enabled`, `type`, and `duration`. The `type` can be `fadeInOut` and the `duration` is the animation duration in milliseconds.
- **container\_shadow:** Container shadow options.
- **label\_shadow:** Label shadow options.

> \[!NOTE]  
> The special keys are keys which you can style and replace with custom icons. Special keys settings are optional. If you don't want to use special keys, you can leave the `special_keys` option empty.
> 
> \[!NOTE]  
> To use header like on screenshot below, you need to edit whkdrc and comment string with double hash `##`. Example `## Open Applications`

## Style

```
.whkd-widget{}
.whkd-widget.windget-container{}
.whkd-widget.label{}
.whkd-widget.icon{}
.whkd-popup{}
.whkd-popup.edit-config-button{}
.whkd-popup.keybind-buttons-container{}
.whkd-popup.keybind-button{}
.whkd-popup.keybind-button.special{}
.whkd-popup.keybind-row{}
.whkd-popup.plus-separator{}
.whkd-popup.filter-input{}
.whkd-popup.keybind-command{}
.whkd-popup.keybind-header{}
```

## Example Styling

```
.whkd-widget{
padding:06px06px;
}
.whkd-widget.icon{
font-size:18px;
}
.whkd-popup.edit-config-button{
background-color:#1743a1;
color:#ffffff;
padding:4px8px6px8px;
font-size:14px;
font-weight:600;
border-radius:4px;
font-family:'Segoe UI',sans-serif;
}

.whkd-popup.keybind-buttons-container{
min-width:240px;
}
.whkd-popup.keybind-button{
background-color:#343538;
color:white;
padding:4px8px6px8px;
font-size:14px;
font-weight:600;
border:1pxinset#4f5055;
border-bottom:2pxinset#4f5055;
border-radius:4px;
font-family:'JetBrainsMono NFP';
}
.whkd-popup.keybind-button.special{
background-color:#343538;
}
.whkd-popup.keybind-row:hover{
background-color:rgba(136,138,155,0.2);
border-radius:8px;
}
.whkd-popup.plus-separator{
padding:00px;
border:none;
font-size:16px;
font-weight:bold;
background-color:transparent
}
.whkd-popup.filter-input{
padding:08px2px8px;
font-size:14px;
font-family:'Segoe UI',sans-serif;
border:1pxsolid#2e2e2e;
border-radius:4px;
outline:none;
color:white;
background-color:#2e2e2e;
min-height:32px;
}
.whkd-popup.filter-input:focus{
border:1pxsolid#0078D4;
}
.whkd-popup.keybind-command{
font-size:14px;
}
.whkd-popup.keybind-header{
font-size:16px;
font-weight:600;
color:white;
padding:8px0;
margin-top:20px;
background-color:rgba(255,255,255,0.05);
border:1pxsolidrgba(255,255,255,0.1);
border-radius:8px;
}
```

## Preview of the WHKD card

![YASB WHKD Widget](https://docs.yasb.dev/latest/widgets/assets/765432109-1a2b3c4d-5e6f-78ab-9012-3456789abcd.png)