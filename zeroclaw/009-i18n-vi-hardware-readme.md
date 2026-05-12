---
title: README
url: https://github.com/openagen/zeroclaw/blob/master/docs/i18n/vi/hardware/README.md
source: git
fetched_at: 2026-05-02T14:51:16.591511245-03:00
rendered_js: false
word_count: 145
summary: This document serves as an entry point for integrating hardware boards, firmware, and peripherals within the ZeroClaw system, providing architectural guidance and setup resources for various microcontrollers.
tags:
    - hardware-integration
    - embedded-systems
    - microcontroller-setup
    - firmware-development
    - peripheral-control
    - zeroclaw
category: guide
optimized: true
optimized_at: 2026-05-05T00:00:00Z
---
# Tài liệu phần cứng và ngoại vi

> [!info] Mục đích
> Điểm vào cho tích hợp board, firmware và ngoại vi trong hệ thống ZeroClaw.

Hệ thống phần cứng của ZeroClaw cho phép điều khiển trực tiếp vi điều khiển và ngoại vi thông qua trait `Peripheral`. Mỗi board cung cấp các tool cho GPIO, ADC và cảm biến, cho phép tương tác phần cứng do agent điều khiển trên các board như STM32 Nucleo, Raspberry Pi và ESP32.

## Điểm bắt đầu

- Kiến trúc và mô hình ngoại vi: [[080-i18n-vi-hardware-peripherals-design|Hardware peripherals design]]
- Thêm board/tool mới: [[036-i18n-vi-adding-boards-and-tools|Adding boards and tools]]
- Thiết lập Nucleo: [[035-i18n-vi-nucleo-setup|Nucleo setup]]
- Thiết lập Arduino Uno R4 WiFi: [[033-i18n-vi-arduino-uno-q-setup|Arduino uno q setup]]

## Datasheet

- Chỉ mục datasheet: [datasheets](../datasheets)
- STM32 Nucleo-F401RE: [[117-i18n-vi-datasheets-nucleo-f401re|Nucleo f401re]]
- Arduino Uno: [[115-i18n-vi-datasheets-arduino-uno|Arduino uno]]
- ESP32: [[116-i18n-vi-datasheets-esp32|Esp32]]

#hardware #embedded-systems #microcontroller #peripheral-control