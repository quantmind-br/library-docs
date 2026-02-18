---
title: Esp32
url: https://github.com/zeroclaw-labs/zeroclaw/blob/main/docs/datasheets/esp32.md
source: git
fetched_at: 2026-02-18T07:18:23.101655-03:00
rendered_js: false
word_count: 76
summary: This document provides a reference for ESP32 GPIO pin assignments and aliases, along with the JSON-based serial protocol for reading and writing pin states.
tags:
    - esp32
    - gpio
    - serial-protocol
    - hardware-reference
    - json-api
category: reference
---

# ESP32 GPIO Reference

## Pin Aliases

| alias       | pin |
|-------------|-----|
| builtin_led | 2   |
| red_led     | 2   |

## Common pins (ESP32 / ESP32-C3)

- **GPIO 2**: Built-in LED on many dev boards (output)
- **GPIO 13**: General-purpose output
- **GPIO 21/20**: Often used for UART0 TX/RX (avoid if using serial)

## Protocol

ZeroClaw host sends JSON over serial (115200 baud):
- `gpio_read`: `{"id":"1","cmd":"gpio_read","args":{"pin":13}}`
- `gpio_write`: `{"id":"1","cmd":"gpio_write","args":{"pin":13,"value":1}}`

Response: `{"id":"1","ok":true,"result":"0"}` or `{"id":"1","ok":true,"result":"done"}`
