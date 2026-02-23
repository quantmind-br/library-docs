---
title: YASB Reborn - Yet Another Status Bar
url: https://docs.yasb.dev/dev/widgets/microphone
source: crawler
fetched_at: 2026-02-23T05:20:35.47583-03:00
rendered_js: false
word_count: 0
---

```
microphone:
type:"yasb.microphone.MicrophoneWidget"
options:
label:"<span>{icon}</span>"
label_alt:"<span>{icon}</span>{level}"
mute_text:"mute"
icons:
normal:"\uf130"
muted:"\uf131"
mic_menu:
blur:true
round_corners:true
round_corners_type:"normal"
border_color:"system"
alignment:"right"
direction:"down"
callbacks:
on_left:"toggle_mic_menu"
on_middle:"toggle_label"
on_right:"toggle_mute"
label_shadow:
enabled:true
color:"black"
radius:3
offset:[1,1]
```

```
.microphone-widget{}
.microphone-widget.your_class{}/* If you are using class_name option */
.microphone-widget.widget-container{}
.microphone-widget.label{}
.microphone-widget.label.alt{}
.microphone-widget.icon{}
.microphone-widget.label.muted{}/* Applied when microphone is muted */
.microphone-widget.icon.muted{}/* Applied when microphone is muted */
.microphone-widget.label.no-device{}/* Applied when no microphone device is connected */
.microphone-widget.icon.no-device{}/* Applied when no microphone device is connected */
/* Microphone progress bar styles if enabled */
.microphone-widget.progress-circle{}
/* Microphone menu styles */
.microphone-widget.microphone-menu{}
/* System microphone volume */
.microphone-menu.system-volume-container.volume-slider{}
.microphone-menu.system-volume-container.volume-slider::groove{}
.microphone-menu.system-volume-container.volume-slider::handle{}
/* Device list styles (if multiple microphones) */
.microphone-menu.microphone-container.device{}
.microphone-menu.microphone-container.device.selected{}
.microphone-menu.microphone-container.device:hover{}
```

```
.microphone-widget.icon{
color:#ff6b6b;
margin:02px00;
}
.microphone-menu{
background-color:rgba(17,17,27,0.4);
min-width:300px;
}
/* System microphone volume */
.microphone-menu.system-volume-container.volume-slider{
border:none;
}
/* Device list styles */
.microphone-menu.microphone-container.device{
background-color:transparent;
border:none;
padding:6px8px6px4px;
margin:2px0;
font-size:12px;
border-radius:4px;
}
.microphone-menu.microphone-container.device.selected{
background-color:rgba(255,255,255,0.085);
}
.microphone-menu.microphone-container.device:hover{
background-color:rgba(255,255,255,0.06);
}
```