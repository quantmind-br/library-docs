---
title: YASB Reborn - Yet Another Status Bar
url: https://docs.yasb.dev/latest/widgets/taskbar
source: crawler
fetched_at: 2026-02-23T05:28:43.214409-03:00
rendered_js: false
word_count: 0
---

```
taskbar:
type:"yasb.taskbar.TaskbarWidget"
options:
icon_size:16
tooltip:true
show_only_visible:false
strict_filtering:true
monitor_exclusive:false
animation:
enabled:true
preview:
enabled:false
width:240
delay:400
padding:8
margin:8
title_label:
enabled:false
show:"always"
min_length:10
max_length:30
ignore_apps:
processes:[]
titles:[]
classes:[]
```

```
.taskbar-widget{}/* Main container for the taskbar widget */
.taskbar-widget.widget-container{}/* Container for the widget */
/* Application containers */
.taskbar-widget.app-container{}/* container for each app */
.taskbar-widget.app-container.foreground{}/* container for the focused app */
.taskbar-widget.app-container.flashing{}/* flashing container for the app (window is flashing) */
.taskbar-widget.app-container.running{}/* container for running apps (not focused) */
.taskbar-widget.app-container.app-icon{}/* Icon inside the container */
.taskbar-widget.app-container.app-title{}/* Label inside the container */
/* Taskbar preview popup is very limited in styling options, do not use margins/paddings here */
.taskbar-preview{}
.taskbar-preview.header{}
.taskbar-preview.header.title{}
.taskbar-preview.close-button{}/* Close button on the preview */
```

```
.taskbar-widget.app-container{
margin:4px2px;
border-radius:4px;
padding:04px;
}
.taskbar-widget.app-container.foreground{
background-color:rgba(255,255,255,0.1);
}
.taskbar-widget.app-container.flashing{
background-color:rgba(255,106,106,0.63);
}
.taskbar-widget.app-container.running{
background-color:rgba(255,255,255,0.25);
}
.taskbar-widget.app-container:hover{
background-color:rgba(255,255,255,0.15);
}
.taskbar-widget.app-container.app-title{
padding-left:4px;
}
/* Taskbar preview popup is very limited in styling options, do not use margins/paddings here */
.taskbar-preview{
border-radius:8px;
background-color:#2b2c2d;
}
.taskbar-preview.flashing{
background-color:#7f434a;
}
.taskbar-preview.header{
padding-bottom:12px;
padding-top:4px;
}
.taskbar-preview.header.title{
color:#d6d6d6;
font-family:"Segoe UI";
font-weight:600;
font-size:13px;
}
.taskbar-preview.close-button{
color:#999;
font-size:20px;
background-color:transparent;
border:none;
min-width:20px;
border-radius:4px;
min-height:20px;
}
.taskbar-preview.close-button:hover{
color:rgb(255,255,255);
background-color:rgb(226,0,0);
}
```