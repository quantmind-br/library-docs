---
title: VI Providers Reference
version: 1.0
authors:
  - Diogo Correia
optimized: true
optimized_at: 2026-05-05T00:00:00Z
date: 2024-01-15
---

# VI Providers Reference

Comprehensive reference for all ZeroClaw VI (Virtual Interface) providers.

## Overview

VI Providers enable communication between ZeroClaw library and hardware interfaces or virtual devices. Each provider implements a standardized interface with provider-specific configuration options.

## Provider Types

Supported provider types:
- **SerialProvider**: UART/Serial communication
- **SPIProvider**: SPI bus communication
- **I2CProvider**: I2C bus communication
- **MockProvider**: Virtual/testing provider
- **NetworkProvider**: TCP/UDP network communication

## SerialProvider

Serial communication provider using UART/RS-232/RS-485 interfaces.

### Configuration Options

| Option | Type | Default | Description |
|--------|------|---------|-------------|
| port | string | "/dev/ttyUSB0" | Serial port path |
| baudrate | int | 9600 | Baud rate (9600, 19200, 38400, 57600, 115200) |
| timeout | int | 1000 | Read timeout in milliseconds |
| databits | int | 8 | Data bits (5, 6, 7, 8) |
| stopbits | int | 1 | Stop bits (1, 2) |
| parity | string | "none" | Parity ("none", "even", "odd") |
| rtscts | bool | false | Hardware flow control |
| xonxoff | bool | false | Software flow control |

### Usage Example

```cpp
#include <ZeroClaw.h>
#include <providers/SerialProvider.h>

SerialProvider serial;
ZeroClaw claw(&serial);

void setup() {
  serial.configure({
    "/dev/ttyUSB0",  // port
    115200,           // baudrate
    1000,             // timeout
    8,                // databits
    1,                // stopbits
    "none",           // parity
    false,            // rtscts
    false             // xonxoff
  });
  
  claw.begin();
}
```

### Platform Notes

**Linux**: Ports are `/dev/ttyS#` (physical) or `/dev/ttyUSB#` (USB adapters)

**Windows**: Ports are `COM#` (e.g., COM3, COM4)

**macOS**: Ports are `/dev/cu.*` or `/dev/tty.*`

## SPIProvider

SPI bus communication provider.

### Configuration Options

| Option | Type | Default | Description |
|--------|------|---------|-------------|
| bus | int | 0 | SPI bus number (0, 1, 2) |
| csPin | int | -1 | Chip select pin (-1 for none) |
| clockSpeed | int | 1000000 | Clock speed in Hz |
| mode | int | 0 | SPI mode (0, 1, 2, 3) |
| bitOrder | int | MSBFIRST | Bit order (MSBFIRST, LSBFIRST) |

### Usage Example

```cpp
#include <ZeroClaw.h>
#include <providers/SPIProvider.h>

SPIProvider spi;
ZeroClaw claw(&spi);

void setup() {
  spi.configure({
    0,                // bus
    10,               // csPin
    4000000,          // clockSpeed (4 MHz)
    0,                // mode
    MSBFIRST          // bitOrder
  });
  
  claw.begin();
}
```

### Platform Notes

**Arduino**: Uses hardware SPI pins (SCK, MISO, MOSI)

**ESP32**: Multiple SPI buses available (HSPI, VSPI)

**STM32**: Multiple SPI interfaces (SPI1, SPI2, SPI3)

## I2CProvider

I2C bus communication provider.

### Configuration Options

| Option | Type | Default | Description |
|--------|------|---------|-------------|
| bus | int | 0 | I2C bus number (0, 1) |
| sdaPin | int | -1 | SDA pin (-1 for default) |
| sclPin | int | -1 | SCL pin (-1 for default) |
| clockSpeed | int | 100000 | Clock speed in Hz (100kHz standard, 400kHz fast) |
| pullup | bool | true | Enable internal pull-up resistors |

### Usage Example

```cpp
#include <ZeroClaw.h>
#include <providers/I2CProvider.h>

I2CProvider i2c;
ZeroClaw claw(&i2c);

void setup() {
  i2c.configure({
    0,                // bus
    -1,               // sdaPin (use default)
    -1,               // sclPin (use default)
    400000,           // clockSpeed (400 kHz)
    true              // pullup
  });
  
  claw.begin();
}
```

### Platform Notes

**Arduino**: Uses A4 (SDA) and A5 (SCL) on Uno, dedicated pins on Mega

**ESP32**: Multiple I2C buses available

**STM32**: Multiple I2C interfaces (I2C1, I2C2)

## MockProvider

Virtual provider for testing without hardware.

### Configuration Options

| Option | Type | Default | Description |
|--------|------|---------|-------------|
| simulateErrors | bool | false | Simulate communication errors |
| delayMs | int | 0 | Simulated delay in milliseconds |
| initialPosition | int | 0 | Initial position value |

### Usage Example

```cpp
#include <ZeroClaw.h>
#include <providers/MockProvider.h>

MockProvider mock;
ZeroClaw claw(&mock);

void setup() {
  mock.configure({
    false,            // simulateErrors
    10,               // delayMs
    42                // initialPosition
  });
  
  claw.begin();
}
```

### Features

- Simulates all ZeroClaw commands
- Can inject errors for testing
- Tracks all calls for verification
- No hardware required

## NetworkProvider

Network communication provider using TCP/UDP protocols.

### Configuration Options

| Option | Type | Default | Description |
|--------|------|---------|-------------|
| protocol | string | "tcp" | Network protocol ("tcp", "udp") |
| host | string | "localhost" | Server hostname or IP address |
| port | int | 5000 | Server port number |
| timeout | int | 5000 | Connection timeout in milliseconds |
| reconnect | bool | true | Auto-reconnect on failure |

### Usage Example

```cpp
#include <ZeroClaw.h>
#include <providers/NetworkProvider.h>

NetworkProvider net;
ZeroClaw claw(&net);

void setup() {
  net.configure({
    "tcp",            // protocol
    "192.168.1.100",  // host
    5000,             // port
    5000,             // timeout
    true              // reconnect
  });
  
  claw.begin();
}
```

### Features

- Supports TCP and UDP
- Automatic reconnection
- DNS resolution
- SSL/TLS support (platform dependent)

## Provider Selection Guide

Choose provider based on hardware:

| Hardware | Recommended Provider | Notes |
|----------|---------------------|-------|
| Arduino Uno | SerialProvider | Limited to UART |
| ESP32 | SerialProvider, SPIProvider, I2CProvider, NetworkProvider | Multiple interfaces |
| NUCLEO-F401RE | SerialProvider, SPIProvider, I2CProvider | Multiple interfaces |
| Raspberry Pi | SerialProvider, SPIProvider, I2CProvider, NetworkProvider | Linux-based |

## Error Handling

All providers implement error handling:

```cpp
if (!provider.connect()) {
  Serial.println("Failed to connect!");
  // Handle error
}

if (!provider.write(data)) {
  Serial.println("Write failed!");
  // Handle error
}

if (!provider.read(response, timeout)) {
  Serial.println("Read failed!");
  // Handle error
}
```

Common error codes:
- `PROVIDER_ERROR_CONNECT_FAILED` (-1)
- `PROVIDER_ERROR_WRITE_FAILED` (-2)
- `PROVIDER_ERROR_READ_FAILED` (-3)
- `PROVIDER_ERROR_TIMEOUT` (-4)
- `PROVIDER_ERROR_INVALID_RESPONSE` (-5)

## Performance Comparison

| Provider | Max Speed | Latency | Reliability | Hardware Required |
|----------|-----------|---------|-------------|-------------------|
| Serial | 115200 baud | ~10ms | High | UART interface |
| SPI | 80 MHz | <1ms | Very High | SPI interface |
| I2C | 400 kHz | ~5ms | Medium | I2C interface |
| Mock | N/A | ~0ms | Perfect | None |
| Network | 1 Gbps (TCP) | ~50ms | Medium | Network connection |

## Tags
#providers #serial #spi #i2c #network #mock #communication

## See Also

- [[021-vi-providers|VI Providers Guide]]
- [[006-api-reference|API Reference]]
- [[235-vi-datasheets-arduino-uno|Arduino Uno Datasheet]]
- [[236-vi-datasheets-esp32|ESP32 Datasheet]]
- [[237-vi-datasheets-nucleo-f401re|NUCLEO-F401RE Datasheet]]
