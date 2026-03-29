---
title: AeroSpace Goodies
url: https://nikitabobko.github.io/AeroSpace/goodies
source: github_pages
fetched_at: 2026-02-08T11:27:16.896120276-03:00
rendered_js: false
word_count: 706
summary: A collection of community-contributed tips, automations, and configuration snippets for the AeroSpace tiling window manager on macOS.
tags:
    - aerospace
    - macos
    - window-management
    - automation
    - tiling-window-manager
    - workflow-optimization
    - configuration-snippets
category: configuration
---

Do you have a cool automatization, AeroSpace integration, or workflow? Feel free to open an issue or pull request to add it to this list! The source code of the page can be found in the `./docs` directory.

## [](#move-by-dragging-any-part-of-the-window)[1. Move windows by dragging any part of the window](#move-by-dragging-any-part-of-the-window)

```
defaultswrite-gNSWindowShouldDragOnGesture-booltrue
```

Now, you can move windows by holding `ctrl + cmd` and dragging any part of the window (not necessarily the window title)

## [](#non-native-fullscreen-in-firefox)[2. Non-native fullscreen in Firefox](#non-native-fullscreen-in-firefox)

Change the following settings in `about:config`:

```
// Disable macOS native fullscreen in Firefox
full-screen-api.macos-native-full-screen = false

// Disable fullscreen transition animations
full-screen-api.transition-duration.enter = 0 0
full-screen-api.transition-duration.leave = 0 0
```

`full-screen-api.ignore-widgets` is also an interesting config knob that might be of your preference.

## [](#highlight-focused-windows-with-colored-borders)[3. Highlight focused windows with colored borders](#highlight-focused-windows-with-colored-borders)

To highlight the focused window with colored border you can use [JankyBorders](https://github.com/FelixKratz/JankyBorders).

You can also use `after-startup-command` to start JankyBorders together with AeroSpace

```
after-startup-command=[
# JankyBorders has a built-in detection of already running process,
# so it won't be run twice on AeroSpace restart
'exec-and-forget borders active_color=0xffe1e3e4 inactive_color=0xff494d64 width=5.0'
]
```

## [](#raycast-extension)[4. AeroSpace Raycast extension](#raycast-extension)

If you struggle remembering shortcuts, it’s useful to search for commands until they become muscle memory.

## [](#disable-open-animations)[5. Disable windows opening animations](#disable-open-animations)

Observable in Google Chrome

```
defaultswrite-gNSAutomaticWindowAnimationsEnabled-boolfalse
```

## [](#show-aerospace-workspaces-in-sketchybar)[7. Show AeroSpace workspaces in Sketchybar](#show-aerospace-workspaces-in-sketchybar)

You can integrate AeroSpace workspace indicators with [Sketchybar](https://github.com/FelixKratz/SketchyBar). Use these snippets as a starting point.

~/.aerospace.toml

```
# Run Sketchybar together with AeroSpace
# sketchybar has a built-in detection of already running process,
# so it won't be run twice on AeroSpace restart
after-startup-command=['exec-and-forget sketchybar']

# Notify Sketchybar about workspace change
exec-on-workspace-change=['/bin/bash','-c',
'sketchybar --trigger aerospace_workspace_change FOCUSED_WORKSPACE=$AEROSPACE_FOCUSED_WORKSPACE'
]
```

~/.config/sketchybar/sketchybarrc

```
sketchybar--addeventaerospace_workspace_change

forsidin$(aerospacelist-workspaces--all);do
sketchybar--additemspace.$sidleft\
--subscribespace.$sidaerospace_workspace_change\
--setspace.$sid\
background.color=0x44ffffff\
background.corner_radius=5\
background.height=20\
background.drawing=off\
label="$sid"\
click_script="aerospace workspace $sid"\
script="$CONFIG_DIR/plugins/aerospace.sh $sid"
done
```

~/.config/sketchybar/plugins/aerospace.sh

```
#!/usr/bin/env bash

# make sure it's executable with:
# chmod +x ~/.config/sketchybar/plugins/aerospace.sh

if["$1"="$FOCUSED_WORKSPACE"];then
sketchybar--set$NAMEbackground.drawing=on
else
sketchybar--set$NAMEbackground.drawing=off
fi
```

## [](#show-aerospace-workspaces-in-simple-bar)[8. Show AeroSpace workspaces in simple-bar](#show-aerospace-workspaces-in-simple-bar)

[simple-bar](https://github.com/Jean-Tinland/simple-bar) can be used to display AeroSpace workspaces.

In order to sync simple-bar with AeroSpace, add these lines to your AeroSpace config file:

~/.aerospace.toml

```
# Notify simple-bar about window focus change
on-focus-changed=[
"exec-and-forget osascript -e 'tell application id \"tracesOf.Uebersicht\" to refresh widget id \"simple-bar-index-jsx\"'",
]

# Notify simple-bar about workspace change
exec-on-workspace-change=[
'/bin/zsh',
'-c',
'/usr/bin/osascript -e "tell application id \"tracesOf.Uebersicht\" to refresh widget id \"simple-bar-index-jsx\""',
]
```

## [](#open-a-new-window-with-applescript)[9. Open a new window with AppleScript](#open-a-new-window-with-applescript)

Invoking Safari/Terminal with a command the obvious way (`exec-and-forget open -a Safari`) results in an outcome that is probably not the intended one. Namely, that any workspace already containing an instance of Safari/Terminal is brought in focus.

Opening **a new window** of a program that can support multiple windows (such as Safari or Terminal.app) can be accomplished with an AppleScript inlined in `aerospace.toml` as follows:

- Safari
  
  ```
  ctrl-g='''exec-and-forget osascript -e '
  tell application "Safari"
      make new document at end of documents
      activate
  end tell'
  '''
  ```
- Terminal
  
  ```
  ctrl-g='''exec-and-forget osascript -e '
  tell application "Terminal"
      do script
      activate
  end tell'
  '''
  ```

## [](#disable-hide-app)[10. Disable annoying and useless "hide application" shortcut](#disable-hide-app)

If `automatically-unhide-macos-hidden-apps` isn’t enough, you can disable `cmd-h` altogether (which will make this hotkey unavailable for apps that might use it for other purposes)

~/.aerospace.toml

```
[mode.main.binding]
cmd-h=[]# Disable "hide application"
cmd-alt-h=[]# Disable "hide others"
```

## [](#screenshoot-shortcut)[11. Take screenshots to clipboard using keyboard shortcut](#screenshoot-shortcut)

You can configure a custom shortcut to take a screenshot. `screencapture` is a built-in macOS command.

~/.aerospace.toml

```
alt-shift-s='exec-and-forget screencapture -i -c'
```

## [](#i3-like-config)[12. i3 like config](#i3-like-config)

```
# Reference: https://github.com/i3/i3/blob/next/etc/config

config-version=2

# In i3, all workspaces are phantom
persistent-workspaces=[]

# i3 doesn't have "normalizations" feature that why we disable them here.
# But the feature is very helpful.
# Normalizations eliminate all sorts of weird tree configurations that don't make sense.
# Give normalizations a chance and enable them back.
enable-normalization-flatten-containers=false
enable-normalization-opposite-orientation-for-nested-containers=false

# Mouse follows focus when focused monitor changes
on-focused-monitor-changed=['move-mouse monitor-lazy-center']

[mode.main.binding]
# See: https://nikitabobko.github.io/AeroSpace/goodies#open-a-new-window-with-applescript
alt-enter='''exec-and-forget osascript -e '
    tell application "Terminal"
        do script
        activate
    end tell'
    '''

# i3 wraps focus by default
alt-j='focus --boundaries-action wrap-around-the-workspace left'
alt-k='focus --boundaries-action wrap-around-the-workspace down'
alt-l='focus --boundaries-action wrap-around-the-workspace up'
alt-semicolon='focus --boundaries-action wrap-around-the-workspace right'

alt-shift-j='move left'
alt-shift-k='move down'
alt-shift-l='move up'
alt-shift-semicolon='move right'

# Consider using 'join-with' command as a 'split' replacement if you want to enable
# normalizations
alt-h='split horizontal'
alt-v='split vertical'

alt-f='fullscreen'

alt-s='layout v_accordion'# 'layout stacking' in i3
alt-w='layout h_accordion'# 'layout tabbed' in i3
alt-e='layout tiles horizontal vertical'# 'layout toggle split' in i3

alt-shift-space='layout floating tiling'# 'floating toggle' in i3

# Not supported, because this command is redundant in AeroSpace mental model.
# See: https://nikitabobko.github.io/AeroSpace/guide#floating-windows
#alt-space = 'focus toggle_tiling_floating'

# `focus parent`/`focus child` are not yet supported, and it's not clear whether they
# should be supported at all https://github.com/nikitabobko/AeroSpace/issues/5
# alt-a = 'focus parent'

alt-1='workspace 1'
alt-2='workspace 2'
alt-3='workspace 3'
alt-4='workspace 4'
alt-5='workspace 5'
alt-6='workspace 6'
alt-7='workspace 7'
alt-8='workspace 8'
alt-9='workspace 9'
alt-0='workspace 10'

alt-shift-1='move-node-to-workspace 1'
alt-shift-2='move-node-to-workspace 2'
alt-shift-3='move-node-to-workspace 3'
alt-shift-4='move-node-to-workspace 4'
alt-shift-5='move-node-to-workspace 5'
alt-shift-6='move-node-to-workspace 6'
alt-shift-7='move-node-to-workspace 7'
alt-shift-8='move-node-to-workspace 8'
alt-shift-9='move-node-to-workspace 9'
alt-shift-0='move-node-to-workspace 10'

alt-shift-c='reload-config'

alt-r='mode resize'

[mode.resize.binding]
h='resize width -50'
j='resize height +50'
k='resize height -50'
l='resize width +50'
enter='mode main'
esc='mode main'
```

## [](#popular-apps-ids)[13. List of Apple application IDs](#popular-apps-ids)

  Application name Application ID

Activity Monitor

`com.apple.ActivityMonitor`

AirPort Utility

`com.apple.airport.airportutility`

App Store

`com.apple.AppStore`

Audio MIDI Setup

`com.apple.audio.AudioMIDISetup`

Automator

`com.apple.Automator`

Books

`com.apple.iBooksX`

Calculator

`com.apple.calculator`

Calendar

`com.apple.iCal`

Chess

`com.apple.Chess`

Clock

`com.apple.clock`

ColorSync Utility

`com.apple.ColorSyncUtility`

Console

`com.apple.Console`

Contacts

`com.apple.AddressBook`

Dictionary

`com.apple.Dictionary`

Disk Utility

`com.apple.DiskUtility`

FaceTime

`com.apple.FaceTime`

Find My

`com.apple.findmy`

Finder

`com.apple.finder`

Freeform

`com.apple.freeform`

Grapher

`com.apple.grapher`

Home

`com.apple.Home`

iMovie

`com.apple.iMovieApp`

Keychain Access

`com.apple.keychainaccess`

Keynote

`com.apple.iWork.Keynote`

Mail

`com.apple.mail`

Maps

`com.apple.Maps`

Messages

`com.apple.MobileSMS`

Music

`com.apple.Music`

Notes

`com.apple.Notes`

Pages

`com.apple.iWork.Pages`

Photo Booth

`com.apple.PhotoBooth`

Photos

`com.apple.Photos`

Podcasts

`com.apple.podcasts`

Preview

`com.apple.Preview`

QuickTime Player

`com.apple.QuickTimePlayerX`

Reminders

`com.apple.reminders`

Safari

`com.apple.Safari`

Shortcuts

`com.apple.shortcuts`

Stocks

`com.apple.stocks`

System Settings

`com.apple.systempreferences`

Terminal

`com.apple.Terminal`

TextEdit

`com.apple.TextEdit`

Time Machine

`com.apple.backup.launcher`

TV

`com.apple.TV`

VoiceMemos

`com.apple.VoiceMemos`

VoiceOver Utility

`com.apple.VoiceOverUtility`

Weather

`com.apple.weather`

Xcode

`com.apple.dt.Xcode`