---
title: VI Datasheets - NUCLEO-F401RE
version: 1.0
authors:
  - Diogo Correia
optimized: true
optimized_at: 2026-05-05T00:00:00Z
date: 2024-01-15
---

# VI Datasheets: NUCLEO-F401RE

Technical specifications for using ZeroClaw with STM32 NUCLEO-F401RE development board.

## Overview

STM32 NUCLEO-F401RE is an affordable board with integrated ST-LINK/V2-1 debugger/programmer based on STM32F401RE microcontroller.

## Pin Mapping

| Pin | ZeroClaw Function | Notes |
|-----|-------------------|-------|
| PA0 | GPIO | General purpose I/O |
| PA1 | PWM | TIM2_CH2 |
| PA2 | UART2 TX | Primary UART TX |
| PA3 | UART2 RX | Primary UART RX |
| PA4 | SPI1 CS | SPI Chip Select |
| PA5 | SPI1 SCK | SPI Clock |
| PA6 | SPI1 MISO | SPI Master In Slave Out |
| PA7 | SPI1 MOSI | SPI Master Out Slave In |
| PA8 | GPIO | General purpose I/O |
| PA9 | UART1 TX | Alternative UART |
| PA10 | UART1 RX | Alternative UART |
| PB0 | GPIO | General purpose I/O |
| PB1 | GPIO | General purpose I/O |
| PB6 | I2C1 SCL | I2C Clock |
| PB7 | I2C1 SDA | I2C Data line |
| PB8 | GPIO | General purpose I/O |
| PB9 | GPIO | General purpose I/O |
| PC0-PC15 | GPIO | General purpose I/O |
| PD2 | GPIO | General purpose I/O |

## Hardware Setup

### Required Components

- STM32 NUCLEO-F401RE board
- ZeroClaw compatible shield or breakout board
- Jumper wires
- ST-LINK/V2-1 debugger (built-in)
- Power supply (via USB or external 5V/3.3V)

### Wiring

```
ZeroClaw Pin 1 → NUCLEO PA0
ZeroClaw Pin 2 → NUCLEO PA1 (PWM)
ZeroClaw Pin 3 → NUCLEO PA2 (UART2 TX)
ZeroClaw Pin 4 → NUCLEO GND
ZeroClaw Pin 5 → NUCLEO 5V or 3.3V (select based on device requirements)
```

### Power

Power options:
- USB connector (5V, 500mA max)
- External 5V via pin 4 (PWR)
- External 3.3V via pin 3 (3V3)

Built-in 3.3V regulator (max 300mA output).

## Software Setup

### Library Installation

1. Install STM32 board support in Arduino IDE:
   - File → Preferences → Additional Boards Manager URLs
   - Add: `https://github.com/stm32duino/BoardManagerFiles/raw/main/package_stmicroelectronics_index.json`
   - Tools → Board → Boards Manager → Search "STM32" → Install "STM32 MCU based boards"

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
  Serial.print("Current position: ");
  Serial.println(position);
  
  delay(100);
}
```

## Communication Protocol

### UART

Multiple UART interfaces available:

| Interface | TX Pin | RX Pin | Notes |
|-----------|--------|--------|-------|
| UART1 | PA9 | PA10 | Primary UART |
| UART2 | PA2 | PA3 | Secondary UART |

Default baud rate: 115200

### SPI

Multiple SPI interfaces:

| Interface | SCK | MISO | MOSI | CS |
|-----------|-----|------|------|----|
| SPI1 | PA5 | PA6 | PA7 | PA4 |
| SPI2 | PB13 | PB14 | PB15 | PB12 |

Maximum speed: 42 MHz

### I2C

Two I2C interfaces:

| Interface | SCL | SDA | Notes |
|-----------|-----|-----|-------|
| I2C1 | PB6 | PB7 | Standard mode |
| I2C2 | PB10 | PB11 | Not on Arduino connectors |

Maximum speed: 400 kHz (standard), 1 MHz (fast mode)

## Supported Baud Rates

| Rate | Notes |
|------|-------|
| 9600 | |
| 19200 | |
| 38400 | |
| 57600 | |
| 115200 | Default |

## Troubleshooting

### Common Issues

**Board not detected**
- Install STM32 drivers if needed
- Check USB connection
- Press reset button
- Verify correct board selected in Arduino IDE

**Upload fails**
- Hold reset button, release when upload starts
- Check ST-LINK drivers
- Update STM32 core to latest version
- Try different USB cable

**Communication errors**
- Verify baud rate settings
- Check wiring for shorts or loose connections
- Add 100nF decoupling capacitor near power pins
- Reduce cable length

**Device not responding**
- Verify power LED is on
- Check 3.3V/5V selection jumper
- Measure voltage on power pins
- Try swapping RX/TX wires

## Performance Characteristics

| Parameter | Value |
|-----------|-------|
| Max Position Range | 0-65535 (16-bit) |
| Position Resolution | 1 unit |
| Max Speed | 2000 units/second |
| Response Time | < 10ms |
| Operating Temperature | -40°C to +85°C |
| Core Clock Speed | Up to 84 MHz |

## Compatibility

- Arduino IDE with STM32 board support
- STM32F401RE microcontroller
- 3.3V logic levels
- Arduino UNO R3 compatible connectors

## Tags
#stm32 #nucleo #f401re #datasheet #hardware #uart #spi #i2c

## See Also

- [[020-vi-datasheets|VI Datasheets Overview]]
- [[235-vi-datasheets-arduino-uno|Arduino Uno Datasheet]]
- [[236-vi-datasheets-esp32|ESP32 Datasheet]]
- [[006-api-reference|API Reference]]
