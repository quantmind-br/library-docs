---
title: YASB Reborn - Yet Another Status Bar
url: https://docs.yasb.dev/latest/widgets/komorebi-control
source: crawler
fetched_at: 2026-02-23T05:28:48.716487-03:00
rendered_js: false
word_count: 33
---

*This widget provides a control interface for Komorebi, allowing users to start, stop, and reload the application. It also includes options for running AutoHotKey and WHKD, as well as displaying the Komorebi version.*

```
komorebi_control:
type:"komorebi.control.KomorebiControlWidget"
options:
label:"<span>\udb80\uddd9</span>"
icons:
start:"\uead3"
stop:"\uead7"
reload:"\uead2"
run_ahk:false
run_whkd:false
run_masir:false
show_version:true
komorebi_menu:
blur:true
round_corners:true
round_corners_type:'normal'
border_color:'System'
alignment:'left'
direction:'down'
offset_top:6
offset_left:0
label_shadow:
enabled:true
color:"black"
radius:3
offset:[1,1]
```

```
.komorebi-control-widget{}
.komorebi-control-widget.widget-container{}
.komorebi-control-widget.widget-container.label{}
.komorebi-control-widget.widget-container.icon{}
/* Komorebi Menu */
.komorebi-control-menu{}
.komorebi-control-menu.button{}
.komorebi-control-menu.button:hover{}
.komorebi-control-menu.button.start{}
.komorebi-control-menu.button.stop{}
.komorebi-control-menu.button.reload{}
.komorebi-control-menu.button.active{}
.komorebi-control-menu.button:disabled{}
.komorebi-control-menu.footer{}
.komorebi-control-menu.footer.text{}
```

```
.komorebi-control-widget.label{
font-size:14px;
color:#cdd6f4;
font-weight:600;
}
.komorebi-control-menu{
background-color:rgba(17,17,27,0.2);
}
.komorebi-control-menu.button{
color:rgba(162,177,199,0.4);
padding:8px16px;
font-size:32px;
border-radius:8px;
background-color:rgba(255,255,255,0.04);
}
.komorebi-control-menu.button.active{
color:rgb(228,228,228);
background-color:rgba(255,255,255,0.04);
}
.komorebi-control-menu.button:disabled,
.komorebi-control-menu.button.active:disabled{
background-color:rgba(255,255,255,0.01);
color:rgba(255,255,255,0.2);
}
.komorebi-control-menu.footer.text{
font-size:12px;
color:#6c7086;
}
```