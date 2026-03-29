---
title: Development | Dank Linux
url: https://danklinux.com/docs/dankmaterialshell/plugin-development
source: sitemap
fetched_at: 2026-01-24T13:35:58.826029899-03:00
rendered_js: false
word_count: 1205
summary: This document provides a comprehensive guide for developing and deploying plugins for DankMaterialShell, covering environment setup, manifest configuration, and QML component patterns.
tags:
    - dank-material-shell
    - plugin-development
    - qml
    - widget-creation
    - environment-setup
    - manifest-configuration
category: tutorial
---

```
██████╗ ███████╗██╗   ██╗
██╔══██╗██╔════╝██║   ██║
██║  ██║█████╗  ██║   ██║
██║  ██║██╔══╝  ╚██╗ ██╔╝
██████╔╝███████╗ ╚████╔╝
╚═════╝ ╚══════╝  ╚═══╝  
```

Build and ship plugins for DankMaterialShell. This guide covers the actual patterns and components you'll use, with real working examples from the plugin library.

## Development Environment[​](#development-environment "Direct link to Development Environment")

For IDE support (autocomplete, type checking, etc.), clone the DMS repo and develop plugins there:

```
mkdir-p ~/repos &&cd ~/repos
git clone https://github.com/AvengeMedia/DankMaterialShell.git
cd DankMaterialShell/quickshell

# Generate QML language server config
touch .qmlls.ini
qs -p.# Press Ctrl+C after it starts

# Create your plugins here
mkdir-p dms-plugins/MyPlugin
```

### VSCode Setup[​](#vscode-setup "Direct link to VSCode Setup")

1. Install the [QML Extension](https://marketplace.visualstudio.com/items?itemName=TheQtCompany.qt-qml)
2. Configure qmlls path via `Ctrl+Shift+P` → "Preferences: Open User Settings (JSON)":

```
{
"qt-qml.doNotAskForQmllsDownload":true,
"qt-qml.qmlls.customExePath":"/usr/lib/qt6/bin/qmlls"
}
```

3. Open VSCode in the `~/repos/DankMaterialShell/quickshell` directory

### Live Development[​](#live-development "Direct link to Live Development")

Symlink your plugin to the DMS plugins directory for live testing:

```
ln-sf ~/repos/DankMaterialShell/quickshell/dms-plugins/MyPlugin \
       ~/.config/DankMaterialShell/plugins/MyPlugin
```

Reload your plugin at runtime without restarting DMS:

```
dms ipc call plugins reload myPlugin
```

List all plugins and their status:

```
dms ipc call plugins list
```

tip

Use [Run on Save](https://marketplace.visualstudio.com/items?itemName=emeraldwalk.RunOnSave) to auto-reload your plugin during development. The reload command uses the plugin `id` from your `plugin.json`.

## Quick Start[​](#quick-start "Direct link to Quick Start")

### 1. Create Plugin Directory[​](#1-create-plugin-directory "Direct link to 1. Create Plugin Directory")

```
mkdir-p ~/.config/DankMaterialShell/plugins/MyPlugin
cd ~/.config/DankMaterialShell/plugins/MyPlugin
```

### 2. Create Manifest[​](#2-create-manifest "Direct link to 2. Create Manifest")

Save this as `plugin.json`:

```
{
"id":"myPlugin",
"name":"My Plugin",
"description":"What this plugin does",
"version":"1.0.0",
"author":"Your Name",
"icon":"widgets",
"type":"widget",
"component":"./MyWidget.qml",
"settings":"./MySettings.qml",
"permissions":["settings_read","settings_write"]
}
```

### 3. Create Widget Component[​](#3-create-widget-component "Direct link to 3. Create Widget Component")

Save this as `MyWidget.qml`:

```
import QtQuick
import qs.Common
import qs.Services
import qs.Widgets
import qs.Modules.Plugins

PluginComponent{
id:root

propertystringdisplayText:pluginData.displayText ||"Hello"

horizontalBarPill:Component{
Row{
spacing:Theme.spacingS

DankIcon{
name:"widgets"
size:Theme.iconSize
color:Theme.primary
anchors.verticalCenter:parent.verticalCenter
}

StyledText{
text:root.displayText
font.pixelSize:Theme.fontSizeMedium
color:Theme.surfaceText
anchors.verticalCenter:parent.verticalCenter
}
}
}

verticalBarPill:Component{
Column{
spacing:Theme.spacingXS

DankIcon{
name:"widgets"
size:Theme.iconSize
color:Theme.primary
anchors.horizontalCenter:parent.horizontalCenter
}

StyledText{
text:root.displayText
font.pixelSize:Theme.fontSizeSmall
color:Theme.surfaceText
anchors.horizontalCenter:parent.horizontalCenter
}
}
}
}
```

### 4. Create Settings Component[​](#4-create-settings-component "Direct link to 4. Create Settings Component")

Save this as `MySettings.qml`:

```
import QtQuick
import qs.Common
import qs.Modules.Plugins
import qs.Widgets

PluginSettings{
id:root
pluginId:"myPlugin"

StyledText{
width:parent.width
text:"My Plugin Settings"
font.pixelSize:Theme.fontSizeLarge
font.weight:Font.Bold
color:Theme.surfaceText
}

StyledText{
width:parent.width
text:"Configure your plugin here"
font.pixelSize:Theme.fontSizeSmall
color:Theme.surfaceVariantText
wrapMode:Text.WordWrap
}

StringSetting{
settingKey:"displayText"
label:"Display Text"
description:"Text shown in the bar"
placeholder:"Enter text"
defaultValue:"Hello"
}
}
```

### 5. Load It[​](#5-load-it "Direct link to 5. Load It")

1. Open DMS Settings → Plugins
2. Click "Scan for Plugins"
3. Toggle your plugin on
4. Add to DankBar widget list
5. Restart shell: `dms restart`

You now have a working plugin.

Widget plugins show up in DankBar or the Control Center. They use `PluginComponent` as the base.

### DankBar Widget[​](#dankbar-widget "Direct link to DankBar Widget")

Here's a real color display widget:

```
import QtQuick
import qs.Common
import qs.Services
import qs.Widgets
import qs.Modules.Plugins

PluginComponent{
id:root

propertycolorcustomColor:pluginData.customColor || Theme.primary

horizontalBarPill:Component{
Row{
spacing:Theme.spacingS

Rectangle{
width:20
height:20
radius:4
color:root.customColor
border.color:Theme.outlineStrong
border.width:1
anchors.verticalCenter:parent.verticalCenter
}

StyledText{
text:root.customColor.toString()
font.pixelSize:Theme.fontSizeSmall
color:Theme.surfaceText
anchors.verticalCenter:parent.verticalCenter
}
}
}

verticalBarPill:Component{
Column{
spacing:Theme.spacingXS

Rectangle{
width:20
height:20
radius:4
color:root.customColor
border.color:Theme.outlineStrong
border.width:1
anchors.horizontalCenter:parent.horizontalCenter
}

StyledText{
text:root.customColor.toString()
font.pixelSize:Theme.fontSizeSmall
color:Theme.surfaceText
anchors.horizontalCenter:parent.horizontalCenter
}
}
}
}
```

The widget pulls `customColor` from `pluginData`, which automatically syncs with your settings. No manual loading needed.

### Widget with Popout[​](#widget-with-popout "Direct link to Widget with Popout")

Add a popout menu that opens when you click the widget.

To add a layer namespace to your plugin, just add `layerNamespacePlugin: "<namespace for your plugin>"` like below. Make sure to only type what you want the namespace to be and to not add a prefix (like `dms:` or `dms-plugin:` for example) since the shell will add `dms-plugin:` as a prefix automatically. For example, the namespace of the plugin below will be `dms-plugin:emoji-launcher`.

While you don't have to add a layer namespace to you widget (it will fallback to `dms-plugin:plugin`), it's prefered to do so.

warning

As of right now, layer namespace only work with popout widget plugins.

```
PluginComponent{
id:root

layerNamespacePlugin:"emoji-launcher"

propertyvardisplayedEmojis:["😊","😢","❤️"]

horizontalBarPill:Component{
Row{
spacing:Theme.spacingXS
Repeater{
model:root.displayedEmojis
StyledText{
text:modelData
font.pixelSize:Theme.fontSizeLarge
}
}
}
}

verticalBarPill:Component{
Column{
spacing:Theme.spacingXS
Repeater{
model:root.displayedEmojis
StyledText{
text:modelData
font.pixelSize:Theme.fontSizeMedium
anchors.horizontalCenter:parent.horizontalCenter
}
}
}
}

popoutContent:Component{
PopoutComponent{
id:popoutColumn

headerText:"Emoji Picker"
detailsText:"Click an emoji to copy it"
showCloseButton:true

propertyvarallEmojis:[
"😀","😃","😄","😁","😆","🤣",
"❤️","🧡","💛","💚","💙","💜"
]

Item{
width:parent.width
implicitHeight:root.popoutHeight - popoutColumn.headerHeight -
                               popoutColumn.detailsHeight - Theme.spacingXL

DankGridView{
anchors.fill:parent
cellWidth:50
cellHeight:50
model:popoutColumn.allEmojis

delegate:StyledRect{
width:45
height:45
radius:Theme.cornerRadius
color:emojiMouse.containsMouse ?
Theme.surfaceContainerHighest:
                               Theme.surfaceContainerHigh

StyledText{
anchors.centerIn:parent
text:modelData
font.pixelSize:Theme.fontSizeXLarge
}

MouseArea{
id:emojiMouse
anchors.fill:parent
hoverEnabled:true
cursorShape:Qt.PointingHandCursor

onClicked:{
                                Quickshell.execDetached(["sh","-c",
"echo -n '"+ modelData +"' | wl-copy"])
                                ToastService.showInfo("Copied "+ modelData)
                                popoutColumn.closePopout()
}
}
}
}
}
}
}

popoutWidth:400
popoutHeight:500
}
```

The `PopoutComponent` helper gives you consistent header/footer and a `closePopout()` function.

### Control Center Widget[​](#control-center-widget "Direct link to Control Center Widget")

Add a toggle to the Control Center:

```
PluginComponent{
id:root

propertyboolisEnabled:pluginData.isEnabled ||false
propertyintclickCount:pluginData.clickCount ||0

ccWidgetIcon:isEnabled ?"toggle_on":"toggle_off"
ccWidgetPrimaryText:"Example Toggle"
ccWidgetSecondaryText:isEnabled ?`Active • ${clickCount} clicks`:"Inactive"
ccWidgetIsActive:isEnabled

onCcWidgetToggled:{
        isEnabled =!isEnabled
        clickCount +=1
if(pluginService){
            pluginService.savePluginData(pluginId,"isEnabled", isEnabled)
            pluginService.savePluginData(pluginId,"clickCount", clickCount)
}
        ToastService.showInfo(isEnabled ?"Enabled":"Disabled")
}

horizontalBarPill:Component{
Row{
DankIcon{
name:root.isEnabled ?"toggle_on":"toggle_off"
color:root.isEnabled ? Theme.primary : Theme.surfaceVariantText
}
StyledText{
text:`${root.clickCount} clicks`
color:Theme.surfaceText
}
}
}

verticalBarPill:Component{
Column{
DankIcon{
name:root.isEnabled ?"toggle_on":"toggle_off"
color:root.isEnabled ? Theme.primary : Theme.surfaceVariantText
anchors.horizontalCenter:parent.horizontalCenter
}
StyledText{
text:`${root.clickCount}`
color:Theme.surfaceText
anchors.horizontalCenter:parent.horizontalCenter
}
}
}
}
```

Set `ccWidgetIcon`, `ccWidgetPrimaryText`, `ccWidgetSecondaryText`, and `ccWidgetIsActive`. Handle `onCcWidgetToggled` for toggle clicks.

## Daemon Plugins[​](#daemon-plugins "Direct link to Daemon Plugins")

Daemon plugins run in the background without UI. They monitor events, automate tasks, or provide services.

Here's a daemon that runs a script whenever the wallpaper changes:

```
import QtQuick
import Quickshell
import Quickshell.Io
import qs.Common
import qs.Services
import qs.Modules.Plugins

PluginComponent{
id:root

propertystringscriptPath:pluginData.scriptPath ||""

Connections{
target:SessionData
functiononWallpaperPathChanged(){
if(scriptPath && scriptPath !==""){
var process = scriptProcessComponent.createObject(root,{
wallpaperPath: SessionData.wallpaperPath
})
                process.running =true
}
}
}

Component{
id:scriptProcessComponent

Process{
propertystringwallpaperPath:""
command:[scriptPath, wallpaperPath]

stdout:SplitParser{
onRead:line=> console.log("Script:", line)
}

stderr:SplitParser{
onRead:line=>{
if(line.trim()){
                        ToastService.showError("Script error", line)
}
}
}

onExited:(exitCode)=>{
if(exitCode !==0){
                    ToastService.showError("Script failed","Exit code: "+ exitCode)
}
destroy()
}
}
}

Component.onCompleted:{
        console.info("Wallpaper watcher daemon started")
}
}
```

Daemon manifest uses `"type": "daemon"`:

```
{
"id":"wallpaperWatcher",
"type":"daemon",
"component":"./WallpaperWatcher.qml"
}
```

## Desktop Plugins[​](#desktop-plugins "Direct link to Desktop Plugins")

Desktop plugins render directly on the desktop background layer using Wayland's wlr-layer-shell protocol. Users can freely position and resize them.

### Basic Desktop Widget[​](#basic-desktop-widget "Direct link to Basic Desktop Widget")

```
import QtQuick
import Quickshell
import qs.Common
import qs.Modules.Plugins

DesktopPluginComponent{
id:root

// Size constraints
minWidth:150
minHeight:100

// Access saved settings via pluginData
propertystringdisplayText:pluginData.displayText ??"Hello"
propertyrealbgOpacity:(pluginData.backgroundOpacity ??80)/100

Rectangle{
anchors.fill:parent
radius:Theme.cornerRadius
color:Theme.withAlpha(Theme.surfaceContainer, root.bgOpacity)

Text{
anchors.centerIn:parent
text:root.displayText
color:Theme.surfaceText
font.pixelSize:Theme.fontSizeLarge
}
}
}
```

Desktop manifest uses `"type": "desktop"`:

```
{
"id":"myDesktopWidget",
"name":"My Desktop Widget",
"description":"A custom desktop widget",
"version":"1.0.0",
"author":"Your Name",
"type":"desktop",
"capabilities":["desktop-widget"],
"component":"./MyWidget.qml",
"icon":"widgets",
"settings":"./MySettings.qml",
"requires_dms":">=1.2.0",
"permissions":["settings_read","settings_write"]
}
```

### DesktopPluginComponent Properties[​](#desktopplugincomponent-properties "Direct link to DesktopPluginComponent Properties")

**Auto-injected** (don't declare these):

PropertyTypeDescription`pluginService`varReference to PluginService for data persistence`pluginId`stringYour plugin's unique identifier`widgetWidth`realCurrent widget width`widgetHeight`realCurrent widget height`pluginData`varObject containing all saved plugin settings

**Optional** (define on your component):

PropertyTypeDefaultDescription`minWidth`real100Minimum allowed width`minHeight`real100Minimum allowed height`defaultWidth`real200Initial width for new widgets`defaultHeight`real200Initial height for new widgets`forceSquare`boolfalseConstrain to square aspect ratio

**Helper functions:**

```
// Read a specific setting with default value
function getData(key, defaultValue)

// Write a setting (triggers pluginDataChanged signal)
function setData(key, value)
```

### User Interaction[​](#user-interaction "Direct link to User Interaction")

Desktop widgets support:

ActionTriggerDescriptionMoveRight-click + drag anywhereRepositions the widgetResizeRight-click + drag bottom-right cornerResizes within min/max bounds

### Responsive Layout[​](#responsive-layout "Direct link to Responsive Layout")

Adapt to widget dimensions:

```
GridLayout{
columns:{
if(root.widgetWidth <200)return1
if(root.widgetWidth <400)return2
return3
}
}
```

### Dynamic Size Constraints[​](#dynamic-size-constraints "Direct link to Dynamic Size Constraints")

```
DesktopPluginComponent{
id:root

propertyboolshowAllTiles:pluginData.showAllTiles ??true

minWidth:showAllTiles ?200:100
minHeight:{
if(tileCount ===0)return60
if(tileCount ===1)return80
return120+(tileCount -2)*40
}
}
```

### Time-Based Updates[​](#time-based-updates "Direct link to Time-Based Updates")

Use `SystemClock` for efficient time updates:

```
import Quickshell

DesktopPluginComponent{
id:root

SystemClock{
id:clock
precision:SystemClock.Seconds  // or Minutes

onDateChanged:updateDisplay()
}

functionupdateDisplay(){
// Update widget content
}
}
```

### Canvas/Graph Performance[​](#canvasgraph-performance "Direct link to Canvas/Graph Performance")

For graphing widgets:

```
Canvas{
id:graph
renderStrategy:Canvas.Cooperative

propertyvarhistory:[]

onHistoryChanged:requestPaint()

onPaint:{
var ctx =getContext("2d")
        ctx.reset()
// Draw graph...
}
}
```

### Complete Example: Desktop Clock[​](#complete-example-desktop-clock "Direct link to Complete Example: Desktop Clock")

A clock widget with analog and digital modes, demonstrating dynamic component loading and responsive sizing.

```
// DesktopClock.qml
import QtQuick
import Quickshell
import qs.Common
import qs.Modules.Plugins

DesktopPluginComponent{
id:root

minWidth:120
minHeight:120

propertyboolshowSeconds:pluginData.showSeconds ??true
propertyboolshowDate:pluginData.showDate ??true
propertystringclockStyle:pluginData.clockStyle ??"analog"
propertyrealbackgroundOpacity:(pluginData.backgroundOpacity ??50)/100

SystemClock{
id:systemClock
precision:root.showSeconds ? SystemClock.Seconds : SystemClock.Minutes
}

Rectangle{
id:background
anchors.fill:parent
radius:Theme.cornerRadius
color:Theme.surfaceContainer
opacity:root.backgroundOpacity
}

Loader{
anchors.fill:parent
anchors.margins:Theme.spacingM
sourceComponent:root.clockStyle ==="digital"? digitalClock : analogClock
}

Component{
id:analogClock

Item{
id:analogClockRoot

propertyrealclockSize:Math.min(width, height)-(root.showDate ?30:0)

Item{
id:clockFace
width:analogClockRoot.clockSize
height:analogClockRoot.clockSize
anchors.horizontalCenter:parent.horizontalCenter
anchors.top:parent.top
anchors.topMargin:Theme.spacingS

// Hour markers
Repeater{
model:12

Rectangle{
                        required property int index
propertyrealmarkAngle:index *30
propertyrealmarkRadius:clockFace.width /2-8

x:clockFace.width /2+ markRadius * Math.sin(markAngle * Math.PI/180)- width /2
y:clockFace.height /2- markRadius * Math.cos(markAngle * Math.PI/180)- height /2
width:index %3===0?8:4
height:width
radius:width /2
color:index %3===0? Theme.primary : Theme.outlineVariant
}
}

// Hour hand
Rectangle{
id:hourHand
propertyinthours:systemClock.date?.getHours()%12??0
propertyintminutes:systemClock.date?.getMinutes()??0

x:clockFace.width /2- width /2
y:clockFace.height /2- height +4
width:6
height:clockFace.height *0.25
radius:3
color:Theme.primary
antialiasing:true
transformOrigin:Item.Bottom
rotation:(hours + minutes /60)*30
}

// Minute hand
Rectangle{
id:minuteHand
propertyintminutes:systemClock.date?.getMinutes()??0
propertyintseconds:systemClock.date?.getSeconds()??0

x:clockFace.width /2- width /2
y:clockFace.height /2- height +4
width:4
height:clockFace.height *0.35
radius:2
color:Theme.onSurface
antialiasing:true
transformOrigin:Item.Bottom
rotation:(minutes + seconds /60)*6
}

// Second hand
Rectangle{
id:secondHand
visible:root.showSeconds
propertyintseconds:systemClock.date?.getSeconds()??0

x:clockFace.width /2- width /2
y:clockFace.height /2- height +4
width:2
height:clockFace.height *0.4
radius:1
color:Theme.error
antialiasing:true
transformOrigin:Item.Bottom
rotation:seconds *6
}

// Center dot
Rectangle{
anchors.centerIn:parent
width:10
height:10
radius:5
color:Theme.primary
}
}

Text{
visible:root.showDate
anchors.horizontalCenter:parent.horizontalCenter
anchors.bottom:parent.bottom
anchors.bottomMargin:Theme.spacingXS
text:systemClock.date?.toLocaleDateString(Qt.locale(),"ddd, MMM d")??""
font.pixelSize:Theme.fontSizeSmall
font.weight:Font.Medium
color:Theme.surfaceText
}
}
}

Component{
id:digitalClock

Item{
id:digitalRoot

propertyrealtimeFontSize:Math.min(width *0.16, height *(root.showDate ?0.4:0.5))
propertyrealdateFontSize:Math.max(Theme.fontSizeSmall, timeFontSize *0.35)

Text{
id:timeText
anchors.horizontalCenter:parent.horizontalCenter
anchors.verticalCenter:parent.verticalCenter
anchors.verticalCenterOffset:root.showDate ?-digitalRoot.dateFontSize *0.8:0
text:systemClock.date?.toLocaleTimeString(Qt.locale(), root.showSeconds ?"hh:mm:ss":"hh:mm")??""
font.pixelSize:digitalRoot.timeFontSize
font.weight:Font.Bold
font.family:"monospace"
color:Theme.primary
}

Text{
id:dateText
visible:root.showDate
anchors.horizontalCenter:parent.horizontalCenter
anchors.top:timeText.bottom
anchors.topMargin:Theme.spacingXS
text:systemClock.date?.toLocaleDateString(Qt.locale(),"ddd, MMM d")??""
font.pixelSize:digitalRoot.dateFontSize
color:Theme.surfaceText
}
}
}
}
```

```
// DesktopClockSettings.qml
import QtQuick
import qs.Common
import qs.Modules.Plugins

PluginSettings{
id:root
pluginId:"exampleDesktopClock"

SelectionSetting{
settingKey:"clockStyle"
label:I18n.tr("Clock Style")
options:[
{label:I18n.tr("Analog"),value:"analog"},
{label:I18n.tr("Digital"),value:"digital"}
]
defaultValue:"analog"
}

ToggleSetting{
settingKey:"showSeconds"
label:I18n.tr("Show Seconds")
defaultValue:true
}

ToggleSetting{
settingKey:"showDate"
label:I18n.tr("Show Date")
defaultValue:true
}

SliderSetting{
settingKey:"backgroundOpacity"
label:I18n.tr("Background Opacity")
defaultValue:50
minimum:0
maximum:100
unit:"%"
}
}
```

### Desktop Plugin Best Practices[​](#desktop-plugin-best-practices "Direct link to Desktop Plugin Best Practices")

1. **Use Theme singleton** - Never hardcode colors, spacing, or font sizes
2. **Set appropriate minWidth/minHeight** - Prevent unusable widget sizes
3. **Handle null data** - Use `??` operator for all `pluginData` access
4. **Optimize Canvas redraws** - Use `renderStrategy: Canvas.Cooperative`
5. **Responsive layouts** - Adapt to widget dimensions dynamically
6. **Transparency** - Provide opacity controls so wallpaper shows through

## Launcher Plugins[​](#launcher-plugins "Direct link to Launcher Plugins")

Launcher plugins add items to Spotlight search. They use `QtObject` as their root (not `Item` or `PluginComponent`) since they don't render any UI directly.

### Required Interface[​](#required-interface "Direct link to Required Interface")

Your launcher plugin must provide:

Property/FunctionDescription`pluginService`Auto-injected service for data persistence`trigger`Prefix that activates your plugin (e.g., `"="` or `"#"`)`itemsChanged`Signal to emit when your items list updates`getItems(query)`Returns filtered items matching the query`executeItem(item)`Handles item selection`getContextMenuActions(item)`*(Optional)* Returns context menu actions for an item

Add right-click context menus to your launcher items by implementing `getContextMenuActions(item)`:

```
function getContextMenuActions(item) {
    if (!item)
        return [];

    return [
{
icon:"content_copy",
text:I18n.tr("Copy"),
action:()=>{
                Quickshell.execDetached(["sh","-c","echo -n '"+ item.name +"' | wl-copy"]);
                ToastService.showInfo("Copied", item.name);
}
},
{
icon:"open_in_new",
text:I18n.tr("Open"),
action:()=>executeItem(item)
}
];
}
```

Each action object has:

- `icon` - Material icon name
- `text` - Menu item label
- `action` - Callback function to execute

Here's a more complete example with dynamic actions based on item state:

```
functiongetContextMenuActions(item){
if(!item ||!item._id)
return[];

const pinned =isPinned(item._id);
return[
{
icon: pinned ?"keep_off":"push_pin",
text: pinned ? I18n.tr("Unpin"): I18n.tr("Pin"),
action:()=>togglePin(item._id)
},
{
icon:"content_copy",
text: I18n.tr("Copy"),
action:()=>executeItem(item)
}
];
}
```

### Example: Calculator Plugin[​](#example-calculator-plugin "Direct link to Example: Calculator Plugin")

A complete launcher plugin that evaluates math expressions:

```
import QtQuick
import Quickshell
import qs.Services
import"calculator.js"as Calculator

QtObject{
id:root

propertyvarpluginService:null
propertystringtrigger:""

    signal itemsChanged

Component.onCompleted:{
if(!pluginService)
return;
        trigger = pluginService.loadPluginData("calculator","trigger","=");
}

functiongetItems(query){
if(!query || query.trim().length ===0)
return[];

const trimmedQuery = query.trim();
if(!Calculator.isMathExpression(trimmedQuery))
return[];

const result = Calculator.evaluate(trimmedQuery);
if(!result.success)
return[];

return[{
name: result.result.toString(),
icon:"material:equal",
comment: trimmedQuery +" = "+ result.result,
action:"copy:"+ result.result,
categories:["Calculator"],
keywords:["math","calculate","equals"]
}];
}

functionexecuteItem(item){
if(!item?.action)
return;

const actionParts = item.action.split(":");
const actionType = actionParts[0];
const actionData = actionParts.slice(1).join(":");

if(actionType ==="copy"){
            Quickshell.execDetached(["sh","-c","echo -n '"+ actionData +"' | wl-copy"]);
            ToastService.showInfo("Calculator","Copied to clipboard: "+ actionData);
}
}

onTriggerChanged:{
if(pluginService)
            pluginService.savePluginData("calculator","trigger", trigger);
}
}
```

### Launcher Settings[​](#launcher-settings "Direct link to Launcher Settings")

Launcher plugins use `PluginSettings` just like widget plugins:

```
import QtQuick
import qs.Common
import qs.Widgets
import qs.Modules.Plugins

PluginSettings{
id:root
pluginId:"calculator"

StyledText{
width:parent.width
text:"Calculator Plugin"
font.pixelSize:Theme.fontSizeLarge
font.weight:Font.Bold
color:Theme.surfaceText
}

StyledText{
width:parent.width
text:"Evaluates math expressions and copies results to clipboard."
font.pixelSize:Theme.fontSizeSmall
color:Theme.surfaceVariantText
wrapMode:Text.WordWrap
}

ToggleSetting{
id:noTriggerToggle
settingKey:"noTrigger"
label:"Always Active"
description:value ?"Type expressions directly":"Use trigger prefix"
defaultValue:false
onValueChanged:{
if(value)
                root.saveValue("trigger","");
else
                root.saveValue("trigger", triggerSetting.value ||"=");
}
}

StringSetting{
id:triggerSetting
visible:!noTriggerToggle.value
settingKey:"trigger"
label:"Trigger"
description:"Prefix to activate calculator (e.g., =, calc)"
placeholder:"="
defaultValue:"="
}
}
```

Launcher manifest needs `"type": "launcher"` and a `"trigger"`:

```
{
"id":"emojiLauncher",
"type":"launcher",
"trigger":"#",
"component":"./EmojiLauncher.qml"
}
```

**Item properties**:

- `name` - Display name (required)
- `icon` - Icon to show (see formats below)
- `comment` - Secondary text/description
- `action` - What happens on selection (see formats below)
- `categories` - Array of category strings
- `keywords` - Array of strings for search matching (e.g., `["math", "calculate"]`)

**Icon formats**:

- Material Design: `"material:icon_name"` or just `"icon_name"`
- Unicode/Emoji: `"unicode:🚀"`

**Action formats**:

- Copy to clipboard: `"copy:text"`
- Show toast: `"toast:message"`
- Run script: `"script:command args"`

## Plugin Settings[​](#plugin-settings "Direct link to Plugin Settings")

Use `PluginSettings` as the base and drop in setting components. They handle all the loading and saving automatically.

```
import QtQuick
import qs.Common
import qs.Modules.Plugins
import qs.Widgets

PluginSettings{
id:root
pluginId:"colorDemo"

StyledText{
width:parent.width
text:"Color Demo Settings"
font.pixelSize:Theme.fontSizeLarge
font.weight:Font.Bold
color:Theme.surfaceText
}

StyledText{
width:parent.width
text:"Pick colors for your widget"
font.pixelSize:Theme.fontSizeSmall
color:Theme.surfaceVariantText
wrapMode:Text.WordWrap
}

ColorSetting{
settingKey:"customColor"
label:"Widget Color"
description:"Color shown in the bar"
defaultValue:Theme.primary
}

SliderSetting{
settingKey:"updateInterval"
label:"Update Speed"
description:"How often to refresh"
defaultValue:60
minimum:10
maximum:300
unit:"sec"
}

ToggleSetting{
settingKey:"showInBar"
label:"Show in Bar"
description:"Display widget in DankBar"
defaultValue:true
}

StringSetting{
settingKey:"apiKey"
label:"API Key"
description:"Your service API key"
placeholder:"Enter key"
defaultValue:""
}

SelectionSetting{
settingKey:"theme"
label:"Theme"
description:"Widget appearance"
options:[
{label:"Light",value:"light"},
{label:"Dark",value:"dark"},
{label:"Auto",value:"auto"}
]
defaultValue:"dark"
}
}
```

The setting components available:

- `ColorSetting` - Opens color picker modal
- `SliderSetting` - Numeric slider
- `ToggleSetting` - Boolean switch
- `StringSetting` - Text input
- `SelectionSetting` - Dropdown menu

Access settings in your widget via `pluginData`:

```
propertycolorcustomColor:pluginData.customColor || Theme.primary
propertyintupdateInterval:pluginData.updateInterval ||60
propertyboolshowInBar:pluginData.showInBar !==undefined? pluginData.showInBar :true
propertystringapiKey:pluginData.apiKey ||""
propertystringtheme:pluginData.theme ||"dark"
```

## Common Patterns[​](#common-patterns "Direct link to Common Patterns")

### Auto-injected Properties[​](#auto-injected-properties "Direct link to Auto-injected Properties")

`PluginComponent` automatically provides these properties - don't declare them yourself:

- `pluginData` - Reactive settings object
- `pluginService` - Service for manual data operations
- `pluginId` - Your plugin's ID
- `axis` - Bar axis info
- `section` - "left", "center", or "right"
- `parentScreen` - Screen reference
- `widgetThickness` - Widget height/width
- `barThickness` - Bar height/width
- `iconSize` - Recommended icon size for the current bar context
- `variants` - Variant instances

Use `iconSize` for consistent icon sizing that adapts to bar orientation and user preferences:

```
DankIcon{
name:"settings"
size:root.iconSize
}
```

### Saving Data Manually[​](#saving-data-manually "Direct link to Saving Data Manually")

Most of the time `pluginData` handles everything, but if you need to save manually:

```
if (pluginService) {
    pluginService.savePluginData(pluginId,"key", value)
}
```

### Showing Notifications[​](#showing-notifications "Direct link to Showing Notifications")

```
ToastService.showInfo("Title","Message")
ToastService.showError("Title","Error message")
```

### Copying to Clipboard[​](#copying-to-clipboard "Direct link to Copying to Clipboard")

```
Quickshell.execDetached(["sh","-c","echo -n 'text' | wl-copy"])
```

### Timers[​](#timers "Direct link to Timers")

```
PluginComponent{
Timer{
interval:1000
running:true
repeat:true
onTriggered:{
// Do something every second
}
}
}
```

## Plugin Manifest Reference[​](#plugin-manifest-reference "Direct link to Plugin Manifest Reference")

### Required Fields[​](#required-fields "Direct link to Required Fields")

```
{
"id":"pluginId",
"name":"Plugin Name",
"description":"What it does",
"version":"1.0.0",
"author":"Your Name",
"type":"widget",
"component":"./Widget.qml"
}
```

### Optional Fields[​](#optional-fields "Direct link to Optional Fields")

```
{
"icon":"material_icon",
"settings":"./Settings.qml",
"trigger":"#",
"permissions":["settings_read","settings_write"],
"requires_dms":">=0.1.18",
"requires":["tool1","tool2"]
}
```

### Plugin Types[​](#plugin-types "Direct link to Plugin Types")

- `"widget"` - DankBar or Control Center widget
- `"daemon"` - Background service
- `"launcher"` - Spotlight extension
- `"desktop"` - Desktop layer widget

### Permissions[​](#permissions "Direct link to Permissions")

- `"settings_read"` - Read plugin settings
- `"settings_write"` - Write plugin settings
- `"process"` - Execute system commands
- `"network"` - Network access

## Testing[​](#testing "Direct link to Testing")

1. Enable plugin: Settings → Plugins → Scan → Toggle on
2. Add to bar: Settings → DankBar → Add widget
3. Check console: Look for errors in shell output
4. Hot-reload your plugin: `dms ipc call plugins reload myPlugin`
5. Check settings file: `~/.config/DankMaterialShell/settings.json`

### Hot Reloading[​](#hot-reloading "Direct link to Hot Reloading")

During development you can reload plugins without restarting the shell:

```
# Reload your plugin after making changes
dms ipc call plugins reload myPlugin

# Check if it's running
dms ipc call plugins status myPlugin

# List all plugins and their state
dms ipc call plugins list
```

This is way faster than `dms restart` when you're iterating on your code.

## Publishing[​](#publishing "Direct link to Publishing")

1. Create GitHub repo
2. Include `plugin.json`, README, screenshots
3. Tag releases: `git tag v1.0.0 && git push --tags`
4. Submit to registry: [dms-plugin-registry](https://github.com/AvengeMedia/dms-plugin-registry)

## Examples[​](#examples "Direct link to Examples")

Check the `PLUGINS/` directory in the DMS repo for real examples:

- **ColorDemoPlugin** - Color picker integration
- **ExampleEmojiPlugin** - Popout with grid view
- **ControlCenterExample** - Control Center toggle
- **LauncherExample** - Spotlight extension
- **WallpaperWatcherDaemon** - Background event watcher

**Built-in desktop widgets**

- **DesktopClockWidget** - Digital/analog clock with date display and style options
- **SystemMonitorWidget** - CPU, memory, network, disk, GPU tiles with real-time graphs

Clone them and experiment.