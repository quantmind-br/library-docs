---
title: Configuration | Dank Linux
url: https://danklinux.com/docs/dgop/configuration
source: sitemap
fetched_at: 2026-04-26T08:39:35.456384091-03:00
rendered_js: false
word_count: 69
summary: This document provides configuration details for the dgop application, including API environment variables, custom color scheme definitions, and basic troubleshooting steps.
tags:
    - dgop
    - api-configuration
    - color-theme
    - json-schema
    - troubleshooting
category: configuration
optimized: true
optimized_at: 2026-04-26T00:00:00Z
---

```
██████╗  ██████╗  ██████╗ ██████╗
██╔══██╗██╔════╝ ██╔═══██╗██╔══██╗
██║  ██║██║  ███╗██║   ██║██████╔╝
██║  ██║██║   ██║██║   ██║██╔═══╝
██████╔╝╚██████╔╝╚██████╔╝██║
╚═════╝  ╚═════╝  ╚═════╝ ╚═╝

```

## API

Set the following environment variable to override the default HTTP server port (`63484`):

- `API_PORT`

## Colors

dgop reads colors from `~/.config/dgop/colors.json`.

```json
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

### matugen template

Template for use with matugen:

```json
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

## Troubleshooting

**API not starting:**

- Check port availability: `netstat -tlnp | grep :63484`
- Check logs

## Next Steps

- [[030-docs-dgop-usage|Usage]] — CLI commands and API usage
