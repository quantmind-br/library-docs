---
title: Arduino uno
url: https://github.com/openagen/zeroclaw/blob/master/docs/i18n/vi/datasheets/arduino-uno.md
source: git
fetched_at: 2026-05-02T14:51:10.724794573-03:00
rendered_js: false
word_count: 221
summary: This document provides a technical overview of the Arduino Uno board, detailing pin configurations, GPIO operations, serial communication, and the use of ZeroClaw tools for automated code deployment.
tags:
    - arduino-uno
    - gpio-pins
    - serial-communication
    - microcontroller
    - zeroclaw
    - pin-mapping
category: reference
optimized: true
optimized_at: 2026-05-05T12:00:00Z
---

# Arduino Uno

> [!note]
> Tài liệu tham khảo nhanh về cấu hình pin, GPIO và giao thức serial cho Arduino Uno trong ZeroClaw

---

## 1. Pin Aliases

| Alias | Pin |
|---|---|
| `red_led` | 13 |
| `builtin_led` | 13 |
| `user_led` | 13 |

---

## 2. Tổng quan

Arduino Uno là board vi điều khiển dựa trên ATmega328P.

- **14 pin digital I/O** (0–13)
- **6 đầu vào analog** (A0–A5)

---

## 3. Pin Digital

| Loại | Pins | Mô tả |
|---|---|---|
| Digital I/O | 0–13 | Có thể cấu hình INPUT hoặc OUTPUT |
| LED tích hợp | 13 | LED sẵn có trên board |
| Serial | 0–1 | Cũng dùng cho Serial (RX/TX). Tránh dùng nếu đang sử dụng Serial |

---

## 4. GPIO

**API ZeroClaw:**
- `gpio_read`: Đọc giá trị pin (trả về 0 hoặc 1)
- `gpio_write`: Đặt pin lên cao (1) hoặc xuống thấp (0)

**Chú ý:**
- Số pin trong giao thức ZeroClaw: **0–13**
- `digitalWrite(pin, HIGH)` / `digitalWrite(pin, LOW)`
- `digitalRead(pin)`

---

## 5. Serial

| Đặc điểm | Chi tiết |
|---|---|
| UART | Pin 0 (RX) và 1 (TX) |
| USB | Qua ATmega16U2 hoặc CH340 (bản clone) |
| Baud rate | 115200 cho firmware ZeroClaw |

---

## 6. ZeroClaw Tools

**Công cụ tự động hóa:**
- `gpio_read`: Đọc giá trị pin
- `gpio_write`: Điều khiển pin
- `arduino_upload`: Agent tạo code Arduino sketch đầy đủ; ZeroClaw biên dịch và tải lên qua `arduino-cli`

**Ví dụ sử dụng:**
- "make a heart"
- Các pattern tùy chỉnh

**Lưu ý:**
- Agent viết code, không cần chỉnh sửa thủ công
- Pin 13 = LED tích hợp

#arduino-uno #gpio-pins #serial-communication #microcontroller #zeroclaw #pin-mapping #vietnamese-docs