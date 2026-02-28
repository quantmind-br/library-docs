---
title: YASB Reborn - Yet Another Status Bar
url: https://docs.yasb.dev/latest/widgets/libre-hw-monitor
source: crawler
fetched_at: 2026-02-23T05:28:38.795279-03:00
rendered_js: false
word_count: 22
---

```
libre_gpu:
type:"yasb.libre_monitor.LibreHardwareMonitorWidget"
options:
label:"<span>\udb82\udcae</span>{info[value]}{info[unit]}"
label_alt:"<span>\uf437</span>{info[histogram]}{info[value]}({info[min]}/{info[max]}){info[unit]}"
sensor_id:"/gpu-nvidia/0/temperature/0"
update_interval:1000
precision:2
histogram_num_columns:10
class_name:"libre-monitor-widget"

history_size:60
histogram_icons:

-"\u2581"# 0%
-"\u2581"# 10%
-"\u2582"# 20%
-"\u2583"# 30%
-"\u2584"# 40%
-"\u2585"# 50%
-"\u2586"# 60%
-"\u2587"# 70%
-"\u2588"# 80%+

# histogram_fixed_min: 0.0
# histogram_fixed_max: 100.0

# server_host: "localhost"
# server_port: 8085
# server_username: "admin"
# server_password: "password"

callbacks:
on_left:"toggle_label"
on_middle:"do_nothing"
on_right:"toggle_menu"
label_shadow:
enabled:true
color:"black"
radius:3
offset:[1,1]
libre_menu:
blur:true
round_corners:true
round_corners_type:"normal"
border_color:"System"
alignment:"right"
direction:"down"
offset_top:6
offset_left:0
header_label:"YASBHardwareMonitor"
precision:1
columns:1
sensors:

-id:"/intelcpu/0/temperature/8"
name:"CPUTemp"

-id:"/intelcpu/0/load/0"
name:"CPULoad"

-id:"/intelcpu/0/power/0"
name:"CPUPackagePower"

-id:"/intelcpu/0/power/1"
name:"CPUCorePower"

-id:"/gpu-nvidia/0/temperature/0"
name:"NvidiaTemp"

-id:"/lpc/it8689e/0/fan/0"
name:"CPUFan"

-id:"/lpc/it8689e/0/fan/1"
name:"SystemFan"
```

**Note**: Libre Hardware Monitor and its web server must be running in the background for the widget to work. Autostart is recommended.

```
.libre-monitor-widget{}
.libre-monitor-widget.widget-container{}
.libre-monitor-widget.widget-container.label{}
.libre-monitor-widget.widget-container.label.alt{}
.libre-monitor-widget.widget-container.icon{}

.libre-menu{}
.libre-menu.header{}
.libre-menu.sensor-item{}
.libre-menu.sensor-name{}
.libre-menu.sensor-value{}
```

```
.libre-menu{
background-color:rgba(17,17,27,0.9);
}
.libre-menu.header{
font-size:18px;
font-weight:600;
color:#cdd6f4;
font-family:"Segoe UI";
padding:20px010px0;
margin:040px;
}
.libre-menu.sensor-item{
background-color:rgba(255,255,255,0.01);
padding:0px8px;
border-radius:6px;
border:1pxsolidrgba(255,255,255,0.05);
}
.libre-menu.sensor-item:hover{
background-color:rgba(255,255,255,0.05);
}
.libre-menu.sensor-name{
font-size:12px;
font-weight:600;
font-family:"Segoe UI";
color:rgba(255,255,255,0.5);
}
.libre-menu.sensor-value{
font-size:12px;
font-family:"Segoe UI";
font-weight:600;
color:rgb(255,255,255);
min-width:60px;
}
```