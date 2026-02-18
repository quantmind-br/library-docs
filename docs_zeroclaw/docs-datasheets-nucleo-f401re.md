---
title: Nucleo f401re
url: https://github.com/zeroclaw-labs/zeroclaw/blob/main/docs/datasheets/nucleo-f401re.md
source: git
fetched_at: 2026-02-18T07:18:23.190688-03:00
rendered_js: false
word_count: 47
summary: This document provides technical details for the Nucleo-F401RE GPIO pins, including pin aliases and hardware configuration for the onboard user LED.
tags:
    - nucleo-f401re
    - gpio-mapping
    - stm32f401
    - pin-aliases
    - embedded-systems
category: reference
---

# Nucleo-F401RE GPIO

## Pin Aliases

| alias       | pin |
|-------------|-----|
| red_led     | 13  |
| user_led    | 13  |
| ld2         | 13  |
| builtin_led | 13  |

## GPIO

Pin 13: User LED (LD2)
- Output, active high
- PA5 on STM32F401
