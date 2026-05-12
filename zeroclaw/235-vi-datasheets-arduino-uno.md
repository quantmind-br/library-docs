---
title: VI Datasheets - Arduino Uno
version: 1.0
authors:
  - Diogo Correia
optimized: true
optimized_at: 2026-05-05T00:00:00Z
date: 2024-01-15
---

# VI Datasheets: Arduino Uno

Technical specifications for using ZeroClaw with Arduino Uno boards.

## Overview

The Arduino Uno is a microcontroller board based on the ATmega328P with 14 digital I/O pins (6 PWM), 6 analog inputs, 16 MHz crystal, USB, power jack, ICSP header, and reset button.

## Pin Mapping

| Arduino Pin | ZeroClaw Function | Notes |
|-------------|-------------------|-------|
| D0 (RX) | Serial RX | Not recommended for general use |
| D1 (TX) | Serial TX | Not recommended for general use |
| D2 | GPIO | General purpose I/O |
| D3 | PWM | Pulse-width modulation output |
| D4 | GPIO | General purpose I/O |
| D5 | PWM | Pulse-width modulation output |
| D6 | PWM | Pulse-width modulation output |
| D7 | GPIO | General purpose I/O |
| D8 | GPIO | General purpose I/O |
| D9 | PWM | Pulse-width modulation output |
| D10 | SPI CS | SPI Chip Select |
| D11 | SPI MOSI | SPI Master Out Slave In |
| D12 | SPI MISO | SPI Master In Slave Out |
| D13 | SPI SCK | SPI Clock |
| A0-A5 | Analog Input | 10-bit ADC |

## Hardware Setup

### Required Components

- Arduino Uno board
- ZeroClaw compatible shield or breakout board
- Jumper wires
- Power supply (5V or 7-12V via barrel jack)

### Wiring

```
ZeroClaw Pin 1 → Arduino D2
ZeroClaw Pin 2 → Arduino D3 (PWM)
ZeroClaw Pin 3 → Arduino A0 (Analog)
ZeroClaw Pin 4 → Arduino GND
ZeroClaw Pin 5 → Arduino 5V
```

### Power

Arduino Uno powers small loads from 5V pin (max 500mA). Use external power for higher current loads via Vin or barrel jack.

## Software Setup

### Library Installation

1. Download ZeroClaw library from official repository
2. In Arduino IDE: Sketch → Include Library → Add .ZIP Library...
3. Select downloaded ZIP file
4. Restart Arduino IDE

### Basic Example

```cpp
#include <ZeroClaw.h>

ZeroClaw claw;

void setup() {
  Serial.begin(9600);
  claw.begin(9600);
  
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

Uses UART communication with ZeroClaw devices. Default baud rate: 9600.

### Supported Baud Rates

- 9600 (default)
- 19200
- 38400
- 57600
- 115200

### Command Format

All commands are ASCII strings terminated with newline (`\n`).

| Command | Description | Response |
|---------|-------------|----------|
| `GET POS` | Get current position | `POS:<value>` |
| `SET POS <value>` | Set target position | `ACK` or `NAK` |
| `GET STATUS` | Get device status | `STATUS:<value>` |
| `RESET` | Reset device | `ACK` |

## Troubleshooting

### Common Issues

**Device not responding**
- Check wiring connections
- Verify 5V power supply
- Ensure correct baud rate
- Try different USB cable

**Incorrect position values**
- Calibrate using `SET CAL <value>` command
- Check mechanical obstructions
- Verify sensor alignment

**Communication errors**
- Reduce cable length
- Add pull-up resistors to RX/TX lines
- Check for electrical noise

## Performance Characteristics

| Parameter | Value |
|-----------|-------|
| Max Position Range | 0-1023 (10-bit) |
| Position Resolution | 1 unit |
| Max Speed | 500 units/second |
| Response Time | < 50ms |
| Operating Temperature | -10°C to +70°C |

## Compatibility

- Arduino IDE 1.8.0+
- ATmega328P chip
- 3.3V and 5V logic levels

## Tags
#arduino #uno #datasheet #hardware #uart

## See Also

- [[020-vi-datasheets|VI Datasheets Overview]]
- [[236-vi-datasheets-esp32|ESP32 Datasheet]]
- [[237-vi-datasheets-nucleo-f401re|NUCLEO-F401RE Datasheet]]
- [[006-api-reference|API Reference]]
