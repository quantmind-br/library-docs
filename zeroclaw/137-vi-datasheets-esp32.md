---
title: Tham chiếu GPIO ESP32
url: https://github.com/openagen/zeroclaw/blob/master/docs/vi/datasheets/esp32.md
source: git
fetched_at: 2026-05-02T14:52:33.575358296-03:00
rendered_js: false
word_count: 91
summary: Tài liệu cung cấp hướng dẫn tham chiếu chân ESP32 và định nghĩa giao thức serial JSON-based dùng bởi ZeroClaw cho điều khiển GPIO.
tags:
    - esp32
    - gpio-mapping
    - serial-protocol
    - embedded-systems
    - microcontroller
    - pinout-reference
    - vi-docs
category: reference
optimized: true
optimized_at: 2026-05-05T00:00:00Z
---
# Tham chiếu GPIO ESP32

## Bảng bí danh chân

| bí danh | chân |
|---|---|
| builtin_led | 2 |
| red_led | 2 |

---

## Các chân thông dụng (ESP32 / ESP32-C3)

- **GPIO 2**: LED tích hợp trên nhiều dev board (output)
- **GPIO 13**: Đầu ra mục đích chung
- **GPIO 21/20**: Thường dùng cho UART0 TX/RX (tránh nếu đang dùng serial)

---

## Giao thức

ZeroClaw host gửi JSON qua serial (115200 baud):

- `gpio_read`: `{"id":"1","cmd":"gpio_read","args":{"pin":13}}`
- `gpio_write`: `{"id":"1","cmd":"gpio_write","args":{"pin":13,"value":1}}`

Response:
- `{"id":"1","ok":true,"result":"0"}`
- `{"id":"1","ok":true,"result":"done"}`
