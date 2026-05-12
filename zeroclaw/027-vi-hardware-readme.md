---
title: README
tags:
  - hardware-integration
  - embedded-systems
  - peripheral-control
  - microcontroller-setup
  - zeroclaw-framework
url: https://github.com/openagen/zeroclaw/blob/master/docs/vi/hardware/README.md
source: git
category: guide
optimized: true
optimized_at: 2026-05-05T00:00:00Z
word_count: 132
---
# Tài liệu phần cứng và ngoại vi

Tích hợp board, firmware và ngoại vi.

Hệ thống phần cứng của ZeroClaw cho phép điều khiển trực tiếp vi điều khiển và ngoại vi thông qua trait `Peripheral`. Mỗi board cung cấp các tool cho GPIO, ADC và các thao tác cảm biến, cho phép tương tác phần cứng do agent điều khiển trên các board như STM32 Nucleo, Raspberry Pi và ESP32.

## Điểm bắt đầu

- Kiến trúc và mô hình ngoại vi: [[../hardware-peripherals-design|hardware peripherals design]]
- Thêm board/tool mới: [[../adding-boards-and-tools|adding boards and tools]]
- Thiết lập Nucleo: [[../nucleo-setup|Nucleo setup]]
- Thiết lập Arduino Uno R4 WiFi: [[../arduino-uno-q-setup|Arduino Uno Q setup]]

## Datasheet

- Chỉ mục datasheet: [[../datasheets|datasheets]]
- STM32 Nucleo-F401RE: [[../datasheets/nucleo-f401re|Nucleo F401RE]]
- Arduino Uno: [[../datasheets/arduino-uno|Arduino Uno]]
- ESP32: [[../datasheets/esp32|ESP32]]
