---
title: YASB Reborn - Yet Another Status Bar
url: https://docs.yasb.dev/dev/widgets/wifi
source: crawler
fetched_at: 2026-02-23T05:20:41.753333-03:00
rendered_js: false
word_count: 0
---

```
wifi:
type:"yasb.wifi.WifiWidget"
options:
label:"<span>{wifi_icon}</span>"
label_alt:"{wifi_name}{wifi_strength}%"
update_interval:5000
callbacks:
on_left:"toggle_menu"
on_middle:"execcmd.exe/cstartms-settings:network"
on_right:"toggle_label"
ethernet_label:"<span>{wifi_icon}</span>"
ethernet_label_alt:"<span>{wifi_icon}</span>{ip_addr}"
ethernet_icon:"\ueba9"
get_exact_wifi_strength:false# Optional. Will require location access permission if true.
wifi_icons:[
"\udb82\udd2e",# Icon for 0% strength
"\udb82\udd1f",# Icon for 1-24% strength
"\udb82\udd22",# Icon for 25-49% strength
"\udb82\udd25",# Icon for 50-74% strength
"\udb82\udd28"# Icon for 75-100% strength
]
label_shadow:
enabled:true
color:"black"
radius:3
offset:[1,1]
menu_config:
blur:true
round_corners:true
round_corners_type:"normal"
border_color:"System"
alignment:"right"
direction:"down"
offset_top:6
offset_left:0
wifi_icons_secured:[
"\ue670",
"\ue671",
"\ue672",
"\ue673",
]
wifi_icons_unsecured:[
"\uec3c",
"\uec3d",
"\uec3e",
"\uec3f",
]
```

```
.wifi-widget{}
.wifi-widget.your_class{}/* If you are using class_name option */
.wifi-widget.widget-container{}
.wifi-widget.widget-container.label{}
.wifi-widget.widget-container.label.alt{}
.wifi-widget.widget-container.icon{}
```

```
.wifi-menu{}
.wifi-menu.progress-bar{}
.wifi-menu.header{}
.wifi-menu.error-message{}
.wifi-menu.wifi-list{}
.wifi-menu.wifi-item{}
.wifi-menu.wifi-item[active=true]{}
.wifi-menu.wifi-item.icon{}
.wifi-menu.wifi-item.name{}
.wifi-menu.wifi-item.password{}
.wifi-menu.wifi-item.status{}
.wifi-menu.wifi-item.strength{}
.wifi-menu.wifi-item.controls-container{}
.wifi-menu.wifi-item.connect{}
.wifi-menu.footer{}
.wifi-menu.footer.settings-button{}
.wifi-menu.footer.refresh-icon{}

/* Right click menu style */
.context-menu{}
.context-menu.menu-checkbox{}
.context-menu.menu-checkbox.checkbox{}
.context-menu::item{}
```

```
.wifi-menu{
font-family:'Segoe UI';
background-color:rgba(17,17,27,0.4);
max-height:350px;
min-height:375px;
min-width:375px;
}

.wifi-menu.progress-bar{
max-height:2px;
color:#4cc2ff;
}

.wifi-menu.header{
font-family:'Segoe UI';
font-size:14px;
font-weight:600;
margin-bottom:2px;
padding:12px;
background-color:rgba(17,17,27,0.6);
color:white;
border-bottom:1pxsolidrgba(255,255,255,0.1);
}

.wifi-menu.error-message{
font-family:'Segoe UI';
font-size:14px;
font-weight:600;
margin-bottom:2px;
padding:12px;
background-color:red;
color:white;
border-bottom:1pxsolidrgba(255,255,255,0.1);
}

.wifi-menu.wifi-list{
background-color:rgba(17,17,27,0.8);
margin-right:3px;
}

.wifi-menu.wifi-item{
min-height:35px;
padding:2px12px;
margin:2px4px;
}

.wifi-menu.wifi-item:hover{
background-color:rgba(255,255,255,0.05);
border-radius:6px;
}

.wifi-menu.wifi-item[active=true]{
background-color:rgba(255,255,255,0.15);
font-size:14px;
border-radius:6px;
min-height:80px;
}

.wifi-menu.wifi-item.icon{
font-family:'Segoe Fluent Icons';
font-size:26px;
margin-right:10px;
}

.wifi-menu.wifi-item.name{
font-family:'Segoe UI';
font-size:14px;
margin-right:10px;
}

.wifi-menu.wifi-item.password{
font-family:'Segoe UI';
background-color:transparent;
font-size:14px;
}

.wifi-menu.wifi-item.status{
font-family:'Segoe UI';
font-size:14px;
}

.wifi-menu.wifi-item.strength{
font-family:'Segoe UI';
font-size:14px;
}

.wifi-menu.wifi-item.controls-container{
padding-top:8px;
}

.wifi-menu.wifi-item.connect{
background-color:rgba(255,255,255,0.15);
padding:4px30px;
border-radius:4px;
border:none;
font-size:14px;
}

.wifi-menu.wifi-item.connect:hover{
background-color:rgba(255,255,255,0.2);
}

.wifi-menu.wifi-item.connect:pressed{
background-color:rgba(255,255,255,0.3);
}

.wifi-menu.footer{
font-size:12px;
font-weight:600;
padding:12px;
margin-top:2px;
color:#9399b2;
background-color:rgba(17,17,27,0.6);
border-top:1pxsolidrgba(255,255,255,0.1);
}

.wifi-menu.footer.settings-button{
font-family:'Segoe UI';
background-color:transparent;
border:none;
padding:02px;
min-width:26px;
min-height:26px;
color:#fff;
}

.wifi-menu.footer.refresh-icon{
font-family:'Segoe Fluent Icons';
background-color:transparent;
border:none;
min-width:26px;
min-height:26px;
color:#fff;
}

.wifi-menu.footer.refresh-icon:hover{
background-color:rgba(255,255,255,0.1);
border-radius:4px;
}
```