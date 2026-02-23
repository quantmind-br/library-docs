---
title: YASB Reborn - Yet Another Status Bar
url: https://docs.yasb.dev/latest/widgets/home
source: crawler
fetched_at: 2026-02-23T05:18:02.273309-03:00
rendered_js: false
word_count: 0
---

```
home:
type:"yasb.home.HomeWidget"
options:
label:"<span>\udb81\udf17</span>"
menu_list:

-{ title:"UserHome", path:"~"}
-{ title:"Download", path:"D:\\Downloads"}
-{ title:"Documents", path:"C:\\Users\\amn\\Documents"}
-{ title:"Pictures", path:"C:\\Users\\amn\\Pictures"}
-{ title:"SoundSettings", command:"cmd.exe/cstartms-settings:sound"}
-{ title:"WindowsSettings", uri:"ms-settings:"}
-{ separator:true}
-{ title:"PowerShell", command:"powershell.exe", show_window:true}
-{ title:"WingetUpdate", command:"powershell.exe", args:["-NoProfile","-NoExit","-Command","wingetupgrade"], show_window:true}
system_menu:true
power_menu:true
blur:true
round_corners:true
round_corners_type:"normal"
border_color:"System"
offset_top:6
offset_left:0
alignment:"left"
direction:"down"
menu_labels:
shutdown:"Shutdown"
restart:"Restart"
hibernate:"Hibernate"
logout:"Logout"
lock:"Lock"
sleep:"Sleep"
system:"SystemSettings"
about:"AboutThisPC"
task_manager:"TaskManager"
label_shadow:
enabled:true
color:"black"
radius:3
offset:[1,1]
```

```
.home-widget{
padding:04px012px;
}
.home-widget.icon{
color:#b4befe;
}
.home-widget.icon:hover{
color:#cdd6f4;
}
.home-menu{
background-color:rgba(17,17,27,0.5);
}
.home-menu.menu-item{
padding:6px48px7px16px;
font-size:12px;
font-family:'Segoe UI',Tahoma,Geneva,Verdana,sans-serif;
color:var(--text);
font-weight:600;
}
.home-menu.menu-item:hover{
background-color:rgba(128,130,158,0.15);
color:#fff;
}
.home-menu.separator{
max-height:1px;
background-color:rgba(128,130,158,0.3);
}
```