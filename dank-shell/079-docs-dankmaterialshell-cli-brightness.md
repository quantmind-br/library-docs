---
title: Brightness Control | Dank Linux
url: https://danklinux.com/docs/dankmaterialshell/cli-brightness
source: sitemap
fetched_at: 2026-04-26T08:38:37.536265016-03:00
rendered_js: false
word_count: 714
summary: This document provides a reference for the dms brightness command, a unified tool used to manage screen backlight, LED indicators, and external DDC/I2C monitors.
tags:
    - dms
    - brightness
    - backlight
    - ddc-ci
    - led-control
    - cli-reference
    - hardware-management
category: reference
optimized: true
optimized_at: 2026-04-26T00:00:00Z
---

`dms brightness` provides a unified interface for controlling brightness across backlight devices, LEDs, and DDC/I2C monitors — replacing `brightnessctl` and `ddcutil`.

## Supported Devices

- **Backlight**: Laptop screens, integrated displays (`amdgpu_bl1`, `intel_backlight`, `nvidia_0`)
- **LEDs**: Keyboard backlights, indicator LEDs (`asus::kbd_backlight`, `phy0-led`)
- **DDC/I2C**: External monitors via DDC/CI protocol (requires `--ddc` flag)

## Quick Start

```bash
# List all devices
dms brightness list
# Set laptop backlight to 50%
dms brightness set backlight:amdgpu_bl1 50
# Set keyboard backlight to 25%
dms brightness set leds:asus::kbd_backlight 25
# Get current brightness
dms brightness get backlight:amdgpu_bl1
```

**Example output:**

```text
Device                      Class         Name                   Brightness
────────────────────────────────────────────────────────────────────────────────
leds:phy0-led               leds          phy0-led               100%
backlight:amdgpu_bl1        backlight     amdgpu_bl1              43%
backlight:nvidia_0          backlight     nvidia_0               100%
leds:asus::kbd_backlight    leds          asus::kbd_backlight      0%
```

## Device Identification

Devices use `<class>:<name>` format:

| Class     | Example                          |
|-----------|----------------------------------|
| backlight | `backlight:amdgpu_bl1`           |
| backlight | `backlight:intel_backlight`      |
| backlight | `backlight:nvidia_0`             |
| leds      | `leds:asus::kbd_backlight`       |
| leds      | `leds:phy0-led`                  |

## Commands

### `dms brightness list [flags]`

List all brightness devices.

| Flag   | Description                          |
|--------|--------------------------------------|
| `--ddc` | Include DDC/I2C monitors (slower)   |
| `-h`   | Show help                            |

```bash
dms brightness list
dms brightness list --ddc
```

### `dms brightness get <device_id> [flags]`

Get current brightness percentage.

| Flag   | Description               |
|--------|---------------------------|
| `--ddc` | Enable DDC/I2C support    |
| `-h`   | Show help                 |

```bash
dms brightness get backlight:amdgpu_bl1
dms brightness get ddc:monitor-name --ddc
```

### `dms brightness set <device_id> <percent> [flags]`

Set brightness (0–100).

| Flag           | Description                        |
|----------------|------------------------------------|
| `--ddc`        | Enable DDC/I2C support             |
| `--exponential` | Use exponential brightness scaling |
| `--exponent N` | Exponent for scaling (default: 1.2) |
| `-h`           | Show help                          |

```bash
dms brightness set backlight:amdgpu_bl1 50
dms brightness set backlight:amdgpu_bl1 50 --exponential
dms brightness set backlight:amdgpu_bl1 50 --exponential --exponent 1.5
dms brightness set ddc:monitor-name 75 --ddc
```

## Exponential Brightness Scaling

Human perception of brightness is non-linear. Exponential scaling makes changes feel more natural.

- Default exponent: 1.2
- Higher exponents = darker at mid-range
- Lower exponents = gentler curve

```bash
# Without exponential: 50% may feel like 70%
dms brightness set backlight:amdgpu_bl1 50
# With exponential: 50% feels more natural
dms brightness set backlight:amdgpu_bl1 50 --exponential
# More aggressive curve
dms brightness set backlight:amdgpu_bl1 50 --exponential --exponent 1.5
```

> [!tip]
> Try exponential scaling if you rarely use the lower half of your brightness range.

## DDC/I2C Monitor Support

External monitors via DDC/CI over I2C (requires `--ddc`).

**Requirements:**
- Monitor must support DDC/CI
- I2C permissions (udev rules or user groups)

```bash
dms brightness list --ddc
dms brightness get ddc:monitor-name --ddc
dms brightness set ddc:monitor-name 60 --ddc
```

> [!warning]
> DDC operations are slower than backlight/LED control due to I2C communication.

## DMS IPC Integration

For shell-integrated OSD and brightness controls, use `dms ipc call brightness` instead of direct CLI commands. This enables:

- On-screen display on brightness changes
- Increment/decrement by steps
- Per-device exponential mode toggling
- Status queries

See [[084-docs-dankmaterialshell-keybinds-ipc#brightness]] for IPC target details.

**Hyprland keybind example:**

```conf
bind = , XF86MonBrightnessUp,   exec, dms ipc call brightness increment 5
bind = , XF86MonBrightnessDown, exec, dms ipc call brightness decrement 5
bind = , XF86MonBrightnessDown+Shift, exec, dms ipc call brightness toggleExponential
```

## Troubleshooting

### Permission Denied

1. Check if your user is in the `video` or `input` group
2. Add yourself:

   ```bash
   sudo usermod -aG video $USER
   sudo usermod -aG input $USER
   ```

3. Log out and log back in

### Device Not Found

- Backlights: check `/sys/class/backlight/`
- LEDs: check `/sys/class/leds/`
- DDC: ensure `--ddc` flag and monitor supports DDC/CI

### DDC/I2C Not Working

1. Verify DDC/CI is enabled in monitor OSD settings
2. Check I2C kernel module is loaded
3. Test with `i2cdetect`

## Command Reference

```bash
dms brightness [command] [flags]
```

| Command                | Description                  |
|------------------------|------------------------------|
| `list`                 | List all brightness devices   |
| `get <device_id>`      | Get brightness for a device  |
| `set <device_id> <pct>`| Set brightness (0–100)        |

| Global Flag              | Description                    |
|--------------------------|--------------------------------|
| `-c, --config <path>`    | Custom DMS config directory    |
| `-h, --help`             | Show help                      |
| `--ddc`                  | Include DDC/I2C monitors       |
| `--exponential`           | Use exponential scaling (set)  |
| `--exponent <value>`     | Custom exponent (set, default 1.2) |
