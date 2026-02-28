---
title: YASB Reborn - Yet Another Status Bar
url: https://docs.yasb.dev/latest/widgets/server-monitor
source: crawler
fetched_at: 2026-02-23T05:28:40.641873-03:00
rendered_js: false
word_count: 0
---

```
server_monitor:
type:"yasb.server_monitor.ServerMonitor"
options:
label:"<span>\uf510</span>"
label_alt:"{online}/{offline}of{total}"
ssl_check:true
ssl_verify:true
ssl_warning:10
timeout:2
update_interval:300
desktop_notifications:
ssl:true
offline:true
servers:[
'netflix.com',
'google.com',
'subdomain.yahoo.com'
]
menu:
blur:True
round_corners:True
round_corners_type:"normal"
border_color:"System"
alignment:"right"
direction:"down"
callbacks:
on_left:"toggle_menu"
on_right:"toggle_label"
label_shadow:
enabled:true
color:"black"
radius:3
offset:[1,1]
```

```
.server-widget{
padding:06px06px
}
.server-widget.widget-container{}
.server-widget.label{}
.server-widget.icon{
font-size:14px
}
.server-widget.warning.icon{
color:#f9e2af
}
.server-widget.error.icon{
color:#f38ba8
}
.server-menu{
background-color:rgba(17,17,27,0.4);
}
.server-menu-header{
border-bottom:1pxsolidrgba(255,255,255,0.1);
}
.server-menu-header.refresh-time{
padding-left:18px;
padding-bottom:8px;
padding-top:8px;
font-family:'Segoe UI',Tahoma,Geneva,Verdana,sans-serif;
}
.server-menu-header.reload-button{
font-size:16px;
padding-right:18px;
padding-bottom:8px;
padding-top:8px;
color:#cdd6f4
}
.server-menu-container{
background-color:rgba(17,17,27,0.74);
}
.server-menu-container.row{
font-family:'Segoe UI',Tahoma,Geneva,Verdana,sans-serif;
max-height:40px;
padding:8px;
border-radius:6px;
min-width:300px;
border:1pxsolidrgba(128,128,128,0);
}
.server-menu-container.row:hover{
background-color:rgba(255,255,255,0.05);
border:1pxsolidrgba(255,255,255,0.1);
}
.server-menu-container.name{
font-size:14px;
font-weight:600;
padding:6px10px2px10px;
color:#cdd6f4;
font-family:'Segoe UI',Tahoma,Geneva,Verdana,sans-serif;
}
.server-menu-container.status{
font-size:24px;
padding-right:10px;
font-family:'Segoe UI',Tahoma,Geneva,Verdana,sans-serif;
}
.server-menu-container.details{
font-size:11px;
font-weight:600;
padding:2px10px6px10px;
color:#9399b2;
font-family:'Segoe UI',Tahoma,Geneva,Verdana,sans-serif;
}
.server-menu-container.row.online.status{
color:#09e098
}
.server-menu-container.row.offline.status{
color:#f38ba8
}
.server-menu-container.row.warning.status{
color:#ccca53
}
.server-menu-container.placeholder{
font-family:'Segoe UI',Tahoma,Geneva,Verdana,sans-serif;
font-size:16px;
font-weight:600;
color:#cdd6f4;
padding:50px8px;
min-width:300px;
background-color:transparent
}
.server-menu-overlay{
background-color:rgba(17,17,27,0.85);
}
.server-menu-overlay.text{
padding:8px;
font-family:'Segoe UI',Tahoma,Geneva,Verdana,sans-serif;
font-size:16px;
font-weight:600;
color:#cdd6f4;
}
```