---
title: Example configurations - Komorebi
url: https://lgug2z.github.io/komorebi/example-configurations.html
source: github_pages
fetched_at: 2026-02-20T08:45:00.216617-03:00
rendered_js: true
word_count: 1017
summary: This document provides a comprehensive guide to downloading and understanding example configuration files for the komorebi tiling window manager and whkd hotkey daemon. It explains how to customize window layouts, workspace padding, active borders, and keyboard shortcuts.
tags:
    - komorebi
    - window-manager
    - tiling-window-manager
    - configuration-guide
    - whkd
    - layout-management
    - windows-customization
category: configuration
---

[](https://github.com/LGUG2Z/komorebi/edit/master/docs/example-configurations.md "Edit this page")[](https://github.com/LGUG2Z/komorebi/raw/master/docs/example-configurations.md "View source of this page")

`komorebi`, and tiling window managers in general, are very complex pieces of software.

In an attempt to reduce some of the initial configuration burden for users who are looking to try out the software for the first time, example configurations are provided and updated whenever appropriate.

## Downloading example configurations

Run the following command to download example configuration files for `komorebi` and `whkd`. Pay attention to the output of the command to see where the example files have been downloaded. For most new users this will be in the `$Env:USERPROFILE` directory.

## Corporate Devices Enrolled in MDM

If you are using `komorebi` on a corporate device enrolled in mobile device management, you will receive a pop-up when you run `komorebic start` reminding you that the [Komorebi License](https://github.com/LGUG2Z/komorebi-license) does not permit any kind of commercial use.

You can remove this pop-up by running `komorebic license <email>` with the email associated with your Individual Commercial Use License. A single HTTP request will be sent with the given email address to verify license validity.

## Starting komorebi

With the example configurations downloaded, you can now start `komorebi`, `komorebi-bar` and `whkd`.

```
komorebic start --whkd --bar
```

If you don't want to use the komorebi status bar, you can remove the `--bar` option from the above command.

## komorebi.json

The example window manager configuration sets some sane defaults and provides seven preconfigured workspaces on the primary monitor each with a different layout.

```
{
"$schema":"https://raw.githubusercontent.com/LGUG2Z/komorebi/v0.1.39/schema.json",
"app_specific_configuration_path":"$Env:USERPROFILE/applications.json",
"window_hiding_behaviour":"Cloak",
"cross_monitor_move_behaviour":"Insert",
"default_workspace_padding":20,
"default_container_padding":20,
"border":true,
"border_width":8,
"border_offset":-1,
"theme":{
"palette":"Base16",
"name":"Ashes",
"unfocused_border":"Base03",
"bar_accent":"Base0D"
},
"monitors":[
{
"workspaces":[
{
"name":"I",
"layout":"BSP"
},
{
"name":"II",
"layout":"VerticalStack"
},
{
"name":"III",
"layout":"HorizontalStack"
},
{
"name":"IV",
"layout":"UltrawideVerticalStack"
},
{
"name":"V",
"layout":"Rows"
},
{
"name":"VI",
"layout":"Grid"
},
{
"name":"VII",
"layout":"RightMainVerticalStack"
}
]
}
]
}
```

### Application-specific configuration

There is a [community-maintained repository](https://github.com/LGUG2Z/komorebi-application-specific-configuration) of "apps behaving badly" that do not conform to Windows application development guidelines and behave erratically when used with `komorebi` without additional configuration.

You can always download the latest version of these configurations by running `komorebic fetch-asc`. The output of this command will also provide a line that you can paste into `komorebi.json` to ensure that the window manager looks for the file in the correction location.

When installing and running `komorebi` for the first time, the `komorebic quickstart` command will usually download this file to the `$Env:USERPROFILE` directory.

### Padding

While you can set the workspace padding (the space between the outer edges of the windows and the bezel of your monitor) and the container padding (the space between each of the tiled windows) for each workspace independently, you can also set a default for both of these values that will apply to all workspaces using `default_workspace_padding` and `default_container_padding`.

### Active window border

You may have seen videos and screenshots of people using `komorebi` with a thick, colourful active window border. You can also enable this by setting `border` to `true`. However, please be warned that this feature is a crude hack trying to compensate for the insistence of Microsoft Windows design teams to make custom borders with widths that are actually visible to the user a thing of the past and removing this capability from the Win32 API.

I know it's buggy, and I know that most of the it sucks, but this is something you should be bring up with the billion dollar company and not with me, the solo developer.

### Border colours

If you choose to use the active window border, you can set different colours to give you visual queues when you are focused on a single window, a stack of windows, or a window that is in monocle mode.

The example colours given are blue single, green for stack and pink for monocle.

### Layouts

#### BSP

```
+-------+-----+
|       |     |
|       +--+--+
|       |  |--|
+-------+--+--+
```

#### Vertical Stack

```
+-------+-----+
|       |     |
|       +-----+
|       |     |
+-------+-----+
```

#### RightMainVerticalStack

```
+-----+-------+
|     |       |
+-----+       |
|     |       |
+-----+-------+
```

#### Horizontal Stack

```
+------+------+
|             |
|------+------+
|      |      |
+------+------+
```

#### Columns

```
+--+--+--+--+
|  |  |  |  |
|  |  |  |  |
|  |  |  |  |
+--+--+--+--+
```

#### Rows

If you have a vertical monitor, I recommend using this layout.

```
+-----------+
|-----------|
|-----------|
|-----------|
+-----------+
```

#### Ultrawide Vertical Stack

If you have an ultrawide monitor, I recommend using this layout.

```
+-----+-----------+-----+
|     |           |     |
|     |           +-----+
|     |           |     |
|     |           +-----+
|     |           |     |
+-----+-----------+-----+
```

### Grid

If you like the `grid` layout in [LeftWM](https://github.com/leftwm/leftwm-layouts) this is almost exactly the same!

The `grid` layout does not support resizing windows tiles.

```
+-----+-----+   +---+---+---+   +---+---+---+   +---+---+---+
|     |     |   |   |   |   |   |   |   |   |   |   |   |   |
|     |     |   |   |   |   |   |   |   |   |   |   |   +---+
+-----+-----+   |   +---+---+   +---+---+---+   +---+---|   |
|     |     |   |   |   |   |   |   |   |   |   |   |   +---+
|     |     |   |   |   |   |   |   |   |   |   |   |   |   |
+-----+-----+   +---+---+---+   +---+---+---+   +---+---+---+
  4 windows       5 windows       6 windows       7 windows
```

## whkdrc

`whkd` is a fairly basic piece of software with a simple configuration format: key bindings go to the left of the colon, and shell commands go to the right of the colon.

As of [`v0.2.4`](https://github.com/LGUG2Z/whkd/releases/tag/v0.2.4), `whkd` can override most of Microsoft's limitations on hotkey bindings that include the `win` key. However, you will still need to [modify the registry](https://superuser.com/questions/1059511/how-to-disable-winl-in-windows-10) to prevent `win + l` from locking the operating system.

You can toggle an overlay of the current `whkdrc` shortcuts related to `komorebi` at any time when using the example configuration with `alt + i`.

```
.shell powershell

# Reload whkd configuration
# alt + o                 : taskkill /f /im whkd.exe && start /b whkd # if shell is cmd
alt + o                 : taskkill /f /im whkd.exe; Start-Process whkd -WindowStyle hidden # if shell is pwsh / powershell
alt + shift + o         : komorebic reload-configuration

alt + i                 : komorebic toggle-shortcuts

# App shortcuts - these require shell to be pwsh / powershell
# The apps will be focused if open, or launched if not open
# alt + f                 : if ($wshell.AppActivate('Firefox') -eq $False) { start firefox }
# alt + b                 : if ($wshell.AppActivate('Chrome') -eq $False) { start chrome }

alt + q                 : komorebic close
alt + m                 : komorebic minimize

# Focus windows
alt + h                 : komorebic focus left
alt + j                 : komorebic focus down
alt + k                 : komorebic focus up
alt + l                 : komorebic focus right
alt + shift + oem_4     : komorebic cycle-focus previous # oem_4 is [
alt + shift + oem_6     : komorebic cycle-focus next # oem_6 is ]

# Move windows
alt + shift + h         : komorebic move left
alt + shift + j         : komorebic move down
alt + shift + k         : komorebic move up
alt + shift + l         : komorebic move right
alt + shift + return    : komorebic promote

# Stack windows
alt + left              : komorebic stack left
alt + down              : komorebic stack down
alt + up                : komorebic stack up
alt + right             : komorebic stack right
alt + oem_1             : komorebic unstack # oem_1 is ;
alt + oem_4             : komorebic cycle-stack previous # oem_4 is [
alt + oem_6             : komorebic cycle-stack next # oem_6 is ]

# Resize
alt + oem_plus          : komorebic resize-axis horizontal increase
alt + oem_minus         : komorebic resize-axis horizontal decrease
alt + shift + oem_plus  : komorebic resize-axis vertical increase
alt + shift + oem_minus : komorebic resize-axis vertical decrease

# Manipulate windows
alt + t                 : komorebic toggle-float
alt + shift + f         : komorebic toggle-monocle

# Window manager options
alt + shift + r         : komorebic retile
alt + p                 : komorebic toggle-pause

# Layouts
alt + x                 : komorebic flip-layout horizontal
alt + y                 : komorebic flip-layout vertical

# Workspaces
alt + 1                 : komorebic focus-workspace 0
alt + 2                 : komorebic focus-workspace 1
alt + 3                 : komorebic focus-workspace 2
alt + 4                 : komorebic focus-workspace 3
alt + 5                 : komorebic focus-workspace 4
alt + 6                 : komorebic focus-workspace 5
alt + 7                 : komorebic focus-workspace 6
alt + 8                 : komorebic focus-workspace 7

# Move windows across workspaces
alt + shift + 1         : komorebic move-to-workspace 0
alt + shift + 2         : komorebic move-to-workspace 1
alt + shift + 3         : komorebic move-to-workspace 2
alt + shift + 4         : komorebic move-to-workspace 3
alt + shift + 5         : komorebic move-to-workspace 4
alt + shift + 6         : komorebic move-to-workspace 5
alt + shift + 7         : komorebic move-to-workspace 6
alt + shift + 8         : komorebic move-to-workspace 7
```

### Configuration

`whkd` searches for a `whkdrc` configuration file in the following locations:

- `$Env:WHKD_CONFIG_HOME`
- `$Env:USERPROFILE/.config`

It is also possible to change a hotkey behavior depending on which application has focus:

```
alt + n [
    # ProcessName as shown by `Get-Process`
    Firefox       : echo "hello firefox"

    # Spaces are fine, no quotes required
    Google Chrome : echo "hello chrome"
]
```

### Setting .shell

There is one special directive at the top of the file, `.shell` which can be set to either `powershell`, `pwsh` or `cmd`. Which one you use will depend on which shell you use in your terminal.

- `powershell` - set this if you are using the version of PowerShell that comes installed with Windows 10+ (the executable file for this is `powershell.exe`)
- `pwsh` - set this if you are using PowerShell 7+, which you have installed yourself either through the Windows Store or WinGet (the executable file for this is `pwsh.exe`)
- `cmd` - set this if you don't want to use PowerShell at all and instead you want to call commands through the shell used by the old-school Command Prompt (the executable file for this is `cmd.exe`)

### Key codes

Key codes for alphanumeric and arrow keys are just what you would expect. For punctuation and other keys, please refer to the [Virtual Key Codes](https://learn.microsoft.com/en-us/windows/win32/inputdev/virtual-key-codes) reference.

If you want to use one of those key codes, put them into lower case and remove the `VK_` prefix. For example, the keycode `VK_OEM_PLUS` becomes `oem_plus` in the sample configuration above.

## komorebi.bar.json

The example status bar configuration sets some sane defaults and provides a number of pre-configured widgets on the primary monitor.

```
{
"$schema":"https://raw.githubusercontent.com/LGUG2Z/komorebi/v0.1.39/schema.bar.json",
"monitor":0,
"font_family":"JetBrains Mono",
"theme":{
"palette":"Base16",
"name":"Ashes",
"accent":"Base0D"
},
"left_widgets":[
{
"Komorebi":{
"workspaces":{
"enable":true,
"hide_empty_workspaces":false
},
"layout":{
"enable":true
},
"focused_window":{
"enable":true,
"show_icon":true
}
}
}
],
"right_widgets":[
{
"Update":{
"enable":true
}
},
{
"Media":{
"enable":true
}
},
{
"Storage":{
"enable":true
}
},
{
"Memory":{
"enable":true
}
},
{
"Network":{
"enable":true,
"show_activity":true,
"show_total_activity":true
}
},
{
"Date":{
"enable":true,
"format":"DayDateMonthYear"
}
},
{
"Time":{
"enable":true,
"format":"TwentyFourHour"
}
},
{
"Battery":{
"enable":true
}
}
]
}
```

### Themes

Themes can be set in either `komorebi.json` or `komorebi.bar.json`. If set in `komorebi.json`, the theme will be applied to both komorebi's borders and stackbars as well as the status bar.

If set in `komorebi.bar.json`, the theme will only be applied to the status bar.

All [Catppuccin palette variants](https://catppuccin.com/) and [most Base16 palette variants](https://tinted-theming.github.io/tinted-gallery/) are available as themes.