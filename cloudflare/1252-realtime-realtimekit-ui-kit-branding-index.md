---
title: Customise Branding · Cloudflare Realtime docs
url: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/branding/index.md
source: llms
fetched_at: 2026-01-24T15:37:01.292365154-03:00
rendered_js: false
word_count: 250
summary: This document explains how to customize and replace default UI icons within the RealtimeKit UI Kit by providing custom icon packs and SVG strings.
tags:
    - realtimekit
    - ui-kit
    - icon-customization
    - svg-icons
    - web-sdk
    - frontend-development
category: guide
---

RealtimeKit's UI Kit provides all the necessary UI components to allow complete customization of all its UI Kit components. You can customize your meeting icons such as chat, clock, leave meeting, mic on and off, and more.

## Prerequisites

To get started with customizing the icons for your meetings, you need to first integrate RealtimeKit's Web SDK into your web application.

## Customize the default icon pack

RealtimeKit's default icon set is available at [icons.dyte.io](https://icons.dyte.io/). You can modify and generate your custom icon set from there.

To replace RealtimeKit's default icon set with your own, pass the link to your icon set in the UI component.

## IconPack reference

The IconPack is an object where:

* **Object key** - Denotes the name of the icon
* **Object value** - Stores the SVG string

### Available icons

The default icon pack includes the following icons:

* `attach`
* `call_end`
* `chat`
* `checkmark`
* `chevron_down`
* `chevron_left`
* `chevron_right`
* `chevron_up`
* `clock`
* `copy`
* `disconnected`
* `dismiss`
* `download`
* `emoji_multiple`
* `full_screen_maximize`
* `full_screen_minimize`
* `image`
* `image_off`
* `join_stage`
* `leave_stage`
* `mic_off`
* `mic_on`
* `more_vertical`
* `participants`
* `people`
* `pin`
* `pin_off`
* `poll`
* `recording`
* `rocket`
* `search`
* `send`
* `settings`
* `share`
* `share_screen_person`
* `share_screen_start`
* `share_screen_stop`
* `speaker`
* `spinner`
* `spotlight`
* `stop_recording`
* `subtract`
* `vertical_scroll`
* `vertical_scroll_disabled`
* `video_off`
* `video_on`
* `wand`
* `warning`
* `wifi`

Each icon in your custom icon pack JSON file should be defined as a key-value pair where the key matches one of the icon names above, and the value is the SVG string for that icon.

## Next steps

Explore additional customization options:

* [Render Default Meeting UI](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/) - Complete meeting experience out of the box
* [Build Your Own UI](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/build-your-own-ui/) - Create custom meeting interfaces