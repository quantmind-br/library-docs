---
title: Configuration | Dank Linux
url: https://danklinux.com/docs/dankgreeter/configuration
source: sitemap
fetched_at: 2026-01-24T13:35:08.824061574-03:00
rendered_js: false
word_count: 138
summary: This document explains how to configure and synchronize the DMS system greeter with user themes, wallpapers, and settings using command-line tools and JSON configuration files.
tags:
    - dms-greeter
    - theme-syncing
    - configuration-management
    - desktop-customization
    - wallpaper-settings
    - system-greeter
category: configuration
---

tip

Custom compositor configurations allow you to configure displays (resolution, refresh rate, position, etc.) specifically for the greeter.

You can automatically sync the system greeter with the logged in user's wallpaper, themes, fonts, etc.

You can use `dms greeter sync` to automatically set up theme syncing. This command is available for:

note

After running `dms greeter sync`, you will need to log out and log back in for group membership changes to take effect. After logging back in, your greeter will automatically reflect your current DMS theme, wallpaper, and settings.

To verify that your greeter is properly configured and syncing with your user settings, run:

```
=== DMS Greeter Status ===

Group Membership:
  ✓ User is in greeter group

Greeter Cache Directory:
  ✓ /var/cache/dms-greeter exists

Configuration Symlinks:
  ✓ Settings: synced correctly
  ✓ Session state: synced correctly
  ✓ Color theme: synced correctly

✓ All checks passed! Greeter is properly configured.
```

The greeter uses three main configuration files located in `/var/cache/dms-greeter/` (or your custom `DMS_GREET_CFG_DIR`):

The `settings.json` file controls the greeter's appearance and behavior. Here's a complete reference:

```
{
"use24HourClock":true,
"showSeconds":false,
"lockDateFormat":""
}
```

```
{
"weatherEnabled":true,
"weatherLocation":"New York, NY",
"weatherCoordinates":"40.7128,-74.0060",
"useAutoLocation":false,
"useFahrenheit":false
}
```

```
{
"currentThemeName":"blue",
"customThemeFile":"",
"matugenScheme":"scheme-tonal-spot",
"iconTheme":"System Default",
"fontFamily":"Inter Variable",
"fontWeight":400,
"fontScale":1.0,
"cornerRadius":12,
"widgetBackgroundColor":"sch",
"surfaceBase":"s",
"animationSpeed":2
}
```

```
{
"use24HourClock":true,
"showSeconds":false,
"lockDateFormat":"",
"lockScreenShowPowerActions":true,
"useFahrenheit":false,
"weatherLocation":"New York, NY",
"weatherCoordinates":"40.7128,-74.0060",
"useAutoLocation":false,
"weatherEnabled":true,
"currentThemeName":"blue",
"customThemeFile":"",
"matugenScheme":"scheme-tonal-spot",
"nightModeEnabled":false,
"iconTheme":"System Default",
"fontFamily":"Inter Variable",
"fontWeight":400,
"fontScale":1.0,
"cornerRadius":12,
"widgetBackgroundColor":"sch",
"surfaceBase":"s",
"animationSpeed":2
}
```

The `session.json` file controls wallpaper settings.

```
{
"wallpaperPath":"/path/to/default.jpg",
"wallpaperFillMode":"PreserveAspectCrop",
"monitorWallpapers":{
"DP-1":"/path/to/monitor1-wallpaper.jpg",
"DP-2":"/path/to/monitor2-wallpaper.jpg",
"HDMI-A-1":"#1a1a1a"
}
}
```

```
{
"wallpaperPath":"/usr/share/backgrounds/default.jpg",
"wallpaperFillMode":"PreserveAspectCrop",
"monitorWallpapers":{
"DP-1":"/home/user/Pictures/wallpaper-main.png",
"DP-2":"#2e3440",
"HDMI-A-1":"/home/user/Pictures/wallpaper-side.jpg"
}
}
```