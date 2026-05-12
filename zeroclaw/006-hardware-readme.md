---
title: README
url: https://github.com/openagen/zeroclaw/blob/master/docs/hardware/README.md
source: git
fetched_at: 2026-05-02T14:50:48.665327053-03:00
rendered_js: false
word_count: 115
summary: This document serves as a central hub for configuring and integrating microcontrollers and peripherals within the ZeroClaw system. It provides architectural documentation, board-specific setup guides, and a repository for hardware datasheets.
tags:
    - hardware-integration
    - firmware-development
    - microcontroller-setup
    - peripheral-architecture
    - embedded-systems
category: reference
optimized: true
optimized_at: 2026-05-05T00:00:00Z
---
# Hardware & Peripherals Docs

> [!info] Purpose
> Central hub for configuring and integrating microcontrollers, peripherals, and hardware datasheets.

ZeroClaw's hardware subsystem enables direct control of microcontrollers and peripherals via the `Peripheral` trait. Each board exposes tools for GPIO, ADC, and sensor operations, allowing agent-driven hardware interaction on boards like STM32 Nucleo, Raspberry Pi, and ESP32.

## Entry Points

- Architecture and peripheral model: [[076-hardware-hardware-peripherals-design|Hardware peripherals design]]
- Add a new board/tool: [[146-contributing-adding-boards-and-tools|Adding boards and tools]]
- Nucleo setup: [[062-hardware-nucleo-setup|Nucleo setup]]
- Arduino Uno R4 WiFi setup: [[061-hardware-arduino-uno-q-setup|Arduino uno q setup]]

## Datasheets

- Datasheet index: [datasheets](datasheets)
- STM32 Nucleo-F401RE: [[110-hardware-datasheets-nucleo-f401re|Nucleo f401re]]
- Arduino Uno: [[108-hardware-datasheets-arduino-uno|Arduino uno]]
- ESP32: [[109-hardware-datasheets-esp32|Esp32]]

#hardware #embedded-systems #microcontroller #peripheral-architecture