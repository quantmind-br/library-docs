---
title: YASB Reborn - Yet Another Status Bar
url: https://docs.yasb.dev/latest/widgets/glazewm-tiling-direction
source: crawler
fetched_at: 2026-02-23T05:18:00.481801-03:00
rendered_js: false
word_count: 131
---

Option Type Default Description `horizontal_label` string `'\udb81\udce1'` The label used for horizontal tiling direction. `vertical_label` string `'\udb81\udce2'` Optional label for populated workspaces. `glazewm_server_uri` string `'ws://localhost:6123'` Optional GlazeWM server uri. `container_shadow` dict `None` Container shadow options. `btn_shadow` dict `None` Workspace button shadow options

## Example Configuration

```
glazewm_tiling_direction:
type:"glazewm.tiling_direction.GlazewmTilingDirectionWidget"
options:
horizontal_label:"\udb81\udce1"
vertical_label:"\udb81\udce2"
btn_shadow:
enabled:true
color:"black"
radius:3
offset:[1,1]
```

## Description of Options

- **horizontal\_label:** Label used for horizontal tiling direction.
- **vertical\_label:** Label for vertical tiling direction.
- **glazewm\_server\_uri:** Optional GlazeWM server uri if it ever changes on GlazeWM side.
- **container\_shadow:** Container shadow options.
- **btn\_shadow:** Workspace button shadow options.

## Note on Shadows

`container_shadow` is applied to the container if it's not transparent. If it is transparent, container shadows will be applied to the `btn` instead. This can cause double shadows if you have `btn_shadow` already. Apply the shadows only to the container that is actually visible.

## Style

```
.glazewm-tiling-direction{}/*Style for widget.*/
.glazewm-tiling-direction.btn{}/*Style for tiling direction button.*/
```

## Example CSS

```
.glazewm-tiling-direction{
background-color:transparent;
padding:0;
margin:0;
}

.glazewm-tiling-direction.btn{
font-size:18px;
width:14px;
padding:04px04px;
color:#CDD6F4;
border:none;
}

.glazewm-tiling-direction.btn:hover{
background-color:#727272;
}
```