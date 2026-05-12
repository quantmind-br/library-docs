---
title: Esp32
url: https://github.com/openagen/zeroclaw/blob/master/docs/i18n/vi/datasheets/esp32.md
source: git
fetched_at: 2026-05-02T14:51:11.623185204-03:00
rendered_js: false
word_count: 85
summary: This document provides a reference for ESP32 GPIO pin assignments and the JSON-based serial communication protocol used for controlling pins via the ZeroClaw host.
tags:
    - esp32
    - gpio-pinout
    - serial-communication
    - embedded-systems
    - json-api
    - hardware-reference
category: reference
optimized: true
optimized_at: 2026-05-05T12:00:00Z
---

# Tham chiếu GPIO ESP32

> [!note]
> Tài liệu tham khảo nhanh về cấu hình pin ESP32 và giao thức serial JSON cho ZeroClaw

---

## 1. Pin Aliases

| Alias | Pin |
|---|---|
| `builtin_led` | 2 |
| `red_led` | 2 |

---

## 2. Các pin thông dụng (ESP32 / ESP32-C3)

| Pin | Loại | Ghi chú |
|---|---|---|
| GPIO 2 | Output | LED tích hợp trên nhiều dev board |
| GPIO 13 | Output | Đầu ra mục đích chung |
| GPIO 21/20 | UART | Thường dùng cho UART0 TX/RX (tránh nếu đang dùng serial) |

---

## 3. Giao thức Serial JSON

ZeroClaw host gửi JSON qua serial (115200 baud):

**Yêu cầu:**
- `gpio_read`: `{"id":"1","cmd":"gpio_read","args":{"pin":13}}`
- `gpio_write`: `{"id":"1","cmd":"gpio_write","args":{"pin":13,"value":1}}`

**Phản hồi:**
- `{"id":"1","ok":true,"result":"0"}`
- `{"id":"1","ok":true,"result":"done"}`

#esp32 #gpio-pinout #serial-communication #embedded-systems #json-api #hardware-reference #vietnamese-docs