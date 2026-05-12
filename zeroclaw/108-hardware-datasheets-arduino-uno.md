---
title: Arduino uno
title_vi: Arduino Uno
url: https://github.com/openagen/zeroclaw/blob/master/docs/hardware/datasheets/arduino-uno.md
source: git
fetched_at: 2026-05-02T14:50:51.712857745-03:00
rendered_js: false
word_count: 207
summary: This document provides technical specifications, pin mapping, and interface instructions for the Arduino Uno within the ZeroClaw development environment.
optimized: true
optimized_at: 2026-05-05T00:00:00Z
tags:
  - arduino-uno
  - gpio-mapping
  - serial-communication
  - zeroclaw-tools
  - microcontroller-specs
category: reference
---
# Arduino Uno

## Pin Aliases

| Alias | Pin |
|-------|-----|
| `red_led` | 13 |
| `builtin_led` | 13 |
| `user_led` | 13 |

## Tổng quan

Arduino Uno là board vi điều khiển dựa trên ATmega328P. Có 14 chân digital I/O (0–13) và 6 đầu vào analog (A0–A5).

## Chân Digital

- **Chân 0–13:** Digital I/O. Có thể INPUT hoặc OUTPUT
- **Chân 13:** LED built-in (trên board). Kết nối LED tới GND hoặc dùng làm output
- **Chân 0–1:** Cũng dùng cho Serial (RX/TX). Tránh dùng nếu dùng Serial

## GPIO

- `digitalWrite(pin, HIGH)` hoặc `digitalWrite(pin, LOW)` cho output
- `digitalRead(pin)` cho input (trả về 0 hoặc 1)
- Số chân trong protocol ZeroClaw: 0–13

## Serial

- UART trên chân 0 (RX) và 1 (TX)
- USB qua ATmega16U2 hoặc CH340 (bản clone)
- Baud rate: 115200 cho firmware ZeroClaw

## ZeroClaw Tools

- `gpio_read`: Đọc giá trị chân (0 hoặc 1)
- `gpio_write`: Set chân high (1) hoặc low (0)
- `arduino_upload`: Agent sinh code sketch Arduino đầy đủ; ZeroClaw compile và upload qua arduino-cli. Dùng cho "make a heart", patterns tùy chỉnh — agent viết code, không chỉnh sửa thủ công. Chân 13 = built-in LED

#arduino-uno #gpio #microcontroller