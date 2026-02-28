---
title: YASB Reborn - Yet Another Status Bar
url: https://docs.yasb.dev/latest/widgets/clock
source: crawler
fetched_at: 2026-02-23T05:28:33.383623-03:00
rendered_js: false
word_count: 0
---

```
clock:
type:"yasb.clock.ClockWidget"
options:
label:"<span>{icon}</span><span>{alarm}</span>{%H:%M:%S}"
label_alt:"\uf017{%d-%m-%y%H:%M:%S}"
locale:""
update_interval:1000
timezones:[]
icons:
clock_01 :"\udb85\udc3f"
clock_02 :"\udb85\udc40"
clock_03 :"\udb85\udc41"
clock_04 :"\udb85\udc42"
clock_05 :"\udb85\udc43"
clock_06 :"\udb85\udc44"
clock_07 :"\udb85\udc45"
clock_08 :"\udb85\udc46"
clock_09 :"\udb85\udc47"
clock_10 :"\udb85\udc48"
clock_11 :"\udb85\udc49"
clock_12 :"\udb85\udc4a"
clock_16 :"SNACKTIME!"
clock_21 :"Zzz..."
clock_22 :"Zzz..."
clock_23 :"Zzz..."
alarm_icons:
enabled:"\uf0f3"
disabled:"\uf0a2"
snooze:"\uf1f6"
calendar:
blur:true
round_corners:true
round_corners_type:"normal"
border_color:"system"
alignment:"center"
direction:"down"
offset_top:6
offset_left:0
show_holidays:false
show_week_numbers:true
show_years:true
country_code:"AR"
holiday_color:"#FF6464"
extended:false
callbacks:
on_left:"toggle_calendar"
on_middle:"next_timezone"
on_right:"toggle_label"
container_padding:
top:0
left:0
bottom:0
right:0
label_shadow:
enabled:true
color:"black"
radius:3
offset:[1,1]
```

```
/* Clock widget base styles */
.clock-widget{}
/* If you are using class_name option, you can add custom styles here */
.clock-widget.your_class{}
.clock-widget.widget-container{}
.clock-widget.icon{}
.clock-widget.icon.clock_02{}
.clock-widget.label{}
.clock-widget.label.clock_15{}
.clock-widget.label.alarm{}
.clock-widget.label.alarm.snooze{}
.clock-widget.icon.alarm{}
.clock-widget.icon.alarm.snooze{}

/* All popup window in this widget share the .clock-popup base class */
/* Calendar popup styles */
.clock-popup.calendar{}
.clock-popup.calendar.calendar-layout{}
.clock-popup.calendar.calendar-table{}
.clock-popup.calendar.calendar-table::item{}
.clock-popup.calendar.calendar-table::item:selected{}
.clock-popup.calendar.day-label{}
.clock-popup.calendar.year-label{}
.clock-popup.calendar.month-label{}
.clock-popup.calendar.date-label{}
.clock-popup.calendar.week-label{}
.clock-popup.calendar.holiday-label{}
.clock-popup.calendar.extended-container{}
.clock-popup.calendar.upcoming-events-item{}
.clock-popup.calendar.upcoming-events-header{}

/* Alarm/Timer dialog styles */
.clock-popup{}
.clock-popup.alarm{}
.clock-popup.timer{}
.clock-popup.clock-popup-container{}
.clock-popup.clock-popup-footer{}
.clock-popup.clock-label-timer{}
.clock-popup.clock-input-time{}
.clock-popup.clock-input-time.colon{}
.clock-popup.alarm-input-title{}
.clock-popup.button{}
.clock-popup.button.day{}
.clock-popup.button.quick-option{}
.clock-popup.button.is-alarm-enabled{}
.clock-popup.button.is-alarm-disabled{}
.clock-popup.button.save{}
.clock-popup.button.cancel{}
.clock-popup.button.delete{}
.clock-popup.button.start{}
.clock-popup.button.alarm.small{}
.clock-popup.button.timer.small{}

/* Active alarm popup styles */
.active-alarm-window{}
.active-alarm-window.alarm-title-icon{}
.active-alarm-window.alarm-title{}
.active-alarm-window.alarm-info{}
.active-alarm-window.button{}

/* Context menu styles use global styles. For more info, see https://github.com/amnweb/yasb/wiki/Styling#context-menu-styling */
```

```
/* Clock Widget Styles */
.clock-widget{
padding:04px00px;
}
.clock-widget.icon{
color:#89dceb;
font-size:14px;
padding-right:4px;
}
.clock-widget.icon.alarm{
color:#f38ba8;
margin-left:4px;
}
.clock-widget.label{
color:#89dceb;
}
.clock-widget.label.alarm{
color:#74b0ff;
margin-left:4px;
}

/* Calendar, Alarm, and Timer Popups */
.clock-popup.alarm,
.clock-popup.timer,
.clock-popup.calendar{
min-width:460px;
background-color:rgba(17,17,27,0.4);
}

.clock-popup.calendar.calendar-table,
.clock-popup.calendar.calendar-table::item{
background-color:rgba(17,17,27,0);
color:rgba(162,177,196,0.85);
font-family:'Segoe UI';
margin:0;
padding:0;
border:none;
outline:none;
}
.clock-popup.calendar.calendar-table::item:selected{
color:#282936;
font-weight:bold;
background-color:#74b0ff;
border-radius:12px;
}
.clock-popup.calendar.day-label{
margin-top:20px;
}
.clock-popup.calendar.day-label,
.clock-popup.calendar.month-label,
.clock-popup.calendar.year-label,
.clock-popup.calendar.date-label{
font-family:'Segoe UI';
font-size:16px;
color:#fff;
font-weight:700;
min-width:180px;
max-width:180px;
}
.clock-popup.calendar.month-label{
font-weight:normal;
}
.clock-popup.calendar.year-label{
font-weight:normal;
}
.clock-popup.calendar.date-label{
font-size:88px;
font-weight:900;
color:rgb(255,255,255);
margin-top:-20px;
}
.clock-popup.calendar.extended-container{
border-left:1pxsolidrgba(255,255,255,0.2);
background-color:transparent;
padding-left:16px;
}
.clock-popup.calendar.extended-container.button.alarm.small,
.clock-popup.calendar.extended-container.button.timer.small{
min-width:32px;
min-height:16px;
font-size:12px;
padding:4px8px;
border-radius:2px;
}
.clock-popup.calendar.extended-container.upcoming-events-header{
font-size:12px;
font-family:'Segoe UI';
font-weight:600;
margin:4px08px0;
color:#d2d6e2;
}
.clock-popup.calendar.extended-container.upcoming-events-item{
font-size:12px;
font-family:'Segoe UI';
font-weight:600;
padding:3px0;
color:#b2b6c0;
}
.clock-popup.calendar.extended-container.upcoming-events-item:hover{
color:#ced1d8;
}

/* Alarm and Timer Dialog Containers */
.clock-popup.timer.clock-popup-container,
.clock-popup.alarm.clock-popup-container{
padding:16px;
}
.clock-popup.timer.clock-popup-footer,
.clock-popup.alarm.clock-popup-footer{
padding:16px;
border-top:1pxsolidrgb(0,0,0);
background-color:rgba(0,0,0,0.3);
}
.clock-popup.clock-label-timer{
font-size:13px;
font-family:'Segoe UI';
font-weight:600;
color:#8d9196;
}
.clock-popup.clock-input-time{
font-size:48px;
background-color:transparent;
border:none;
font-family:monospace,"Tahoma","Segoe UI";
font-weight:600;
color:#ced3d8;
}
.clock-popup.clock-input-time.colon{
padding-bottom:8px;
}

/* Dialog Buttons */
.clock-popup.button{
border-radius:4px;
font-family:'Segoe UI';
font-weight:600;
font-size:13px;
min-height:28px;
min-width:64px;
margin:4px0;
background-color:rgba(255,255,255,0.1);
}
.clock-popup.button.save,
.clock-popup.button.start,
.clock-popup.button.delete,
.clock-popup.button.cancel{
min-width:120px;
}

.clock-popup.button.save,
.clock-popup.button.start{
background-color:rgba(0,110,255,0.5);
margin-right:8px;
}

.clock-popup.button.save:hover,
.clock-popup.button.start:hover{
background-color:rgba(0,110,255,0.7);
}
.clock-popup.button.delete{
background-color:rgba(255,80,80,0.5);
}
.clock-popup.button.delete:hover{
background-color:rgba(255,80,80,0.7);
}
.clock-popup.button.is-alarm-enabled{
background-color:rgba(0,110,255,0.5);
}
.clock-popup.button.is-alarm-enabled:hover{
background-color:rgba(0,110,255,0.7);
}
.clock-popup.button.is-alarm-disabled{
background-color:rgba(255,255,255,0.2);
}
.clock-popup.button.day{
background-color:rgba(255,255,255,0.1);
max-height:20px;
min-height:20px;
}
.clock-popup.button.day:checked{
background-color:rgba(0,110,255,0.5);
}
.clock-popup.button.quick-option{
background-color:rgba(255,255,255,0.1);
}
.clock-popup.button.quick-option:checked{
background-color:rgba(0,110,255,0.5);
}
.clock-popup.button:hover{
background-color:rgba(255,255,255,0.2);
}
.clock-popup.button:disabled{
background-color:rgba(100,100,100,0.2);
color:rgba(150,150,150,0.7);
}
.clock-popup.alarm-input-title{
font-size:14px;
font-family:'Segoe UI';
font-weight:600;
color:#d2d6e2;
background-color:rgba(255,255,255,0.1);
border:1pxsolidtransparent;
border-radius:4px;
padding:4px8px;
margin-top:8px;
outline:none;
min-width:300px;
}

.clock-popup.alarm-input-title:focus{
border:1pxsolid#0078D4;
}

/* Active Alarm Popup Window */
.active-alarm-window{
background-color:rgba(255,255,255,0.048);
max-width:500px;
min-width:500px;
padding:32px;
}
.active-alarm-window.alarm-title-icon{
font-size:64px;
color:#ffffff;
margin-bottom:16px;
}
.active-alarm-window.alarm-title{
font-size:24px;
font-family:'Segoe UI';
font-weight:600;
color:#ffffff;
max-width:500px;
min-width:500px;
}
.active-alarm-window.alarm-info{
font-size:16px;
font-family:'Segoe UI';
font-weight:600;
color:#b2b6c0;
margin-bottom:32px;
}
.active-alarm-window.button{
border-radius:4px;
font-family:'Segoe UI';
font-weight:600;
font-size:14px;
min-height:36px;
min-width:100px;
margin:04px;
background-color:rgba(255,255,255,0.1);
}
.active-alarm-window.button:hover{
background-color:rgba(255,255,255,0.3);
}
```