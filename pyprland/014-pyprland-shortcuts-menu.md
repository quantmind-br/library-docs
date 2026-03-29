---
title: shortcuts_menu | Pyprland web
url: https://hyprland-community.github.io/pyprland/shortcuts/menu
source: github_pages
fetched_at: 2026-01-31T16:01:01.414573276-03:00
rendered_js: true
word_count: 130
summary: This document provides detailed configuration options for customizing menu behavior and appearance, including entry structures, separators, and display formatting.
tags:
    - menu-configuration
    - command-interface
    - user-interface
    - display-settings
    - configuration-options
category: reference
---

- `menu[name]`Shows the menu, if "name" is provided, will only show this sub-menu.

Basic (1)

OptionDescription[`entries`i](#config-entries "More details below")dictrequiredMenu entries structure (nested dict of commands)

Behavior (1)

OptionDescription[`skip_single`i](#config-skip-single "More details below")bool

=`true`

Auto-select when only one option available

Appearance (5)

OptionDescription`separator`str

=`" | "`

Separator for menu display[`command_start`i](#config-command-start "More details below")strPrefix for command entries[`command_end`i](#config-command-start "More details below")strSuffix for command entries[`submenu_start`i](#config-submenu-start "More details below")strPrefix for submenu entries[`submenu_end`i](#config-submenu-start "More details below")str

=`"➜"`

Suffix for submenu entries

Menu (2)

OptionDescription`engine`strMenu engine to use`parameters`strExtra parameters for the menu engine command

### `entries` dictrequired [​](#config-entries)

### `command_start` / `command_end` str [​](#config-command-start)

Allow adding some text (eg: icon) before / after a menu entry for final commands.

### `submenu_start` / `submenu_end` str [​](#config-submenu-start)

Allow adding some text (eg: icon) before / after a menu entry leading to another menu.

By default `submenu_end` is set to a right arrow sign, while other attributes are not set.

### `skip_single` bool=`true` [​](#config-skip-single)