---
title: New Desktop Widgets & Plugins Coming in DMS 1.2
url: https://danklinux.com/blog/desktop-widgets-1-2
source: sitemap
fetched_at: 2026-04-26T08:35:00.452301245-03:00
rendered_js: false
word_count: 462
summary: This document introduces Desktop Widgets for the Dank Material Shell (DMS) 1.2 release and provides a technical walkthrough for developers on how to create, configure, and install custom desktop plugins.
tags:
    - dms
    - desktop-widgets
    - plugin-development
    - qml-development
    - custom-ui
    - software-release
category: tutorial
optimized: true
optimized_at: 2026-04-26T12:00:00Z
---

DMS 1.2 introduces **Desktop Widgets** — small applets that live on your desktop, below windows and above your wallpaper. They are positioned, placed, and sized per-display.

With the DMS plugin system, these widgets are easy to build. DMS 1.2 ships with two built-in desktop widgets:

### Clock

A configurable clock with analog and digital modes, modeled after Material Design expressive clock widgets.

![Desktop Clock Widget](https://danklinux.com/img/blog/widgets/clock_light.png) ![Desktop Clock Widget](https://danklinux.com/img/blog/widgets/clock_dark.png)

### System Monitor (dgop)

A configurable system monitor displaying CPU, memory, GPU, disk, network, process, temperature, and other system information in a variety of formats.

![System Monitor Widget](https://danklinux.com/img/blog/widgets/dgop_light.png) ![System Monitor Widget](https://danklinux.com/img/blog/widgets/dgop_dark.png)

One first-party plugin is available on the registry: **Dank Desktop Weather** (requires DMS git/nightly). This plugin adds a weather widget showing current conditions and forecasts.

![Dank Desktop Weather Plugin](https://danklinux.com/img/blog/widgets/weather_light.png) ![Dank Desktop Weather Plugin](https://danklinux.com/img/blog/widgets/weather_dark.png)

## Building Your Own

Making your own desktop widget is straightforward. If you've written JavaScript and a declarative layout (React, Vue, JSON, etc.), it should feel familiar.

### 1. Create the plugin folder

```bash
mkdir -p ~/.config/DankMaterialShell/plugins/MyDesktopWidget
cd ~/.config/DankMaterialShell/plugins/MyDesktopWidget
```

### 2. Write the manifest

Save as `plugin.json`:

```json
{
  "id": "myDesktopWidget",
  "name": "My Desktop Widget",
  "description": "A custom desktop widget",
  "version": "1.0.0",
  "author": "Your Name",
  "type": "desktop",
  "license": "<your-license-here>",
  "component": "./MyWidget.qml",
  "icon": "widgets",
  "settings": "./MySettings.qml",
  "requires_dms": ">=1.2.0"
}
```

The key is `"type": "desktop"` — that tells DMS this is a desktop widget, not a bar widget.

### 3. Create the widget

Save as `MyWidget.qml`:

```qml
import QtQuick
import qs.Common
import qs.Widgets
import qs.Modules.Plugins

DesktopPluginComponent {
  id: root
  minWidth: 150
  minHeight: 100
  property string displayText: pluginData.displayText ?? "Hello!"
  property real bgOpacity: (pluginData.backgroundOpacity ?? 80) / 100

  Rectangle {
    anchors.fill: parent
    radius: Theme.cornerRadius
    color: Theme.withAlpha(Theme.surfaceContainer, root.bgOpacity)
    StyledText {
      anchors.centerIn: parent
      text: root.displayText
      color: Theme.surfaceText
      font.pixelSize: Theme.fontSizeLarge
    }
  }
}
```

Users can right-click and drag to move or resize the widget. The `minWidth`/`minHeight` properties set the lower bounds.

### 4. Create the settings panel

Save as `MySettings.qml`:

```qml
import QtQuick
import qs.Common
import qs.Modules.Plugins

PluginSettings {
  id: root
  pluginId: "myDesktopWidget"

  StringSetting {
    settingKey: "displayText"
    label: "Display Text"
    description: "Text shown in the widget"
    placeholder: "Enter text"
    defaultValue: "Hello!"
  }

  SliderSetting {
    settingKey: "backgroundOpacity"
    label: "Background Opacity"
    defaultValue: 80
    minimum: 0
    maximum: 100
    unit: "%"
  }
}
```

Display settings (position, size, which monitors) are injected automatically — you don't need to handle those.

### 5. Load it

1. Open **Settings → Plugins**
2. Click **Scan for Plugins**
3. Toggle your plugin on
4. Open **Settings → Widgets** and enable the widget on your desired display

For settings panels, timers, graphs, and more, see [[018-docs-dankmaterialshell-plugin-development#desktop-plugins|plugin development guide]].

## Get Involved

Some ideas for desktop widgets:

- Media controls (mpris, spotify, etc.)
- Todo lists
- Stock/Crypto tickers
- News feeds

Submit plugins to the [plugin registry](https://github.com/AvengeMedia/dms-plugin-registry) — we hope to feature some in the next DMS release.

Desktop widgets land in **DMS 1.2**. Keep an eye on the repo and [join the Discord](https://discord.gg/ppWTpKmPgT) if you want to get started early.

#desktop-widgets #plugin-development #dms #qml
