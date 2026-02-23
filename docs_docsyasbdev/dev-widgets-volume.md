---
title: YASB Reborn - Yet Another Status Bar
url: https://docs.yasb.dev/dev/widgets/volume
source: crawler
fetched_at: 2026-02-23T05:20:40.102041-03:00
rendered_js: false
word_count: 0
---

```
volume:
type:"yasb.volume.VolumeWidget"
options:
label:"<span>{icon}</span>{level}"
label_alt:"{volume}"
volume_icons:

-"\ueee8"# Icon for muted
-"\uf026"# Icon for 0-10% volume
-"\uf027"# Icon for 11-30% volume
-"\uf027"# Icon for 31-60% volume
-"\uf028"# Icon for 61-100% volume
audio_menu:
blur:true
round_corners:true
round_corners_type:"normal"
border_color:"system"
alignment:"right"
direction:"down"
callbacks:
on_left:"toggle_volume_menu"
on_right:"toggle_mute"
label_shadow:
enabled:true
color:"black"
radius:3
offset:[1,1]
```

```
audio_menu:
blur:true# Enable blur effect for the menu
round_corners:true# Enable round corners for the menu (not supported on Windows 10)
round_corners_type:"normal"# Set the type of round corners for the menu (normal, small) (not supported on Windows 10)
border_color:"system"# Set the border color for the menu, "system", Hex color or None
alignment:"right"# Set the alignment of the menu (left, right, center)
direction:"down"# Set the direction of the menu (up, down)
offset_top:6# Set the top offset of the menu
offset_left:0# Set the left offset of the menu
show_apps:true# Whether to show the list of applications with audio sessions
show_app_labels:false# Whether to show application labels in the audio menu
show_app_icons:true# Whether to show application icons in the audio menu
show_apps_expanded:false# Whether application volumes are expanded by default when opening the menu
app_icons:# Icons for the toggle button to expand/collapse application volumes
toggle_down:"\uf078"# Icon for btn collapsed state
toggle_up:"\uf077"# Icon for btn expanded state
```

```
.volume-widget{}
.volume-widget.your_class{}/* If you are using class_name option */
.volume-widget.widget-container{}
.volume-widget.label{}
.volume-widget.label.alt{}
.volume-widget.icon{}
.volume-widget.label.muted{}/* Applied when audio is muted */
.volume-widget.icon.muted{}/* Applied when audio is muted */
.volume-widget.label.no-device{}/* Applied when no audio device is connected */
.volume-widget.icon.no-device{}/* Applied when no audio device is connected */
/* Volume progress bar styles if enabled */
.volume-widget.progress-circle{}
/* Audio menu styles */
.volume-widget.audio-menu{}
/* System volume */
.audio-menu.system-volume-container.volume-slider{}
.audio-menu.system-volume-container.volume-slider::groove{}
.audio-menu.system-volume-container.volume-slider::handle{}
/* Device list styles */
.audio-menu.audio-container.device{}
.audio-menu.audio-container.device.selected{}
.audio-menu.audio-container.device:hover{}
/* Toggle button for application volumes (if is enabled) */
.audio-menu.toggle-apps{}
.audio-menu.toggle-apps.expanded{}
.audio-menu.toggle-apps:hover{}
/* Container for application volumes (if is enabled) */
.audio-menu.apps-container{}/* Individual application volume container */
.audio-menu.apps-container.app-volume{}/* Individual application volume container */
.audio-menu.apps-container.app-volume:hover{}
.audio-menu.apps-container.app-volume.app-label{}/* Application label */
.audio-menu.apps-container.app-volume.app-icon-container.app-icon{}/* Application icon */
.audio-menu.apps-container.app-volume.app-slider{}/* Application volume slider */
```

```
.volume-widget.icon{
color:#74b0ff;;
margin:02px00;
}
.audio-menu{
background-color:rgba(17,17,27,0.4);
min-width:300px;
}
/* System volume */
.audio-menu.system-volume-container.volume-slider{
border:none;
}
/* Device list styles */
.audio-menu.audio-container.device{
background-color:transparent;
border:none;
padding:6px8px6px4px;
margin:2px0;
font-size:12px;
border-radius:4px;
}
.audio-menu.audio-container.device.selected{
background-color:rgba(255,255,255,0.085);

}
.audio-menu.audio-container.device:hover{
background-color:rgba(255,255,255,0.06);
}
/* Toggle button for application volumes (if is enabled) */
.audio-menu.toggle-apps{
background-color:transparent;
border:none;
padding:0;
margin:0;
min-height:24px;
min-width:24px;
border-radius:4px;
}
.audio-menu.toggle-apps.expanded{
background-color:rgba(255,255,255,0.1);
}
.audio-menu.toggle-apps:hover{
background-color:rgba(255,255,255,0.15);

}
/* Container for application volumes (if is enabled) */
.audio-menu.apps-container{
padding:8px;
margin-top:20px;
border-radius:8px;
background-color:rgba(255,255,255,0.062)
}
.audio-menu.apps-container.app-volume.app-icon-container{
min-width:40px;
min-height:40px;
max-width:40px;
max-height:40px;
border-radius:6px;
margin-right:8px;
}
.audio-menu.apps-container.app-volume.app-icon-container:hover{
background-color:rgba(255,255,255,0.1);
}
```