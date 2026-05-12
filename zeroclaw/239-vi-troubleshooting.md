---
title: VI Troubleshooting Guide
version: 1.0
authors:
  - Diogo Correia
optimized: true
optimized_at: 2026-05-05T00:00:00Z
date: 2024-01-15
---

# VI Troubleshooting Guide

Solutions to common issues when using ZeroClaw with various hardware platforms.

## Overview

Addresses frequently encountered problems with step-by-step solutions.

## General Troubleshooting Steps

1. **Verify physical connections** – Check all wires
2. **Confirm power supply** – Adequate voltage and current
3. **Check communication settings** – Baud rate, parity, stop bits
4. **Update software** – Latest library and firmware
5. **Review error messages** – Understand system feedback
6. **Test with minimal setup** – Isolate the problem

## Communication Issues

### No Communication / Device Not Responding

**Symptoms:**
- `claw.initialize()` returns false
- No response to commands
- Timeout errors

**Causes:**
- Incorrect wiring
- Wrong baud rate
- Power issues
- Device not powered
- Wrong serial port

**Solutions:**

1. **Check wiring:**
   ```
   ZeroClaw Pin 1 → GND
   ZeroClaw Pin 2 → RX (connect to TX on controller)
   ZeroClaw Pin 3 → TX (connect to RX on controller)
   ZeroClaw Pin 4 → 5V or 3.3V (depending on device)
   ```

2. **Verify baud rate:**
   ```cpp
   claw.begin(9600);
   delay(100);
   if (!claw.initialize()) {
     claw.begin(115200);
     // ...
   }
   ```

3. **Check power:**
   - Measure voltage on VCC and GND pins
   - Ensure minimum 500mA current
   - Try external power supply

4. **Test with known-good device**
5. **Verify port selection:**
   - Linux: `/dev/ttyUSB0`, `/dev/ttyACM0`
   - Windows: `COM3`, `COM4`
   - macOS: `/dev/cu.usbserial-*`

### Communication Errors / Garbled Data

**Symptoms:**
- Incorrect position values
- Random characters in responses
- CRC errors
- "NAK" responses

**Causes:**
- Electrical noise
- Incorrect baud rate
- Wrong data format
- Voltage mismatch
- Long cable lengths

**Solutions:**

1. **Reduce cable length** – Keep under 1 meter
2. **Add capacitors** – 100nF ceramic capacitor near device power pins
3. **Use shielded cables** – For long runs
4. **Check voltage levels** – Use logic level converter if needed
5. **Verify baud rate** – Both ends must match
6. **Add pull-up resistors** – 4.7KΩ on RX/TX lines
7. **Enable parity checking** – If supported

### Timeout Errors

**Symptoms:**
- `PROVIDER_ERROR_TIMEOUT` errors
- Commands hang indefinitely
- No response within expected time

**Causes:**
- Device not responding
- Slow communication
- Buffer overflows
- Interrupt conflicts

**Solutions:**

1. **Increase timeout:**
   ```cpp
   serial.configure({
     "/dev/ttyUSB0",
     115200,
     5000  // 5 second timeout
   });
   ```

2. **Check for blocking operations**
3. **Reduce communication speed**
4. **Add watchdog timer**

## Platform-Specific Issues

### Arduino Uno

#### Upload Issues

**Problem:** Sketch won't upload

**Solutions:**
- Select correct board: Tools → Board → Arduino Uno
- Select correct port: Tools → Port → COM#
- Press reset button before upload
- Try different USB cable
- Update Arduino IDE

#### Serial Monitor Issues

**Problem:** Garbage or no output

**Solutions:**
- Set baud rate to match device (9600 or 115200)
- Check Tools → Board selection
- Try different serial monitor
- Verify USB drivers installed

### ESP32

#### WiFi Issues

**Problem:** WiFi connection fails

**Solutions:**
- Check SSID and password
- Verify WiFi network in range
- Update ESP32 core libraries
- Add 10uF capacitor between 3.3V and GND

#### Deep Sleep Issues

**Problem:** Device doesn't wake from deep sleep

**Solutions:**
- Ensure wakeup pin properly connected
- Check deep sleep duration settings
- Verify power consumption limits
- Add external pull-up on wakeup pin

### NUCLEO-F401RE

#### Upload Issues

**Problem:** Upload fails with timeout or no device

**Solutions:**
- Hold reset button, release when upload starts
- Select correct board: Tools → Board → STM32 NUCLEO-F401RE
- Select correct port
- Update STM32duino core
- Install ST-LINK drivers

#### Clock Issues

**Problem:** Device runs at wrong speed

**Solutions:**
- Verify clock configuration in STM32CubeMX
- Check HSE/HSI settings
- Update board support package
- Measure clock output

## Device-Specific Issues

### Position Tracking Problems

**Symptoms:**
- Position values jump around
- Position doesn't update
- Values clamped or limited

**Causes:**
- Mechanical issues
- Sensor calibration needed
- Electrical noise
- Insufficient power

**Solutions:**

1. **Calibrate device:**
   ```cpp
   claw.setCalibration(0, 1023);
   claw.calibrate();
   ```

2. **Check mechanical assembly:**
   - Ensure no obstructions
   - Verify all parts tight
   - Check for wear or damage

3. **Add filtering:**
   ```cpp
   int position = claw.getPosition();
   position = filter.update(position);
   ```

4. **Verify power:**
   - Measure voltage under load
   - Check for voltage drops
   - Add decoupling capacitors

### Performance Issues

**Symptoms:**
- Slow response times
- Lag in position updates
- Commands take too long

**Causes:**
- High communication latency
- Slow controller
- Inefficient code
- Buffer overflows

**Solutions:**

1. **Optimize communication:**
   - Use higher baud rate (if supported)
   - Switch to SPI or I2C if using UART
   - Reduce message frequency

2. **Optimize code:**
   ```cpp
   int pos = claw.getPosition();
   ```

3. **Check for blocking operations:**
   - Replace `delay()` with non-blocking timers
   - Use interrupts for time-critical operations

4. **Upgrade hardware:**
   - Faster controller board
   - Dedicated communication interface
   - Better power supply

## Error Code Reference

| Error Code | Description | Solution |
|------------|-------------|----------|
| `PROVIDER_ERROR_CONNECT_FAILED` | Could not establish connection | Check wiring, power, port |
| `PROVIDER_ERROR_WRITE_FAILED` | Failed to send data | Verify connection, check buffers |
| `PROVIDER_ERROR_READ_FAILED` | Failed to receive data | Check baud rate, reduce noise, increase timeout |
| `PROVIDER_ERROR_TIMEOUT` | Operation timed out | Increase timeout, check device |
| `PROVIDER_ERROR_INVALID_RESPONSE` | Malformed data received | Verify protocol, check electrical issues |
| `CLAW_ERROR_NOT_INITIALIZED` | Library not initialized | Call `claw.begin()` first |
| `CLAW_ERROR_INVALID_PARAMETER` | Invalid parameter value | Check parameter ranges |
| `CLAW_ERROR_OUT_OF_RANGE` | Value outside allowed range | Verify position limits, calibration |

## Advanced Debugging

### Logging

Enable detailed logging:

```cpp
#define DEBUG 1

void setup() {
  Serial.begin(115200);
  #if DEBUG
  claw.setDebugLevel(DEBUG_ALL);
  #endif
  
  claw.begin(115200);
}
```

### Oscilloscope Analysis

Verify:
- Signal integrity on RX/TX lines
- Voltage levels (0V to VCC)
- Rise/fall times
- Noise levels

### Logic Analyzer

Identify:
- Missing or extra bits
- Incorrect baud rate
- Protocol violations
- Timing issues

## When to Contact Support

Contact support if:
- All troubleshooting steps followed
- Issue persists across multiple devices
- Hardware defect suspected
- Need clarification on error messages

**Provide:**
- Library version
- Hardware platform
- Full error messages
- Steps to reproduce
- Serial output with debug enabled

## Tags
#troubleshooting #debugging #uart #spi #i2c #network #arduino #esp32 #stm32

## See Also

- [[010-troubleshooting|General Troubleshooting]]
- [[235-vi-datasheets-arduino-uno|Arduino Uno Datasheet]]
- [[236-vi-datasheets-esp32|ESP32 Datasheet]]
- [[237-vi-datasheets-nucleo-f401re|NUCLEO-F401RE Datasheet]]
- [[238-vi-providers-reference|Providers Reference]]
