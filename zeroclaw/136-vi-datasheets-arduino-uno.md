---
title: Tham chiếu Arduino Uno
url: https://github.com/openagen/zeroclaw/blob/master/docs/vi/datasheets/arduino-uno.md
source: git
fetched_at: 2026-05-02T14:52:32.713315812-03:00
rendered_js: false
word_count: 220
summary: Tài liệu cung cấp tổng quan kỹ thuật về cấu hình chân Arduino Uno, chức năng GPIO, giao tiếp serial và tích hợp với tools ZeroClaw cho việc triển khai sketch tự động.
tags:
    - arduino-uno
    - gpio-mapping
    - serial-communication
    - zeroclaw-tools
    - microcontroller
    - pin-configuration
    - vi-docs
category: reference
optimized: true
optimized_at: 2026-05-05T00:00:00Z
---
# Tham chiếu Arduino Uno

## Bảng bí danh chân

| bí danh | chân |
|---|---|
| red_led | 13 |
| builtin_led | 13 |
| user_led | 13 |

---

## Tổng quan

Arduino Uno là board vi điều khiển dựa trên ATmega328P. Có 14 chân digital I/O (0–13) và 6 đầu vào analog (A0–A5).

---

## Chân Digital

- **Chân 0–13:** Digital I/O (INPUT hoặc OUTPUT)
- **Chân 13:** LED tích hợp (onboard)
- **Chân 0–1:** Cũng dùng cho Serial (RX/TX). Tránh dùng nếu đang sử dụng Serial

---

## GPIO

- `digitalWrite(pin, HIGH)` hoặc `digitalWrite(pin, LOW)` để xuất tín hiệu
- `digitalRead(pin)` để đọc đầu vào (trả về 0 hoặc 1)
- Số chân trong giao thức ZeroClaw: 0–13

---

## Serial

- UART trên chân 0 (RX) và 1 (TX)
- USB qua ATmega16U2 hoặc CH340 (bản clone)
- Baud rate: 115200 cho firmware ZeroClaw

---

## ZeroClaw Tools

- `gpio_read`: Đọc giá trị chân (0 hoặc 1)
- `gpio_write`: Đặt chân lên cao (1) hoặc xuống thấp (0)
- `arduino_upload`: Agent tạo code Arduino sketch đầy đủ; ZeroClaw biên dịch và tải lên qua arduino-cli

> [!note]
> Dùng cho "make a heart", các pattern tùy chỉnh — agent viết code, không cần chỉnh sửa thủ công. Chân 13 = LED tích hợp
