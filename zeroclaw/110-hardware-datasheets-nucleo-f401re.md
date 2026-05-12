---
title: Nucleo f401re
title_vi: Nucleo-F401RE GPIO
url: https://github.com/openagen/zeroclaw/blob/master/docs/hardware/datasheets/nucleo-f401re.md
source: git
fetched_at: 2026-05-02T14:50:53.734706274-03:00
rendered_js: false
word_count: 50
summary: This document provides the pin mapping and GPIO configuration details for the built-in user LED on the Nucleo-F401RE development board.
optimized: true
optimized_at: 2026-05-05T00:00:00Z
tags:
  - nucleo-f401re
  - gpio-mapping
  - pin-aliases
  - stm32
  - microcontroller
  - hardware-configuration
category: reference
---
# Nucleo-F401RE GPIO

## Pin Aliases

| Alias | Pin |
|-------|-----|
| `red_led` | 13 |
| `user_led` | 13 |
| `ld2` | 13 |
| `builtin_led` | 13 |

## GPIO

**Chân 13:** User LED (LD2)
- Output, active high
- PA5 trên STM32F401

#nucleo-f401re #gpio #stm32