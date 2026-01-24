---
title: Brightness Control | Dank Linux
url: https://danklinux.com/docs/dankmaterialshell/cli-brightness
source: sitemap
fetched_at: 2026-01-24T13:33:21.479397223-03:00
rendered_js: false
word_count: 714
summary: This document provides a comprehensive guide to the dms brightness command, a unified interface for controlling brightness on laptop screens, LEDs, and external DDC/I2C monitors.
tags:
    - brightness-control
    - backlight
    - ddc-ci
    - command-line-interface
    - led-management
    - display-settings
category: reference
---

```
██████╗ ██████╗ ██╗ ██████╗ ██╗  ██╗████████╗███╗   ██╗███████╗███████╗███████╗
██╔══██╗██╔══██╗██║██╔════╝ ██║  ██║╚══██╔══╝████╗  ██║██╔════╝██╔════╝██╔════╝
██████╔╝██████╔╝██║██║  ███╗███████║   ██║   ██╔██╗ ██║█████╗  ███████╗███████╗
██╔══██╗██╔══██╗██║██║   ██║██╔══██║   ██║   ██║╚██╗██║██╔══╝  ╚════██║╚════██║
██████╔╝██║  ██║██║╚██████╔╝██║  ██║   ██║   ██║ ╚████║███████╗███████║███████║
╚═════╝ ╚═╝  ╚═╝╚═╝ ╚═════╝ ╚═╝  ╚═╝   ╚═╝   ╚═╝  ╚═══╝╚══════╝╚══════╝╚══════╝
```

The `dms brightness` command provides a unified interface for controlling brightness across different device types. It's a replacement for tools like `brightnessctl` and `ddcutil`, supporting backlight devices, LEDs, and DDC/I2C monitors.

## Overview[​](#overview "Direct link to Overview")

**Supported Device Types**:

- **Backlight devices**: Laptop screens, integrated displays (e.g., `amdgpu_bl1`, `intel_backlight`, `nvidia_0`)
- **LED devices**: Keyboard backlights, indicator LEDs (e.g., `asus::kbd_backlight`, `phy0-led`)
- **DDC/I2C monitors**: External monitors via DDC/CI protocol (requires `--ddc` flag)

**Key Features**:

- List all brightness devices with current values
- Get and set brightness for specific devices
- Support for exponential brightness scaling for more natural perception
- Fast operation for backlight/LED devices
- Optional DDC/I2C support for external monitors

## Quick Start[​](#quick-start "Direct link to Quick Start")

List all available brightness devices:

**Example output**:

```
Device                      Class         Name                   Brightness
────────────────────────────────────────────────────────────────────────────────
leds:phy0-led               leds          phy0-led               100%
backlight:amdgpu_bl1        backlight     amdgpu_bl1              43%
backlight:nvidia_0          backlight     nvidia_0               100%
leds:asus::kbd_backlight    leds          asus::kbd_backlight      0%
```

Set brightness for a specific device:

```
# Set laptop backlight to 50%
dms brightness set backlight:amdgpu_bl1 50

# Set keyboard backlight to 25%
dms brightness set leds:asus::kbd_backlight 25
```

Get current brightness for a device:

```
dms brightness get backlight:amdgpu_bl1
```

## Device Identification[​](#device-identification "Direct link to Device Identification")

Devices are identified using the format `<class>:<name>`:

- **Class**: The device class (`backlight`, `leds`, or `ddc`)
- **Name**: The device name as shown in the list output

**Examples**:

- `backlight:amdgpu_bl1` - AMD GPU backlight
- `backlight:intel_backlight` - Intel integrated graphics backlight
- `backlight:nvidia_0` - NVIDIA GPU backlight
- `leds:asus::kbd_backlight` - ASUS keyboard backlight
- `leds:phy0-led` - WiFi/network activity LED

## Commands[​](#commands "Direct link to Commands")

### `dms brightness list`[​](#dms-brightness-list "Direct link to dms-brightness-list")

List all available brightness devices with their current brightness values.

```
dms brightness list [flags]
```

**Flags**:

- `--ddc`: Include DDC/I2C monitors (slower, requires additional scanning)
- `-h, --help`: Show help

**Examples**:

```
# List backlight and LED devices (fast)
dms brightness list

# Include external DDC/I2C monitors (slower)
dms brightness list --ddc
```

**Note**: The `--ddc` flag causes the command to scan for external monitors via DDC/I2C, which takes longer than listing backlight/LED devices.

### `dms brightness get`[​](#dms-brightness-get "Direct link to dms-brightness-get")

Get the current brightness percentage for a specific device.

```
dms brightness get <device_id>[flags]
```

**Arguments**:

- `device_id` (required): Device identifier (e.g., `backlight:amdgpu_bl1`)

**Flags**:

- `--ddc`: Enable DDC/I2C device support
- `-h, --help`: Show help

**Examples**:

```
# Get laptop backlight brightness
dms brightness get backlight:amdgpu_bl1

# Get external monitor brightness
dms brightness get ddc:monitor-name --ddc
```

### `dms brightness set`[​](#dms-brightness-set "Direct link to dms-brightness-set")

Set the brightness percentage (0-100) for a specific device.

```
dms brightness set<device_id><percent>[flags]
```

**Arguments**:

- `device_id` (required): Device identifier
- `percent` (required): Brightness percentage (0-100)

**Flags**:

- `--ddc`: Enable DDC/I2C device support
- `--exponential`: Use exponential brightness scaling
- `--exponent <value>`: Exponent for exponential scaling (default: 1.2)
- `-h, --help`: Show help

**Examples**:

```
# Set brightness to 50%
dms brightness set backlight:amdgpu_bl1 50

# Set brightness with exponential scaling
dms brightness set backlight:amdgpu_bl1 50--exponential

# Set brightness with custom exponent
dms brightness set backlight:amdgpu_bl1 50--exponential--exponent1.5

# Set external monitor brightness
dms brightness set ddc:monitor-name 75--ddc
```

## Exponential Brightness Scaling[​](#exponential-brightness-scaling "Direct link to Exponential Brightness Scaling")

Human perception of brightness is non-linear. A 50% brightness value may appear much brighter than expected. Exponential scaling makes brightness changes feel more natural.

**How it works**:

- Applies an exponential curve to the brightness value before setting it
- Default exponent: 1.2
- Higher exponents create more aggressive curves (darker at mid-range)
- Lower exponents create gentler curves

**Example**:

```
# Without exponential scaling: 50% may feel like 70%
dms brightness set backlight:amdgpu_bl1 50

# With exponential scaling: 50% feels more like 50%
dms brightness set backlight:amdgpu_bl1 50--exponential

# More aggressive curve
dms brightness set backlight:amdgpu_bl1 50--exponential--exponent1.5
```

**Tip**: Try exponential scaling if you find yourself rarely using the lower half of your brightness range.

## DDC/I2C Monitor Support[​](#ddci2c-monitor-support "Direct link to DDC/I2C Monitor Support")

External monitors can be controlled via the DDC/CI protocol over I2C. This requires the `--ddc` flag and may be slower than backlight/LED control.

**Requirements**:

- Monitor must support DDC/CI
- I2C permissions (typically handled by udev rules or user groups)

**Usage**:

```
# List all devices including DDC/I2C monitors
dms brightness list --ddc

# Get external monitor brightness
dms brightness get ddc:monitor-name --ddc

# Set external monitor brightness
dms brightness set ddc:monitor-name 60--ddc
```

**Note**: DDC operations are slower than backlight operations due to the I2C communication protocol. Expect a slight delay when setting brightness on external monitors.

## Integration with DMS[​](#integration-with-dms "Direct link to Integration with DMS")

DMS integrates with the shell over IPC via a Unix socket. To show brightness OSDs and use shell-integrated brightness controls, use `dms ipc` commands instead of the direct CLI commands.

The `dms ipc call brightness` target provides additional functionality:

- On-screen display (OSD) when brightness changes
- Increment/decrement brightness by steps
- Per-device exponential mode toggling
- Status queries

See the [Keybinds & IPC](https://danklinux.com/docs/dankmaterialshell/keybinds-ipc#brightness) documentation for complete details on the brightness IPC target.

**Example keybind integration**:

```
# Hyprland example - shows OSD overlay
bind = , XF86MonBrightnessUp, exec, dms ipc call brightness increment 5
bind = , XF86MonBrightnessDown, exec, dms ipc call brightness decrement 5
bind = , XF86MonBrightnessDown+Shift, exec, dms ipc call brightness toggleExponential
```

### vs brightnessctl[​](#vs-brightnessctl "Direct link to vs brightnessctl")

- **Same functionality** for backlight and LED devices
- **Simpler device identification** (class:name format)
- **Exponential scaling** built-in
- **DDC/I2C support** in the same tool

### vs ddcutil[​](#vs-ddcutil "Direct link to vs ddcutil")

- **Same functionality** for DDC/I2C monitors
- **Faster** for simple brightness operations
- **Unified interface** with backlight devices

## Troubleshooting[​](#troubleshooting "Direct link to Troubleshooting")

### Permission Denied[​](#permission-denied "Direct link to Permission Denied")

If you get permission errors:

1. Check if your user is in the `video` or `input` group:
2. Add yourself to the appropriate group:
   
   ```
   sudousermod-a-G video $USER
   sudousermod-a-G input $USER
   ```
3. Log out and log back in for changes to take effect

### Device Not Found[​](#device-not-found "Direct link to Device Not Found")

If a device isn't listed:

- For backlights: Check `/sys/class/backlight/`
- For LEDs: Check `/sys/class/leds/`
- For DDC: Make sure to use the `--ddc` flag and verify monitor supports DDC/CI

### DDC/I2C Not Working[​](#ddci2c-not-working "Direct link to DDC/I2C Not Working")

If external monitors don't respond:

1. Verify DDC/CI is enabled in your monitor's OSD settings
2. Check I2C kernel module is loaded:
3. Test with `i2cdetect`:

## Command Reference[​](#command-reference "Direct link to Command Reference")

```
dms brightness [command][flags]
```

**Available Commands**:

- `list`: List all brightness devices
- `get <device_id>`: Get brightness for a device
- `set <device_id> <percent>`: Set brightness for a device

**Global Flags**:

- `-c, --config <path>`: Specify custom DMS config directory
- `-h, --help`: Show help

**Command-Specific Flags**:

- `--ddc`: Include DDC/I2C monitors (available on all commands)
- `--exponential`: Use exponential scaling (set command only)
- `--exponent <value>`: Custom exponent value (set command only, default: 1.2)