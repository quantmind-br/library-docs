---
title: Querying Information | SketchyBar
url: https://felixkratz.github.io/SketchyBar/config/querying
source: github_pages
fetched_at: 2026-02-15T21:17:23.564668-03:00
rendered_js: false
word_count: 97
summary: This document explains how to retrieve configuration and state information from SketchyBar using various query commands that return JSON-formatted data. It covers querying the bar, specific items, defaults, events, and display configurations.
tags:
    - sketchybar
    - macos-customization
    - command-line-interface
    - json-output
    - querying
category: reference
---

## Querying[​](#querying "Direct link to heading")

*SketchyBar* can be queried for information about a number of things.

### Bar Properties[​](#bar-properties "Direct link to heading")

Information about the bar can be queried via:

The output is a JSON structure containing relevant information about the configuration settings of the bar.

### Item Properties[​](#item-properties "Direct link to heading")

Information about an item can be queried via:

```
sketchybar --query <name>
```

The output is a JSON structure containing relevant information about the configuration of the item.

### Default Properties[​](#default-properties "Direct link to heading")

Information about the current defaults.

```
sketchybar --query defaults
```

### Event Properties[​](#event-properties "Direct link to heading")

Information about the events.

```
sketchybar --query events
```

The names of the menu bar items in the default macOS bar:

```
sketchybar --query default_menu_items
```

### Display Configuration Information[​](#display-configuration-information "Direct link to heading")

Information about the current display configuration:

```
sketchybar --query displays
```