---
title: Keybinds & IPC | Dank Linux
url: https://danklinux.com/docs/dankmaterialshell/keybinds-ipc
source: sitemap
fetched_at: 2026-01-24T13:35:45.063487405-03:00
rendered_js: false
word_count: 1490
summary: This document provides a technical reference for the DankMaterialShell Inter-Process Communication (IPC) interface, detailing command-line functions for controlling system settings, media, and UI components.
tags:
    - dms
    - ipc-reference
    - shell-automation
    - command-line-interface
    - desktop-environment
    - system-control
category: reference
---

```
██████╗ ███╗   ███╗███████╗
██╔══██╗████╗ ████║██╔════╝
██║  ██║██╔████╔██║███████╗
██║  ██║██║╚██╔╝██║╚════██║
██████╔╝██║ ╚═╝ ██║███████║
╚═════╝ ╚═╝     ╚═╝╚══════╝
```

DankMaterialShell provides comprehensive IPC (Inter-Process Communication) functionality that allows external control of the shell through command-line commands. All IPC commands follow the format:

```
dms ipc call <target><function>[parameters...]
```

## Core Controls[​](#core-controls "Direct link to Core Controls")

### audio[​](#audio "Direct link to audio")

Manage audio output and input devices.

FunctionDescriptionParameters`setvolume <percentage>`Set output volumepercentage (0-100)`increment <step>`Increase output volumestep (default: 5)`decrement <step>`Decrease output volumestep (default: 5)`mute`Toggle output mute-`setmic <percentage>`Set microphone volumepercentage (0-100)`micmute`Toggle microphone mute-`cycleoutput`Cycle through audio output devices-`status`Get current audio status-

**Examples:**

```
dms ipc call audio setvolume 50
dms ipc call audio increment 10
dms ipc call audio mute
dms ipc call audio cycleoutput
```

### brightness[​](#brightness "Direct link to brightness")

Control display brightness for internal and external displays.

FunctionDescriptionParameters`set <percentage> [device]`Set brightness levelpercentage (1-100), device (optional)`increment <step> [device]`Increase brightnessstep, device (optional)`decrement <step> [device]`Decrease brightnessstep, device (optional)`status`Get current brightness status-`list`List all brightness devices-`enableExponential [device]`Enable exponential brightness modedevice (optional, uses current if not specified)`disableExponential [device]`Disable exponential brightness modedevice (optional, uses current if not specified)`toggleExponential [device]`Toggle exponential brightness modedevice (optional, uses current if not specified)

**Examples:**

```
dms ipc call brightness set80
dms ipc call brightness increment 10""
dms ipc call brightness decrement 5"intel_backlight"
dms ipc call brightness disableExponential "backlight:intel_backlight"
dms ipc call brightness toggleExponential
```

### night[​](#night "Direct link to night")

Night mode (gamma/color temperature) control.

FunctionDescriptionParameters`toggle`Toggle night mode on/off-`enable`Enable night mode-`disable`Disable night mode-`status`Get night mode status-`temperature [value]`Get/set color temperaturevalue in Kelvin (2500-6000, optional)`automation [mode]`Get/set automation mode"manual", "time", or "location" (optional)`schedule <start> <end>`Set time-based schedulestart time (HH:MM), end time (HH:MM)`location <lat> <lon>`Set location coordinateslatitude, longitude

**Examples:**

```
dms ipc call night toggle
dms ipc call night temperature 4000
dms ipc call night automation time
dms ipc call night schedule 20:00 06:00
dms ipc call night location 40.7128-74.0060
```

### mpris[​](#mpris "Direct link to mpris")

Media player control via MPRIS interface.

FunctionDescription`list`List all available media players`play`Start playback`pause`Pause playback`playPause`Toggle play/pause`previous`Skip to previous track`next`Skip to next track`stop`Stop playback

**Examples:**

```
dms ipc call mpris playPause
dms ipc call mpris next
```

### lock[​](#lock "Direct link to lock")

Screen lock control and status.

FunctionDescription`lock`Lock the screen immediately`demo`Show lock screen demo (doesn't lock)`isLocked`Check if screen is locked

**Examples:**

```
dms ipc call lock lock
dms ipc call lock isLocked
```

### inhibit[​](#inhibit "Direct link to inhibit")

Idle inhibitor control to prevent automatic sleep/lock.

FunctionDescription`toggle`Toggle idle inhibit state`enable`Enable idle inhibit (prevent sleep)`disable`Disable idle inhibit (allow sleep)

**Examples:**

```
dms ipc call inhibit toggle
dms ipc call inhibit enable
```

## Wallpaper & Profile[​](#wallpaper--profile "Direct link to Wallpaper & Profile")

### wallpaper[​](#wallpaper "Direct link to wallpaper")

Wallpaper management with support for global and per-monitor configurations.

#### Global Wallpaper Functions[​](#global-wallpaper-functions "Direct link to Global Wallpaper Functions")

FunctionDescriptionParameters`get`Get current wallpaper path-`set <path>`Set wallpaperpath to image file`clear`Clear all wallpapers-`next`Cycle to next wallpaper-`prev`Cycle to previous wallpaper-

#### Per-Monitor Functions[​](#per-monitor-functions "Direct link to Per-Monitor Functions")

FunctionDescriptionParameters`getFor <screen>`Get wallpaper for monitormonitor name (e.g., "DP-2")`setFor <screen> <path>`Set wallpaper for monitormonitor name, path to image`nextFor <screen>`Cycle to next wallpapermonitor name`prevFor <screen>`Cycle to previous wallpapermonitor name

**Examples:**

```
# Global wallpaper mode
dms ipc call wallpaper set /path/to/image.jpg
dms ipc call wallpaper next

# Per-monitor wallpaper mode
dms ipc call wallpaper setFor DP-2 /path/to/image1.jpg
dms ipc call wallpaper setFor eDP-1 /path/to/image2.jpg
dms ipc call wallpaper nextFor eDP-1

# Clear and return to global mode
dms ipc call wallpaper clear
```

**Note:** When per-monitor mode is enabled, legacy global functions will return error messages directing you to use the per-monitor equivalents.

### profile[​](#profile "Direct link to profile")

User profile image management.

FunctionDescriptionParameters`getImage`Get current profile image path-`setImage <path>`Set profile imagepath to image file`clearImage`Clear profile image-

**Examples:**

```
dms ipc call profile setImage /path/to/avatar.png
dms ipc call profile clearImage
```

## Appearance Controls[​](#appearance-controls "Direct link to Appearance Controls")

### theme[​](#theme "Direct link to theme")

Theme mode control (light/dark mode switching).

FunctionDescription`toggle`Toggle between light and dark themes`light`Switch to light theme`dark`Switch to dark theme`getMode`Get current theme mode

**Examples:**

```
dms ipc call theme toggle
dms ipc call theme dark
```

### bar[​](#bar "Direct link to bar")

Control individual bars using flexible selectors.

FunctionDescriptionParameters`reveal <selector> <value>`Show a barselector + value`hide <selector> <value>`Hide a barselector + value`toggle <selector> <value>`Toggle bar visibilityselector + value`status <selector> <value>`Get bar visibility statusselector + value`autoHide <selector> <value>`Enable auto-hide modeselector + value`manualHide <selector> <value>`Disable auto-hide modeselector + value`toggleAutoHide <selector> <value>`Toggle auto-hide modeselector + value`getPosition <selector> <value>`Get bar positionselector + value`setPosition <selector> <value> <position>`Set bar positionselector + value + position (top, bottom, left, right)

**Selectors:**

- `index` - Select by position (0-based)
- `id` - Select by unique bar ID
- `name` - Select by bar name

**Examples:**

```
# By index
dms ipc call bar hide index 0
dms ipc call bar reveal index 1
dms ipc call bar toggle index 0

# By name
dms ipc call bar toggle name "Main Bar"
dms ipc call bar status name "Secondary"

# By ID
dms ipc call bar reveal id abc123

# Auto-hide controls
dms ipc call bar autoHide index 0
dms ipc call bar manualHide name "Main Bar"
dms ipc call bar toggleAutoHide index 1

# Position controls
dms ipc call bar getPosition index 0
dms ipc call bar getPosition id default
dms ipc call bar setPosition index 0top
dms ipc call bar setPosition id default left
```

### dock[​](#dock "Direct link to dock")

Dock visibility and behavior control.

FunctionDescription`reveal`Show the dock`hide`Hide the dock`toggle`Toggle dock visibility`status`Get dock visibility status`autoHide`Enable auto-hide mode`manualHide`Disable auto-hide mode`toggleAutoHide`Toggle auto-hide mode

**Examples:**

```
dms ipc call dock toggle
dms ipc call dock hide
dms ipc call dock reveal
dms ipc call dock status

# Auto-hide controls
dms ipc call dock autoHide
dms ipc call dock manualHide
dms ipc call dock toggleAutoHide
```

### widget[​](#widget "Direct link to widget")

Control bar widget popouts, menus, and visibility (including plugins).

FunctionDescriptionParameters`toggle <widgetId>`Toggle widget popout visibilitywidget ID`list`List all registered widget IDs with visibility state-`status <widgetId>`Get widget popout visibility statuswidget ID`visibility <widgetId>`Get widget visibility statewidget ID`reveal <widgetId>`Force widget to be visiblewidget ID`hide <widgetId>`Force widget to be hiddenwidget ID`reset <widgetId>`Clear visibility override, return to normal behaviorwidget ID

**Examples:**

```
dms ipc call widget list
dms ipc call widget toggle clock
dms ipc call widget status weather

# Control widget visibility on the bar
dms ipc call widget visibility weather
dms ipc call widget hide weather
dms ipc call widget reveal weather
dms ipc call widget reset weather
```

**Notes:**

- Use `list` to discover available widget IDs with their current visibility state (`[visible]` or `[hidden]`)
- Widget IDs depend on which widgets are enabled in your bar settings
- The `status` function returns "visible" or "hidden" for the widget **popout** state
- The `visibility`, `reveal`, `hide`, and `reset` functions control the widget's **bar presence** (whether it appears on the bar at all)
- Plugins can define conditional visibility via `visibilityCommand` — use `reset` to return to that behavior after overriding

## Modal Controls[​](#modal-controls "Direct link to Modal Controls")

These targets control various modal windows and overlays.

### spotlight[​](#spotlight "Direct link to spotlight")

Application launcher modal with search capabilities.

FunctionDescriptionParameters`open`Show launcher-`close`Hide launcher-`toggle`Toggle launcher visibility-`openQuery <query>`Show launcher with searchsearch text`toggleQuery <query>`Toggle launcher with searchsearch text

**Examples:**

```
dms ipc call spotlight toggle
dms ipc call spotlight openQuery browser
dms ipc call spotlight toggleQuery "!"
```

### Other Modals[​](#other-modals "Direct link to Other Modals")

All these modals support `open`, `close`, and `toggle` functions:

- **clipboard** - Clipboard history manager
- **notifications** - Notification center (also supports `clearAll`, `dismissAllPopups`, `toggleDoNotDisturb`, and `getDoNotDisturb`)
- **processlist** - System process list and performance monitor (also supports `focusOrToggle`)
- **powermenu** - Power menu for system actions
- **control-center** - Quick settings (network, bluetooth, audio, etc.)
- **notepad** - Quick notepad/scratchpad

**Examples:**

```
dms ipc call clipboard toggle
dms ipc call notifications open
dms ipc call notifications clearAll
dms ipc call notifications dismissAllPopups
dms ipc call notifications toggleDoNotDisturb
dms ipc call notifications getDoNotDisturb
dms ipc call processlist open
dms ipc call powermenu toggle
dms ipc call control-center toggle
dms ipc call notepad open
```

### settings[​](#settings "Direct link to settings")

Settings modal with additional read/write access to configuration values.

FunctionDescriptionParameters`open`Show settings modal-`openWith <tab>`Open settings to specific tabtab ID`close`Hide settings modal-`toggle`Toggle settings modal-`toggleWith <tab>`Toggle settings to specific tabtab ID`focusOrToggle`Focus settings if open, otherwise toggle-`focusOrToggleWith <tab>`Focus/toggle to specific tabtab ID`tabs`List available tab IDs-`get <key>`Get a setting valuesetting key name`set <key> <value>`Set a setting valuesetting key, new value

**Available Tab IDs:**

- **Personalization:** `personalization`, `wallpaper`, `theme`, `typography`, `time_weather`, `sounds`
- **Dankbar:** `dankbar`, `dankbar_settings`, `dankbar_widgets`
- **Widgets:** `workspaces_widgets`, `workspaces`, `media_player`, `notifications`, `osd`, `running_apps`, `updater`
- **Dock & Launcher:** `dock_launcher`, `dock`, `launcher`
- **System:** `keybinds`, `displays`, `network`, `printers`
- **Power & Security:** `power_security`, `lock_screen`, `power_sleep`
- **Other:** `plugins`, `about`

**Examples:**

```
dms ipc call settings toggle
dms ipc call settings openWith theme
dms ipc call settings toggleWith dock
dms ipc call settings tabs
dms ipc call settings set showSeconds true
dms ipc call settings set opacity 0.9
```

**Note:** The `set` function supports boolean, number, and string values. Objects and arrays are not currently supported.

### dash[​](#dash "Direct link to dash")

Dashboard popup with multiple tabs.

FunctionDescriptionParameters`open [tab]`Show dashboardtab: "", "overview", "media", "weather"`close`Hide dashboard-`toggle [tab]`Toggle dashboardtab

**Examples:**

```
dms ipc call dash toggle ""
dms ipc call dash open overview
dms ipc call dash toggle media
dms ipc call dash open weather
```

### file[​](#file "Direct link to file")

File browser controls for selecting wallpapers and profile images.

FunctionDescriptionParameters`browse <type>`Open file browser"wallpaper" or "profile"

**Examples:**

```
dms ipc call file browse wallpaper
dms ipc call file browse profile
```

### dankdash[​](#dankdash "Direct link to dankdash")

DankDash wallpaper browser control.

FunctionDescription`wallpaper`Toggle DankDash wallpaper browser

**Examples:**

```
dms ipc call dankdash wallpaper
```

### welcome[​](#welcome "Direct link to welcome")

First-launch welcome wizard with feature overview, system diagnostics, and configuration quick links.

FunctionDescriptionParameters`open`Show wizard at Welcome page-`doctor`Show wizard at System Check page-`page <num>`Show wizard at specific page0=Welcome, 1=Doctor, 2=Complete

**Pages:**

- **0 - Welcome**: Feature overview with DMS highlights
- **1 - System Check**: Runs `dms doctor` with filterable results (Errors, Warnings, Info, OK)
- **2 - Complete**: Configuration quick links, keybind shortcuts, and external resources

**Examples:**

```
dms ipc call welcome open
dms ipc call welcome doctor
dms ipc call welcome page 2
```

**Settings Integration:** Available in Settings → About → Tools as "Show Welcome" and "System Check" buttons.

## System Utilities[​](#system-utilities "Direct link to System Utilities")

### niri[​](#niri "Direct link to niri")

**Requires niri 25.11+**

Screenshot functionality for the niri compositor. Captures are opened in your configured editor for markup and annotation.

FunctionDescription`screenshot`Interactive selection screenshot`screenshotScreen`Capture entire screen`screenshotWindow`Capture focused window

**Examples:**

```
dms ipc call niri screenshot
dms ipc call niri screenshotScreen
dms ipc call niri screenshotWindow
```

**Configuration:**

Set the `DMS_SCREENSHOT_EDITOR` environment variable to choose your preferred screenshot editor backend:

```
# Use Swappy (default)
exportDMS_SCREENSHOT_EDITOR=swappy

# Use Satty
exportDMS_SCREENSHOT_EDITOR=satty
```

**Requirements:** niri compositor and your chosen screenshot editor (Swappy or Satty) must be installed.

### keybinds[​](#keybinds "Direct link to keybinds")

Dynamic keybinds cheatsheet modal that works with multiple providers.

FunctionDescriptionParameters`open <provider>`Show keybinds modalprovider name (e.g., "hyprland", "sway", "mangowc")`openWithPath <provider> <path>`Show keybinds modal with custom config pathprovider name, path to config`close`Hide keybinds modal-`toggle <provider>`Toggle keybinds modal visibilityprovider name`toggleWithPath <provider> <path>`Toggle keybinds modal with custom config pathprovider name, path to config

**Examples:**

```
dms ipc call keybinds toggle hyprland
dms ipc call keybinds toggle sway
dms ipc call keybinds toggle mangowc
dms ipc call keybinds open tmux

# With custom config paths
dms ipc call keybinds openWithPath hyprland /custom/path/to/hypr
dms ipc call keybinds toggleWithPath sway /etc/sway/config
```

**Supported Providers:**

The keybinds modal supports all providers available through the `dms keybinds` CLI:

- **Built-in providers**: Hyprland, Sway, MangoWC (automatically parse compositor configs)
- **Custom cheatsheets**: Any JSON-based cheatsheet in `~/.config/DankMaterialShell/cheatsheets/`

The modal automatically parses configuration files and displays keybinds organized by category with optional subcategories. See the [Keybinds & Cheatsheets](https://danklinux.com/docs/dankmaterialshell/cli-keybinds-cheatsheets) documentation for more details on providers and creating custom cheatsheets.

### hypr[​](#hypr "Direct link to hypr")

**Hyprland-only features**

Hyprland-specific workspace overview control.

FunctionDescription`openOverview`Show Hyprland workspace overview`closeOverview`Hide Hyprland workspace overview`toggleOverview`Toggle Hyprland workspace overview visibility

**Examples:**

```
dms ipc call hypr toggleOverview
```

**Workspace Overview:**

The workspace overview shows all your workspaces across all monitors with live window previews:

- **Multi-monitor support** - Shows workspaces from all connected monitors with monitor name labels
- **Live window previews** - Real-time screen capture of all windows on each workspace
- **Drag-and-drop** - Move windows between workspaces and monitors by dragging
- **Keyboard navigation** - Use Left/Right arrow keys to switch between workspaces on current monitor
- **Visual indicators** - Active workspace highlighted when it contains windows
- **Click to switch** - Click any workspace to switch to it
- **Click outside or press Escape** - Close the overview

**Note:** All hypr functions return `HYPR_NOT_AVAILABLE` if not running Hyprland.

### plugins[​](#plugins "Direct link to plugins")

Manage plugins at runtime - useful for development and troubleshooting.

FunctionDescriptionParameters`list`List all available plugins with status-`status <pluginId>`Check if a plugin is loadedplugin ID`reload <pluginId>`Hot-reload a plugin without restartingplugin ID`enable <pluginId>`Enable a disabled pluginplugin ID`disable <pluginId>`Disable a loaded pluginplugin ID

**Examples:**

```
# See what plugins are available
dms ipc call plugins list

# Check if a specific plugin is running
dms ipc call plugins status myPlugin

# Hot-reload during development (no shell restart needed)
dms ipc call plugins reload myPlugin

# Toggle plugins on/off
dms ipc call plugins enable myPlugin
dms ipc call plugins disable myPlugin
```

### systemupdater[​](#systemupdater "Direct link to systemupdater")

System updater external check request.

FunctionDescription`updatestatus`Trigger system update check

**Examples:**

```
dms ipc call systemupdater updatestatus
```

### desktopWidget[​](#desktopwidget "Direct link to desktopWidget")

Control desktop widget instances (clocks, system monitors, etc.).

FunctionDescriptionParameters`list`List all widget instances with ID, type, name, and status-`status <instanceId>`Get widget status (enabled, overlay, clickThrough, etc.)instance ID`enable <instanceId>`Enable the widgetinstance ID`disable <instanceId>`Disable the widgetinstance ID`toggleEnabled <instanceId>`Toggle widget enabled/disabledinstance ID`toggleOverlay <instanceId>`Toggle show on overlay layerinstance ID`setOverlay <instanceId> <bool>`Set overlay visibilityinstance ID, true/false`toggleClickThrough <instanceId>`Toggle click-through modeinstance ID`setClickThrough <instanceId> <bool>`Set click-through modeinstance ID, true/false`toggleSyncPosition <instanceId>`Toggle position sync across screensinstance ID`setSyncPosition <instanceId> <bool>`Set position sync across screensinstance ID, true/false

**Examples:**

```
# List all desktop widgets
dms ipc call desktopWidget list

# Get widget status
dms ipc call desktopWidget status dw_1234567890_abc123

# Toggle overlay visibility (useful for keybinds)
dms ipc call desktopWidget toggleOverlay dw_1234567890_abc123

# Enable click-through mode
dms ipc call desktopWidget setClickThrough dw_1234567890_abc123 true

# Toggle position sync
dms ipc call desktopWidget toggleSyncPosition dw_1234567890_abc123
```

**Notes:**

- Use `list` to discover widget instance IDs
- Click-through mode allows mouse clicks to pass through the widget to windows below
- Position sync keeps the widget at the same relative position across multiple monitors

## Scripting and Automation[​](#scripting-and-automation "Direct link to Scripting and Automation")

IPC commands are designed for integration with keybindings, scripts, and automation tools.

### Time-based Automation[​](#time-based-automation "Direct link to Time-based Automation")

```
#!/bin/bash
# Toggle night mode based on time of day
hour=$(date +%H)
if[$hour-ge20]||[$hour-le6];then
    dms ipc call night enable
else
    dms ipc call night disable
fi
```

### Status Checking[​](#status-checking "Direct link to Status Checking")

```
# Check if screen is locked before performing action
if dms ipc call lock isLocked |grep-q"false";then
    dms ipc call notifications open
fi
```

### Conditional Logic[​](#conditional-logic "Direct link to Conditional Logic")

```
# Increase brightness only if below threshold
current=$(dms ipc call brightness status |grep-oP'\d+')
if["$current"-lt50];then
    dms ipc call brightness set50
fi
```

## Return Values[​](#return-values "Direct link to Return Values")

Most IPC functions return string messages indicating:

- Success confirmation with current values
- Error messages if operation fails
- Status information for query functions
- Empty/void return for simple action functions

Functions that return void (like media controls) execute the action but don't provide feedback. Check the application state through other means if needed.

## Next Steps[​](#next-steps "Direct link to Next Steps")

See compositor-specific keybinding configuration in your compositor's documentation to integrate these IPC commands with your workflow.