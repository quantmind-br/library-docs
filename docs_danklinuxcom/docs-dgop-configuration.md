---
title: Configuration | Dank Linux
url: https://danklinux.com/docs/dgop/configuration
source: sitemap
fetched_at: 2026-01-24T13:36:17.71497224-03:00
rendered_js: false
word_count: 18
summary: This document details the JSON configuration structure used for customizing the visual themes of UI components, charts, and status indicators.
tags:
    - ui-configuration
    - theme-settings
    - color-mapping
    - visual-customization
    - json-format
category: configuration
---

For the API, you can set the following environment variable to override the port of the http server:

```
{
"ui":{
"border_primary":"#ccbeff",
"border_secondary":"#cac3dc",
"header_background":"#ccbeff",
"header_text":"#33275e",
"footer_background":"#141318",
"footer_text":"#cac4cf",
"text_primary":"#e6e1e9",
"text_secondary":"#cac4cf",
"text_accent":"#ccbeff",
"selection_background":"#ccbeff",
"selection_text":"#33275e"
},
"charts":{
"network_download":"#ccbeff",
"network_upload":"#4a3e76",
"network_line":"#cac3dc",
"cpu_core_low":"#4a3e76",
"cpu_core_medium":"#ccbeff",
"cpu_core_high":"#eeb8ca",
"disk_read":"#ccbeff",
"disk_write":"#4a3e76"
},
"progress_bars":{
"memory_low":"#4a3e76",
"memory_medium":"#ccbeff",
"memory_high":"#eeb8ca",
"disk_low":"#4a3e76",
"disk_medium":"#ccbeff",
"disk_high":"#eeb8ca",
"cpu_low":"#4a3e76",
"cpu_medium":"#ccbeff",
"cpu_high":"#eeb8ca",
"progress_background":"#201f24"
},
"temperature":{
"cold":"#4a3e76",
"warm":"#ccbeff",
"hot":"#eeb8ca",
"danger":"#ffb4ab"
},
"status":{
"success":"#22C55E",
"warning":"#F59E0B",
"error":"#ffb4ab",
"info":"#ccbeff"
}
}
```

```
{
"ui":{
"border_primary":"{{colors.primary.default.hex}}",
"border_secondary":"{{colors.secondary.default.hex}}",
"header_background":"{{colors.primary.default.hex}}",
"header_text":"{{colors.on_primary.default.hex}}",
"footer_background":"{{colors.surface_container.default.hex}}",
"footer_text":"{{colors.on_surface_variant.default.hex}}",
"text_primary":"{{colors.on_surface.default.hex}}",
"text_secondary":"{{colors.on_surface_variant.default.hex}}",
"text_accent":"{{colors.primary.default.hex}}",
"selection_background":"{{colors.primary.default.hex}}",
"selection_text":"{{colors.on_primary.default.hex}}"
},
"charts":{
"network_download":"{{colors.primary.default.hex}}",
"network_upload":"{{colors.primary_container.default.hex}}",
"network_line":"{{colors.secondary.default.hex}}",
"cpu_core_low":"{{colors.primary_container.default.hex}}",
"cpu_core_medium":"{{colors.primary.default.hex}}",
"cpu_core_high":"{{colors.tertiary.default.hex}}",
"disk_read":"{{colors.primary.default.hex}}",
"disk_write":"{{colors.primary_container.default.hex}}"
},
"progress_bars":{
"memory_low":"{{colors.primary_container.default.hex}}",
"memory_medium":"{{colors.primary.default.hex}}",
"memory_high":"{{colors.tertiary.default.hex}}",
"disk_low":"{{colors.primary_container.default.hex}}",
"disk_medium":"{{colors.primary.default.hex}}",
"disk_high":"{{colors.tertiary.default.hex}}",
"cpu_low":"{{colors.primary_container.default.hex}}",
"cpu_medium":"{{colors.primary.default.hex}}",
"cpu_high":"{{colors.tertiary.default.hex}}",
"progress_background":"{{colors.surface_container_high.default.hex}}"
},
"temperature":{
"cold":"{{colors.primary_container.default.hex}}",
"warm":"{{colors.primary.default.hex}}",
"hot":"{{colors.tertiary.default.hex}}",
"danger":"{{colors.error.default.hex}}"
},
"status":{
"success":"#22C55E",
"warning":"#F59E0B",
"error":"{{colors.error.default.hex}}",
"info":"{{colors.primary.default.hex}}"
}
}
```