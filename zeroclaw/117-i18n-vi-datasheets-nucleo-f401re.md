---
title: Nucleo f401re
url: https://github.com/openagen/zeroclaw/blob/master/docs/i18n/vi/datasheets/nucleo-f401re.md
source: git
fetched_at: 2026-05-02T14:51:13.640302323-03:00
rendered_js: false
word_count: 51
summary: This document defines the GPIO pin mappings and aliases for the Nucleo-F401RE development board, specifically identifying the configuration for the built-in user LED.
tags:
    - gpio
    - nucleo-f401re
    - pin-mapping
    - hardware-configuration
    - stm32f401
    - led-control
category: reference
optimized: true
optimized_at: 2026-05-05T12:00:00Z
---

# GPIO Nucleo-F401RE

> [!note]
> Tham chiếu nhanh cấu hình pin GPIO cho Nucleo-F401RE

---

## 1. Pin Aliases

| Alias | Pin |
|---|---|
| `red_led` | 13 |
| `user_led` | 13 |
| `ld2` | 13 |
| `builtin_led` | 13 |

---

## 2. Thông tin GPIO

| Đặc điểm | Chi tiết |
|---|---|
| **Pin 13** | User LED (LD2) |
| **Loại** | Output (mức cao tích cực) |
| **Chân STM32** | PA5 trên STM32F401 |

#gpio #nucleo-f401re #pin-mapping #hardware-configuration #stm32f401 #led-control #vietnamese-docs