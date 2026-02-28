---
title: YASB Reborn - Yet Another Status Bar
url: https://docs.yasb.dev/latest/widgets/weather
source: crawler
fetched_at: 2026-02-23T05:28:47.354821-03:00
rendered_js: false
word_count: 0
---

```
weather:
type:"yasb.weather.WeatherWidget"
options:
label:"<span>{icon}</span>{temp}"
label_alt:"{location}:Min{min_temp},Max{max_temp},Humidity{humidity}"
api_key:"3bf4cf9a7c3f40d6b31174128242807"# Get your free API key from https://www.weatherapi.com/
show_alerts:true
tooltip:true
update_interval:600# Update interval in seconds, Min 600 seconds
hide_decimal:true
units:"metric"# Can be 'metric' or 'imperial'
location:"LosAngeles,CA,USA"# You can use "USA Los Angeles 90006" {COUNTRY CITY ZIP_CODE}, or just city.
callbacks:
on_left:"toggle_card"
on_middle:"do_nothing"
on_right:"toggle_label"
```

```
weather:
type:"yasb.weather.WeatherWidget"
options:
label:"<span>{icon}</span>{temp}"
label_alt:"{location}:Min{min_temp},Max{max_temp},Humidity{humidity}"
api_key:"3bf4cf9a7c3f40d6b31174128242807"# Get your free API key from https://www.weatherapi.com/
show_alerts:true
tooltip:true
update_interval:600# Update interval in seconds, Min 600 seconds
hide_decimal:true
units:"metric"# Can be 'metric' or 'imperial'
location:"LosAngeles,CA,USA"# You can use "USA Los Angeles 90006" {COUNTRY CITY ZIP_CODE}, or just city.
callbacks:
on_left:"toggle_card"
on_middle:"do_nothing"
on_right:"toggle_label"
icons:
sunnyDay:"\ue30d"
clearNight:"\ue32b"
cloudyDay:"\ue312"
cloudyNight:"\ue311"
rainyDay:"\ue308"
rainyNight:"\ue333"
snowyDay:"\ue30a"
snowyNight:"\ue335"
blizzardDay:"\udb83\udf36"
blizzardNight:"\udb83\udf36"
foggyDay:"\ue303"
foggyNight:"\ue346"
thunderstormDay:"\ue30f"
thunderstormNight:"\ue338"
default:"\uebaa"
weather_card:
blur:true
round_corners:true
round_corners_type:"normal"
border_color:"system"
alignment:"right"
direction:"down"
icon_size:64
show_hourly_forecast:true# Set to False to disable hourly forecast
time_format:"24h"# can be 12h or 24h
hourly_point_spacing:76
hourly_icon_size:32# better to set 16, 32 or 64 for better quality
icon_smoothing:true# should be true for smoother icon or false for sharper icon if using 16, 32 or 64 for hourly_icon_size
temp_line_width:2# can be 0 to hide the temperature line
current_line_color:"#8EAEE8"
current_line_width:1# can be 0 to hide the current hour line
current_line_style:"dot"
hourly_gradient:
enabled:false
top_color:"#8EAEE8"
bottom_color:"#2A3E68"
hourly_forecast_buttons:# Optional hourly forecast data type toggle buttons, default disabled
enabled:true# Set to false to hide the buttons
default_view:"temperature"# Default view when opening the weather card. Options: "temperature", "rain", "snow"
temperature_icon:"\udb81\udd99"
rain_icon:"\udb81\udd96"
snow_icon:"\udb81\udd98"
weather_animation:
enabled:false
snow_overrides_rain:true
temp_line_animation_style:both# can be "rain", "snow", "both", or "none"
rain_effect_intensity:1.0# 0.01 - 10.0
snow_effect_intensity:1.0# 0.01 - 10.0
scale_with_chance:true
enable_debug:false
label_shadow:
enabled:true
color:"black"
radius:3
offset:[1,1]
```

```
.weather-widget{}
.weather-widget.your_class{}/* If you are using class_name option */
.weather-widget.widget-container{}
.weather-widget.label{}
.weather-widget.label.alt{}
.weather-widget.icon{}

/* Individual weather icons */
.weather-widget.icon.sunnyDay{}
.weather-widget.icon.clearNight{}
.weather-widget.icon.cloudyDay{}
.weather-widget.icon.cloudyNight{}
.weather-widget.icon.rainyDay{}
.weather-widget.icon.rainyNight{}
.weather-widget.icon.snowyDay{}
.weather-widget.icon.snowyNight{}
.weather-widget.icon.blizzardDay{}
.weather-widget.icon.blizzardNight{}
.weather-widget.icon.foggyDay{}
.weather-widget.icon.foggyNight{}
.weather-widget.icon.thunderstormDay{}
.weather-widget.icon.thunderstormNight{}
.weather-widget.icon.default{}

/* Weather card style */
.weather-card{
background-color:rgba(17,17,27,0.5);
}
.weather-card-today{
border:1pxsolid#282936;
border-radius:8px;
background-color:rgba(17,17,27,0.2);
}
.weather-card-today.label{
font-size:12px;
}
.weather-card-today.label.location{
font-size:24px;
font-weight:700;
}
.weather-card-today.label.alert{
font-size:12px;
font-weight:700;
background-color:rgba(247,199,42,0.05);
border:1pxsolidrgba(247,209,42,0.1);
color:rgba(196,181,162,0.85);
border-radius:6px;
padding:5px0;
}
.weather-card-day{
border:1pxsolid#45475a;
border-radius:8px;
background-color:rgba(17,17,27,0.2);
}

.weather-card-day.active{
background-color:rgba(40,40,60,0.6);
border:1pxsolidrgba(50,50,75,1);
}

.weather-card-day:hover{
background-color:rgba(40,40,60,0.6);
}

.weather-card-day.label{
font-size:12px;
}

.weather-card.hourly-container{
border:1pxsolid#282936;
background-color:#3c5fa0;
border-radius:8px;
min-height:150px;
}

.weather-card.hourly-data{
/* font-family: 'Segoe UI';*/
/* color: cyan;*//* <- Font color */
font-size:12px;
font-weight:bold;
}

.weather-card.hourly-data.temperature{
background-color:#FAE93F;/* Temperature curve & line color */
}

.weather-card.hourly-data.rain{
background-color:#4A90E2;/* Rain curve & line color */
}

.weather-card.hourly-data.snow{
background-color:#A0C4FF;/* Snow curve & line color */
}

.weather-card.hourly-data.hourly-rain-animation{
color:rgba(150,200,255,40);/* Rain color */
background-color:rgba(0,0,0,0.1);/* Rain background color */
}

.weather-card.hourly-data.hourly-snow-animation{
color:rgba(255,255,255,150);/* Snow color */
background-color:rgba(0,0,0,0.1);/* Snow background color */
}

/* Hourly forecast toggle buttons */
.weather-card.hourly-data-buttons{
margin:0px;
}
.weather-card.hourly-data-button{
border-radius:4px;
min-height:24px;
min-width:24px;
max-width:24px;
max-height:24px;
font-size:14px;
color:rgba(255,255,255,0.3);
border:1pxsolidtransparent;
}
.weather-card.hourly-data-button.active{
color:#fff;
background-color:rgba(255,255,255,0.1);
border:1pxsolidrgba(255,255,255,0.1);
}
```