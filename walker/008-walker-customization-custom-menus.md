---
title: Custom Menus | Walker
url: https://benz.gitbook.io/walker/customization/custom-menus
source: sitemap
fetched_at: 2026-02-01T13:48:31.528275747-03:00
rendered_js: false
word_count: 102
summary: This document explains how to configure custom menus using the Elephant menu provider, including syntax for entries, actions, and Lua script integration.
tags:
    - menu-provider
    - custom-menus
    - elephant
    - lua-scripts
    - configuration
    - walker
category: guide
---

Walker is just a frontend that interacts with a backend, Elephant: [https://github.com/abenz1267/elephantarrow-up-right](https://github.com/abenz1267/elephant) Elephant allows you to create custom menus via its `menu` provider. Running `elephant generatedoc` will generate markdown output of every installed provider and it's configuration options. It also includes examples for custom menus. You can find more examples [herearrow-up-right](https://github.com/abenz1267/elephant-community).

```
name = "other"
name_pretty = "Other"
icon = "applications-other"
[[entries]]
text = "Color Picker"
keywords = ["color", "picker", "hypr"]
actions = { "cp_use" = "sleep 0.5 && wl-copy $(hyprpicker)" }
icon = "color-picker"
[[entries]]
icon = "zoom-in"
text = "Zoom Toggle"
actions = { "zoom_use" = "hyprctl -q keyword cursor:zoom_factor $(hyprctl getoption cursor:zoom_factor -j | jq '(.float) | if . > 1 then 1 else 1.5 end')" }
[[entries]]
text = "Volume"
async = "echo $(wpctl get-volume @DEFAULT_AUDIO_SINK@)"
icon = "audio-volume-high"
[entries.actions]
"volume_raise" = "wpctl set-volume @DEFAULT_AUDIO_SINK@ 0.1+"
"volume_lower" = "wpctl set-volume @DEFAULT_AUDIO_SINK@ 0.1-"
"volume_mute" = "wpctl set-volume @DEFAULT_AUDIO_SINK@ 0"
"volume_unmute" = "wpctl set-volume @DEFAULT_AUDIO_SINK@ 1"
"volume_set" = "wpctl set-volume @DEFAULT_AUDIO_SINK@ %VALUE%"
[[entries]]
keywords = ["disk", "drive", "space"]
text = "Disk"
actions = { "disk_copy" = "wl-copy '%VALUE%'" }
async = """echo $(df -h / | tail -1 | awk '{print "Used: " $3 " - Available: " $4 " - Total: " $2}')"""
icon = "drive-harddisk"
[[entries]]
text = "Mic"
async = "echo $(wpctl get-volume @DEFAULT_AUDIO_SOURCE@"
icon = "audio-input-microphone"
actions = { "mic_set" = "wpctl set-volume @DEFAULT_AUDIO_SOURCE@ %VALUE%" }
[[entries]]
text = "System"
async = """echo $(echo "Memory: $(free -h | awk '/^Mem:/ {printf "%s/%s", $3, $2}') | CPU: $(top -bn1 | grep 'Cpu(s)' | awk '{printf "%.1f%%", 100 - $8}')")"""
icon = "computer"
[[entries]]
text = "Today"
keywords = ["date", "today", "calendar"]
async = """echo $(date "+%H:%M - %d.%m. %A - KW %V")"""
icon = "clock"
actions = { "open_cal" = "xdg-open https://calendar.google.com" }
[[entries]]
text = "uuctl"
keywords = ["uuctl"]
icon = "applications-system"
submenu = "dmenu:uuctl"
```

... and here is a more simple one!

```
name = "bookmarks"
name_pretty = "Bookmarks"
icon = "bookmark"
action = "xdg-open %VALUE%"
[[entries]]
text = "Walker"
value = "https://github.com/abenz1267/walker"
[[entries]]
text = "Elephant"
value = "https://github.com/abenz1267/elephant"
```

By default, the Lua script will be called on every empty query. If you don't want this behaviour, but instead want to cache the query once, you can set `Cache=true` in the menu's config.

```
Name ="luatest"
NamePretty ="Lua Test"
Icon ="applications-other"
Cache =true
Action ="notify-send %VALUE%"
HideFromProviderlist =false
Description ="lua test menu"
SearchName =true
functionGetEntries()
local entries = {}
local wallpaper_dir ="/home/andrej/Documents/ArchInstall/wallpapers"
local handle =io.popen("find '" ..
        wallpaper_dir ..
"' -maxdepth 1 -type f -name '*.jpg' -o -name '*.jpeg' -o -name '*.png' -o -name '*.gif' -o -name '*.bmp' -o -name '*.webp' 2>/dev/null")
if handle then
for line inhandle:lines() do
local filename =line:match("([^/]+)$")
if filename then
table.insert(entries, {
                    Text = filename,
                    Subtext ="wallpaper",
                    Value = line,
                    Actions = {
                        up ="notify-send up",
                        down ="notify-send down",
                    },
                    -- Preview = line,
                    -- PreviewType = "file",
                    -- Icon = line
                })
end
end
handle:close()
end
return entries
end
```

You can call Lua functions as actions as well:

```
Actions = {
    test ="lua:Test",
}
functionTest(value,args)
os.execute("notify-send '" .. value .."'")
os.execute("notify-send '" .. args .."'")
end
```