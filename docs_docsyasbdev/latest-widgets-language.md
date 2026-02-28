---
title: YASB Reborn - Yet Another Status Bar
url: https://docs.yasb.dev/latest/widgets/language
source: crawler
fetched_at: 2026-02-23T05:28:38.652784-03:00
rendered_js: false
word_count: 36
---

The `callbacks` option allows you to define custom actions for mouse events on the widget. The keys are:

The `language_menu` option allows you to configure the popup menu for language selection. It accepts the following keys:

```
language:
type:"yasb.language.LanguageWidget"
options:
label:"{lang[language_code]}-{lang[country_code]}"
label_alt:"{lang[full_name]}"
update_interval:5
callbacks:
on_left:"toggle_menu"
on_middle:"do_nothing"
on_right:"toggle_label"
language_menu:
blur:true
round_corners:true
round_corners_type:"normal"
border_color:"system"
alignment:"right"
direction:"down"
offset_top:6
offset_left:0
show_layout_icon:true
layout_icon:"\uf11c"
label_shadow:
enabled:true
color:"black"
radius:3
offset:[1,1]
```

```
.language-widget{}
.language-widget.your_class{}/* If you are using class_name option */
.language-widget.widget-container{}
.language-widget.widget-container.caps-lock-on{}/* If Caps Lock is on */
.language-widget.label{}
.language-widget.label.alt{}
.language-widget.icon{}
.language-widget.widget-container.caps-lock-on.label{}/* If Caps Lock is on */
.language-widget.widget-container.caps-lock-on.icon{}/* If Caps Lock is on */

/* Language Menu */
.language-menu{}
.language-menu.header{}
.language-menu.footer{}
.language-menu.language-item{}
.language-menu.language-item.active{}
.language-menu.language-item.code{}
.language-menu.language-item.icon{}
.language-menu.language-item.name{}
.language-menu.language-item.layout{}
```

```
.language-menu{
background-color:rgba(17,17,27,0.4);
min-width:300px;
}
.language-menu.header{
font-family:'Segoe UI';
font-size:14px;
font-weight:600;
margin-bottom:2px;
padding:12px;
background-color:rgba(17,17,27,0.6);
border-bottom:1pxsolidrgba(255,255,255,0.1);
}
.language-menu.footer{
font-family:'Segoe UI';
font-size:12px;
font-weight:600;
padding:12px;
margin-top:2px;
color:#9399b2;
background-color:rgba(17,17,27,0.6);
border-top:1pxsolidrgba(255,255,255,0.1);
}
.language-menu.footer:hover{
background-color:rgba(36,36,51,0.6);
color:#fff;
}
.language-menu.language-item{
padding:6px12px;
margin:2px4px;
}
.language-menu.language-item.active{
background-color:rgba(255,255,255,0.1);
border-radius:4px;
}
.language-menu.language-item:hover{
background-color:rgba(255,255,255,0.05);
}
.language-menu.language-item.active:hover{
background-color:rgba(255,255,255,0.1);
border-radius:4px;
}
.language-menu.language-item.code{
font-weight:900;
font-size:14px;
min-width:40px;
text-transform:uppercase;
}
.language-menu.language-item.icon{
font-size:16px;
margin-right:8px;
color:#fff;
}
.language-menu.language-item.name{
font-weight:600;
font-family:'Segoe UI';
font-size:14px;
}
.language-menu.language-item.layout{
font-weight:600;
font-family:'Segoe UI';
font-size:12px;
}
```