---
title: Esp32
url: https://github.com/openagen/zeroclaw/blob/master/docs/hardware/datasheets/esp32.md
source: git
fetched_at: 2026-05-02T14:50:52.658087109-03:00
rendered_js: false
word_count: 76
summary: This document provides a reference for ESP32 GPIO pin assignments and the JSON-based serial communication protocol used for controlling pins via the ZeroClaw host.
tags:
  - esp32
  - gpio-mapping
  - serial-protocol
  - hardware-interface
  - embedded-systems
  - pin-aliases
category: reference
optimized: true
optimized_at: 2026-05-05T10:00:00Z
---
# ESP32 GPIO Reference

## Pin Aliases

| alias | pin |
|-------|-----|
| builtin_led | 2 |
| red_led | 2 |

## Common Pins (ESP32 / ESP32-C3)

- **GPIO 2**: Built-in LED on many dev boards (output)
- **GPIO 13**: General-purpose output
- **GPIO 21/20**: Often used for UART0 TX/RX (avoid if using serial)

## Protocol

ZeroClaw host sends JSON over serial (115200 baud):

- **gpio_read**: `{"id":"1","cmd":"gpio_read","args":{"pin":13}}`
- **gpio_write**: `{"id":"1","cmd":"gpio_write","args":{"pin":13,"value":1}}`

Response: `{"id":"1","ok":true,"result":"0"}` or `{"id":"1","ok":true,"result":"done"}`

#esp32 #gpio-mapping #serial-protocol #hardware-interface #embedded-systems #pin-aliases
