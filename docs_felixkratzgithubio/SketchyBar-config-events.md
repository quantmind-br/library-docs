---
title: Events & Scripting | SketchyBar
url: https://felixkratz.github.io/SketchyBar/config/events
source: github_pages
fetched_at: 2026-02-15T21:17:17.278454-03:00
rendered_js: false
word_count: 686
summary: This document explains the event-driven scripting system in SketchyBar, detailing how to subscribe to system events, create custom triggers, and utilize environment variables within scripts.
tags:
    - sketchybar
    - macos-customization
    - event-handling
    - shell-scripting
    - automation
    - system-events
category: guide
---

## Events and Scripting[​](#events-and-scripting "Direct link to heading")

All items can *subscribe* to arbitrary *events*; when the *event* happens, all items subscribed to the *event* will execute their *script*. This can be used to create more reactive and performant items which react to events rather than polling for a change.

```
sketchybar --subscribe <name><event>... <event>
```

where the events are:

&lt;event&gt;description`$INFO``front_app_switched`When the front application changes (not triggered if a different window of the same app is focused)front application name`space_change`When the active mission control space changesJSON for active spaces on all displays`space_windows_change`When a window is created or destroyed on a spaceJSON containing the space and all app windows on this space`display_change`When the active display is changednew active display id`volume_change`When the system audio volume is changednew volume in percent`brightness_change`When a displays brightness is changednew brightness in percent`power_source_change`When the devices power source is changednew power source (`AC` or `BATTERY`)`wifi_change`When the device connects of disconnects from wifinew WiFi SSID or empty on disconnect (not working since macOS Sonoma)`media_change`When a change in now playing media is performed (deprecated on macOS 26.0)media info in a JSON structure`system_will_sleep`When the system prepares to sleep`system_woke`When the system has awaken from sleep`mouse.entered`When the mouse enters over an item`mouse.exited`When the mouse leaves an item`mouse.entered.global`When the mouse enters over *any* part of the bar`mouse.exited.global`When the mouse leaves *all* parts of the bar`mouse.clicked`When an item is clickedmouse button and modifier info`mouse.scrolled`When the mouse is scrolled over an itemscroll wheel delta`mouse.scrolled.global`When the mouse is scrolled over an empty region of the barscroll wheel delta

Some events send additional information in the `$INFO` variable When an item is subscribed to these events the *script* is run and it gets passed the `$SENDER` variable, which holds exactly the above names to distinguish between the different events. It is thus possible to have a script that reacts to each event differently e.g. via a switch for the `$SENDER` variable in the *script*.

Alternatively a fixed *update\_freq* can be *--set*, such that the event is routinely run to poll for change, the `$SENDER` variable will in this case hold the value `routine`.

When an item invokes a script, the script has access to some environment variables, such as:

Where `$NAME` is the name of the item that has invoked the script and `$SENDER` is the reason why the script is executed. The variable `$CONFIG_DIR` contains the absolute path of the directory where the current sketchybarrc file is located.

If an item is *clicked* the script has access to the additional variables:

where the `$BUTTON` can be *left*, *right* or *other* and specifies the mouse button that was used to click the item, while the `$MODIFIER` is either *shift*, *ctrl*, *alt* or *cmd* and specifies the modifier key held down while clicking the item.

If an item receive a *scroll* event from the mouse the script gets send the additional `$SCROLL_DELTA` variable.

All scripts are forced to terminate after 60 seconds and do not run while the system is sleeping.

### Creating custom events[​](#creating-custom-events "Direct link to heading")

This allows to define events which are triggered by arbitrary applications or manually (see Trigger custom events). Items can also subscribe to these events for their script execution.

```
sketchybar --add event <name>[optional: <NSDistributedNotificationName>]
```

Optional: You can subscribe to the notifications sent to the NSDistributedNotificationCenter e.g. the notification Spotify sends on track change: `com.spotify.client.PlaybackStateChanged` ([example](https://github.com/FelixKratz/SketchyBar/discussions/12#discussioncomment-1455842)), or the notification sent by the system when the screen is unlocked: `com.apple.screenIsUnlocked` ([example](https://github.com/FelixKratz/SketchyBar/discussions/12?sort=new#discussioncomment-2979651)) to create more responsive items. Custom events that subscribe to NSDistributedNotificationCenter notifications will receive additional notification information in the `$INFO` variable if available. For more NSDistributedNotifications see [this discussion](https://github.com/FelixKratz/SketchyBar/discussions/151).

### Triggering custom events[​](#triggering-custom-events "Direct link to heading")

This triggers a custom event that has been added before

```
sketchybar --trigger <event>[Optional: <envvar>=<value>... <envvar>=<value>]
```

Optionally you can add environment variables to the trigger command witch are passed to the script, e.g.:

```
sketchybar --trigger demo VAR=Test
```

will trigger the demo event and `$VAR` will be available as an environment variable in the scripts that this event invokes.

### Forcing all shell scripts to run and the bar to refresh[​](#forcing-all-shell-scripts-to-run-and-the-bar-to-refresh "Direct link to heading")

This command forces all scripts to run and all events to be emitted, it should *never* be used in an item script, as this would lead to infinite loops. It is prominently needed after the initial configuration to properly initialize all items by forcing all their scripts to run