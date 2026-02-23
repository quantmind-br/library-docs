---
title: YASB Reborn - Yet Another Status Bar
url: https://docs.yasb.dev/dev/widgets/traffic
source: crawler
fetched_at: 2026-02-23T05:20:37.092793-03:00
rendered_js: false
word_count: 0
---

```
traffic:
type:"yasb.traffic.TrafficWidget"
options:
label:"\ueb01\ueab4{download_speed}|\ueab7{upload_speed}"
label_alt:"Download{download_speed}|Upload{upload_speed}"
update_interval:1000
menu:
blur:true
round_corners:true
round_corners_type:"normal"
border_color:"system"
alignment:"left"
direction:"down"
offset_top:6
offset_left:0
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
/* Main widget styling */
.traffic-widget{}
.traffic-widget.your_class{}/* If you are using class_name option */
.traffic-widget.widget-container{}
.traffic-widget.label{}
.traffic-widget.label.offline{}/* offline state */
.traffic-widget.label.alt{}
.traffic-widget.icon{}
.traffic-widget.icon.offline{}/* offline state */

/* Menu styling */
.traffic-menu{}
.traffic-menu.header{}
.traffic-menu.header.title{}
.traffic-menu.header.resset-button{}
.traffic-menu.interface-info{}
.traffic-menu.internet-info{}
.traffic-menu.internet-info.checking{}
.traffic-menu.internet-info.connected{}
.traffic-menu.internet-info.disconnected{}

/* Section-specific styling */
.traffic-menu.section{}
.traffic-menu.section-title{}
.traffic-menu.section.speeds-section{}
.traffic-menu.section.session-section{}
.traffic-menu.section.today-section{}
.traffic-menu.section.alltime-section{}

/* Speed columns styling */
.traffic-menu.upload-speed,
.traffic-menu.download-speed{}

/* Speed columns values and units styling */
.traffic-menu.upload-speed-value{}
.traffic-menu.download-speed-value{}
.traffic-menu.upload-speed-unit{}
.traffic-menu.download-speed-unit{}
.traffic-menu.upload-speed-placeholder{}
.traffic-menu.download-speed-placeholder{}

/* Separator styling between upload and download speeds columns */
.traffic-menu.speed-separator{}

/* Text labels styling */
.traffic-menu.data-text{}
.traffic-menu.data-text.session-upload-text,
.traffic-menu.data-text.session-download-text,
.traffic-menu.data-text.session-duration-text,
.traffic-menu.data-text.today-upload-text,
.traffic-menu.data-text.today-download-text,
.traffic-menu.data-text.alltime-upload-text,
.traffic-menu.data-text.alltime-download-text{}

/* Value labels styling */
.traffic-menu.data-value{}
.traffic-menu.data-value.session-upload-value,
.traffic-menu.data-value.session-download-value,
.traffic-menu.data-value.session-duration-value,
.traffic-menu.data-value.today-upload-value,
.traffic-menu.data-value.today-download-value,
.traffic-menu.data-value.alltime-upload-value,
.traffic-menu.data-value.alltime-download-value{}
```

```
.traffic-menu{
background-color:rgba(24,25,27,0.85);
min-width:280px;
}
.traffic-menu.header{
border-bottom:1pxsolidrgba(255,255,255,0.1);
background-color:rgba(24,25,27,0.8);
}
.traffic-menu.header.title{
padding:8px;
font-size:16px;
font-weight:600;
font-family:'Segoe UI';
color:#ffffff
}
.traffic-menu.header.reset-button{
font-size:11px;
padding:4px8px;
margin-right:8px;
font-family:'Segoe UI';
border-radius:4px;
font-weight:600;
background-color:transparent;
border:none;
}
.traffic-menu.reset-button:hover{
color:#ffffff;
background-color:rgba(255,255,255,0.05);
border:1pxsolidrgba(255,255,255,0.1);
}
.traffic-menu.reset-button:pressed{
color:#ffffff;
background-color:rgba(255,255,255,0.1);
border:1pxsolidrgba(255,255,255,0.2);
}
/* Speed column styles */
.traffic-menu.download-speed,
.traffic-menu.upload-speed{
background-color:transparent;
padding:4px10px;
margin-right:12px;
margin-left:12px;
margin-top:16px;
margin-bottom:0;
border-bottom:1pxsolidrgba(255,255,255,0.2);
}
.traffic-menu.download-speed{
margin-left:12px;
margin-right:12px;
}
.traffic-menu.speed-separator{
max-width:1px;
background-color:rgba(255,255,255,0.2);
margin:32px016px0;
}
.traffic-menu.upload-speed-value,
.traffic-menu.download-speed-value{
font-size:24px;
font-weight:900;
font-family:'Segoe UI';
color:#bcc2c5;
}
.traffic-menu.upload-speed-unit,
.traffic-menu.download-speed-unit{
font-size:13px;
font-family:'Segoe UI';
font-weight:600;
padding-top:4px;
}
.traffic-menu.upload-speed-placeholder,
.traffic-menu.download-speed-placeholder{
color:#747474;
font-size:11px;
font-family:'Segoe UI';
padding:004px0;
}

/* Section and data styles */
.traffic-menu.section-title{
font-size:12px;
font-weight:600;
color:#7c8192;
margin-bottom:4px;
font-family:'Segoe UI';
}
.traffic-menu.session-section,
.traffic-menu.today-section,
.traffic-menu.alltime-section{
margin:8px8px08px;
padding:010px10px10px;
background-color:transparent;
border-bottom:1pxsolidrgba(255,255,255,0.1);
}
.traffic-menu.data-text{
font-size:13px;
color:#afb5cc;
padding:2px0;
font-family:'Segoe UI';

}
.traffic-menu.data-value{
font-weight:600;
font-size:13px;
font-family:'Segoe UI';
padding:2px0;
}

/* Interface and Internet info styles */
.traffic-menu.interface-info,
.traffic-menu.internet-info{
font-size:12px;
color:#6f7486;
padding:8px0;
font-family:'Segoe UI';
}
.traffic-menu.internet-info{
background-color:rgba(68,68,68,0.1);
}
.traffic-menu.internet-info.connected{
background-color:rgba(166,227,161,0.096);
color:#a6e3a1;
}
.traffic-menu.internet-info.disconnected{
background-color:rgba(243,139,168,0.1);
color:#f38ba8;
}
```