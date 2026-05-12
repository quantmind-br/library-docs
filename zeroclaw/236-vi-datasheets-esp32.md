---
title: VI Datasheets - ESP32
version: 1.0
authors:
  - Diogo Correia
optimized: true
optimized_at: 2026-05-05T00:00:00Z
date: 2024-01-15
---

# VI Datasheets: ESP32

Technical specifications for using ZeroClaw with ESP32 development boards.

## Overview

ESP32 is a low-cost, low-power SoC with integrated Wi-Fi and dual-mode Bluetooth. Uses Tensilica Xtensa LX6/LX7 or RiscV processor with dual-core/single-core variations.

## Pin Mapping

| ESP32 Pin | ZeroClaw Function | Notes |
|-----------|-------------------|-------|
| GPIO0 | Boot mode control | Avoid use in normal operation |
| GPIO1 (TX0) | Serial TX | Primary UART TX |
| GPIO2 | GPIO | General purpose I/O |
| GPIO3 (RX0) | Serial RX | Primary UART RX |
| GPIO4 | GPIO | General purpose I/O |
| GPIO5 | SPI CS | SPI Chip Select |
| GPIO12 | GPIO | General purpose I/O |
| GPIO13 | GPIO | General purpose I/O |
| GPIO14 | SPI SCK | SPI Clock |
| GPIO15 | SPI MOSI | SPI Master Out Slave In |
| GPIO16 | SPI MISO | SPI Master In Slave Out |
| GPIO17 | GPIO | General purpose I/O |
| GPIO18 | PWM | Pulse-width modulation output |
| GPIO19 | PWM | Pulse-width modulation output |
| GPIO21 | I2C SDA | I2C Data line |
| GPIO22 | I2C SCL | I2C Clock line |
| GPIO23 | GPIO | General purpose I/O |
| GPIO25 | ADC | 12-bit ADC |
| GPIO26 | ADC | 12-bit ADC |
| GPIO27 | ADC | 12-bit ADC |
| GPIO32 | ADC | 12-bit ADC |
| GPIO33 | ADC | 12-bit ADC |
| GPIO34 | Input only | No internal pull-up/pull-down |
| GPIO35 | Input only | No internal pull-up/pull-down |
| GPIO36 | Input only | No internal pull-up/pull-down |
| GPIO39 | Input only | No internal pull-up/pull-down |

## Hardware Setup

### Required Components

- ESP32 development board (e.g., ESP32-WROOM-32)
- ZeroClaw compatible shield or breakout board
- Jumper wires
- 5V to 3.3V logic level converter (if needed)
- Power supply (5V USB or external 5V source)

### Wiring

```
ZeroClaw Pin 1 → ESP32 GPIO2
ZeroClaw Pin 2 → ESP32 GPIO18 (PWM)
ZeroClaw Pin 3 → ESP32 GPIO25 (ADC)
ZeroClaw Pin 4 → ESP32 GND
ZeroClaw Pin 5 → ESP32 3.3V
```

### Power

ESP32 operates at 3.3V logic levels. Use logic level converter if ZeroClaw requires 5V. Power options:
- USB: 500mA max
- External 5V: via 5V pin (regulated to 3.3V)
- Vin pin: 5-12V input (regulated to 3.3V)

## Software Setup

### Library Installation

1. Install ESP32 board support in Arduino IDE:
   - File → Preferences → Additional Boards Manager URLs
   - Add: `https://raw.githubusercontent.com/espressif/arduino-esp32/gh-pages/package_esp32_index.json`
   - Tools → Board → Boards Manager → Search "esp32" → Install

2. Install ZeroClaw library

### Basic Example

```cpp
#include <ZeroClaw.h>

ZeroClaw claw;

void setup() {
  Serial.begin(115200);
  claw.begin(115200);
  
  if (!claw.initialize()) {
    Serial.println("Initialization failed!");
    while (1);
  }
}

void loop() {
  int position = claw.getPosition();
  Serial.printf("Current position: %d\n", position);
  
  delay(100);
}
```

## Communication Protocol

Supports multiple communication interfaces:

### UART

- Default baud rate: 115200
- Supports hardware serial ports UART0, UART1, UART2
- UART0 (GPIO1/TX0, GPIO3/RX0) used for programming/debugging

### SPI

- Up to 4 SPI interfaces
- Default pins: HSPI (GPIO12-15) or VSPI (GPIO5,18,23,19)
- Maximum speed: 80 MHz

### I2C

- Two I2C interfaces
- Default pins: I2C0 (GPIO21/SDA, GPIO22/SCL)
- Maximum speed: 800 kHz

## Supported Baud Rates

| Rate | Notes |
|------|-------|
| 9600 | Low speed, reliable |
| 19200 | |
| 38400 | |
| 57600 | |
| 115200 | Default, recommended |

## Troubleshooting

### Common Issues

**Device not detected**
- Check USB connection
- Verify correct board selected in Arduino IDE
- Ensure drivers installed (CP210x, CH340)
- Try different USB port

**Communication errors**
- Verify baud rate matches on both ends
- Check wiring for loose connections
- Add 100nF capacitor between 3.3V and GND
- Reduce cable length

**ESP32 crashes or reboots**
- Add 10uF capacitor between Vin and GND
- Reduce power consumption
- Check for electrical noise
- Update ESP32 core to latest version

## Performance Characteristics

| Parameter | Value |
|-----------|-------|
| Max Position Range | 0-4095 (12-bit) |
| Position Resolution | 1 unit |
| Max Speed | 1000 units/second |
| Response Time | < 20ms |
| Operating Temperature | -40°C to +85°C |
| WiFi Range | Up to 1km (outdoor, line of sight) |

## Compatibility

- Arduino IDE with ESP32 board support
- ESP32-WROOM-32, ESP32-WROOM-32D, ESP32-WROOM-32E
- 3.3V logic levels
- WiFi and Bluetooth connectivity

## Tags
#esp32 #datasheet #hardware #uart #spi #i2c #wifi #bluetooth

## See Also

- [[020-vi-datasheets|VI Datasheets Overview]]
- [[235-vi-datasheets-arduino-uno|Arduino Uno Datasheet]]
- [[237-vi-datasheets-nucleo-f401re|NUCLEO-F401RE Datasheet]]
- [[006-api-reference|API Reference]]
