---
optimized: true
optimized_at: 2026-05-05T00:00:00Z
title: Nucleo f401re
url: https://github.com/openagen/zeroclaw/blob/master/docs/vi/datasheets/nucleo-f401re.md
source: git
fetched_at: 2026-05-02T14:52:35.576298336-03:00
rendered_js: false
word_count: 47
summary: This document provides a reference mapping for GPIO pin aliases and specifications for the Nucleo-F401RE development board, specifically identifying the User LED configuration.
tags:
    - gpio
    - nucleo-f401re
    - pin-mapping
    - embedded-systems
    - stm32
    - hardware-reference
category: reference
---
# GPIO Nucleo-F401RE

## Pin Aliases

| alias | pin |
|-------|-----|
| red_led | 13 |
| user_led | 13 |
| ld2 | 13 |
| builtin_led | 13 |

## GPIO

Pin 13: User LED (LD2)
- Output, active high
- PA5 on STM32F401
