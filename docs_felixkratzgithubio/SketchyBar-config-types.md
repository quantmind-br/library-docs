---
title: Type Nomenclature | SketchyBar
url: https://felixkratz.github.io/SketchyBar/config/types
source: github_pages
fetched_at: 2026-02-15T21:17:30.62446-03:00
rendered_js: false
word_count: 134
summary: This document defines the data types and value nomenclature used for configuration, providing details on boolean operations and ARGB hex color manipulations.
tags:
    - type-system
    - configuration-syntax
    - data-types
    - boolean-logic
    - color-formatting
    - sketchybar
category: reference
---

## Type nomenclature[​](#type-nomenclature "Direct link to heading")

`type``values``<boolean>``on`, `off`, `yes`, `no`, `true`, `false`, `1`, `0`, `toggle``<argb_hex>`Color as an 8 digit hex with alpha, red, green and blue channels`<path>`An absolute file path`<string>`Any UTF-8 string or symbol`<float>`A floating point number`<integer>`An integer`<positive_integer>`A positive integer`<positive_integer list>`A comma separated list of positive integers

### Further `<boolean>` operations[​](#further-boolean-operations "Direct link to heading")

All `<boolean>` properties can be negated with an exclamation mark, e.g. `!on`.

### Further `<argb_hex>` operations[​](#further-argb_hex-operations "Direct link to heading")

All colors (i.e. all fields where the value type is `<argb_hex>`) can additionally be accessed to change specific channels like this:

&lt;color\_property&gt;&lt;value&gt;defaultdescription`alpha``<float>``1.0`The alpha channel of the color (0 to 1)`red``<float>``1.0`The red channel of the color (0 to 1)`green``<float>``1.0`The green channel of the color (0 to 1)`blue``<float>``1.0`The blue channel of the color (0 to 1)

So for example, if I want to only change the alpha channel of the bars color I would use

```
sketchybar --bar color.alpha=0.5
```